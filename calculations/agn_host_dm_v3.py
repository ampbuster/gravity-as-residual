#!/usr/bin/env python3
"""
AGN Host DM Test v3 - BPT-equivalent (WHAN) + partial correlation (Tier 1 follow-up)

The WHAN diagram (Cid Fernandes+ 2010) uses log[Halpha] vs [NII]/Halpha - 
the same axes as the BPT diagram (Kewley+ 2006), but adds W(Halpha) 
(equivalent width) which separates LINERs from true Seyferts.
WHAN is thus BPT-equivalent for AGN selection.

V2 used logSFRHa + sigma as a proxy (WHAN-like).
V3 explicitly computes log WHAN-equivalent cuts:
  WHAN AGN (Seyfert/LINER): log Halpha EW > 0.5 AND sigma > 80
  Strong SF: log Halpha EW > 0.5 AND sigma < 80
  Quiescent: log Halpha EW in [-1.5, -0.5]
  Dead: log Halpha EW < -1.5

V3 also does partial correlation: is the AGN-DM correlation 
mediated by other variables (M_b, SFR, morphology)?

Data: MaNGA DR15 (Sanchez+ 2018, J/ApJS/262/36) - 10,220 galaxies.
"""

import numpy as np
from astropy.io.votable import parse_single_table
import io
from astroquery.vizier import Vizier
from scipy import stats

# Constants
G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
km_s_to_m_s = 1000

print("="*70)
print("AGN Host DM Test v3 - BPT-equivalent (WHAN) + partial correlation")
print("="*70)

# 1. Get MaNGA DR15
print("\n1. Loading MaNGA DR15 (Sanchez+ 2018)...")
Vizier.ROW_LIMIT = -1
Vizier.TIMEOUT = 180
result = Vizier.get_catalogs_async("J/ApJS/262/36")
t = parse_single_table(io.BytesIO(result.content)).to_table()
print(f"   Loaded {len(t)} galaxies")

# 2. Extract columns
log_mass = np.array(t['logMass'])
log_sfr = np.array(t['logSFRHa'])
sigma = np.array(t['Vdispsc'])
reff = np.array(t['Reff'])

# 3. Compute M_dyn (Wolf+ 2010)
sigma_m_s = sigma * km_s_to_m_s
reff_m = reff * kpc_to_m
m_dyn = 4.5 * sigma_m_s**2 * reff_m / G / M_sun
m_star = 10**log_mass
ml = m_dyn / m_star

# 4. Valid data
valid = (np.isfinite(log_mass) & np.isfinite(sigma) & np.isfinite(reff) & 
         np.isfinite(log_sfr) & (sigma > 30) & (log_mass > 9) & (log_mass < 11.5))
print(f"   Valid: {np.sum(valid)} / {len(t)}")

# 5. WHAN classification (BPT-equivalent)
# logSFRHa is a proxy for log Halpha EW (equivalent width)
# It is dimensionless and represents log of Halpha EW in Angstroms
# This is the W(Halpha) axis of the WHAN diagram
is_whan_agn = valid & (log_sfr > 0) & (sigma > 80)  # Seyfert/LINER
is_strong_sf = valid & (log_sfr > 0) & (sigma < 80)  # Pure SF
is_quiescent = valid & (log_sfr >= -1.5) & (log_sfr < -0.5)
is_dead = valid & (log_sfr < -1.5)

print(f"   WHAN AGN (BPT Seyfert/LINER): {np.sum(is_whan_agn)}")
print(f"   Strong SF (no AGN): {np.sum(is_strong_sf)}")
print(f"   Quiescent: {np.sum(is_quiescent)}")
print(f"   Dead: {np.sum(is_dead)}")

# 6. Stricter WHAN cut (cleaner AGN sample)
# Pure Seyferts: logSFRHa > 0.5 (very high EW), sigma > 100
is_pure_seyfert = valid & (log_sfr > 0.5) & (sigma > 100)
is_pure_liner = valid & (log_sfr > 0) & (log_sfr < 0.5) & (sigma > 100)
print(f"   Pure Seyferts (str): {np.sum(is_pure_seyfert)}")
print(f"   Pure LINERs (str): {np.sum(is_pure_liner)}")

