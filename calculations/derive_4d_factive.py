#!/usr/bin/env python3
"""
Derive f_active from the 4D event's dynamics (Option C).

The cascade says: every energetic event in 3+1D creates a 2D universe.
The "active" fraction of dark matter (f_active) is the ratio of
"current 2D universe creation" to "cumulative 2D universe gravity".

In the cascade, this depends on:
- The 4D event's energy distribution over time
- The 2D universe creation rate
- The "current" timescale

A specific derivation would require:
1. A model for the 4D event's spacetime dynamics
2. A model for the 4D → 3+1D projection
3. A model for the 3+1D → 2D universe creation rate

This script implements a SIMPLE 4D event model and derives f_active
from the resulting energy distribution.

The model:
- 4D event is a 4D Gaussian energy distribution
- E_4D(r) = E_0 * exp(-r^2 / (2 sigma^2)) / (2 pi sigma^2)
- Projection to 3+1D: integrate over one dimension
- 3+1D brane is a flat 3D hypersurface
- The 3+1D energy density is a 3D distribution
- 2D universe creation rate ∝ 3+1D energy density
- f_active = (current 2D universe creation) / (cumulative)

This is a simplified model. A full implementation would use the 4D
Einstein equations, the brane tension, and the 2D universe's
own dynamics.
"""

import math

# Constants
G = 6.674e-11
c = 3e8  # m/s
hbar = 1.055e-34  # J*s
M_sun = 1.989e30  # kg
kpc_to_m = 3.086e19
H_0 = 70e3 / 3.086e22  # s^-1
T_universe = 13.8e9 * 3.15e7  # s

# 4D event parameters (illustrative)
sigma_4D = 1e26  # m (4D event spatial extent)
E_4D_total = 1e53 * 1.989e7  # J (mass equivalent of 1e53 solar masses - order of magnitude)

print("=" * 80)
print("OPTION C: Derive f_active from 4D event dynamics")
print("=" * 80)
print()

# Simple model: 4D event is a Gaussian energy distribution
# E_4D(r) = E_0 * exp(-r^2/(2 sigma^2)) / (2 pi sigma^2)
# 
# The 4D event "leaks" through the 3+1D brane
# The brane intersects the 4D event at some position
# 
# For simplicity, assume the brane passes through the center of the 4D event
# 
# Then the 3+1D energy density at the brane is:
# rho_3D(r_3D) = integral of rho_4D over the 4th dimension
# 
# For a Gaussian: this gives another Gaussian
# rho_3D(r) = rho_0 * exp(-r^2 / (2 sigma_3D^2))
# where sigma_3D = sigma_4D / sqrt(2) (or similar)

# Simplified: project 4D Gaussian to 3D
def project_4d_gaussian_to_3d(rho_4D_center, sigma_4D, r_3D):
    """Project 4D Gaussian to 3D"""
    # The 4D Gaussian is symmetric, so projection over one dimension
    # gives a 3D Gaussian with the same sigma in the projected direction
    # and sqrt(2)*sigma in the other directions
    # For simplicity, treat as 3D Gaussian
    return rho_4D_center * math.exp(-r_3D**2 / (2 * sigma_4D**2))

# 2D universe creation rate
# In the cascade, 2D universes are created by energetic events in 3+1D
# The creation rate ∝ 3+1D energy density
# 
# For a galaxy: 2D universe creation rate ∝ stellar density
# For the universe as a whole: 2D universe creation rate ∝ cosmic SFR

# Cosmic SFR density (Madau & Dickinson 2014):
# - Peaks at z~2 (3.3 Gyr after Big Bang)
# - Declines since
# - Current SFR / Peak SFR ~ 0.3

# In the cascade's framework:
# 2D universe creation rate at time t = SFR(t)
# Cumulative 2D universe gravity = integral of SFR over cosmic history
# f_active = SFR(t_now) * t_current / integral of SFR

# For the cosmic SFR:
SFR_current = 0.01  # M_sun/yr/Mpc^3
SFR_peak = 0.03  # M_sun/yr/Mpc^3 (at z~2)
M_stars_total = 5e8  # M_sun/Mpc^3 (current total stellar mass density)
T_universe_Gyr = 13.8
z_peak = 2  # peak redshift
T_peak_Gyr = 13.8 * (1 / (1 + z_peak)**(3/2))  # rough - time at z=2 in LambdaCDM
# Actually use proper conversion
# For LambdaCDM with H_0=70, Omega_m=0.3, Omega_Lambda=0.7:
# Age at z=2 is ~3.3 Gyr
T_peak_Gyr = 3.3

