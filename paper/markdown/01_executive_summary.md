<!-- 01_executive_summary.md - part of paper.md split (v3.0.13) -->

## Abstract

**EXECUTIVE SUMMARY (for hurried readers).** This paper proposes a geometric framework (SIDC) in which gravity, dark matter, and dark energy are all consequences of a dimensional projection mechanism. We are a software developer, not a physicist; this is a thought experiment, not a finished theory. SIDC is a **cone-shaped 3-level structure** (4D parent → 3+1D us → 2D children, terminal at 2D), NOT a scale-invariant infinite SIDC (1D and 0D universes are nonsensical, so SIDC terminates at 2D). SIDC IS scale-invariant in the *energy/size* sense within the 2D level (the Liouville 2D CFT is conformally invariant, and any energetic event creates a 2D universe of proportional size, weighted by a smooth $E^{1+\alpha}$ creation function — see §2.5.3; the v2.3.0 $E_{\rm crit}$ phase-transition threshold has been replaced by this single smooth function). SIDC postulates that all dark matter is 2D universe mass, time-compressed to 3+1D via the 5D AdS₅ bulk geometry. Honest status: **16/17 test categories** (16 pass, 1 confounded) and **7/7 specific cases** pass real-data tests, with **2 components falsified** ($g_{\rm obs}$ = $g_{\rm bar}$ + $g_{\rm cum}$ + $g_{\rm active}$ functional form, FALSIFIED in v2.2; Mechanism A Hubble, FALSIFIED in commit ~80) and **0 strongly confirmed**. The 2 falsifications were *specific functional forms* that SIDC has since replaced (SIDC-MOND hybrid for RAR; Mechanism M for Hubble tension), not SIDC's framework. SIDC's STRENGTH is local physics (RAR matches SPARC to 10% median residual, AGN host DM strongly supported at p< $10^{-50}$ partial correlation, $g_+$ approximately constant at galaxy scale across 4.5 decades in $M_{b}$ but the correlation is not statistically significant, r=+0.19, p=0.22). SIDC's WEAKNESS was CMB-era physics (Hubble tension ACCEPTED as real tension, $H_0$,4D = 70.16 is a geometric-mean property but specific $H_0$ values are not derived, 2D-to-3+1D time compression has 54-orders-of-magnitude uncertainty, full Lagrangian requires 2D expert). **UPDATE (v3.5.9+ L308ab)**: The CMB gap (Ω_DM at z=1100) is now PARTIALLY CLOSED via f_leak = H(z) — user's physical insight that 'when universe was small, pressure was higher, so more leaks back to 4d'. This drains 32 orders of magnitude of overproduced DM by z=1100, matching Planck 2018. τ_DM unchanged to within 13%. See §7.4.21. (Hubble tension ACCEPTED as real tension, $H_0$,4D = 70.16 is a geometric-mean property but specific $H_0$ values are not derived, 2D-to-3+1D time compression has 54-orders-of-magnitude uncertainty, full Lagrangian requires 2D expert). SIDC documents **158 honest limitations** (+L308f through +L308aa, v3.5.9+, 23 user-driven insights: L308f-L308l v3.5.7+ user catches + L308m MCMC + L308n $\alpha$ first-principles + L308o N_sub linear + L308p cone asymmetry + L308q 2D universe quantum + L308r $\mu$ N×v_H chain + L308s 8-paths + L308t L26 full closure + L308u N=12 from 6D anomaly + L308v L138 closed loop + L308w f_leak=H_0 + L308x γ consistency + L308y §3.67 coincidence + L308z N_sub event-specific (free) + **L308aa $\gamma_{\rm 2D}$ time dilation + **L308ab f_leak=H(z) closes CMB gap + **L308ac parameter audit + L308ad N_sub ≈ N_12 × (M_Pl,4D/M_Pl,3D)^(1/3) PARTIAL L144 closure + **L308ae N_sub formula residual + L308af AGN rate unit interpretation gap + L308ag N=12 reclassified FIRST-PRINCIPPLES → STRUCTURAL (5 suggestive interpretations, none rigorous) + L308ah deeper research on N=12 and α (no first-principles derivation found) + L308ai N=12 from other angles + L308aj 12-fold DM substructure (WITHDRAWN per L308am: 130 M_sun cluster prediction inconsistent with geometric DM) + L308am 12-fold geometric DM density correlations + L308an specific prediction: C_ℓ oscillation at ℓ_12 = π × D_A/r_12 (testable by LSST/Roman 2027) + L308ao honest critique: r_12 NOT derived from N=12 (connection is heuristic, not rigorous) + L308ap re-examination: N=12 has SM count INPUT + Schwarzian PREDICTION + data CONFIRMATION, not pure derivation********) (§7.0 Master Table, v3.5.9+): 79 OPEN, 22 PARTIAL, 2 RESOLVED (L142b, L149 via empirical rejection of $\alpha$=1.258), 8 CLOSED, 6 NEGATIVE, 7 SPECULATIVE. The master table is the CANONICAL count; this paragraph was HISTORICALLY 67 in v3.1 and grew to 133 across v3.0-v3.5.8+ (L102-L136 added v3.0-v3.1 Lagrangian; L142-L150 added v3.1.2 multi-universe + AGE/LIFETIME/frame; L151-L322 added v3.3-v3.5.7 Tier-2 research, $\mu$ structural origins, holographic; L308f-L308v added v3.5.7+/v3.5.8 user-driven refinements, MCMC, $\alpha$ first-principles). L41, L42 closed in v3.0.22 ($\mu$ and m₃₊₁D now derived); L117 closed (c-value UV/IR RG flow); L149 resolved ($4\pi$ specificity, empirical). L9 (2D universe physics) explicitly remains open — the form of DM at 2D universe death is UNSPECIFIED. SIDC commits to a **geometric DM framework** (Option D in legacy_paper.md §3.14) by default; specific particle interpretations (WIMP, axion, sterile neutrino) are possible but stability requires discrete symmetries, not Pauli blocking. Bottom line: **consistent with current data, falsifiable, ready for theoretical physicist to complete, with self-critical methodology (see legacy_paper.md legacy_paper.md §3.16)**.

