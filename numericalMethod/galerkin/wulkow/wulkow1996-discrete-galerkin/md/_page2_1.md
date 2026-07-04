be given analytically, e.g. if complicated chain-length-dependent reaction coefficients are in the kinetic scheme. Then the right-hand side of the differential equation must be evaluated numerically. A sophisticated ODE-solver, however, detects the errors and disturbances of a numerical right-hand side as a non-smoothness of the differential equation and will fail or shrink down step sizes to unrealistic values, respectively. To avoid this, one could drop the adaptive error control (undesirable) or approximate the right-hand side close to machine accuracy (unrealistic). Thus, many attempts to find a general method for polyreactions ended at the bounds given by the method of lines: whenever analytical preprocessing of any kind is possible, some methods are equivalent, if not, none of the methods above will work.

## Summing up

If we reflect advantages and disadvantages of the methods described above, we get the following picture:

● If the solution distribution is close to a well-known basis function, the most efficient approximation can be obtained by a global approach (global means here: the complete chain length axis is modeled by one set of equations, one weight function). The reason is the global structure of many reaction steps.

● Some kind of a local approach is necessary to resolve the fine structure of a distribution (multiple maxima, steep flanks).

● The derivation of differential equations for any kind of “substitute variables” (moments, generalized moments, lumping parameters, fractions etc.) often requires certain analytical properties depending on the reaction steps in connection with the chosen approach. This analytical preprocessing must be replaced by a general numerical procedure for not restricting the class of problems to the usual ones (this prohibits a method of lines).

• An error estimation is necessary.

● Weight functions, clusters or grids have to be adapted with reaction time.

● No additional assumptions (as, e.g., QSSA) should be necessary.

● The interesting range of the chain length must be given by the method, not by a priori knowledge.

● The computational effort should not (strongly) depend on the degree of polymerization.

A connection of the positive and the prevention of the negative aspects, respectively, by means of new numerical techniques has led to a new numerical method (cf. Tab. 2.), which is called discrete Galerkin h-p-method (h-p: variable grid — variable order).

## The discrete Galerkin h-p-method

## Time discretization

Instead of a method of lines we use a time discretization by means of a Rothe method. This technique was introduced by Bornemann $ ^{20,21} $ for parabolic differential equations and was transferred and extended to polyreaction kinetics in ref. $ ^{9} $. We consider again Eq. (3). The idea is to discretize the countable system as an abstract