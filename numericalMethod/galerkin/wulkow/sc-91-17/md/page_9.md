COROLLARY 1.4. Define for  $ k = 0, 1, \ldots $, the moments  $ \mu_k[u] $ of  $ u $ by

 $$ \mu_{k}[u]:=\sum_{s=1}^{\infty}s^{k}u(s)\;. $$ 

Then for  $ u \in H_{\rho,\alpha} $ all moments of  $ u $ are bounded.

Proof.

 $$ \sum_{s=1}^{\infty}s^{k}\;u(s)=\left(s^{k}\;\Psi_{\rho,\alpha}\;,\;u\right)_{\rho,\alpha}\leq\mu_{2k}[\Psi_{\rho,\alpha}||u||_{\rho,\alpha}<\infty\;, $$ 

using the Cauchy–Schwarz inequality and the fact that all moments of  $ \Psi_{\rho,\alpha} $ are bounded.

The following results are important for the treatment of certain nonlinear operators (e.g. the convolution operator in Example 1.6). We only consider the case  $ \alpha = 0 $ here. For  $ \alpha \neq 0 $ the constants become a little bit more complicated. The proofs are straightforward and can be found in [39].

LEMMA 1.5. For  $ 0 < \varepsilon < \rho $ it is  $ \Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}},0} \in H_{\rho-\varepsilon,0} $ and

 $$ \|\Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}},0}\|_{\rho-\varepsilon,0}=\frac{1}{\sqrt{\varepsilon}}\;M_{\rho,\varepsilon}\;,\;M_{\rho,\varepsilon}:=\frac{(\sqrt{\rho}-\rho+\varepsilon)}{\sqrt{(1-\rho+\varepsilon)}} $$ 

COROLLARY 1.6. For  $ u \in H_{\rho-\varepsilon,0} $,  $ 0 < \varepsilon < \rho $, the following inequality holds:

 $$ \sum_{s=1}^{\infty}u(s)\;\Psi_{\sqrt{\rho},0}(s)^{-1}\leq\frac{1}{\sqrt{\varepsilon}}\;\bar{M}_{\rho,\varepsilon}\left\|u\right\|_{\rho-\varepsilon,0}\;, $$ 

with a constant

 $$ \bar{M}_{\rho,\varepsilon}:=\frac{(\rho(1-\rho+\varepsilon))^{1/2}}{1-\sqrt{\rho}}\;. $$ 

### 1.3 Theory of Countable Systems

Mathematical theory concerning countable systems has been developed for many years, a survey is given in the monograph of DEIMLING [13]. In contrary to the most authors, which e.g. put conditions on linear countable systems, which are formulated as infinite matrix equations in an $l^{p}$-space, we will take a different view. The present approach is motivated by the qualitative behavior of the solutions and their efficient approximation. It turns out, that the operators studied here are Lipschitz continuous as operators on a fixed $H_{\rho,\alpha}$ - space or on the scale of these spaces.