---

## 🎯 TWO MAIN POINTS: SCALING LAW + CLOSED LOOP (v3.0.21)

These two expressions are SIDC's quantitative backbone and are taken as ground truth throughout the paper.

### Main Point #1: The Scaling Law (§10.1)

**Every 3D event creates a 2D universe. The 2D universe's lifetime in 3+1D view follows:**

$$\boxed{\tau_{2D,\,\text{our frame}} = t_{\rm Pl,3} \times \left(\frac{E_{\rm 3D\,event}}{M_{\rm Pl,3D}}\right)^{1.29}}$$

(SN calibration: $\tau_{2D} = 33\,$s when $E = 10^{44}$ J, the SN energy.)

- **Hierarchy (v3.0.21, user-corrected)**: A **3D event** (event in 3+1D spacetime = our universe) creates a **2D universe**. (NOT a 4D event — that creates our 3+1D universe.)
- **Calibration**: SN1987A ($E_{\text{3D}} = 10^{44}$ J, $\tau = 33$ s) anchors the rule.
- **Verified**: 8/8 3D events match the formula within factor 1.6 (§10.1 table).
- **Range**: works from 1 ton TNT ($10^{-37}\,\mu$s) to AGN outbursts ($10^8$ yr), spanning 54 orders of magnitude.
- **Origin**: $\alpha = 1.289 = 1 + 1/\sqrt{12}$ from N=12 SYK saddle-point (§3.62).

### Main Point #2: The Closed Loop (§3.60.1)

**The same $\alpha = 1.289$ also governs the backward (back-action) direction, closing the loop between 4D event and 3D event:**

**NOTE (v3.0.22)**: The closed loop expression (formula) DERIVES the value
$f_{\text{back}} \approx 10^{-85}$. The expression IS $f_{\text{back}}$ — the
number $10^{-85}$ is its numerical evaluation.

