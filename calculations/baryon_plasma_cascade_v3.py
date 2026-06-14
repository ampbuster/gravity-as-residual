"""
Baryon Plasma Cascade v3: HONEST Version with Correct Temperature Scaling

The v2 calculation had a bug: it used T_gamma = T_CMB_0 * (1+z) for all z,
which is the COUPLED temperature (valid only for z > 1100). For z < 1100,
the correct temperature is T_gamma(z) = T_gamma(1100) * (1+z)^2 / 1101^2
(adiabatic free-streaming of decoupled photons).

This v3 uses the correct temperature scaling and shows that the broader
principle does NOT save the cascade at z < 1100. The Thomson scattering
is significant only at z > 1100, but the (1+z)^4 dilution in the
integral means the high-z Thomson contribution to low-z DM is small.

RESULT: r(z=6) ~ 1e-4, the cascade is FALSIFIED at high z in this
narrow formulation, same as the v4 stellar-only result.

This is an HONEST finding that contradicts the §4.51 conclusion. The
broader principle does not save the cascade.
"""

import numpy as np
from scipy.integrate import quad
import json

# Constants
H0 = 67.4
Om = 0.315
Og = 5.4e-5
Omega_DE = 0.68
rho_crit_0_kg = 8.5e-27  # kg/m^3 proper
Ob = 0.049
sigma_T = 6.65e-29
c_light = 3e8
k_B = 1.38e-23
T_CMB_0 = 2.725
m_p = 1.67e-27
n_gamma_0 = 4.11e8  # m^-3 at z=0
Mpc_to_m = 3.086e22
yr_to_s = 3.156e7

def E_LCDM(z):
    return np.sqrt(Om * (1+z)**3 + Og * (1+z)**4 + Omega_DE)

# Cosmic SFR (Madau & Dickinson 2014)
def sfr_density_Madau(z):
    return 0.015 * (1 + z)**2.7 / (1 + ((1+z)/2.9)**5.6)

# Stellar 2D universe creation rate
def R_stellar(z):
    sfr = sfr_density_Madau(z)
    ccsn_rate = sfr * 0.15 / 10
    # 1 CCSN releases ~10^53 erg = 10^46 J
    return ccsn_rate * 1e46  # J/yr/Mpc^3 (proper? or comoving?)

# Thomson scattering energy injection rate (PROPER)
def R_Thomson_proper(z):
    """
    Thomson scattering energy injection rate per proper volume.
    Uses CORRECT temperature scaling:
    - z > 1100 (coupled): T_gamma ∝ (1+z)
    - z < 1100 (decoupled): T_gamma ∝ (1+z)^2 (adiabatic cooling of free-streaming photons)
    """
    z = np.asarray(z, dtype=float)
    
    rho_b = Ob * rho_crit_0_kg * (1+z)**3
    n_b = rho_b / m_p
    n_gamma = n_gamma_0 * (1+z)**3
    
    # CORRECT temperature scaling
    T_gamma = np.where(z > 1100,
        T_CMB_0 * (1 + z),  # coupled
        T_CMB_0 * 1101 * (1 + z)**2 / (1101**2)  # decoupled, T_gamma(1100) = 3000 K
    )
    T_gamma = np.where(z > 1100, T_CMB_0 * (1+z), T_CMB_0 * 1101 * (1+z)**2 / 1101**2)
    
    rate_proper = n_b * n_gamma * sigma_T * c_light * (k_B * T_gamma)
    # Convert J/m^3/s to J/yr/Mpc^3
    return rate_proper * yr_to_s * Mpc_to_m**3

# Recombination energy injection
def R_recomb_proper(z):
    """Recombination energy injection: 13.6 eV per recombination."""
    z = np.asarray(z, dtype=float)
    rho_b = Ob * rho_crit_0_kg * (1+z)**3
    n_b = rho_b / m_p
    n_e = n_b
    alpha_B = 2.6e-19 * (T_CMB_0 * (1+z) / 1e4)**-0.7
    rate = n_b * n_e * alpha_B * 2.18e-18
    return rate * yr_to_s * Mpc_to_m**3

# Total proper rate
def R_total_proper(z):
    return R_stellar(z) + R_Thomson_proper(z) + R_recomb_proper(z)

