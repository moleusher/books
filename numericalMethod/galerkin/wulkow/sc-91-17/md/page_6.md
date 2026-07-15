Specializing  $ \varphi_{s} = \delta_{s,1} $,  $ \delta_{s,r} $ the Kronecker symbol, the solution  $ u_{s}(t) $ is a Poisson distribution with parameter t:

 $$ u_{s}(t)=\epsilon^{-t}\frac{t^{s-1}}{(s-1)!} $$ 

Example 1.2: Summatory systems. Equations of this type have been studied by HILLE [28] and are related to mathematical models of polymer degradation processes [5], which have already been treated numerically by use of the discrete Galerkin method in [19] and [38] (see also Example 4.2). Let us consider the following system:

 $$ u_{s}^{\prime}(t)=-(s-1)u_{s}(t)+\sum_{r=s+1}^{\infty}u_{r}(t),u_{s}(0)=\varphi_{s},s\in\mathbb{N}. $$ 

The initial value problem (1.5) is not uniquely solvable, because its solution depends on an arbitrary (only integrable) function  $ f = f(t) $ [28]. However, with the definition of a family of Hilbert spaces

 $$ H_{t}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid||u||_{t}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}e^{s t}<\infty\right\}, $$ 

the condition  $ u(t) \in H_t $ enforces the uniqueness of the solution and the bound-edness of all statistical moments of  $ u $ (Corollary 1.4). The latter property is a natural requirement in many problems. Finally, in  $ H_t $ an efficient approximation of solutions of (1.5) is possible [19].

Example 1.3: Smolochowski model. In [19], the solution of the Smolochowski model

 $$ u_{s}^{\prime}(t)=\frac{1}{2}\sum_{r=1}^{s-1}u_{r}(t)u_{s-r}(t)-u_{s}(t)\sum_{s=1}^{\infty}u_{r}(t)\quad,\quad u_{s}(0)=\delta_{s,1}\quad,\quad s\in\mathbb{N}\quad, $$ 

could be approximated well in the scale of Hilbert spaces

 $$ H_{\rho}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid||u||_{\rho}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}\left(1-\rho\right)^{-1}\rho^{-(s-1)}<\infty\right\} $$ 

for $\rho > \left(\frac{t}{t+2}\right)^2$. The condition on $\rho$ is necessary and enforces the change of the space $H_\rho$ with $t$. The reason is, that the operator describing this problem is not Lipschitz continuous as an operator on $H_\rho$ for fixed $\rho$, but only as an operator on the scale $H_\rho$, $0 < \rho < 1$ (Example 1.6).