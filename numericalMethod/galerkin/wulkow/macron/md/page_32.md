iii. The species symbol is a unique sequence of (up to 10) alphanumeric digits (but no blank space) and may not start with a "*" or "()". A species symbol is either a species name, a third body name or a macromolecular species. The latter is identified by containing the pair "[]" in the name, "[]" and "[]" may stay anywhere in a species symbol. The string enclosed in "[]" and "[]" will be interpreted as index (e.g. chain length). More than one pair is not allowed. The name of such a species is the species symbol without the index. For example the species symbol "P[M]" leads to the species name P[] with index M and "N[I+2]0" to the species name N[I]0 with index I+2. In general the index of every macromolecular species will be ignored for its identification. Note that "[]" and "[]" are parts of the name. The syntax for the species will be checked. No stoichiometric coefficients can be given.

iv. There are 3 types of valid delimiters:

+ delimiter between two species symbols (reactants, products)

=> delimiter between reactants and products for an irreversible equation

<=> delimiter between reactants and products for a reversible equation

v. The kinetic parameter field consists of 1 up to 3 numbers (separated by commas and enclosed in parenthesis). If only one number is given, this value is assumed to be the rate reaction coefficient. If 2 (or 3) numbers are given, the rate constant is computed internally according to the (modified) Arrhenius law (RC: reaction constant, TEMP: temperature):

 $$ \mathrm{R C~}:=\mathrm{~A~}*\mathrm{~e x p}(-{\mathrm{E}}/(\mathrm{R}*\mathrm{T E M P}))*\mathrm{~T E M P}**{\mathrm{A L P H A}} $$ 

where the first kinetic parameter is assumed to be A, the second to be E and the possible third to be ALPHA. To define the rate constants for a reversible equation there are two possibilities:

a) A reversible reaction is followed by two kinetic parameter fields, where the first is assigned to the direction "=>" and the second to "<=".

b) If there is only one kinetic parameter field after a reversible equation, then the reverse rate constant is computed via the equilibrium constant (this is only possible if thermodynamical data is available for all species appearing in this equation).

vi. The use of reaction inequalities is possible, i.e. an equation may have no reactant or no product, to allow the modeling of addition (subtraction) of substances during the reaction. Note that this is in contradiction with the assumptions made for the modeling of thermodynamics.

vii. A reaction equation may consist of an arbitrary number of lines, i.e. the input is regarded as a stream and the separation of the equations is not indicated by the end of the line, but by the end of the associated kinetic parameter field.

viii. The syntax of reactions containing a macromolecular species is checked to match one of the implemented macromolecular processes (see Appendix 4.3).

Example: (Three reactions, see also Figure 1 and 5 at page 8 and 17, respectively.)

 $$ \begin{array}{r l r l r l r l}&{*\mathrm{R E A C T I O N~S Y S T E M}}\\ &{H2+O2}&{=>}&{H^{*}+H O2}&{\quad(.6D2)}\\ &{O3+M}&{<=}&{O2+O}&{+}&{M}&{(0.38D09,\quad0.95D0D5)}\\ &{C2H2+O}&{<=}&{C O+C H2}&{\quad(0.41D9,0.7D4,1.5)\quad(.2D8,1.D3,1.)}\end{array} $$ 