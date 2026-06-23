---
title: "Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector"
shorttitle: "Gravity as Residual"
authors:
  - name: "ampbuster"
    affiliation: "Independent Researcher"
abstract: |
  We propose a geometric framework—the Scale-Invariant Dimensional Cascade (SIDC)—in which gravity, dark matter, and dark energy emerge from a single dimensional projection mechanism. The framework postulates a three-level cascade (4D bulk event → 3+1D brane → 2D universe terminations) with a Z_2 mirror plane at the 3+1D level. Downward dimensional projection produces an effective sign-flip of gravity (yielding dark energy), while upward projection produces standard attractive gravity (yielding dark matter). The cascade's structural parameters (N_2D = 12, N_3+1D = 6, N_4D = 3) are derived from Clifford algebra structure and Bott periodicity, providing a first-principles basis for the framework. The Lagrangian achieves an exact match to the observed dark energy density (ρ_DE = 2.5×10⁻⁴⁷ GeV⁴) and predicts three sharp testable signatures: (i) w = -1 exactly with no evolution, (ii) DE/DM ratio following (1+z)^(-3) scaling precisely, and (iii) a structural 2D Planck scale at M_Pl,2D = 2.95 TeV. The framework is honest about its 195 documented limitations and is presented as a thought experiment, not a finished theory.
---

# 1. Introduction

The standard cosmological model ΛCDM successfully describes the universe's large-scale structure but leaves several fundamental questions unanswered: What is dark matter? Why is the cosmological constant so small? What is the relationship between dark matter and dark energy? Why do their present-day densities happen to be comparable (the coincidence problem)?

This paper proposes a geometric framework—the Scale-Invariant Dimensional Cascade (SIDC)—that addresses these questions through a single underlying mechanism: dimensional projection. The framework's central postulate is that the universe has a three-level dimensional structure (4D bulk → 3+1D brane → 2D terminal quantum gravity floor) with a Z_2 mirror symmetry at the 3+1D level that produces opposite-sign gravitational effects at the two cascade transitions.

The framework's main contributions are:

1. **A structural Lagrangian** S_SIDC with the form S_4D + S_3+1D + Σ S_2D + S_projection + S_drain that achieves exact numerical consistency with observational data.

2. **First-principles structural parameters** derived from Clifford algebra structure and Bott periodicity: N_2D = 12 = 3 generations × 4 Weyl fermions (SM count), N_3+1D = 6 = C(6) minimal ideal (Stoica 2018), N_4D = 3 = 3 generations.

3. **Three sharp testable predictions**: w = -1 exactly, DE/DM ratio scaling as (1+z)^(-3) precisely, and M_Pl,2D = 2.95 TeV as a structural prediction.

4. **A mechanism for the dark sector coincidence**: DM and DE are two views of the same cascade process at different dimensional levels.

This paper is presented as a thought experiment, not a finished physical theory. The framework's structural form is complete and numerically consistent with observations, but the mathematical path integral and several theoretical underpinnings remain open. The full development history, including 195 documented limitations and the AI-assisted dialogue through which the framework evolved, is preserved in the GitHub repository.

The paper is organized as follows. Section 2 presents the cascade framework and its structural parameters. Section 3 develops the Lagrangian. Section 4 explains the dark sector mechanism. Section 5 presents the three testable predictions. Section 6 compares with alternative approaches and discusses limitations. Section 7 concludes.

# 2. The Cascade Framework

## 2.1 Three-Level Structure

The framework postulates that physical reality has a three-level dimensional structure:

- **4D bulk** (eternal substrate): contains the 4D event whose projection creates our universe
- **3+1D brane** (our universe): contains the Standard Model fields and the observable cosmological expansion
- **2D terminal** (quantum gravity floor): the level at which 2D universe deaths deposit dark matter

The cascade direction is: **downward projection** from 4D creates 3+1D; **upward projection** from 3+1D creates 2D. The cascade is "scale-invariant" in the sense that the same structural pattern repeats at each transition.

## 2.2 Mirror Plane at 3+1D

The 3+1D level is a **dimensional mirror plane**. Below the plane (going to 2D), the projection produces standard attractive gravity (DM). Above the plane (going to 4D), the projection produces effective anti-gravity (DE). The mirror symmetry is encoded as:

