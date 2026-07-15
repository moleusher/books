such that the maximum of the distribution $u_s(0)$ roughly occurs at chain length $s = r_{\max}$ (e.g. $r_{\max} \approx 60000$ in [5]). We mentioned in Section 1.3, that the $H_{\rho,\alpha}$ - theory is valid for the degradation operator only if $\rho(1 + \alpha/2) < 1$. Therefore we cannot use the exact representation

 $$ u_{s}(0)=\frac{\bar{\rho}}{(1-\bar{\rho})^{2}r_{\mathrm{m a x}}}\;\Psi_{\bar{\rho},1}(s)\;,\;s\geq1\;, $$ 

if $\bar{\rho} > 2/3$. This implies, that distributions of the type (4.5) can only be represented in $H_{\bar{\rho},1}$ for $r_{\max} = 1 - \text{the case of a geometric distribution. Hence we use the representation of } u_s(0) \text{ in } H_{\rho,0} \text{ with } \rho = 2\bar{\rho}/(1 + \bar{\rho}) \text{ (due to } (3.31))$ and the expansion coefficients

 $$ a_{k}=\frac{\bar{\rho}}{(1-\bar{\rho})^{2}r_{\max}}2^{-k}(1-k)\ ,\ k\geq0\ , $$ 

and have to control the moving weight function fitting additionally by  $ \bar{\rho}(1 + \bar{\alpha}/2) < c $,  $ c < 1 $ a safety factor.

The degradation problem will be attacked here for the reaction coefficients

 $$ k_{s r}=k_{s}=k_{p}\;s^{\beta}\;,\;k_{p}=2.11\cdot10^{-7}\;,\;\beta=-1/3\;. $$ 

This modeling of a heterogeneous polymerization is suggested in [5] and has been treated in [38] by replacing the fractional power  $ s^{\beta} $ by a so-called factorial power. Introducing a (small and analyzed) modeling error, the problem could be solved there using product linerization formulas of discrete Laguerre polynomials. In order to solve the original problem, we have to evaluate (respectively approximate) the scalar products

 $$ \begin{array}{r l}&{\left(A_{D}\psi_{k}(\rho,\alpha),\psi_{j}(\rho,\alpha)\right)_{\rho,\alpha}=}\\ &{\displaystyle\sum_{s=1}^{\infty}l_{j}(s)\left((1-s)k_{s}l_{k}(s)\Psi_{\rho,\alpha}(s)+2\displaystyle\sum_{r=1}^{\infty}l_{k}(r+s)\Psi_{\rho,\alpha}(r+s)k_{r+s}\right)}\end{array} $$ 

by applying a double Gauss summation. Before discussing the realistic setting  $ (r_{\max}=60000) $, we show that the problem is reliably approximated by CODEX. For that we choose  $ r_{\max}=50 $ in (4.5),  $ k_{p}=1.0 $ in (4.6) and  $ t_{end}=0.01 $, such that a reference solution can be obtained by a direct integration of system (4.4) truncated at  $ s_{\max}=1000 $ and treated as an ODE. Table 2 shows the nice behavior of the Galerkin approximations for different tolerances. The original case with  $ r=60000 $ in (4.5) and  $ t_{end}=3600 $ sec. implies that the interesting maximum chain length  $ s_{\max} $ is larger than 400000. Obviously it is no longer possible to compute a direct solution of the problem in this case. But a comparison of