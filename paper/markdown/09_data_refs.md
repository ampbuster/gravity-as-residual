<!-- 09_data_refs.md - part of paper.md split (v3.0.13) -->

## Data and code availability

**Code.** All Python code used in the analysis is in the `calculations/` directory of this paper's GitHub repository (https://github.com/ampbuster/gravity-as-residual). Each calculation has a corresponding `.py` file (the script) and a `_results.txt` file (the output), with detailed inline comments explaining SIDC's predictions and the comparison to data. The code is intentionally written in plain Python (numpy, scipy, matplotlib, astropy) without proprietary dependencies; it can be re-run by anyone with a standard scientific Python environment.

**Data.** All observational data used in this paper is from publicly-available catalogs:
- SPARC database (Lelli+ 2016, AJ 152, 157): https://astroweb.cwru.edu/SPARC/
- Tian+ 2024 BCGs (50 brightest cluster galaxies): published in A&A
- Harris 1996 GC catalog: VizieR J/AJ/112/1487
- Usher+ 2013 GC catalog: VizieR J/MNRAS/431/1707
- LZ 2024 direct detection: arXiv:2410.17036
- XENONnT 2023: arXiv:2303.14729
- PandaX-4T 2024: arXiv:2408.00664
- Read+ 2017 isolated dwarfs: MNRAS 471, 2192
- Sawala+ 2014/2016 cluster dwarfs: MNRAS 448, L33 / ApJ 819, L20
- de Blok+ 2008 THINGS: ApJ 679, 1323
- MaNGA DR15 (Sanchez+ 2018): via SDSS
- Planck 2018 cosmological parameters: arXiv:1807.06209
- SH0ES Cepheid calibration: arXiv:2112.04510
- Pantheon+ SNe: https://github.com/PantheonPlusSH0ES

All derived quantities ( $M_{dyn}$, $M_{\rm halo}$, M_*, $g_{\rm obs}$, etc.) are computed in the corresponding calculation scripts, with full statistical methodology (covariance matrices, MCMC posteriors, etc.) documented inline.

**Reproducibility.** The paper's repository includes a `requirements.txt` file listing the exact Python package versions used. Each calculation script can be re-run with `python calculations/<script>.py` to reproduce the corresponding `_results.txt` file. The paper's main PDF (`paper/paper.pdf`) is built from `paper/paper.md` using `pandoc`; the build is deterministic.

**Correspondence.** The author's correspondence details are at the end of this paper; comments and critiques are welcome.

---

## References

[ADD98] N. Arkani-Hamed, S. Dimopoulos, G. Dvali, "The Hierarchy Problem and New Dimensions at a Millimeter," Phys. Lett. B 429 (1998) 263-272.

[Desmond25] H. Desmond, "Modified Newtonian Dynamics: Observational Successes and Failures," arXiv:2505.21638 (2025).

[Golini24] G. Golini, M. Montes, E. R. Carrasco, J. Román, I. Trujillo, "Ultra-deep imaging of NGC1052-DF2 and NGC1052-DF4 to unravel their origins," Astronomy & Astrophysics 684, A99 (2024).

[Gregory00] R. Gregory, V. A. Rubakov, S. M. Sibiryakov, "Brane worlds: the gravity of escaping matter," Class. Quantum Grav. 17 (2000) 4437-4450.

[Júlio25] M. P. Júlio, J. I. Read, M. S. Pawlowski, P. Li, D. Vaz, J. Brinchmann, M. P. Rey, O. Agertz, T. Holmes, "The radial acceleration relation at the EDGE of galaxy formation: testing its universality in low-mass dwarf galaxies," arXiv:2510.06905 (2025).

[Kravtsov24] A. Kravtsov, "On the dark matter content of ultra-diffuse galaxies," arXiv:2406.13732 (2024).

[LawSmith24] J. A. P. Law-Smith, G. Obied, A. Prabhu, C. Vafa, "Astrophysical Constraints on Decaying Dark Gravitons," arXiv:2307.11048 (2024).

[Maldacena97] J. M. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity," Int. J. Theor. Phys. 38 (1999) 1113-1133.

[McGaugh16] S. S. McGaugh, F. Lelli, J. M. Schombert, "Radial Acceleration Relation in Rotationally Supported Galaxies," Phys. Rev. Lett. 117 (2016) 201101.

[Mercado24] F. J. Mercado et al., "Hooks & Bends in the radial acceleration relation," MNRAS 530, 1349 (2024).

[Mistele24] T. Mistele, S. McGaugh, F. Lelli, J. Schombert, P. Li, "Radial acceleration relation of galaxies with joint kinematic and weak-lensing data," arXiv:2310.15248 (2024).

