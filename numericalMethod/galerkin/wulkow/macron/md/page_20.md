*HEAD
--- Quasi Living Radical Polymerization ---
CH. H. J. Johnson et al., Aust. J. Chem. 43, (1990), 1215
*MODEL PARAMETER
1
*UNIT SYSTEM
5
*REACTION SYSTEM
    P + X    => PX    (1.D9)
    PX    => P + X    (1.D-5)
    P[N]X    => P[N] + X    (1.D-5)
    P[N] + X    => P[N]X    (1.D9)
    P + M    => P[1]    (2.D3)
    P[N] + M    => P[N+1]    (2.D4)
    P + P    => D    (1.D7)
    P + P[N]    => D + P[N]    (2.D4)
    P[N] + P[M]    => D[N+M]    (1.D7)
*GALERKIN PROJECTION
P[]    2
D[]    2
P[]X    2
*INITIAL CONCENTRATIONS (0)
M    10.0DO
X    0.0DO
PX    0.1DO
*ACCURACY
1.0D-4
*INTEGRATION BOUNDS
0.0
750000.0
*PRINT PARAMETER
0
*DISTRIBUTION OUTPUT
1 10000 100

<div style="text-align: center;">Table 5: Input file CHEMIN for Quasi Living Radical Polymerization.</div>
