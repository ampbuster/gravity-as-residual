#!/usr/bin/env python3
"""
v3.3 Pattern finder: per-event mu ratios and the role of alpha
===============================================================

We use the BRUTE FORCE RESULT directly:
  For SN, mu = alpha * (E/M_Pl,3D) / tau_Pl  (matched by construction to give 9.67e6 GeV^2)

We then compute per-event mu for all 8 events using this formula,
look for patterns, and test if a formula involving alpha works better.
"""

import numpy as np
from math import pi, sqrt, log, exp, log10

# Physical constants
c_light = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
GeV = 1.602e-10

t_Pl = sqrt(hbar * G / c_light**5)
M_Pl_3D = sqrt(hbar * c_light / G) / GeV  # 1.22e19 GeV
alpha = 1.289
mu_framework = 9e6  # GeV^2

# SIDC events
events = [
    # name, E (J), tau_2D (s)
    ("1 ton TNT",        4e9,    1e-43),
    ("X-class flare",    1e25,   1e-23),
    ("Type Ia SN",       1e44,   33),
    ("Hypernova",        1e46,   1.26e4),
    ("Long GRB",         1e47,   2.42e5),
    ("BNS merger",       1e53,   1.26e13),
    ("AGN flare",        1e55,   3.16e15),
    ("Quasar outburst",  1e60,   1.58e22),
]

print("=" * 80)
print("PER-EVENT MU VIA ENTROPY MATCHING")
print("=" * 80)
print()
print(f"Framework target mu = {mu_framework:.2e} GeV^2 (SN calibrated)")
print(f"alpha = {alpha}")
print()

# The brute force formula was:
# mu = alpha * (E/M_Pl,3D) / tau_2D * K
# where K was calibrated to give 9.67e6 for SN.
# This means: for the brute force formula to work, K is fixed by SN.

# Define mu via the brute force formula (K from SN)
E_SN_J = 1e44
tau_SN_s = 33
E_SN_GeV = E_SN_J / GeV
E_SN_MPl = E_SN_GeV / M_Pl_3D
tau_SN_Pl = tau_SN_s / t_Pl

# K = mu_SN / (alpha * E_SN/M_Pl / tau_SN)
mu_SN_brute = 9.67e6  # GeV^2
K_brute = mu_SN_brute / (alpha * E_SN_MPl / tau_SN_Pl)
print(f"K_brute = {K_brute:.4e} GeV^2 units")
print()

# Now compute mu for each event
mus = []
for name, E_J, tau_s in events:
    E_GeV = E_J / GeV
    tau_Pl = tau_s / t_Pl
    E_MPl = E_GeV / M_Pl_3D
    mu_i = K_brute * alpha * E_MPl / tau_Pl
    mus.append(mu_i)

print("Per-event mu (entropy-matching formula):")
print()
print(f"{'Event':<20}{'E (J)':<12}{'tau (s)':<12}{'mu (GeV^2)':<15}{'log10(mu/mu_SN)':<18}")
print("-" * 80)
SN_idx = 2
for i, (name, E_J, tau_s) in enumerate(events):
    log_ratio = log10(mus[i] / mus[SN_idx])
    print(f"{name:<20}{E_J:<12.0e}{tau_s:<12.0e}{mus[i]:<15.2e}{log_ratio:<+18.2f}")
print()
print(f"Range: {min(mus):.2e} to {max(mus):.2e}")
print(f"Spread: max/min = {max(mus)/min(mus):.2e}")
print()

print("=" * 80)
print("PATTERN: log10(mu/mu_SN) vs log10(E/E_SN) and log10(tau/tau_SN)")
print("=" * 80)
print()

print(f"{'Event':<20}{'log10(E/E_SN)':<18}{'log10(tau/tau_SN)':<20}{'log10(mu/mu_SN)':<18}")
print("-" * 80)
for i, (name, E_J, tau_s) in enumerate(events):
    log_E = log10(E_J / E_SN_J)
    log_tau = log10(tau_s / tau_SN_s)
    log_mu = log10(mus[i] / mus[SN_idx])
    print(f"{name:<20}{log_E:<+18.2f}{log_tau:<+20.2f}{log_mu:<+18.2f}")
print()

print("If mu = K * E^a / tau^b, then:")
print("  log(mu/mu_SN) = a * log(E/E_SN) - b * log(tau/tau_SN)")
print()

# Linear fit
import numpy as np
A_mat = []
b_vec = []
for i, (name, E_J, tau_s) in enumerate(events):
    log_E = log10(E_J)
    log_tau = log10(tau_s)
    log_mu = log10(mus[i])
    A_mat.append([log_E, log_tau, 1])
    b_vec.append(log_mu)

A_mat = np.array(A_mat)
b_vec = np.array(b_vec)
x, residuals, rank, sv = np.linalg.lstsq(A_mat, b_vec, rcond=None)
a, b, c = x

print("=" * 80)
print("LINEAR FIT: log10(mu) = a * log10(E) + b * log10(tau) + c")
print("=" * 80)
print()
print(f"a = {a:.4f} (expected 1 from brute force formula)")
print(f"b = {b:.4f} (expected -1 from brute force formula)")
print(f"c = {c:.4f}")
print()

