<!-- 11_testable.md - part of paper.md split (v3.0.13) -->

## 11. Testable Predictions for Current and Upcoming Surveys (2026–2034)

While §10 focuses on the speculative end-of-universe extension, SIDC's *core* mechanism (DM as cumulative 2D universe back-projection) makes specific, near-term testable predictions for ongoing and upcoming surveys. This section consolidates the most important such predictions, anchored to the **47 Tucanae (NGC 104) test case** in the context of the **Rubin/LSST Data Preview 1 (DP1)**, released June 30, 2025.

### 11.1 Why 47 Tuc is a CLEAN test of SIDC's DM mechanism

SIDC predicts that **DM is the cumulative 2D universe back-projection from energetic 3D events**. A *direct* consequence: **DM should track energetic activity over cosmic time**. Objects with NO current energetic activity should have NO local DM enhancement; they should be tracers of the surrounding Galactic DM halo only.

47 Tucanae (NGC 104) is the *cleanest* test of this prediction:
- **No current massive star formation** (all O/B stars died > 1 Gyr ago)
- **No current core-collapse supernovae** (none in > 1 Gyr, none expected)
- **No current Type Ia supernovae** (theoretical rate ~ 1 per 10,000 yr, no events in recorded history)
- **Only ~20 millisecond pulsars** (energetic but their flares are ~$10^{40}$ J, sub-second 2D universes)
- **Mass dominated by ~$10^{6}$ old, low-mass stars** (M < 0.9 $M_\odot$, mostly main-sequence + RGB)

SIDC prediction: **47 Tuc's dynamical mass ≈ its stellar mass**. No local DM spike. The 5 known tidal tails should be consistent with the *Galactic* DM potential, not any local 47 Tuc contribution.

### 11.2 Quantitative prediction for 47 Tuc

See `calculations/v27_47_tuc_cascade.py` for the full calculation. Key numbers:

| Quantity | Value | Source |
|---|---|---|
| Distance from Sun | 4.52 ± 0.03 kpc | Gaia DR3 |
| Galactocentric distance | 7.4 kpc | from Sun distance + Galactic center |
| Current mass ($M_{dyn}$) | $7 \times 10^{5}$ $M_\odot$ | σ_v = 11.7 km/s |
| Half-mass radius | 6.0 pc | literature |
| Velocity dispersion | 11.7 km/s | literature |
| M/$L_V$ (observed) | ~1.7 | literature |
| M/$L_V$ (predicted, 12 Gyr, [Fe/H] = −0.78) | ~1.7 | PARSEC isochrones |
| Age | 12 Gyr | literature |
| Central BH upper limit | 578 $M_\odot$ (3σ) | Della Croce+ 2024, A&A |
| Tidal tails | 5 known | Shipp+ 2021, Ibata+ 2024, Boldrini+ 2024 |

**SIDC calculation results:**

1. **Current 2D universe creation rate:** essentially **ZERO** in 47 Tuc. No current SN. The most energetic current events are ms-pulsar giant flares (~$10^{40}$ J, ~$10^{-3}$ /yr, $\tau_{2D}$ ~ $230$ μs) and recurrent novae (~$10^{39}$ J, ~$10^{-3}$ /yr, $\tau_{2D}$ ~ $11$ μs). All of these are microsecond-scale 2D universes that die essentially instantly and contribute negligible DM.

2. **Cumulative 2D universe contribution over 12 Gyr:** at formation, 47 Tuc had ~$10^{4}$ O/B stars, each producing a SN at ~$10^{44}$ J. Total SN energy ~ $10^{48}$ J. With SIDC's $f_{\rm back}$ ~ $10^{-85}$, the resulting DM contribution is:
   - E_DM = $10^{48}$ × $10^{-85}$ = $10^{-37}$ J = **$5.6 \times 10^{-85}$ $M_\odot$**
   - **Completely negligible.** The SN energy that did become 2D universe mass contributes essentially zero to 47 Tuc's local DM.

