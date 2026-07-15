The coefficients  $ b_{km} $ can be computed here to be

 $$ b_{10}=\nu_{1}(\rho,\alpha),b_{11}=-\frac{1}{1-\rho} $$ 

and

 $$ b_{20}=\nu_{2}(\rho,\alpha),b_{21}=-\frac{2\alpha\rho+\rho+3}{(1-\rho)^{2}},b_{22}=\frac{2}{(1-\rho)^{2}}. $$ 

In general, the condition (3.22) has a nice characterization for weight functions  $ \Psi $ with p parameters and associated orthogonal polynomials. Assume that the statistical moments  $ \nu_k $ of  $ \Psi $ are known and  $ \nu_0 = \gamma_0 = 1 $. By (3.26) the condition (3.22) is equivalent to

 $$ \begin{array}{r c l}{\mu_{0}[u]}&{=}&{a_{0}\;,}\\ {\displaystyle\sum_{m=0}^{k}b_{k m}a_{m}\gamma_{m}}&{=}&{b_{k0}a_{0}\;,\;1\leq k\leq p\;.}\\ \end{array} $$ 

From (3.27) we obtain by induction

 $$ a_{1}=a_{2}=\cdots=a_{p}=0. $$ 

This property has been used in [18] for p = 1 to derive a differential equation for the parameter of the Galerkin method.

Remark. In order to ensure a reliable computation of $\bar{\rho}$, $\bar{\alpha}$ for (possibly) perturbed coefficients $\tilde{a}_{0}$, $\tilde{a}_{1}$, $\tilde{a}_{2}$, additionally to condition (3.20) the following relations should be fulfilled

 $$ \begin{array}{r l r}{|\bar{\rho}(\tilde{u}^{n})-\bar{\rho}(u^{n})|}&{{}\leq}&{\varepsilon_{\bar{\rho}}}\\ {|\bar{\alpha}(\tilde{u}^{n})-\bar{\alpha}(u^{n})|}&{{}\leq}&{\varepsilon_{\bar{\alpha}}\;,}\end{array} $$ 

with  $ \tilde{u}^{n} $ from (3.1) and appropriate (relative) accuracies  $ \varepsilon_{\tilde{p}}, \varepsilon_{\tilde{\alpha}} $. Obviously the left-hand sides in (3.29) are replaced by estimates in the actual implementation.

Connection with Charlier polynomials. The weight function fitting condition leads us in a natural way to the Charlier polynomials associated to the Poisson distribution.

Let

 $$ u(s;\lambda)=e^{-\lambda}\frac{\lambda^{s-1}}{(s-1)!},s\in\mathbb{N}, $$ 

a Poisson distribution. The moments  $ \mu_{0}, \mu_{1}, \mu_{2} $ of u are

 $$ \mu_{0}=1,\mu_{1}=\lambda+1,\mu_{2}=\lambda^{2}+3\lambda+1. $$ 