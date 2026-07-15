The Frechét derivative  $ DF(\varphi)(u) $ of F with respect to u at  $ \varphi $ (required for a semi-implicit Euler discretization) can be computed pointwise (the time dependency is omitted) by

 $$ D F(\varphi)(u)(s)=\sum_{r=1}^{s-1}k_{r,s-r}\varphi_{s-r}u_{r}-\varphi_{s}\sum_{r=1}^{\infty}k_{s r}u_{r}-u_{s}\sum_{r=1}^{\infty}k_{s r}\varphi_{r}\;. $$ 

The treatment of a coagulation process with general rate coefficients  $ k_{sr} $ is a very difficult task, which has actually not been solved up to now. In [39] a discrete Fourier transform is applied, however, apart from the fact, that it turned out to be very time-consuming, a product separation of the  $ k_{rs} $ with respect to r and s has been assumed. This is not met in many examples – see e.g. the realistic coefficients

 $$ k_{r,s}:=k_{p}\cdot\left(\frac{1}{r}+\frac{1}{s}\right)^{1/2}\left(r^{1/3}+s^{1/3}\right)^{2}\;,\;k_{p}\;\mathrm{c o n s t a n t}, $$ 

given by FRENKLACH [21].

First, the behavior of a semi-implicit Euler discretization will be demonstrated for the case  $ k_{rs} = k_p $,  $ k_p $ constant. We assume  $ u $,  $ \varphi \in H_{\rho-\varepsilon,0} $ with expansions

 $$ u_{s}=\sum_{k=0}^{\infty}a_{k}\psi(s;\rho,0),\varphi_{s}=\sum_{k=0}^{\infty}b_{k}\psi_{k}(s;\rho,0), $$ 

in  $ H_{\rho,0} $. For  $ \alpha = 0 $ we can use the convolution formula (2.34). Then by manipulations essentially described in [18] the preprocessing results in

 $$ \frac{1}{\gamma_{j}^{\rho}}\left(D F(\varphi)(u),\psi_{j}\right)_{\rho}=\left\{\begin{array}{c c}-k_{p}a_{0}b_{0},&j=0,\\ k_{p}\displaystyle\sum_{k=1}^{j-1}a_{k}b_{j-k}-\frac{k_{p}}{\rho}\displaystyle\sum_{k=0}^{j-1}a_{k}b_{j-1-k},&j\neq0.\end{array}\right. $$ 

We end up with the following Galerkin equations for the semi-implicit Euler discretization  $ (a = (a_0, a_1, \ldots), b = (b_0, b_1, \ldots) $

 $$ \begin{array}{r c l}{(I-\tau k_{p}C)\;a_{\Delta}}&{=}&{\tau k_{p}\;f}\\ {a}&{=}&{b+a_{\Delta}\;,}\\ \end{array} $$ 

where the Matrix  $ C = (c_{jk}) $ is defined by

 $$ \begin{array}{l l}{c_{00}=-b_{0}\;,}&{c_{j k}=0\;,j\leq k\;,}\\ {c_{j0}=-b_{j-1}/\rho\;,j\geq1\;,}&{c_{j k}=b_{j-k}-b_{j-k-1}/\rho\;\mathrm{o t h e r w i s e}\;.}\\ \end{array} $$ 