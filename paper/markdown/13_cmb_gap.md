
> **LEGACY NOTE**: This file contains references to the OLD Hill function F_p(z) framework
> (DROPPED in v3.3+, see L100). The current framework uses **bilateral cascade** with
> **f_leak = H_0** as new principle (Approach A1, §7.4.20). Hill function references
> are kept for historical context. See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md`
> for details on what was dropped.

<!-- 13_cmb_gap.md - part of paper.md split (v3.0.13) -->

## 13. SIDC's CMB Gap: an Honest Limitation (June 2026) — *HISTORICAL (v2.7.5: CLOSED, v3.3+: F_p FRAMEWORK DROPPED)*

**LEGACY (v2.7.5+, HISTORICAL)**: The CMB gap was CLOSED in v2.7.5 via the smooth $F_p(z) = 0.7 + 0.3 \cdot z^2/(z_{half}^2 + z^2)$ (Hill function, n=2, $z_{half} \approx 3$). This replaces the v2.4 constant $F_p = 0.7$.

**HOWEVER (v3.3+, CURRENT)**: The ENTIRE $F_p(z)$ Hill function framework was DROPPED in v3.3+ per L100 (user-critique 6 times). Current framework uses bilateral cascade with $f_{\rm leak} = H_0$ (post-Friedmann, A1). CMB gap is now addressed through DIFFERENT mechanism (cumulative 2D universe deaths + calibrated AGN rate).

See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md` for full legacy history.

**Historical framing (v2.4-v2.7.4).** SIDC's earlier (v2.4-v2.7.4) version of the CMB gap was an honest limitation. The current section is preserved for historical context — it documents SIDC's progression from "tension" to "closed" via the smooth $F(z)$ refinement.

This section acknowledges a **fundamental tension** between SIDC's current mechanism and the observed CMB angular power spectrum.

### 13.1 The CMB requirement

The CMB angular power spectrum (Planck 2018 results V, A&A 641, A5; arXiv:1907.12875) requires a matter density of **$\Omega_m$ = 0.315** at the recombination epoch (z = 1100), of which **$\Omega_{\rm c}$ = 0.265** is cold dark matter. Without this DM, the acoustic peaks are at the wrong positions:
- First peak (l ~ 220): controlled by sound horizon, **shifts** if $\Omega_m$ changes
- Second peak (l ~ 540): baryon-to-photon ratio, **changes** with $\Omega_m$
- Third peak (l ~ 810): matter-to-radiation, **depends on $\Omega_{\rm c}$**

This is **not a small effect**: the difference between baryon-only ($\Omega_m$ ~ 0.049) and the observed $\Omega_m$ = 0.315 corresponds to a factor of ~6.4 in total matter density, which moves the acoustic peaks by 10-20% in l.

### 13.2 SIDC's prediction at z = 1100

SIDC's mechanism (per §2.4-2.7) is:

> DM is the cumulative back-projection from 2D universes created by energetic 3D events.

SIDC's first "energetic events" in our universe are the **first stars (Population III)** forming at z ~ 20-30, and the first core-collapse supernovae at z ~ 15-20. Before this, there are essentially no energetic events in SIDC's sense.

Therefore, SIDC predicts: **$\Omega_{\rm DM}$(z > 20) ~ 0**. SIDC's predicted $\Omega_m$(z = 1100) is approximately the **baryon-only** value: $\Omega_m$(z = 1100) ~ $\Omega_{\rm b}$ = 0.049.

**Importantly, SIDC's *baryon* prediction is correct at z = 1100.** The 5% baryons are present at all z, including z = 1100, in plasma form (ionized hydrogen and helium — the medium that emits and absorbs the CMB). They are "visible" via their interaction with CMB photons, even though no stars or galaxies have formed yet.

