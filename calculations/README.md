# Cascade Model — Python Implementation

This directory contains Python code implementing the dimensional-cascade
model from
**"Gravity as Residual: A Thought Experiment on Dimensional Inversion,
Annihilation, and the Origin of the Dark Sector"**.

## Files

- **`cascade_model.py`** — Object-oriented framework for the cascade.
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
  2D universe's own dark energy / dark matter growth factor)
- A replacement for actual physics derivations

The framework is intended as a *scaffolding* for future work, not a
finished calculation.
