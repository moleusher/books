Adaptive choice of the summation tolerance. The numerical evaluation of the scalar products (4.26) or (3.11) by the summation algorithm SUMMATOR (Chapter 6) requires a careful matching between the error control of the Galerkin process and the tolerance of the summation. Without information about the condition number of the linear system arising from the Galerkin equation, a sufficient summation tolerance cannot be given a priori. Even if for fixed truncation index n such a tolerance is known, an increase of n may increase the condition number, such that a summation performed for the old n is no longer sufficiently accurate. Then all summations have to be repeated. Thus the following algorithm is suggested:

Each new entry of the Galerkin equations is computed with a basic tolerance  $ tol_S^0 $, on its own summation grid, which is stored. For fixed  $ n $ the approximation  $ \tilde{u}^n $ is computed for  $ tol_S^0 $ and  $ tol_S^k := c \cdot tol_S^0 $, where  $ 0 < c < 1 $ is a reduction factor. In actual computations  $ c = 0.5 $ has been set. Comparison between the two results yields an estimation of the error  $ \|u^n - \tilde{u}^n\| $, which can be regarded as a truncation error. The summation tolerance is increased until

 $$ \left|\left|u^{n}-\tilde{u}^{n}\right|\right|<\frac{1}{2}\left|\left|\tilde{u}^{n}-\tilde{u}^{n-1}\right|\right| $$ 

or  $ c^k \tan^0_S < \tan^max_S $,  $ \tan^max_S $ chosen before. If for  $ \bar{n} > n $ a refinement of a certain grid is required, this can be done by using the stored information.

Initial grids The choice of the initial grids for the SUMMATOR uses the only general insight known at the beginning of the summation: all terms in the sum of an  $ H_{\rho,\alpha} $ - scalar product must be dominated asymptotically by the factor

 $$ \rho^{s-1}=e^{-\lambda(s-1)},\lambda>0, $$ 

from the weight function  $ \Psi_{\rho,\alpha} $. Thus the initial nodes are taken equidistant – in the logarithmic scale, where the actual value of  $ \rho $ can give hints about the scale of the required upper bound of the sum. As pointed out in Chapter 6, the initial number of points has to be odd, the actual implementation uses 3–11 points with a controlling device.

Evaluation of a Galerkin Approximation. The pointwise evaluation of a Galerkin approximation

 $$ u^{n}(s)=\sum_{k=0}^{n}a_{k}\psi_{k}(s;\rho,\alpha) $$ 

has been realized by a fast and stable summation algorithm (adjoint summation) suggested by DEUFLHARD [14] for special functions satisfying a linear