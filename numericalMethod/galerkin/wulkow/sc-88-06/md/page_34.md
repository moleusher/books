are selected. From (4.22.b)  $ \rho $ can be seen to be independent from the truncation index N. So the error estimator (5.8) with (2.19) (replacing  $ P_{s}(t) $ by  $ N_{s}(t) $, of course) is compared with the true truncation error

 $$ \overline{{\epsilon}}_{N}:=\frac{\|\bar{N}_{s}^{(N)}-\bar{N}_{s}\|_{\Psi}}{\|\bar{N}_{s}\|_{\Psi}} $$ 

for varying N. The results are arranged in Table 1 showing that the error estimator is useful.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>truncation index  $ N $</td><td style='text-align: center; word-wrap: break-word;'>estimated error  $ \epsilon_{N} $</td><td style='text-align: center; word-wrap: break-word;'>true error  $ \bar{\epsilon}_{N} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.245</td><td style='text-align: center; word-wrap: break-word;'>0.387</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0.235</td><td style='text-align: center; word-wrap: break-word;'>0.295</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0.170</td><td style='text-align: center; word-wrap: break-word;'>0.195</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0.112</td><td style='text-align: center; word-wrap: break-word;'>0.124</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>0.070</td><td style='text-align: center; word-wrap: break-word;'>0.074</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>0.043</td><td style='text-align: center; word-wrap: break-word;'>0.042</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>0.026</td><td style='text-align: center; word-wrap: break-word;'>0.023</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>0.015</td><td style='text-align: center; word-wrap: break-word;'>0.012</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>0.008</td><td style='text-align: center; word-wrap: break-word;'>0.006</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0.003</td><td style='text-align: center; word-wrap: break-word;'>0.004</td></tr></table>

<div style="text-align: center;">Table 1: Comparison of estimated and true approximation error for the initial values (4.23)/(5.13) in the polymer degradation problem.</div>


In Figure 3, the time evolution of

 $$ P_{s}(t):=s\;N_{s}(t) $$ 

is plotted on the basis of the Galerkin-Laguerre approximation for $N=10$. The obtained error estimates for $N_{s}(t)$ were:

 $$ \begin{aligned}&\begin{aligned}\\ &\epsilon_{10}(0)&=&0.003\\&\epsilon_{10}(0.001)&=&0.002\\&\epsilon_{10}(0.01)&=&0.0004\\&\epsilon_{10}(0.1)&=&0.00001.\\ &\end{aligned}\\ \end{aligned} $$ 