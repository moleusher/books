can be evaluated:

 $$ a_{jk}=\left\{\begin{array}{ll}\frac{k_{p}}{1-\rho}j&,\text{for}k=j-1,k\neq0,\\\frac{k_{p}}{1-\rho}(-j-\rho(j-1)-\alpha\rho)&,\text{for}k=j,k\neq0,\\\frac{k_{p}}{1-\rho}\rho(j-1)(1+\alpha/(j+1))&,\text{for}k=j+1.\end{array}\right. $$ 

For  $ |j - k| > 1 $,  $ k \neq 0 $ the scalar products are zero ( $ \rightarrow A_D $ is 1-invariant), the remaining terms are

 $$ a_{00}=\frac{k_{p}}{1-\rho}\rho(1+\alpha),a_{10}=\frac{k_{p}}{1-\rho}(1+\rho\alpha),a_{j0}=\frac{2k_{p}\rho\alpha}{(1-\rho)(j+1)},j\geq2. $$ 

We know from Example 1.6 and Corollary 1.12, that the algorithm can be applied to the degradation operator for  $ \rho(1+\alpha/2)<1 $. Therefore we cannot use the exact representation (3.4) of the initial value  $ \varphi $ by

 $$ \varphi(s)=\frac{\bar{\rho}}{(1-\bar{\rho})^{2}r}\Psi_{\bar{\rho},1}(s),s\geq1, $$ 

when $\bar{\rho} > 2/3$ ($\bar{\rho} > 1/2$ with a safety factor). This means, that distributions of the type (5.6) can only be represented in $H_{\bar{\rho},1}$ for $r = 1$. But with this we are back to a geometric distribution. Hence we use the representation of $\varphi$ in $H_{\rho,0}$ with $\rho = 2\bar{\rho}/(1+\bar{\rho})$ and the expansion coefficients $a_k$ from Example 3.1 and have to control the moving weight function fitting additionally by $\bar{\rho}(1+\bar{\alpha}/2) < c, c < 1$ a safety factor. Taking e.g. 30 coefficients introduces an error of about $10^{-8}$ for $\varphi - \text{sufficient}$ for all computations. By the way we note, that a simulation started in $H_{\bar{\rho},1}$ failed indeed.

Figure 5.9 shows a typical simulation of a degradation up to  $ t = 1000 $ seconds, started with (5.6) having a maximum at  $ r = 60000 $ and a reaction constant  $ k_p = 2.11 \cdot 10^{-7} $ due to [4]. The lines show the weight distribution

 $$ P_{s}(t):=s\cdot u_{s}(t),1\leq s\leq400000. $$ 

As the qualitative behavior of the process is the same for small $r$, Figure 5.10 and Table 5.3 are computed using $r = 50$, $k_p = 1$ and $t = 1$. This numbers are chosen just to compare the results with a true solution obtained by direct integration of a system of 1000 ODE's here.