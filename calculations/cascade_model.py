#!/usr/bin/env python3
"""
Object-oriented implementation of the dimensional-cascade model from
"Gravity as Residual: A Thought Experiment on Dimensional Inversion,
Annihilation, and the Origin of the Dark Sector"

A single Universe class represents a universe at *any* level of the
cascade. The 4D event that projects into our 3+1D universe is a
Universe object with level=0 (the top). Our 3+1D universe is a child
Universe with level=1. A 2D universe created by an LHC collision is a
child with level=2, etc.

Every Universe is itself a parent — it can have its own child
universes created by its energetic events, and it can end in a
Big Crunch, heat death, etc., and return its energy to its parent
as that parent's dark-matter contribution.

Run with: python3 cascade_model.py

Author: Mavis (M3, MiniMax AI assistant, developed in conversation with the paper's author)
Date: 2026-06
License: MIT
"""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum


# ============================================================
# Physical constants (SI units, except where noted)
# ============================================================
class Constants:
    """Standard physical constants in SI."""
    c = 2.998e8                    # m/s
    h = 6.626e-34                  # J·s
    hbar = h / (2 * math.pi)
    G = 6.674e-11                  # m^3 / (kg·s^2)
    k_B = 1.381e-23                # J/K
    eV_to_J = 1.602e-19
    erg_to_J = 1e-7
    M_sun = 1.989e30               # kg
    M_earth = 5.972e24             # kg
    m_p = 1.673e-27                # proton mass, kg
    m_e = 9.109e-31                # electron mass, kg
    year_s = 365.25 * 24 * 3600    # seconds per year
    Gyr_s = 1e9 * year_s

    # Derived
    @classmethod
    def M_Pl(cls) -> float:
        """Reduced Planck mass (kg)."""
        return math.sqrt(cls.hbar * cls.c / (8 * math.pi * cls.G / 3))  # in natural units -> kg

    @classmethod
    def M_Pl_kg(cls) -> float:
        """Reduced Planck mass in kg."""
        return math.sqrt(cls.hbar * cls.c / (8 * math.pi ** 5 * cls.G / 3))  # (hbar*c/G)^0.5 in kg
        # Note: above is approximate; full form involves 8*pi*G


# ============================================================
# Cascade parameters (the 4 free parameters of §2.6)
# ============================================================
@dataclass
class CascadeParams:
    """
    The four free parameters of the dimensional-cascade model
    (per §2.6 of the paper):
      - epsilon: bulk-brane cancellation fraction (hierarchy)
      - f_back: staying fraction (DE)
      - f_deliver: 4D event's energy delivery efficiency to 3+1D
      - cumulative_back_projection: 2D universe's back-projection
        efficiency to 3+1D (DM)
    """
    epsilon: float = 5.9e-39        # ~1/10^38
    f_back: float = 5.2e-85         # staying fraction
    f_deliver: float = 1.0          # 4D event's energy delivery (default: full)
    cumulative_back_projection: float = 1e-3  # 2D->3+1D back-projection (placeholder)


# ============================================================
# Universe ending types
# ============================================================
class Ending(Enum):
    """The five possible universe endings (per §2.8 of the paper)."""
    FIXED_TIME_BOUNDARY = "fixed-time boundary"
    CYCLIC = "cyclic"
    DIMINISHING_CYCLIC = "diminishing cyclic"
    BIG_CRUNCH = "big crunch (death-flash)"
    BIG_RIP = "big rip"
    BIG_FREEZE = "big freeze / heat death"


# ============================================================
# Rules — the cascade extends standard physics with these
# ============================================================
class InversionRule:
    """
    The downward perceptual inversion principle (per §2.4 of the paper).

    *Downward* dimensional projection (parent -> child) is *perceived*
    by the child as having the *opposite sign* of gravity. The
    *underlying* gravity in the parent remains attractive (standard GR);
    the inversion is a *perceptual* effect of the bulk-brane coupling.

    *Upward* back-projection (child -> parent) does *not* invert the
    perception; the parent perceives the child's net attractive gravity
    as attractive.

    This is a *postulate* of the model, *motivated* by the standard GR
    mechanism for negative effective gravitating density (rho + 3P < 0).
    """

    @staticmethod
    def project_downward(parent_gravity: float) -> float:
        """
        Project a parent's gravity *down* to a child universe.
        Returns the antigravity (inverted) contribution.
        """
        return -parent_gravity  # inversion

    @staticmethod
    def project_upward(child_attractive_residue: float) -> float:
        """
        Project a child's attractive gravity residue *up* to the parent.
        Returns the back-projected (still attractive) contribution.
        """
        return child_attractive_residue  # no inversion


