# SPARC Galaxy Database (Local Copy)

This directory contains a local copy of the SPARC database for galactic-scale
rotation curve analysis.

## Source

- Lelli, McGaugh, Schombert 2016, AJ 152, 157
- URL: https://astroweb.case.edu/SPARC/
- 175 late-type galaxies (spirals and irregulars)
- Spitzer photometry at 3.6 μm + HI rotation curves
- Citation: Lelli, F.; McGaugh, S. S.; Schombert, J. M., 2016, AJ, 152, 157

## Files

- `Rotmod_LTG.zip` — Original zipped download
- `*_rotmod.dat` — 175 rotation curve files

## File format

Each `_rotmod.dat` file contains:
```
# Distance = X Mpc
# Rad	Vobs	errV	Vgas	Vdisk	Vbul	SBdisk	SBbul
# kpc	km/s	km/s	km/s	km/s	km/s	L/pc^2	L/pc^2
0.16	1.99	1.50	1.86	3.75	0.00	30.32	0.00
...
```

- Rad: radius (kpc)
- Vobs: observed rotation velocity (km/s)
- errV: error on Vobs (km/s)
- Vgas: gas contribution (km/s)
- Vdisk: stellar disk contribution (km/s)
- Vbul: stellar bulge contribution (km/s)
- SBdisk, SBbul: surface brightness (L/pc²)

## How to use

```python
import numpy as np
data = np.loadtxt('UGC02885_rotmod.dat', comments='#')
rad = data[:, 0]   # kpc
vobs = data[:, 1]  # km/s
vgas = data[:, 3]  # km/s
vdisk = data[:, 4] # km/s
```

## Related data (not yet downloaded)

- THINGS: Walter et al. 2008 (19 high-res rotation curves)
- LITTLE THINGS: Hunter et al. 2012 (26 dwarf galaxies)
- SPARC ETG: Early-type galaxies
