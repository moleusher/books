To indicate that the unit for the initial concentrations is the molar concentration (according to the value of IUNIT) the keyword *INITIAL CONCENTRATION (0) is required. To indicate that the unit for the initial concentrations is the mole fraction the keyword *INITIAL CONCENTRATION (1) must be used. Each line of this block may contain only one initial concentration definition.

i. An initial concentration definition is composed of one species name and one number for the associated initial concentration.

ii. A species may appear only once.

iii. Species symbol and associated value may appear anywhere in the line, separated by at least one blank space.

Example: (Species A with molar concentration 0.003.)

*INITIAL CONCENTRATIONS (0)

A 0.003

## 13 Keyword *RHO VALUES

In special cases it may be advantageous to use a constant  $ \rho $-value for the approximation of a macromolecular distribution. This can be done in this block. According to the syntax of the previous block *INITIAL CONCENTRATIONS an input line containing the name of a macromolecular species followed by a  $ \rho $-value between 0.0 and 1.0 may occur for every macromolecular species. No adaptation of these  $ \rho $-values during the whole processing time will be done. In the best case, this will increase the numerical stability and decrease the cpu time, but if wrong  $ \rho $-values are chosen a Galerkin approximation will not be possible. Thus we recommend to use this facility only after a simulation with NPROJ=2. By the maximum of the mean chain length ( $ \delta $) during the whole processing time you can suppose a good  $ \rho $-value to be around  $ \rho = 1.0 - 1 / (\delta) $. But notice, that this value will be used during the whole processing time, whereas the standard  $ \rho $-adaptation leads to the optimized  $ \rho $-values at every time step.

Example: (Set of constant  $ \rho $-values for P[] and D[] to 0.99 and 0.998, respectively)

*RHO VALUES (0)

P[] 0.99

D[] 0.998

## 14 Keyword *ENTHALPY COEFFICIENTS

This block is used to define the coefficients for the NASA-fits of thermodynamical data (see [12]) and is not required in two cases:

a. MODEL ≤ 2 and no equilibrium constant is needed (to compute reverse kinetic parameters)

b. all required thermodynamical data can be found in file THERMO

Data given here overwrite data from file THERMO. If MODEL ≥ 3, thermodynamical data should be available for all species in the reaction system, missing coefficients are internally set to zero. Data for species not appearing in the reaction system are ignored.