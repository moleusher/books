where  $ \varepsilon > 0 $ is chosen such that  $ \bar{\rho} - \varepsilon > \rho_{0} $. In order to get rid of the factor  $ 1/(k + 1) $ we set

 $$ \varepsilon=\frac{\bar{\rho}-\rho_{0}}{(k+1)^{1/\gamma}} $$ 

and end up with

 $$ \|u_{k+1}(t)-u_{k}(t)\|_{\bar{\rho}}\leq C_{\rho_{0}}(t)\left(\frac{M t d_{\gamma}}{(\bar{\rho}-\rho_{0})^{\gamma}}\right)^{k+1}\frac{1}{d_{\gamma}}\left(\frac{k+1}{((k+1)^{1/\gamma}-1)^{\gamma}}\right)^{k}. $$ 

The last factor on the right-hand side is bounded in  $ k $ for  $ \gamma \leq 1 $. This leads to the definition of  $ d_\gamma $. In particular for  $ \gamma = 1/2 $ the maximum is achieved at  $ k = 1 $ with  $ d_{1/2} $. For  $ \gamma = 1 $ the term reduces to  $ ((k + 1)/k)^k \leq e $. Thus (1.51) holds for all  $ k $ and as  $ Mtd_\gamma(\bar{\rho} - \rho)^{-\gamma} < 1 $ for  $ t \in [0, \delta(\bar{\rho} - \rho_0)^\gamma) $ the sequence  $ u_k(t) $ is a Cauchy sequence and converges uniformly on every closed subinterval of  $ [0, \delta(\bar{\rho} - \rho_0)^\gamma) $ to a continuous  $ u(t) $ satisfying

 $$ u(t)=\varphi+\int_{0}^{t}F(s,u(s))\mathrm{d}s. $$ 

Moreover  $ u(t) $ is a solution of the initial value problem, since

 $$ F(\cdot,u(\cdot)):[0,\delta(\bar{\rho}-\rho_{0})^{\gamma})\to H_{\bar{\rho}} $$ 

is continuous. In order to prove local uniqueness, we consider two solutions  $ u(t) $,  $ v(t) \in H_{\bar{\rho}} $,  $ \bar{\rho} > \rho_0 $. For fixed  $ t $ and  $ \rho_1 > \bar{\rho} $,

 $$ \left\|u(t)-v(t)\right\|_{\rho_{1}}\leq\frac{M t d_{\gamma}}{(\rho_{1}-\bar{\rho})^{\gamma}}C_{1}(t),C_{1}(t)=\max_{s\in[0,t]}\left\|u(s)-v(s)\right\|_{\bar{\rho}}. $$ 

Now, similar to the considerations above, we ‘fill in’ estimates in $k$ spaces between $H_{\rho_{1}}$ and $H_{\bar{\rho}}$ – setting $\varepsilon = (\rho_{1} - \bar{\rho}) / (k + 1)^{1/\gamma}$ in the $k$-th step – and end up with

 $$ ||u(t)-v(t)||_{\rho_{1}}\leq C_{1}(t)\left(\frac{M t d_{\gamma}}{(\rho_{1}-\bar{\rho})^{\gamma}}\right)^{k}. $$ 

Thus for $t < (\rho_1 - \bar{\rho})^{-\gamma}(M d_\gamma)^{-1}$ we have $u(t) = v(t)$. The rest follows by continuation.

Remarks. (i) Theorem 1.9 serves only as an example for the structure of the problems we are dealing with. An extension to larger time intervals could be tried as well as the obtainment of results explaining solutions for unbounded operators in a ‘smaller’ space (see  $ A_{1} $ in Example 1.6). But this might be a