3. **Density comparison (47 Tuc vs Galaxy's halo DM):**
   - Galaxy's NFW DM density at 7.4 kpc Galactocentric: **$\rho_{\rm DM,galaxy} \approx 0.061$ GeV/${\rm cm}^3$** (with $\rho_s = 0.32$ GeV/${\rm cm}^3$, r_s = 21.5 kpc)
   - 47 Tuc's *central* density (within r_core = 0.5 pc): **$\rho_{\rm core} \approx$ 7.3 GeV/${\rm cm}^3$** — ~ $120 \times$ the Galaxy's local DM
   - 47 Tuc's *average* density (within $r_h = $6 pc): **$\rho_{\rm avg} \approx$ 0.029 GeV/${\rm cm}^3$** — ½× the Galaxy's local DM
   - **47 Tuc is a dense stellar system embedded in a sparse DM halo.** The Galaxy's DM halo *passes through* 47 Tuc but is locally overwhelmed by 47 Tuc's baryonic concentration.

4. **Mass budget:** $M_{dyn}$ ≈ $7 \times 10^{5}$ $M_\odot$; $M_{stars}$ (from CMD + IMF) ≈ $5.5 \times 10^{5}$ $M_\odot$. The "missing" $1.5 \times 10^{5}$ $M_\odot$ (21% of $M_{dyn}$) is **within the 20-30% uncertainty** of IMF, mass segregation, binary fraction, and velocity anisotropy. Consistent with **no local DM enhancement**.

5. **Central BH (≤ 578 $M_\odot$):** the BH formation event ~12 Gyr ago released E_BH ~ $10^{49}$ J, creating a 2D universe with $\tau_{2D}$ ~ $3$ yr (energy-scaling rule). The 2D universe died long ago; energy was returned to 3+1D. With $f_{\rm back}$ ~ $10^{-85}$, the BH's DM contribution is **~$10^{-84}$ $M_\odot$** — zero. The BH's gravitational influence on 47 Tuc is via standard GR (it acts as a point mass), not via 2D universe back-projection.

6. **Mass loss over 12 Gyr:** dM/dt from 2-body relaxation is ~$2 \times 10^{-6}$ $M_\odot$/yr (negligible). Stellar evolution mass loss is ~30% of initial mass. Total: ~$3 \times 10^{5}$ $M_\odot$ lost, leaving the observed $7 \times 10^{5}$ $M_\odot$. The 5 known tidal tails (Shipp+ 2021, Ibata+ 2024, Boldrini+ 2024) contain ~0.5% of the cluster mass and are consistent with Galactic tidal stripping + 47 Tuc's complex orbit.

### 11.3 Testable predictions for Rubin/LSST DP1, DR1, and Y10

SIDC's prediction for 47 Tuc can be tested at three time horizons:

**DP1 (released June 30, 2025; WCS FITS fix Jan 8, 2026):**
- **What DP1 contains:** 4 nights of LSSTComCam (commissioning camera) observations of 47 Tuc field, ugrizy bands. Plus 6 other ~1 sq deg fields = ~7 sq deg total.
- **SIDC prediction:** 47 Tuc's color-magnitude diagram (CMD) is **consistent with single-population 12 Gyr stellar evolution** (PARSEC or BaSTI isochrones, [Fe/H] = −0.78). The mass function should follow a standard IMF (Kroupa or Chabrier). No evidence of a "DM-modified" mass function. Stars should appear with masses consistent with standard stellar evolution.
- **Test:** compare observed CMD + mass function to PARSEC/BaSTI isochrones. Look for systematic deviations that would indicate a non-stellar mass component.
- **Why it matters:** DP1 primarily validates Rubin's crowded-field photometry pipeline. SIDC predicts a *null* result (no DM component in the stars themselves) — a baseline check before more sensitive tests.

**DR1 (LSST Y1, expected 2027):**
- **What DR1 contains:** First full LSST data release, ~18,000 sq deg wide-fast-deep survey. Proper motions for ~$10^{9}$ stars to ~24th mag. 47 Tuc will have ~$10^{6}$ stars with proper motion measurements.
- **SIDC prediction:** 47 Tuc's proper motion field is **consistent with Galactic rotation + dynamical friction** in the Galactic NFW potential. The 5 tidal tails should be **kinematically consistent with 47 Tuc's orbit** through the Galaxy, with no evidence of local 47 Tuc DM enhancement (e.g., no anomalous velocity dispersion in the tails beyond what Galactic tides predict).
- **Test:** fit 47 Tuc's orbit in the Galactic potential using Gaia+LSST proper motions. Use tail kinematics to constrain the local DM density at 47 Tuc's location.
- **Why it matters:** A direct test of whether 47 Tuc's dynamics are governed by Galactic DM or have a local component.

**LSST Y10 (~2034):**
- **What Y10 contains:** Final 10-year LSST data, ~30 mag depth in coadds. Mass function precision ~1% for bright stars, ~10% for faint. Ultra-faint tidal features visible to ~100 kpc from 47 Tuc.
- **SIDC prediction:** No "dark star" component in 47 Tuc. All stars in the CMD are normal, single-population, 12 Gyr old. The mass function should match a standard IMF at the low-mass end (~0.1 $M_\odot$) with no excess of "phantom" mass.
- **Test:** count stars vs mass function prediction. Look for "missing" mass in the low-luminosity end. Search for ultra-faint tidal features that would indicate DM substructure.
- **Why it matters:** A direct count of stellar mass vs total dynamical mass. If SIDC is right, the two should match within IMF uncertainties.

### 11.4 Falsifiability matrix for the 47 Tuc test

SIDC's prediction for 47 Tuc is *falsifiable* by the following observations:

| Observation | SIDC prediction | Falsification criterion |
|---|---|---|
| $M_{dyn}$ / $M_{stars}$ ratio | 1.0 ± 0.3 (IMF + anisotropy) | If $M_{dyn}$ / $M_{stars} > 2$ at 3σ, local DM detected → SIDC falsified |
| Tidal tail symmetry in cluster rest frame | Symmetric (within orbit projection) | If tails are anomalously asymmetric, requires local DM → SIDC falsified |
| CMD vs PARSEC isochrones | Matches 12 Gyr single-population | If systematic offset in mass function, "DM-modified" stars → SIDC falsified |
| Central BH mass | ≤ $10^{4}$ $M_\odot$ (consistent with no local DM spike) | If BH > $10^{4}$ $M_\odot$ detected, would create real local DM spike → SIDC testable but not falsified |
| Tidal tail kinematics | Consistent with Galactic NFW potential | If tails require local 47 Tuc DM, would imply missing component → SIDC falsified |
| 47 Tuc proper motion | Galactic rotation + dynamical friction in NFW | If PM requires local DM beyond NFW, SIDC is incomplete |

### 11.5 Connection to SIDC's DM mechanism

The 47 Tuc test is a *direct* test of SIDC's core claim (§2.4–2.7): **DM is the cumulative 2D universe back-projection from energetic 3D events**. SIDC's prediction is *qualitatively* clear: objects with no current energetic activity should have no local DM enhancement. 47 Tuc is the *cleanest* such object — a massive, nearby, well-studied globular cluster with **zero** current SN activity and **zero** current massive star formation.

SIDC's prediction is *quantitatively* clean: the SN energy from 47 Tuc's formation would have created 2D universes, but the $f_{\rm back}$ ~ $10^{-85}$ suppression means the DM contribution is ~$10^{-85}$ $M_\odot$ — effectively zero. The 47 Tuc test therefore isolates the *Galactic* DM halo from any *local* 2D universe contribution.

If 47 Tuc's dynamical mass significantly exceeds its stellar mass ($M_{dyn}$ / $M_{stars} > 2$ at 3σ), this would imply a local DM component that SIDC cannot explain. This would be a **strong falsification** of SIDC's "no current activity → no local DM" prediction, though it would not necessarily falsify SIDC as a whole (the *Galactic* DM contribution would still be consistent).

Conversely, if 47 Tuc's dynamical mass matches its stellar mass within IMF uncertainties (SIDC's prediction), this would be a **strong confirmation** of SIDC's DM mechanism, supporting the link between *energetic activity* and *local DM enhancement* that SIDC proposes.

