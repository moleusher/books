Example 3.1. Let

 $$ u_{s}=\frac{s}{r}\bar{\rho}^{s}\quad,\quad\bar{\rho}:=e^{-1/r}\quad,\quad s\geq1\quad,\quad r\quad given\ . $$ 

This is a realistic setting of initial values in some applications. It is easily seen that

 $$ u=\frac{\bar{\rho}}{(1-\bar{\rho})^{2}r}\Psi_{\bar{\rho},1}\in H_{\bar{\rho},1}, $$ 

but it will turn out in Example 5.3, that an approximation in  $ H_{\bar{\rho},1} $ is not feasible in that context. Instead of this, u can be expanded for  $ \rho = 2\bar{\rho}/(1+\bar{\rho}) $ and  $ \alpha = 0 $ in the respective space with coefficients

 $$ a_{k}=\frac{\bar{\rho}}{(1-\bar{\rho})^{2}r}2^{-k}(1-k),k\geq0. $$ 

This can be seen from

 $$ s=\frac{1}{\bar{\rho}-1}\left(l_{1}(s;\bar{\rho},0)-l_{0}(s;\rho,\alpha)\right) $$ 

and the transformation formula (2.24) in Lemma 2.2.

Whenever there are no analytical properties to obtain the exact coefficients  $ a_k $, we have to evaluate the scalar products in (2.36) numerically. This will be done by the summation algorithm described in Chapter 6 and leads to approximations  $ \tilde{a}_k $ of  $ a_k $ and hence to an expansion (3.1).

Next we consider projections of Au, A a linear operator. We will try to apply properties of the  $ H_{\rho,\alpha} $ - basis as far as possible again and propose a classification of linear CODE's formulated in terms of the projections  $ \mathcal{P}_{n}^{\rho,\alpha} $:

DEFINITION 3.1.

(i) A is called invariant, if

 $$ \mathcal{P}_{n}^{\rho,\alpha}A=\mathcal{P}_{n}^{\rho,\alpha}A\mathcal{P}_{n}^{\rho,\alpha}\quad{f o r~a l l}\quad n\in\mathbb{N}. $$ 

(ii) A is called m-invariant, if there is an m > 0, such that

 $$ \mathcal{P}_{n}^{\rho,\alpha}A=\mathcal{P}_{n}^{\rho,\alpha}A\mathcal{P}_{n+m}^{\rho,\alpha}\quad{f o r~a l l}\quad n\in\mathbb{N}. $$ 

(iii) otherwise A is called general.