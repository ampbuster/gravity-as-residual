#!/usr/bin/env python3
"""
Mechanism L: Model-dependent interpretation of the Hubble tension

HISTORICAL CONTEXT (v2.5 update): This file was written when the cascade's
Mechanism M era claimed H_0 = 73 (a value borrowed from SH0ES, not derived
by the cascade). The file tests whether the cascade's picture is consistent
with the SH0ES value. The H_0 = 73 used here is a TEST INPUT, not a cascade
prediction. In v2.5 (commit 281), the HubbleTensionCalculator was removed
and §2.6.1 (Honest H_0 framework) added: the cascade is qualitatively
consistent with H_0 = 70 ± 3 across all measurements but does NOT derive a
specific H_0 value.

CLAIM: The CMB-inferred H_0 = 67.4 is an ARTIFACT of assuming LCDM.
       In the cascade's model, CMB analysis would give H_0 ~ 73.

This file makes the argument quantitative, even without re-running Planck.

Key question: how does Planck infer H_0 = 67.4?
Answer: Planck measures the acoustic peak structure of the CMB.
        The peak positions depend on the angular size of the sound horizon
        at recombination: theta_* = r_s(z_*) / D_A(z_*).
        
        r_s(z_*) = integral of c_s / H(z) from z_* to infinity
        D_A(z_*) = (c / H_0) integral of 1/E(z) from 0 to z_*
        
        Planck measures theta_* very precisely.
        r_s depends on early-universe physics (H(z) at high z).
        D_A depends on late-universe physics (H_0, Omega_m).
        
        So: theta_* = r_s / (c/H_0 * integral) = (H_0 * r_s) / (c * integral)
        => H_0 = theta_* * c * integral / r_s

Now, in the cascade model:
  1. The early-universe physics (z > 1100) is mostly the same as LCDM
     (radiation-dominated, recombination physics unchanged)
     => r_s is approximately the same
  2. The late-universe physics (z < 1100) is different
     - In LCDM: D_A depends on H_0 and Omega_m via standard integral
     - In cascade: D_A also depends on the cascade-specific back-projection
     
Let's see what Planck ACTUALLY uses:
  theta_* = r_s / D_A(z_*)
  D_A(z_*) = c/H_0 * integral from 0 to z_* of dz/E(z)
  
Planck measures theta_* = 0.01041 (very precise, ~0.03% error)

In LCDM with H_0 = 67.4, Omega_m = 0.315:
  r_s = 144.4 Mpc
  D_A(1089) = 13,800 Mpc
  theta_* = 144.4/13800 = 0.01046 (matches)

If H_0 were 73:
  r_s is the same (early universe)
  D_A(1089) would be smaller (less H_0, same Omega_m)
  D_A_new = D_A_LCDM * 67.4/73 = 13800 * 67.4/73 = 12,743 Mpc
  theta_*_new = 144.4/12743 = 0.01133 (TOO BIG, doesn't match Planck)

So if everything else is the same and H_0 changes, theta_* changes.
Planck forces theta_* = 0.01041.
This forces H_0 = 67.4 in LCDM.

Now: in the cascade, is r_s different? What if the cascade modifies
the early-universe physics enough that r_s is larger?

For the cascade to give H_0 = 73, we need theta_* to match Planck
with D_A_LCDM_73. The D_A_LCDM_73 = 12,743 Mpc.
For theta_* = 0.01041:
  r_s_cascade = theta_* * D_A_LCDM_73 = 0.01041 * 12743 = 132.6 Mpc

But LCDM gives r_s = 144.4 Mpc. So r_s would need to be SMALLER
in the cascade, not larger.

Wait, that's the wrong direction. If r_s is smaller in cascade, then
D_A needs to be smaller too for theta_* to match. So H_0 would be
LARGER. But then D_A = c/H_0 * integral, and H_0 is in the denominator.

Let me redo this:
  theta_* = r_s / D_A(z_*) = r_s * H_0 / (c * integral)
  
  => H_0 = theta_* * c * integral / r_s

In LCDM: r_s = 144.4, integral = ..., H_0 = 67.4
In cascade: we want H_0 = 73. So we need:
  73 = theta_* * c * integral / r_s_cascade
  73/67.4 = r_s_LCDM / r_s_cascade
  r_s_cascade = r_s_LCDM * 67.4/73 = 144.4 * 0.923 = 133.4 Mpc

So the cascade's r_s would need to be 133.4 Mpc instead of 144.4 Mpc.
That's an 8% smaller sound horizon.

Is this plausible in the cascade? Let me think about what controls r_s:

  r_s(z_*) = integral from z_* to infinity of c_s(z) dz / H(z)
  
  c_s(z) = c / sqrt(3 (1 + R))
  R = 3 rho_b / (4 rho_gamma)
  
  H(z) = H_0 * sqrt(Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L)
  
At high z (z > 1000), radiation dominates:
  H(z) ~ H_0 * sqrt(Omega_r) * (1+z)^2
  
  r_s ~ integral of c_s / (H_0 sqrt(Omega_r) (1+z)^2) dz
      = (c_s/H_0/sqrt(Omega_r)) * integral of 1/(1+z)^2 dz from z_* to inf
      = (c_s/H_0/sqrt(Omega_r)) * 1/z_*

So r_s ~ 1/(H_0 sqrt(Omega_r))
   H_0 is here! Because H_0 sets the overall expansion rate scale.

In LCDM, H_0 = 67.4, sqrt(Omega_r) is fixed.
r_s = 144.4 Mpc.

In cascade, H_0 = 73. If r_s is computed the same way:
  r_s_cascade = 144.4 * 67.4/73 = 133.4 Mpc (using H_0 = 73)

But this is exactly what we needed! If the cascade uses the SAME
early-universe physics formula but with H_0 = 73 (its actual expansion
rate at all z), then r_s automatically becomes 133.4 Mpc.

Wait, this is circular. Let me think again.

The way Planck infers H_0:
1. Planck measures theta_* = 0.01041
2. Planck assumes LCDM
3. Planck computes r_s(z_*) using the LCDM formula with their assumed parameters
4. Planck computes D_A(z_*) using the LCDM formula with their assumed H_0
5. r_s / D_A must equal theta_*
6. This constrains H_0 to 67.4

In the cascade:
1. Planck measures theta_* = 0.01041 (same data, model-independent)
2. Cascade uses cascade model
3. Cascade computes r_s(z_*) using cascade's formula for early universe
4. Cascade computes D_A(z_*) using cascade's formula for late universe
5. r_s / D_A must equal theta_*
6. This constrains cascade's H_0 to... something else

The question: does the cascade's early-universe formula give a different r_s?
The cascade's late-universe formula gives a different D_A?

For the late universe, the cascade has H_0 = 73 (the "real" H_0).
D_A in cascade uses H_0 = 73 and the cascade's 2D back-projection
(equivalent to Omega_m = 0.27, the cascade's 27% matter + 5% 2D
back-projected DM = 32%).

For the early universe, the cascade has:
  - Same radiation content (photons, neutrinos)
  - Same baryon content
  - DE = 0 at z > 1100 (cascade says DE is from 4D event, only contributes
    at low z in cascade's picture)
  - DM = 0 at z > 1100 (cascade says DM is from 2D universes, which
    didn't exist at z > 1100)
  - "Matter" = only baryons at z > 1100

So in cascade's early universe:
  Omega_m(early) = Omega_b = 0.05 (just baryons)
  Omega_DM(early) = 0
  Omega_DE(early) = 0
  Omega_r(early) = 0.0001 (photons + neutrinos)
  Omega_L(early) = 0.9499 (??)

This is a HUGE difference! At z = 1100, the cascade has:
  H(z)^2 = H_0^2 [Omega_r (1+z)^4 + Omega_b (1+z)^3 + 0.9499]
  vs LCDM:
  H(z)^2 = H_0^2 [Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L]

The 0.9499 "Lambda-like" term would dominate at z = 1100 if Omega_b is
small. But Omega_b = 0.05 (1+z)^3 = 0.05 * 1100^3 = 6.65e10
And 0.9499 vs (1+z)^0 = 0.9499

So Omega_b (1+z)^3 = 6.65e10 >> 0.9499. Baryons dominate at z = 1100
in cascade. Good.

But LCDM at z = 1100 has:
  Omega_m (1+z)^3 = 0.315 * 1100^3 = 4.19e11
  Omega_L (1+z)^0 = 0.685
  Omega_m (1+z)^3 >> Omega_L
  So matter (baryons + DM) dominates in LCDM at z = 1100

In cascade at z = 1100:
  Omega_b (1+z)^3 = 0.05 * 1100^3 = 6.65e10
  0.9499 (1+z)^0 = 0.9499
  Omega_b (1+z)^3 >> 0.9499
  So baryons dominate in cascade at z = 1100

The ratio: cascade's H(z=1100)^2 / LCDM's H(z=1100)^2
= Omega_b(1+z)^3 + 0.9499 / (Omega_m(1+z)^3 + Omega_L)
= 6.65e10 + 0.9499 / (4.19e11 + 0.685)
~ 6.65e10 / 4.19e11
= 0.159

So cascade's H(z=1100) is sqrt(0.159) = 0.398 of LCDM's H(z=1100).
H_cascade(z=1100) = 0.398 * H_LCDM(z=1100)

Now r_s = integral c_s / H(z) dz from z_* to inf
In cascade: r_s_cascade = r_s_LCDM * H_LCDM(z=1100) / H_cascade(z=1100)
                   = 144.4 * 1/0.398 = 363 Mpc
                   
That's MUCH BIGGER than LCDM's r_s = 144.4 Mpc.

And D_A(z_*) = c/H_0 * integral dz/E(z) from 0 to z_*
For D_A, we use the LATE universe (z < z_*).
In cascade late universe:
  H(z) = H_0_cascade * E_cascade(z)
  where E_cascade(z) = sqrt(Omega_m_eff (1+z)^3 + Omega_L_eff)
  with Omega_m_eff = 0.32 (cascade's effective matter) and Omega_L_eff = 0.68
  
  D_A_cascade(z_*) = c/H_0_cascade * integral
  with H_0_cascade = 73

For theta_*:
  theta_* = r_s_cascade / D_A_cascade
  = 363 / (c/73 * integral)

For LCDM:
  theta_* = 144.4 / (c/67.4 * integral)
  
If integrals are the same (same Omega_m_eff = 0.32, Omega_L_eff = 0.68):
  ratio of D_A: D_A_cascade/D_A_LCDM = (c/73 * integral) / (c/67.4 * integral)
              = 67.4/73 = 0.923
              
So D_A_cascade = 0.923 * D_A_LCDM

theta_*_cascade / theta_*_LCDM = (363 / 144.4) / 0.923
= 2.51 / 0.923
= 2.72

So cascade's theta_* would be 2.72 times LCDM's theta_*. That's WAY off.

This means: if cascade's early universe has only baryons (no DM, no DE),
the r_s is MUCH bigger, and theta_* would be 2.72x too big.

That's clearly inconsistent with Planck's measurement of theta_* = 0.01041.

Hmm. This is a problem for Mechanism L.

Wait, let me reconsider. The cascade DOES have radiation at z = 1100.
It just has baryons and photons. The factor of 0.159 vs 1 was comparing
Omega_b (1+z)^3 to Omega_m (1+z)^3. But Omega_m = 0.315 and Omega_b = 0.05.
Ratio = 0.05/0.315 = 0.159. Yes, the cascade's H(z=1100) is sqrt(0.159)
times LCDM's H(z=1100).

But that gives a cascade r_s that's 2.5x too big.

So... the cascade's early universe IS different from LCDM's.
If we use cascade's early universe, r_s is larger, theta_* is larger,
Planck would have measured a different theta_*.

But Planck measured theta_* = 0.01041 (the same as LCDM predicts).
So if cascade is the right model, and Planck measured theta_* = 0.01041,
the cascade's r_s and D_A must combine to give theta_* = 0.01041.

For cascade: theta_* = r_s_cascade / D_A_cascade
We computed: r_s_cascade = 2.51 * r_s_LCDM
            D_A_cascade = 0.923 * D_A_LCDM (using H_0 = 73 in late universe)
            theta_*_cascade = 2.51/0.923 * theta_*_LCDM = 2.72 * 0.01041 = 0.0283

But Planck measured 0.01041. So the cascade as I've modeled it
predicts theta_* = 0.0283, which is 2.7x too big.

This means: the cascade, in its current form, CANNOT have H_0 = 73
at all z and still match Planck's theta_* measurement.

The cascade's prediction IS that theta_* would be different from LCDM.
And if Planck measured 0.01041 (matching LCDM), then... the cascade
is wrong about H_0 = 73?

OR: the cascade has some additional physics at high z that I'm missing.
Let me think.

What if the cascade's 2D universe creation starts at z = 1100 and adds
DM gradually? At z = 1100, no DM yet. As z decreases, 2D universes are
created, contributing DM. By z = 0, total DM = 27%.

In that case, between z = 0 and z = 1100, the effective Omega_m is
gradually increasing from Omega_b to Omega_b + Omega_DM.

This means the sound horizon integral is:
  r_s = integral c_s/H(z) dz
  
  H(z) depends on Omega_m(z), which varies with z in cascade.
  At high z: H(z) ~ H_0 * sqrt(Omega_r (1+z)^4 + Omega_b(z) (1+z)^3)
  At low z: H(z) ~ H_0 * sqrt(Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L)
  
  With H_0 = 73 (the cascade's H_0).

Let me compute more carefully:

At z = 1100:
  cascade: H(z) = 73 * sqrt(Omega_r * 1100^4 + Omega_b * 1100^3 + Omega_L_4d(1100))
  In cascade, Omega_L_4d(z=1100) is... 0? (DE only at low z?)
  H(1100) = 73 * sqrt(Omega_r * 1100^4 + 0.05 * 1100^3)
  
  Omega_r ~ 9e-5 (photons + neutrinos)
  9e-5 * 1100^4 = 9e-5 * 1.46e12 = 1.32e8
  0.05 * 1100^3 = 0.05 * 1.33e9 = 6.65e7
  Sum: 1.98e8
  
  H(1100) = 73 * sqrt(1.98e8) = 73 * 14071 = 1.027e6 km/s/Mpc

For LCDM with H_0 = 67.4:
  H(1100) = 67.4 * sqrt(9e-5 * 1100^4 + 0.315 * 1100^3 + 0.685)
  = 67.4 * sqrt(1.32e8 + 4.19e11 + 0.685)
  = 67.4 * sqrt(4.19e11)
  = 67.4 * 647227
  = 4.36e7 km/s/Mpc

So cascade's H(1100) / LCDM's H(1100) = 1.027e6 / 4.36e7 = 0.0236

Hmm, that's even smaller than before. Let me recheck.

Wait, in LCDM:
  H(1100) = H_0 * sqrt(Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L)
  = 67.4 * sqrt(9e-5 * 1100^4 + 0.315 * 1100^3 + 0.685)
  
  9e-5 * 1100^4 = 9e-5 * 1.46e12 = 1.32e8
  0.315 * 1100^3 = 0.315 * 1.33e9 = 4.19e11
  0.685
  
  Sum: 4.19e11 + 1.32e8 + 0.685 ~ 4.19e11 (matter dominates at z=1100)
  sqrt: 6.47e5
  H(1100) = 67.4 * 6.47e5 = 4.36e7

In cascade (no DM, no DE at z=1100):
  H(1100) = 73 * sqrt(9e-5 * 1100^4 + 0.05 * 1100^3 + 0)
  
  9e-5 * 1100^4 = 1.32e8
  0.05 * 1100^3 = 6.65e7
  
  Sum: 1.99e8
  sqrt: 1.41e4
  H(1100) = 73 * 1.41e4 = 1.03e6

So cascade's H(1100) is 1.03e6, LCDM's is 4.36e7. Ratio = 0.024.

So cascade's H(1100) is 42x SMALLER than LCDM's.

This means r_s_cascade / r_s_LCDM = H_LCDM(1100) / H_cascade(1100) = 42x

r_s_cascade = 42 * 144.4 = 6065 Mpc

D_A in cascade: D_A_cascade(z_*) = c/H_0_cascade * integral
  H_0_cascade = 73
  integral = same as LCDM? (Same Omega_m_eff at low z)
  D_A_cascade = (c/73) * integral
  
  vs LCDM:
  D_A_LCDM = (c/67.4) * integral
  
  D_A_cascade / D_A_LCDM = 67.4/73 = 0.923

So theta_*_cascade = r_s_cascade / D_A_cascade
                  = (42 * 144.4) / (0.923 * D_A_LCDM)
                  = 42 / 0.923 * 144.4 / D_A_LCDM
                  = 45.5 * 0.01041
                  = 0.474

So cascade's predicted theta_* = 0.474, which is 45x larger than Planck's measured 0.01041.

This is HUGE. The cascade as currently formulated is INCOMPATIBLE with Planck's theta_* measurement, because the early-universe H(z) is too small (no DM, no DE at z > 1100 in cascade).

Hmm, this is a problem.

Wait, let me check the omega_b value. In Pantheon+ constraints, Omega_b ~ 0.05. But in cascade's picture, 5% of the universe is "matter" (which is baryons in cascade), so Omega_b_cascade = 0.05.

OK so the cascade's early universe has:
  - Photons + neutrinos: Omega_r = 9e-5
  - Baryons: Omega_b = 0.05
  - NO DM
  - NO DE
  - "Lambda" or "DE" term: 1 - 0.05 - 9e-5 = 0.9499

Wait, I forgot the 0.9499! If the cascade has H_0 = 73 and total
Omega = 1, and at z=0 it has 5% matter, 27% DM, 68% DE, then at
z=0: H(0) = H_0 * sqrt(Omega_m + Omega_DM + Omega_DE) = H_0 * 1 = H_0.
At z=1100 in cascade, the "Omega_DE" term might be different.

Actually, in cascade: 68% DE at z=0, but DE comes from the 4D event's
antigravity projection. At z=1100, the projection is from 4D time = some
specific value. Is the projection the same at z=1100 as at z=0?

The cascade says: 4D event projects to 3+1D continuously. So the
projection should be the same at all z. The "DE" contribution to H(z)
is Omega_L = 0.68, which is constant in z (just like LCDM's DE).

If cascade's Omega_L is constant at 0.68 (just like LCDM):
  At z=1100: H(1100) = 73 * sqrt(9e-5 * 1100^4 + 0.05 * 1100^3 + 0.68)
  = 73 * sqrt(1.32e8 + 6.65e7 + 0.68)
  = 73 * sqrt(1.99e8)
  = 73 * 14106
  = 1.03e6 km/s/Mpc

But that's the same as before (the 0.68 term is negligible at z=1100).

OK so the cascade at z=1100 has H = 1.03e6 with H_0 = 73 and
Omega_m = 0.05 (no DM), Omega_L = 0.68.

In LCDM at z=1100: H = 4.36e7 with H_0 = 67.4 and Omega_m = 0.32,
Omega_L = 0.68.

So cascade's H(1100) is 42x smaller than LCDM's H(1100).

This gives r_s_cascade = 42 * r_s_LCDM = 42 * 144.4 = 6065 Mpc.

That's absurd. r_s should be around 144 Mpc, not 6065 Mpc.

So Mechanism L is BUSTED in its simplest form.

The cascade CANNOT have H_0 = 73 at all z and match Planck's theta_*.

Unless the cascade has some additional physics at high z that makes
H(z) similar to LCDM at z=1100.

What could the cascade add? Let me think:

Option 1: The cascade has 32% effective matter at all z, not just at
low z. So at z=1100, Omega_m_eff = 0.32, not 0.05.

But this contradicts the cascade's picture: 2D universes are created
by 3+1D events, so DM only exists at low z.

Option 2: The cascade has additional radiation at high z.
E.g., if 4D event's "creation" at z=1100 is itself a high-energy event
that adds radiation.

Option 3: The cascade has Omega_L_4d that's not constant. Maybe at
z > 1100, the projection creates more "Lambda" than at z = 0.

Option 4: The cascade's H_0 is NOT 73 at all z. Maybe the cascade's
H_0 is 73 at z = 0 but smaller at high z (like Mechanism B/F predicted).

But B/F was rejected.

Option 5: The cascade's r_s is just different. Then theta_* would be
different from 0.01041. But Planck measured 0.01041.

So if Planck's theta_* = 0.01041 is a hard measurement, and cascade's
r_s = 6065 Mpc (using H_0 = 73), then D_A_cascade must be:
  D_A_cascade = r_s_cascade / theta_* = 6065 / 0.01041 = 582,613 Mpc

For comparison, D_A_LCDM = c/67.4 * integral
With integral = ... let me compute.

D_A(z_*) = c/H_0 * integral_0^z_* dz/E(z)
For z_* = 1089 in LCDM with H_0 = 67.4, Omega_m = 0.315, Omega_L = 0.685:
  integral_0^1089 of dz/sqrt(0.315 (1+z)^3 + 0.685)
  
  At z = 0: 1/sqrt(1) = 1
  At z = 1: 1/sqrt(0.315*8 + 0.685) = 1/sqrt(3.205) = 0.559
  At z = 10: 1/sqrt(0.315*1331 + 0.685) = 1/sqrt(420) = 0.049
  At z = 100: 1/sqrt(0.315*1e6 + 0.685) = 1/sqrt(315000) = 0.0018
  At z = 1000: 1/sqrt(0.315*1e9 + 0.685) = 1/sqrt(3.15e8) = 5.6e-5
  At z = 1089: 1/sqrt(0.315*1.29e9 + 0.685) = 1/sqrt(4.06e8) = 4.97e-5
  
  Approximating integral by trapezoidal rule on a coarse grid:
  
  z: 0, 1, 10, 100, 1000, 1089
  1/E: 1, 0.559, 0.049, 0.0018, 5.6e-5, 4.97e-5
  dz: 0-1, 1-10, 10-100, 100-1000, 1000-1089
  integrand*dz:
    0-1: 0.5 * (1+0.559) * 1 = 0.78
    1-10: 0.5 * (0.559+0.049) * 9 = 2.74
    10-100: 0.5 * (0.049+0.0018) * 90 = 2.29
    100-1000: 0.5 * (0.0018+5.6e-5) * 900 = 0.835
    1000-1089: 0.5 * (5.6e-5+4.97e-5) * 89 = 0.0047
    
  Total: 0.78 + 2.74 + 2.29 + 0.835 + 0.0047 = 6.65

D_A_LCDM(1089) = (c/67.4) * 6.65 = (3e5/67.4) * 6.65 = 4451 * 6.65 = 29,600 Mpc

Hmm wait, that doesn't match the standard 13,800 Mpc for D_A(1089).
Let me recompute.

Actually, the integral I computed gives 1/E integrated, but the
integral should be from 0 to z_*, not from z_* to infinity. And the
correct formula is:
  D_A(z_*) = (c/H_0) / (1+z_*) * integral_0^{z_*} dz / E(z)

Wait, no. The luminosity distance is:
  d_L(z) = (1+z) * (c/H_0) * integral_0^z dz' / E(z')
  d_A(z) = d_L / (1+z)^2 = (c/H_0) / (1+z) * integral

For z_* = 1089:
  d_A(1089) = (c/H_0) / 1090 * integral
            = (c/67.4) / 1090 * 6.65
            = 4451 / 1090 * 6.65
            = 4.083 * 6.65
            = 27.16 (in units of c/H_0)
            
  c/H_0 = c/67.4 = 3e5/67.4 = 4451 Mpc
  
  d_A(1089) = 27.16 * 4451 Mpc = 120,889 Mpc

That's 120 Gpc. Standard value for D_A(1089) is about 14 Gpc.

I'm making an error. Let me look up the standard formula.

D_A(z) = c / (H_0 (1+z)) * integral_0^z dz' / H(z') / H_0
       = c / (H_0 (1+z)) * integral_0^z dz' / E(z')

where E(z) = H(z)/H_0.

For LCDM, E(z) = sqrt(Omega_m (1+z)^3 + Omega_L)
For z = 1089: E(z) = sqrt(0.315 * 1100^3 + 0.685) = sqrt(4.19e11) = 6.47e5

integral_0^1089 dz / E(z):
  At z=1089, E is 6.47e5, so dz/E = dz/6.47e5
  Most of the integral is at LOWER z where E is smaller.
  
  Let me redo with finer grid:
  z: 0, 0.1, 0.5, 1, 2, 5, 10, 50, 100, 500, 1089
  E: 1, sqrt(0.315*1.331+0.685)=1.057, sqrt(0.315*3.375+0.685)=1.46, sqrt(0.315*8+0.685)=1.79, sqrt(0.315*27+0.685)=3.05, sqrt(0.315*216+0.685)=8.34, sqrt(0.315*1331+0.685)=20.5, sqrt(0.315*1.32e5+0.685)=204, sqrt(0.315*1.05e6+0.685)=575, sqrt(0.315*1.32e8+0.685)=6450, sqrt(0.315*1.29e9+0.685)=63800
  1/E: 1, 0.946, 0.685, 0.559, 0.328, 0.120, 0.0488, 0.0049, 0.00174, 0.000155, 1.57e-5
  dz: 0.1, 0.4, 0.5, 1, 3, 5, 40, 50, 400, 589
  integrand*dz:
    0-0.1: 0.5*(1+0.946)*0.1 = 0.0973
    0.1-0.5: 0.5*(0.946+0.685)*0.4 = 0.326
    0.5-1: 0.5*(0.685+0.559)*0.5 = 0.311
    1-2: 0.5*(0.559+0.328)*1 = 0.444
    2-5: 0.5*(0.328+0.120)*3 = 0.672
    5-10: 0.5*(0.120+0.0488)*5 = 0.422
    10-50: 0.5*(0.0488+0.0049)*40 = 1.074
    50-100: 0.5*(0.0049+0.00174)*50 = 0.166
    100-500: 0.5*(0.00174+0.000155)*400 = 0.379
    500-1089: 0.5*(0.000155+1.57e-5)*589 = 0.0508
  Total: 0.0973 + 0.326 + 0.311 + 0.444 + 0.672 + 0.422 + 1.074 + 0.166 + 0.379 + 0.0508 = 3.94

D_A(1089) = c/H_0 / 1090 * 3.94 = 4451/1090 * 3.94 = 4.083 * 3.94 = 16.09 (in c/H_0 units)
         = 16.09 * 4451 Mpc = 71,617 Mpc

Standard value: 14,000 Mpc. So I'm still off by a factor of 5.

Oh wait, the issue is that at high z, the integrand is so small that
my coarse grid is missing it. Let me think again.

Actually, the standard D_A(1089) is 14,000 Mpc, so the integral I should
get is:
  integral = D_A * 1090 / c * H_0 = 14000 * 1090 / 4451 = 3427
  
But I computed 3.94. So I need to check my computation.

Oh! I see my error. The integral should be the integral of 1/E(z),
not the integral of dz * 1/E(z). My trapezoidal sums ARE the latter,
not the former. Let me re-examine.

Wait, my trapezoidal IS integrating 1/E(z) * dz, which is what I want.
And I got 3.94. But the correct value should be around 3427?

Oh! The integral 1/E(z) at z = 1089 is 1/63800 = 1.57e-5.
But at z = 500, 1/E(z) = 0.000155.
The integral from 500 to 1089: about 0.5 * (0.000155 + 1.57e-5) * 589
                           = 0.05 (my calculation)
                           
That's only 0.05, not 1.

Hmm, the issue is that 1/E at z=1089 is much smaller than at z=500.
So 1/E is rapidly decreasing with z. The bulk of the integral is at LOW z.

Let me check: integral from 0 to 1 of dz/E(z):
  0-1: 0.5*(1+0.559)*1 = 0.78 (from my coarse grid above)
  This is most of the integral.

Integral from 1 to 5: 0.5*(0.559+0.120)*4 = 1.36
Integral from 5 to 10: 0.5*(0.120+0.0488)*5 = 0.42
Integral from 10 to 100: ~1.07 + 0.17 = 1.24
Integral from 100 to 1089: ~0.38 + 0.05 = 0.43

Total: 0.78 + 1.36 + 0.42 + 1.24 + 0.43 = 4.23

So integral ~ 4.2, and D_A = (c/H_0)/1090 * 4.2 = 4.083 * 4.2 * 4451 Mpc
                                     = 17.15 * 4451 = 76,335 Mpc
                                     
That's still 5x the standard 14,000 Mpc.

I think I have an error in the formula. Let me look up.

Actually, the correct angular diameter distance is:
  D_A(z) = (c / H_0) * S_k(integral_0^z dz' / E(z'))

For flat universe: S_k(x) = x
  D_A(z) = (c / H_0) * integral_0^z dz' / E(z')
  
  Wait, but I had a (1+z) factor before. Let me check.
  
  The FLRW metric: ds^2 = -c^2 dt^2 + a^2(t) [dr^2/(1-kr^2) + r^2 dOmega^2]
  Comoving distance: chi(z) = integral_0^z c dz' / H(z')
  Angular diameter distance: D_A(z) = S_k(chi(z)) / (1+z) = chi(z) / (1+z) for flat
  Luminosity distance: D_L(z) = (1+z) * chi(z)

So:
  chi(z) = (c/H_0) * integral_0^z dz' / E(z')
  D_A(z) = chi(z) / (1+z) = (c/H_0) / (1+z) * integral_0^z dz' / E(z')

For z = 1089:
  chi(1089) = (c/67.4) * 4.2 = 4451 * 4.2 = 18,694 Mpc
  D_A(1089) = chi(1089) / 1090 = 18,694 / 1090 = 17.15 Mpc
  
  Wait, that doesn't have units of Mpc. Let me check.

c/H_0 with H_0 in km/s/Mpc:
  c/H_0 = 3e5 km/s / 67.4 km/s/Mpc = 4451 Mpc (units work)
  integral is dimensionless
  chi = 4451 Mpc * 4.2 = 18,694 Mpc (correct)
  D_A = 18,694 / 1090 Mpc = 17.15 Mpc

But standard value is 14,000 Mpc. So my integral is 5x too small.

Wait, looking up the standard D_A(1089):
  https://arxiv.org/abs/1502.01589
  D_A(z_*) = 14,094 Mpc (for Planck best-fit LCDM)
  
And the integral of 1/E(z) from 0 to 1089 is...
  
Let me check: chi(1089) = D_A * 1090 = 14,094 * 1090 = 15,362,460 Mpc
   (c/H_0) * integral = 15,362,460
   integral = 15,362,460 / 4451 = 3452

So integral ~ 3452, not 4.2. Off by a factor of ~820.

OH! I see my error. I confused 1/E(z) with the integrand. Let me recheck.

For z = 1089, E(z) = sqrt(0.315 * 1100^3 + 0.685)
                   = sqrt(4.19e11)
                   = 647,500
So 1/E(z) at z = 1089 is 1/647500 = 1.54e-6

Not 1.57e-5! I was off by a factor of 10. Let me recompute the grid:
  z: 0, 0.1, 0.5, 1, 2, 5, 10, 50, 100, 500, 1089
  E: 1, 1.057, 1.46, 1.79, 3.05, 8.34, 20.5, 204, 575, 6450, 647500
  1/E: 1, 0.946, 0.685, 0.559, 0.328, 0.120, 0.0488, 0.0049, 0.00174, 0.000155, 1.54e-6
  
So at z = 1089, 1/E = 1.54e-6. At z = 500, 1/E = 0.000155.

Integral from 500 to 1089:
  0.5 * (0.000155 + 1.54e-6) * 589 = 0.046

Hmm, still about 0.05. The integral isn't dominated by high z.

Let me check: at z=0, 1/E=1. At z=1, 1/E=0.559. At z=10, 1/E=0.0488.
At z=100, 1/E=0.00174.

So the integral from 0 to 100 should be:
  0-1: ~0.78
  1-10: ~0.5*(0.559+0.0488)*9 = 2.74
  10-100: ~0.5*(0.0488+0.00174)*90 = 2.276
  Total 0-100: 5.8

But this is 5.8, not 3452. So my integral is way off by a factor of ~600.

Let me check: D_A(1089) is supposed to be 14,094 Mpc.
chi(1089) = D_A * 1090 = 14,094 * 1090 = 15.36 million Mpc
chi/H_0^-1 = chi/(c/H_0) = 15.36e6 / 4451 = 3452 (dimensionless)

So the dimensionless integral of dz/E(z) from 0 to 1089 should be 3452.

But I computed 4.2. Off by factor 800.

There must be a unit error. Let me look at chi(z) carefully.

chi(z) = integral_0^z c dz' / H(z')
       = c * integral_0^z dz' / (H_0 * E(z'))
       = (c / H_0) * integral_0^z dz' / E(z')

For LCDM, H_0 = 67.4 km/s/Mpc, c = 3e5 km/s.
  c/H_0 = 3e5 / 67.4 = 4451 Mpc
  
At z = 1, chi(1) = (c/H_0) * integral_0^1 dz/E(z)
  integral_0^1 of 1/E = 0.78 (from trapezoidal)
  chi(1) = 4451 * 0.78 = 3472 Mpc

Standard chi(1) for LCDM is about 3400 Mpc. OK so that matches.

At z = 1089:
  integral should be much larger because we're integrating to 1089
  But the integrand 1/E(z) decreases as z increases.
  
  Let me check: at z = 100, 1/E = 0.00174
                at z = 1000, 1/E = 1.54e-6
                at z = 1089, 1/E = 1.54e-6
                
  Integral from 100 to 1089:
    0.5 * (0.00174 + 1.54e-6) * 989 = 0.86
  
  Integral from 0 to 100: ~5.8
  Integral from 100 to 1089: ~0.86
  Total: 6.66

  chi(1089) = 4451 * 6.66 = 29,643 Mpc
  
  D_A(1089) = 29,643 / 1090 = 27.2 Mpc

But standard D_A(1089) is 14,094 Mpc. So I'm off by a factor of 500.

Wait, the standard D_A(1089) = 14,094 Mpc gives chi(1089) = 14,094 * 1090 = 15.36e6 Mpc.
And chi(1089)/(c/H_0) = 15.36e6 / 4451 = 3452.

So the integral of 1/E(z) from 0 to 1089 should be 3452, not 6.66.

But I computed 6.66. So I'm off by 500.

Hmm, let me sanity check with z = 0.1:
  integral_0^0.1 of 1/E(z) dz = 0.5*(1+0.946)*0.1 = 0.097
  chi(0.1) = 4451 * 0.097 = 432 Mpc
  Standard chi(0.1) for LCDM is ~430 Mpc. So my computation matches.

At z = 1: chi(1) ~ 3470 Mpc, standard is 3400. Close enough.

At z = 10: chi(10) = 4451 * 7.6 = 33,800 Mpc.
  Standard chi(10) for LCDM is ~ 10,000 Mpc? Let me check.
  Actually, with H_0 = 67.4, chi(10) = integral c dz/H(z)
  At z = 10, H(z) = 67.4 * sqrt(0.315*1331 + 0.685) = 67.4*20.5 = 1382 km/s/Mpc
  c/H(10) = 3e5/1382 = 217 Mpc
  chi(10) should be integral of c/H(z) from 0 to 10
  At z=0: c/H = 4451
  At z=10: c/H = 217
  Approximate: chi(10) ~ 5000-10000 Mpc. (Rough)
  
  Using trapezoidal with my grid:
  chi(10) = (c/H_0) * integral = 4451 * 0.97+0.33+0.44+0.67+0.42 = 4451 * 2.83 = 12,600 Mpc
  
  Hmm, this is higher than 5000-10000. Let me redo with more z values.

Actually wait, I think my issue is that I have a factor wrong. Let me look
up the correct formula for D_A:

D_A(z) = c / (H_0 (1+z)) * integral_0^z dz' / E(z')

OK so D_A(1089) = c / (H_0 * 1090) * integral_0^1089 dz' / E(z')

= (c / H_0) / 1090 * integral
= 4451 / 1090 * integral
= 4.083 * integral

For D_A(1089) = 14,094 Mpc:
  integral = 14,094 / 4.083 = 3451

So integral = 3451. My trapezoidal gives 6.66. Off by factor 518.

Wait... 6.66 * 518 = 3450. Hmm.

Oh! I see. The 1/E(z) at z=1089 is 1.54e-6. But this is the
DIMENSIONLESS 1/E. Let me recheck:

E(z) = H(z)/H_0
H(z) = H_0 * sqrt(Omega_m (1+z)^3 + Omega_L)
E(z=1089) = sqrt(0.315 * 1100^3 + 0.685) = sqrt(4.19e11) = 6.47e5
1/E(z=1089) = 1.54e-6

At z=1, E = sqrt(0.315*8 + 0.685) = sqrt(3.205) = 1.79
1/E(z=1) = 0.559

Hmm, those are correct.

integral_0^1089 dz/E(z) should be around 3451.

But my trapezoidal sum is 6.66. So my sum is way off.

Let me check: maybe I need finer z values.

At z = 1000, E = sqrt(0.315*1.001e9 + 0.685) = sqrt(3.15e8) = 17748
1/E = 5.63e-5

At z = 1089, E = sqrt(0.315 * 1.29e9 + 0.685) = sqrt(4.06e8) = 20149
1/E = 4.96e-5

At z = 500, E = sqrt(0.315 * 1.26e8 + 0.685) = sqrt(3.96e7) = 6293
1/E = 1.59e-4

At z = 100, E = sqrt(0.315 * 1.01e6 + 0.685) = sqrt(3.18e4) = 178.3
1/E = 5.61e-3

Wait, 1/E(z=100) = 1/178.3 = 0.00561

But earlier I had 1/E(z=100) = 0.00174. Let me recheck.
At z=100: 0.315 * 101^3 = 0.315 * 1,030,301 = 324,545
Plus 0.685 = 324,546
E(100) = sqrt(324,546) = 569.7
1/E(100) = 1/569.7 = 1.755e-3

OK so 1/E(100) = 1.755e-3. My earlier 0.00174 was right.

At z = 200: 0.315 * 201^3 = 0.315 * 8.12e6 = 2.56e6
E(200) = sqrt(2.56e6) = 1600
1/E(200) = 6.25e-4

At z = 500: 0.315 * 501^3 = 0.315 * 1.257e8 = 3.96e7
E(500) = 6292
1/E(500) = 1.59e-4

At z = 1000: 0.315 * 1001^3 = 0.315 * 1.003e9 = 3.16e8
E(1000) = 17,776
1/E(1000) = 5.63e-5

At z = 1089: 0.315 * 1090^3 = 0.315 * 1.295e9 = 4.08e8
E(1089) = 20,200
1/E(1089) = 4.95e-5

OK so 1/E ranges from 0.5 (at z=0) down to 4.95e-5 (at z=1089).

Now let me compute the integral from 100 to 1089 with finer grid:
  z: 100, 200, 300, 500, 700, 900, 1089
  1/E: 1.76e-3, 6.25e-4, 3.5e-4, 1.59e-4, 9.4e-5, 6.2e-5, 4.95e-5

  100-200: 0.5 * (1.76e-3 + 6.25e-4) * 100 = 0.119
  200-300: 0.5 * (6.25e-4 + 3.5e-4) * 100 = 0.0488
  300-500: 0.5 * (3.5e-4 + 1.59e-4) * 200 = 0.0509
  500-700: 0.5 * (1.59e-4 + 9.4e-5) * 200 = 0.0253
  700-900: 0.5 * (9.4e-5 + 6.2e-5) * 200 = 0.0156
  900-1089: 0.5 * (6.2e-5 + 4.95e-5) * 189 = 0.0103

  Total 100-1089: 0.119 + 0.0488 + 0.0509 + 0.0253 + 0.0156 + 0.0103 = 0.270

So integral from 100 to 1089 is about 0.27, not 0.86 or 6.66. So my
earlier 6.66 was too high. And it's still way less than 3451.

Hmm. Let me look up a calculator or formula.

Oh! I think the issue is that 1/E at low z is large (around 1), but the
integral from 0 to 100 is bounded.

At z=0, 1/E=1.
At z=100, 1/E=1.76e-3.

The integral from 0 to 100 should be on the order of 1 (not 5.8).
Let me redo with finer grid:
  z: 0, 0.01, 0.1, 0.3, 0.5, 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100
  1/E: 1, 0.99, 0.94, 0.85, 0.78, 0.56, 0.33, 0.23, 0.12, 0.077, 0.049, 0.018, 0.011, 5.0e-3, 3.0e-3, 1.76e-3

  0-0.01: 0.5 * (1 + 0.99) * 0.01 = 0.00995
  0.01-0.1: 0.5 * (0.99+0.94) * 0.09 = 0.0869
  0.1-0.3: 0.5 * (0.94+0.85) * 0.2 = 0.179
  0.3-0.5: 0.5 * (0.85+0.78) * 0.2 = 0.163
  0.5-1: 0.5 * (0.78+0.56) * 0.5 = 0.335
  1-2: 0.5 * (0.56+0.33) * 1 = 0.445
  2-3: 0.5 * (0.33+0.23) * 1 = 0.28
  3-5: 0.5 * (0.23+0.12) * 2 = 0.35
  5-7: 0.5 * (0.12+0.077) * 2 = 0.197
  7-10: 0.5 * (0.077+0.049) * 3 = 0.189
  10-20: 0.5 * (0.049+0.018) * 10 = 0.335
  20-30: 0.5 * (0.018+0.011) * 10 = 0.145
  30-50: 0.5 * (0.011+5.0e-3) * 20 = 0.16
  50-70: 0.5 * (5.0e-3+3.0e-3) * 20 = 0.08
  70-100: 0.5 * (3.0e-3+1.76e-3) * 30 = 0.0714

  Total 0-100: 0.00995 + 0.0869 + 0.179 + 0.163 + 0.335 + 0.445 + 0.28 + 0.35 + 0.197 + 0.189 + 0.335 + 0.145 + 0.16 + 0.08 + 0.0714 = 3.026

So integral from 0 to 100 ~ 3.0. Not 5.8 or 3451.

Adding 100-1089 = 0.27, total integral = 3.30.

But standard integral should be 3451. So I'm off by a factor of 1045.

Wait... 3451/3.30 = 1045. Hmm.

Let me check: chi(1) for LCDM with H_0 = 67.4:
  integral_0^1 dz/E = 0.78 (from above)
  chi(1) = (c/H_0) * 0.78 = 4451 * 0.78 = 3472 Mpc

Standard chi(1) for LCDM with H_0 = 67.4 is 3400 Mpc. So my computation is correct.

So chi(1089) = 4451 * 3.30 = 14,688 Mpc.
D_A(1089) = 14,688 / 1090 = 13.48 Mpc? 

That doesn't make sense. D_A is in Mpc.

Let me check units:
  chi(1089) = 14,688 Mpc
  D_A(1089) = chi(1089) / (1+z) = 14,688 / 1090 = 13.48 Mpc

But standard D_A(1089) is 14,094 Mpc. So I'm off by factor ~1000.

Hmm, let me sanity check by trying chi(1):
  chi(1) = 4451 * 0.78 = 3472 Mpc
  D_A(1) = chi(1) / 2 = 1736 Mpc
  Standard D_A(1) for LCDM is about 1700 Mpc. 

And chi(10) for LCDM:
  integral_0^10 = 0.00995+0.0869+0.179+0.163+0.335+0.445+0.28+0.35+0.197+0.189 = 2.234
  chi(10) = 4451 * 2.234 = 9943 Mpc
  D_A(10) = 9943 / 11 = 904 Mpc
  Standard D_A(10) for LCDM is about 920 Mpc. So my computation is correct.

So at z = 10, chi ~ 10,000 Mpc, D_A ~ 900 Mpc. Correct.
At z = 1089, chi ~ 14,000 Mpc, D_A ~ 13 Mpc. But standard says D_A ~ 14,000 Mpc.

That can't be right. Let me look up the standard value.

Actually, looking at Planck 2018 results: D_A(1089) = 14,094 Mpc.
https://arxiv.org/abs/1807.06209
Table 2: D_A(z_*) = 14,094 ± 65 Mpc.

So D_A(1089) is 14,094 Mpc, NOT 14 Mpc. I had a factor of 1000 error somewhere.

Let me redo the calculation very carefully.

chi(z) = (c/H_0) * integral_0^z dz' / E(z')

For z = 1089:
  c/H_0 = 3e5/67.4 = 4451 Mpc (this is correct)
  integral_0^1089 dz'/E(z') = ??
  
The integral should make chi(1089) = 14,094 * 1090 = 15,362,460 Mpc
So integral = 15,362,460 / 4451 = 3451

So integral = 3451. I computed 3.30. Off by factor 1045.

Oh wait! I bet I made an error in E(z). Let me recompute.

E(z) = H(z)/H_0
H(z) = H_0 * sqrt(Omega_m (1+z)^3 + Omega_L)
E(z) = sqrt(Omega_m (1+z)^3 + Omega_L)

For z = 1089:
  Omega_m = 0.315
  Omega_L = 0.685
  (1+z) = 1090
  (1+z)^3 = 1090^3 = 1.295e9
  Omega_m (1+z)^3 = 0.315 * 1.295e9 = 4.08e8
  Omega_m (1+z)^3 + Omega_L = 4.08e8 + 0.685 = 4.08e8
  E(1089) = sqrt(4.08e8) = 20,200
  
So E(1089) = 20,200. And 1/E(1089) = 4.95e-5.

Hmm, that's what I had. So why is the integral so small?

Actually wait. At z = 0:
  E(0) = sqrt(0.315 + 0.685) = sqrt(1) = 1
  1/E(0) = 1

At z = 1:
  E(1) = sqrt(0.315 * 8 + 0.685) = sqrt(2.52 + 0.685) = sqrt(3.205) = 1.79
  1/E(1) = 0.559

So the integral should be on the order of z, not 1. Specifically,
the integral of 1/E from 0 to 1089 is on the order of... hmm.

Let me think: if E(z) ~ (1+z)^(3/2) at high z, then 1/E(z) ~ (1+z)^(-3/2).
Integral from 0 to z of (1+z')^(-3/2) dz' = -2 [(1+z')^(-1/2)]_0^z
                                          = 2 [1 - (1+z)^(-1/2)]
                                          = 2 at z = infinity.
                                          
So the integral converges to 2 as z -> infinity (for matter-dominated).
Adding DE: integral converges to ~3 (in matter + DE universe).

But the standard integral I should get is 3451. So the integral isn't 3,
it's 3451. That means I'm missing a factor.

OH! I see my error. The integral is 1/E(z) dz, but I was integrating
1/E(z) dz. Let me re-examine my formula:

chi(z) = (c/H_0) * integral_0^z dz' / E(z')

So the integrand is 1/E(z') (no c, no H_0 inside the integral). And
I multiply by c/H_0 outside.

c/H_0 = 4451 Mpc.

For chi(1089) = 14,094 * 1090 = 15,362,460 Mpc
We need integral = 15,362,460 / 4451 = 3451.

But I computed 3.30. So I'm off by 1045.

Hmm. Let me check chi(0.1) for sanity:
  integral_0^0.1 = 0.00995 + 0.0869 = 0.097
  chi(0.1) = 4451 * 0.097 = 432 Mpc
  Standard chi(0.1) for LCDM = 430 Mpc. So my computation is correct.

So at z = 0.1, my integral is 0.097. That matches standard.

At z = 1089, my integral is 3.30. But standard is 3451.

So somewhere between z = 0.1 and z = 1089, the integral must increase
by 1000x. But 1/E(z) is decreasing, so the integral should only
increase by ~3 (the asymptotic value).

So my computation must be wrong somewhere.

Oh!! I just realized: I was computing D_A wrong.

D_A(z) = (1/(1+z)) * chi(z)

For z = 1089:
  D_A(1089) = chi(1089) / 1090

If chi(1089) is 14,094 * 1090 = 15,362,460 Mpc, then D_A = 14,094 Mpc. ✓

But the standard value of D_A(1089) is 14,094 Mpc. So chi(1089) = 15,362,460 Mpc.

For chi(1089) to be 15,362,460 Mpc, and c/H_0 = 4451 Mpc, the integral
must be 3451.

So integral_0^1089 dz/E(z) = 3451.

But I computed 3.30. So I have a factor of 1045 error.

Wait... let me look at this differently. What if c is not 3e5 km/s?

c = 299,792.458 km/s. So 3e5 is correct (approximately).

And H_0 = 67.4 km/s/Mpc. So c/H_0 = 299792.458/67.4 = 4448 Mpc.

OK so c/H_0 = 4448 Mpc. Close to 4451.

Hmm, but my integral computation is way off. Let me look at what 1/E(1089) should be.

E(1089) = sqrt(0.315 * 1090^3 + 0.685) = sqrt(0.315 * 1.295e9) = sqrt(4.08e8) = 20,200

1/E(1089) = 4.95e-5.

This is very small. The integral of a small number from 100 to 1089 is at most 1089 * 4.95e-5 = 0.054. So the integral from 100 to 1089 is at most 0.054, plus 3 from 0 to 100, total ~ 3.05. 

So the integral of 1/E(z) from 0 to 1089 is ~3, not 3451.

But standard says it should be 3451. So either:
1. My computation of E(1089) is wrong
2. My formula for chi(z) is wrong
3. The standard value is wrong

Let me recheck standard chi(1089):
  chi(z) = (c/H_0) * integral_0^z dz' / E(z')
  
  For z = 1089, the integral of 1/E is ~3 in matter-dominated era.
  So chi(1089) ~ 4451 * 3 = 13,353 Mpc.
  
  D_A(1089) = chi(1089) / 1090 = 12.25 Mpc.
  
  But standard says D_A(1089) = 14,094 Mpc.
  
  So 14,094 Mpc * 1090 = 15,362,460 Mpc = chi(1089).
  15,362,460 / 4451 = 3451 = integral.

So the integral MUST be 3451. But I can't see how.

OH WAIT! I think I see my confusion. The integral I should be computing
is not 1/E(z) but something else.

Let me re-derive the formula.

d_C(z) = comoving distance to redshift z
       = integral_0^z c dz' / H(z')
       = (c/H_0) * integral_0^z dz' / E(z')

where E(z) = H(z)/H_0.

For z = 1089 in LCDM, this should be ~ 14,000 Mpc.
14,000 Mpc / 4451 Mpc = 3.15.

So the integral is 3.15, not 3451. ✓ My computation is correct!

So d_C(1089) ~ 14,000 Mpc.
And D_A(1089) = d_C / (1+z) = 14,000 / 1090 = 12.85 Mpc.

But Planck says D_A(1089) = 14,094 Mpc. That's MUCH LARGER.

Wait, let me double-check Planck's value.

From Planck 2018 paper (https://arxiv.org/abs/1807.06209, Table 2):
  D_A(z_*) = 14,094 ± 65 Mpc

Hmm, but my calculation says D_A(1089) = 12.85 Mpc. So Planck's value
is 1000x larger?

Let me look at this more carefully. Actually, I wonder if I have a unit
confusion. Let me try to compute d_A(1) for LCDM:

d_A(1) = d_C(1) / 2 = 3472 / 2 = 1736 Mpc
Standard d_A(1) for LCDM: ~1700 Mpc. ✓ Matches.

d_A(10) = d_C(10) / 11 = 9943 / 11 = 904 Mpc
Standard d_A(10) for LCDM: ~900 Mpc. ✓ Matches.

d_A(100) = d_C(100) / 101 = ?
d_C(100) = 4451 * (integral 0-100) = 4451 * 3.0 = 13,353 Mpc
d_A(100) = 13,353 / 101 = 132 Mpc
Standard d_A(100) for LCDM: ~130 Mpc. ✓ Matches.

d_A(1000) = d_C(1000) / 1001
d_C(1000) = 4451 * 3.3 = 14,688 Mpc
d_A(1000) = 14,688 / 1001 = 14.7 Mpc

d_A(1089) = d_C(1089) / 1090
d_C(1089) = 4451 * 3.30 = 14,688 Mpc
d_A(1089) = 14,688 / 1090 = 13.5 Mpc

So d_A(1089) = 13.5 Mpc, NOT 14,094 Mpc.

But Planck says d_A(1089) = 14,094 Mpc. Off by factor ~1000.

So either Planck is reporting d_C(1089) (and calling it d_A by mistake),
or my formula is wrong, or the standard value of d_A(1089) is actually 13.5 Mpc.

Let me look this up more carefully.

Actually, I think I see my confusion. The "D_A" in cosmology papers is
often the comoving angular diameter distance, defined as:
  D_M(z) = (1+z) * D_A(z) = d_C(z)

If D_A(z_*) = 14,094 Mpc is the COMOVING angular diameter distance
(aka D_M), then D_A(physical) = 14,094 / 1090 = 12.93 Mpc. And my
computation gives 13.5 Mpc. Close enough.

Actually wait, looking at Planck 2018 Table 2 more carefully:
"D_A(z_*) / Gpc" - so the value 14.094 is in Gpc, not Mpc!

14.094 Gpc = 14,094 Mpc. Yes!

Hmm. So if D_A(1089) = 14.094 Gpc = 14,094 Mpc, and my computation
gives 13.5 Mpc, then I'm off by factor 1000.

Wait, let me recompute. Maybe I have the H_0 convention wrong.

In Planck 2018, they use H_0 = 67.4 km/s/Mpc. And they report:
  D_A(z_*) = 14,094 Mpc (or 14.094 Gpc)

OK so that's D_A(1089) = 14,094 Mpc.

But my computation gives 13.5 Mpc. So I'm off by factor ~1000.

Let me double-check by computing D_C(1) for H_0 = 67.4:
  D_C(1) = (c/H_0) * integral_0^1 dz/E(z)
         = 4448 Mpc * 0.78
         = 3470 Mpc

Standard D_C(1) for H_0 = 67.4 is around 3400 Mpc. ✓

D_C(1089) = 4448 * 3.3 = 14,678 Mpc.

And D_A(1089) = D_C(1089) / 1090 = 13.5 Mpc.

But Planck says D_A(1089) = 14,094 Mpc.

Wait, maybe Planck's value of 14,094 Mpc is D_C(1089), not D_A(1089)?

Let me check. D_C(1089) for H_0 = 67.4 with my computation = 14,678 Mpc.
Planck: 14,094 Mpc. Close (within 4%).

So Planck's "D_A(z_*)" is actually D_C(z_*) = 14,094 Mpc.

That makes sense! D_C is the "comoving angular diameter distance",
which is the same as the comoving distance. And it's often what people
report as "D_A" because it doesn't include the (1+z) factor.

OK so my computation is correct, and Planck's D_A = 14,094 Mpc is the
comoving distance. The PHYSICAL angular diameter distance is 14,094/1090
= 12.93 Mpc.

Great, so my formula is right.

Now: r_s for cascade vs LCDM.

In LCDM:
  r_s = 144.4 Mpc (standard value)
  D_A(1089) = 14,094 Mpc (comoving) = 12.93 Mpc (physical)
  theta_* = r_s / D_A = 144.4 / 14,094 = 0.01025
  Planck measured: 0.01041 (close to my 0.01025)

For the cascade with H_0 = 73 and Omega_m = 0.05 (no DM at z=1100):
  H(1100) = 73 * sqrt(9e-5 * 1100^4 + 0.05 * 1100^3 + 0.68)
         = 73 * sqrt(1.32e8 + 6.65e7 + 0.68)
         = 73 * sqrt(1.99e8)
         = 73 * 14106
         = 1.03e6 km/s/Mpc
         
  H_LCDM(1100) = 67.4 * sqrt(0.315 * 1100^3 + 0.685)
              = 67.4 * sqrt(4.19e11 + 0.685)
              = 67.4 * 6.47e5
              = 4.36e7 km/s/Mpc
              
  Ratio: H_cascade(1100) / H_LCDM(1100) = 1.03e6 / 4.36e7 = 0.0236

  r_s = integral c_s / H(z) dz from z_* to inf
     ~ c / H(z_*) / z_* (for radiation-dominated era)
     So r_s ~ 1/H(z_*)
     
  r_s_cascade = r_s_LCDM * (H_LCDM(1100) / H_cascade(1100))
              = 144.4 * 1/0.0236
              = 6119 Mpc
              
  D_A_cascade(1089) (comoving) = (c/H_0_cascade) * integral
                              = (c/73) * 3.3
                              = 4107 * 3.3
                              = 13,553 Mpc
                              
  theta_*_cascade = r_s_cascade / D_A_cascade
                  = 6119 / 13,553
                  = 0.4515
                  
But Planck measured theta_* = 0.01041. So cascade predicts theta_* 43x too large.

This is a HUGE problem. The cascade as I've formulated it (no DM at
z = 1100, no DE at z = 1100) gives a theta_* that's 43 times larger
than Planck's measurement.

So Mechanism L is BUSTED in this form.

UNLESS the cascade has additional physics at z > 1100 that I'm missing.

Possible fix: maybe the cascade's "matter" at z = 1100 is not 5% baryons
only. Maybe the cascade's 2D universe creation happens at z > 1100 too.

But the cascade says 2D universes are created by 3+1D events, and 3+1D
is the universe we live in, so 2D creation happens at z < z_form (when
3+1D formed). z_form is around 0 to 1100.

Hmm. So this is a real problem for Mechanism L.

Let me think of other ways the cascade could resolve the tension:

A) The cascade has the same early universe as LCDM (32% matter, 68% DE).
   This contradicts the cascade's picture but gives the right theta_*.
   
B) The cascade has H_0 = 73 at low z, but ~67 at high z (Mechanism B/F).
   Rejected by Pantheon+.

C) The cascade's H_0 is 67.4 (same as Planck). Then the cascade
   doesn't have a "high H_0" issue, but it also doesn't explain the
   local H_0 = 73 from SH0ES.

D) The cascade accepts that H_0 is 67.4 (CMB-inferred) and 73 (local),
   and the cascade is consistent with this. Local H_0 is high because
   of local physics, not because the cascade has H_0 = 73 everywhere.

Hmm, this last option (D) is actually consistent! Let me think.

In the cascade:
  H_0 (the "true" expansion rate) is the 4D event's projection rate.
  This is what Planck would measure: H_0 = 67.4.
  
  But locally, we observe H_0 = 73 (SH0ES, distance ladder).
  Why? Because of local physics:
    - 2D universes in our region
    - Local void
    - Late-time effects
  
This is the "local physics" interpretation. The cascade has H_0 = 67.4
(the 4D event's projection rate), and local measurements give 73 due to
local 2D universe effects.

This is essentially Mechanism C (local bubble) recast in cascade terms.

Or it's Mechanism M (accept the tension).

Let me think about what's most natural for the cascade...

The cascade's H_0 should be a fundamental property of the 4D event.
If the cascade's H_0 is 67.4 (matching Planck), then local H_0 = 73
must come from something other than the 4D event's projection.

What could it be?
- 2D universes contribute DM. The 2D universe "back-projection" is
  cumulative over all of 3+1D's history. So the local H_0 might be
  affected by the local 2D universe density.
- If our region has more 2D universes (more activity, more stars, etc.),
  we have more DM in our region, and that affects local H_0.

So Mechanism L recast: H_0 is 67.4 (fundamental) at all z. Local H_0
is 73 due to local 2D universe over-density. SH0ES measures local H_0
in our region with high 2D density. CMB measures cosmic average H_0
(no local bias).

This is Mechanism C (local bubble) recast.

But wait, Pantheon+ best-fit H_0 = 73, NOT 67.4. So Pantheon+ agrees
with SH0ES, not with Planck.

If Pantheon+ measures the cosmic average (over 1588 SNe spanning z=0.01-1.5),
and Pantheon+ best-fit H_0 = 73, then the cosmic average H_0 is 73, not 67.4.

So Planck's H_0 = 67.4 is at odds with both local and Pantheon+ measurements.

Maybe Mechanism L is:
  - The CMB-inferred H_0 = 67.4 is an artifact of assuming LCDM
  - The "true" H_0 of the universe is 73
  - In the cascade model, CMB analysis gives H_0 = 73

But we showed this requires r_s_cascade = 133 Mpc (smaller than LCDM's
144.4 Mpc). The cascade has Omega_m at z=1100 = 0.05 (just baryons),
which makes H(1100) smaller, which makes r_s bigger, NOT smaller.

So this doesn't work.

UNLESS the cascade has additional "stuff" at z > 1100 that makes
H(1100) larger, not smaller.

What could that be? Maybe the cascade's 4D event created a much denser
universe at z = 1100? Or maybe the cascade has dark radiation?

OK this is getting too speculative. Let me just be honest:

The cascade's Mechanism L (re-interpret Planck's H_0 = 67.4 as
cascade-consistent) requires the cascade to have the same early
universe as LCDM. But the cascade's picture (no DM, no DE at z > 1100)
is fundamentally different from LCDM.

So Mechanism L doesn't naturally work for the cascade.

The honest options are:
1. Mechanism C: local bubble, with cascade's 2D universe density
2. Mechanism M: accept the tension
3. Mechanism I: late-time physics modification

Let me write this up.
"""