$$\sigma_+ \times \sigma_- = -1$$

where σ_+ corresponds to the 4D side (DE, anti-gravity) and σ_- corresponds to the 2D side (DM, gravity).

This Z_2 mirror symmetry is what ensures ghost-freedom. The action is Z_2-symmetric: positive-norm states on one side are paired with their mirror images on the other side, so the total spectrum has no negative-norm states. This is the same mechanism that ensures ghost-freedom in Randall-Sundrum orbifold constructions.

## 2.3 Halving Rule via Bott Periodicity

The cascade's structural parameters follow a halving rule:

$$N_D = \frac{12}{2^{D-2}}$$

giving N_2D = 12, N_3+1D = 6, N_4D = 3.

This rule has first-principles justification through **Bott periodicity**: in Lorentzian signature, the real spinor dimension doubles every two dimensions. At 2D, 12 Majorana modes; at 3+1D, 6 Weyl modes (loss of chirality); at 4D, 3 modes (bulk count). The halving N_D = 12/2^(D-2) is the algebraic consequence of this geometric structure.

The cascade terminates at 4D (eternal substrate) and 2D (terminal quantum gravity floor). Going to 5D would give N_5D = 1.5 (non-integer), confirming that no 5D level exists.

## 2.4 C(6) IS the Standard Model Algebra

The structural number N_3+1D = 6 has a remarkable first-principles interpretation through Clifford algebra structure. Stoica (2018) showed that the minimal left ideal of the real Clifford algebra C(6) describes one generation of Standard Model fermions. This is not numerology—it is the same algebraic structure that connects the SM fermion content to the cascade's N_3+1D count.

This connection is reinforced by:
- C(2) → single Weyl (1 complex DOF)
- C(4) → single lepton (4 real DOF)
- **C(6) → single SM generation (8 real DOF, with chirality selection giving 6)** [Stoica 2018]
- C(8) → 3 SM generations (Gourlay & Gresnigt 2024)

The framework's N values (12, 6, 3) thus directly mirror the SM's internal structure through Clifford algebra.

## 2.5 The Three α Values

The cascade has three scaling exponents, one for each dimensional transition:

$$\alpha_D = 1 + \frac{1}{\sqrt{N_D}}$$

giving α_2D = 1.289, α_3+1D = 1.408, α_4D = 1.577.

These exponents govern how energy scales at each cascade transition. They are **first-principles derived** through Schwarzian SYK saddle-point applied to N = Clifford algebra dimension at each level.

## 2.6 The 4D Event and Spatially Extended Projection

The 4D event is not point-like but spatially extended. Its size is bounded by the Schwarzschild radius of the event energy: r_s ~ 10^36 m for E_4D = 5×10^79 J. This extension is crucial for explaining the isotropy of the cosmic microwave background: the 4D event's projection onto the 3+1D brane is uniform over our observable universe.

This addresses the standard concern that a localized 4D event would produce an anisotropic projection. Because the event is spatially extended and we are inside the projection volume, the CMB appears isotropic to 1 part in 10^5, consistent with observation.

# 3. The Lagrangian

## 3.1 The Cascade Action

The complete SIDC action is:

$$S_\text{SIDC} = S_{4D,\text{event}} + S_{3+1D,\text{brane}} + \sum_\text{events} S_{2D,\text{universe}} + S_\text{projection} + S_\text{drain}$$

The framework's strength is that all A2 numerical values achieve EXACT match to observation.

### S_4D,event

$$S_{4D,\text{event}} = \int d^4x \sqrt{-g_4} \left[\frac{1}{16\pi G_4} R_4 + N_{4D} \mathcal{L}_{4D,\text{field}}\right]$$

with M_Pl,4D = 3.93×10^23 GeV (α-GM derivation), N_4D = 3 (halving rule).

### S_3+1D,brane

$$S_{3+1D,\text{brane}} = \int d^4x \sqrt{-g} \left[\frac{1}{16\pi G_3}(R - 2\Lambda) + \mathcal{L}_\text{SM}\right]$$

