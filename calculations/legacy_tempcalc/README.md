# legacy_tempcalc/

This directory preserves the development-process scripts and findings that
were originally in `tempcalc/` at the root of the repository. As of v2.7.3,
all active code has been moved to `calculations/`, and `tempcalc/` has been
deleted from the repository root.

The files in this directory are **historical working scripts and findings**
from the cascade's development. They are preserved for transparency and
auditability, but are **not** the canonical implementations.

## What is here

- **Working scripts** (`*.py`): Development scripts that were used to test
  ideas, derive parameters, and explore 2D CFT frameworks. Many have been
  superseded by the `v27_*.py` files in the parent `calculations/`
  directory, which contain the canonical derivations.

- **Findings memos** (`*.md`): Memos documenting the development
  decisions, assessments, and honest corrections made during the cascade's
  development. These are valuable for understanding how the model was
  developed and what was tried and rejected.

- **JSON results** (`*.json`): Raw output from specific test runs.

## File mapping

| File in legacy_tempcalc/ | Status | Maps to |
|---|---|---|
| `2d_universe_population_spectrum.py` | Duplicate of `v27_2d_universe_population_spectrum.py` | (parent) |
| `4zone_quantized_test.py` | Unique development script | (kept for audit) |
| `4zone_data_fitting_assessment.md` | Findings memo | (v2.7: 4-zone REMOVED) |
| `5_27_68_honest_framing.md` | Findings memo | (v2.7.1: 5/27 inner split DROPPED) |
| `agc_kkr_other_models.py` | Duplicate of `v27_agc_kkr_other_models.py` | (parent) |
| `asymmetric_hubble_test.py` | Unique (v2.6 era) | (kept for audit) |
| `boltzmann_2d_cft_inverse_problem.py` | Duplicate of `v27_boltzmann_2d_cft_inverse_problem.py` | (parent) |
| `calculate_running_hubble.py` | Unique (v2.6 era) | (kept for audit) |
| `cascade_architecture_decision.md` | Decision memo | (cone-shape chosen) |
| `cascade_boltzmann_*.py` | Various (v2.6 era) | (parent has v27_ versions) |
| `cascade_boltzmann_findings.md` | Findings memo | (Boltzmann code v2.6) |
| `cascade_camb*.py` | CAMB-based Boltzmann code (v2.6) | (parent has v27_cascade_camb_full.py) |
| `cascade_camb_*_findings.md` | Findings memos | (CAMB v2.6) |
| `cascade_hybrid_assessment.md` | Assessment memo | (cascade as hybrid) |
| `cascade_rz_*.py` | r(z) tests (v2.6-v2.7) | (parent has v27_ versions) |
| `cascade_unify_cdm_mond.py` | Duplicate of `v27_cascade_unify_cdm_mond.py` | (parent) |
| `cascade_g_plus_derivation.py` | Duplicate of `v27_cascade_g_plus_derivation.py` | (parent) |
| `cascade_cmb_anisotropy.py` | Duplicate of `v27_cascade_cmb_anisotropy.py` | (parent) |
| `cleaner_power_law.py` | Unique (v2.6 era) | (kept for audit) |
| `derive_2d_cft_lagrangian.py` | Duplicate of `v27_derive_2d_cft_lagrangian.py` | (parent) |
| `derive_cascade_parameters.py` | Unique (development script) | (kept for audit) |
| `derive_cascade_parameters_v2.py` | Unique (development script) | (kept for audit) |
| `derive_cascade_parameters_*_findings.md` | Findings memos | (parameters derivation) |
| `discrete_horizon_test.py` | Unique (v2.6 era) | (kept for audit) |
| `hubble_tension_4zone_assessment.md` | Assessment memo | (v2.7: 4-zone REMOVED) |
| `karch_randall_2d_universes.py` | Duplicate of `v27_karch_randall_2d_universes.py` | (parent) |
| `lagrangian_literature_memo.md` | Literature research memo | (2D Lagrangian options) |
| `liouville_factive_test.py` | Unique (v2.6 era) | (kept for audit) |
| `liouville_factive_findings.md` | Findings memo | (Liouville f_active) |
| `liouville_factive_results.json` | Raw results | (Liouville f_active) |
| `liouville_frame_analysis.md` | Analysis memo | (2D vs 3+1D frames) |
| `liouville_more_tests.py` | Unique (v2.6 era) | (kept for audit) |
| `liouville_v3_findings.md` | Findings memo | (Liouville v3) |
| `liouville_v3_results.json` | Raw results | (Liouville v3) |
| `omega_dm_derived_quantities.md` | Findings memo | (Ω_DM = 0.27) |
| `omega_dm_honest_correction.md` | Honest correction memo | (Ω_DM = 0.27) |
| `pure_liouville_hubble_test.py` | Unique (v2.6 era) | (kept for audit) |
| `pure_liouville_hubble_test_results.md` | Findings memo | (pure Liouville Hubble) |
| `py_problem_explained.md` | Explanation memo | (Python problem) |
| `rs_ii_calculations.py` | Duplicate of `v27_rs_ii_calculations.py` | (parent) |
| `rs_ii_calculations_summary.md` | Findings memo | (RS-II) |
| `rs_ii_liouville_boltzmann.py` | Duplicate of `v27_rs_ii_liouville_boltzmann.py` | (parent) |
| `rs_ii_liouville_boltzmann_summary.md` | Findings memo | (RS-II + Liouville + Boltzmann) |
| `rs_ii_references.md` | References memo | (RS-II literature) |
| `sparc_btfr_test.py` | Unique (v2.6 era) | (kept for audit) |
| `spec_reference_test.py` | Unique (v2.6 era) | (kept for audit) |
| `time_compression_memo.md` | Memo | (time compression mechanism) |
| `trial_and_error_2d_universe*.py` | Unique (development scripts) | (kept for audit) |
| `trial_and_error_*_findings.md` | Findings memos | (2D universe parameters) |
| `trial_and_error_v26_findings.md` | Findings memo | (v2.6 parameters) |
| `trial_and_error_v26_results.json` | Raw results | (v2.6 parameters) |
| `v27_4zone_removed_memo.md` | Decision memo | (v2.7: 4-zone REMOVED) |
| `v27_desi_act_2025.py` | Duplicate of `v27_desi_act_2025.py` | (parent) |
| `v27_final_2025_constraints.py` | Duplicate of `v27_final_2025_constraints.py` | (parent) |
| `v27_final_external_constraints.py` | Duplicate of `v27_final_external_constraints.py` | (parent) |
| `v27_jt_karch_randall.py` | Duplicate of `v27_jt_karch_randall.py` | (parent) |
| `v27_more_external_constraints.py` | Duplicate of `v27_more_external_constraints.py` | (parent) |
| `v27_ultra_light_dm_limit.py` | Duplicate of `v27_ultra_light_dm_limit.py` | (parent) |
| `v27_web_2d_cft_convergence.py` | Duplicate of `v27_web_2d_cft_convergence.py` | (parent) |
| `web_research_2d_cft_convergence.md` | Findings memo | (2D CFT web research) |
| `why_5pct_active.md` | Honest analysis memo | (5% active) |

## What was deleted

- `__pycache__/` — Python bytecode cache (auto-regenerated)
- 13 duplicate .py files (renamed to v27_*.py in parent `calculations/`)
- 7 v27_*.py duplicates (already in parent `calculations/`)

All 74 unique files (71 .py/.md + 3 .json) have been moved here for
preservation. The `tempcalc/` directory at the repo root has been
deleted.

## Why this organization?

The cascade's active code lives in `calculations/`. The legacy development
scripts and findings live in `calculations/legacy_tempcalc/`. This makes
it easy to find the canonical implementations while preserving the
audit trail of how the model was developed.

The 30 external constraints catalogued in paper §8.1.1–§8.1.7 are the
most current tests. Earlier development work (Boltzmann code, 4-zone H(z),
Liouville tests, etc.) is preserved here for transparency.
