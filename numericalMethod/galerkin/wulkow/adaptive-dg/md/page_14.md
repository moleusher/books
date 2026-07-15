with  $ u^1 $ an approximation of  $ u(t+\tau) $ and  $ A $ an approximate Frechet derivative of  $ f $ at some not further specified argument  $ u $, which is computationally available. Formally, this approach involves solving an ODE in Hilbert space so that well-known devices like stepsize control can be exploited. Such control devices are based on higher order estimates of the error of the computed solution. In the present context, a reliable estimate of the approximation error is the second order correction  $ \eta^1 $ defined by

 $$ (I-\tau A)\eta^{1}=-\frac{1}{2}\tau^{2}A f(u(t))\quad. $$ 

Note that  $ (4.9) $ implies

 $$ u^{\prime\prime}\approx A f. $$ 

Of course, this second order correction  $ \eta^{1} $ can simultaneously be used to improve the approximation  $ u^{1} $ to yield

 $$ u(t+\tau)\approx u^{2}=u^{1}+\eta^{1}. $$ 

An estimate  $ \bar{\tau} $ for a reasonable local step size will then be

 $$ \bar{\tau}=\tau\sqrt{\frac{\mathrm{e p s}}{||\eta^{1}||}}\quad. $$ 

wherein eps represents the user prescribed accuracy. At this point, the adaptation of the truncation index n enters the computational scheme, so that a time-dependent truncation index  $ n(t) $ can be realized without further complication. Crucial, however, for the actual implementation of this algorithmic approach is that the above corrections are not computed from differencing (which would involve possible cancellation of leading digits) but from division by large numbers, which is meant by the phrase “multiplicative error correction”. This feature is indeed realized in both (4.10) and (4.12).

The adaptive Rothe variant of the discrete Galerkin method in combination with the rather general weight function  $ \Psi_{\rho,\alpha} $ has been implemented by Wulkow in the C++ program CODEX. This program has been applied successfully to an impressive number of macromolecular reaction systems in different fields of science and industrial engineering [16, 18, 19].