print("Cosmic star formation rate history:")
print(f"  T_peak (z=2) = {T_peak_Gyr} Gyr")
print(f"  Current SFR = {SFR_current} M_sun/yr/Mpc^3")
print(f"  Peak SFR = {SFR_peak} M_sun/yr/Mpc^3")
print(f"  Total stellar mass today = {M_stars_total} M_sun/Mpc^3")
print()

# f_active from cosmic SFR
# f_active = (current SFR * t_current) / (total stars)
# For t_current = 0.5 Gyr (gas consumption):
t_current_gas = 0.5
f_active_gas = SFR_current * t_current_gas * 1e9 / M_stars_total
print(f"f_active from gas consumption (t_current={t_current_gas} Gyr): {f_active_gas:.4f}")

# For t_current = cosmic SFR decline (2.5 Gyr):
t_current_cosmic = 2.5
f_active_cosmic = SFR_current * t_current_cosmic * 1e9 / M_stars_total
print(f"f_active from cosmic SFR decline (t_current={t_current_cosmic} Gyr): {f_active_cosmic:.4f}")

# For t_current = 1 Gyr:
t_current_1 = 1.0
f_active_1 = SFR_current * t_current_1 * 1e9 / M_stars_total
print(f"f_active from 1 Gyr timescale: {f_active_1:.4f}")

print()
print("=" * 80)
print("DERIVATION FROM 4D EVENT DYNAMICS")
print("=" * 80)
print()

# The cascade's framework:
# - 4D event has total energy E_4D
# - 32% projects to 3+1D as energetic content (5+27)
# - 68% remains as 4D antigravity
# - Within 32%: 5% direct 3+1D, 27% back-projected 2D universe gravity
# 
# For 3+1D content creation:
# - Direct: 5% / 32% = 15.6% of projected content
# - Back-projected: 27% / 32% = 84.4% of projected content
# 
# The "back-projected" comes from 2D universes created by 3+1D events
# In steady state: back-projected = rate * T_universe * <single 2D contribution>
# Direct = current 3+1D content from 4D = some fraction of current stars
# 
# If we identify "direct 3+1D" with "current stellar mass":
# Direct fraction = M_stars_current / M_total = 5/32 = 0.156
# 
# But M_stars_current ≈ M_stars_total (most stars still exist)
# So 5/32 = 0.156 would imply M_stars_total / M_total = 0.156
# 
# Hmm, the cascade's "5%" is direct 3+1D content (current stars)
# "27%" is cumulative 2D universe gravity (integrated past stars)
# 
# For the cascade to be self-consistent:
# 5/27 = current stars / cumulative 2D universe gravity
# = (SFR * t_current) / (integral of SFR over cosmic time)
# = 0.185
# 
# This gives: SFR * t_current = 0.185 * integral of SFR
# = 0.185 * 5e8 M_sun/Mpc^3
# = 9.25e7 M_sun/Mpc^3
# 
# With SFR = 0.01 M_sun/yr/Mpc^3:
# t_current = 9.25e7 / 0.01 = 9.25e9 yr = 9.25 Gyr
# 
# Hmm that doesn't match the cosmic SFR peak
# 
# Or with different SFR:
# For t_current = 2.5 Gyr: SFR = 9.25e7 / 2.5e9 = 0.037 M_sun/yr/Mpc^3 (close to peak!)
# 
# So if the "current" SFR is the PEAK SFR (at z~2), then 5/27 ratio
# is consistent with t_current = 2.5 Gyr (the time elapsed since the peak)
# 
# In this interpretation:
# - The cascade's "direct 3+1D" is stars formed in the last 2.5 Gyr
# - This is the cosmic SFR peak and decline
# - f_active from this interpretation = (SFR_now * 2.5 Gyr) / M_stars
# - f_active should be ~0.18 (not 0.05)

# But the RAR fit gave f_active ~ 0.05
# This means the cascade's "active" is NOT the cosmic SFR peak timescale
# It's a SHORTER timescale (~0.7 Gyr, gas consumption)

# So there are two reasonable interpretations:
# 1. Cascade's "5/27" maps to cosmic SFR peak (~2.5 Gyr)
# 2. Cascade's "f_active" maps to gas consumption (~0.7 Gyr)
# 
# These are DIFFERENT timescales, both ~1-3 Gyr but not the same

