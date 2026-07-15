### 3.3 Weight Function Fitting

In order to minimize the computational effort of the discrete Galerkin method, a good choice of the parameters  $ \rho $ and  $ \alpha $ is crucial. In this work, we choose an heuristic approach which is an extension of the moving weight function concept suggested in [19]. After each step, an actual approximation  $ u^n \in H_{\rho,\alpha} $ is transformed to  $ \bar{u}^n \in H_{\bar{\rho},\bar{\alpha}} $ (using the formulas derived in Section 2.2), where  $ \bar{n} < n $ is expected.

The main idea is the fitting of the first moments of  $ u^n \in H_{\rho,\alpha} $ to those of the weight function  $ \Psi_{\bar{\rho},\bar{\alpha}} $, a procedure which is possible by Corollary 1.4. Due to the normalization of the family  $ \Psi_{\rho,\alpha} $ this leads to an implicit definition of the parameters  $ \bar{\rho}, \bar{\alpha} $ by

 $$ \begin{array}{r c l}{\frac{\mu_{1}[u]}{\mu_{0}[u}}}&{\stackrel{!}{=}}&{\mu_{1}[\Psi_{\bar{\rho},\bar{\alpha}}]=\frac{1+\bar{\alpha}\bar{\rho}}{1-\bar{\rho}},}\\ {\frac{\mu_{2}[u]}{\mu_{0}[u}}}&{\stackrel{!}{=}}&{\mu_{2}[\Psi_{\bar{\rho},\bar{\alpha}}]=\frac{\bar{\alpha}^{2}\bar{\rho}^{2}+3\bar{\alpha}\bar{\rho}+\bar{\rho}+1}{(1-\bar{\rho})^{2}}.}\\ \end{array} $$ 

From (3.29) it follows, that  $ (\mu_k = \mu_k[u]) $:

 $$ \begin{array}{r c l}{\bar{\rho}(u)=\bar{\rho}}&{=}&{\frac{\mu_{0}\mu_{2}-\mu_{1}^{2}-\mu_{1}\mu_{0}+\mu_{0}^{2}}{\mu_{0}\mu_{2}-\mu_{1}^{2}},}\\ {\bar{\alpha}(u)=\bar{\alpha}}&{=}&{\frac{2\mu_{1}^{2}-\mu_{1}\mu_{0}-\mu_{2}\mu_{0}}{\mu_{0}\mu_{2}-\mu_{1}^{2}-\mu_{1}\mu_{0}+\mu_{0}^{2}}}\\ \end{array} $$ 

The requirements 0 <  $ \bar{\rho} $ < 1 and  $ \bar{\alpha} $ > -1 are fulfilled, whenever the denominators of the expressions in (3.30) are positive. Whenever only the parameter  $ \rho $ has to be adapted (i.e.  $ \alpha = 0 $), (3.29) leads to (consistent with [19], (3.15))

 $$ \bar{\rho}(u)=1-\frac{\mu_{0}[u]}{\mu_{1}[u]}\;. $$ 

In order to compute the moments  $ \mu_0[u] $,  $ \mu_1[u] $,  $ \mu_2[u] $ for  $ u \in H_{\rho,\alpha} $ given in the basis expansion, we use the fact, that the monomials  $ s^k $ can be represented in terms of the polynomials  $ l_k(\rho, \alpha) $ by

 $$ s^{k}=\sum_{m=0}^{k}b_{k m}\;l_{m}(s)\;,\;k=0,1,\cdots, $$ 

with coefficients  $ b_{km} = b_{km}(\rho, \alpha) $,  $ b_{kk} \neq 0 $. Then  $ \mu_k[\Psi_{\rho, \alpha}] = b_{k0} $ and insertion of  $ u $ into the definition of the moments yields

 $$ \mu_{k}[u]=\sum_{m=0}^{k}b_{k m}a_{m}\gamma_{m}^{\rho,\alpha}~. $$ 