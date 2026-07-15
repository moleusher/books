<div style="text-align: center;">Table 5.2 presents the performance of CODEX for variable tolerances in Example 5.2.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>TOL</td><td style='text-align: center; word-wrap: break-word;'>time-steps</td><td style='text-align: center; word-wrap: break-word;'>max.order</td><td style='text-align: center; word-wrap: break-word;'>n_{max}</td><td style='text-align: center; word-wrap: break-word;'>CPU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>0.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 5 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>34</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>1.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>14.5</td></tr></table>

<div style="text-align: center;">* run represented in Fig. 5.5–5.8</div>


<div style="text-align: center;">TABLE 5.2: CODEX: performance for variable order (Example 5.2)</div>


The increase of the computing time for accuracy  $ 10^{-2} $ gives an hint, that the algorithm runs in difficulties, if the solution of a process is too far from the family  $ \Psi_{\rho,\alpha} $, e.g. distributions with two or more extrema or piecewise nearly constant solutions.

Example 5.3: Polymer Degradation. In a degradation reaction of the type

 $$ P_{s}\xrightarrow{k_{s}r}P_{r}+P_{s-r}\quad,\quad s>r\geq1\quad, $$ 

a polymer $P_{s}$ of chain length $s$ breaks at position $r$ into two polymers of length $r$ and length $s - r$. In general (see e.g. [4]) the reaction rate coefficients $k_{sr}$ depend on the degree of the polymer $s$ and the location $r$ of the breaking bond in the polymer chain. Mathematical modeling of a degradation leads to the following CODE, with $u_{s}(t)$ the number of polymers of chain length $s$ at time $t$:

 $$ u_{s}^{\prime}(t)=(A_{D}u)(s):=-\left(\sum_{r=1}^{s-1}k_{s r}\right)u_{s}(t)+2\sum_{r=s+1}^{\infty}k_{r s}u_{r}(t)\;, $$ 

re-defining the degradation operator (1.42). A realistic initial distribution  $ u_{s}(0) $ is given in [52] by

 $$ u_{s}(0)=\frac{s}{r}\bar{\rho}^{s}\quad,\quad\bar{\rho}=e^{1/\tau}\quad, $$ 

such that the maximum of the distribution $u_{s}(0)$ roughly occurs at chain length $s = r$. We consider the case $k_{sr} = k_{p}$, $k_{p}$ constant first. For an analytical preprocessing we need the relation (2.33) and employ the recurrence formula (2.22). Then the scalar products

 $$ a_{j k}:=(A_{D}\;\psi_{k}\;,\;\psi_{j})_{\rho,\alpha} $$ 