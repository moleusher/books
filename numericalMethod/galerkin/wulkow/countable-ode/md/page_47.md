The application of the implicit Euler scheme to an abstract ODE (1.52) with step size  $ \tau $ requires the solution of systems

 $$ \left(I-\tau A\right)u=\varphi,A\operatorname{l i n e a r}, $$ 

with respect to u. For nonlinear operators the semi-implicit Euler method [16] (see Section 5, (4.1)) can be used, leading to problems of the same structure.

We assume that for  $ \varphi \in H_{\rho,\alpha} $ (3.8) has a unique solution  $ u $ in  $ H_{\rho,\alpha} $. With the orthogonal projection (2.39) the Galerkin equations

 $$ u^{n}-\tau\mathcal{P}_{n}^{\rho,\alpha}A u^{n}=\mathcal{P}_{n}^{\rho,\alpha}\varphi~,~u^{n}\in H_{\rho,\alpha}^{n}~,~n=0,1,\ldots $$ 

are equivalent to

 $$ \left(u^{n}-\tau A u^{n},\psi_{k}\right)_{\rho,\alpha}=\left(\varphi,\psi_{k}\right)_{\rho,\alpha},u^{n}\in H_{\rho,\alpha}^{n},k=0,\cdots,n. $$ 

Inserting the basis expansion of u in  $ H_{\rho,\alpha} $, for fixed n this is seen to be a linear system:

 $$ \left(I-\tau B\right)a=b,B:=\left(b_{j k}\right),b_{j k}:=\left(A\psi_{k},\psi_{j}\right)_{\rho,\alpha}, $$ 

 $ a = (a_0, \ldots, a_n) $ the coefficients of  $ u $ and  $ b = (b_0, \ldots, b_n) $ the coefficients of  $ \varphi $ in the  $ H_{\rho,\alpha} $ - basis. The assembling of these equations requires projections of the form  $ Au $, respectively  $ A\psi_j(\rho, \alpha) $,  $ j = 0, \ldots, n $, implying the application either of analytical properties or of numerical summation. For  $ m $-invariant or general operators, the Galerkin equations depend on the truncation index  $ \tilde{n} $ from (3.7) or the summation tolerance. Thus the Galerkin approximation will be of the form (3.1) again. In this work we will only treat two cases theoretically and omit an examination of perturbed Galerkin equations:

(i) A is the generator of a  $ C_{0} $ - semigroup of contractions

(ii)  $ \tau A $ is contractive, i.e.  $ \tau \| A \|_{\rho, \alpha} \leq 1 $

We ask for existence of solutions  $ u^n $ of the Galerkin equations (3.9) and for estimates  $ \|u - u^n\|_{\rho, \alpha} $. The following theorem, essentially taken from [53], Theorem 21.G, is a standard result for Galerkin methods in Hilbert spaces adapted to our case.

THEOREM 3.2. Let  $ A : D(A) \subset H_{\rho,\alpha} \to H_{\rho,\alpha} $ be a linear operator. For the following cases the problem (3.8) has a unique solution in  $ H_{\rho,\alpha} $ and the Galerkin method converges, i.e.  $ \|u^n - u\| \to 0 $ for  $ n \to \infty $.