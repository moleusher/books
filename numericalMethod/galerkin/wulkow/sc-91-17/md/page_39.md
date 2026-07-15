 $ (u_{s}(t) $ defined as in Example 4.2 $

 $$ u_{s}^{\prime}(t)=F(u(t))(s):=\frac{1}{2}\sum_{r=1}^{s-1}k_{r,s-r}u_{r}(t)u_{s-r}(t)-u_{s}(t)\sum_{r=1}^{\infty}k_{s r}u_{r}(t)\;. $$ 

Concerning the  $ k_{sr} $, we refer to a model by FRENKLACH [21], where the following reaction coefficients are suggested:

 $$ k_{r s}:=k_{p}\;\left(\frac{1}{r}+\frac{1}{s}\right)^{1/2}\;\left(r^{1/3}+s^{1/3}\right)^{2}\;,\;k_{p}\;\mathrm{c o n s t a n t}. $$ 

Note, that the algorithm CODEX works for arbitrary coefficients  $ k_{sr} $ (as far as the  $ H_{\rho,\alpha} $ - theory is valid).

The problem (4.8) has been attacked by different authors. In [21], a special approximation of the moments is tried just for the coefficients (4.9). In [32], a discrete Fourier transform is applied, but this requires a certain separation of r and s in the expression for the  $ k_{rs} $. A continuous modeling as in [22] leads to theoretical difficulties.

In order to obtain a reference solution of (4.8), we perform again a direct time integration of a truncated system as an ODE (replace  $ \infty $ by  $ s_{\max} $ in (4.8),  $ s_{\max} $ large enough).

Such an integration up to an interesting  $ t_{end} $ took more than 14000 sec. (CPU) on a Cray-YMP. This value would be even larger, if the truncation index  $ s_{\max} $ was not known from the simulations with CODEX a priori! A realistic number of size-classes is given in [21] to be about  $ s_{\max} = 10000 $, thus we used  $ k_p = 1 $ and  $ t_{end} $ large enough to obtain comparable results. By the way we note, that the whole simulation with CODEX is independent of the parameter  $ s_{\max} $.

The application of the semi-implicit Euler scheme (3.5) in CODEX requires the Frechét derivative  $ DF(\varphi)(u) $ of F with respect to u at  $ \varphi $, which can be computed pointwise (the time dependency is omitted) by

 $$ D F(\varphi)(u)(s)=\sum_{r=1}^{s-1}k_{r,s-r}\varphi_{s-r}u_{r}-\varphi_{s}\sum_{r=1}^{\infty}k_{s r}u_{r}-u_{s}\sum_{r=1}^{\infty}k_{s r}\varphi_{r}\;. $$ 

As in Example 4.2, the entries of the Galerkin equations are computed by a double Gauss summation with two infinite sums of the structure described in Section 2.4. This can be done after an appropriate re-ordering of the appearing sums.

It turns out, that the solution  $ u_{s}(t) $ (number distribution) at  $ t = 100 $ sec. has a narrow peak for small chain lengths ( $ s < 100 $). This peak is obviously hard to approximate (i.e. time consuming) by a polynomial expansion as used herein