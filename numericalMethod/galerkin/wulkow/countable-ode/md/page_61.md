necessary. This implies several disadvantages: The extrapolation control may be disturbed, since the transformations roughen the entries of the table. The norms used in the error estimation are changed within the extrapolation table. Moreover, for problems with m-invariant or general operators the parameters  $ \rho $,  $ \alpha $ possibly depend on the truncation index, such that additional devices have to be implemented. The most important point is, that the concept of the controlled perturbation of the extrapolation table described in Section 4.1 is destroyed. Finally, in case (i) the scalar products used for the assembling of the Galerkin equations have only to be computed once in one global time step, whereas in the second approach it may happen, that even an increase of the truncation index makes a new computation of all scalar products necessary.

Owing to the above considerations the first way seems to be more promising, extended by an additional feature which is called coefficient reduction. After transformation of  $ u_{T}^{n}(t+T) $ to a space  $ H_{\tilde{\rho},\tilde{\alpha}} $, we choose a (minimal) truncation index  $ \bar{n} $ such that  $ \varepsilon_{\bar{n}} $ will be smaller than the prescribed local tolerance. This avoids instabilities for higher coefficients introduced by the transformation and has been successfully applied in all considered examples.

### 4.2 REALIZATION OF THE GALERKIN METHOD

Analytical Preprocessing. Whenever an analytical evaluation of the scalar products (A linear)

 $$ \left(\begin{matrix}{A u,}&{\psi_{k}(\rho,\alpha)}\\ \end{matrix}\right)_{\rho,\alpha} $$ 

is possible, it is done using the properties of the modified discrete Laguerre polynomials from Section 2.2. Examples for such a preprocessing can also be found in [18], [9], [52] and some results are used herein. The Galerkin equations (3.9) are assembled up to a truncation index  $ n $. By means of a Gauss elimination the approximation  $ u^n $ can be computed together with an error estimation  $ \varepsilon_{n-1} $ due to Lemma 3.3. If the error is still too large, the Galerkin equations are extended by  $ n \to n + 1 $.

For general problems, the coefficients  $ a_k $ also depend on  $ n $. Then the Galerkin equations are assembled up to an index  $ \tilde{n} > n $ and the truncation error is controlled by (3.20).

Numerical Preprocessing. The numerical evaluation of the scalar products (4.26) by the summation algorithm SUMMATOR (Chapter 6) requires some additional considerations. Following the red threat of this work, the tolerances for the summations have to be given adaptively, and the initial grids have to be chosen automatically.