and end up with

 $$ \|u_{k+1}(t)-u_{k}(t)\|_{\bar{\rho}}\leq C_{\rho_{0}}(t)\left(\frac{M t d_{\gamma}}{(\bar{\rho}-\rho_{0})^{\gamma}}\right)^{k+1}\frac{1}{d_{\gamma}}\left(\frac{k+1}{((k+1)^{1/\gamma}-1)^{\gamma}}\right)^{k}. $$ 

The last factor on the right-hand side is bounded in $k$ for $\gamma \leq 1$. For $\gamma = 1/2$ the maximum is achieved at $k = 1$ with $d_{1/2}$. For $\gamma = 1$ we can see that $(k + 1)/k)^k \leq e$. Thus (1.20) holds for all $k$ and as $Mtd_\gamma(\bar{\rho} - \rho)^{-\gamma} < 1$ for $t \in [0, \delta(\bar{\rho} - \rho_0)^\gamma)$ the sequence $u_k(t)$ is a Cauchy sequence and converges uniformly on every closed subinterval of $[0, \delta(\bar{\rho} - \rho_0)^\gamma)$ to a continuous $u(t)$ satisfying

 $$ u(t)=\varphi+\int_{0}^{t}F(s,u(s))\mathrm{d}s. $$ 

Moreover  $ u(t) $ is a solution of the initial value problem, since

 $$ F(\cdot,u(\cdot)):[0,\delta(\bar{\rho}-\rho_{0})^{\gamma})\to H_{\bar{\rho}} $$ 

is continuous. In order to prove local uniqueness, we consider two solutions  $ u(t) $,  $ v(t) \in H_{\bar{p}} $,  $ \bar{\rho} > \rho_0 $. For fixed  $ t $ and  $ \rho_1 > \bar{\rho} $,

 $$ ||u(t)-v(t)||_{\rho_{1}}\leq\frac{M t d_{\gamma}}{(\rho_{1}-\bar{\rho})^{\gamma}}C_{1}(t),C_{1}(t)=\max_{s\in[0,t]}||u(s)-v(s)||_{\bar{\rho}}. $$ 

Now, similar to the considerations above, we ‘fill in’ estimates in $k$ spaces between $H_{\rho_1}$ and $H_{\bar{\rho}}$ - setting $\varepsilon = (\rho_1 - \bar{\rho}) / (k + 1)^{1/\gamma}$ in the $k$-th step - and end up with

 $$ ||u(t)-v(t)||_{\rho_{1}}\leq C_{1}(t)\left(\frac{M t d_{\gamma}}{(\rho_{1}-\bar{\rho})^{\gamma}}\right)^{k}. $$ 

Thus for  $ t < (\rho_1 - \bar{\rho})^{-\gamma}(Md_\gamma)^{-1} $ we have  $ u(t) = v(t) $. The rest follows by continuation.

Example 1.6. Consider the convolution operator  $ A_{C} $,

 $$ (A_{C}\;u)(s)=\sum_{r=1}^{s-1}u_{r}\;u_{s-r}\;, $$ 

which is the first part of the Smolochowski model in Example 1.3. Using Lemma 1.5 and Corollary 1.6 it can be shown for the Frechét derivative  $ DA_C $ of  $ A_C $, that

 $$ \left\|D A_{C}(u)v\right\|_{\rho}^{2}\leq\frac{1}{\varepsilon}2(1-\rho+\varepsilon)\left\|u\right\|_{\rho}^{2}\left\|v\right\|_{\rho-\varepsilon}^{2}. $$ 

Application of the mean-value theorem gives (1.18) with  $ \gamma = 1/2 $. Thus Theorem 1.7 explains, why the space  $ H_{\rho} $ has to be changed with time for the Smolochowski model.