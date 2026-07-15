COROLLARY 1.4. If  $ u \in H_{\rho-\varepsilon,\alpha} $ for one  $ \alpha > -1 $, then  $ u \in H_{\rho,\beta} $ for all  $ \beta > -1 $.

The condition  $ u \in H_{\rho-\varepsilon,\alpha} $ plays an important role in this work. Under numerical aspects it ensures, that we do not approximate an element at the ‘edge’ of the space  $ H_{\rho,\alpha} $. Corollary 1.4 implies, that on this condition the  $ \rho $-scale is the crucial scale, whereas the  $ \alpha $-scale can be used for approximation purposes.

Proof of Corollary 1.4. For  $ \beta \geq \alpha $ see Theorem 1.2.(ii). For  $ \beta < \alpha $ the estimation

 $$ \binom{s-1+\alpha}{s-1}\binom{s-1+\beta}{s-1}^{-1}\leq p(s)^{2} $$ 

holds by use of a polynomial $p$ with degree $j \geq (\alpha - \beta)/2$. Application of Lemma 1.3 leads to the assertion.

Example 1.5. Let  $ \rho $ be given. Define  $ u(s):=\left(\sqrt{\rho}\right)^{s-1}/s $,  $ s\geq1 $. Then

 $$ \left\|u\right\|_{\rho,0}^{2}=\frac{1}{1-\rho}\sum_{s=1}^{\infty}\frac{1}{s^{2}}<\infty, $$ 

but  $ \sum_{s=1}^{\infty} u(s)^2 \Psi_{\bar{\rho},0}(s)^{-1} $ is not bounded for any  $ \bar{\rho} < \rho $. For  $ v(s) := s u(s) $ we see that  $ v \notin H_{\rho,0} $. This confirms, that the assumption of Lemma 1.3 and Corollary 1.4 concerning  $ \rho $ is necessary.

COROLLARY 1.5. For  $ k = 0, 1, \ldots $, the statistical moments  $ \mu_k[u] $ of  $ u $ are defined by

 $$ \mu_{k}[u]:=\sum_{s=1}^{\infty}s^{k}u(s)~. $$ 

For  $ u \in H_{\rho,\alpha} $ all statistical moments of  $ u $ are bounded.

Proof.

 $$ \begin{array}{r c l}{\displaystyle\sum_{s=1}^{\infty}s^{k}u(s)}&{=}&{\displaystyle\sum_{s=1}^{\infty}s^{k}\Psi_{\rho,\alpha}(s)u(s)\Psi_{\rho,\alpha}(s)^{-1}=\left(s^{k}\Psi_{\rho,\alpha}\;,\;u\right)_{\rho,\alpha}\leq}\\ {}&{\leq}&{\|s^{k}\Psi_{\rho,\alpha}\|_{\rho,\alpha}\|u\|_{\rho,\alpha}=\mu_{2k}[\Psi_{\rho,\alpha}]\|u\|_{\rho,\alpha}<\infty\;,}\\ \end{array} $$ 

using the Cauchy–Schwarz inequality and the fact that all statistical moments of  $ \Psi_{\rho,\alpha} $ are bounded. Corollary 1.5 supplies a nice property of the spaces  $ H_{\rho,\alpha} $ and goes with the considerations in Example 1.2.