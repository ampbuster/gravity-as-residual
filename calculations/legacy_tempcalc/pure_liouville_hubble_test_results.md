# Pure Liouville Hubble Code — Test Results

## What the code does

```python
def continuous_liouville_field(p, z):
    E_crit = 1.44
    effective_temperature = 0.35 * (1.0 + np.log1p(z))
    structural_density_wave = 1.85 * np.sin(np.pi * (z ** 0.45)) if z < 1.0 else -1.78
    f_density = np.exp(-p**2 / effective_temperature) * structural_density_wave
    threshold_activation = 1.0 if (p**2) >= E_crit else 0.05
    return (p**2) * f_density * threshold_activation

def calculate_pure_liouville_hubble(z, h_bulk=70.16):
    net_perturbation, _ = quad(continuous_liouville_field, 0, np.inf, args=(z,))
    if z < 0.02:
        net_perturbation *= (1.0 - np.tanh((z - 0.01) / 0.002)) / 2.0 + 0.5
    return float(h_bulk + net_perturbation)
```

## What the code ACTUALLY produces

I ran the code at the key redshifts:

| z | H_eff (code) | Expected (data) | Match? |
|---|--------------|-----------------|--------|
| 0.0 | 70.16 | 73.04 (SH0ES) | ✗ NO |
| 0.005 | 70.17 | ~70.16 (TRGB) | ✓ yes |
| 0.01 | 70.17 | ~70.16 (TRGB) | ✓ yes |
| 0.02 | 70.17 | transition | ~ |
| 0.05 | 70.17 | ~73 (H0LiCOW) | ✗ NO |
| 0.1 | 70.18 | ~73 (H0LiCOW) | ✗ NO |
| 0.5 | 70.19 | 73.0 (Pantheon+) | ✗ NO |
| 1.0 | 70.08 | transition | ✗ NO |
| 2.0 | 70.01 | 67.4 (Planck) | ✗ NO |
| 1100 | 67.18 | 67.4 (Planck) | ~ close |

**The code does NOT reproduce the cascade's 4-zone H(z) picture.**

## Why the code fails

### 1. At z=0, the integrand is ZERO

At z=0:
- `effective_temperature = 0.35 * (1.0 + log(1+0)) = 0.35 * 1.0 = 0.35`
- `structural_density_wave = 1.85 * sin(pi * 0^0.45) = 1.85 * sin(0) = 0`
- `f_density = exp(-p²/0.35) * 0 = 0`
- The integrand is ZERO everywhere
- `H_eff(0) = 70.16 + 0 = 70.16`

The "boundary correction" `net_perturbation *= 1.5` multiplies a zero, so it stays zero.

The code does NOT give 73.04 at z=0. The "claimed" local boost is not implemented.

### 2. The 73.00 boost at z=0.05-1 is missing

At z=0.5:
- `effective_temperature = 0.35 * (1.0 + log(1.5)) = 0.35 * 1.405 = 0.49`
- `structural_density_wave = 1.85 * sin(pi * 0.5^0.45) = 1.85 * sin(pi * 0.685) = 1.85 * 0.836 = 1.55`
- The integrand is positive but small (~0.04 total)
- `H_eff(0.5) = 70.16 + 0.034 = 70.19`

This is NOT 73.00. The "secular boost" at z=0.05-1 is not implemented.

### 3. The 67.4 drag at z>1 is too weak

At z=1100:
- `effective_temperature = 0.35 * (1.0 + log(1101)) = 0.35 * 7.00 = 2.45`
- `structural_density_wave = -1.78` (since z > 1.0)
- The integrand is negative (because of -1.78)
- Total integral: -2.98
- `H_eff(1100) = 70.16 - 2.98 = 67.18`

This is close to 67.4 but not exact. The CMB drag is partially captured but not perfectly.

## What's actually happening

The code is a **3-parameter fit disguised as a derivation**:
- `E_crit = 1.44` — the threshold (chosen to make the integral work)
- `0.35` — the temperature prefactor (chosen to set the right scale)
- `1.85` — the structural wave amplitude (chosen to get the right magnitude)
- `-1.78` — the CMB drag amplitude (chosen to match Planck)
- `0.45` — the exponent in z^0.45 (chosen to shape the z-dependence)
- `0.05` — the "off" threshold value (chosen to give the baseline)

None of these are derived from any physical principle. They're all hand-tuned to approximately match the data.

## The numerical reality

The code gives:
- H_eff(0) = 70.16 (should be 73.04 — off by 2.88)
- H_eff(0.5) = 70.19 (should be 73.00 — off by 2.81)
- H_eff(1100) = 67.18 (should be 67.4 — off by 0.22)

The CMB drag is approximately right, but the local R_stellar boost and the secular boost are both missing.

## Why the local boost is missing

The "local boost" (R_stellar firing) at z=0 is supposed to add +2.88 to H_eff. But:
- The integral at z=0 is ZERO (because structural_density_wave = sin(0) = 0)
- The "boundary correction" tanh factor is multiplied by a zero, so it does nothing
- There is NO mechanism in the code to add the local R_stellar boost

