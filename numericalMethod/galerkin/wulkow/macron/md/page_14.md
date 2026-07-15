• Test 1. In Table 2, estimated errors  $ \epsilon_{n} $ and true errors  $ \bar{\epsilon}_{n} $ are listed, which arise from the approximation of a (typical) distribution

 $$ u_{s}=\rho^{s}\cdot s~,\;\rho=0.95\;. $$ 

Here the moving weight function condition leads to the choice  $ \bar{\rho}=2\rho/(1+\rho) $. For example, from  $ \epsilon_{5} $ and  $ \epsilon_{8} $, we can expect with (2.3), that

 $$ \epsilon_{15}\approx\left(\frac{\epsilon_{8}^{10}}{\epsilon_{5}^{7}}\right)^{1/3}=2.8\cdot10^{-4} $$ 

— a value which indeed is nearly obtained. In Table 2, the predictions are based on the respective last two error estimations.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>n</td><td style='text-align: center; word-wrap: break-word;'>estimated error  $ \epsilon_{n} $</td><td style='text-align: center; word-wrap: break-word;'>true error  $ \bar{\epsilon}_{n} $</td><td style='text-align: center; word-wrap: break-word;'>prediction of  $ \epsilon_{n} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>2.3 \cdot 10^{-1}</td><td style='text-align: center; word-wrap: break-word;'>3.1 \cdot 10^{-1}</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6.7 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>7.6 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>1.3 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>1.4 \cdot 10^{-2}</td><td style='text-align: center; word-wrap: break-word;'>2.0 \cdot 10^{-2}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>3.9 \cdot 10^{-3}</td><td style='text-align: center; word-wrap: break-word;'>4.0 \cdot 10^{-3}</td><td style='text-align: center; word-wrap: break-word;'>4.4 \cdot 10^{-3}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>1.7 \cdot 10^{-4}</td><td style='text-align: center; word-wrap: break-word;'>1.7 \cdot 10^{-4}</td><td style='text-align: center; word-wrap: break-word;'>1.9 \cdot 10^{-4}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>6.7 \cdot 10^{-6}</td><td style='text-align: center; word-wrap: break-word;'>3.1 \cdot 10^{-6}</td><td style='text-align: center; word-wrap: break-word;'>7.4 \cdot 10^{-6}</td></tr></table>

<div style="text-align: center;">Table 2: Behavior of error, Test 1</div>


As a rule of thumb we can say, that whenever the error (estimates) behaves that regular, the user may expect to get reliable approximations.

The α-check (based on the extended weight function (1.3)) leads in this case to

 $$ \bar{\rho}=0.95\mathrm{a n d}\bar{\alpha}=1, $$ 

corresponding to the fact, that the distribution  $ u_s $ can be written as  $ C \cdot \Psi_{0.95,1}(s) $.

● Test 2. We try to approximate a Poisson-distribution having a maximum at index s = 50:

 $$ u_{s}=e^{-\lambda}\frac{\lambda^{s-1}}{(s-1)!},\lambda=50 $$ 

Table 3 shows that the true error  $ \bar{\epsilon}_n $ decreases very slowly, the error estimates are in the right scale, but predictions on the bases of the estimates  $ \epsilon_n $ are not reasonable. There is especially no monotony of the  $ \epsilon_n $. In a real simulation we would not know a priori the form of the true distribution and in order to find