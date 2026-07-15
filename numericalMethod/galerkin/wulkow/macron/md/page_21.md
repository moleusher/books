<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>PERCENT. CONVERSION ( * E+02 )</th><th style='text-align: center;'>DISPERSITY ( * E+01 ) (Solid)</th><th style='text-align: center;'>DISPERSITY ( * E+01 ) (Dashed)</th><th style='text-align: center;'>DISPERSITY ( * E+01 ) (Dotted)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.150</td><td style='text-align: center;'>0.150</td><td style='text-align: center;'>0.150</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.235</td><td style='text-align: center;'>0.240</td><td style='text-align: center;'>0.250</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.210</td><td style='text-align: center;'>0.255</td><td style='text-align: center;'>0.265</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>0.180</td><td style='text-align: center;'>0.265</td><td style='text-align: center;'>0.275</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.160</td><td style='text-align: center;'>0.270</td><td style='text-align: center;'>0.280</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.145</td><td style='text-align: center;'>0.270</td><td style='text-align: center;'>0.285</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0.135</td><td style='text-align: center;'>0.265</td><td style='text-align: center;'>0.290</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>0.128</td><td style='text-align: center;'>0.255</td><td style='text-align: center;'>0.295</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.122</td><td style='text-align: center;'>0.240</td><td style='text-align: center;'>0.300</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0.118</td><td style='text-align: center;'>0.225</td><td style='text-align: center;'>0.305</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.115</td><td style='text-align: center;'>0.210</td><td style='text-align: center;'>0.310</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6: Dispersity of  $ P_iX $ for reaction constants  $ k_f = 10^{-2} $ (—),  $ 10^{-3} $ (—-),  $ 10^{-4} $ (…) and  $ 10^{-5} $ (− · -) versus percentage conversion of the monomer M</div>


and the remaining two polymer species  $ P_iX $,  $ P_i $ were considered only for short time calculations ( $ t \leq 10s $) with maximal chain length  $ i_{\max} $ up to  $ i_{\max} = 500 $. For long time calculations (10 - 5000s) the restriction  $ i_{\max} \leq 200 $ was used, because the computing time is proportional to  $ i_{\max}^2 $.

With the constants of Table 1 in [9] the MACRON input for the reaction system (3.1) has the form presented in Table 5. Note that the first member of each polymer species is not handled as part of a distribution, but as ordinary chemical species. In this manner different values for  $ k_p(1) $ and  $ k_p(i) = k_p $ for  $ i \geq 2 $ can be chosen. The  $ D_i $ are considered separately for every index i.

First we discuss the properties of main chemical interest, i.e. the average molecular weight (defined in [9] as conversion/number of all polymer chains) and the polydispersity of the mainly built polymer species  $ P_i X $. With regard to that, it is sufficient to use only two expansion coefficients for each polymer species (see Section 2.2). It is especially interesting to study these quantities in dependency to the rate constant  $ k_f(i) = k_f $, which in turn depends on the