class BulkBraneCoupling:
    """
    The bulk-brane coupling (per §2.4, §2.6 of the paper).

    The bulk-brane interaction produces a *near-cancellation* between
    the brane's native attractive gravity and the projected (inverted)
    bulk gravity, leaving a small net attractive residue.

    G_brane_eff = epsilon * G_brane_native

    where epsilon << 1 is the cancellation fraction (one of the
    cascade's free parameters).
    """

    def __init__(self, params: CascadeParams):
        self.params = params

    def effective_gravity(self, G_native: float) -> float:
        """Compute the effective gravity after bulk-brane cancellation."""
        return self.params.epsilon * G_native

    def un_cancelled_antigravity(self, G_parent: float) -> float:
        """
        The un-cancelled antigravity (the dark energy contribution).
        Per §2.6, this is of order epsilon * G_parent.
        """
        return self.params.epsilon * G_parent


class EnergyConservationRule:
    """
    Standard energy conservation (per §2.6 of the paper).

    The model does *not* propose a new conservation law. Energy is
    conserved in the usual sense. The 4D event's energy is *delivered*
    to 3+1D with efficiency f_deliver (default: 1, full delivery).
    """

    def __init__(self, params: CascadeParams):
        self.params = params

    def delivered_energy(self, original_energy: float) -> float:
        """Energy delivered from parent to child, accounting for f_deliver."""
        return self.params.f_deliver * original_energy


class SymmetriesAndConservationLaws:
    """
    The model assumes standard symmetries and conservation laws
    (per §2.6 of the paper):
      - Energy conservation
      - Momentum and angular momentum conservation
      - CPT symmetry
      - Lorentz invariance
    """

    @staticmethod
    def verify_energy_conserved(
        parent_energy: float,
        delivered_energy: float,
        child_energies: list,
    ) -> bool:
        """
        Check energy conservation: parent's delivered energy equals
        the sum of children's energies (within numerical precision).
        """
        return math.isclose(delivered_energy, sum(child_energies), rel_tol=1e-9)