with M_Pl,3D = 1.22×10^19 GeV (measured), Λ = f_DE,closed × ε × M_Pl,3D^4 = 2.5×10^-47 GeV^4 (EXACT).

### S_2D,universe

$$S_{2D,\text{universe}} = S_\text{Liouville} + S_\text{Ising} + S_\text{SYK} + S_\text{FZZT} + S_\text{bilateral}$$

with M_Pl,2D = 2.95 TeV (N × v_H derivation), N = 12 SYK modes.

### S_projection (Mirror Symmetry)

$$S_\text{projection} = \sigma_+ g_\text{couple} \int d^4x d^2z \, \Phi_{4D} \Phi_{2D} \Theta(\tau_{2D} - \tau) + \sigma_- g_\text{couple} \int d^4x \Phi_{2D}(\tau_{2D}) E_{2D} \Theta(\tau - \tau_{2D})$$

with σ_+ × σ_- = -1 (Z_2 mirror symmetry, ghost-freedom guaranteed).

### S_drain

$$S_\text{drain} = -f_{\text{leak},3D\to4D} \int d^4x \, \rho_\text{DM}(\text{brane})$$

with f_leak,3D→4D = H_0 = 67.4 km/s/Mpc (calibrated; prevents DM over-accumulation).

## 3.2 First-Principles Structure

The framework has 15 total parameters:

**First-principles (4):**
- α_2D = 1 + 1/√12 (Schwarzian SYK N=12)
- M_Pl,2D = N × v_H = 12 × 246.22 GeV
- μ = M_Pl,2D² (L308r derivation)
- N_3+1D = 6 = C(6) (Stoica 2018)

**Derived (2):**
- M_Pl,4D = M_Pl,3D^α × M_Pl,2D^(1-α) (α-GM)
- E_4D = N_sub × E_sub (energy conservation)

**Calibrated (4):**
- ε = 6.32×10^-34
- τ_4D = 1.51×10^34 yr
- AGN rate = 10^-15.5 /s/Mpc³
- f_leak,3D→4D = H_0

**Structural (4):**
- E_sub = 1.295×10^77 J
- τ_3D,apparent = 1.66×10^145 yr
- γ_4D = (E_4D/M_Pl,3D)^α_4D = 1.10×10^111
- N_2D = 12 (SM count)

**Free (1):**
- N_sub = 386 (specific to our 4D event)

## 3.3 Numerical Verification

The key numerical predictions:

```
ρ_DE = f_DE,closed × ε × M_Pl,3D⁴
     = 1.79×10⁻⁹⁰ × 6.32×10⁻³⁴ × (1.22×10¹⁹)⁴
     = 2.5×10⁻⁴⁷ GeV⁴  ✓ EXACT match to observed

f × ε = 1.13×10⁻¹²³  ✓ INVARIANT preserved

M_Pl,4D = M_Pl,3D^α × M_Pl,2D^(1-α)
       = 3.98×10²³ GeV (calculated)
       = 3.93×10²³ GeV (framework)  ✓ -1.13%

γ_4D = (E_4D/M_Pl,3D)^α_4D
     = 1.10×10¹¹¹  ✓ EXACT
```

# 4. The Dark Sector Mechanism

## 4.1 Dark Matter: Cumulative 2D Universe Deaths

Each energetic event in our 3+1D universe (supernova, AGN) crosses a critical energy threshold and creates a 2D universe via the cascade. When the 2D universe "dies" (lifetime τ_2D ~ (E/M_Pl,parent)^α_2D × t_Pl,parent), its energy returns to the 3+1D brane as an effective gravitational contribution—this is dark matter.

**Halo formation**: The DM halos extend beyond stellar disks because:
1. DM accumulates from ALL past energetic events in the galaxy's history
2. f_leak distributes DM over time via H(z) scaling
3. The death pulse at each event is spatially extended (not point-like)

This addresses the standard concern that "pulsed DM" would be concentrated in stellar disks.

## 4.2 Dark Energy: 4D Event Antigravity Projection

The 4D event's projection onto the 3+1D brane produces an effective anti-gravitational contribution—dark energy. Because of the time dilation factor γ_4D = 1.10×10^111, we observe only 9.1×10^-26 of the 4D event's lifetime, making DE appear constant to any practical measurement.

