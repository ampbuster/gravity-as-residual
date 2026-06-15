# 2D Lagrangian Literature Research — Memo

## Goal
Find existing 2D theoretical frameworks that could constrain the cascade's
2D universe Lagrangian L_2D. The cascade's 2D universe is a 2D brane
(2D worldsheet + boundary), so we need a 2D CFT or 2D gravity action
that can host:
- A 2D metric (the 2D universe's geometry)
- A scalar (the 2D universe's energy/scale)
- A natural "lifetime" mechanism (so it can die and return energy to 3+1D)

## Key literature found

### 1. Liouville quantum gravity (LQG) — most promising

**Status:** mathematically rigorous as of 2021 (Miller-Sheffield).

**Action (worldsheet):**
```
S_L = (1/4π) ∫_Σ d²σ √γ [ (1/2) g^{ab} ∂_a φ ∂_b φ + Q R[γ] φ + μ e^{2bφ} ]
```

Where:
- φ is the Liouville field (the 2D universe's "scale")
- γ is the 2D worldsheet metric
- R[γ] is the 2D Ricci scalar
- b is the Liouville parameter (related to central charge c = 1 + 6Q², Q = 1/b + b)
- μ is the worldsheet "cosmological constant" (sets 2D universe lifetime)
- e^{2bφ} is the Liouville potential (provides bounded φ)

**Why this is good for the cascade:**
- **φ is a 2D scale field** — exactly what the cascade needs (the 2D universe's "scale")
- **μ sets a lifetime** — μ e^{2bφ} growth gives a natural destruction timescale
- **2D CFT with known spectrum** — primary operators V_α = e^{2αφ}
- **Central charge c determines correlation functions** — the cascade's 2D universe CFT correlators are calculable
- **Holographic dual to 3D quantum gravity** — AdS_3/Liouville correspondence gives 4D bulk view
- **Liouville vertex operators** are "punctures" — the 2D universe can be "created" at a point

**Cascade interpretation:**
- 2D universe's lifetime τ_2D ~ 1/√μ (set by Liouville potential)
- 2D universe's "scale" φ matches the 2D metric's overall size
- 2D universe's "energy" = ∫ √γ (μ e^{2bφ} + ...) d²σ — at destruction, this returns to 3+1D
- The 2D universe's "death" = φ → 0 limit where Liouville potential diverges

**Coupling to 3+1D brane:**
- L_coupling = -α ∫_brane d⁴x V_SM(x) · e^{2α_0 φ(x)} |_{2D boundary}
- V_SM is a SM operator (T_μν, J_μ, ...)
- e^{2α_0 φ} is the Liouville vertex operator (a primary of weight (α_0, α_0))
- This is the creation operator for a 2D universe (1-point function of V_α₀)
- The destruction is encoded in the CTP "- branch" of the action

### 2. Randall-Sundrum brane-worlds

**Action (RS-II single-brane):**
```
S = (1/2κ_5²) ∫_bulk d⁵X √-G [ R_5 - 2Λ_5 ]
  + ∫_brane d⁴x √-g [ L_SM + V ]
  + (1/κ_5²) ∫_brane d⁴x √-g K  [Israel junction term]
```

**Why this is the cascade's "parent" framework:**
- 5D bulk + 4D brane is exactly the cascade's geometric setup
- Warped geometry (AdS_5) gives gravity localization → 4D gravity on brane
- The cascade adds: 2D sub-branes (2D universes) that come and go

**Cascade embedding:**
- Cascade's bulk = 5D AdS_5 (or modified by 2D universe population)
- Cascade's brane = 4D SM
- Cascade's 2D universes = 2D boundaries of 5D bulk geodesics (Feynman-Wheeler)
- The 2D universes are NOT just metaphorical — they're real topological features

### 3. Euclidean wormholes / baby universes (Coleman, Giddings-Strominger)

**Action (Giddings-Strominger axion wormhole):**
```
S = (1/16π) ∫_Σ d²σ √γ [ R_2 - 2Λ_eff + f²(∇θ)² ]
```

**Why this is relevant:**
- 2D "baby universe" creation/annihilation is well-studied
- The action has a 2D gravitational part + axion (or other field)
- "Baby universes" are tiny, transient, disconnected geometries
- They form via Euclidean instantons and dissipate via Lorentzian evolution

**Cascade interpretation:**
- 2D universe creation = Euclidean instanton nucleation (probability e^{-S_E})
- 2D universe destruction = Lorentzian decay (rate ~ 1/τ_2D)
- Energy at death = total action content (returns to 3+1D as DM)
- The cascade's 5/27/68 split might be derivable from this instanton calculus

### 4. Karch-Randall 2D branes in AdS_3

**Setup:** A 2D boundary of an AdS_3 wedge, with boundary gravitons.

**Action:** Same as 2D Liouville, but the "Liouville field" φ is interpreted as
the 2D boundary's location in the AdS_3 bulk.

**Why this is good for the cascade:**
- 2D branes are HOLED IN AdS_3 bulk → 2D universes are "defects" in the bulk
- Boundary gravitons = localized gravity modes on the 2D universe
- The 2D universe's "energy" is the boundary graviton Casimir energy
- The 2D universe's "lifetime" is the geodesic distance to the bulk boundary

**Cascade interpretation:**
- 2D universes are bulk defects, not separate objects
- They carry boundary graviton energy (the cascade's DM)
- They die when the AdS_3 wedge closes (geodesic reaches the bulk horizon)

### 5. 2D string worldsheet action (Polyakov)

**Action (matter + gravity):**
```
S_P = (1/4π α') ∫ d²σ √γ [ γ^{ab} ∂_a X^μ ∂_b X_μ + T (det h_{ab}) ]
```

**Why this is less relevant:**
- The 2D universe is NOT a string (it's a 2D extended object with a boundary)
- Polyakov's action is for 1D strings, not 2D surfaces
- Liouville is a better fit because 2D universe is a 2D surface

## Recommended cascade Lagrangian

Combining the above, the cascade's 2D universe Lagrangian should be:

```
S_2D = (1/4π) ∫_Σ d²σ √γ [ (1/2) (∇φ)² + Q R[γ] φ + μ e^{2bφ} ]
        (Liouville 2D gravity, with φ = 2D universe's scale field)
```

And the coupling to the 3+1D brane (creation operator):

```
S_coupling = -α ∫_brane d⁴x [ T_SM(x) · e^{2α_0 φ(x)} ]
              (vertex operator insertion, V_α₀ = e^{2α₀φ} Liouville primary)
```

And the destruction (energy return):

```
S_destruction = +α ∫_brane d⁴x [ T_DM(x) · δ(t - τ_2D) ]
                 (instantaneous return of 2D universe's energy to 3+1D as DM)
```

With CTP formulation (Schwinger-Keldysh) to handle the teleological structure:

```
S_CTP[φ_+, φ_-] = S_2D[φ_+] - S_2D[φ_-] + S_coupling[φ_+] - S_destruction[φ_-]
```

## Specific predictions this Lagrangian makes

1. **τ_2D ~ 1/√μ** (Liouville timescale) — relates the 2D universe's lifetime
   to the Liouville potential strength μ. Currently we use τ_2D = 0.7 Gyr
   from physical analogy. With Liouville, this becomes a calculable quantity.

2. **f_active = (1/π) ∫_0^{τ_2D} dt / T_universe** — but with Liouville,
   the active fraction is weighted by e^{2bφ(t)}, giving a different
   f_active ~ 0.05 than the current 0.051.

3. **The 5/27/68 split** — with Liouville, the action evaluates to specific
   integrals over the Liouville potential. The 5/27/68 might emerge from
   e^{2bφ} asymptotics.

4. **The RAR a_0 = 1.2e-10** — with Liouville, the energy deposit rate
   ∂E/∂t at the 2D brane's boundary gives a natural acceleration scale.

5. **The f_back ~ 10^-85** — with Liouville, f_back is the 2-point function
   of V_α₀ on the Liouville sphere, which is calculable.

## What still needs to be done

1. **Calculate 2D universe's lifetime τ_2D from Liouville potential μ.**
   Currently: τ_2D ~ 0.7 Gyr (analogy). Liouville: τ_2D ~ 1/√μ.
   Question: what is μ in the cascade's framework?

2. **Calculate the 2D universe's energy at death.**
   E_2D = ∫_Σ d²σ √γ [μ e^{2bφ} + ...] — depends on b, μ, and 2D geometry.

3. **Calculate the 2-point function ⟨V_α₀ V_α₀⟩.**
   This is a known Liouville result: depends on the central charge c = 1 + 6Q².
   For c = 1 (matter-free), the result is specific.

4. **Calculate the 3-point function ⟨V_α₁ V_α₂ V_α₃⟩.**
   This is the DOZZ formula (Dorn-Otto-Zamolodchikov-Zamolodchikov).
   Determines the 2D universe creation rate.

5. **Map the cascade's f_active to a Liouville correlator.**
   f_active = (1/T_universe) ∫ dt × [Liouville field amplitude at time t]
            = some function of b, μ, and the 2D universe's birth time

6. **Derive the cascade-MOND g_+ from Liouville.**
   g_+ = (1/c × H_0) × [2D universe energy deposit rate] × [geometrical factor]
   With Liouville, the energy deposit rate is calculable.

7. **Derive the cascade's H_0,4D = sqrt(H_CMB × H_local) from Liouville.**
   This is a remarkable property. With Liouville, the 4D event's intrinsic
   H_0 is the geometric mean of the 2D universe creation/annihilation rates.

8. **Derive the 5/27/68 from the Liouville + bulk geometry.**
   The 5/27/68 is the cascade's biggest unresolved derivation.

## Limitations of this approach

- The Liouville framework assumes a 2D CFT. The cascade's 2D universe
  is a 2D CFT only if its energy is in the 2D gravitational sector.
  This is a POSTULATE of the cascade, not derived.
- The Liouville parameter b and Q = 1/b + b are free parameters.
  They determine the central charge c = 1 + 6Q² and all correlators.
- The Liouville potential μ is also a free parameter (it sets τ_2D).
- These free parameters correspond to the cascade's existing free
  parameters (f_active ~ 0.05, g_+ ~ 1.2e-10, etc.).

## Conclusion

The Liouville 2D quantum gravity framework is the BEST match for the
cascade's 2D universe Lagrangian. It is:
- Mathematically rigorous (Miller-Sheffield 2021)
- Has well-known correlation functions (DOZZ)
- Naturally provides a 2D universe "lifetime" via the Liouville potential
- Naturally couples to 3+1D brane via vertex operator insertions
- Connects to AdS_3/CFT for the bulk view (Karch-Randall)

The cascade's action can be made more concrete by adopting Liouville
for the 2D universe sector. This is a MAJOR step forward for the
cascade's theoretical foundations, but it does NOT change the
cascade's empirical status (still consistent with data, still
requires free parameters b and μ).

The next step is to:
1. Calculate f_active from Liouville 2-point function
2. Calculate τ_2D from Liouville potential
3. Calculate g_+ from Liouville energy deposit rate
4. Compare to current empirical values

If these calculations reproduce the cascade's empirical f_active,
τ_2D, g_+ (within factors of 2-3), that's strong evidence for the
Liouville framework as the cascade's 2D universe sector.

## References for further reading

- Erbin, "Notes on 2d quantum gravity and Liouville theory" (2020)
- Miller-Sheffield, "Liouville quantum gravity and the Brownian map" (2021)
- Zamolodchikov-Zamolodchikov, "Liouville field theory on a pseudosphere" (2001)
- Karch-Randall, "Locally localized gravity" (JHEP 2000)
- Randall-Sundrum, "An alternative to compactification" (PRL 1999)
- Coleman, "Black holes as red herrings" (Nucl Phys B 1988) — baby universes
- Giddings-Strominger, "Axion-induced topology change" (PLB 1988) — wormholes
- Polyakov, "Quantum geometry of bosonic strings" (PLB 1981) — 2D strings
- Schwinger, "Brownian motion of a quantum oscillator" (J Math Phys 1961)
- Keldysh, "Diagram technique for nonequilibrium processes" (JETP 1964)
