Theorem (Wulkow). Consider a sub-scale of  $ H_\rho $ spaces (with  $ \alpha $ omitted) for  $ \rho \in [\rho_0, 1) $,  $ 0 < \rho_0 < 1 $. Let  $ J = [0, T_f] \subset \mathbb{R} $ and assume:

• The operator

 $$ F:J\times H_{\rho}\longrightarrow H_{\bar{\rho}} $$ 

is continuous for  $ \bar{\rho} > \rho $ and  $ F(t, u(0)) \in H_{\rho_0} $ on  $ J $.

• There exists a constant M such that

 $$ \|F(t,u)-F(t,v)\|_{\bar{\rho}}\leq\frac{M}{(\bar{\rho}-\rho)^{\gamma}}\|u-v\|_{\rho},\quad0<\gamma\leq1, $$ 

for  $ t \in J $,  $ \bar{\rho} > \rho $ and  $ u, v \in H_{\rho} $.

Then for every  $ \rho \in (\rho_0, 1) $ the initial value problem

 $$ u^{\prime}(t)=F(t,u(t)),u(0)=\varphi\in H_{\rho_{0}} $$ 

has a unique solution

 $$ u:[0,\delta(\bar{\rho}-\rho)^{\gamma})\longrightarrow H_{\bar{\rho}}\:, $$ 

with $\delta = \min\{T_f, (Md_\gamma)^{-1}\}$. The constant $d_\gamma > 1$ can be computed in concrete cases, e.g. $d_1 = e$, $d_{1/2} = 2\sqrt{3}/3$.

In order to overcome the second above mentioned difficulty, Wulkow adopted an adaptive Rothe method with a so-called multiplicative error correction, that Bornemann [4, 5] had designed for parabolic PDE's. This method, which is theoretically based on analytic semigroup theory [14], also uses a scale of Hilbert spaces (appropriate for the parabolic case, of course). The name "Rothe method" stands for the fact that in this approach time is discretized first, which thus generates a stationary problem on a single Hilbert space. For example, time discretization of the linear CODE (3.1) by the implicit Euler scheme with time step  $ \tau $ leads to the countable system of algebraic equations

 $$ (I-\tau A)\tilde{u}(t+\tau)=u(t). $$ 

Here  $ \tilde{u}(t+\tau) $ is understood to be the approximation of the solution  $ u(t+\tau) $. For the in general nonlinear CODE

 $$ u_{s}^{\prime}(t)=f_{s}(u_{1}(t),u_{2}(t),\ldots)\quad,\quad s=1,2,\ldots\quad, $$ 

the adaptive Rothe method may be based on the semi-implicit Euler discretization due to [11], which here reads

 $$ \begin{aligned}(I-\tau A)\Delta u&=f(u(t))\quad,\\u(t+\tau)&\approx u^{1}=u+\Delta u\end{aligned} $$ 