The family of sequence spaces  $ H_{\rho} $ is an extension of the family  $ H_{t} $ in Example 1.2. It is easily seen, that the solution of (1.13) is given by

 $$ u_{s}(t)=(t(1-\rho)+\rho)^{s-1}\left(1-\rho\right). $$ 

We can also show, that  $ u(t) \in H_{\bar{\rho}} $ only for  $ (t(1-\rho)+\rho)^2 < \bar{\rho} < 1 $ and  $ t < 1 $. So for the initial value (1.15) we only have a solution of (1.13) in  $ H_{\bar{\rho}} $ if

 $$ t<\frac{\sqrt{\bar{\rho}}-\rho}{1-\rho}\;. $$ 

A numerical consequence of this effect has been observed in [18], p. 296, where a CODE with an extended convolution operator is treated. There it is pointed out, that on the one hand an efficient Galerkin method for such problems can be realized in the spaces  $ H_{\rho} $, on the other hand the numerical approximations are breaking down for fixed  $ \bar{\rho} $ and increasing t. We will explain in Section 1.3, that the operator  $ A_{C} $ is not Lipschitz continuous as an operator on  $ H_{\rho} $ for fixed  $ \rho $, but as an operator on the scale  $ H_{\rho} $,  $ 0 < \rho < 1 $.

Computational approach: Discrete Galerkin method. The preceding examples give a first impression of the characteristics of CODE's. Now we turn to the numerical treatment of such problems and give a brief summary of the discrete Galerkin method introduced in [18]. The details will become evident in Chapter 2 and Chapter 3.

We assume for the solution  $ u(t) $ of a CODE, that (compare Example 1.3)

 $$ u(t)\in H_{\rho}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid\|u\|_{\rho}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}\Psi_{\rho}(s)^{-1}<\infty\right\} $$ 

where  $ \Psi_{\rho}(s) $ is a positive weight function with a (possibly time-dependent) real parameter  $ \rho $. On certain conditions on the weight function  $ \Psi_{\rho} $,  $ H_{\rho} $ is a separable Hilbert space equipped with the scalar product

 $$ (u,v)_{\rho}:=\sum_{s=1}^{\infty}u(s)v(s)\Psi_{\rho}^{-1}(s)\;. $$ 

The orthogonal basis  $ \{\psi_{j}(\rho)\}_{j} $ of  $ H_{\rho} $ can be written as

 $$ \psi_{j}(s;\rho)=\Psi_{\rho}(s)\;l_{j}(s;\rho)\;,\;j=0,\;1,\;\dots,\;s\in\mathbb{N}\;, $$ 

with the $\{l_j(s;\rho)\}_{j=0,1,\ldots}$ a set of polynomials of a discrete variable $s$. These polynomials are associated with $\Psi_\rho(s)$ by the orthogonality relation

 $$ \left(\psi_{j}(\rho),\psi_{k}(\rho)\right)_{\rho}=\sum_{s=1}^{\infty}l_{j}(s;\rho)l_{k}(s;\rho)\Psi_{\rho}(s)=\gamma_{j}^{\rho}\delta_{j k},\gamma_{j}^{\rho}>0, $$ 