# ============================================================
# Universe — the main class
# ============================================================
class Universe:
    """
    Represents a universe at *any* level of the dimensional cascade.

    The 4D event that creates our 3+1D universe is a Universe with
    level=0 (the top of the cascade). Our 3+1D universe is a child
    with level=1. A 2D universe created by an LHC collision is a
    grandchild with level=2. Etc.

    Every Universe has:
      - a parent (None if level=0)
      - children (created by its own energetic events)
      - a lifetime in its parent's frame
      - a "Standard Model" at its own level (matter, gravity, dark
        energy, ending)

    The Universe class extends the standard laws (GR, SM) with
    cascade-specific rules: bulk-brane cancellation, downward
    perceptual inversion, active + cumulative return of dark matter.
    """

    def __init__(
        self,
        level: int,
        spatial_extent: float,
        energy: float,
        parent: Optional["Universe"] = None,
        params: Optional[CascadeParams] = None,
        ending: Ending = Ending.FIXED_TIME_BOUNDARY,
        name: str = "",
    ):
        """
        Parameters
        ----------
        level : int
            0 = top (the 4D event), 1 = our 3+1D universe, 2 = 2D universe, etc.
        spatial_extent : float
            Spatial extent in *this* universe's frame, in meters.
            For level=0 (4D event), this is the 4D spatial extent that
            becomes our 3+1D universe's lifetime.
        energy : float
            Total energy of this universe in joules.
        parent : Universe, optional
            The parent universe (None if level=0).
        params : CascadeParams, optional
            Cascade parameters (default = standard).
        ending : Ending
            The universe's ending type.
        name : str
            Optional name for printing.
        """
        self.level = level
        self.spatial_extent = spatial_extent
        self.energy = energy
        self.parent = parent
        self.params = params or CascadeParams()
        self.ending = ending
        self.name = name or f"Universe(L{level})"

        # Children (created by this universe's energetic events)
        self.children: List[Universe] = []

        # Track the universe's *lifetime* in its own frame
        self.lifetime_own_frame = spatial_extent / Constants.c

        # Track the universe's *lifetime* as seen from its parent
        # (per the dimensional time-dilation rule tau = l/c in the
        # parent's frame, where l is the creating event's spatial
        # extent in the parent).
        # NOTE: the child's `spatial_extent` is the *event's* spatial
        # extent in the parent, so the lifetime in the parent's frame
        # is `self.spatial_extent / c` (the same as lifetime_own_frame
        # for a child created by a point-like event in the parent).
        if parent is not None:
            self.lifetime_parent_frame = self.spatial_extent / Constants.c
        else:
            # Top-level universe's "parent" is the 4D bulk; its lifetime
            # in the bulk is just its full 4D duration
            self.lifetime_parent_frame = self.lifetime_own_frame

        # Register as a child of parent
        if parent is not None:
            parent.children.append(self)

    # --------------------------------------------------------
    # Cascade physics: how this universe's gravity relates to its parent's
    # --------------------------------------------------------
    def gravity_coupling_own(self) -> float:
        """
        This universe's *own* (native) gravitational coupling G_own,
        in SI units. For level=0, this is the 4D gravitational coupling
        G_4. For level=1, this is the 3+1D G (Newton's G).

        Convention: level=0 -> G_4 = G_newton (in 4D the natural
        Newton constant is rescaled by extra-dimensional volume, but
        we use G_newton for simplicity).
        """
        return Constants.G

    def gravity_coupling_effective(self) -> float:
        """
        This universe's *effective* (observed) gravitational coupling
        G_eff, after the bulk-brane cancellation.

        G_eff = epsilon * G_own
        """
        return self.params.epsilon * self.gravity_coupling_own()

    def antigravity_from_parent(self) -> float:
        """
        The antigravity contribution from the parent universe's gravity,
        projected into this universe.

        For level=0, this is 0 (no parent).
        For level>0, the parent's gravity is *inverted* (per the downward
        perceptual inversion principle) when projected into the child,
        giving an antigravity contribution. The *un-cancelled* fraction
        of this antigravity is the dark energy in this universe.

        Returns the magnitude of the projected antigravity (in G units).
        """
        if self.parent is None:
            return 0.0
        # The parent's gravity, projected into the child, is inverted.
        # The un-cancelled fraction is ~ epsilon * G_parent (per §2.4).
        return self.params.epsilon * self.parent.gravity_coupling_own()

    def antigravity_dark_energy_density(self) -> float:
        """
        The dark energy density in this universe from the un-cancelled
        antigravity of the parent (per §2.4, §2.6).

        For level=0: 0 (no parent).
        For level=1 (our 3+1D universe): the dark energy is the
        un-cancelled fraction of the 4D event's antigravity, modulated
        by f_back.
        """
        if self.parent is None:
            return 0.0
        # Convert from gravitational coupling to vacuum energy density
        # (per §2.6): rho_DE ~ epsilon * M_Pl^4 (in natural units)
        # In SI: rho_DE [J/m^3] = epsilon * f_back * (M_Pl c^2 / l_Pl)^4
        # where l_Pl is the Planck length.
        # For our universe (level=1), this should be ~ 6e-10 J/m^3.
        M_Pl = math.sqrt(Constants.hbar * Constants.c / Constants.G)  # kg
        l_Pl = math.sqrt(Constants.hbar * Constants.G / Constants.c ** 3)  # m
        # Energy density at Planck scale
        rho_Pl_4 = (M_Pl * Constants.c ** 2 / l_Pl ** 3) ** 1  # J/m^3 at Planck scale
        # Simplified: the model has the post-hoc factor f_back bridging the 10^85 gap
        return self.params.epsilon * self.params.f_back * rho_Pl_4

    def attractive_gravity_to_parent(self) -> float:
        """
        The *attractive* gravity back-projection from this universe to
        its parent (per §2.4 — the upward back-projection does NOT
        invert).

        This is the small net attractive residue of this universe's
        bulk-brane cancellation, projected *up* to the parent without
        sign change. This is the dark matter contribution to the parent.

        Returns the magnitude in G units.
        """
        return self.gravity_coupling_effective()

    # --------------------------------------------------------
    # Observable dark-sector quantities
    # --------------------------------------------------------
    def dark_energy_density_observed(self) -> float:
        """
        The dark energy density *observed* in this universe, in J/m^3.

        For our 3+1D universe, this should be ~ 6e-10 J/m^3
        (Planck 2018: rho_DE ~ 6.9e-27 kg/m^3 * c^2 ~ 6.2e-10 J/m^3).

        Per §2.6, the cascade predicts rho_DE ~ epsilon * M_Pl^4, which
        is 10^85 *larger* than observed. The f_back staying fraction
        bridges this gap: rho_DE_observed = epsilon * f_back * rho_Pl_4.

        For our universe (level=1), this gives:
          rho_DE_observed = 5.9e-39 * 5.2e-85 * rho_Pl_4
                         ~ 6e-10 J/m^3
        """
        M_Pl = math.sqrt(Constants.hbar * Constants.c / Constants.G)  # kg
        l_Pl = math.sqrt(Constants.hbar * Constants.G / Constants.c ** 3)  # m
        # Planck energy density in SI (J/m^3)
        # rho_Pl = M_Pl * c^2 / l_Pl^3
        rho_Pl = M_Pl * Constants.c ** 2 / l_Pl ** 3
        return self.params.epsilon * self.params.f_back * rho_Pl

    def active_dark_matter_density(self) -> float:
        """
        The *active* contribution to dark matter density in this
        universe, in J/m^3.

        This is the back-projection of *currently-alive* child
        universes (per §2.5, §4.2). The active population is
        (current event rate) × (average child lifetime in this frame).

        For our 3+1D universe, the active contribution is dominated by
        long-lived AGN-scale 2D universes (per §2.6 calc).

        NOTE: this is a *naive* estimate that doesn't include the
        growth factor (2D universe's own dark energy dominating its
        mass budget). A full implementation would include that.
        """
        # The active population = (sum over child event rates) × (avg lifetime)
        # For each child, its back-projection contributes
        # (cumulative_back_projection * child.energy) / (this volume)
        # to this universe's dark matter density.
        #
        # We use this universe's spatial extent as a proxy for volume:
        if self.spatial_extent <= 0:
            return 0.0
        volume = self.spatial_extent ** 3
        total_active_E = sum(
            self.params.cumulative_back_projection * c.energy
            for c in self.children
        )
        return total_active_E / volume

    def cumulative_return_dark_matter_density(self) -> float:
        """
        The *cumulative return* contribution to dark matter density
        in this universe, in J/m^3.

        This is the *integrated* return from all past child universe
        *endings* (Big Crunch death-flashes + heat death diffuse
        returns) over the universe's history.

        For our 3+1D universe, this is approximately uniform
        spatially (since the integrated past activity is roughly
        similar across the universe).
        """
        if self.spatial_extent <= 0:
            return 0.0
        volume = self.spatial_extent ** 3
        total_cumulative_E = sum(
            self._cumulative_return(child)
            for child in self.children
        )
        return total_cumulative_E / volume

    def _cumulative_return(self, child: "Universe") -> float:
        """
        The total cumulative return from a child universe and all its
        descendants, assuming the child has completed its lifecycle.
        """
        if child.ending in (Ending.BIG_CRUNCH, Ending.DIMINISHING_CYCLIC):
            # Death-flash: all energy returns at once
            return child.end()
        elif child.ending == Ending.BIG_FREEZE:
            # Heat death: energy returns slowly over a long time
            return child.end()
        else:
            return child.end()

    def total_dark_matter_density(self) -> float:
        """
        The *total* dark matter density in this universe (active +
        cumulative return), in J/m^3.
        """
        return self.active_dark_matter_density() + self.cumulative_return_dark_matter_density()

    # --------------------------------------------------------
    # Energetic event: create a child universe
    # --------------------------------------------------------
    def create_child(
        self,
        event_energy: float,
        event_extent: float,
        ending: Ending = Ending.FIXED_TIME_BOUNDARY,
        name: str = "",
    ) -> "Universe":
        """
        A new energetic event in *this* universe creates a child
        universe at the next level down.

        Parameters
        ----------
        event_energy : float
            Energy of the creating event in joules.
        event_extent : float
            Spatial extent of the creating event in meters.
        ending : Ending
            The child universe's ending.
        name : str
            Optional name.

        Returns
        -------
        Universe
            The new child universe.
        """
        child = Universe(
            level=self.level + 1,
            spatial_extent=event_extent,
            energy=event_energy,
            parent=self,
            params=self.params,
            ending=ending,
            name=name,
        )
        return child

    # --------------------------------------------------------
    # Ending: return energy to parent
    # --------------------------------------------------------
    def end(self) -> float:
        """
        This universe ends. Its energy is returned to its parent as
        a dark-matter contribution. The form depends on the ending:
          - BIG_CRUNCH: brief, intense, localized death-flash
          - BIG_FREEZE: slow, diffuse, distributed return
          - OTHER: combination

        Returns the energy returned to the parent.
        """
        if self.parent is None:
            # Top-level universe: energy goes... somewhere. The model
            # doesn't specify. Return 0 (or could return to 5D+, but
            # we stop at level 0 for now).
            return 0.0

        # The 2D universe's *attractive* gravity residue back-projects
        # to the parent. Per §2.6 universal-split, the attractive
        # fraction is ~32% of the 2D universe's *total* mass-energy
        # (5% ordinary + 27% dark matter from 1D universe
        # back-projection in 2D). But the 2D universe's total
        # mass-energy is dominated by its own dark energy (68%),
        # not the original event energy.
        #
        # For simplicity here, we return the original event energy
        # (the "ordinary matter" 5% contribution) as the attractive
        # back-projection. A full implementation would include the
        # growth factor and the cumulative 1D universe contributions.
        attractive_back_projection = (
            self.params.cumulative_back_projection
            * self.energy
            * (0.05 + 0.27)  # ordinary + dark matter fraction in 2D
        )
        return attractive_back_projection

    # --------------------------------------------------------
    # Snapshot
    # --------------------------------------------------------
    def describe(self, indent: int = 0) -> str:
        """Pretty-print this universe and its descendants."""
        pad = "  " * indent
        s = (
            f"{pad}{self.name}\n"
            f"{pad}  level:        {self.level}\n"
            f"{pad}  spatial extent: {self.spatial_extent:.3e} m\n"
            f"{pad}  energy:        {self.energy:.3e} J\n"
            f"{pad}  lifetime (own frame):     {self.lifetime_own_frame:.3e} s\n"
            f"{pad}  lifetime (parent frame):  {self.lifetime_parent_frame:.3e} s\n"
            f"{pad}  G_eff:         {self.gravity_coupling_effective():.3e} (m^3/kg/s^2)\n"
            f"{pad}  G_eff/G_newton: {self.gravity_coupling_effective() / Constants.G:.3e}\n"
            f"{pad}  ending:        {self.ending.value}\n"
            f"{pad}  children:      {len(self.children)}\n"
        )
        if self.parent is not None:
            s += (
                f"{pad}  parent:        {self.parent.name} (L{self.parent.level})\n"
                f"{pad}  antigravity from parent: {self.antigravity_from_parent():.3e} (m^3/kg/s^2)\n"
                f"{pad}  attractive back-projection to parent: {self.attractive_gravity_to_parent():.3e} (m^3/kg/s^2)\n"
            )
        for child in self.children:
            s += "\n" + child.describe(indent + 1)
        return s

    # --------------------------------------------------------
    # Magic: lifecycle
    # --------------------------------------------------------
    def __repr__(self):
        return f"Universe(level={self.level}, energy={self.energy:.3e} J, ending={self.ending.value})"


