wherein  $ \rho < 1 $ is an additional safety factor. This timestep control can be used for finite-dimensional ODE systems as well as for infinite dimensional CODEs.

The trick in the infinite dimensional case is that all arising norms of state space terms can be approximated to prescribed accuracy within the Galerkin setting. Suppose we are given some Galerkin subspace  $ \mathcal{H}_r $; then we may compute an associated spatial error estimate (details to be worked out in the Section 2 below)

 $$ \left\| \mathbf{p}_{r}-\mathbf{p} \right\|\leq TOL_{p}. $$ 

Here TOL $ _{p} $ is an imposed spatial error tolerance. In [3], Bornemann linked this error tolerance to the user-specified tolerance TOL, on the basis of approximation theory, as

 $$ \mathrm{TOL}_{p}=c\frac{1}{8}\mathrm{TOL} $$ 

to ensure reliable working of the time step control The factor  $ c < 1 $ can be considered as a safety factor, a choice of  $ c = 1/4 $ covers linear and quadratic problems with sufficient accuracy.

As already mentioned above, the ROM permits an easy adaptation of Galerkin subspaces for the solution of the arising boundary value problems (1.8) or (1.9). Moreover, this method is also clearly preferable for theoretical reasons that are elaborated in [4, 33]. Numerical evidence in polyreaction kinetics simulations clearly confirms that the above mentioned difficulty of “leaving” the subspace (as apparent in MOL) is significantly reduced, see again [33]. In connection with the “moving weight function” concept, ROM turned out to be both robust and extremely well-suited for spatial and temporal adaptivity in complex real life problems. On this basis, we suggest this approach also for the present context of the CME.

## 2 Realization of Discrete Galerkin Methods

In this section, we work out details on the choice of basis functions  $ \{q_k\} $. Given an inner product associated with the Hilbert spaces  $ \mathcal{H}_r \subset \mathcal{H} $, which may be weighted or unweighted, we arrive at orthogonal systems of polynomials of discrete variables. For this purpose, we partly recall material already given in [10, 33] and modify it for use in the present CME context.