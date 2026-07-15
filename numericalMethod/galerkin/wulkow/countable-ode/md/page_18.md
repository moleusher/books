The following Lemma 1.6 and Corollary 1.7 concerning the weight function  $ \Psi_{\rho,\alpha} $ will be important for the treatment of the convolution operator (1.14) in Example 1.7 later on. We only consider the case  $ \alpha = 0 $ here. For  $ \alpha \neq 0 $ the constants become a little bit more complicated.

LEMMA 1.6. For  $ 0 < \varepsilon < \rho $ it is  $ \Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}},0} \in H_{\rho-\varepsilon,0} $ and

 $$ \left\|\Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}},0}\right\|_{\rho-\varepsilon,0}=\frac{1}{\sqrt{\varepsilon}}M_{\rho,\varepsilon},M_{\rho,\varepsilon}:=\frac{\left(\sqrt{\rho}-\rho+\varepsilon\right)}{\sqrt{(1-\rho+\varepsilon)}} $$ 

Proof. Omitting the  $ \alpha $ - scale in the notation we have

 $$ \begin{array}{r l}{\displaystyle\sum_{s=1}^{\infty}\Psi_{\frac{\rho-\epsilon}{\sqrt{\rho}}}(s)^{2}\Psi_{\rho-\epsilon}(s)^{-1}}&{=\frac{\left(C^{\frac{\rho-\epsilon}{\sqrt{\rho}}}\right)^{2}}{C^{\rho-\epsilon}}\displaystyle\sum_{s=1}^{\infty}\left(\frac{\rho-\varepsilon}{\rho}\right)^{s-1}}\\ &{=\frac{(\sqrt{\rho}-\rho+\varepsilon)^{2}}{\varepsilon(1-\rho+\varepsilon)}=\frac{1}{\varepsilon}M_{\rho,\varepsilon}^{2}\;,}\end{array} $$ 

using the normalizing constant  $ C^{\rho} = C^{\rho,0} $ from (1.27).

With Lemma 1.6 we can derive

Corollary 1.7. For  $ u \in H_{\rho-\varepsilon,0} $,  $ 0 < \varepsilon < \rho $, the following estimate holds:

 $$ \sum_{s=1}^{\infty}u(s)\;\Psi_{\sqrt{\rho},0}(s)^{-1}\leq\frac{1}{\sqrt{\varepsilon}}\;\bar{M}_{\rho,\varepsilon}\left\|u\right\|_{\rho-\varepsilon,0}\;, $$ 

with a constant

 $$ \bar{M}_{\rho,\epsilon}:=\frac{(\rho(1-\rho+\varepsilon))^{1/2}}{1-\sqrt{\rho}}\;. $$ 

This implies, that the weighted $l^2$ norm with parameter $\rho - \varepsilon$ can be replaced by a weighted $l^1$ norm with $\sqrt{\rho}$ for $u \in H_{\rho-\varepsilon}$.

Proof. Neglecting the  $ \alpha $ - dependency again,

 $$ \begin{array}{r c l}{\displaystyle\sum_{s=1}^{\infty}u(s)\Psi_{\sqrt{\rho}}(s)^{-1}}&{=}&{\displaystyle\frac{C^{\rho-\varepsilon}}{C^{\sqrt{\rho}}C^{\frac{\rho-\varepsilon}{\sqrt{\rho}}}}\sum_{s=1}^{\infty}u(s)\Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}}}(s)\Psi_{\rho-\varepsilon}(s)^{-1}}\\ {}&{\leq}&{\displaystyle\frac{C^{\rho-\varepsilon}}{C^{\sqrt{\rho}}C^{\frac{\rho-\varepsilon}{\sqrt{\rho}}}}\|\Psi_{\frac{\rho-\varepsilon}{\sqrt{\rho}}}\|_{\rho-\varepsilon}\left\|u\right\|_{\rho-\varepsilon}.}\\ \end{array} $$ 

Lemma 1.6 and careful insertion of the respective constants  $ C^{\rho,0} $ yield the result (1.37).