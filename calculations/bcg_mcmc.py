#!/usr/bin/env python3
"""
MCMC fit of MOND g_+ on Tian+ 2024 cluster data.
"""

import math
import numpy as np
import json

def mond(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

# Load data
with open('/workspace/github-repo/supporting/data/Tian/tian_bcgs.json', 'r') as f:
    bcgs = json.load(f)

g_bars = np.array([10**b['log_gbar'] for b in bcgs])
g_obss = np.array([10**b['log_gobs'] for b in bcgs])
M_bars = np.array([10**b['log_Mbar'] for b in bcgs])

# Simple MCMC
def log_likelihood(log_g_plus):
    g_plus = 10**log_g_plus
    preds = np.array([mond(g_b, g_plus) for g_b in g_bars])
    with np.errstate(divide='ignore', invalid='ignore'):
        log_resid = np.log10(preds / g_obss)
    log_resid = log_resid[np.isfinite(log_resid)]
    if len(log_resid) == 0:
        return -np.inf
    return -0.5 * np.sum(log_resid**2)

def log_prior(log_g_plus):
    # Uniform prior in log g_+ from -11 to -7
    if -11 < log_g_plus < -7:
        return 0
    return -np.inf

def log_posterior(log_g_plus):
    return log_prior(log_g_plus) + log_likelihood(log_g_plus)

# Metropolis-Hastings
np.random.seed(42)
n_steps = 10000
current = -9.0  # log g_+ ~ 1e-9
samples = [current]
accept = 0
for i in range(n_steps):
    proposal = current + np.random.normal(0, 0.1)
    if np.log(np.random.uniform()) < log_posterior(proposal) - log_posterior(current):
        current = proposal
        accept += 1
    samples.append(current)

samples = np.array(samples[1000:])  # discard burn-in
acceptance_rate = accept / n_steps

print("=" * 80)
print("MCMC FIT OF g_+ ON TIAN+ 2024 BCG DATA")
print("=" * 80)
print()
print(f"  Acceptance rate: {acceptance_rate:.1%}")
print()
print(f"  log10(g_+) posterior:")
print(f"    mean: {np.mean(samples):+.3f}")
print(f"    std: {np.std(samples):.3f}")
print(f"    median: {np.median(samples):+.3f}")
print(f"    16th-84th percentile: {np.percentile(samples, 16):+.3f} to {np.percentile(samples, 84):+.3f}")
print()
print(f"  Physical g_+:")
print(f"    median: {10**np.median(samples):.2e} m/s^2")
print(f"    1-sigma range: {10**np.percentile(samples, 16):.2e} to {10**np.percentile(samples, 84):.2e}")
print()
print(f"  Tian+ 2024 measured: 1.7e-9 m/s^2")
print()

# Compare to galaxy g_+ (from SPARC)
galaxy_g_plus = 1.0e-10
ratio = 10**np.median(samples) / galaxy_g_plus
print(f"  Ratio cluster/galaxy g_+: {ratio:.1f}")
print(f"  Tian+ 2024 claimed ratio: 17")
print()

# Save
results = {
    'bcg_data': {
        'n': len(bcgs),
        'median_g_plus': float(10**np.median(samples)),
        'log_g_plus_median': float(np.median(samples)),
        'log_g_plus_std': float(np.std(samples)),
        'log_g_plus_16pct': float(np.percentile(samples, 16)),
        'log_g_plus_84pct': float(np.percentile(samples, 84)),
    },
    'tian_2024_g_plus': 1.7e-9,
    'sparc_galaxy_g_plus': 1.0e-10,
    'ratio_cluster_galaxy': float(ratio),
}
with open('/workspace/github-repo/supporting/data/Tian/bcg_mcmc_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Saved")
