The simulation is started with (5.6),  $ r = 60000 $, the upper bound  $ s_{\text{max}} $ of the sum in the scalar product is chosen to be  $ 10^6 $. This number is not crucial.

Obviously the computational effort is now significantly higher than the effort in the case of constant reaction coefficients above, in particular for high accuracies and high time discretization order. Thus we restrict ourselves to technical accuracies and order 2 in the extrapolation table. Figure 5.11 compares the solution  $ u(t) $ at  $ t = 3600 $ sec obtained by the method suggested in [52] ( $ \cdots $) and by CODEX (—). It can be seen that the results are in good agreement.

The number of nodes in the finest summation grid per time step is presented in Figure 5.12. The adaptive generation of these grids, described in Chapter 6, is controlled by the required truncation error of the Galerkin approximation, which in turn gets its tolerance from the time-step control. This means that the outline of the algorithm, suggested at the end of Section 1.1, has been completely realized.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>s ( · E+05)</th><th style='text-align: center;'>u(s) ( · E+01)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.545</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.480</td></tr>
    <tr><td style='text-align: center;'>0.03</td><td style='text-align: center;'>0.420</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.370</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.330</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.290</td></tr>
    <tr><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.250</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.210</td></tr>
    <tr><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.170</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.140</td></tr>
    <tr><td style='text-align: center;'>0.11</td><td style='text-align: center;'>0.110</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.090</td></tr>
    <tr><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.070</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.030</td></tr>
    <tr><td style='text-align: center;'>0.17</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.005</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">FIGURE 5.11: Heterogeneous degradation, t = 3600 sec. (Example 5.4)</div>
