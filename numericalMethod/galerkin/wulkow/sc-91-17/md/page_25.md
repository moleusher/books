(i) The pure projection error

 $$ \bar{\varepsilon}_{n}=||u-\mathcal{P}_{n}^{\rho,\alpha}u||, $$ 

where u denotes the solution of  $ (3.7) $.

(ii) The error  $ \|u - \tilde{u}^n\| $, where  $ \tilde{u}^n $ is the solution of a Galerkin equation, which may not be self-closing.

(iii) The general error  $ \|u - \tilde{u}^{n,l}\| $, which includes all effects.

We will discuss later in this section, how the error is estimated in general and we will illustrate, that the error introduced by numerical summations can be controlled. First we examine the case, that the Galerkin equations are not perturbed.

The case of unperturbed Galerkin equations. We ask for existence of solutions  $ \tilde{u}^n $ of the Galerkin equations (3.9) and for estimates  $ \|u - \tilde{u}^n\|_{\rho,\alpha} $. The following theorem, essentially taken from [40], Theorem 21.G, is a standard result for Galerkin methods in Hilbert spaces – adapted to our case.

THEOREM 3.3. Let  $ A: D(A) \subset H_{\rho,\alpha} \to H_{\rho,\alpha} $ be a linear operator. For the following cases the problem (3.7) has a unique solution in  $ H_{\rho,\alpha} $ and the Galerkin method converges, i.e.  $ \|\tilde{u}^n - u\| \to 0 $ for  $ n \to \infty $.

(i)  $ \tau A $ is contractive. Then the estimate

 $$ \left|\left|u-\tilde{u}^{n}\right|\right|\leq\left(1-\tau\left\|A\right\|_{\rho,\alpha}\right)^{-1}\left\|u-\mathcal{P}_{n}^{\rho,\alpha}u\right\| $$ 

holds.

(ii) A is generator of a  $ C_{0} $ - semigroup of contractions and fulfills the invariance condition

 $$ \mathcal{P}_{n}^{\rho,\alpha}A=\mathcal{P}_{n}^{\rho,\alpha}A\mathcal{P}_{n}^{\rho,\alpha}\;,\;{~f o r~a l l~}\;n\in\mathbb{N}\;. $$ 

Then we have convergence for  $ \tau > 0 $ and for the Galerkin solution  $ \tilde{u}^{n} $ holds

 $$ \tilde{u}^{n}=\mathcal{P}_{n}^{\rho,\alpha}u. $$ 