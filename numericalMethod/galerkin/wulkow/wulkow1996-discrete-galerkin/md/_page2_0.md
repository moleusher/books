● The computation of the generalized moments can be done numerically stable, the statistical moments can directly be obtained from the generalized moments. The weighted Galerkin method is somewhat like a pre-conditioner for the method of moments.

● The quality of the weight function and the approximation can be estimated.

● There is a global representation of the molecular weight distribution.

● The closing-problem of the moment equation for certain processes (e.g. polymer degradation) is solved in a natural way.

But resuming, the weighted Galerkin method is not flexible enough for a general treatment of polyreactions and requires too much insight again. The number of expansion coefficients has to be set a priori, no change is possible during the time integration (drawback of a method of lines, see below).

In order to overcome these problems (a part of them at least), Wulkow $ ^{9} $ extended the family of weight functions to

 $$ \psi\left(s;\rho,\alpha\right):=\left(1-\rho\right)^{1-\alpha}\binom{s-1-\alpha}{s-1}\rho^{s-1}\qquad0<\rho<1\qquad\alpha>-1 $$ 

including Schulz-Flory ( $ \alpha = 0 $) and Poisson distributions with parameter  $ \lambda $ ( $ \rho \cdot \alpha = \lambda $,  $ \rho $ small) as special cases. In combination with a time discretization of Rothe's type (see below), the extended method allows the treatment of nearly all types of reaction steps without analytical preprocessing, but was still restricted to distributions of a certain form. So after all, the situation was unsatisfactory for a general purpose solver, even if some interesting problems could be solved $ ^{9,18,19} $.

Related to the discrete weighted Galerkin-methods are discrete weighted collocation methods, where certain basis functions are chosen in a way that the kinetic equations are exactly fulfilled at nodes n of the chain length axis and the error for the residual is minimized $ ^{10} $. The transformation of the original balance equations into a numerical algorithm may be easier for collocation methods than for Galerkin methods, but there are difficulties with the change of the collocation nodes with time — in particular for strongly varying distributions. The computation of the collocation nodes depends on the choice of a weight function again.

Summarizing, the discrete weighted Galerkin and collocation methods have not been extensively applied to processes resulting in multi-modal or complex distributions because of restrictions induced by the weight functions.

## The method of lines' drawback

The most methods described above are methods of lines (MOL): a time-dependent distribution  $ P_s(t) $,  $ s $ “large”, is approximated by variables  $ a_j(t) $,  $ j $ “small”. A certain approximation scheme leads to differential equations for the  $ a_j $’s and the resulting system is numerically solved by a standard ODE-solver (ODE: ordinary differential equation). A reformulation of the approximation — change of number of  $ a_j $’s, reformulation of lumping scheme, new grid, etc. — during the time-integration is not possible or very difficult (regridding problem, often described by algebraic conditions on the coefficients  $ a_j(t) $). In many interesting cases, the equations for the  $ a_j $’s cannot