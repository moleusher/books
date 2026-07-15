<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>NPROJ ( * E+02 )</th><th style='text-align: center;'>estimated error</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.350</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.060</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.138</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.080</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.050</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.070</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>0.050</td></tr>
    <tr><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.030</td></tr>
    <tr><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.42</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.44</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.48</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.52</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.54</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.56</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.62</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.64</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.66</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.68</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.74</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.76</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.010</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8: Estimation of the Galerkin projection error versus the number of polynomials</div>


timalization of parameters or extension of the simulated reaction times up to 750000 s (100% conversion). Note that our treatment is not restricted by the formation of very long chains. Thus we also can calculate the polydispersity for the  $ k_f $-values  $ k_f = 10^{-3} $,  $ 10^{-4} $, and  $ 10^{-5} $. The results are plotted in Figure 6. For the simulation of the reaction time 750000 s in case  $ k_f = 10^{-5} $ we need 44 s CPU time on the SPARC 1. Figure 6 makes clear that the choice of polymers  $ P_jX $ with high rate coefficient  $ k_f $ is crucial to get narrow polymer distributions.

Dealing now with the computation of the CLD’s we choose the worst case, i.e. the high structured distribution of  $ P_i $ at t=0.001 s. This CLD — plotted in Figure 1 of ref. [9] — has a very narrow peak at chain length  $ \approx $ 120 and decreases steeply for higher chain lengths. By a simulation with NPROJ=2, which was sufficient for the quantities discussed before, we get the estimate for the Galerkin projection error  $ \epsilon_2 = 0.36 $. The corresponding CLD is plotted in Figure 7.

Increasing $n=NPROJ$ lowers the estimate $\epsilon_{n}$, but the descent of $\epsilon_{n}$ is superposed by a rather oscillatory behavior (Figure 8). This is very similar to the