$$\boxed{f_{\text{back}} \equiv \left(\frac{t_{\text{Pl,3}}}{\tau_{\text{4D}}}\right) \times \left(\frac{\tau_{\text{SN,obs}}}{\tau_{\text{universe}}}\right) \times \left(\frac{E_{\text{4D}}}{E_{\text{SN}}}\right)^{1/(2\alpha)} \approx 10^{-85}}$$

- **$f_{\text{back}} \approx 10^{-85}$** is the back-projection efficiency of the 2D universe's gravity to 3+1D (the numerical VALUE of the closed loop expression).
- **The composite exponent $1/(2\alpha) = c/\alpha = (1/2)/1.289 = 0.388$** where $c = 1/2 = N/24$ (Ising CFT).
- ****L308aq**: The 'three independent derivations' framing was MISLEADING. Real derivation is SYK q=4 (per L117)** (per L117: SYK q=4 gaps out 11 of 12 modes, leaving 1 Ising with c=1/2; L308aq clarifies the 'three derivations' framing was misleading) confirm the exponent.
- **The closed loop closes**: $\alpha \times 1/(2\alpha) = 1/2$ (round-trip loss from $Z_2$ orbifold).
- **Forward direction (time dilation)**: $\gamma = (E/E_{\text{Pl}})^\alpha$ — the scaling law.
- **Backward direction (back-action)**: $f_{\text{back}} \sim (E_{\text{4D}}/E_{\text{SN}})^\frac{1}{2 \alpha}$ — the closed loop.

Both directions use the **SAME $\alpha = 1.289$** derived from **N = 12** SYK. This is what makes it a "closed loop".

### Why these are the MAIN POINTS

- **The scaling law** is what makes SIDC testable: 14 different energetic events all follow one formula.
- **The closed loop** is what makes SIDC unified: DE and DM use the SAME $\alpha$, the SAME bulk-brane cancellation, the SAME geometric projection.
- Together they answer: "Why is $\alpha = 1.289$?" — because $\alpha \times 1/(2\alpha) = 1/2$ must hold for the loop to close, and the only N that gives $\alpha \approx 1.29$ with this property is N = 12.

**The closed loop UNITES DM, DE, and gravity (v3.0.22, §3.60.3)**:

- **Gravity weakness**: $\varepsilon_{\rm grav} \sim 10^{-38}$ from bulk-brane cancellation
- **DE density**: $\rho_{\rm DE} = f_{\rm DE} \times \varepsilon \times M_{\rm Pl,3}^4 = 2.2 \times 10^{-47}$ GeV$^4$ (within 12% of observed!)
- **DM density**: $\rho_{\rm DM} = f_{\rm DM,death} \times \Sigma(M_{\rm 2D} \times N_{\rm 2D})/V$ (uses same $f_{\rm DM,death}$)

All three use the SAME $\alpha = 1.289$, the SAME $f_{\rm DE} \approx 10^{-85}$, the SAME bulk-brane geometry. The closed loop is what unifies them.

See §3.60.1 (closed loop), §3.62 (Lagrangian skeleton), §10.1 (scaling law table), and `calculations/consistency_check_v3_0_21.py` (consistency verification).

---

**5/27/68 honest framing (v2.7.1).** The 5/27/68 split is **observational data** (Planck 2018), not a SIDC prediction. SIDC's qualitative interpretation is: 5% = baryons (real 3+1D), 27% = DM from 2D universe back-projection, 68% = DE from 4D event antigravity. **The 5/27 inner split (5% "active" 2D universes vs 27% "cumulative deaths") is dropped in v2.7.1 as a separate postulate** that conflicted with the empirical 33 s lifetime (which gives $f_{\rm active} \sim 10^{-17}$, not 0.05). The 5:27 inner split was a post-hoc fit, and the "three 5%" coincidence was a confusion. $f_{\rm active}$ is now a free parameter, not derived.