The local boost would need to be added as a SEPARATE term, like:
```python
if z < 0.01:
    H_eff += 2.88  # Local R_stellar boost
```

But this is not in the code. It's a missing piece.

## Why the secular boost at z=0.05-1 is missing

The "secular boost" at z=0.05-1 is supposed to add +2.84 to H_eff. The code has:
- `structural_density_wave = 1.85 * sin(pi * z^0.45)` for z < 1.0

At z=0.1: sin(pi * 0.1^0.45) = sin(pi * 0.355) = sin(1.115) = 0.898
- So `structural_density_wave = 1.85 * 0.898 = 1.66`

But the integrand has `exp(-p²/T)` which decays fast. For p > 2, the integrand is negligible.

The integral gives ~0.03-0.04, not 2.84. The "secular boost" is off by a factor of ~70.

This is because the structural_density_wave is in the **integrand**, which gets multiplied by exp(-p²/T) (a decaying function) and integrated over p. The integral averages out the wave to a small number.

To get a +2.84 boost, the code would need either:
- A much larger amplitude (1.85 → 130 or so)
- A different functional form
- An additional term that's not integrated

## Why this is still curve fitting

Even though the code looks more sophisticated than the 4-zone spec, it's still curve fitting because:

1. **The 6 parameters are all hand-tuned** (E_crit, 0.35, 1.85, -1.78, 0.45, 0.05)
2. **The functional forms are chosen to approximately match the data** (sin(pi * z^0.45), exp(-p²/T), Heaviside)
3. **The Heaviside threshold is a discontinuity** — the "phase transition" is hardcoded, not derived
4. **The "boundary correction" at z<0.02 is a hand-tuned tanh** — it's not from any equation
5. **The "microscopically locked parameters" claim is false** — they're not from microphysics, they're from data fitting

## What the code COULD do (if parameters were right)

If the parameters WERE derived from first principles, the code would be a real Liouville framework. The structure is:
- Liouville-like field: exp(-p²/T) (Gaussian, not Liouville)
- Threshold barrier: Heaviside at E_crit (a phase transition)
- Cosmic scaling: (1 + log(1+z)) (a cosmic clock)
- Structural modulation: sin(pi * z^0.45) (a structural wave)

If these were all DERIVED (not fitted), the code would be a real derivation. But they're all chosen by hand.

## Honest assessment

The code is **a 6-parameter curve fit dressed up in Liouville language**. It does NOT:
- Derive the 4-zone H(z) structure from first principles
- Use a real Liouville 2D CFT (no DOZZ formula, no 2-point function, no reflection coefficient)
- Implement the cascade's principles (no 2D universe creation, no death energy, no line-of-sight integral)
- Reproduce the claimed H_eff values (off by 2-3 km/s/Mpc at most redshifts)

The code DOES:
- Have a clear structure (integral over momentum space with threshold)
- Use a continuous function (no hardcoded zones)
- Approximately match the CMB drag at z=1100
- Demonstrate that a 6-parameter fit can approximately match the 4-zone data

## Recommendation

**Do NOT add this code to the paper as "first-principles Liouville framework."** It is curve fitting, not derivation. The honest framing would be:

> "An empirical 6-parameter fit to the cascade's 4-zone H(z) data, using a Liouville-inspired functional form. The fit approximately matches the CMB drag at z=1100 but does not reproduce the local R_stellar boost or the secular cosmic web boost. This is included as an alternative parameterization, not as a derivation."

## Comparison to the 4-zone spec

| Approach | Parameters | Fit quality | Honest status |
|----------|------------|-------------|---------------|
| 4-zone spec | 4 (H_bulk, z_trgb, z_rise, z_fall, 3 perturbations) | EXACT match | Empirical fit |
| Pure Liouville code | 6 (E_crit, 0.35, 1.85, -1.78, 0.45, 0.05) | Partial match (only CMB) | Empirical fit, more parameters, worse fit |

The 4-zone spec is **simpler AND fits better** than the Liouville code. There's no advantage to the Liouville code.

## What would make this real

For the code to be a real derivation, we would need:
1. **E_crit derived from microphysics** (e.g., from Liouville 2D CFT critical exponents)
2. **Temperature prefactor 0.35 derived** (e.g., from the Liouville potential μ)
3. **Structural wave amplitude 1.85 derived** (e.g., from DOZZ 3-point function)
4. **CMB drag -1.78 derived** (e.g., from 2D universe death energy integral)
5. **Exponent 0.45 derived** (e.g., from Liouville 2D CFT scaling dimension)
6. **Threshold "off" value 0.05 derived** (e.g., from Liouville 2-point function)

None of these are derived. They're all fitted. The code is empirical fitting.

## File locations

- Test code: `tempcalc/pure_liouville_hubble_test.py`
- This memo: `tempcalc/pure_liouville_hubble_test_results.md`
- Comparison to 4-zone spec: `tempcalc/4zone_quantized_test.py` (v3 tempcalc)
