Discretization scheme for nonlinear problems. For the nonlinear case (see Example 4.3)

 $$ u^{\prime}(t)=f(u(t)),\;u(0)\;\mathrm{g i v e n}, $$ 

the semi-implicit Euler scheme [16] is used as basic discretization:

 $$ \begin{array}{r c l}{(I-\tau\;A)\;\Delta u^{1}}&{=}&{\tau\;f(\varphi)\;,}\\ {u^{1}}&{=}&{\varphi+\Delta u^{1}\;,}\\ \end{array} $$ 

with A now the Frechét derivative $f_{u}(\varphi)$ of the right-hand side $f(u)$. Obviously the implicit Euler discretization is identical with the semi-implicit Euler scheme in the linear case. A correction formula, which fulfills the two requirements (direct computation of the error, only one type of stationary problem) is given by:

 $$ \begin{array}{r c l}{\eta^{1}}&{=}&{-\frac{1}{2}\tau^{2}\left(I-\tau A\right)^{-1}A f(\varphi)\;,}\\ {u^{2}}&{=}&{u^{1}+\eta^{1}\;.}\\ \end{array} $$ 

As will be demonstrated in Example 4.3, the scheme (3.6) works very well for nonlinear countable systems. A theory comparable to Theorem 3.1 does not yet exist.

The numerical implementation of the above formulas requires an adaptive Galerkin method for the solution of the linear systems in (3.3) and (3.6). The correction terms  $ \eta^{1} $ are then computed with the same accuracy using the results of the Euler step. When a time step  $ \tau $ has been performed, a new step size  $ \bar{\tau} $ can be computed by

 $$ \bar{\tau}=\tau\sqrt{\frac{\mathsf{T O L}}{||\eta^{1}||}}. $$ 

### 3.2 GALERKIN APPROXIMATIONS IN  $ H_{\rho,\alpha} $

Before we discuss the details of the Galerkin method, we restrict to the following types of linear operators:

(i)  $ \tau A $ is contractive, i.e.  $ \tau \| A \|_{\rho, \alpha} < 1 $.

(ii) A is the generator of a  $ C_{0} $ - semigroup of contractions.

Some of the considerations below can be extended by assuming e.g. a Vellipticity of A (in Theorem 3.3 and Theorem 3.7), but such an assumption does not really fit to CODE's and a general classification of the appearing operators is still missing. Consequently the following results have to be understand as exemplary.