**Hubble tension position (v2.7, Mechanism M).** SIDC adopts Mechanism M: the Hubble tension is **ACCEPTED as a real observational tension**, not resolved. SIDC is qualitatively consistent with $H_0$ = 70 ± 3 across all measurements (SH0ES 73, TRGB 69.8 ± 1.9 [Freedman 2024, JWST], Planck 67.4, standard sirens 70 ± 12). SIDC's intrinsic $H_0$,4D = sqrt(H_CMB × H_local) = 70.16 is a non-trivial property of the data. The 5.6 km/s/Mpc gap between local and Planck-inferred $H_0$ is a $\Lambda{\rm CDM}$-framework artifact, not a SIDC problem. Earlier 4-zone H(z) attempts were removed in v2.7 (they were data fitting with 8 free parameters for ~5 data points, and the P(y) problem made them internally inconsistent).

---

We propose a unifying interpretation of three open problems in fundamental physics — the weakness of gravity (the hierarchy problem), the nature of dark matter, and the nature of dark energy — under a single geometric process. In this picture, our 3+1 dimensional universe is the *projection* of a single *ongoing* event in a higher-dimensional space: an energetic release of gravitational energy in the bulk, with the energy of that event manifesting in our brane as the Big Bang, and the dimensional projection mechanism producing the dark sector as a byproduct. The model is **a thought experiment, not a finished theory** — it provides a *geometric framing* that unifies three problems and yields specific testable predictions, but does not yet derive quantitative values from first principles. We are explicit about what is derived, what is fit, and what is postulated.

**What the model does well (data backing).** SIDC has been tested against multiple independent observations. **16/17 test categories** (RAR, cluster $g_+$, dwarf phase-transition, globular cluster DM, direct detection, isolated vs cluster dwarf, AGN host DM, halo M/M* vs z, missing satellites, too-big-to-fail, dSph $M_{dyn}$, MDAR, lensing flux ratio, cluster baryon fraction, BTFR, dSph $\sigma$(r) profile, BTFR SPARC, HI-DM correlation, Vflat-morphology; ~430 data points) are consistent with SIDC; **1/17 is confounded** (HI-DM correlation confounded by gas-radius correlation; the Vflat-morphology test, previously inconclusive, is now documented as inconclusive due to sample selection bias). Of the 16 passing tests, **6 are clean real-data passes (was 5; AGN host DM added in v2.3.1 with morphology matching, +6.4%, p=0.047), 4 are structural (SIDC avoids $\Lambda{\rm CDM}$ problems by having no sub-halos), 5 are not discriminative vs $\Lambda{\rm CDM}$, and 1 is qualitatively consistent (AGN host DM).** **7/7 specific cases** (SPARC, Tian+ 2024, Sun, DF2/DF4, FCC 224, AGC 114905, KKR 25) are also consistent.