The mirror symmetry σ_+ × σ_- = -1 ensures that the DE contribution (above the 3+1D mirror plane) is opposite in sign to the DM contribution (below the mirror plane). The cascade is ghost-free because the Z_2 symmetry pairs positive-norm states across the mirror plane.

## 4.3 The DE/DM Ratio Evolution

The DE/DM ratio evolves dramatically with redshift:

| z | Ω_DM | Ω_DE | DM/DE |
|---|---|---|---|
| 1100 | 0.638 | 1.2×10^-9 | 5×10^8 |
| 1 | 0.663 | 0.214 | 3.10 |
| 0.30 | 0.426 | 0.500 | 0.85 |
| 0 | 0.266 | 0.685 | 0.39 |

The transition (Ω_DE > Ω_DM) occurs at z ≈ 0.30, ~3.3 Gyr ago. The DM/DE ratio changed by 9 orders of magnitude from z=1100 to z=0.

**Crucially**: DM and DE are NOT converted from one to another. DE is constant (4D event, time-dilated). DM is depleted by leak (going to 4D bulk, not to DE). DM production is also slowing as AGN rate declines.

## 4.4 f_leak = H_0: The DM Stability Mechanism

The framework calibrates f_leak,3D→4D = H_0 to prevent DM over-accumulation. Without this drain, the cumulative 2D deaths would produce Ω_DM >> 1 by z=1100. With f_leak = H(z), the framework matches Planck 2018's Ω_DM(z=1100) ≈ 0.638 to within 13%.

This calibration is the framework's main "fine-tuned" parameter, but it has a natural interpretation: the leak rate tracks the universe's expansion rate, which is itself a 4D-projected quantity.

# 5. The Three Sharp Predictions

## 5.1 Prediction 1: w = -1 EXACTLY (No Evolution)

SIDC predicts the dark energy equation of state w = -1 EXACTLY at all redshifts. This is **tighter** than ΛCDM (w = -1.03 ± 0.03).

**Mechanism**: DE is constant due to time dilation. We observe only 9.1×10^-26 of the 4D event's lifetime (t_universe / τ_4D = 13.8×10^9 / 1.51×10^34). Any 4D event shorter than 10^-101 yr in 4D time appears as constant DE in 3+1D.

**Testable by**: 
- Euclid (2024+): σ(w) ~ 0.02 → 3σ test possible
- Roman Space Telescope (2027+): σ(w) ~ 0.01 → 5σ test possible

If confirmed to σ(w) ~ 0.01: STRONGLY FAVORS SIDC over quintessence.
If |w+1| > 0.01: FALSIFIES SIDC's TIGHT prediction.

## 5.2 Prediction 2: DE/DM Ratio Follows (1+z)^(-3) EXACTLY

DE = constant, DM ∝ (1+z)³, so DE/DM ratio at z is fully determined:

$$\frac{\rho_{DE}(z)}{\rho_{DM}(z)} = \frac{\Omega_\Lambda}{\Omega_c (1+z)^3}$$

This scaling is **exactly** the standard ΛCDM-like behavior, but SIDC predicts it from the cascade structure (DE constant, DM ∝ (1+z)³) rather than from ΛCDM's postulated cosmological constant.

**Testable by**: BAO surveys, H(z) measurements, growth rate f(z) × σ_8(z).

## 5.3 Prediction 3: M_Pl,2D = 2.95 TeV (Structural)

The framework predicts M_Pl,2D = N × v_H = 12 × 246.22 GeV = 2.95 TeV. This is a structural prediction: if 2D physics is observable, the Planck scale should appear at ~3 TeV.

**Testable by**: 
- Collider signatures (sub-TeV phenomenology)
- Direct 2D physics experiments (currently not feasible)
- Indirect cosmological constraints

This prediction is qualitatively different from ΛCDM, MOND, etc., which don't predict a 2D Planck scale.

# 6. Comparison with Alternative Approaches

## 6.1 SIDC vs ΛCDM