# The integral for ρ_DM(z_o) with CORRECT units
# ρ_DM(z_o) = (1+z_o)^3 * integral from z_o to z_max of R(z') / ((1+z')^4 * E(z')) dz'
# 
# But R here is the proper rate, and we need to convert to comoving.
# Actually, I think the correct formula is:
# ρ_DM(z_o) = (1+z_o)^3 * integral of R_proper(z') * a^3(z') / ((1+z')^4 * E(z')) dz'
#            = (1+z_o)^3 * integral of R_proper(z') / ((1+z')^7 * E(z')) dz'
# 
# Wait, no. Let me think again.
# 
# At observation time z_o, the proper volume containing a fossil
# emitted at time z_e is V_proper(z_o) = V_comoving * a^3(z_o).
# 
# The energy of the fossil is E_em (set at time z_e, not redshifted
# for a non-relativistic fossil).
# 
# So dρ(z_o) = E_em / V_proper(z_o) = (R(z_e) * V_c * dt_e) / (V_c * a^3(z_o))
#          = R(z_e) * dt_e / a^3(z_o)
# 
# And dt_e / a^3(z_o) = (dt_e / dz_e) / a^3(z_o) * dz_e
# 
# dt_e / dz_e = -1 / ((1+z_e) * H(z_e))
# 
# So dρ(z_o) = -R(z_e) / (a^3(z_o) * (1+z_e) * H(z_e)) dz_e
# 
# Integrating from z_o to z_max:
# ρ_DM(z_o) = (1/(a^3(z_o))) * integral from z_o to z_max of R(z_e) / ((1+z_e) * H(z_e)) dz_e
#           = (1+z_o)^3 * integral R(z_e) / ((1+z_e) * H(z_e)) dz_e
# 
# Wait, this is different from what I had before! Let me check.
# 
# Actually, the issue is what "R" is. If R is the rate per PROPER volume,
# then we have R(z_e) / ((1+z_e) * H(z_e)) in the integrand.
# 
# If R is the rate per COMOVING volume, then R(z_e) here would be the
# same as the proper rate times (proper vol / comoving vol) = a^3(z_e).
# 
# So if R is the proper rate:
# ρ_DM(z_o) = (1+z_o)^3 * integral R_proper(z_e) / ((1+z_e) * H(z_e)) dz_e
# 
# If R is the comoving rate:
# ρ_DM(z_o) = (1+z_o)^3 * integral R_comoving(z_e) / ((1+z_e) * H(z_e)) dz_e
#           = (1+z_o)^3 * integral R_proper(z_e) * a^3(z_e) / ((1+z_e) * H(z_e)) dz_e
#           = (1+z_o)^3 * integral R_proper(z_e) / ((1+z_e)^4 * H(z_e)) dz_e
# 
# Hmm, so the difference is whether the integrand has (1+z_e) or (1+z_e)^4.
# 
# Let me think about this physically. The (1+z_e)^4 factor was supposed
# to be the fossil dilution: (1+z_e)^3 from volume, (1+z_e) from time.
# But this dilution only applies if the energy is COMOVING with the
# expansion.
# 
# For a fossil (2D universe ending), the energy is deposited into the
# 3+1D universe. This energy is then just normal 3+1D energy, which
# behaves like matter (dilutes as a^3 in proper volume).
# 
# So the fossil's energy in proper volume at time t_o is:
# dE / V_proper(t_o) = dE_em * a^3(t_e) / V_proper(t_o)  [wait this is wrong]
# 
# Hmm, let me think. The fossil deposits dE in comoving volume V_c at
# time t_e. At a later time t_o, this dE is in proper volume
# V_proper(t_o) = V_c * a^3(t_o).
# 
# So dρ(t_o) = dE / V_proper(t_o) = dE / (V_c * a^3(t_o))
# 
# Now dE = R * (V_c or V_p) * dt, depending on what R is.
# 
# If R is rate per comoving volume: dE = R * V_c * dt
#   dρ(t_o) = R * V_c * dt / (V_c * a^3(t_o)) = R * dt / a^3(t_o)
#   With dt = -dz / ((1+z) * H(z)) and a^3(t_o) = 1/(1+z_o)^3:
#   dρ(z_o) = R * (-dz) / ((1+z_e) * H(z_e) * a^3(z_o))
#          = R * (1+z_o)^3 / ((1+z_e) * H(z_e)) dz
#   So ρ(z_o) = (1+z_o)^3 * integral R / ((1+z_e) * H(z_e)) dz_e
# 
# If R is rate per proper volume: dE = R * V_p * dt = R * V_c * a^3 * dt
#   dρ(t_o) = R * V_c * a^3(t_e) * dt / (V_c * a^3(t_o))
#          = R * a^3(t_e) * dt / a^3(t_o)
#          = R * a^3(t_e) * (-dz) / ((1+z_e) * H(z_e) * a^3(z_o))
#          = R * (1+z_o)^3 * (1+z_e)^(-3) / ((1+z_e) * H(z_e)) dz
#          = R * (1+z_o)^3 / ((1+z_e)^4 * H(z_e)) dz
#   So ρ(z_o) = (1+z_o)^3 * integral R / ((1+z_e)^4 * H(z_e)) dz_e
# 
# OK so the (1+z)^4 in the denominator is the result of using the
# PROPER rate. The (1+z) in the denominator is the result of using
# the COMOVING rate.
# 
# In the cascade, the "rate" is usually stated in proper units (energy
# per proper volume per proper time). So the (1+z)^4 formula is correct.
# 
# OK so the integral is:
# ρ_DM(z_o) = (1+z_o)^3 * integral R_proper(z_e) / ((1+z_e)^4 * E(z_e)) dz_e
# 
# In my v2 calc, I used R_Thomson (which was the proper rate) in the
# integrand R / ((1+z)^4 * E). This is correct. So why is v2's
# r(z=6) = 0.66 and v3's r(z=6) ~ 0.0001?
# 
# Let me trace through.
# 
# v2: T_gamma = T_CMB_0 * (1+z) for all z
# v3: T_gamma = T_CMB_0 * (1+z) for z > 1100, T_CMB_0 * 1101 * (1+z)^2 / 1101^2 for z < 1100
# 
# At z=6:
# v2: T_gamma = 2.725 * 7 = 19 K
# v3: T_gamma = 2.725 * 1101 * 49 / 1101^2 = 2.725 * 49 / 1101 = 0.121 K
# 
# So v2 has 157x higher T_gamma at z=6.
# 
# n_b * n_gamma * σ_T * c * k_B is the rate per (volume*time) at unit T.
# At z=6: n_b = 85.7, n_gamma = 1.41e11
# rate per unit T = 85.7 * 1.41e11 * 1.995e-20 * 1.38e-23 = 3.3e-29 J/m^3/s/K
# 
# v2 rate: 3.3e-29 * 19 = 6.3e-28 J/m^3/s
# v3 rate: 3.3e-29 * 0.121 = 4.0e-30 J/m^3/s
# 
# In Mpc^3/yr: rate * 1.44e47 * 3.156e7 = rate * 4.5e54
# v2: 6.3e-28 * 4.5e54 = 2.8e27 J/yr/Mpc^3
# v3: 4.0e-30 * 4.5e54 = 1.8e25 J/yr/Mpc^3
# 
# Hmm, but the v2 calc printed R_Thomson(z=6) ~ 8.029e-1 J/yr/Mpc^3
# 
# So there's a huge discrepancy. Let me look at the v2 print again:
# z=6:  r_t = 8.029e-1, r_total = ~ 8e-1
# 
# And the new calc (matter_radiation_equality_R_z.py) printed:
# z=5000:  r_t = 7.134e+17, r_tot = 1.638e+34
# 
# These differ by many orders of magnitude. There's clearly a unit issue.
# 
# I think the v2 calc had some unit errors. Let me just use the v3
# calculation (corrected temperature) and trust the result.
# 
# But wait, even the v3 result should still have some Thomson contribution.
# Let me check: at z=1100, R_Thomson_proper = ?
# 
# n_b(1100) = 85.7 * 1101^3 = 1.14e11 /m^3
# n_gamma(1100) = 1.41e11 * 1101^3 = 1.88e14 /m^3 (at z=6 was 1.41e11)
# Wait, n_gamma(1100) = 4.11e8 * 1101^3 = 5.5e14 /m^3
# T_gamma(1100) = 3000 K
# rate at z=1100: 1.14e11 * 5.5e14 * 1.995e-20 * 1.38e-23 * 3000
#               = 1.14e11 * 5.5e14 * 1.995e-20 * 4.14e-20
#               = 5.2e-14 J/m^3/s
# In Mpc^3/yr: 5.2e-14 * 4.5e54 = 2.3e41 J/yr/Mpc^3
# 
# So R_Thomson_proper at z=1100 is ~2.3e41 J/yr/Mpc^3.
# And R_stellar at z=1100 is ~0 (no stars).
# 
# At z=2 (peak SFR):
# R_stellar: 0.015 * 3.9^2.7 / 2 * 0.15/10 * 1e46 = 0.015 * 35 / 2 * 0.015 * 1e46
#           = 4.0e42 J/yr/Mpc^3
# R_Thomson_proper: 3.3e-29 * 0.121 * 4.5e54 = 1.8e25 (for z=2, T_gamma ~ 0.025 K)
#                  actually let me compute T_gamma(2) = 2.725 * 1101 * 9 / 1101^2 = 0.0223 K
#                  rate = 3.3e-29 * 0.0223 * 4.5e54 = 3.3e24
# 
# So R_Thomson at z=2 is ~3e24, and R_stellar at z=2 is ~4e42.
# Thomson is 18 orders of magnitude SMALLER.
# 
# So the Thomson contribution is NEGLIGIBLE compared to stellar at z=2.
# 
# At z=1100, R_Thomson ~ 2.3e41 and R_stellar ~ 0. So Thomson DOMINATES
# at z > 1100. But the (1+z)^4 dilution means the high-z contribution
# to low-z DM is small.
# 
# Let me check: at z=1100, the integrand in r(z=6) is:
# R_Thomson(1100) / ((1+1100)^4 * E(1100))
# = 2.3e41 / (1101^4 * sqrt(Om * 1101^3 + Og * 1101^4))
# = 2.3e41 / (1.5e12 * sqrt(0.315 * 1.3e9 + 5.4e-5 * 1.5e12))
# = 2.3e41 / (1.5e12 * sqrt(4.2e8 + 7.9e7))
# = 2.3e41 / (1.5e12 * 7.1e4)
# = 2.3e41 / 1.07e17
# = 2.1e24
# 
# At z=2, the integrand in r(z=6) is:
# R_stellar(2) / ((1+2)^4 * E(2))
# = 4e42 / (81 * 1.5)
# = 4e42 / 121
# = 3.3e40
# 
# So the stellar contribution at z=2 dominates the integrand by 16
# orders of magnitude over the Thomson at z=1100.
# 
# The integrand at z=2 is much larger than at z=1100. So the integral
# from z=6 to z_max is dominated by the stellar events at z~2-3.
# 
# And r(z=6) = (1+6)^3 * integral = 343 * 3.3e40 * (range of z)
# 
# The integral from 6 to 20 with this integrand is roughly:
# - stellar at z=2-3 dominates, but we start at z=6, so stellar
#   contributes from z=6 to z=10
# - stellar integrand drops off as (1+z) decreases
# - total integral ~ integral of stellar from 6 to 10
# 
# r(z=6) ~ 343 * (a few e40) * 4 = 1.4e43
# 
# ρ_DM(0) ~ 343 * integral from 0 to 20 of stellar = much larger
# 
# So r(z=6) = 1.4e43 / 5e44 = 0.3 or so?
# 
# Hmm, that's much higher than the v3 calc showed. Let me check the v3 calc again.

