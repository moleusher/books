in terms of higher differences of $u$ (analogue to higher derivatives in the continuous case), which should be a measure of the smoothness of $u$ in $H_{\rho,\alpha}$. In $H^{\rho,\alpha}$, which is spanned by polynomials, we could use the standard forward difference operator, since for $p$ a polynomial of degree $m$

 $$ \Delta^{m+1}p(s)=0\;. $$ 

However, in  $ H_{\rho,\alpha} $ the basis consists of polynomials multiplied by the weight function  $ \Psi_{\rho,\alpha}(s) $, and it is easily seen that even

 $$ \Delta^{m}\Psi_{\rho,\alpha}(s)=\Psi_{\rho,\alpha}(s)\left[\frac{\rho(s+\alpha)}{s}-1\right]^{m}\neq0\mathrm{f o r}m\geq1. $$ 

This consideration together with (2.23) inspires the following definition of a modified difference operator.

DEFINITION 2.11. Let for  $ u \in H_{\rho,\alpha} $ the weighted difference operator  $ \Delta_\alpha $ be defined by

 $$ \Delta_{\alpha}u(s):=\Psi_{\rho,\alpha+1}(s)\Delta\left(\frac{u(s)}{\Psi_{\rho,\alpha}}\right),\Delta_{\alpha}u\in H_{\rho,\alpha+1}, $$ 

by means of the forward difference operator  $ \Delta $. Higher weighted differences are inductively given by

 $$ \Delta_{\alpha}^{m}u(s):=\Delta_{\alpha+m-1}\Delta_{\alpha+m-2}\ldots\Delta_{\alpha}u(s)~. $$ 

The re-multiplication with  $ \Psi_{\rho,\alpha+1} $ instead of  $ \Psi_{\rho,\alpha} $ has been done for analytical convenience as we will see below. From Lemma 1.2 we know, that if  $ u \in H_{\rho-\varepsilon,\alpha} $, the weighted difference is an element of  $ H_{\rho,\alpha} $.

COROLLARY 2.12. For  $ u \in H_{\rho,\alpha} $ with a representation (2.35) the m-th weighted higher difference can be written as

 $$ \Delta_{\alpha}^{m}u(s)=\Psi_{\rho,\alpha+m}(s)\sum_{k=0}^{\infty}a_{k+m}\left(\rho-1\right)^{m}l_{k}(s;\rho,\alpha+m)\;. $$ 

Proof. Again we use the difference relation (2.23)

 $$ \Delta l_{k}(s;\rho,\alpha)=(\rho-1)\;l_{k-1}(s;\rho,\alpha+1)\;. $$ 

Inserting (2.35) we get

 $$ \begin{array}{r c l}{\Delta_{\alpha}u(s)}&{=}&{\Psi_{\rho,\alpha+1}\displaystyle\sum_{k=0}^{\infty}a_{k}\Delta l_{k}(s;\rho,\alpha)}\\ {}&{=}&{\Psi_{\rho,\alpha+1}\displaystyle\sum_{k=0}^{\infty}a_{k+1}\left(\rho-1\right)l_{k}(s;\rho,\alpha+1),}\\ \end{array} $$ 