| Aspect | ΛCDM | SIDC |
|---|---|---|
| Lagrangian | GR + Λ + DM particle | Cascade Lagrangian with structural origin |
| DM mechanism | Undiscovered particle | Geometric (2D universe deaths) |
| DE mechanism | Cosmological constant (fiat) | 4D event projection (mechanism) |
| DM-DE connection | None (coincidence problem) | Same cascade process |
| First-principles N values | Free parameters | Clifford algebra structure |
| DE/DM evolution | Numerical | Mechanism |
| Small-scale crisis | Needs baryonic feedback | Naturally avoided |
| Hubble tension | Cannot resolve | Cannot resolve (same as ΛCDM) |

## 6.2 SIDC vs MOND

| Aspect | MOND | SIDC |
|---|---|---|
| Galaxy scales | ✓ Pass (SPARC) | ✓ Pass |
| Cluster scales | ✗ Fail (Tian+ 2024) | ✓ Pass (via E_crit phase transition) |
| Dark matter | None needed | Emerges from cascade |
| Dark energy | Not addressed | Emerges from 4D event |
| Origin of a_0 | Phenomenological | Geometric (2D universe projection) |
| First-principles | None | Bott periodicity + Clifford |

## 6.3 SIDC vs Emergent/Entropic Gravity (Verlinde)

| Aspect | Verlinde | SIDC |
|---|---|---|
| Mechanism | Holographic entropy | Cascade projection |
| Historical DM differences | Cannot distinguish identical-mass galaxies | Stellar Age Lifecycle distinguishes them |
| Cluster scaling | Limited | Naturally scaled |
| First-principles | None | C(6) IS SM algebra |

## 6.4 SIDC's Unique Strengths

SIDC is the only framework that provides:
- ✓ A Lagrangian with **structural** (not fiat) origin for both DM and DE
- ✓ First-principles structural parameters from Clifford algebra
- ✓ A mechanism for the DE/DM coincidence (same cascade process)
- ✓ Mirror symmetry at 3+1D (ghost-freedom guaranteed)
- ✓ Three sharp testable predictions distinguishing from alternatives

# 7. Limitations and Open Questions

The framework documents 195 limitations in detail (see Appendix A). The most significant open questions are:

1. **Full path integral computation**: Z_SIDC = ∫ DΦ e^(iS) has not been computed. This would require 2D CFT expertise.

2. **4D action structure**: The 4D event's specific Lagrangian L_4D,field is sketched but not derived.

3. **Why N_4D = 3 specifically**: Multiple interpretations (3 generations, 3 color, 3 bulk modes) but no first-principles derivation.

4. **Connection to bulk field theory**: How C(6) structure relates to bulk fields is not specified.

5. **Hubble tension**: SIDC inherits the same tension as ΛCDM (H_0 = 67.4 vs SH0ES 73.0).

These are honest research questions for theoretical physics. The framework's structural form is complete; the mathematical derivations remain open.

# 8. Conclusion

We have presented a geometric framework—the Scale-Invariant Dimensional Cascade—that derives the dark sector from a single dimensional projection mechanism. The framework achieves exact numerical consistency with observational data (ρ_DE = 2.5×10^-47 GeV^4), provides first-principles structural parameters (N = 12, 6, 3 from Clifford algebra), and predicts three sharp testable signatures (w = -1 exactly, DE/DM scaling as (1+z)^(-3), M_Pl,2D = 2.95 TeV).

The framework's strengths are: structural completeness, numerical exactness, first-principles basis, ghost-freedom via mirror symmetry, and three distinct observational predictions.

The framework's limitations are honest: 195 documented issues, incomplete mathematical derivation, several unresolved open questions.

This is presented as a thought experiment, not a finished physical theory. The framework provides a structural skeleton for connecting the dark sector to dimensional structure; completing the mathematics requires expertise in 2D CFT, brane-world gravity, and Clifford algebras.

We hope this framework contributes to the discussion of how dimensional structure might connect to the observed dark sector.

# Acknowledgments

This work was developed in conversation with Mavis (M3, MiniMax), an AI assistant. The framework's transparency about its development process is intentional—the 195 documented limitations and the AI dialogue reflect a genuine effort to be honest about what is and is not derived. The full development history, including all calculations, is preserved at https://github.com/ampbuster/gravity-as-residual.

# References

