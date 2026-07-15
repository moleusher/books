LEMMA 2.5. The transformation between  $ l_{j}(s;\rho,\alpha) $ and  $ l_{j}(s;\rho,\bar{\alpha}) $ is given by

 $$ \begin{array}{r c l}{l_{j}(s;\rho,\bar{\alpha})}&{=}&{\displaystyle\sum_{k=0}^{j}d_{\rho}^{j,k}\big(\alpha,\bar{\alpha}\big)l_{k}(s;\rho,\alpha),\bar{\alpha}>-1,}\\ {d_{\rho}^{j,k}\big(\alpha,\bar{\alpha}\big)}&{:=}&{\rho^{j-k}\binom{\bar{\alpha}-\alpha+j-k-1}{j-k},j\geq k\geq0.}\\ \end{array} $$ 

Proof. Following the lines of the proof of Lemma 2.2 we insert the series expansion of $l_{j}(s;\rho,\alpha)$ into the series on the right-hand side of (2.29) and reorder the summations:

 $$ \sum_{k=0}^{j}d_{\rho}^{j,k}(\alpha,\bar{\alpha})l_{k}(s;\rho,\alpha)=\rho^{j}\sum_{\nu=0}^{j}\left(\frac{\rho-1}{\rho}\right)\binom{s-1}{\nu}\sum_{k=\nu}^{j}\binom{k+\alpha}{k-\nu}\binom{\bar{\alpha}-\alpha+j-k-1}{j-k} $$ 

If we can show that the inner sum is equal to  $ \binom{j+\bar{\alpha}}{j-\nu} $ we will be finished. By setting  $ m = j - \nu $,  $ n = \bar{\alpha} - \alpha + j - \nu $,  $ p = \nu + \alpha $, we can use a relation from [46], p. 10, which is given there only for natural numbers but can be extended easily to real n and p. Then

 $$ \sum_{k=0}^{m}\binom{p+k}{k}\binom{n-k-1}{m-k}=\binom{n+p}{m}=\binom{j+\bar{\alpha}}{j-\nu}. $$ 

The transformation of coefficients  $ a_j(\rho, \alpha) $ of an  $ H_{\rho,\alpha} $-basis expansion to coefficients  $ a_j(\rho, \bar{\alpha}) $ of an  $ H_{\rho,\bar{\alpha}} $-expansion works analogue to Corollary 2.3 and is independent of  $ \rho $ in this case. This nice feature shows how the two scales are separated. A differentiation formula can be derived similar to Corollary 2.4:

COROLLARY 2.6. The derivative of the $l_{j}(s;\rho,\alpha)$ with respect to $\alpha$ can be expressed by

 $$ \frac{\partial l_{j}(s;\rho,\alpha)}{\partial\alpha}=\sum_{\nu=0}^{j}\frac{\rho^{j-\nu}}{\left(j-\nu\right)}l_{\nu}(s;\rho,\alpha)~. $$ 

Proof. Application of the definition of the binomial coefficients.

Now we prove two important shift properties of the discrete Laguerre polynomials.