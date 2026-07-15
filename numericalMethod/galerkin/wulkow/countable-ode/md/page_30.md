## 2 MODIFIED DISCRETE LAGUERRE POLYNOMIALS

The experiences made with the discrete Galerkin method in [18], [9], [52] and the considerations in Chapter 1 admit the expectation, that the weight function  $ \Psi_{\rho,\alpha} $ will be a good basis for the Galerkin approximation of realistic problems. For an illustration we discuss the behavior of  $ \Psi_{\rho,\alpha} $ for different values of  $ \rho $ and  $ \alpha $.

For  $ \alpha = 0 $ the weight function is reduced to the geometric distribution, which plays an important role in polymer chemistry under the name Schulz-Flory distribution [45], [9]. For further discussions we need the first statistical moments of  $ \Psi_{\rho,\alpha} $. The constant  $ C^{\rho,\alpha} $ from (1.27) is chosen such that

 $$ \nu_{0}(\rho,\alpha)=\nu_{0}:=\mu_{0}[\Psi_{\rho,\alpha}]=1,0<\rho<1,\alpha>-1. $$ 

Using the definition of the binomial coefficient, we can derive that

 $$ \begin{array}{r c l}{\nu_{1}(\rho,\alpha):=\mu_{1}[\Psi_{\rho,\alpha}]}&{=}&{1+\displaystyle\sum_{s=2}^{\infty}(s-1)\Psi_{\rho,\alpha}=}\\ {}&{=}&{1+\rho\displaystyle\sum_{s=1}^{\infty}(s+\alpha)\Psi_{\rho,\alpha}=1+\rho\alpha+\rho\nu_{1}(\rho,\alpha)}\\ \end{array} $$ 

and therefore

 $$ \nu_{1}(\rho,\alpha)=\frac{1+\alpha\rho}{1-\rho}\;. $$ 

By a similar procedure we get

 $$ \nu_{2}(\rho,\alpha):=\mu_{2}[\Psi_{\rho,\alpha}]=\frac{\alpha^{2}\rho^{2}+3\alpha\rho+\rho+1}{(1-\rho)^{2}}~. $$ 

The so-called dispersion coefficient d is defined by

 $$ d:=\frac{\mu_{0}\mu_{2}}{\mu_{1}^{2}} $$ 

and can give some hints about the weight function for special settings of  $ \rho $ and  $ \alpha $. For  $ \alpha \gg 1 $ d tends to 1, which means that  $ \Psi_{\rho,\alpha} $ becomes a very peaked distribution. In fact, if we set  $ \alpha = \lambda / \rho $,  $ \lambda $ the parameter of a Poisson distribution,  $ \Psi_{\rho,\lambda / \rho} $ converges pointwise to the Poisson distribution for  $ \rho \to 0 $. A motivation of such a parameter setting will be given at the end of Section 3.2. Therewith the two discrete Galerkin methods suggested in [18], based on the geometric distribution (discrete Laguerre polynomials) and the Poisson distribution (Charlier polynomials) are combined by the two-parameter family  $ \Psi_{\rho,\alpha} $. We note, that a Galerkin method based on the Poisson distribution itself