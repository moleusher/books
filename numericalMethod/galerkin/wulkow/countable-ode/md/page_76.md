<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>step ( E+01 )</th><th style='text-align: center;'>nodes ( E+02 )</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>0.49</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>0.68</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.35</td></tr>
  </tbody>
</table>

<div style="text-align: center;">FIGURE 5.12: Evolution of the maximum number of grid points per step.</div>


The following Table 5.4 demonstrates, that only about 45000 evaluations of the grid function  $ g(s) $ are necessary during the whole computation (TOL=5  $ \cdot $  $ 10^{-2} $).


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>TOL</td><td style='text-align: center; word-wrap: break-word;'>time-steps</td><td style='text-align: center; word-wrap: break-word;'>n_{max}</td><td style='text-align: center; word-wrap: break-word;'>max. no. of grid points</td><td style='text-align: center; word-wrap: break-word;'>total no. of grid points</td><td style='text-align: center; word-wrap: break-word;'>CPU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>24258</td><td style='text-align: center; word-wrap: break-word;'>22.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 5.10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>67</td><td style='text-align: center; word-wrap: break-word;'>45125</td><td style='text-align: center; word-wrap: break-word;'>41.1</td></tr></table>

<div style="text-align: center;">* run represented in Fig. 5.11, 5.12</div>


<div style="text-align: center;">TABLE 5.4: CODEX: performance for numerical preprocessing (Example 5.3).</div>


Example 5.4: Coagulation Processes. Finally an important and challenging nonlinear class of problems is addressed. Coagulation (combination) processes can be described in chemical notation by

 $$ P_{r}+P_{s}\xrightarrow{k_{r s}}P_{r+s}, $$ 

where $P_{s}$ may denote a polymer molecule or a soot (smog) particle of size $s$. Coagulation (combination) processes appear frequently in applications - distinguished by different modelings of the reaction rate coefficients $k_{rs}$. In polymer chemistry often moment dependent rate coefficients are in use, whereas the modeling of surface effects for the combination of smog particles leads to coefficients dependent on the size of the reacting molecules. The CODE of a coagulation process reads in general $(u_{s}(t)$ defined as in Example 5.3)

 $$ u_{s}^{\prime}(t)=F(u(t)):=\frac{1}{2}\sum_{r=1}^{s-1}k_{r,s-r}u_{r}(t)u_{s-r}(t)-u_{s}(t)\sum_{r=1}^{\infty}k_{s r}u_{r}(t)\;. $$ 