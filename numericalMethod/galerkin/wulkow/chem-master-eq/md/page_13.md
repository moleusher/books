Algebraic Galerkin equations. At the core of discrete Galerkin methods, algebraic equations must be constructed. For simplicity, we choose the implicit Euler operator equation (1.8) for the first order approximation  $ u_1 = u_0 + \Delta u_0 $. Let the Galerkin approximation of  $ \Delta u_0 $ in  $ \mathcal{H}_r $ be defined in terms of the coefficients  $ \Delta \eta_0 = ((\Delta \eta_0)_1, \ldots, (\Delta \eta_0)_r) $. Upon applying inner products with each orthogonal polynomial, we arrive at the formal relations

 $$ \left\langle\sum_{k=0}^{r}(q_{k}-\tau\mathcal{A}q_{k})(\Delta\eta_{0})_{k},q_{l}\right\rangle_{\psi}=\langle\tau\mathcal{A}u_{0},q_{l}\rangle_{\psi}. $$ 

From this, using orthogonality properties, we obtain algebraic systems of the kind (1.6) already shown in the context of the MOL, i.e.

 $$ \begin{array}{r c l}{(\Gamma_{r}-\tau A)\Delta\eta_{0}}&{=}&{b}\end{array} $$ 

in terms of the  $ r \times r $-matrices

 $$ \Gamma_{r}=\mathrm{diag}(\gamma_{k})\quad and\quad A=(\langle\mathcal{A}q_{k},q_{l}\rangle_{\psi})_{kl} $$ 

and with right-hand side coefficients  $  b = (b_1, \ldots, b_r)  $. In a similar way we obtain coefficients  $ \Delta\eta_1 $ for the Galerkin approximation of the correction  $ \Delta u_1 $. The solution of these linear equations is usually not difficult, since they are of low dimension  $ r $. The difficulty, however, lies in the computation of the matrix elements for  $ \Gamma $,  $ A $ and the vector elements  $ b $, which require infinite sums to be approximated.

Gauss-Christoffel summation. In order to compute the inner products  $ \langle\cdot,\cdot\rangle_{\psi} $ we have to approximate infinite sums. In [9, Section 9.7], an adaptive discrete multigrid algorithm (code SUMMATOR), which has been developed by Wulkow, has been presented to approximate large sums efficiently. In the course of further improvement of the polyreaction algorithms, discrete Gauss-Christoffel methods have been worked out intimately linked to the structure of the weighted inner products. For the trivial weight  $ \psi\equiv1 $, which we suggest to apply in the CME context, this leads to a discrete Gauss-Legendre quadrature, i.e., to a high-order summation technique. On the basis of the theory for Gauss-Christoffel quadrature, the nodes and weights can easily be computed also in the discrete case: Given a truncation index r, a triangular eigenvalue problem must be solved, for details see, e.g., [9]. It has been shown in [34] that the “aliasing error” introduced by the Gauss-Christoffel summation does not affect the quality of a Galerkin approximation of order r, if only at least  $ r+1 $ nodes are used.