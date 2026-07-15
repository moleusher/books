leading in turn to the condition

 $$ \mid\int_{\frac{t}{2}}^{t}e^{s\tau}g(\tau)\mathrm{d}\tau\mid\leq M,s=1,2,\ldots, $$ 

for a constant $M$ and $g(\tau) := (1 - e^{t - \tau}) f(\tau)$. Extension of the proof of Lemma 4.1.1 in [44] to integrable functions allows to conclude from (1.12), that $g(\tau) \equiv 0$ on $[0, t]$ almost everywhere. This means, that by restriction from $l^1$ to the space $H_t$ we obtain a unique solution

 $$ u_{s}(t)=v_{s}(0)e^{-(s-1)t}-v_{s+1}(0)e^{-s t}\;. $$ 

If we compare this result with the numerical solution of degradation processes achieved by the discrete Galerkin method in [18], we observe that there a so-called moving weight function condition in principle has led to the space  $ H_t $. As we will see below (Corollary 1.5), the condition  $ u \in H_t $ in particular implies, that all statistical moments of u are bounded. This is a natural assumption for many problems. In addition, we have seen in [18], that in  $ H_t $ an efficient approximation of solutions of (1.7) is possible. So for theoretical and for numerical reasons the choice of the spaces  $ H_t $ seems to be promising.

In the above example we got uniqueness by restricting the solution to ‘smaller’ spaces. We will exemplify now, that in order to obtain existence of solutions it can be necessary to extend to ‘larger’ spaces (see also examples in [12]):

Example 1.3: Discrete convolution. Consider the problem

 $$ u_{s}^{\prime}(t)=\sum_{r=1}^{s-1}u_{r}(t)u_{s-r}(t)\quad,\quad u_{s}(0)=\varphi_{s}\quad, $$ 

defined by means of the convolution operator  $ A_{C} $

 $$ \left(A_{C}\;u\right)_{s}:=\sum_{r=1}^{s-1}u_{r}\;u_{s-r}\;. $$ 

This operator is nonlinear and plays a role in many applications, where objects (e.g. chemical molecules) of size r and size s - r are combined to an object of size s (combination or coagulation processes).

Let us assume that the initial value

 $$ \varphi(s):=(1-\rho)\rho^{s-1},\ 0<\rho<1, $$ 

is prescribed. Such an initial setting is typical for the problems treated in Chapter 5 and convenient for our considerations anyway. We can check, that

 $$ \varphi\in H_{\rho}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid\|u\|_{\rho}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}\left(1-\rho\right)^{-1}\rho^{-\left(s-1\right)}<\infty\right\}. $$ 