In general we obtain a perturbed approximation (3.8). The error  $ \|\tilde{u}^{n,l} - u\|_{\rho,\alpha} $ can be written in terms of the projection error and a so-called truncation error.

 $$ \begin{array}{r c l l}{\|\tilde{u}^{n,l}-u\|_{\rho,\alpha}^{2}}&{=}&{\|u-\mathcal{P}_{n}^{\rho,\alpha}u\|_{\rho,\alpha}^{2}}&{+}&{\|\tilde{u}^{n,l}-u^{n}\|_{\rho,\alpha}^{2}}\\ {}&{=}&{\displaystyle\sum_{k=n+1}^{\infty}a_{k}^{2}\hat{\gamma}_{k}^{\rho,\alpha}}&{\overset{,}{+}}&{\displaystyle\sum_{k=0}^{n}\left(\tilde{a}_{k}^{l}-a_{k}\right)^{2}\hat{\gamma}_{k}^{\rho,\alpha}.}\\ \end{array} $$ 

Let now an algorithm produce successive approximations  $ \tilde{a}_{k}^{\prime} $ of  $ x_{k} - e.g $ by increasing the truncation index n or by Gauss summations in (3.10) with an increasing number of nodes. Assuming that

 $$ \tilde{a}_{k}^{l}\;\to\;a_{k}\;\mathrm{~f o r~}\;l\to\infty\;,\;k\;\mathrm{~f i x e d}\;, $$ 

the following error estimation can be applied ( $ \varepsilon_{P,n,l} = \varepsilon_{n} $ in Lemma 3.4):

 $$ \varepsilon_{n,l}^{2}:=\varepsilon_{T,n,l}^{2}+\varepsilon_{P,n,l}^{2}:=\sum_{k=0}^{n}\left(\tilde{a}_{k}^{l}-\tilde{a}_{k}^{l+1}\right)^{2}\gamma_{k}^{\rho,\alpha}+\left(\tilde{a}_{n+1}^{l+1}\right)^{2}\gamma_{n+1}^{\rho,\alpha}\;. $$ 

We are only interested in a truncation error (respectively its estimate)  $ \varepsilon_{T,n,l} $ being just a little smaller than the projection error  $ \varepsilon_{P,n,l} $ for that the estimate of the projection error is reliable. Thus we require l to be chosen such that

 $$ \left|\tilde{u}^{n+1,l}-u^{n+1}\right|_{\rho,\alpha}<\kappa\left|\tilde{u}^{n,l}-u\right|_{\rho,\alpha} $$ 

with some safety factor  $ 0 < \kappa < 1 $ (see also [17], (1.26)). In actual computations, the terms on both sides are replaced by the estimates suggested in (3.17),  $ \kappa $ is set to 1/4.

The Effect of Numerical Summation. Finally we examine, whether a numerical summation algorithm as presented in Section 2.4 can be applied to construct the Galerkin equations. The scalar products in (3.10) are replaced by approximations  $ (u, v)_{\rho,\alpha}' $, where the index  $ l $ denotes now, that

 $$ (u,\;v)_{\rho,\alpha}^{l}=(u,\;v)_{\rho,\alpha}\;\mathrm{~f o r~}\;\frac{u\;v}{\Psi_{\rho,\alpha}}\in H_{\rho,\alpha}^{l}\;. $$ 

The question is, how l must be chosen for not perturbing the Galerkin method essentially. As the discussion of the general problem requires additional assumptions on the operator A again, in this paper we treat only the case of a projection

 $$ u^{n,l}=\mathcal{P}_{n}^{\rho,\alpha}u~,\;\mathcal{P}_{n}^{\rho,\alpha}\;\mathrm{n u m e r i c a l l y~e v a l u t a t e d}, $$ 

as an example and ask how  $ u^{n} $ is perturbed. We use techniques described in the textbook by CIARLET [11] for the case of finite elements.