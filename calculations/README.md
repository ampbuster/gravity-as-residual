# Cascade Model — Python Implementation

This directory contains Python code implementing the dimensional-cascade
model from
**"Gravity as Residual: A Thought Experiment on Dimensional Inversion,
Annihilation, and the Origin of the Dark Sector"**.

## Files

- **`cascade_model.py`** — Object-oriented framework for the cascade.
- **`section_2_1_derivations.py`** — Standalone script running the 7
  derivations from first principles (hierarchy, DE, DM, growth factor,
  Hubble tension, 2D lifetime, universal-split). Each derivation
  prints its inputs, math, and outputs. Run with
  `python3 section_2_1_derivations.py`.
- **`parameter_sweep.py`** — Sweep 2D universe parameter space
  (Omega_DE, lifetime, f_eq, h_2D) for G ~ 1e8 robustness. Shows
  that G ~ 1e8 is achieved for a moderate range of parameters
  (lifetime 25-35 Gyr, h_2D 0.8-1.2).
- **`hubble_sfr_correlation.py`** — Falsifiable prediction: H_0
  correlates with local star formation rate. Predicts H_0 in
  starbursts ~ 72 km/s/Mpc vs H_0 in passive ellipticals ~ 68 km/s/Mpc.
- **`hubble_tightened.py`** — Honest analysis of the Hubble tension
  prediction: simple model gives 2.7 km/s/Mpc, half the observed
  5.6. Identifies 4 alternative mechanisms to close the gap.
- **`cmb_imprint.py`** — Order-of-magnitude CMB power spectrum
  imprint from 4D->3+1D projection. Discusses tensor modes, spectral
  index, and specific features.
- **`rar_check.py`** — Radial Acceleration Relation (RAR) check.
  Cascade predicts g+ ~ 1e-10 m/s² (matches observed). Notes that
  the predicted *shape* is 'broken' (uniform halo DM) while the
  empirical RAR is smooth (NFW-like profile).
- **`universal_split_derivation.py`** — Attempts to derive the
  5/27/68 split from projection geometry. Honest result: the split
  is a POSTULATE, not derived. 5% and 68% are coupled via epsilon,
  27% follows from G (now derived in Task 1).
- **`parameter_collapse.py`** — Free parameter reduction. Shows
  the cascade has effectively 1 free parameter (f_back), with
  epsilon (defined by hierarchy), G (derived), and f_deliver
  (set to 1 by parsimony). More parsimonious than ΛCDM.
- **`derivations.md`** — Paper-style document with the math behind
  each quantitative claim.
- **`numerical_verification.py`** — First-principles derivations
  of the paper's main numerical claims.
