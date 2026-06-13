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

  Key methods:
  - `gravity_coupling_own()` — the universe's native G
  - `gravity_coupling_effective()` — the universe's *effective* G
    (after bulk-brane cancellation)
  - `antigravity_from_parent()` — the antigravity contribution from
    the parent universe (this is the dark energy in this universe)
  - `attractive_gravity_to_parent()` — the attractive gravity
    back-projection to the parent (this is the dark matter
    contribution to the parent)
  - `dark_energy_density_observed()` — the dark energy density in
    this universe, in J/m^3
  - `active_dark_matter_density()` — the *active* contribution to
    dark matter density (from currently-alive children)
  - `cumulative_return_dark_matter_density()` — the *cumulative
    return* contribution (from past child universe endings)
  - `total_dark_matter_density()` — active + cumulative return
  - `create_child()` — create a new child universe from an
    energetic event
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