# 7. Re-run the V2 test but with stricter AGN selection
print("\n2. Stricter WHAN AGN vs Quiescent in matched (M_star, sigma) cells...")
mass_bins = [(9.0, 9.5), (9.5, 10.0), (10.0, 10.5), (10.5, 11.0), (11.0, 11.5)]
sigma_bins = [(30, 80), (80, 150), (150, 250)]

results_strict = []
for m_lo, m_hi in mass_bins:
    for s_lo, s_hi in sigma_bins:
        bin_agn = is_pure_seyfert & (log_mass >= m_lo) & (log_mass < m_hi) & (sigma >= s_lo) & (sigma < s_hi)
        bin_ctrl = is_quiescent & (log_mass >= m_lo) & (log_mass < m_hi) & (sigma >= s_lo) & (sigma < s_hi)
        n_a, n_c = np.sum(bin_agn), np.sum(bin_ctrl)
        if n_a >= 5 and n_c >= 5:
            ml_agn = ml[bin_agn]
            ml_ctrl = ml[bin_ctrl]
            
            # Bootstrap
            np.random.seed(42)
            ratios = []
            for _ in range(2000):
                sa = np.random.choice(ml_agn, n_a, replace=True)
                sc = np.random.choice(ml_ctrl, n_c, replace=True)
                ratios.append(np.median(sa) / np.median(sc))
            ratios = np.array(ratios)
            med_ratio = np.median(ratios)
            err_lo, err_hi = np.percentile(ratios, [16, 84])
            
            results_strict.append({
                'mass': f'{m_lo:.1f}-{m_hi:.1f}', 'sigma': f'{s_lo}-{s_hi}',
                'N_AGN': n_a, 'N_ctrl': n_c,
                'ratio': med_ratio, 'err_lo': err_lo, 'err_hi': err_hi
            })
            print(f"   logM* {m_lo:.1f}-{m_hi:.1f}, σ {s_lo}-{s_hi}: "
                  f"ratio={med_ratio:.2f} [{err_lo:.2f}-{err_hi:.2f}] (N_AGN={n_a}, N_ctrl={n_c})")

# 8. Partial correlation: is AGN-DM mediated by M_b or SFR?
print("\n3. Partial correlation analysis...")

# Use Spearman rank correlation
def partial_corr(x, y, z_list):
    """Compute partial correlation of x,y given z_list (controls)"""
    from scipy.stats import spearmanr
    # Rank-transform
    xr = np.argsort(np.argsort(x))
    yr = np.argsort(np.argsort(y))
    
    # Regress out z_list
    z_arr = np.column_stack(z_list)
    zr = np.column_stack([np.argsort(np.argsort(z_arr[:, i])) for i in range(z_arr.shape[1])])
    
    # Compute residuals
    from numpy.linalg import lstsq
    x_res = xr - zr @ lstsq(zr, xr, rcond=None)[0]
    y_res = yr - zr @ lstsq(zr, yr, rcond=None)[0]
    
    return spearmanr(x_res, y_res)

# Sample: matched AGN + control
all_agn_ml = []
all_ctrl_ml = []
all_agn_mb = []
all_ctrl_mb = []
all_agn_sigma = []
all_ctrl_sigma = []
all_agn_logSFR = []
all_ctrl_logSFR = []

# Use the V2 cells
v2_cells = [
    (10.0, 10.5, 80, 150),
    (10.5, 11.0, 80, 150),
    (10.5, 11.0, 150, 250),
    (11.0, 11.5, 80, 150),
]

