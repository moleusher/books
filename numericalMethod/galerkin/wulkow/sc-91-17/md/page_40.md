(see Figure 6). Nevertheless, a relative accuracy of 8-10% can be obtained in moderate computing times (about 50 sec. CPU on a SPARC 1+), which increase strongly for higher accuracies. This is an effect of properties of the basis functions, not a consequence of the used time and operator discretization. For

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>s (E+04)</th><th style='text-align: center;'>P(s) (E-06)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>0.03</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.88</td></tr>
    <tr><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.99</td></tr>
    <tr><td style='text-align: center;'>0.09</td><td style='text-align: center;'>1.00</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.67</td></tr>
    <tr><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.62</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.54</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.51</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.48</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.36</td></tr>
    <tr><td style='text-align: center;'>0.42</td><td style='text-align: center;'>0.34</td></tr>
    <tr><td style='text-align: center;'>0.44</td><td style='text-align: center;'>0.32</td></tr>
    <tr><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>0.48</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.26</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6: Comparison between direct solution (…) and Galerkin approximations with n = 4 (-) and n = 20 (---) of a heterogeneous coagulation process at t = 100.</div>


a better study of the algorithm for higher accuracies, we compute directly the weight distribution  $ u_{s}(t) \cdot s $ from a transformed equation (4.8). Table 3 shows the performance of CODEX for a simulation up to  $ t = 100 $ sec. in this case. If


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>TOL</td><td style='text-align: center; word-wrap: break-word;'>time-steps</td><td style='text-align: center; word-wrap: break-word;'>n_{max}</td><td style='text-align: center; word-wrap: break-word;'>true error in H_{\rho,\alpha}</td><td style='text-align: center; word-wrap: break-word;'>CPU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1.4 \cdot 10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>67</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>8.5 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>49</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>135</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>3.1 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>1386</td></tr></table>

<div style="text-align: center;">Table 3:</div>


<div style="text-align: center;">CODEX: performance for several tolerances.</div>


the direct solution at $t = 100$ sec. is directly represented by a basis expansion with the parameters obtained by CODEX (i.e. $\rho$, $\alpha$ and $n$), the behavior of the time error estimation can be studied. In Table 4 it can be seen, that this device works very accurate. Figure 7 shows the time evolution (in logarithmic scale) of the weight distribution up to $t = 100$ sec., showing how fast the mean value increases with time. Table 5 compares the computing times of CODEX and