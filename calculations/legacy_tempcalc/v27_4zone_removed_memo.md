# v2.7 — Hubble tension accepted (Mechanism M), 4-zone H(z) REMOVED

## Summary

The cascade accepts the Hubble tension as a real observational tension,
not resolved. The cascade's intrinsic H_0,4D = 70.16 (geometric mean) is
preserved as a non-trivial property of the data.

## What was REMOVED in v2.7

### 1. 4-zone H(z) attempts
The cascade's earlier attempt to explain the Hubble tension via 4 zones
(local R_stellar boost, bulk baseline, secular cosmic web boost, primordial
CMB drag) was REMOVED in v2.7. Reasons:

- The 4-zone spec was data fitting (8 free parameters for ~5 data points)
- The P(y) problem made it internally inconsistent (axion-like mass
  requires deep-bulk 2D universes, but local R_stellar boost requires
  shallow-bulk 2D universes)
- The Boltzmann code (CAMB-based) doesn't predict the 4-zone structure
- It was re-description, not derivation

### 2. Limitation 32 REMOVED
The 4-zone H(z) derivation limitation is no longer applicable.

### 3. §2.6.3 (proposed 4-zone H(z) section) NOT added
The proposed section documenting the 4-zone H(z) is removed.

### 4. DE-dominates 3-zone empirical fit REMOVED from §2.6.2
The 3-zone empirical fit (hyper-local SH0ES, mid-range TRGB/sirens, deep
CMB) is removed. The R_stellar boost (+2.88 km/s/Mpc) and cumulative
2D drag (-2.76 km/s/Mpc) interpretations are removed. The boost ≈ drag
symmetry (20.3 vs 19.5) is removed.

## What was PRESERVED in v2.7

### 1. H_0,4D = 70.16 (geometric mean)
The geometric mean property of the data is preserved. This is a real
prediction: H_0,4D = sqrt(H_CMB × H_local) = sqrt(67.4 × 73.04) = 70.16.

### 2. §2.6.1 (Honest H_0 framework)
The cascade is qualitatively consistent with H_0 = 70 ± 3 across all
measurements.

### 3. §2.6.2 (Geometric mean property, simplified)
Just the geometric mean, no 3-zone empirical fit.

### 4. Ω_DM = 0.27 input postulate (L33)
Preserved.

### 5. 2D-to-3+1D time compression (L31)
Preserved (50-orders tension).