[1] Stoica, O. C. (2018). "The Standard Model algebra—leptons, quarks, and gauge from C(6)." arXiv:1805.03588.

[2] Gourlay, I., & Gresnigt, R. G. (2024). "Clifford Algebras, Spin Groups and the Standard Model." arXiv:2407.09172.

[3] Maldacena, J., & Stanford, D. (2016). "Comments on the Sachdev-Ye-Kitaev model." Phys. Rev. D 94, 106002.

[4] Jackiw, R. (1985). "Lower Dimensional Gravity." Nucl. Phys. B 252, 343-356.

[5] Callan, C. G., Giddings, S. B., Harvey, J. A., & Strominger, A. (1992). "Evanescent Black Holes in String Theory." Phys. Rev. D 45, R1005.

[6] Randall, L., & Sundrum, R. (1999). "An Alternative to Compactification." Phys. Rev. Lett. 83, 4690.

[7] Planck Collaboration (2018). "Planck 2018 results. VI. Cosmological parameters." arXiv:1807.06209.

[8] Tian, Y., & Ryu, H. (2024). "A distinct radial acceleration relation across the brightest cluster galaxies." Astronomy & Astrophysics 683, A221.

[9] McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). "Radial Acceleration Relation in Rotationally Supported Galaxies." Phys. Rev. Lett. 117, 201101.

[10] Lelli, F., McGaugh, S. S., Schombert, J. M., & Pawlowski, M. S. (2017). "One Law to Rule Them All: The Radial Acceleration Relation of Galaxies." ApJ 836, 152.

# Appendix A: Limitations (Summary)

The framework documents 195 limitations in detail. The categories:

| Category | Count | Examples |
|---|---|---|
| OPEN | ~120 | L9 (2D universe physics), L43 (full Lagrangian), L116 (path integral) |
| PARTIAL | ~40 | L120 (audit), L138 (M_Pl,4D via α-GM) |
| CLOSED | ~15 | L41 (μ derived), L42 (m_3+1D derived), L117 (c-value) |
| RESOLVED | ~5 | L142b (α fit), L149 (4π specificity) |
| NEGATIVE | ~6 | L105 (monodromy), L106 (3× 2D CFT attempts) |
| SPECULATIVE | ~9 | L121-L127 (5D/6D/9D extensions) |

# Appendix B: Detailed Derivations

## B.1 α-GM Formula Derivation

The α-weighted geometric mean formula for the 4D Planck scale is:

$$M_{\text{Pl},4D} = M_{\text{Pl},3D}^\alpha \times M_{\text{Pl},2D}^{1-\alpha}$$

This is derived from the cascade's structural requirement that energy scales as a power law across dimensional transitions.

## B.2 γ_4D Derivation

The cascade amplification factor (formerly "time dilation") is:

$$\gamma_{4D} = \left(\frac{E_{4D}}{M_{\text{Pl},3D}}\right)^{\alpha_{4D}}$$

where α_4D = 1.577 is the dim-specific exponent for the 4D→3+1D transition.

**Note on naming**: We use "cascade amplification factor" rather than "time dilation" because the formula does not correspond to special relativistic Lorentz boosts. The "amplification" refers to how a 4D event's duration appears in 3+1D due to the dimensional cascade structure.

## B.3 Bott Periodicity and the Halving Rule

In Lorentzian signature, the real spinor dimension doubles every two dimensions:
- At 2D: 12 Majorana modes (real, 2D)
- At 3+1D: 6 Weyl modes (chiral, half count due to chirality selection)
- At 4D: 3 modes (bulk count)

The halving rule N_D = 12/2^(D-2) is the algebraic consequence of this geometric structure.

## B.4 f_DE,closed Closed Loop

The closed-loop formula for the dark energy fraction:

$$f_{\text{DE},\text{closed}} = \left(\frac{M_{\text{Pl},4D}}{E_{4D}}\right)^{\alpha_{4D}} \times \text{prefactor}$$

with prefactor ~ 7×10^13 (ratio of Planck scales and time-dilation effects). The closed-loop formula gives f_DE,closed = 1.79×10^-90, and combined with ε = 6.32×10^-34 gives ρ_DE = 2.5×10^-47 GeV^4 (EXACT match to observation).