# ============================================================
# Concrete universe factories — known physics
# ============================================================
def our_3plus1d_universe(
    params: Optional[CascadeParams] = None,
) -> Universe:
    """
    Our 3+1D universe as a Universe object at level=1.

    Parent: 4D event (level=0, the top of the cascade).
    Spatial extent: ~ 8.8e26 m (size of observable universe).
    Energy: ~ 4e69 J (total mass-energy of observable universe, dominated by DE).
    """
    if params is None:
        params = CascadeParams()

    # 4D event (parent)
    # 4D spatial extent / c = 4D duration
    # Our universe's lifetime ~ 13.8 Gyr, so 4D duration ~ 13.8 Gyr * c
    # (using the simplest interpretation: 4D full duration maps to 3+1D lifetime)
    four_d_duration_s = 13.8e9 * Constants.year_s  # seconds
    four_d_extent_m = four_d_duration_s * Constants.c  # m

    # 4D event's energy: in the simplest case, equal to our universe's mass-energy
    our_energy = 4e69  # J (rough total mass-energy of observable universe)

    four_d_event = Universe(
        level=0,
        spatial_extent=four_d_extent_m,
        energy=our_energy,
        parent=None,
        params=params,
        ending=Ending.FIXED_TIME_BOUNDARY,
        name="4D event (parent of our universe)",
    )

    # Our 3+1D universe (child of 4D event)
    observable_universe_extent_m = 8.8e26  # m
    our_universe = Universe(
        level=1,
        spatial_extent=observable_universe_extent_m,
        energy=our_energy,
        parent=four_d_event,
        params=params,
        ending=Ending.FIXED_TIME_BOUNDARY,
        name="Our 3+1D universe",
    )
    return our_universe


