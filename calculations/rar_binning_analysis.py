#!/usr/bin/env python3
"""
Binning analysis: bin by g_bar (standard RAR approach) and check if
the cascade's binned g_obs matches the RAR's binned g_obs.
"""

import math
import numpy as np

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
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

def g_DM(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
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

# Generate galaxies
np.random.seed(42)
galaxies = []
M_halo_values = np.logspace(8, 13, 30)
for i, M_halo in enumerate(M_halo_values):
    kappa = 5 + (i % 10) * 10
    M_disk = M_halo / kappa
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa))

def collect_data(galaxies, f_active=0.05, r_core_frac=0.25, scale=0.15):
    """Get all (g_bar, g_obs_cascade, g_obs_RAR) data points"""
    data = []
    for name, M_disk, R_disk, M_halo, R_halo, kappa in galaxies:
        # 10 test radii per galaxy
        for r in [0.3*R_disk, 0.5*R_disk, 1*R_disk, 1.5*R_disk, 2*R_disk, 3*R_disk, 4*R_disk, 5*R_disk, 7*R_disk, 0.5*R_halo]:
            if r > R_halo * 0.9:
                continue
            g_b = g_bar_disk(r, M_disk, R_disk)
            if g_b <= 0:
                continue
            g_dm = g_DM(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
            g_obs = g_b + g_dm
            g_obs_rar = rar(g_b, g_plus_galaxy)
            if g_obs_rar > 0:
                data.append((g_b, g_obs, g_obs_rar))
    return data

data = collect_data(galaxies)
print(f"Total data points: {len(data)}")
print()

# Bin by g_bar (logarithmic bins)
g_bars = np.array([d[0] for d in data])
g_obs_cas = np.array([d[1] for d in data])
g_obs_rar = np.array([d[2] for d in data])

# Define log g_bar bins
log_gbar_min = math.log10(min(g_bars))
log_gbar_max = math.log10(max(g_bars))
print(f"g_bar range: {10**log_gbar_min:.3e} to {10**log_gbar_max:.3e}")
print()

n_bins = 8
bin_edges = np.logspace(log_gbar_min, log_gbar_max, n_bins + 1)
print("=" * 80)
print("BINNED ANALYSIS (cascade vs RAR by g_bar bin)")
print("=" * 80)
print()
print(f"  {'g_bar bin':>20s}  {'<g_bar>':>12s}  {'<g_cas>':>12s}  {'<g_RAR>':>12s}  {'diff':>8s}  {'% diff':>8s}")
print()

total_chi2 = 0
n_total = 0
for i in range(n_bins):
    in_bin = (g_bars >= bin_edges[i]) & (g_bars < bin_edges[i+1])
    if i == n_bins - 1:
        in_bin = (g_bars >= bin_edges[i]) & (g_bars <= bin_edges[i+1])
    n_in_bin = sum(in_bin)
    if n_in_bin == 0:
        continue
    mean_g_bar = np.mean(g_bars[in_bin])
    mean_g_cas = np.mean(g_obs_cas[in_bin])
    mean_g_rar = np.mean(g_obs_rar[in_bin])
    diff = mean_g_cas - mean_g_rar
    pct_diff = diff / mean_g_rar * 100
    print(f"  {bin_edges[i]:>10.2e}-{bin_edges[i+1]:.2e}  {mean_g_bar:>12.3e}  {mean_g_cas:>12.3e}  {mean_g_rar:>12.3e}  {diff:>8.2e}  {pct_diff:>+7.1f}%")

print()
print("=" * 80)
print("OVERALL FIT QUALITY (cascade vs RAR in binned data)")
print("=" * 80)
print()

# Compute overall RMS residual
rms_log_cas = np.sqrt(np.mean((np.log10(g_obs_cas) - np.log10(g_obs_rar))**2))
print(f"  RMS log residual: {rms_log_cas:.3f} dex")
print(f"  Equivalent: {10**rms_log_cas:.2f}x factor")
print()

# Per-bin chi^2 contribution
chi2_per_bin = []
for i in range(n_bins):
    in_bin = (g_bars >= bin_edges[i]) & (g_bars < bin_edges[i+1])
    if i == n_bins - 1:
        in_bin = (g_bars >= bin_edges[i]) & (g_bars <= bin_edges[i+1])
    if sum(in_bin) > 0:
        chi2 = np.sum((np.log10(g_obs_cas[in_bin]) - np.log10(g_obs_rar[in_bin]))**2)
        chi2_per_bin.append((bin_edges[i], bin_edges[i+1], chi2, sum(in_bin)))

print("  {'bin':>25s}  {'chi^2':>10s}  {'n':>5s}  {'chi^2/n':>10s}")
for low, high, chi2, n in chi2_per_bin:
    print(f"  {low:.2e} - {high:.2e}  {chi2:>10.3f}  {n:>5d}  {chi2/n:>10.3f}")
print()
total_chi2 = sum(c[2] for c in chi2_per_bin)
total_n = sum(c[3] for c in chi2_per_bin)
print(f"  Total: chi^2 = {total_chi2:.2f}, n = {total_n}, chi^2/n = {total_chi2/total_n:.3f}")
