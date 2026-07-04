 $$ \begin{aligned}\frac{\mathrm{d}P_{1}\left(t\right)}{\mathrm{d}t}&=k_{\mathrm{s}}IM-\left(k_{\mathrm{p}}+k_{\mathrm{f}}\right)MP_{1}-P_{1}\sum_{r}\left(k_{\mathrm{ic}}^{1,r}+k_{\mathrm{id}}^{1,r}\right)P_{r}-k_{1}P_{l}\sum_{r}rD_{r}+\left(k_{1}D_{s}+k_{\mathrm{f}}M\right)\sum_{r}P_{r}\\\frac{\mathrm{d}P_{s}\left(t\right)}{\mathrm{d}t}&=-\left(k_{\mathrm{p}}+k_{\mathrm{f}}\right)MP_{s}+k_{\mathrm{p}}MP_{s-1}-P_{s}\sum_{r}\left(k_{\mathrm{ic}}^{s,r}+k_{\mathrm{id}}^{s,r}\right)P_{r}-k_{1}P_{s}\sum_{r}rD_{r}+k_{1}sD_{s}\sum_{r}P_{r}\\\frac{\mathrm{d}D_{s}\left(t\right)}{\mathrm{d}t}&=k_{\mathrm{f}}MP_{s}+P_{s}\sum_{r}k_{\mathrm{id}}^{s,r}P_{r}+\frac{1}{2}\sum_{r=1}^{1}k_{\mathrm{tc}}^{r,s-r}P_{r}P_{s-r}+\mathbf{k}_{1}P_{s}\sum_{r}rD_{r}-k_{1}sD_{s}\sum_{r}P_{r}\end{aligned} $$ 

The initial concentrations are set to  $ I(0) = 0.01 $ and  $ M(0) = 10 $. The values of the reaction rate coefficients are chosen to reflect a typical and interesting behavior:  $ k_{\mathrm{s}} = 10^{-4} $,  $ k_{\mathrm{p}} = 200 $,  $ k_{\mathrm{f}} = 0.01 $. The combination and the disproportionate coefficients are set to  $ k_{\mathrm{tc}} = (2/3) k_{\mathrm{t}} $ and  $ k_{\mathrm{td}} = (1/3) k_{\mathrm{t}} $ in the following.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>10⁻³, Time/s</th><th style='text-align: center;'>P_n, P_w</th><th style='text-align: center;'>Conversion</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.000000</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.000008</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.000015</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.000022</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.000030</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.000038</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.000045</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.000050</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.000052</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.000053</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.000054</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 4. Number-average  $ (-\cdot-\cdot) $ and weight-average  $ \left(\cdots\right) $ degrees of polymerization  $ \left(P_{n}, P_{w}\right) $ of dead polymer, and conversion of monomer  $ (\text{—}) $</div>


<div style="text-align: center;">Neglecting any type of gel-effect first, we simulate the system with  $ k_t = 3 \cdot 10^7 $ up to about 52% conversion of monomer ( $ t = 150000 $ s). The resulting molecular weight distribution  $ D_s $ has the dispersity index 2.77 (computed directly from the distribution) and is presented as  $ w(\log M) $-distribution ( $ D_s \cdot s \cdot s $, comparable to gel permeation chromatography) in Fig. 5 (dotted line). Note that more than 50000 size classes had to be resolved. For this model the discrete h-p-method used about 120 degrees of freedom (for both distributions  $ P_s $ and  $ D_s $), a computing time (CPU) of about 10 minutes on a Pentium 90 MHz Computer (32 bit program) was necessary to simulate the complete dynamic process. In order to show how sensitive the algorithm works, the straight line in Fig. 5 shows the result of the same model, but with a slight gel-effect model of the form</div>


 $$ k_{\mathrm{t}}=k_{\mathrm{t,0}}\exp(-X_{\mathrm{M}})\qquad,\quad X_{\mathrm{M}}\mathrm{m o n o m e r c o n v e r s i o n} $$ 

In the next step, we replace the constant termination coefficient  $ k_{t} $ by the function

 $$ k_{\mathrm{t}}^{\mathrm{s},\mathrm{r}}=k_{\mathrm{t}}(s,r)=\frac{k_{\mathrm{t},0}}{(s+r)^{\alpha}}\qquad\quad\alpha=0.4\qquad\quad k_{\mathrm{t},0}=5\cdot10^{8} $$ 

which is chosen such that we obtain nearly the same time-conversion graph as before. Actually, there are many models for  $ k_{t}(s, r) $ in discussion and the h-p-algorithm has