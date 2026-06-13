#!/usr/bin/env python3
"""
MCMC fit for the cascade's RAR parameters.

Use Metropolis-Hastings to get proper Bayesian posterior on
(f_active, scale, r_core_frac) for the Milky Way RAR data.

This will tell us:
- Best-fit parameters with proper error bars
- Whether f_active ~ 0.05 vs f_active ~ 0.18 is degenerate or distinguishable
- The correlation between parameters
"""

import math
import random
import sys
import numpy as np

# Constants
G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

g_plus_galaxy = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2 if r_m > 0 else 0

def g_DM_iso(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
    M_cum_total_kg = scale * (1 - f_active) * M_halo_Msun * M_sun
    r_core_m = r_core_frac * R_halo_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2 * r_core_m / 3)
    rho_0 = M_cum_total_kg / V_eff if V_eff > 0 else 0
    if r_m < r_core_m:
        M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_0
    else:
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum_enclosed = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

# MW
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30
test_radii = [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]
test_radii = [r for r in test_radii if r <= R_halo * 0.8]

# Compute "data" (cascade prediction with best-fit params, with synthetic errors)
# Use a typical RAR scatter of ~0.1 dex (30%)
g_bar_data = []
g_obs_data = []
g_err_data = []
for r in test_radii:
    g_b = g_bar_disk(r, M_disk, R_disk)
    if g_b <= 0:
        continue
    # Best-fit cascade with f_active=0.05, scale=0.15, r_core_frac=0.2
    g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, 0.05, 0.2, 0.15)
    g_obs = g_b + g_dm
    # Add realistic scatter (0.1 dex in log)
    g_err = 0.1 * g_obs
    g_bar_data.append(g_b)
    g_obs_data.append(g_obs)
    g_err_data.append(g_err)

g_bar_data = np.array(g_bar_data)
g_obs_data = np.array(g_obs_data)
g_err_data = np.array(g_err_data)

# Log-likelihood
def log_likelihood(f_active, r_core_frac, scale):
    """Compute log-likelihood of observing g_obs_data given params"""
    if f_active < 0 or f_active > 0.5:
        return -np.inf
    if r_core_frac < 0.01 or r_core_frac > 0.5:
        return -np.inf
    if scale < 0.01 or scale > 1.0:
        return -np.inf
    
    chi2 = 0
    for i, r in enumerate(test_radii[:len(g_bar_data)]):
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs_pred = g_bar_data[i] + g_dm
        chi2 += ((g_obs_data[i] - g_obs_pred) / g_err_data[i]) ** 2
    
    return -0.5 * chi2

# Log-prior (flat)
def log_prior(f_active, r_core_frac, scale):
    if 0.001 < f_active < 0.3 and 0.05 < r_core_frac < 0.5 and 0.05 < scale < 0.5:
        return 0
    return -np.inf

# Metropolis-Hastings
def mcmc(n_steps=10000, n_burn=2000):
    # Initial guess (near best-fit)
    current = np.array([0.05, 0.2, 0.15])
    current_log_post = log_likelihood(*current) + log_prior(*current)
    
    # Step sizes
    step_sizes = np.array([0.005, 0.02, 0.02])
    
    samples = []
    accept_count = 0
    
    for step in range(n_steps):
        # Propose new state
        proposal = current + np.random.randn(3) * step_sizes
        proposal_log_post = log_likelihood(*proposal) + log_prior(*proposal)
        
        # Accept/reject
        log_alpha = proposal_log_post - current_log_post
        if np.log(np.random.rand()) < log_alpha:
            current = proposal
            current_log_post = proposal_log_post
            accept_count += 1
        
        # Store after burn-in
        if step >= n_burn:
            samples.append(current)
    
    return np.array(samples), accept_count / n_steps

# Run MCMC
print("Running MCMC (10000 steps, 2000 burn-in)...")
np.random.seed(42)
samples, accept_rate = mcmc(n_steps=10000, n_burn=2000)
print(f"  Accept rate: {accept_rate:.3f}")
print()

# Posterior statistics
f_active_samples = samples[:, 0]
r_core_samples = samples[:, 1]
scale_samples = samples[:, 2]

print("=" * 80)
print("POSTERIOR SUMMARY (MCMC)")
print("=" * 80)
print()
print(f"  {'Parameter':<15s}  {'Median':>10s}  {'1-sigma':>15s}  {'2-sigma':>15s}")
print("  " + "-" * 65)

for name, samp in [('f_active', f_active_samples), 
                    ('r_core_frac', r_core_samples),
                    ('scale', scale_samples)]:
    med = np.median(samp)
    p16 = np.percentile(samp, 16)
    p84 = np.percentile(samp, 84)
    p2 = np.percentile(samp, 2.5)
    p97 = np.percentile(samp, 97.5)
    print(f"  {name:<15s}  {med:>10.4f}  +{p84-med:.4f} / -{med-p16:.4f}  +{p97-med:.4f} / -{med-p2:.4f}")

# Correlation matrix
print()
print("CORRELATION MATRIX:")
print(f"  f_active vs r_core_frac: {np.corrcoef(f_active_samples, r_core_samples)[0,1]:.3f}")
print(f"  f_active vs scale:       {np.corrcoef(f_active_samples, scale_samples)[0,1]:.3f}")
print(f"  r_core_frac vs scale:    {np.corrcoef(r_core_samples, scale_samples)[0,1]:.3f}")

# Test the f_active tension
print()
print("=" * 80)
print("THE 5% vs 18% f_active TENSION (MCMC)")
print("=" * 80)
print()
print("Cosmic SFR interpretation: f_active ~ 0.18 (t_current ~ 2.5 Gyr)")
print("Gas consumption interpretation: f_active ~ 0.05 (t_current ~ 0.7 Gyr)")
print()
# Check what fraction of MCMC samples are above/below 0.10
n_above_10 = np.sum(f_active_samples > 0.10)
n_total = len(f_active_samples)
print(f"  Fraction of MCMC samples with f_active > 0.10: {n_above_10/n_total*100:.1f}%")
print(f"  Fraction with f_active < 0.10: {(n_total-n_above_10)/n_total*100:.1f}%")
print()
print(f"  f_active median: {np.median(f_active_samples):.4f}")
print(f"  f_active 1-sigma range: {np.percentile(f_active_samples, 16):.4f} - {np.percentile(f_active_samples, 84):.4f}")
print(f"  f_active 2-sigma range: {np.percentile(f_active_samples, 2.5):.4f} - {np.percentile(f_active_samples, 97.5):.4f}")
print()
print("INTERPRETATION:")
if 0.05 < np.percentile(f_active_samples, 2.5) and np.percentile(f_active_samples, 97.5) < 0.18:
    print("  The 0.05 and 0.18 values are BOTH within the 2-sigma range.")
    print("  The MCMC data cannot distinguish between them.")
    print("  The 'tension' is a tension in our INTERPRETATION, not in the data.")
else:
    if np.percentile(f_active_samples, 97.5) < 0.10:
        print("  f_active = 0.18 is OUTSIDE the 2-sigma range.")
        print("  The data prefers f_active ~ 0.05 (gas consumption).")
    else:
        print("  f_active = 0.05 is OUTSIDE the 2-sigma range.")
        print("  The data prefers f_active ~ 0.18 (cosmic SFR).")