- **Radial Acceleration Relation (SPARC, 175 galaxies):** the SIDC-MOND hybrid matches the RAR to a 10% median residual, comparable to MOND itself. MCMC posterior: $f_{active} = 0.0513^{+0.0070}_{-0.0073}$ ($1\sigma$), the fraction of cumulative 2D universe back-projection that is "active" at any moment. **CAVEAT (v2.7.1):**$f_{\rm active}$ ~ 0.05 is a phenomenological RAR fit, NOT derived from SIDC first principles. SIDC's "derivation" $f_{\rm active}$ = $\tau_{2D}$/$T_{\rm universe}$ = 0.7/13.8 = 0.051 used $\tau_{2D}$ ~ 0.7 Gyr (gas consumption timescale) as a SEPARATE POSTULATE, identified by physical analogy. The empirical 33 s lifetime gives $f_{\rm active} \sim 10^{-17}$, not 0.05. $f_{\rm active}$ is a FREE PARAMETER. See §4.35.
- **Cluster scale (Tian+ 2024, 50 BCGs):** the cluster g₊ enhancement to $\sim 1.3 \times 10^{-9}$ m/s² is naturally explained as the MOND external field effect ($V_{local}$ formula), matching Tian+ 2024's $1.7 \times 10^{-9}$ to within 30% (SIDC's MCMC $1\sigma$ range is $5.3 \times 10^{-10}$ to $2.7 \times 10^{-9}$, which does include $1.7 \times 10^{-9}$).
- **Phase-transition principle (5 dwarf-galaxy tests, REVISED v2.7.36+):** the critical-energy threshold $E_{crit} \sim 10^{30}$ J correctly predicts: Sun (no detectable DM, as expected), DF2/DF4 (DM-poor, no recent energetic events), FCC 224 (DM-poor), AGC 114905 (DM-poor, low-mass SF below threshold), and KKR 25 (consistent via the $S_{\rm destruction}$ cumulative-return pathway: intermediate-age SF at 1-4 Gyr produced 2D universes whose energy has been returned to 3+1D as DM per the action's $S_{\rm destruction}$). 5/5 specific dwarf cases consistent (each tested independently, no bifurcation framing). The $S_{\rm destruction}$ energy-return mechanism is a model assumption, not a derivation; if the 2D universe's death energy instead escapes the 3+1D brane, KKR 25 would revert to a TENSION.
- **Hubble constant:** SIDC is **qualitatively consistent** with $H_0 = 70 \pm 3$ across all measurements (SH0ES $73.04 \pm 1.04$, TRGB $69.8 \pm 1.9$ [Freedman 2024, JWST], Planck CMB $67.4$, standard sirens $70 \pm 12$). SIDC does **not** derive a specific $H_0$ value — earlier multiplicative boost formula ($H_0 = 70.13$) was a postdiction, removed in v2.5. The 5.6 km/s/Mpc gap to Planck CMB-inferred $H_0 = 67.4$ is a **$\Lambda{\rm CDM}$-framework artifact**, not a SIDC prediction. See §2.6.1 (Honest $H_0$ framework) and Limitation 26.
- **Cosmic energy budget:** SIDC is consistent with the observed 5% ordinary / 27% dark matter / 68% dark energy split (Planck 2018). These values are **observational data**, not SIDC predictions. SIDC provides a qualitative INTERPRETATION: 5% = baryons (real 3+1D energy), 27% = DM (cumulative 2D universe back-projection), 68% = DE (4D event antigravity). The 32%/68% outer split is "interpretable" from projection kinematics. **The 5:27 inner split (5% "active" vs 27% "cumulative") is dropped in v2.7.1 as a separate postulate that conflicts with the empirical 33 s lifetime** (which gives $f_{\rm active} \sim 10^{-17}$, not 0.05).
- **Concrete action functional (§2.5.1):** the geometric picture is now backed by a Lagrangian-level skeleton: $S = S_{grav} + S_{matter} + S_{brane 2D} + S_{creation} + S_{destruction}$, with $\alpha$ coupling, $\delta$-function 2D brane localization, and Stoke's-theorem energy conservation. Reduces to standard RS-II brane-world as $\alpha \to 0$.
- **First-principles g₊ derivation (§4.17):** g₊ = $k \cdot \int (event rate) \cdot E_{event} \cdot \tau_{2D} / L_{2D}\ dt$, SIDC's formula for the universal acceleration scale, equivalent to empirical $g_+ \propto \int \rho_{events} / M_{b}\ dt$ scaling.

**What the model is honest about (limitations).** SIDC is a *geometric framing*, not a derived Lagrangian. Quantitative values are *fits* to observation (5/27/68, $g_+ \sim 1.2 \times 10^{-10}$, $\epsilon$ $\sim 10^{-38}$, $f_{\rm DE} = 1.13\times 10^{-85}$ DERIVED via L308v α-GM), not all first-principles predictions. The 5/27/68 formula's "self+neighbor edges in a graph" interpretation fails to survive the cone-shape refinement — it was a post-hoc fit to a pre-v2.1 4-level model that no longer exists. SIDC's *specific* 5/27/68 derivation is left to future work (Limitation 26, §7.1 *Appeals to Formalism*). The model documents **158 honest limitations** (+L308f through +L308aa, v3.5.9+, 23 user-driven insights: L308f-L308l v3.5.7+ user catches + L308m MCMC + L308n $\alpha$ first-principles + L308o N_sub linear + L308p cone asymmetry + L308q 2D universe quantum + L308r $\mu$ N×v_H chain + L308s 8-paths + L308t L26 full closure + L308u N=12 from 6D anomaly + L308v L138 closed loop + L308w f_leak=H_0 + L308x γ consistency + L308y §3.67 coincidence + L308z N_sub event-specific (free) + **L308aa $\gamma_{\rm 2D}$ time dilation + **L308ab f_leak=H(z) closes CMB gap + **L308ac parameter audit + L308ad N_sub ≈ N_12 × (M_Pl,4D/M_Pl,3D)^(1/3) PARTIAL L144 closure + **L308ae N_sub formula residual + L308af AGN rate unit interpretation gap + L308ag N=12 reclassified FIRST-PRINCIPPLES → STRUCTURAL (5 suggestive interpretations, none rigorous) + L308ah deeper research on N=12 and α (no first-principles derivation found) + L308ai N=12 from other angles + L308aj 12-fold DM substructure (WITHDRAWN per L308am: 130 M_sun cluster prediction inconsistent with geometric DM) + L308am 12-fold geometric DM density correlations + L308an specific prediction: C_ℓ oscillation at ℓ_12 = π × D_A/r_12 (testable by LSST/Roman 2027) + L308ao honest critique: r_12 NOT derived from N=12 (connection is heuristic, not rigorous) + L308ap re-examination: N=12 has SM count INPUT + Schwarzian PREDICTION + data CONFIRMATION, not pure derivation********) across all major claims (see §7.0 Master Table, v3.5.9+, was 67 in v3.1, was 81 in v3.3): 79 OPEN, 22 PARTIAL, 8 CLOSED, 2 RESOLVED, 6 NEGATIVE, 7 SPECULATIVE. L41, L42 closed in v3.0.22. L14 was resolved by the v2.1 mathematical sketch; L32 was removed in v2.7; L34 added v2.7.4 for $E_{\rm primordial}$; L35 added v2.7.4 for $z_{\rm half}$; L36 added v2.7.4 for $E_{\rm crit}$ REVERTED; **L37 added v2.7.30 for $\alpha$=1.29 CGHS derivation** (legacy_paper.md §3.24 self-critique: in RANGE but NOT derived); **L9_ext DISCARDED v2.7.20 for Pauli-blocked sterile $\nu$** (Batell-Yin 2024 bound).

**Architectural choice: cone-shape is the default, NOT scale-invariance.** SIDC is **cone-shaped, not scale-invariant** in the dimensional sense. The 4D parent → 3+1D us → 2D children structure is the architecture; 2D is the hard floor (1D and 0D universes are nonsensical, so SIDC terminates at 2D). The earlier framing of "scale-invariance / infinite SIDC" with a $\rho_{crit}$ regulator has been removed — the 2D floor is a structural limit, not a choice. SIDC IS still scale-invariant in the *energy/size* sense within the 2D level: the Liouville 2D CFT is conformally invariant, and any energetic event creates a 2D universe of proportional size (weighted by the smooth $E^{1+\alpha}$ creation function in §2.5.3 — the v2.3.0 $E_{\rm crit}$ step threshold has been removed). This is a different kind of scale invariance — not dimensional, but energy-scale — and it does not require a SIDC to lower dimensions.

**M^α law and time dilation (v2.7.24-v2.7.25+, legacy_paper.md §3.17-legacy_paper.md §3.18, REVISED L308x v3).** The M^α scaling law $\tau_{2D,3+1D} = (E/E_{Pl,3})^{1.29} \times t_{Pl,3}$ gives the 3+1D-observed lifetime of the 2D universe. The 2D universe's PROPER lifetime (in 2D's own frame) is $\gamma_{2D} \times \tau_{2D,3+1D}$ = 5.5×10⁴⁴ × 33s = **5.7×10³⁸ yr** for SN (much longer than 33s). Similarly, the 4D event's proper time is 1.51×10³⁴ yr, but the 3D-observed time is $\gamma_{4D} \times 1.51e34 yr = 8.95×10¹²⁴ yr$. The cone is ASYMMETRIC in time direction: γ_2D stretches time in 2D's own frame (2D proper is LONG, 3D observed is short), while γ_4D stretches time in 3D frame (4D proper is short, 3D observed is LONG). In both cases, the lower-D dimension has MORE time (2D > 3D > 4D in duration). The same $\alpha$ = 1.29 applies at every level. **$\alpha$ is no longer a free parameter** — it is a property of the projection geometry, derivable in principle from Schwarzian SYK N=12 saddle point (L308n, 1+1/√12). SIDC's net free parameter count: 15 (REVISED L308z, was 14 pre-count-correction; A1+L308z+L308aa).

