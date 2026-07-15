The present example will demonstrate, that this task can be efficiently accomplished by the SUMMATOR. For demonstration purposes we restrict ourselves here to a case which also can be treated analytically. For this we consider

 $$ \begin{array}{r}{\big(\psi_{10}(s;\rho,0),\psi_{10}(s;\rho,0)\big)_{\rho,0}=\rho^{10}\quad\mathrm{a n d}\quad\big(\psi_{10}(s;\rho,0),\psi_{9}(s;\rho,0)\big)^{\rho,0}=0\;.}\end{array} $$ 

In both cases the terms of the sum are dominated by a polynomial of high degree. The second case is of interest as a test of the absolute scaling for results near zero. For the computations the sums in the scalar products have been truncated at  $ s_{\max} = 10^5 $ for  $ \rho = 0.999 $.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>s ( * E+05 )</th><th style='text-align: center;'>( * E-04 )</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>1.610</td></tr>
    <tr><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.750</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.720</td></tr>
    <tr><td style='text-align: center;'>0.03</td><td style='text-align: center;'>0.700</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.680</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.660</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.640</td></tr>
    <tr><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.620</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.600</td></tr>
    <tr><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.580</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.560</td></tr>
    <tr><td style='text-align: center;'>0.11</td><td style='text-align: center;'>0.540</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.520</td></tr>
    <tr><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.500</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.480</td></tr>
    <tr><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.460</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.440</td></tr>
    <tr><td style='text-align: center;'>0.17</td><td style='text-align: center;'>0.420</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.400</td></tr>
    <tr><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.380</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.360</td></tr>
    <tr><td style='text-align: center;'>0.21</td><td style='text-align: center;'>0.340</td></tr>
    <tr><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.320</td></tr>
    <tr><td style='text-align: center;'>0.23</td><td style='text-align: center;'>0.300</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>0.280</td></tr>
    <tr><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.260</td></tr>
    <tr><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.240</td></tr>
    <tr><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.220</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.200</td></tr>
    <tr><td style='text-align: center;'>0.29</td><td style='text-align: center;'>0.180</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.160</td></tr>
    <tr><td style='text-align: center;'>0.31</td><td style='text-align: center;'>0.140</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.120</td></tr>
    <tr><td style='text-align: center;'>0.33</td><td style='text-align: center;'>0.100</td></tr>
    <tr><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.080</td></tr>
    <tr><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.060</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>0.37</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">FIGURE 6.2: Typical grid (tol=10⁻³, 63 nodes) arising from the summation of scalar products in  $ H^{\rho,\alpha} $.</div>


The number of nodes for these examples range from 50 for tolerance  $ 10^{-2} $ up to about 500 for tolerance  $ 10^{-6} $. For further applications see Example 5.3.

Example 6.3. Finally we present some results for double series. We consider the sum

 $$ \sum_{s=1}^{s_{\mathrm{m a x}}}l_{1}(s;\rho,0)\sum_{r=1}^{s-1}k_{r,s-r}P_{r}P_{s-r}, $$ 

with the coefficients (5.14)

 $$ k_{r,s}:=\left(\frac{1}{r}+\frac{1}{s}\right)^{1/2}\left(r^{1/3}+s^{1/3}\right)^{2} $$ 