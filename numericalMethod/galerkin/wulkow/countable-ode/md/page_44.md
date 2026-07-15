## 3 Discrete Galerkin Method

Assume  $ \varphi \in H_{\rho,\alpha} $. It can be seen from (1.54), (1.55) that the realization of implicit or explicit Euler steps consists of three tasks:

(i) projections of the form  $ \mathcal{P}_{n}^{\rho,\alpha}\varphi $,  $ \mathcal{P}_{n}^{\rho,\alpha} $ from (2.39).

(ii) projections of the form  $ \mathcal{P}_{n}^{\rho,\alpha}A\varphi $, A bounded linear operator (explicit Euler step).

(iii) approximate solutions of the countable system of algebraic equations

 $$ (I-\tau A)u=\varphi~\mathrm{i n}~H_{\rho,\alpha}^{n}~\mathrm{(i m p l i c i t~o r~s e m i-i m p l i c i t~E u l e r~s t e p).} $$ 

As we are interested in Galerkin approximations in  $ H_{\rho,\alpha} $, we assume that  $ \varphi $,  $ A\varphi $ and the solution  $ u $ of the CAE in (iii) (all called  $ u $ from now on) have a basis expansion (2.35). The discrete Galerkin method yields perturbed approximations  $ \tilde{u}^n \in H_{\rho,\alpha}^n $ of  $ u $ of the form

 $$ \tilde{u}^{n}=\sum_{k=0}^{n}\tilde{a}_{k}\psi_{k}(\rho,\alpha)\;, $$ 

with a truncation index  $ n $ and coefficients  $ \tilde{a}_k $,  $ k = 0, 1, \ldots, n $, which may be the exact expansion coefficients  $ a_k $ or approximations of them. The error  $ \|\tilde{u}^n - u\|_{\rho,\alpha} $ of approximation (3.1) can be written in terms of the projection error  $ \|u^n - u\|_{\rho,\alpha} $ (compare (2.40)) and a so-called truncation error  $ \|\tilde{u}^n - u^n\|_{\rho,\alpha} $:

 $$ \begin{array}{r c l l}{\|\tilde{u}^{n}-u\|_{\rho,\alpha}^{2}}&{=}&{\|u^{n}-u\|_{\rho,\alpha}^{2}}&{+}&{\|\tilde{u}^{n}-u^{n}\|_{\rho,\alpha}^{2}}\\ {}&{=}&{\displaystyle\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}}&{+}&{\displaystyle\sum_{k=0}^{n}\left(\tilde{a}_{k}-a_{k}\right)^{2}\gamma_{k}^{\rho,\alpha}.}\\ \end{array} $$ 

An estimation of error (3.2) and a matching of projection error and truncation error are suggested at the end of the following section.

### 3.1 PROJECTIONS AND APPROXIMATE SOLUTIONS

The projection of an element  $ u \in H_{\rho,\alpha} $ to the subspace  $ H_{\rho,\alpha}^n $ can formally be written as

 $$ u^{n}(s)=\sum_{k=0}^{n}a_{k}\psi_{k}(s;\rho,\alpha)=\Psi_{\rho,\alpha}(s)\sum_{k=0}^{n}a_{k}l_{k}(s;\rho,\alpha)\;. $$ 

In general the expansion coefficients  $ a_{k} $ can formally be expressed by relation (2.36). Sometimes properties of the modified discrete Laguerre polynomials  $ l_{k}(\rho, \alpha) $ make an analytic calculation of the  $ a_{k} $ possible.