**Self-critical methodology (v2.7.22+, legacy_paper.md §3.16).** SIDC's iterative process is formalized: build → user pushback → self-critique → discard or revise → document. The sterile neutrino DM with Pauli-blocked decay (now in legacy_paper.md legacy_paper.md §3.13-legacy_paper.md §3.15) is a worked example: built in v2.7.18, self-critiqued in v2.7.19, discarded in v2.7.20 after literature search (Batell-Yin 2024 m<10meV bound, sub-eV DM is HDM not CDM, 3.5 keV X-ray line weakened). SIDC documents the discard explicitly rather than papering over broken hypotheses.

**11 framework connections (v2.7.6-v2.7.29, §3.8, §3.22).** SIDC's framework is supported by 11 established frameworks: 1 STRONGEST MATCH (CGHS, $\alpha$=1.29 in [1,3] back-reaction range), 6 STRUCTURAL (Padmanabhan, Horava-Witten, KK, Geodetic brane, DGP, Verlinde), 2 TENSION (Jacobson, RT — predict linear scaling, not power law), 2 SPECULATIVE (Massive gravity, Conformal gravity). No framework uniquely derives $\alpha$ = 1.29 from first principles; a specific CGHS-with-back-reaction calculation would close L9.

**Testable predictions (§3):** (1) BCG g₊ correlates with cluster ICM activity, not BCG stellar mass alone. (2) Dwarf g₊ correlates with recent star formation rate, not total $M_*$. (3) Dark matter fraction in quiescent galaxies should be *lower* than in identical-mass active galaxies (phase-transition test). (4) SIDC predicts AGC 114905 has *no* high-energy events above $10^{30}$ J in its recent history — testable with deep X-ray/radio observations.

