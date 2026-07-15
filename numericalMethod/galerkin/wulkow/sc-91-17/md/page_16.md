COROLLARY 2.3. An element  $ u(s) \in H_{\rho,\alpha} $ with basis expansion

 $$ u(s)=\sum_{j=0}^{\infty}a_{j}(\rho,\alpha)\psi_{j}(s;\rho,\alpha)=\Psi_{\rho,\alpha}\sum_{j=0}^{\infty}a_{j}(\rho,\alpha)l_{j}(s;\rho,\alpha)\;, $$ 

which is also in the space $H_{\bar{p},\alpha}$, can be expressed in the $H_{\bar{p},\alpha}-$ basis in terms of the coefficients

 $$ a_{j}(\bar{\rho},\alpha)=\frac{1}{\bar{\rho}^{j}}\sum_{k=0}^{j}a_{k}(\rho,\alpha)\binom{j}{k}\frac{(\bar{\rho}-\rho)^{j-k}}{(1-\rho)^{j}}\left(1-\bar{\rho}\right)^{k}\rho^{k}. $$ 

Note that this transformation is independent of  $ \alpha $.

Proof. The projection of u to a basis element  $ \psi_{j}(\bar{\rho},\alpha)=\Psi_{\rho,\alpha}l_{j}(\bar{\rho},\alpha) $ can be written as

 $$ \frac{1}{\gamma_{j}^{\bar{\rho},\alpha}}\left(u,\psi_{j}(\bar{\rho},\alpha)\right)_{\bar{\rho},\alpha}=\frac{1}{\gamma_{j}^{\bar{\rho},\alpha}}\sum_{k=0}^{\infty}a_{k}(\rho,\alpha)\left(l_{k}(\rho,\alpha),l_{j}(\bar{\rho},\alpha)\right)^{\rho,\alpha} $$ 

Insertion of Lemma 2.2 in the form (2.9) and remembering in the definition of the  $ \gamma_{j}^{\rho,\alpha} $ leads to (2.10).

LEMMA 2.4. The transformation between the $\{l_j(s;\rho,\alpha)\}$ and the $\{l_j(s;\rho,\bar{\alpha})\}$ is given by

 $$ \begin{array}{r c l}{l_{j}(s;\rho,\bar{\alpha})}&{=}&{\displaystyle\sum_{k=0}^{j}d_{\rho}^{j,k}(\alpha,\bar{\alpha})\:l_{k}(s;\rho,\alpha)\;,\:\bar{\alpha}>-1\;,}\\ {d_{\rho}^{j,k}(\alpha,\bar{\alpha})}&{:=}&{\rho^{j-k}\:\binom{\bar{\alpha}-\alpha+j-k-1}{j-k}\;,\;j\geq k\geq0\;.}\\ \end{array} $$ 

Proof. Following the lines of the proof of Lemma 2.2 we insert the series expansion of  $ l_{j}(s;\rho,\alpha) $ into the series on the right-hand side of (2.11) and reorder the summations:

 $$ \sum_{k=0}^{j}d_{\rho}^{j,k}(\alpha,\bar{\alpha})\;l_{k}(s;\rho,\alpha)=\rho^{j}\sum_{\nu=0}^{j}\;\left(\frac{\rho-1}{\rho}\right)\;\binom{s-1}{\nu}\sum_{k=\nu}^{j}\binom{k+\alpha}{k-\nu}\binom{\bar{\alpha}-\alpha+j-k-1}{j-k}\;. $$ 

In order to show, that the inner sum is equal to  $ \binom{j+\bar{\alpha}}{j-\nu} $, we set  $ m = j - \nu $,  $ n = \bar{\alpha} - \alpha + j - \nu $,  $ p = \nu + \alpha $, and use relation (3b), p. 8, [36].

The transformation of coefficients  $ a_j(\rho, \alpha) $ of an  $ H_{\rho,\alpha} $-basis expansion to coefficients  $ a_j(\rho, \bar{\alpha}) $ of an  $ H_{\rho,\bar{\alpha}} $-expansion works analogue to Corollary 2.3 and is independent of  $ \rho $ in this case. This nice feature shows, how the two scales are separated.

Finally we prove two important shift properties of the discrete Laguerre polynomials.