# Predicted vs actual
print(f"{'Event':<20}{'log10(mu) actual':<20}{'log10(mu) predicted':<22}{'residual':<12}")
print("-" * 80)
for i, (name, E_J, tau_s) in enumerate(events):
    log_mu_pred = a * log10(E_J) + b * log10(tau_s) + c
    log_mu_actual = log10(mus[i])
    residual = log_mu_pred - log_mu_actual
    print(f"{name:<20}{log_mu_actual:<20.2f}{log_mu_pred:<22.2f}{residual:<+12.4f}")
print()

print("The fit should give a=1, b=-1 (the brute force formula).")
print()

# Now look at the pattern with alpha
print("=" * 80)
print("PATTERN INVOLVING alpha")
print("=" * 80)
print()

# Try: mu = K * alpha^a * (E/M_Pl,3D)^beta * (tau/t_Pl)^gamma
# Fit: log10(mu) = a * log10(alpha) + beta * log10(E/M_Pl) + gamma * log10(tau/t_Pl) + log10(K)
# But alpha is constant, so it just contributes to K

# More interesting: try including (E/tau) relationships
# log10(E/tau) = log10(E) - log10(tau) for each event
# mu ~ E/tau from brute force

print("Try: mu = (E/tau)^a * M_Pl,3D^b * alpha^c")
print()
# This is: log10(mu) = a * log10(E/tau) + b * log10(M_Pl,3D) + c * log10(alpha)
# But log10(M_Pl,3D) and log10(alpha) are constants
# So fit: log10(mu) = a * log10(E/tau) + const

log_E_over_tau = []
log_mu = []
for i, (name, E_J, tau_s) in enumerate(events):
    log_E_over_tau.append(log10(E_J) - log10(tau_s))
    log_mu.append(log10(mus[i]))

log_E_over_tau = np.array(log_E_over_tau)
log_mu = np.array(log_mu)

# Linear fit: log_mu = a * log_E_over_tau + b
A = np.column_stack([log_E_over_tau, np.ones(8)])
x = np.linalg.lstsq(A, log_mu, rcond=None)[0]
a_single, b_single = x

print(f"Fit: log10(mu) = {a_single:.4f} * log10(E/tau) + {b_single:.4f}")
print(f"Slope a = {a_single:.4f} (expected 1 if mu ~ E/tau)")
print(f"Intercept b = {b_single:.4f}")
print(f"In natural form: mu = 10^{b_single:.4f} * (E/tau)^{a_single:.4f}")
print()

# Predicted vs actual
print(f"{'Event':<20}{'log10(mu) actual':<20}{'log10(mu) predicted':<22}{'residual':<12}")
print("-" * 80)
for i, (name, E_J, tau_s) in enumerate(events):
    log_mu_pred = a_single * (log10(E_J) - log10(tau_s)) + b_single
    log_mu_actual = log10(mus[i])
    residual = log_mu_pred - log_mu_actual
    print(f"{name:<20}{log_mu_actual:<20.2f}{log_mu_pred:<22.2f}{residual:<+12.4f}")
print()

print("=" * 80)
print("WHAT FORMULA EXPLAINS THE mu_i / mu_SN RATIOS?")
print("=" * 80)
print()

# Look for relations involving alpha
# Pattern: mu_i / mu_SN should equal some function of (E_i/E_SN, tau_i/tau_SN, alpha)
# Try: (mu_i/mu_SN) = (E_i/E_SN)^alpha^a * (tau_i/tau_SN)^alpha^b

# For alpha = 1.289, try a=1, b=-1: (E_i/E_SN)^1.289 * (tau_i/tau_SN)^(-1.289)
# Or: a=1/alpha, b=-1/alpha

print("Test formulas for mu_i/mu_SN:")
print()
SN_mu = mus[SN_idx]
E_SN, tau_SN = 1e44, 33

for a_exp in [1, 1/alpha, alpha, 1-alpha]:
    for b_exp in [-1, -1/alpha, -alpha, -(1-alpha)]:
        # Compute predicted ratio
        predicted_ratios = []
        actual_ratios = []
        for i, (name, E_J, tau_s) in enumerate(events):
            pred = (E_J/E_SN)**a_exp * (tau_s/tau_SN)**b_exp
            actual = mus[i] / SN_mu
            predicted_ratios.append(pred)
            actual_ratios.append(actual)
        
        # Compute residuals in log space
        residuals = [log10(p/a) for p, a in zip(predicted_ratios, actual_ratios)]
        max_resid = max(abs(r) for r in residuals)
        
        if max_resid < 0.5:
            print(f"  mu_i/mu_SN = (E_i/E_SN)^{a_exp:.4f} * (tau_i/tau_SN)^{b_exp:.4f}")
            print(f"    max log-residual = {max_resid:.4f}")
            print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print(f"The brute force formula mu = K * alpha * (E/M_Pl,3D) / tau gives:")
print(f"  - SN match by construction (K calibrated to SN)")
print(f"  - Per-event mu varies by {max(mus)/min(mus):.2e}")
print(f"  - Slope of log mu vs log E is 1, slope vs log tau is -1")
print(f"  - This is the entropy-matching pattern")
print()
print(f"CONCLUSION: mu is EVENT-DEPENDENT if we use the entropy-matching formula.")
print(f"The framework's choice of universal mu = 9e6 GeV^2 is the SN-calibrated value.")
print(f"No formula involving alpha makes mu universal.")
print()
print("=" * 80)