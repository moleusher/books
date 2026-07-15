### 4. Analytic Preprocessing of Kinetic Equations

Application of the discrete Galerkin method as derived in Section 2 will lead to a system of ordinary differential equations for the associated generalized moments  $ \{a_{k}(t)\} $. This procedure is now exemplified for the two sets of orthogonal polynomials presented in Section 3. The mechanisms to be treated have already been introduced in Section 1.1. In actual computation, these mechanisms will only be part of a large system to be simulated. For the sake of clarity, however, the new approach is demonstrated only for a few isolated model problems. For real life applications, an automated preprocessor will be used, of course.

### 4.1 Preprocessing by Discrete Laguerre Polynomials

Starting point is the representation (2.7) with  $ \Psi $ from (3.2)

 $$ P_{s}(t):=(1-\rho)\rho^{s-1}\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s)\quad,\quad0<\rho<1\quad, $$ 

with  $ \{l_{k}\} $ the discrete Laguerre polynomials as introduced in Section 3.1.

Moving weight function. The time-dependent adaptation of  $ \rho $ according to (3.15) is recalled:

 $$ 1-\rho(t)=\frac{\mu_{0}(t)}{\mu_{1}(t)}\geq0 $$ 

which implies (2.30). Upon observing this time dependence in the representation (4.1), the total time derivation reads

 $$ \begin{array}{r c l}{P_{s}^{\prime}}&{=}&{\displaystyle\sum_{k=0}^{\infty}\left\{(1-\rho)\rho^{s-1}\left[a_{k}^{\prime}l_{k}+a_{k}\frac{\partial l_{k}}{\partial\rho}\rho^{\prime}\right]+\dotsb\right.}\\ {}&{}&{\left.+(1-\rho)(s-1)\rho^{s-2}\cdot\rho^{\prime}\cdot a_{k}l_{k}-\rho^{\prime}\rho^{s-1}a_{k}l_{k}\right\}\;.}\\ \end{array} $$ 

Upon inserting the relations (3.19) and (3.3.a,b), one ends up with

 $$ P_{s}^{\prime}=(1-\rho)\rho^{s-1}\sum_{k=0}^{\infty}\left[a_{k}^{\prime}l_{k}+\frac{a_{k}\rho^{\prime}}{(1-\rho)\rho}(k l_{k}-(k+1)l_{k+1})\right]. $$ 

Projection onto the associated basis yields (with  $ a_{-1} := 0 $):

 $$ \rho^{-j}\left\langle l_{j},P_{s}^{\prime}\right\rangle=a_{j}^{\prime}+\frac{j\rho^{\prime}}{(1-\rho)\rho}(a_{j-1}^{\prime}-a_{j-1})j=0,1,\cdots $$ 