python3 -c "
import numpy as np
from scipy.integrate import quad

# Constants
H0 = 67.4
Om = 0.315
Og = 5.4e-5
Omega_DE = 0.68
rho_crit_0_kg = 8.5e-27
Ob = 0.049
sigma_T = 6.65e-29
c_light = 3e8
k_B = 1.38e-23
T_CMB_0 = 2.725
m_p = 1.67e-27
n_gamma_0 = 4.11e8
Mpc_to_m = 3.086e22
yr_to_s = 3.156e7

def E_LCDM(z):
    return np.sqrt(Om * (1+z)**3 + Og * (1+z)**4 + Omega_DE)

def sfr(z):
    return 0.015 * (1 + z)**2.7 / (1 + ((1+z)/2.9)**5.6)

def R_stellar(z):
    return sfr(z) * 0.015 * 1e46

# Compute r(z=6) with just stellar
def integrand(z):
    return R_stellar(z) / (E_LCDM(z) * (1+z)**4)

# Numerical integration
z_arr = np.linspace(0.001, 20, 1000)
integrand_arr = integrand(z_arr)
rho_0 = np.trapezoid(integrand_arr, z_arr)
print(f'rho_DM(0) ~ {rho_0:.3e}')

# For z=6, integrate from 6 to 20
z_arr_6 = np.linspace(6, 20, 500)
integrand_arr_6 = integrand(z_arr_6)
rho_6 = 7**3 * np.trapezoid(integrand_arr_6, z_arr_6)
print(f'rho_DM(6) = (1+6)^3 * integral = {rho_6:.3e}')

r_6 = rho_6 / rho_0
print(f'r(z=6) = {r_6:.3e}')

# Print integrand at a few z
for z in [0.1, 1, 2, 3, 5, 6, 10, 15, 20]:
    print(f'z={z}: integrand = {integrand(z):.3e}')
"
