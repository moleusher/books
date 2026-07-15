The solution  $ u^n \in H_{\rho,\alpha}^n $ of the equation

 $$ (u^{n},v^{n})_{\rho,\alpha}=(u,v^{n})_{\rho,\alpha}\;,\;\forall v^{n}\in H_{\rho,\alpha}\;,\;u\in H_{\rho,\alpha}\;\mathrm{g i v e n}, $$ 

is just the projection  $ u^n = \mathcal{P}_n^{\rho,\alpha} u $. Let the perturbed projection  $ u^{n,l} $ be the solution of

 $$ (u^{n,l},v^{n})_{\rho,\alpha}^{l}=(u,v^{n})_{\rho,\alpha}^{l}\;\forall v^{n}\in H_{\rho,\alpha}\;, $$ 

where the index l characterizes a summation formula. Following estimates in the proof of the STRANG lemma ([11], Theorem 4.1.1), we can show that

 $$ \|u-u^{n,l}\|\leq M\left\|u-u^{n}\right\|+\sup_{w^{n}\in H_{\rho,\alpha}^{n}}\frac{\left|(u,w^{n})_{\rho,\alpha}-(u,w^{n})_{\rho,\alpha}^{l}\right|}{\left\|w^{n}\right\|}. $$ 

The error  $ E^{l}(f) $ of a numerical summation in  $ H_{\rho,\alpha} $ is given by

 $$ E^{l}(f)=\sum_{s=1}^{\infty}f(s)-\sum_{j=1}^{\overline{l}}\omega_{j}f(s_{j}) $$ 

where  $ \bar{l} $, the  $ s_j $ and the  $ \omega_j $ are chosen such that  $ E^l(f) = 0 $ for  $ f \in H_{\rho,\alpha}^l $. Thus the missing term in (3.22) is

 $$ |(u,w^{n})_{\rho,\alpha}-(u,w^{n})_{\rho,\alpha}^{l}|=|E^{l}(\frac{u w^{n}}{\Psi_{\rho,\alpha}})|~. $$ 

In order to get an estimate of this error, we prove an analogue to the Bramble-Hilbert lemma [8].

LEMMA 3.5. Let f be a continuous linear form on the space  $ H_{\rho,\alpha} $ with the property

 $$ \forall p\in H_{\rho,\alpha}^{l}\quad,\quad f(p)=0\quad. $$ 

Then with the expressions $C(\rho,\alpha,m)$ and $M(l,m)$ from Theorem 2.10 the following estimate holds:

 $$ \forall v\in H_{\rho,\alpha},\ |f(v)|\leq||f||\;C(\rho,\alpha,m)\;M(l,m)\;||v||_{\rho,\alpha,m} $$ 

for  $ l+1 \geq m \geq 1 $.