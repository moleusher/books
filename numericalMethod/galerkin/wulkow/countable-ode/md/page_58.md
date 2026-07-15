LEMMA 4.2. (i) Assume that the explicit Euler scheme (time step  $ \tau $) is applied to a (nonlinear) problem with operator f having a Lipschitz constant M. For  $ \tau M \leq 1 $ we obtain the estimate

 $$ \left\|\pi\Delta\right\|\leq\left\|\Delta\right\|, $$ 

for the propagation of a previous error  $ \Delta $, i.e.  $ \Delta $ is not propagated.

(ii) For the implicit Euler discretization applied to a linear problem with A generator of a  $ C_{0} $ - semi-group of contractions

 $$ \left\|\pi\right\|\leq1. $$ 

holds.

Proof. (i) Let  $ u^{0} = u(t) $,  $ u^{1} = u_{\tau}(t + \tau) $. If  $ u^{0} $ is perturbed by an error  $ \Delta $, the explicit discretization yields

 $$ u^{1}+\pi\Delta=u^{0}+\tau f(u^{0}+\Delta)\;. $$ 

As  $ u^{0} - u^{1} = -\tau f(u^{0}) $ this leads to

 $$ \left\|\pi\Delta\right\|=\tau\left\|f(u^{0}+\Delta)-f(u^{0})\right\|\leq\tau M\|\Delta\|\leq\|\Delta\|. $$ 

(ii) By a similar procedure as in (i) we obtain for the implicit case

 $$ \pi=(I-\tau A)^{-1}=\frac{1}{\tau}R\left(\frac{1}{\tau};A\right) $$ 

and the Hille-Yosida theorem (Theorem 1.11) gives the assertion.

Now assume that there is a reliable error estimation for approximation of the sub-problems of an Euler step. According to (4.17) and (4.18), (4.19) we get

 $$ ||\Delta_{j}||_{\rho,\alpha}\leq j\epsilon\;, $$ 

 $ \varepsilon $ the tolerance per step. Using (4.16) this results in the condition

 $$ \epsilon:=\frac{1}{j}\alpha_{j}^{k}\mathrm{T O L} $$ 

as accuracy of the approximation of Euler steps leading to  $ U_{j_1} $ for an extrapolation table up to row  $ k $. This is BORNEMANN's fundamental connection between the time–control mechanism (extrapolation table) and the space discretization. The coefficients  $ \alpha_j^k $ are shown in Table 4.1 for  $ \mathcal{F} = \{1, 2, 3, \ldots\} $, the harmonic sequence, optimized in [8] with respect to an amount of work assumed to be  $ n \approx \sqrt{\varepsilon} $,  $ n $ the truncation index in the discrete Galerkin method. This assumption, though not verified theoretically, turned out to be the best empirical setting over all examples.