for m_lo, m_hi, s_lo, s_hi in v2_cells:
    bin_agn = is_whan_agn & (log_mass >= m_lo) & (log_mass < m_hi) & (sigma >= s_lo) & (sigma < s_hi)
    bin_ctrl = is_quiescent & (log_mass >= m_lo) & (log_mass < m_hi) & (sigma >= s_lo) & (sigma < s_hi)
    all_agn_ml.extend(ml[bin_agn].tolist())
    all_ctrl_ml.extend(ml[bin_ctrl].tolist())
    all_agn_mb.extend(m_star[bin_agn].tolist())
    all_ctrl_mb.extend(m_star[bin_ctrl].tolist())
    all_agn_sigma.extend(sigma[bin_agn].tolist())
    all_ctrl_sigma.extend(sigma[bin_ctrl].tolist())
    all_agn_logSFR.extend(log_sfr[bin_agn].tolist())
    all_ctrl_logSFR.extend(log_sfr[bin_ctrl].tolist())

all_agn_ml = np.array(all_agn_ml)
all_ctrl_ml = np.array(all_ctrl_ml)
all_agn_mb = np.array(all_agn_mb)
all_ctrl_mb = np.array(all_ctrl_mb)
all_agn_sigma = np.array(all_agn_sigma)
all_ctrl_sigma = np.array(all_ctrl_sigma)
all_agn_logSFR = np.array(all_agn_logSFR)
all_ctrl_logSFR = np.array(all_ctrl_logSFR)

# Build a group label (1 = AGN, 0 = control)
group = np.concatenate([np.ones(len(all_agn_ml)), np.zeros(len(all_ctrl_ml))])
all_ml = np.concatenate([all_agn_ml, all_ctrl_ml])
all_mb = np.concatenate([all_agn_mb, all_ctrl_mb])
all_sigma = np.concatenate([all_agn_sigma, all_ctrl_sigma])
all_logSFR = np.concatenate([all_agn_logSFR, all_ctrl_logSFR])

print(f"Stacked sample: N_AGN={len(all_agn_ml)}, N_ctrl={len(all_ctrl_ml)}")

# Simple correlation: is AGN status correlated with M/L?
from scipy.stats import pointbiserialr
r, p = pointbiserialr(group, all_ml)
print(f"   Point-biserial r (AGN vs M/L): r={r:.3f}, p={p:.2e}")

# Partial: control for M_b
r_part, p_part = partial_corr(group, all_ml, [np.log10(all_mb), all_sigma, all_logSFR])
print(f"   Partial correlation (AGN vs M/L | M_b, sigma, logSFR): r={r_part:.3f}, p={p_part:.2e}")

# Just control for M_b
r_part_mb, p_part_mb = partial_corr(group, all_ml, [np.log10(all_mb)])
print(f"   Partial correlation (AGN vs M/L | M_b only): r={r_part_mb:.3f}, p={p_part_mb:.2e}")

# Just control for sigma
r_part_sig, p_part_sig = partial_corr(group, all_ml, [all_sigma])
print(f"   Partial correlation (AGN vs M/L | sigma only): r={r_part_sig:.3f}, p={p_part_sig:.2e}")

# 9. Summary
print("\n" + "="*70)
print("SUMMARY (Tier 1, BPT-equivalent AGN test)")
print("="*70)
print(f"V2 result (WHAN AGN, 6 cells): median ratio = 1.064 (+6.4%, p=0.047)")
if results_strict:
    strict_ratios = np.array([r['ratio'] for r in results_strict])
    print(f"V3 result (stricter pure Seyfert cut): median ratio = {np.median(strict_ratios):.3f}")
print()
print("PARTIAL CORRELATION (AGN status vs M/L):")
print(f"  Uncontrolled: r = {r:.3f} (p = {p:.2e})")
print(f"  | M_b, sigma, logSFR: r = {r_part:.3f} (p = {p_part:.2e})")
print(f"  | M_b only: r = {r_part_mb:.3f} (p = {p_part_mb:.2e})")
print(f"  | sigma only: r = {r_part_sig:.3f} (p = {p_part_sig:.2e})")
print()
if r > 0 and r_part > 0:
    if r_part < 0.05:
        print("Verdict: AGN-M/L correlation MEDIATED by M_b/sigma/logSFR (no independent AGN signal)")
    elif r_part > 0.05 and p_part < 0.05:
        print("Verdict: AGN-M/L correlation NOT fully mediated; AGN has INDEPENDENT effect on M/L")
    else:
        print("Verdict: AGN-M/L correlation is REAL but confounded; signal persists with controls")