- **`README.md`** — This file.
  A single `Universe` class represents a universe at *any* level of
  the cascade. The 4D event that creates our 3+1D universe is a
  `Universe` object with `level=0`; our universe is a child with
  `level=1`; a 2D universe created by an LHC collision is a grandchild
  with `level=2`; and so on. Every universe is itself a parent and can
  have its own children.

  Key classes:
  - `Universe` — a universe at any level of the cascade (parent +
    children, gravity couplings, lifetime, ending, etc.)
  - `CascadeParams` — the 4 free parameters of the model (epsilon,
    f_back, f_deliver, cumulative_back_projection)
  - `Cascade` — top-level orchestrator (params, rules, root universe)
  - `StandardModel` (abstract) — the physics at a given level
  - `StandardModel_L0_4D` — abstract 4D SM (unknown)
  - `StandardModel_L1_3plus1D` — the SM we know (real force carriers,
    matter particles, coupling constants)
  - `StandardModel_L2_2D` — abstract 2D SM (unknown)
  - `InversionRule` — the downward perceptual inversion principle
  - `BulkBraneCoupling` — the bulk-brane interaction (G_eff = epsilon * G)
  - `EnergyConservationRule` — standard energy conservation
  - `SymmetriesAndConservationLaws` — standard physics laws assumed
  - `EnergeticEvent` — an event that creates a child universe
    (LHC, supernova, AGN, etc.)
  - `Ending` (enum) — the 5 possible universe endings
  - `Constants` — standard physical constants
  - `GrowthFactorCalculator` — derives the 2D universe's growth factor
    from its own FRW dynamics (matter era, DE era, lifetime)
  - `HierarchyUnificationCalculator` — shows hierarchy, DE, and DM
    all follow from the same cascade formula
  - `HubbleTensionCalculator` — predicts H_0_local > H_0_CMB from
    active vs cumulative DM in local region

  Key methods on Universe:
  - `gravity_coupling_own()` / `_effective()` — native and effective G
  - `antigravity_from_parent()` — dark energy in this universe
  - `attractive_gravity_to_parent()` — dark matter to parent
  - `dark_energy_density_observed()` — DE density in J/m^3
  - `active_dark_matter_density()` — DM from currently-alive children
  - `cumulative_return_dark_matter_density()` — DM from past endings
  - `total_dark_matter_density()` — active + cumulative return
  - `create_child()` — create a child universe
  - `end()` — end this universe and return energy to parent

  Event factories (create known events):
  - `lhc_collision_universe()` — LHC collision in our universe
  - `supernova_universe()` — Type II supernova
  - `sgr_a_universe()` — Sagittarius A* AGN outburst
  - `cosmic_ray_collision_universe()` — GZK cosmic ray collision
  - `binary_merger_universe()` — binary neutron star merger
  - `primordial_bh_formation_universe()` — PBH formation
  - `simulate_galaxy_events()` — realistic galaxy event simulation

- **`numerical_verification.py`** — Re-derives all numerical claims
  in the paper from first principles (hierarchy, energy budget, 2D
  universe lifetimes, etc.).

## Running

```bash
python3 cascade_model.py
```

## Extending

To add a new kind of universe (e.g., a 1D universe from a 2D
energetic event), just call `parent_universe.create_child(...)` with
the appropriate energy and extent. The new universe is automatically
registered as a child of the parent and inherits the cascade
parameters.

To run a complete cascade (4D event → 3+1D → 2D → 1D → ...), build
the cascade recursively:

```python
our_universe = our_3plus1d_universe()
sn = supernova_universe(our_universe)  # 2D universe from SN
child_of_sn = sn.create_child(  # 1D universe from SN's energetic events
    event_energy=sn.energy * 0.1,
    event_extent=sn.spatial_extent * 0.1,
)
# etc.
```

## What this is and isn't

This is an *object-oriented framework* for the cascade model. It
implements the qualitative structure of the model and computes
several quantitative predictions. It is **not**:

- A derivation of the cascade from first principles
- A full quantitative prediction of dark matter density (the model
  has a 10⁵-10¹⁰ gap in the DM calculation that requires the
  2D universe's own dark energy / dark matter growth factor,
  which is captured by the GrowthFactorCalculator)
- A replacement for actual physics derivations

The framework is intended as a *scaffolding* for future work, not a
finished calculation.

## Derivation summary

The framework demonstrates several derivations from the cascade model:

1. **Hierarchy problem** (§2.1): G_eff / G = (m_proton / M_Pl)^2 = 5.9×10⁻³⁹
2. **Dark energy** (§2.4): ρ_DE = ε × f_back × ρ_Pl = 6.21×10⁻¹⁰ J/m³ (Planck 2018)
3. **Dark matter** (§2.6): M_DM = 6.4 × G × M_event × N_events per galaxy
4. **Growth factor** (§2.6): G = 20 × V_growth, where V_growth is the 2D
   universe's volumetric expansion. With Omega_DE_2D ~ 0.999, lifetime
   ~30 Gyr, t_eq_2D ~ 1% of lifetime: G ~ 1e8 (matches observed DM).
5. **Hubble tension** (§2.7): H_0_local > H_0_CMB by ~3-6 km/s/Mpc,
   from active children boosting local antigravity.
6. **2D universe lifetimes** (§2.2): τ_2D = l_event / c in our frame
   (LHC: 3.3e-24 s, SN: 33 s, AGN: 40 s).