def lhc_collision_universe(
    parent_universe: Universe,
    energy_GeV: float = 13000,  # LHC run-3 energy
) -> Universe:
    """
    A 2D universe created by an LHC collision (a typical event in our 3+1D).
    """
    energy_J = energy_GeV * 1e9 * Constants.eV_to_J
    # LHC collision spatial extent ~ inverse of collision energy
    # ~ 10^-15 m for TeV-scale
    extent_m = 1e-15
    return parent_universe.create_child(
        event_energy=energy_J,
        event_extent=extent_m,
        ending=Ending.BIG_FREEZE,  # small 2D universe: heat death
        name=f"LHC 2D universe ({energy_GeV:.0f} GeV)",
    )


def supernova_universe(
    parent_universe: Universe,
    energy_eV: float = 1e60,  # visible light energy of SN
) -> Universe:
    """
    A 2D universe created by a supernova.
    """
    energy_J = energy_eV * Constants.eV_to_J
    extent_m = 1e10  # photosphere scale
    return parent_universe.create_child(
        event_energy=energy_J,
        event_extent=extent_m,
        ending=Ending.BIG_CRUNCH,  # large 2D universe: Big Crunch (or heat death)
        name="SN 2D universe",
    )


def sgr_a_universe(
    parent_universe: Universe,
) -> Universe:
    """
    A 2D universe created by a Sagittarius A*-scale AGN outburst.
    """
    energy_J = 1e62 * Constants.eV_to_J
    extent_m = 1.2e10  # Sgr A* Schwarzschild radius
    return parent_universe.create_child(
        event_energy=energy_J,
        event_extent=extent_m,
        ending=Ending.BIG_CRUNCH,
        name="Sgr A* 2D universe",
    )


