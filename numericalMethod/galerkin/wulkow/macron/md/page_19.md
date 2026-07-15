<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>PERCENT. CONVERSION ( * E+02 )</th><th style='text-align: center;'>MEANLENGTH ( Solid Blue)</th><th style='text-align: center;'>MEANLENGTH ( Dashed Blue)</th><th style='text-align: center;'>MEANLENGTH ( Solid Red)</th><th style='text-align: center;'>MEANLENGTH ( Dashed Red)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5: Mean values of the chain length of all polymer species for reaction constants  $ k_f = 10^{-2} $ (—),  $ 10^{-3} $ (−−),  $ 10^{-4} $ (…) and  $ 10^{-5} $ (−−) versus percentage conversion of the monomer M</div>


supercomputers and was applied to the following reaction system.

 $$ \begin{array}{ccc} P_{i}X& ↔&\begin{array}{c} k_{f}(i)\\ \longleftrightarrow\\ k_{-f}(i)\end{array} \\ \end{array}P_{i}+X $$ 

 $$ \begin{array}{l}P_{i}+M\quad\xrightarrow{k_{p}(i)}\quad P_{i+1}\\P_{i}+P_{j}\quad\xrightarrow{k_{t}(i,j)}\quad D_{i+j}\end{array} $$ 

Involved chemical species are the monomer M, the radical X, and three different polymer species  $ P_iX $,  $ P_i $,  $ D_i $. For more details we refer to [9].

The maximum number of species that could be handled in [9] was limited by the maximum vector length available on the used supercomputer (CYBER 205) as well as by the demand on the central processing units (CPU). Therefore the concentrations  $ D_{i}, i = 1, 2, \ldots $, were not treated separately for each index i.