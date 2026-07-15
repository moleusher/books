subtle consideration. A comparison of the analytic results of (1.4) and (1.7) shows that the continuous model introduces significant errors for small degree s. In the polymer degradation model (1.9), a short examination demonstrates that

 $$ \lim_{t\to\infty}N_{s}(t)=\frac{1}{s}\delta(s)\;. $$ 

Hence, asymptotically a nasty singularity is introduced by this kind of continuous modeling.

In [14], GAJEWSKI and ZACHARIAS study the continuous analogue of the coagulation equation (1.7), which reads (dropping the convection term):

 $$ \begin{array}{r l}{\mathrm{a})}&{\frac{\partial}{\partial t}N(s;t)^{\prime\prime}=\quad\frac{1}{2}\displaystyle\int\limits_{r=0}^{s}k(r,s-r)N(r,t)N(s-r,t)d r}\\ &{\quad-N(s,t)\displaystyle\int\limits_{r=0}^{\infty}k(s,r)N(r,t)d r}\end{array} $$ 

 $$ \begin{array}{r l r}{b)}&{{}}&{N(s,0)}&{:=~N_{0}(s)}\end{array} $$ 

In order to solve this nonlinear partial integro-differential equation, these authors suggest a Galerkin method based, for example, on finite elements or on modified Laguerre polynomials  $ L_{k}^{\alpha} $. In the latter approach (see [15]), the distribution density  $ P(s, t) $ is approximated by

 $$ P^{(N)}(s,t):=\sigma^{\alpha}e^{-\sigma}\sum_{k=0}^{N}a_{k}(t)L_{k}^{\alpha}(\sigma) $$ 

with  $ \sigma $ defined by

 $$ \sigma:=\beta(t)s $$ 

for suitably chosen  $ \beta(t) $. For example, BAMFORD and TOMPA [1] suggest to use

 $$ \beta(t):=\frac{\mu_{0}(t)}{\mu_{1}(t)}\;. $$ 

The artificial nature of modeling the discrete length s by a continuous variable shows up in the depth of the convergence analysis in [14]: for s = 0, a singularity arises, which needs special regularization. Moreover, even though [14] analyse the approximation error introduced by the Galerkin method in detail, the beforehand introduced modeling error is overlooked. For these reasons, the continuous Galerkin approach seems to be not sufficiently reliable for real life scientific and engineering computations.