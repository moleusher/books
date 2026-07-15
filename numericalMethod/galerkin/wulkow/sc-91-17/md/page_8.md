Proof. For  $ u \in H_{\rho-\varepsilon,0} $ we have by definition

 $$ \sum_{s=1}^{\infty}u(s)^{2}\;e^{(\lambda+\bar{\varepsilon})s}\;<\;\infty\;, $$ 

writing  $ \rho = e^{-\lambda} $,  $ \rho - \varepsilon = e^{-\lambda - \bar{\varepsilon}} $ in terms of  $ \lambda > 0 $,  $ \bar{\varepsilon} > 0 $. Then there is an  $ \bar{s} \geq 1 $ with

 $$ e^{(\lambda+\bar{\varepsilon})s}>p(s)^{2}\;e^{\lambda s} $$ 

for all s >  $ \bar{s} $. Thus  $ \|pu\|_{\rho,0} $ is bounded, if

 $$ \sum_{s=1}^{\infty}u(s)^{2}p(s)^{2}e^{\lambda s}\leq\sum_{s=1}^{\bar{s}}u(s)^{2}p(s)^{2}e^{\lambda s}+\sum_{s=\bar{s}+1}^{\infty}u(s)^{2}e^{(\lambda+\bar{s})s}<\infty, $$ 

which is true for  $ u \in H_{\rho-\varepsilon,0} $. As

 $$ \binom{s-1+\alpha}{s-1}^{-1}\leq1,\alpha\geq0and\binom{s-1+\alpha}{s-1}^{-1}\leq\frac{s}{1+\alpha},-1<\alpha<0, $$ 

we get  $ u \in H_{\rho,\alpha} $ and  $ p u \in H_{\rho,\alpha} $ for all  $ \alpha > -1 $.

With Lemma 1.2 we can prove the important

COROLLARY 1.3. If  $ u \in H_{\rho-\varepsilon,\alpha} $ for one  $ \alpha > -1 $, then  $ u \in H_{\rho,\beta} $ for all  $ \beta > -1 $.

Proof. For  $ \beta \geq \alpha $ see (1.12). For  $ \beta < \alpha $ the inequality

 $$ \binom{s-1+\alpha}{s-1}\binom{s-1+\beta}{s-1}^{-1}\leq p(s)^{2} $$ 

holds by use of a polynomial $p$ with degree $j \geq (\alpha - \beta)/2$. Application of Lemma 1.2 leads to the assertion.

Remark. The condition  $ u \in H_{\rho-\varepsilon,\alpha} $ plays an important role in this work. Under numerical aspects it ensures, that we do not approximate an element at the ‘edge’ of the space  $ H_{\rho,\alpha} $. Corollary 1.3 implies, that on this condition the  $ \rho- $ scale is the crucial scale for the theory, whereas the  $ \alpha- $ scale gives some freedom for approximation purposes.

Example 1.4. Let  $ \rho $ be given. Define  $ u(s):=\left(\sqrt{\rho}\right)^{s-1}/s $,  $ s\geq1 $. Then

 $$ ||u||_{\rho,0}^{2}=\frac{1}{1-\rho}\sum_{s=1}^{\infty}\frac{1}{s^{2}}<\infty, $$ 

but  $ \sum_{s=1}^{\infty} u(s)^2 \Psi_{\bar{\rho},0}(s)^{-1} $ is not bounded for any  $ \bar{\rho} < \rho $. For  $ v(s) := s u(s) $ we see that  $ v \notin H_{\rho,0} $. This confirms, that the assumption of Lemma 1.2 and Corollary 1.3 concerning  $ \rho $ is necessary.