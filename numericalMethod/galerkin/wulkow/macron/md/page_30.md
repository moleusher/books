body. "="," real number", "species name" and "+" must be separated by at least one blank. If no species composition of the third body is given, this third body will be regarded as the unweighted sum of all species.

vi. Each third body may be declared only once.

vii. The third body declaration may appear anywhere on the line.

Example: (Declaration of M)

 $ ^{*} $THIRD BODIES

M = 0.35 H^{+} + 6.5 WATER + 0.4 OH^{+} + 1.5 H_{2}

## 6 Keyword *UNIT SYSTEM

This block specifies the unit system for the actual system. All input values in CHEMIN are assumed to be given in these units. Possible choices are listed in Table 8.

Syntax rules:

i. This block must consist of exactly one line besides the keyword line containing the value of the integer number IUNIT. IUNIT specifies the unit system for the actual system.

Example: (Choice of unit system 1, see Table 8.)

*UNIT SYSTEM


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">IUNIT</td><td colspan="6">unit system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>T</td><td style='text-align: center; word-wrap: break-word;'>P</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>E</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,m^{3}) $</td><td style='text-align: center; word-wrap: break-word;'>(K)</td><td style='text-align: center; word-wrap: break-word;'>(PA)</td><td style='text-align: center; word-wrap: break-word;'>$ (g,m^{3}) $</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,m^{3},sec) $</td><td style='text-align: center; word-wrap: break-word;'>(J)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>(KJ)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,cm^{3}) $</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>$ (atm) $</td><td style='text-align: center; word-wrap: break-word;'>$ (g,cm^{3}) $</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,cm^{3},sec) $</td><td style='text-align: center; word-wrap: break-word;'>(J)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>(KJ)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,l) $</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>$ (cal,l) $</td><td style='text-align: center; word-wrap: break-word;'>$ (g,l) $</td><td style='text-align: center; word-wrap: break-word;'>$ (mole,l,sec) $</td><td style='text-align: center; word-wrap: break-word;'>(cal)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>(kcal)</td></tr></table>

<div style="text-align: center;">Table 8: Unit systems. (C: concentration, T: temperature, P: pressure, S: density, A and E: parameters of the Arrhenius law)</div>


## 7 Keyword *TEMPERATURE

The block consists of one line with a positive real number setting the initial value of temperature. No initial temperature is required if MODEL=1 or MODEL=2, no Arrhenius law is used and the initial concentrations are not given in mole fractions.