subject of further work.

(ii) The proof of Theorem 1.9 can be changed to get the result for bounded (linear) operators respectively Lipschitz continuous nonlinear operators. Then we can use a standard fixed point iteration in  $ H_{\rho,\alpha} $.

(iii) The technique which has been used to prove uniqueness could not be extended by the author to get a stability result of the form

 $$ \begin{array}{r}{\|u(t)-v(t)\|_{\rho}\leq C\phi_{\varepsilon}(M t)\|u(0)-v(0)\|_{\rho-\varepsilon},\phi_{\varepsilon}\mathrm{~b o u n d e d},}\end{array} $$ 

because the constants in the estimates become unbounded. Such a result might be used for a proof of the convergence of explicit, consistent discretization schemes for operators considered in Theorem 1.9, but we will explain in Section 1.4, why this is not expected.

Example 1.7. To show that Theorem 1.9 is indeed a reasonable tool in our context, we consider the convolution operator  $ A_{C} $ (1.14) again. We have to estimate

 $$ ||A_{C}(u)-A_{C}(v)||_{\rho}\mathrm{~f o r~}u,v\in H_{\rho-\varepsilon}\;. $$ 

Denoting by  $ DA_{C}(u) $ the Frechét - derivative of  $ A_{C}(u) $ with respect to u, we can write

 $$ \left(D A_{C}(u)v\right)(s)=\sum_{r=1}^{s-1}u(s-r)v(r),v\in H_{\rho-\varepsilon},u\in H_{\rho}, $$ 

and start with

 $$ \begin{array}{r c l}{\|D A_{G}(u)v\|_{\rho}^{2}}&{=}&{\displaystyle\sum_{s=1}^{\infty}\Psi_{\rho}(s)^{-1}\displaystyle\sum_{r=1}^{s-1}u(s-r)v(r)\displaystyle\sum_{k=1}^{s-1}u(s-k)v(k)}\\ {}&{=}&{\displaystyle\sum_{r=1}^{\infty}v(r)\displaystyle\sum_{k=1}^{\infty}v(k)\displaystyle\sum_{s=\operatorname*{m a x}(r,k)+1}^{\infty}\Psi_{\rho}(s)^{-1}u(s-r)u(s-k)}\\ {}&{\leq}&{\displaystyle\sum_{r=1}^{\infty}v(r)\displaystyle\sum_{k=1}^{r}v(k)\displaystyle\sum_{s=1}^{\infty}\Psi_{\rho}(s+r)^{-1}u(s)u(s+r-k)}\\ {}&{}&{+\displaystyle\sum_{k=1}^{\infty}v(k)\displaystyle\sum_{r=1}^{k-1}v(r)\displaystyle\sum_{s=1}^{\infty}\Psi_{\rho}(s+k)^{-1}u(s)u(s+k-r)}\\ \end{array} $$ 

after reordering of the summations. As both terms are of the same structure, we can change the indices k and r in the second term. The inner sum can be expressed by means of the Shift operator  $ S_{+} $, after adding

 $$ |v(k)|\Psi_{\rho}(s+r)^{-1}u_{s}^{2}>0 $$ 