# ============================================================
# Cascade — top-level orchestrator
# ============================================================
class Cascade:
    """
    Top-level orchestrator for the dimensional cascade.

    A Cascade has:
      - parameters (the 4 free parameters of the model)
      - rules (the cascade-specific extensions to standard physics)
      - a root universe (the 4D event that creates our 3+1D universe)

    The Cascade class is the entry point for running simulations of
    the cascade. It manages the universe tree and provides methods
    for computing observable quantities.
    """

    def __init__(
        self,
        params: Optional[CascadeParams] = None,
        root: Optional[Universe] = None,
    ):
        self.params = params or CascadeParams()
        self.inversion_rule = InversionRule()
        self.bulk_brane = BulkBraneCoupling(self.params)
        self.energy_conservation = EnergyConservationRule(self.params)
        self.symmetries = SymmetriesAndConservationLaws()
        # If no root provided, build the standard cascade:
        # 4D event (level 0) -> our 3+1D universe (level 1)
        if root is None:
            self.root = self._build_standard_cascade()
        else:
            self.root = root

    def _build_standard_cascade(self) -> Universe:
        """Build the standard cascade: 4D event -> 3+1D universe."""
        # Build the 4D event first
        four_d_duration_s = 13.8e9 * Constants.year_s
        four_d_extent_m = four_d_duration_s * Constants.c
        four_d_event = Universe(
            level=0,
            spatial_extent=four_d_extent_m,
            energy=4e69,
            parent=None,
            params=self.params,
            ending=Ending.FIXED_TIME_BOUNDARY,
            name="4D event (parent of our universe)",
        )
        # Then our 3+1D universe as a child
        Universe(
            level=1,
            spatial_extent=8.8e26,
            energy=4e69,
            parent=four_d_event,
            params=self.params,
            ending=Ending.FIXED_TIME_BOUNDARY,
            name="Our 3+1D universe",
        )
        # Return the 4D event (the top of the cascade)
        return four_d_event

    def our_universe(self) -> Universe:
        """Get our 3+1D universe (the first child of the root)."""
        return self.root.children[0]

    def total_descendants(self) -> int:
        """Count all universes in the cascade tree."""
        count = 0
        stack = [self.root]
        while stack:
            u = stack.pop()
            count += 1
            stack.extend(u.children)
        return count

    def describe(self) -> str:
        s = "Cascade:\n"
        s += f"  Total universes in tree: {self.total_descendants()}\n"
        s += f"  Parameters: epsilon={self.params.epsilon:.2e}, f_back={self.params.f_back:.2e}, f_deliver={self.params.f_deliver:.2f}\n"
        s += "\n"
        s += self.root.describe()
        return s


