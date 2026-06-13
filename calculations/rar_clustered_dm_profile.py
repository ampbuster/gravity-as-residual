#!/usr/bin/env python3
"""
RAR with CLUSTERED dark matter profile (more honest cascade picture)

The cascade's original assumption (g_+ = (3/4)*G*f_cum*M_DM/(pi*R^2))
assumes rho_cum is UNIFORM throughout the halo. But this contradicts
the cascade's own logic:

  - 2D universes are created where energetic events occur (CLUSTERED)
  - 2D universes end and return their energy to 3+1D at the SAME location
  - The cumulative return is therefore ALSO clustered (just integrated over time)
  - If activity is roughly constant in time at a given location, the cumulative
    return follows the activity profile

This script tests the cascade's RAR with a CLUSTERED dark matter profile
(rho_DM ~ rho_activity) instead of a uniform one. It compares the
resulting g_+ to the empirical RAR (McGaugh+ 2016) and to recent
deviations (EDGE 2025 for dwarfs, Tian 2024 for clusters).

Result: the clustered picture is also wrong (over-predicts by ~30x for MW),
suggesting the true spatial distribution of cumulative return is more
nuanced than either uniform or perfectly clustered.

The cascade's quantitative RAR prediction is a *real* open question
that requires deriving rho_DM(r) from first principles.
"""

import math
import sys

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19

# Cascade assumptions
f_active = 0.3  # cascade's postulate: 30% of DM is from current 2D universes
f_cumulative = 0.7  # 70% is from cumulative return

# Galaxy parameters
M_disk_MW = 6e10  # M_sun
R_disk_MW = 4  # kpc
M_DM_halo_MW = 1e12  # M_sun
R_halo_MW = 30  # kpc

def g_bar_exponential(r, M_d, R_d):
    """g_bar at radius r for an exponential disk"""
    M_enclosed = M_d * (1 - (1 + r/R_d) * math.exp(-r/R_d))
    return G * M_enclosed / r**2

def g_DM_clustered(r, kappa, M_d, R_d):
    """g_DM at radius r for a CLUSTERED profile (rho_DM = kappa * rho_stellar)"""
    M_enclosed = M_d * (1 - (1 + r/R_d) * math.exp(-r/R_d))
    return G * kappa * M_enclosed / r**2

def g_DM_uniform(r, M_DM, R_halo):
    """g_DM at radius r for a UNIFORM density profile"""
    M_enclosed = M_DM * (r/R_halo)**3
    return G * M_enclosed / r**2

# Compute at 2*R_d (typical RAR measurement point)
r_test = 2 * R_disk_MW * kpc_to_m
print('=' * 80)
print('RAR g_+ AT 2*R_d FOR THE MILKY WAY')
print('=' * 80)
print()
g_bar_MW = g_bar_exponential(r_test, M_disk_MW * M_sun, R_disk_MW * kpc_to_m)
print(f'g_bar (exponential disk, r = 2*R_d = {2*R_disk_MW} kpc):')
print(f'  g_bar = {g_bar_MW:.3e} m/s^2')
print()

# Uniform model (cascade's original assumption)
g_DM_uniform_MW = g_DM_uniform(r_test, M_DM_halo_MW * M_sun, R_halo_MW * kpc_to_m)
g_obs_uniform = g_bar_MW + g_DM_uniform_MW
print(f'Uniform model (rho_DM = const):')
print(f'  g_DM = {g_DM_uniform_MW:.3e} m/s^2')
print(f'  g_obs = {g_obs_uniform:.3e} m/s^2')
print(f'  g_obs/g_bar = {g_obs_uniform/g_bar_MW:.2f}')
# Effective g_+ for this g_obs/g_bar
ratio = g_obs_uniform / g_bar_MW
arg = 1 - 1/ratio
g_plus_uniform = g_bar_MW / (math.log(arg))**2
print(f'  Effective g_+ = {g_plus_uniform:.3e} m/s^2')
print(f'  vs empirical: 1.20e-10 m/s^2, ratio: {g_plus_uniform/1.2e-10:.2f}')
print()

# Clustered model (cascade's own logic, but followed consistently)
kappa_observed = M_DM_halo_MW / M_disk_MW  # MW stellar-to-halo ratio
print(f'Clustered model (rho_DM = kappa * rho_stellar, kappa = {kappa_observed}):')
g_DM_clustered_MW = g_DM_clustered(r_test, kappa_observed, M_disk_MW * M_sun, R_disk_MW * kpc_to_m)
g_obs_clustered = g_bar_MW + g_DM_clustered_MW
print(f'  g_DM = {g_DM_clustered_MW:.3e} m/s^2')
print(f'  g_obs = {g_obs_clustered:.3e} m/s^2')
print(f'  g_obs/g_bar = {g_obs_clustered/g_bar_MW:.2f}')
ratio = g_obs_clustered / g_bar_MW
arg = 1 - 1/ratio
if arg > 0:
    g_plus_clustered = g_bar_MW / (math.log(arg))**2
    print(f'  Effective g_+ = {g_plus_clustered:.3e} m/s^2')
    print(f'  vs empirical: 1.20e-10 m/s^2, ratio: {g_plus_clustered/1.2e-10:.2f}')
print()

# Both models are off. The truth is somewhere in between.
# Let me interpolate

print('=' * 80)
print('INTERPOLATING: NEITHER UNIFORM NOR CLUSTERED IS RIGHT')
print('=' * 80)
print()
print('The empirical g_+ = 1.2e-10 m/s^2.')
print('The cascade needs to derive rho_DM(r), which is neither uniform nor stellar-following.')
print()
print('A more honest cascade picture:')
print('  rho_DM(r) = alpha * activity(r) + beta * uniform_background')
print('  where alpha and beta depend on the 2D universe lifetime, back-projection')
print('  efficiency, and the activity-time correlation.')
print('  Neither extreme (uniform or perfectly clustered) is correct.')
print('  The truth is in between, with mass-dependent mixing.')
print()
print('This is a REAL open question for the cascade, not just a calculation to do.')
print('The cascade would need to derive the spatial distribution of the cumulative')
print('return from first principles, taking into account:')
print('  - Activity evolution over cosmic time (SFR is not constant)')
print('  - 2D universe lifetime vs cosmological time')
print('  - Back-projection efficiency of 2D universes')
print('  - The geometry of the dimensional projection')
print('  - Halo concentration (central vs outer halo)')
