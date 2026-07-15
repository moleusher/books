– adaptivity of the parameters  $ \rho $ and  $ \alpha $

– adaptivity of the truncation index

- numerical preprocessing possible

– treatment of nonlinear problems using a semi-implicit Euler discretization

The algorithm is fully adaptive, i.e. the desired tolerance of the solution leads to automatic choices of order and time-steps, of truncation index and parameters in the Galerkin method and of the tolerance for the numerical preprocessing performed by the SUMMATOR. The time control uses extrapolation in time to obtain higher orders of discretization and an extended moving weight function concept for the choice of the parameters. In each Euler time-step the Galerkin equations are generated using analytical properties as in MACRON (as far as possible) or numerical preprocessing.

With the first version of CODEX interesting realistic models could be treated, in particular heterogeneous degradation processes and coagulation reactions from soot formation with very difficult reaction rate coefficients.