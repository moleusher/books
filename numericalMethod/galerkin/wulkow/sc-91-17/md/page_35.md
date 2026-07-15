<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time ( *10*s)</th><th style='text-align: center;'>TRUE</th><th style='text-align: center;'>CE-MA-53</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.015</td><td style='text-align: center;'>0.006</td></tr>
    <tr><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.03</td><td style='text-align: center;'>0.012</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.045</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.07</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.08</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3: Behavior of the error-estimator</div>


and $a$, $b$, $k_{1}$, $k_{1}^{\prime}$, $k_{2}$, $k_{2}^{\prime}$ constants. This problem can be solved by CODEX, leading to a traveling Poisson distribution comparable to Figure 2.

### 4.2 POLYMER DEGRADATION

In a degradation reaction of the type

 $$ P_{s}\xrightarrow{k_{s r}}P_{r}+P_{s-r}\quad,\quad s>r\geq1\quad, $$ 

a polymer $P_{s}$ of chain length $s$ breaks at position $r$ into two polymers of length $r$ and length $s-r$. In general (see e.g. [5]) the reaction rate coefficients $k_{sr}$ depend on the degree of the polymer $s$ and the location $r$ of the breaking bond in the polymer chain. Mathematical modeling of a degradation leads to the following CODE, with $u_{s}(t)$ the number of polymers of chain length $s$ at time $t$:

 $$ u_{s}^{\prime}(t)=(A_{D}u)(s):=-\left(\sum_{r=1}^{s-1}k_{s r}\right)u_{s}(t)+2\cdot\sum_{r=s+1}^{\infty}k_{r s}u_{r}(t)\;, $$ 

re-defining the degradation operator (1.14). A realistic initial distribution  $ u_{s}(0) $ from [5] can be described qualitatively by

 $$ u_{s}(0)=\frac{s}{r_{\mathrm{m a x}}}\bar{\rho}^{s}\quad,\quad\bar{\rho}=e^{-1/\tau_{\mathrm{m a x}}}\quad, $$ 