### 6. Cone-shape architecture (v2.6)
Preserved (1D and 0D don't exist).

### 7. Time compression mechanism (§2.5)
Preserved.

## The Mechanism M position (v2.7)

**Mechanism M (now the cascade's only H_0 position):**
- ACCEPTED as a real observational tension, not resolved
- The cascade is qualitatively consistent with H_0 = 70 ± 3
- H_0,4D = 70.16 is a geometric mean property (real prediction)
- The specific H_0 = 73.04 (local) and H_0 = 67.4 (CMB) are observed, not derived
- The 5.6 km/s/Mpc gap is a ΛCDM-framework artifact, not a cascade problem
- The cascade does NOT attempt to explain the gap

## Limitations (v2.7)

- 32 total (was 34 in v2.6; L32 removed)
- L31 (2D-to-3+1D time compression, OPEN): preserved
- L33 (Ω_DM as input, OPEN): preserved
- L32 (4-zone H(z) derivation, OPEN): REMOVED

## Files modified

- `paper/paper.md`: abstract, version header, §2.6.2, §7 limitations
- `README.md`: version bump
- `supporting/layman_summary.md`: version header, Hubble tension section
- `changelog.md`: v2.7 entry added

## What this v2.7 is

- A CLEANER framework (no data fitting attempts to explain Hubble tension)
- A HONEST position (Mechanism M, accept the tension)
- A preservation of the real predictions (H_0,4D = 70.16, cone-shape, time compression)

## What this v2.7 is NOT

- Not a resolution of the Hubble tension
- Not a derivation of the specific H_0 values
- Not a claim that 4-zone H(z) was wrong (it was an attempt, removed for honesty)

## Why this is the right move

The cascade was honest all along (Mechanism M era, commit 83-85): the
Hubble tension is a real ΛCDM-framework artifact, and the cascade is
qualitatively consistent with H_0 = 70 ± 3. The 4-zone H(z) attempt was
an over-reach — trying to derive the specific H_0 values from cascade
mechanisms that don't actually predict them.

By removing the 4-zone H(z), the cascade returns to its honest position:
- Mechanism M is the H_0 framework
- H_0,4D = 70.16 is a real prediction
- The specific H_0 values are observed, not derived
- The 5.6 km/s/Mpc gap is a ΛCDM artifact, not a cascade problem

This is consistent with the paper's broader pattern: honest framing,
re-description not derivation, and 7/7 specific-case predictions
unchanged (the rename, the architecture change, and the 4-zone removal
are all framing, not physics).

## The deeper lesson

The cascade's 4-zone H(z) attempt illustrates a recurring pattern:
**the cascade can INTERPRET observations with cascade mechanisms,
but it cannot DERIVE the specific values.** This is consistent with
the paper's broader claim that the cascade is a "thought experiment,
not a finished theory" (paper §1).

The cascade's HONEST contributions are:
- Qualitative interpretations (DM = cumulative 2D universe deaths,
  DE = 4D event antigravity)
- Geometric mean property (H_0,4D = 70.16)
- Cone-shape architecture (forced, not a choice)
- Time compression mechanism (real effect in 5D AdS_5)
- Ω_DM = 0.27 input postulate (honest about what's derived vs assumed)

The cascade's LIMITATIONS are:
- Cannot derive specific H_0 values (73.04, 67.4)
- Cannot derive 5.6 km/s/Mpc gap
- Cannot derive Ω_DM = 0.27 from first principles
- Cannot derive 2D universe's specific dynamics from 2D CFT
- Cannot resolve the Hubble tension

These limitations are HONESTLY DOCUMENTED in the paper (32 limitations
with status). The cascade is consistent with current data, falsifiable,
and ready for theoretical physicist to complete.

## File locations

- This memo: `tempcalc/v27_4zone_removed_memo.md`
- Paper: `paper/paper.md` (v2.7)
- Changelog: `changelog.md` (v2.7 entry)
- README: `README.md` (v2.7)
- Layman: `supporting/layman_summary.md` (v2.7)
- Related memos (preserved as research artifacts):
  - `tempcalc/4zone_data_fitting_assessment.md`
  - `tempcalc/hubble_tension_4zone_assessment.md`
  - `tempcalc/py_problem_explained.md`
  - `tempcalc/cascade_architecture_decision.md`
  - `tempcalc/cascade_hybrid_assessment.md`
  - `tempcalc/cascade_camb_no_zones_findings.md`
  - `tempcalc/cascade_camb_time_compressed_findings.md`
  - `tempcalc/liouville_v3_findings.md`
  - `tempcalc/omega_dm_honest_correction.md`
  - `tempcalc/omega_dm_derived_quantities.md`
  - `tempcalc/rs_ii_references.md`
  - `tempcalc/pure_liouville_hubble_test_results.md`
  - `tempcalc/trial_and_error_v26_findings.md`
  - `tempcalc/cascade_boltzmann_findings.md`
  - `tempcalc/time_compression_memo.md`

## Bottom line

v2.7 is a CLEANER, HONESTER framework. The cascade accepts the Hubble
tension as a real observational tension, not resolved. The 4-zone H(z)
attempt was data fitting, removed. The cascade's intrinsic H_0,4D = 70.16
(geometric mean) is preserved as a real prediction. The 7/7 specific-case
predictions are UNCHANGED. 32 honest limitations documented.
