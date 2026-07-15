### 5.2 Open Systems

Among the selection of polyreaction processes in Section 1.1, the polymer degradation and the reversible polymerization lead to open differential systems. In these cases, the estimate (2.19) of the Galerkin approximation error needs an additional consideration. Whenever the adapted parameters (here  $ \rho $ or  $ \lambda $) are independent of the truncation index N, then a reasonable relative error estimate will be

 $$ \epsilon_{N}:=\frac{\|\bar{P}_{s}^{(N)}-\bar{P}_{s}^{(N+1)}\|_{\Psi}}{\|\bar{P}_{s}^{(N+1)}\|_{\Psi}} $$ 

in terms of the definition (2.19) and

 $$ \|\bar{P}_{s}^{(N+1)}\|_{\Psi}=\left(\sum_{k=0}^{N+1}\left(a_{k}^{(N+1)}\right)^{2}\gamma_{k}\right)^{1/2}\;. $$ 

If, however, the truncation index N affects the value of  $ \rho $ or  $ \lambda $, then also the normalization factors  $ \gamma_{k} $ and the polynomial basis are affected. In this situation, the estimate (2.19) must be modified replacing

 $$ a_{k}^{(N)}-a_{k}^{(N+1)}\longrightarrow a_{k}^{(N)}-a_{k}^{(N+1)}+\frac{j\delta\rho}{(1-\rho)\rho}\left(a_{k}^{(N)}-a_{k-1}^{(N)}\right) $$ 

with

 $$ \begin{array}{r}{\dot{\rho}:=\rho^{(N)}\quad,\quad\delta\rho:=\rho^{(N)}-\rho^{(N+1)}}\end{array} $$ 

for the Galerkin-Laguerre approximation and replacing

 $$ \dot{a}_{k}^{(N)}-\dot{a}_{k}^{(N+1)}\xrightarrow{\quad}\dot{a}_{k}^{(N)}-\dot{a}_{k}^{(N+1)}-\delta\lambda a_{k-1}^{(N)} $$ 

with

 $$ \delta\lambda:=\lambda^{(N)}-\lambda^{(N+1)} $$ 

 $$ \begin{array}{r l}{\zeta}&{{}\approx\zeta_{0}.}\end{array} $$ 

for the Galerkin-Charlier approximation. In both cases, the factors

 $$ \textcircled{r}\quad\textcircled{r}\quad\textcircled{V}M_{n}\approx0.8\quad\textcircled{s} $$ 

 $$ \gamma_{k}:=\gamma_{k}^{(N+1)} $$ 

are to be inserted.

Polymer degradation. The preprocessing of model (1.7)/(1.8.a) by discrete Laguerre polynomials leads to the differential equations (4.22). The initial values (4.23) with

 $$ r:=100\quad,\quad s_{max}=1000 $$ 