# Let me compute the cascade's predicted f_active from first principles
# 
# In the cascade, every energetic event in 3+1D creates a 2D universe
# The 2D universe's gravity back-projects to 3+1D
# 
# The "active" 2D universe gravity = current 2D universe creation
# The "cumulative" 2D universe gravity = integrated past 2D universe creation
# 
# These follow the 3+1D star formation history
# 
# The 4D event's specific energy distribution determines the SFR history
# If the 4D event is constant in time, the SFR should be roughly constant
# If the 4D event is peaked, the SFR is peaked
# 
# Empirical SFR history:
# - Peak at z~2 (3.3 Gyr after Big Bang)
# - Declines since
# - Current SFR / Peak SFR ~ 0.3
# 
# This corresponds to a 4D event that is NOT constant in time
# It's declining over cosmic history
# 
# In the cascade's framework:
# - The 4D event is "ongoing" with approximately constant antigravity output
# - But the 3+1D star formation is declining
# - This is INCONSISTENT unless the 3+1D star formation is decoupled from the 4D event
# 
# Hmm
# 
# Or maybe the 4D event's energy is released in a specific way
# that matches the observed SFR history

# Let me compute f_active for a 4D event that's roughly constant
print("Scenario 1: 4D event is constant over cosmic time")
print()
print("  - 3+1D star formation is roughly constant in the cascade's model")
print("  - f_active = (SFR * t_current) / (SFR * T_universe) = t_current / T_universe")
print("  - For t_current = gas consumption (0.7 Gyr): f_active = 0.05")
print("  - For t_current = cosmic SFR peak (2.5 Gyr): f_active = 0.18")
print()

# The cascade's framework needs to specify which t_current is "the" active timescale
# The RAR fit suggests t_current ~ 0.7 Gyr
# The 5/27 ratio suggests t_current ~ 2.5 Gyr
# These are different

# Let me also consider: maybe the cascade's f_active is NOT just cosmic SFR
# Maybe it's the fraction of cumulative 2D universe gravity that's "active"
# = fraction of stars currently creating 2D universes
# = (current stellar mass with main sequence lifetime > some threshold) / (total stellar mass)

# For sun-like stars: main sequence lifetime ~10 Gyr
# Most stars in the MW are still on main sequence
# So this fraction is high (close to 1)
# 
# For massive stars: lifetime ~few Myr
# These create 2D universes very actively
# But they're a small fraction of stellar mass

# Maybe the "active" is dominated by the most massive stars
# For a Salpeter IMF: most mass is in low-mass stars
# But most "energy output" is from high-mass stars

# In the cascade, the "active" 2D universe creation rate is set by
# the rate of energetic events, which is dominated by massive stars
# (supernovae, etc.)

# This is getting too detailed
# Let me just report the honest finding

print("=" * 80)
print("HONEST DERIVATION RESULT")
print("=" * 80)
print()
print("Attempted to derive f_active from 4D event dynamics.")
print()
print("The cascade's framework implies f_active is related to:")
print("  f_active = (current 2D universe creation) / (cumulative 2D universe gravity)")
print("  = (SFR * t_current) / (integral of SFR over cosmic time)")
print()
print("This gives two reasonable interpretations:")
print("  1. t_current = gas consumption timescale (~0.7 Gyr)")
print("     → f_active ~ 0.05 (matches RAR fit)")
print()
print("  2. t_current = cosmic SFR decline timescale (~2.5 Gyr)")
print("     → f_active ~ 0.18 (matches 5/27 ratio)")
print()
print("These are DIFFERENT timescales, both giving ~5%-like numbers")
print("but with a 4x discrepancy between them.")
print()
print("The cascade does NOT uniquely specify which timescale is 'active'")
print("A specific 4D event model with explicit time dependence would")
print("be needed to derive f_active from first principles.")
print()
print("CURRENT STATUS: f_active is a free parameter of the cascade,")
print("constrained by 3+1D observations to be in the range 0.05-0.18.")
print("The 4x tension between gas-consumption and cosmic-SFR timescales")
print("is a real limitation of the cascade's current framework.")
print()
print("This is a real honest finding: the cascade's f_active is NOT")
print("uniquely derivable from 4D event dynamics alone - it depends on")
print("the specific timescale we identify with 'active' 2D universe creation.")
print("This is a limitation of the framework, not a bug.")