import math
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("MECHANISM L: RIGOROUS ANALYSIS (Planck re-analysis)")
    hr()

    print(f"\n  CLAIM: CMB H_0 = 67.4 is an artifact of assuming LCDM.")
    print(f"          In cascade, CMB analysis gives H_0 = 73.")
    print()
    print(f"  PLAN:")
    print(f"    Step 1: Re-derive Planck's theta_* measurement in cascade's model")
    print(f"    Step 2: Check if theta_* = 0.01041 is achievable with H_0 = 73")
    print(f"    Step 3: Determine what cascade's H_0 must be")

    print(f"\n\n  Step 1: How Planck infers H_0")
    print(f"  ----------------------------------------------------------------")
    print(f"  Planck measures theta_* = r_s(z_*) / D_A(z_*) = 0.01041")
    print()
    print(f"  r_s(z_*) = sound horizon at recombination")
    print(f"  r_s = integral c_s / H(z) dz from z_* to infinity")
    print(f"  At high z (z > 1100), H(z) ~ H_0 sqrt(Omega_m (1+z)^3 + Omega_L)")
    print()
    print(f"  D_A(z_*) = angular diameter distance to z_*")
    print(f"  D_A = (c/H_0) / (1+z_*) * integral_0_to_z* dz/E(z)")
    print()
    print(f"  Plan: at z_* = 1089, E(z_*) = sqrt(0.315 * 1090^3 + 0.685) = 20,200")
    print(f"        So 1/E is small at high z, integral is small.")

    print(f"\n\n  Step 2: H(z) at z = 1100 in cascade vs LCDM")
    print(f"  ----------------------------------------------------------------")
    print()
    print(f"  LCDM (H_0 = 67.4, Omega_m = 0.315, Omega_L = 0.685):")
    H_LCDM_1100 = 67.4 * math.sqrt(0.315 * 1100**3 + 0.685)
    print(f"    H(1100) = 67.4 * sqrt(0.315*1100^3 + 0.685)")
    print(f"           = 67.4 * sqrt(4.19e11)")
    print(f"           = {H_LCDM_1100:.3e} km/s/Mpc")
    print(f"    r_s_LCDM = 144.4 Mpc")
    print()
    print(f"  Cascade (H_0 = 73, Omega_b = 0.05, Omega_DM = 0, Omega_L = 0.68):")
    H_cascade_1100 = 73 * math.sqrt(9e-5 * 1100**4 + 0.05 * 1100**3 + 0.68)
    print(f"    H(1100) = 73 * sqrt(9e-5*1100^4 + 0.05*1100^3 + 0.68)")
    print(f"           = 73 * sqrt(1.99e8)")
    print(f"           = {H_cascade_1100:.3e} km/s/Mpc")
    print()
    print(f"  Ratio: H_cascade(1100) / H_LCDM(1100) = {H_cascade_1100/H_LCDM_1100:.4f}")
    print()
    print(f"  Cascade's H(1100) is {(H_LCDM_1100/H_cascade_1100):.1f}x SMALLER than LCDM's")
    print()
    
    # Compute r_s_cascade
    # r_s ~ 1/H(z_*) (rough scaling for radiation-dominated era)
    # More precisely: r_s ~ c_s / (H_0 sqrt(Omega_m (1+z)^3))
    r_s_LCDM = 144.4
    # r_s scales as 1/H(z_*), so cascade r_s is 1/(H_cascade/H_LCDM) times LCDM r_s
    r_s_cascade = r_s_LCDM * (H_LCDM_1100 / H_cascade_1100)
    print(f"  r_s_cascade = r_s_LCDM * (H_LCDM(1100) / H_cascade(1100))")
    print(f"             = {r_s_LCDM} * {H_LCDM_1100/H_cascade_1100:.1f}")
    print(f"             = {r_s_cascade:.1f} Mpc")
    print(f"  (That's way bigger than LCDM's 144.4 Mpc!)")

    print(f"\n\n  Step 3: D_A in cascade")
    print(f"  ----------------------------------------------------------------")
    # D_A(z_*) = (c/H_0) / (1+z_*) * integral
    # integral ~ 3.3 (computed above)
    c_kms = 3e5
    D_A_LCDM = (c_kms / 67.4) / 1090 * 3.30
    D_A_cascade = (c_kms / 73) / 1090 * 3.30
    print(f"  D_A(1089) for LCDM (H_0=67.4): {D_A_LCDM:.0f} Mpc")
    print(f"  D_A(1089) for cascade (H_0=73): {D_A_cascade:.0f} Mpc")
    print(f"  Cascade's D_A is {D_A_LCDM/D_A_cascade:.3f}x LCDM's D_A")

    print(f"\n\n  Step 4: theta_* in cascade")
    print(f"  ----------------------------------------------------------------")
    theta_star_LCDM = r_s_LCDM / D_A_LCDM
    theta_star_cascade = r_s_cascade / D_A_cascade
    print(f"  theta_*_LCDM = r_s_LCDM / D_A_LCDM")
    print(f"              = {r_s_LCDM} / {D_A_LCDM:.0f}")
    print(f"              = {theta_star_LCDM:.5f}")
    print(f"  Planck measured: 0.01041")
    print()
    print(f"  theta_*_cascade = r_s_cascade / D_A_cascade")
    print(f"                 = {r_s_cascade:.0f} / {D_A_cascade:.0f}")
    print(f"                 = {theta_star_cascade:.4f}")
    print()
    print(f"  Cascade predicts theta_* = {theta_star_cascade:.3f}, but Planck measured 0.01041")
    print(f"  Off by a factor of {theta_star_cascade/0.01041:.0f}!")
    print()
    print(f"  *** THIS DOESN'T WORK ***")
    print()
    print(f"  The cascade's early universe (no DM, no DE at z>1100) gives a")
    print(f"  much larger r_s than LCDM, which makes theta_* much bigger than")
    print(f"  Planck's measurement.")

    print(f"\n\n  Step 5: Why? The cascade's picture vs reality")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade says:")
    print(f"    - 4D event projects to 3+1D (DE-like effect)")
    print(f"    - 3+1D events project to 2D universes (DM-like effect)")
    print(f"  In cascade's natural picture:")
    print(f"    - DE only exists at z < z_form (where 3+1D formed)")
    print(f"    - DM only exists at z < z_form (where 2D universes were created)")
    print(f"  At z > 1100 (recombination), cascade has only baryons and radiation.")
    print()
    print(f"  But LCDM at z = 1100 has matter (baryons + DM) dominating.")
    print(f"  With Omega_m = 0.315 (vs cascade's 0.05), LCDM has 6x more 'mass'")
    print(f"  at z = 1100, so H_LCDM(1100) is sqrt(6) = 2.5x larger than")
    print(f"  H_cascade(1100) would be with just baryons.")
    print()
    print(f"  Wait, I said 42x. Let me recheck.")
    print(f"  LCDM: H ~ sqrt(0.315*1100^3 + 0.685)")
    print(f"  Cascade: H ~ sqrt(9e-5*1100^4 + 0.05*1100^3 + 0.68)")
    print()
    print(f"  At z = 1100, Omega_m(1+z)^3 >> Omega_L, so:")
    print(f"  LCDM: H ~ H_0 * sqrt(0.315*1100^3) = H_0 * sqrt(3.15e8) * sqrt(1100)")
    print(f"  Actually, H ~ H_0 * (1+z)^(3/2) * sqrt(Omega_m)")
    print()
    H_LCDM_1100_simple = 67.4 * 1100**1.5 * math.sqrt(0.315)
    H_cascade_1100_simple = 73 * 1100**1.5 * math.sqrt(0.05)
    print(f"  H_LCDM(1100) ~ 67.4 * 1100^1.5 * sqrt(0.315) = {H_LCDM_1100_simple:.3e}")
    print(f"  H_cascade(1100) ~ 73 * 1100^1.5 * sqrt(0.05) = {H_cascade_1100_simple:.3e}")
    print(f"  Ratio: H_cascade/H_LCDM = {H_cascade_1100_simple/H_LCDM_1100_simple:.3f}")
    print()
    print(f"  Cascade's H(1100) is {H_LCDM_1100_simple/H_cascade_1100_simple:.2f}x smaller than LCDM's")
    print(f"  Cascade's r_s is {(H_LCDM_1100_simple/H_cascade_1100_simple):.2f}x larger than LCDM's r_s")

    print(f"\n\n  Step 6: What would it take to make Mechanism L work?")
    print(f"  ----------------------------------------------------------------")
    print()
    print(f"  For theta_*_cascade = 0.01041, we need:")
    print(f"    r_s_cascade / D_A_cascade = 0.01041")
    print(f"  With D_A_cascade = (c/73) / 1090 * integral ~ 13,553 Mpc (using H_0=73):")
    print(f"    r_s_cascade = 0.01041 * 13,553 = 141 Mpc")
    print()
    print(f"  So r_s_cascade needs to be 141 Mpc (similar to LCDM's 144.4).")
    print(f"  But with H_0 = 73 and no DM at z > 1100, r_s = 6065 Mpc.")
    print()
    print(f"  For r_s_cascade = 141 Mpc, H_cascade(1100) needs to be:")
    print(f"    H_cascade(1100) = H_LCDM(1100) * (r_s_LCDM / r_s_cascade)")
    print(f"                   = 4.36e7 * (144.4 / 141)")
    print(f"                   = 4.36e7 * 1.024")
    print(f"                   = 4.46e7 km/s/Mpc")
    print(f"  (about the same as LCDM's H(1100))")
    print()
    print(f"  For H_cascade(1100) = 4.46e7:")
    print(f"    4.46e7 = 73 * sqrt(Omega_eff * 1100^3 + 0.68)")
    print(f"    sqrt(Omega_eff * 1100^3) ~ 4.46e7/73 = 6.11e5")
    print(f"    Omega_eff * 1100^3 ~ 3.74e11")
    print(f"    Omega_eff ~ 3.74e11 / 1.33e9 ~ 0.281")
    print()
    print(f"  So we'd need Omega_eff at z = 1100 to be 0.281, not 0.05.")
    print(f"  That's basically LCDM's Omega_m (0.315) without the 5% baryons.")
    print()
    print(f"  In other words: the cascade's picture (no DM at z > 1100) is")
    print(f"  INCOMPATIBLE with Planck's theta_* measurement.")
    print()
    print(f"  For Mechanism L to work, the cascade would need to have")
    print(f"  ~28% of the universe in 'matter' at z = 1100, which is essentially")
    print(f"  LCDM's matter content (without distinguishing DM from baryons).")

    print(f"\n\n  Step 7: So what's the verdict on Mechanism L?")
    print(f"  ----------------------------------------------------------------")
    print()
    print(f"  Mechanism L (re-interpret CMB H_0 = 67.4 as cascade-consistent)")
    print(f"  DOES NOT WORK in the cascade's natural form.")
    print()
    print(f"  The cascade's picture (no DM, no DE at z > 1100) is fundamentally")
    print(f"  different from LCDM, and gives theta_* ~ 0.45, NOT 0.01041.")
    print()
    print(f"  For the cascade to match Planck's theta_*, it would need to have")
    print(f"  the same matter content as LCDM at z > 1100, which contradicts")
    print(f"  the cascade's natural picture.")
    print()
    print(f"  So Mechanism L is BUSTED.")
    print()
    print(f"  The cascade's remaining options:")
    print()
    print(f"  1. Mechanism C (local bubble/void):")
    print(f"     - Local 2D universe density affects local H_0")
    print(f"     - This gives 73 locally, 67.4 globally")
    print(f"     - But Pantheon+ best-fit is 73, not 67.4. So Pantheon+ doesn't")
    print(f"       see the global average being 67.4.")
    print()
    print(f"  2. Mechanism M (accept the tension):")
    print(f"     - Honest position")
    print(f"     - 'Cascade accommodates the tension, doesn't fully explain it'")
    print()
    print(f"  3. Mechanism I (late-time physics):")
    print(f"     - w != -1, EDE, etc.")
    print(f"     - Standard physics, not cascade-specific")
    print()
    print(f"  So Mechanism L is rejected. The most honest position is M.")

    # Final summary
    hr()
    print("SUMMARY: MECHANISM L IS BUSTED")
    hr()
    print(f"\n  Mechanism L claimed: 'CMB H_0 = 67.4 is LCDM artifact.'")
    print(f"  This requires cascade to match Planck's theta_* = 0.01041")
    print(f"  with H_0 = 73 (the cascade's 'real' H_0).")
    print()
    print(f"  Computing theta_*_cascade:")
    print(f"    H_cascade(1100) = {H_cascade_1100:.3e} km/s/Mpc (no DM at z>1100)")
    print(f"    r_s_cascade = {r_s_cascade:.0f} Mpc (vs LCDM's 144.4)")
    print(f"    D_A_cascade(1089) = {D_A_cascade:.0f} Mpc (vs LCDM's {D_A_LCDM:.0f})")
    print(f"    theta_*_cascade = {theta_star_cascade:.4f} (vs Planck's 0.01041)")
    print()
    print(f"  Off by factor {theta_star_cascade/0.01041:.0f}.")
    print()
    print(f"  The cascade's picture (no DM, no DE at z > 1100) is")
    print(f"  INCOMPATIBLE with Planck's theta_* measurement.")
    print()
    print(f"  Mechanism L is BUSTED.")
    print(f"  The cascade should adopt Mechanism M (accept the tension)")
    print(f"  or Mechanism C (local bubble) as its Hubble mechanism.")


if __name__ == "__main__":
    main()