### 11.6 Generalization: other testable predictions from SIDC's DM mechanism

The 47 Tuc test is one specific case. SIDC's DM mechanism makes related predictions for other low-activity systems:

1. **Other old, quiescent globular clusters** (e.g., M92, NGC 6397): should have $M_{dyn}$ / $M_{stars}$ ~ $1$, with the *cluster* as a tracer of the *Galactic* DM halo.

2. **Dwarf spheroidal galaxies with no current star formation** (e.g., Tucana, Draco, Sextans): SIDC predicts that *most* of their DM is the *Galactic* halo contribution plus the cumulative 2D universe contribution from their *past* star formation (which was significant in early epochs). The KKR 25 case (1-4 Gyr ago starburst) is the *opposite* extreme.

3. **The Galactic bulge:** should have $M_{dyn}$ / $M_{\rm bulge,\star}$ ~ 1 (or slightly above due to nuclear star formation history). SIDC predicts that the bulge's "DM" is mostly the *Galactic* halo DM, with some 2D universe contribution from the bulge's past activity.

4. **The Galactic halo's old, metal-poor stars (halo stars):** should not be associated with any local DM enhancement beyond the smooth halo. SIDC's prediction is consistent with the standard picture: halo stars are tracers of the Galactic potential, not DM hosts.

5. **The Magellanic Clouds:** should have $M_{dyn}$ / $M_{stars}$ ~ $1$ in their *outer* regions (no current activity beyond tidal interactions) and possibly higher in their *inner* regions (where past star formation created local 2D universe DM).

These are *all* testable with current and upcoming data (Gaia, LSST, DESI, 4MOST, WEAVE), and SIDC's predictions are *specific enough to be falsified* if the data demand.

### 11.7 Summary

SIDC's DM mechanism — DM is the cumulative 2D universe back-projection from energetic 3D events — makes specific, testable predictions for objects with no current energetic activity. **47 Tucanae (NGC 104) is the cleanest such test case**, and the **Rubin/LSST DP1 (June 2025), DR1 (Y1, 2027), and Y10 (~2034)** are the relevant data releases.

- **DP1 (2025):** validates Rubin's crowded-field pipeline; SIDC predicts standard 12 Gyr single-population CMD.
- **DR1 (2027):** 47 Tuc's proper motion + 5 tidal tails should fit the Galactic potential; no local DM needed.
- **Y10 (2034):** no "dark star" component; all stars are normal, $M_{dyn}$ ≈ $M_{stars}$.

**Falsification:** $M_{dyn} > 2$× $M_{stars}$ at 3σ, or asymmetric tidal tails, or DM-modified mass function — any of these would require local 47 Tuc DM that SIDC cannot produce.

The 47 Tuc test is a **near-term, low-cost, high-leverage falsification test** for SIDC. It does not depend on the speculative end-of-universe extension in §10. It tests the **core** of SIDC: the link between *energetic activity* and *local DM enhancement*. If the link is wrong, SIDC's DM mechanism is wrong.

The full calculation is in `calculations/v27_47_tuc_cascade.py`.

---

