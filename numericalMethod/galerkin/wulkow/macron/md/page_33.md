## 11 Keyword *GALERKIN APPROXIMATION

The internal approximation of CLD’s is characterized by the number of expansion coefficients NPROJ and the weight function parameter  $ \rho $. This block enables to determine the values of NPROJ as well as to start the simulation with an initial chain length distribution. For each macromolecular species one line may be supplied. The species name must be given completely, i.e. with "[" and "]. A given index (enclosed in "[" and "]) will be ignored. A species name may appear only once. The following particularities have to be regarded.

i. Range of NPROJ:  $ 2 \leq NPROJ \leq 100 $. Default value: NPROJ = 10.

ii. If the simulation has to be started with an initial distribution, there is a possibility to enter measured distributions as well as standard types. A filename with input data can be entered after the keyword *F in the same line. This file must consist of lines containing an index (e.g. chain length) and the concentration of the associated macromolecules. The index must appear in increasing order, the differences between the indices ( $ \geq 1 $) are arbitrary. Comment lines are allowed and have to begin with "C" in the first column. NPROJ is automatically chosen, except when the user prescribes another value. If the computed value is higher than the given value, this will lead to a warning.

Be sure, that the initial distribution is a number chain length distribution or a number molecular weight distribution. That means, that the quotient of the 1st and 0th moments must be the number mean value of the distribution (possibly multiplied by the molecular weight of the monomer) !

To start the simulation by a Schulz-Flory distribution with parameter  $ \rho $, enter *SF followed by a value for  $ \rho $. The initial concentration of the macromolecular species must be given in *INITIAL CONCENTRATION.

An initial distribution of the form  $ u_{1}=c $,  $ u_{s}=0 $ (only monomer at the beginning) can be declared by *D followed by a the value for c.

Example: (Input data for species P[] in the given filename, 7 expansion coefficients prescribed.)

*GALERKIN APPROXIMATION
P[] 7 *F 'today.data'

Example: (Species D[] started as Schulz-Flory distribution with parameter  $ \rho = 0.99 $ and default value NPROJ=10.)

*GALERKIN APPROXIMATION
D[] *SF 0.99

## 12 Keyword *INITIAL CONCENTRATIONS (I) (I=0,1)

This block is used to define the initial concentrations of the declared species (involved in the reaction mechanism) at the very beginning of the simulation (i.e. concentrations of species at starting point of simulation). Only non-zero values are required because the default concentration of all species appearing in the mechanism is zero.