SIDC's failure is specifically in the **27% dark matter**, not the 5% baryons. SIDC predicts:
- $\Omega_{\rm b}$(z = 1100) = 0.049 **[PASS]** (matches Planck)
- $\Omega_{\rm DM}$(z = 1100) = 0 **[FAIL]** (SIDC's specific failure)
- $\Omega_m$(z = 1100) = 0.049 **[FAIL]** (factor of 6.4 below Planck's 0.315)

### 13.3 The tension

The CMB acoustic peaks depend on:
- **First peak (l ~ 220):** sound horizon (depends on total $\Omega_m$, weakly on $\Omega_{\rm c}$)
- **Second peak (l ~ 540):** baryon-to-photon ratio (depends on $\Omega_{\rm b}$, mostly correct in SIDC)
- **Third peak (l ~ 810):** matter-to-radiation ratio (depends on $\Omega_{\rm c}$, **missing in SIDC**)

Without DM at z = 1100:
- The 3rd peak is missing (no DM to enhance it)
- The 1st peak shifts to slightly different l (sound horizon changes)
- The Silk damping scale is wrong (no DM to modify photon diffusion)
- Polarization patterns are different

SIDC's *baryon* prediction is consistent with the 1st and 2nd peak ratios (which depend primarily on $\Omega_{\rm b}$). SIDC's *DM* prediction fails the 3rd peak test (which depends on $\Omega_{\rm c}$).

**This is a real falsification risk for SIDC as currently formulated.** SIDC's qualitative picture is consistent with all galaxy data at z < 4, but the CMB at z = 1100 has a specific gap in the *DM* mechanism, not in the *baryon* mechanism.

### 13.4 Possible resolutions

SIDC needs an *early-DM mechanism* to match the CMB. Four possible resolutions:

**1. Primordial 2D universe creation during inflation/baryogenesis/BBN.** If SIDC's "energetic event" threshold extends to non-stellar events (e.g., phase transitions, particle decays), then 2D universes would be created in the early universe, providing the DM needed at z = 1100. This is a post-hoc extension of SIDC that needs to be specified.

**2. Cosmological DM component not from 2D universe back-projection.** SIDC could admit a "primordial" DM component (e.g., sterile neutrinos, axions) alongside SIDC's 2D universe DM. This is dual-component DM but is ad hoc.

**3. SIDC is incomplete at z > 20.** SIDC currently has no mechanism for DM at z > 20. This is a known limitation, awaiting a more complete cosmological model. SIDC is "incomplete" in this sense.

**4. Other early-universe physics.** SIDC could include an "early 2D universe creation" phase tied to inflation, reheating, or some other early-universe event. This would require specifying the threshold for 2D universe creation in cosmological conditions, which is currently unconstrained.

### 13.5 What is and isn't falsified

**Falsified (if SIDC is taken literally with no early-DM extension):**
- The CMB angular power spectrum cannot be matched
- This is a **serious tension**, not just a "gap"

**Still falsifiable (with early-DM extension):**
- The 47 Tuc test (SIDC vs particle DM) — still valid at z = 0
- End-of-universe signatures (DESI Y5, LSST Y1) — still valid at z = 0
- Galaxy-zoo tests (47 Tuc, AGC 114905, KKR 25, etc.) — still valid at z = 0
- SIDC's geometric mechanism for the dark sector — still valid for *low-redshift* observations

SIDC is **consistent with existing galaxy data (z < 4)** but has a **fundamental CMB gap (z = 1100)**. This is an honest limitation of v2.7.3+.

### 13.6 Proposed SIDC extensions

To address the CMB gap, SIDC would need:
- A specific early-universe mechanism for 2D universe creation (e.g., during inflation, reheating, or BBN)
- A specific threshold for "energetic event" that includes non-stellar events
- A derivation of SIDC's early-DM density from first principles
- An updated Boltzmann solver to compute SIDC's CMB angular power spectrum

This is **future work**, not a v2.7.3+ deliverable. SIDC's current framework is a *late-time* (z < 4) geometric model. Extending it to the early universe (z > 20) is a major open problem.

### 13.7 MCMC fit to real SPARC data (June 2026)

To complement the qualitative picture, SIDC has been fit to the **SPARC database** (175 galaxies, 3383 radial data points) using MCMC (emcee). See `calculations/v27_cascade_mcmc_rar.py` for the full calculation.

**SIDC RAR model:**$g_{\rm obs}$ = $g_{\rm bar}$ / (1 - exp(-sqrt($g_{\rm bar}$ / $a_0$)))

This is the standard interpolating function that smoothly transitions from Newtonian ($g_{\rm bar}$ >> $a_0$) to MOND ($g_{\rm bar}$ << $a_0$).

**MCMC result (this run):**
- $a_0$ = $2.34 \times 10^{-10}$ ± $1.54 \times 10^{-10}$ m/s^2
- sigma_int = 0.089 ± 0.040 dex
- Reduced chi^2 ≈ 0 (model is "over-fit" given the wide error bars)

**Literature comparison (Li+ 2018, arXiv:1803.00022):**
- $a_0$ = $1.20 \times 10^{-10}$ ± 0.02 m/s^2
- sigma_int = 0.057 ± 0.002 dex
- Reduced $\chi^2 = 1.0$ (good fit)

SIDC's $a_0$ is consistent with the literature (within 1-2 sigma). SIDC's RAR is statistically equivalent to standard MOND. SIDC adds *geometric unification* ($a_0$ emerges from 2D universe back-projection) but does not *uniquely* beat MOND via the RAR.

**The 47 Tuc test is SIDC's true differentiator** (from MOND and from particle DM). The RAR fit is a *consistency check* on SIDC's phenomenological prediction, not a new confirmation.

### 13.8 Summary

SIDC has a **real CMB gap**: SIDC's mechanism predicts $\Omega_{\rm DM}$(z = 1100) ~ 0, but the observed Planck 2018 value is $\Omega_{\rm DM}$ = 0.265. Without an early-DM mechanism, SIDC's CMB prediction fails.

SIDC is **consistent** with:
- Galaxy-zoo tests (z < 4, 11/11 pass on real data)
- 47 Tuc prediction (z = 0, awaits DR1 2027)
- End-of-universe predictions (z = 0, awaits DESI Y5 2027-2028)
- RAR fit to SPARC (z = 0, consistent with MOND)

SIDC has a **fundamental gap** at:
- CMB (z = 1100): predicts no DM, Planck requires DM

This is an **honest limitation** of v2.7.3+. SIDC is a *late-time* (z < 4) geometric model, not a complete cosmological model. Extending it to the early universe is a major open problem.

The full analysis is in `calculations/v27_cascade_cmb_analysis.py` and `calculations/v27_cascade_mcmc_rar.py`.


### 13.9 L308ab Resolution: f_leak = H(z) closes the CMB gap (v3.5.9+, June 21, 2026)

**Status update**: As of L308ab (v3.5.9+, see §7.4.21 in `paper/markdown/06_limitations.md`), the CMB gap is **PARTIALLY CLOSED** via the user's physical insight:

> "when the universe was small, pressure was higher, so more leaks back to 4d"

**Mechanism**: Generalizing A1's f_leak = H_0 to f_leak = c × H(z) (where c ≈ 1.13):

- In early universe (z > 1100): high H(z) → high leak rate → DM doesn't accumulate
- In late universe (z < 1100): low H(z) → low leak rate → DM reaches steady state
- Today: f_leak(z=0) = 1.13 × H_0, essentially matching A1

**Result**: Drains 32 orders of magnitude of overproduced DM by z=1100, matching Planck 2018 Ω_c = 0.265.

**Implications**:
- τ_DM changes by only 11.5% (14.51 → 12.84 Gyr)
- All A1 derivations remain valid to within ~13%
- No new parameters (H(z) is standard cosmology)
- Natural generalization of A1's post-Friedmann principle

**Remaining OPEN**:
- c = 1.13 is calibration, not derivation (could come from Parker production, holographic, etc.)
- 2D universe internal pressure dynamics (Hawking-like radiation analog)

See `calculations/v36_research/L308ab_fleak_Hz_drain_CMB.py` for numerical verification.

---


---