# ============================================================
# Demonstration
# ============================================================
def demo():
    """Run a small demo of the cascade."""
    print("=" * 70)
    print("DIMENSIONAL CASCADE — DEMO")
    print("=" * 70)

    # Build a cascade
    cascade = Cascade()
    us = cascade.our_universe()
    print("\n--- Our 3+1D universe (via Cascade class) ---")
    print(us.describe())

    # Add a few child universes from energetic events
    lhc = lhc_collision_universe(us)
    print("\n--- After an LHC collision ---")
    print(us.describe())

    sn = supernova_universe(us)
    print("\n--- After a supernova ---")
    print(us.describe())

    sgr = sgr_a_universe(us)
    print("\n--- After a Sgr A* outburst ---")
    print(us.describe())

    # End the SN universe
    print("\n--- Ending the SN universe ---")
    returned = sn.end()
    print(f"SN 2D universe ended. Energy returned to parent: {returned:.3e} J")
    print(f"  (As dark matter contribution to 3+1D)")

    # Numerical check: G_eff / G should be ~ 10^-38
    print("\n--- Hierarchy check ---")
    print(f"G_eff / G_newton = {us.gravity_coupling_effective() / Constants.G:.3e}")
    print(f"Expected ~ 10^-38 (hierarchy)")

    # Numerical check: dark energy density
    print("\n--- Dark energy density (in our universe) ---")
    de_density = us.dark_energy_density_observed()
    print(f"rho_DE_observed = {de_density:.3e} J/m^3")
    print(f"Expected ~ 6e-10 J/m^3 (Planck 2018)")

    # Numerical check: dark matter density
    print("\n--- Dark matter density (in our universe) ---")
    dm_active = us.active_dark_matter_density()
    dm_cumulative = us.cumulative_return_dark_matter_density()
    dm_total = us.total_dark_matter_density()
    print(f"rho_DM_active     = {dm_active:.3e} J/m^3")
    print(f"rho_DM_cumulative = {dm_cumulative:.3e} J/m^3")
    print(f"rho_DM_total      = {dm_total:.3e} J/m^3")
    print(f"Expected ~ 3e-10 J/m^3 (Planck 2018; 27% of critical)")
    print(f"NOTE: this is the *naive* calc; real DM needs growth factor")

    # Numerical check: 2D universe lifetimes
    print("\n--- 2D universe lifetimes in our frame ---")
    print(f"LHC 2D universe:  {lhc.lifetime_parent_frame:.3e} s")
    print(f"  Expected ~ 3.3e-24 s")
    print(f"SN 2D universe:   {sn.lifetime_parent_frame:.3e} s")
    print(f"  Expected ~ 33 s (since extent ~ 1e10 m)")
    print(f"Sgr A* 2D universe: {sgr.lifetime_parent_frame:.3e} s")
    print(f"  Expected ~ 40 s (since extent ~ 1.2e10 m)")

    # Demonstrate the cascade: create a 2D universe's child (3D universe)
    print("\n--- Recursive cascade ---")
    # The SN 2D universe's "energetic events" could create 1D universes
    # (but we won't actually do that here, just show the recursion)
    print(f"The SN 2D universe could create its own 1D universe children,")
    print(f"each with shorter lifetime. The cascade is fractal.")

    print("\n" + "=" * 70)
    print("Demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    demo()
