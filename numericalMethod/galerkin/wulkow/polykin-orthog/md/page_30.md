<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>S ( *E+01 )</th><th style='text-align: center;'>P(S,1) (Solid)</th><th style='text-align: center;'>P(S,1) (Dashed)</th><th style='text-align: center;'>P(S,1) (Dotted)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.90</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1: Various discrete Galerkin-Laguerre approximations  $ P_s^{(N)} $, t = 5, for the chain addition polymerization problem. The approximations for N = 1, 10, 30 approach the solution from below. Note that, in this model problem, the Galerkin-Charlier approximation is exact already for N = 1.</div>


Coagulation/polycondensation. The preprocessing of the Smoluchowski model (1.9)/(1.10) by discrete Laguerre polynomials showed that for the special initial values (4.15) the exact solution can be represented already with N = 1, which means

 $$ N_{s}(t)=a_{0}(t)\left(1-\rho(t)\right)\rho(t)^{s-1} $$ 

The functions  $ a_{0}, \rho $ are defined by the 2 coupled differential equations (4.14.a,b), which can be solved in closed analytic form to yield:

 $$ a_{0}(t)=\frac{2}{t+2}\quad,\quad\rho(t)=\frac{t}{t+2}. $$ 

This example is chosen to demonstrate the importance of the Hilbert space condition (2.6). For this purpose, the analytic solution (5.3) and the weight function  $ \Psi $ with, for the time being, arbitrary  $ \rho $ are inserted into (2.6): this means that