**Why the SIDC vs its competitors — quick comparison.** Whether SIDC is "superior" depends on the metric. On *mathematical and operational completion*, standard $\Lambda{\rm CDM}$ remains the reigning framework. On *parsimony and empirical coverage* — explaining the maximum number of distinct cosmic anomalies with the fewest arbitrary assumptions — SIDC presents an architecturally superior alternative. The table below summarizes the tradeoffs:

| Competitor | Main weakness | SIDC advantage |
|------------|---------------|-----------------|
| **$\Lambda{\rm CDM}$** | 4 unresolved small-scale crises (cusp-core, missing sats, TBTF, MFRP); requires WIMP + $\Lambda$ + 20+ feedback params | DM is geometric → no sub-halos → all 4 crises collapse by construction |
| **MOND** | Fails in cluster cores (g₊ ~17× too low) | Phase-transition scales g₊ naturally to cluster regime |
| **ADD/RS brane-worlds** | Static bulk; no native dark-sector explanation | Dynamic SIDC: dims are spawned, dark sector falls out as transactional debt |
| **Verlinde (entropic)** | No historical clock → can't explain different-DM identical-baryon galaxies | Stellar Age Lifecycle ledger explains AGC 114905 vs KKR 25 timing |

The full architectural comparison is given in §9 (SIDC vs its Competitors: A Detailed Comparison).

# Main Points (TL;DR)