[Obied23] G. Obied, C. Dvorkin, E. Gonzalo, C. Vafa, "Dark Dimension and Decaying Dark Matter Gravitons," arXiv:2311.05318 (2023).

[RS99] L. Randall, R. Sundrum, "An Alternative to Compactification," Phys. Rev. Lett. 83 (1999) 4690-4693.

[Tetradis04] N. Tetradis, "Brane-world evolution with brane-bulk energy exchange," hep-th/0414282 (2004).

[Tian24] Y. Tian, H. Ryu, "A distinct radial acceleration relation across the brightest cluster galaxies," Astronomy & Astrophysics (2024).

[Vărăşteanu25] A. A. Vărăşteanu, M. J. Jarvis, A. A. Ponomareva, H. Desmond, I. Heywood, T. Yasin, N. Maddox, M. Glowacki, M. Maksymowicz-Maciata, P. E. Mancera Piña, H. Pan, "MIGHTEE-HI: The radial acceleration relation with resolved stellar mass measurements," arXiv:2504.20857 (2025).

[CGHS92] C. G. Callan, S. B. Giddings, J. A. Harvey, A. Strominger, "Evaporation of Black Holes in String Theory," Phys. Rev. D 45 (1992) R1005.

[RST93] J. G. Russo, L. Susskind, L. Thorlacius, "The Endpoint of Hawking Radiation," Phys. Rev. D 46 (1992) 3444-3449.

[Padmanabhan15] T. Padmanabhan, "Emergent Gravity and Entanglement," arXiv:1505.00078 (2015).

[Jacobson95] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," Phys. Rev. Lett. 75 (1995) 1260-1263.

[HW96] P. Horava, E. Witten, "Heterotic and Type I String Dynamics in Eleven Dimensions," Nucl. Phys. B 460 (1996) 506-524.

[Gibbons96] G. W. Gibbons, "D-branes and topology change," Class. Quantum Grav. 13 (1996) 1-7.

[Polchinski95] J. Polchinski, "Dirichlet Branes and Ramond-Ramond Charges," Phys. Rev. Lett. 75 (1995) 4724-4727.

[Ryu06] S. Ryu, T. Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT," Phys. Rev. Lett. 96 (2006) 181602.

[Kaluza21] T. Kaluza, "Zum Unitätsproblem der Physik," Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.) 1921 (1921) 966-972.

[KKLT03] S. Kachru, R. Kallosh, A. Linde, S. Trivedi, "de Sitter vacua in string theory," Phys. Rev. D 68 (2003) 046005.

[DGP00] G. Dvali, G. Gabadadze, M. Porrati, "4D gravity on a brane in 5D Minkowski space," Phys. Lett. B 485 (2000) 208-214.

[Koyama07] K. Koyama, "Ghosts in the self-accelerating universe," Class. Quantum Grav. 24 (2007) R231-R253.

[Verlinde16] E. P. Verlinde, "Emergent Gravity and the Dark Universe," SciPost Phys. 2 (2016) 016.

[Yousef13] L. Yousef, A. Sheykhi, "QCD Ghost Dark Energy in RS II Braneworld with Bulk-Brane Interaction," Int. J. Theor. Phys. 53 (2014) 1472-1482.

[Borah25] D. Borah, N. Das, R. Roshan, "Evolving Dark Sector and the Dark Dimension Scenario," arXiv:2507.03090 (2025).

[Deng22] Y. Deng, F. Deng, J. Yang, "JT gravity from holographic reduction of 3D asymptotically flat spacetime," arXiv:2211.13415 (2022).

[Karch00] A. Karch, L. Randall, "Locally localized gravity," JHEP 05 (2001) 008; arXiv:hep-th/0011156 (2000).

[Randall99] L. Randall, R. Sundrum, "An alternative to compactification," Phys. Rev. Lett. 83 (1999) 4690-4693; arXiv:hep-th/9906064.

[Teitelboim83] C. Teitelboim, "Gravitation and Hamiltonian Structure in Two Space-Time Dimensions," Phys. Lett. B 126 (1983) 41-45.

[Jackiw85] R. Jackiw, "Lower Dimensional Gravity," Nucl. Phys. B 252 (1985) 343-356.

[DOZZ94] H. Dorn, H.-J. Otto, "Two and three-point functions in Liouville theory," Nucl. Phys. B 429 (1994) 375-388; A. Zamolodchikov, Al. Zamolodchikov, "Structure constants and conformal bootstrap in Liouville field theory," arXiv:hep-th/0506138.

[Meunier24] J. Meunier, B. Gallet, "Effective transport by 2D turbulence: Vortex-gas theory vs. scale-invariant inverse cascade," arXiv:2412.17431 (2024); Phys. Rev. Lett. 134 (2025) 074101.

---

