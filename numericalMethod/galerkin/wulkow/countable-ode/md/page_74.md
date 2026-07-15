
<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>TOL</td><td style='text-align: center; word-wrap: break-word;'>time-steps</td><td style='text-align: center; word-wrap: break-word;'>max.order</td><td style='text-align: center; word-wrap: break-word;'>n_{max}</td><td style='text-align: center; word-wrap: break-word;'>norm of true-error in H_{\rho,\alpha}</td><td style='text-align: center; word-wrap: break-word;'>CPU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>3 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>0.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>2 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>1.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>7 \cdot 10^{-3}</td><td style='text-align: center; word-wrap: break-word;'>5.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5 \cdot 10^{-3}</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>3 \cdot 10^{-3}</td><td style='text-align: center; word-wrap: break-word;'>5.5</td></tr></table>

<div style="text-align: center;">* run represented in Fig. 5.9, 5.10</div>


<div style="text-align: center;">TABLE 5.3: CODEX: performance for variable order (Example 5.3)</div>


As the degradation operator is not invariant in the sense of Definition 3.1, we also have to control the truncation error by increasing the actual truncation index n to an  $ \tilde{n} > n $. Tests show, that in all steps  $ n + 1 $ or  $ n + 2 $ coefficients are sufficient to ensure the condition (3.20). In all runs the number of expansion coefficients decreases during the time evolution. As expected from the theory, the degradation operator is smoothing ( $ A_1 $ is dissipative).

Numerical Preprocessing. Now the degradation problem will be attacked for

 $$ k_{s r}=k_{s}=k_{p}s^{\beta}~,~k_{p}=2.11\cdot10^{-7}~,~\beta=-1/3~. $$ 

This modeling of a heterogeneous polymerization is given in [4] and has been treated in [52] by replacing the fractional power by a so-called factorial power. Introducing a (small and controlled) modeling error, the problem could be solved there using product linerization formulas of discrete Laguerre polynomials. In order to solve the original problem, we use the SUMMATOR in order to evaluate the scalar products

 $$ \left(A_{D}^{\beta}\psi_{k}(\rho,\alpha)\;,\;\psi_{j}(\rho,\alpha)\right)_{\rho,\alpha}=k_{p}\sum_{s=2}^{\infty}\Psi_{\rho,\alpha}(s)\;l_{k}(s)\;s^{\beta}\;g(s)\;, $$ 

with  $ A_{D}^{\beta} $ the degradation operator with coefficients (5.8) and the grid function  $ g(s) $ defined by

 $$ g(s)=-(s-1)l_{j}(s)+\frac{2}{1-\rho}\left(\rho l_{j}(s)-l_{j+1}(s)+\rho^{j+1}\binom{j+\alpha}{j+1}\right) $$ 

for s > 2 and

 $$ g(2)=-l_{j}(2)+2l_{k}(2)l_{j}(1)\Psi_{\rho,\alpha}(2)\;. $$ 

Here relation (2.33) enters again, but the analytic preparations cannot be continued, because there is no closed representation of the scalar products including the fractional power of s. Thus a numerical summation is necessary.