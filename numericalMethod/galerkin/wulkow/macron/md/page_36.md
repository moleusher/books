## 18 *PRINT PARAMETER

This block consists of one line to define the integer print-parameter IPRINT for additional simulation output on several files. IPRINT may be chosen in the range  $ 0 \leq IPRINT \leq 6 $. The effect of IPRINT depends on the special program version (graphic adaption). See the information menu in an interactive session. As a rule IPRINT=0 and IPRINT=6 correspond respectively to minimal and maximal output.

Example: (Maximal output)

*PRINT PARAMETER

## 19 *DISTRIBUTION OUTPUT

For the output of a CLD between chain length SMIN and SMAX with increment INC, these three integer values have to be given in one line.

Example: (CLD output in the chain length range 1 – 10000 with increment 100, e.g. 100 points)

*DISTRIBUTION OUTPUT

1 10000 100

### 4.3 Macromolecular Processes

A number of typical macromolecular reaction steps is implemented up to now. The modular character of the method allows an easy continuation of this list, if the reactions are analytically preprocessable. Whenever a reaction in block *REACTION SYSTEM contains at least one pair “[ ]” (sign of a macromolecular species), the reaction input line is interpreted as a macromolecular reaction step. The reaction is then examined on whether it matches one of the implemented reaction steps below. Therefore the user has to regard strictly the syntax of a macromolecular reaction. The reactions are related to the reaction numbers below, a control output is given. In case of syntax errors or reactions not to analyze, suggestions will be made concerning input line.

In the following we use the names P☐, Q☐ for macromolecules, X, Y and Z for standard chemical species and N, M for integer values to characterize the index of a macromolecule. In case of no other specification, the integers N, M are running variables N, M=1,2,3,... Thus most of the reactions below are synonyms for infinite reaction systems (see Introduction).

The macromolecular reaction steps also have an effect on the standard chemical species expressed in terms of their total concentration (the 0th moment). The number of involved chemical species in the macromolecular reaction is arbitrary. The degradation processes (REAC=9, 10) are an exception, since the situation is more complicated and no chemical species should occur. We only present standard forms for the reaction steps. The letter k always denotes the reaction constant. The attributes closed and open indicate whether the expansion coefficients generally depend on higher indices. This is important for the choice of NPROJ, if the user only wants to compute statistical moments.

i. Initiation (REAC = 0, closed). Initiation of macromolecular species by chemical species has the form

 $$ X+Y\Rightarrow P[1]+Z $$ 