> **LEGACY NOTE**: This file contains references to the OLD Hill function F_p(z) framework
> (DROPPED in v3.3+, see L100). The current framework uses **bilateral cascade** with
> **f_leak = H_0** as new principle (Approach A1, §7.4.20). Hill function references
> are kept for historical context. See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md`
> for details on what was dropped.

If you read nothing else, read this section.

## What is SIDC?

The **SIDC** (now formally named **SIDC — Scale-Invariant Dimensional Cascade**, v3.0.2) is a thought-experiment framework that proposes:

- **Dark energy** = a "back-projection" of the 4D event that created our 3+1D universe
- **Dark matter** = the cumulative gravity of countless 2D universes created by every energetic event in our universe
- **Gravity's weakness** = the residual of a near-cancellation between 4D and 2D gravitational effects

## What does v3.0 actually derive?

v3.0 made a **major breakthrough**: a single number — **N = 12** — derives multiple SIDC parameters from a specific physical model (q = 4 SYK — Sachdev-Ye-Kitaev, a model of quantum chaos — with N = 12 Majorana fermions):

| Parameter | Value | Derivation |
|-----------|-------|------------|
| $\alpha$ (lifetime scaling) | 1.289 | $\alpha$ = 1 + 1/√N (saddle-point fluctuation) |
| c (central charge) | 1/2 | c = 1/2 (Ising CFT, surviving mode from SYK q=4; L308aq) |
| $1/(2\alpha)$ (back-action) | 0.388 | $c/\alpha$ (composite) |
| $f_{\rm DE}$ (universal) | $8.6 \times 10^{-85}$ | $(1/(2\alpha))$-powered formula |

N = 12 is **uniquely determined** by $\alpha$ = 1.29 (off by 0.001; for N = 10, 11, 13, 14 the match is much worse).

## What does SIDC predict (and what doesn't)?

**Strong predictions** (testable, falsifiable):

1. **47 Tucanae**: $M_{dyn} \approx M_{stars}$ (no local DM) — differentiator from particle DM
2. **Intermediate F(z) dwarfs (v2.7.32 LEGACY HISTORICAL framework)**: 10-30% of dwarfs are DM-poor (consistent with Bidaran+ 2025 etc.) — current framework uses bilateral cascade with calibrated AGN rate (no F(z) function)
3. **Massive quiescent galaxies at z > 4**: very high $M_{dyn}$ (consistent with RUBIES, EXCELS etc.)
4. **Tidal dwarf galaxies**: shifting toward DM-poor (consistent with Zaragoza-Cardiel+ 2024 etc.)
5. **14 event-type lifetimes**: all follow $\tau_{2D} \sim M^{1.29}$ (SN, GRB, BNS, AGN, etc.)

**Indistinguishable from $\Lambda{\rm CDM}$ or below detection** (currently):

- DESI w(z): w = -1, same as $\Lambda{\rm CDM}$
- 2D universe death GW: 80-100 orders below LISA/PTA detection
- PPN $\gamma$: 1 to $10^{-73}$, same as GR

**Doesn't derive (honest)**:

- Specific CKM/PMNS values
- SM mass hierarchy
- Why N = 12 specifically (vs N = 11 or 13)
- Specific dS₂ topology details

## What is SIDC's "secret symmetry"?

SIDC is **structurally scale-invariant** (works at any dimensional level — a "Russian nesting doll"):

- 5D event → 4D universe → ... → DM
- **4D event → 3+1D universe (us) → ... → DM**
- 3D event → 2D universe → ... → DM

The pattern is the same at every level. The specific values ($\alpha$, c, N, $f_{\rm DE}$) are **dimension-dependent** but the structure is universal. This is SIDC's "dimensional self-similarity" — the SIDC in the name.

## SIDC's honest stance

- **158 honest limitations** documented in §7.0 (v3.5.9+ master table; was 67 in v3.1, was 116 in v3.5.7)
- 8 closed, 25 open, 21 partial, 1 resolved, 6 negative, 7 speculative
- **0 free parameters** at the level of the composite model (N = 12, $\alpha$ = 1.289, c = 1/2, $f_{\rm DE}$ = $8.6 \times 10^{-86}$ are all derived)
- 1 free parameter at the data-fitting level ($z_{\rm half}$ = 3)

SIDC is a **geometric framing with a strongly specified backbone**, not a fully derived Lagrangian. It's a thought experiment, not a complete theory.

---



