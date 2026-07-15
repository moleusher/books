Strongly continuous semigroups. A one parameter family  $ T(t), 0 \leq t \leq \infty $ of bounded linear operators from a Banach space X into X is called a semigroup, if

 $$ \begin{array}{c}T(0)=I,\;(I\;\mathrm{I d e n t i t y\;o n}\;X)\;,\\ T(t+t^{\prime})=T(t)T(t^{\prime})\;\mathrm{f o r~e v e r y}\;t,\;t^{\prime}\geq0\end{array} $$ 

The linear operator A defined by

 $$ \begin{array}{r l}{D(A):=}&{{}\left\{x\in X\mid\operatorname*{l i m}_{t\downarrow0}\frac{T(t)x-x}{t}\mathrm{~e x i s t s~}\right\}}\end{array} $$ 

 $$ \begin{array}{r l}{A x:=}&{{}\operatorname*{l i m}_{t\downarrow0}\frac{T(t)x-x}{t}=\left.\frac{\mathrm{d}^{+}T(t)x}{\mathrm{d}t}\right|_{t=0},x\in D(A),}\end{array} $$ 

is called the infinitesimal generator of the semigroup  $ T(t) $ with domain  $ D(A) $. In the following we will consider strongly continuous or  $ C_0 $ - semigroups which additionally have the property

 $$ \lim_{t\downarrow0}T(t)x=x\text{for every}x\in X. $$ 

For such semigroups the abstract Cauchy problem (1.52) has a unique solution for  $ \varphi \in D(A) $ and the solution is given by

 $$ u(t)=T(t)\varphi\;. $$ 

It has been shown in [7] that for homogeneous abstract Cauchy problems (1.52) with $A$ generator of a $C_0$-semigroup the global error of the implicit Euler scheme has an asymptotic expansion. As we want to apply extrapolation, we have to ensure that the semigroup approach is reasonable for CODE's formulated in $X = H_{\rho,\alpha}$.

For a $C_0$ semigroup there are constants $\omega \geq 0$ and $M \leq 1$ such that $\|T(t)\| \leq M e^{\omega t}$ for $t \geq 0$. If $\omega = 0$ and $M = 1$, $T(t)$ is called a $C_0$ semi-group of contractions. A characterization of the infinitesimal generator of such a semigroup is given by the HILLE - YOSIDA theorem.

THEOREM 1.11. A linear (possibly) unbounded operator A in a Banach space X is the infinitesimal generator of a  $ C_0 $ semigroup of contractions  $ T(t) $,  $ t \geq 0 $, if and only if

(i) A is closed and  $ D(A) $ is dense in X.

(ii) The resolvent set  $ \rho(A) $ of A contains  $ \mathbb{R}^{+} $ and for every  $ \lambda > 0 $

 $$ \|R(\lambda;A)\|\leq\frac{1}{\lambda}, $$ 

where  $  R(\lambda; A) := (\lambda I - A)^{-1}  $ is the resolvent of A.