### 2.2 PROPERTIES OF THE POLYNOMIALS

The approximation of solutions of countable systems in a most suited space requires the transformation of a given representation of  $ u \in H_{\rho,\alpha} $ to a basis expansion in a space  $ H_{\bar{\rho},\bar{\alpha}} $ (see also Section 3.3). We start with transformations with respect to the parameter  $ \rho $.

LEMMA 2.2. The transformation between the polynomial systems  $ \{l_j(s;\rho,\alpha)\} $ and  $ \{l_j(s;\bar{\rho},\alpha)\} $ can be expressed by

 $$ \begin{array}{r c l}{l_{j}(s;\bar{\rho},\alpha)}&{=}&{\displaystyle\sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})\:l_{k}(s;\rho,\alpha)\quad,\quad0<\bar{\rho}<1\quad,}\\ {d_{\alpha}^{j,k}(\rho,\bar{\rho})}&{:=}&{\displaystyle\frac{(\bar{\rho}-\rho)^{j-k}}{(1-\rho)^{j}}\left(1-\bar{\rho}\right)^{k}\left(\frac{j+\alpha}{j-k}\right)\quad,\quad j\geq k\geq0\quad.}\\ \end{array} $$ 

Proof. After inserting the series representation (2.5) of the  $ l_k(s; \rho, \alpha) $ and the definition of the  $ d_{\alpha}^{j,k}(\rho, \bar{\rho}) $ a reordering of the summations leads to

 $$ \begin{array}{r l}{\displaystyle\sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})\:l_{k}(s;\rho,\alpha)=\left(\frac{\bar{p}-\rho}{1-\rho}\right)^{j}}&{\displaystyle\sum_{k=0}^{j}\left(\frac{\rho-1}{\rho}\right)^{k}\binom{s-1}{k}\binom{j+\alpha}{j-k}\times}\\ {\times}&{\displaystyle\sum_{\nu=k}^{j}\binom{j-k}{\nu-k}\left((\bar{\rho}-\rho)(1-\bar{\rho})\rho\right)^{\nu}\;.}\end{array} $$ 

With the relation  $ [36] $, p. 3)

 $$ \left(\begin{matrix}{j}\\ {\nu}\\ \end{matrix}\right)\left(\begin{matrix}{\nu}\\ {k}\\ \end{matrix}\right)=\left(\begin{matrix}{j}\\ {k}\\ \end{matrix}\right)\left(\begin{matrix}{j-k}\\ {\nu-k}\\ \end{matrix}\right) $$ 

and the Binomial theorem we end up with

 $$ \sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})l_{k}(s;\rho,\alpha)=\sum_{k=0}^{j}\binom{j+\alpha}{j-k}\binom{s-1}{k}(\bar{\rho}-1)^{k}\bar{\rho}^{j-k}=l_{j}(s;\bar{\rho},\alpha) $$ 

As a consequence of this lemma we note that

 $$ \frac{1}{\gamma_{k}^{\rho,\alpha}}\;(l_{j}(\bar{\rho},\alpha)\;,\;l_{k}(\rho,\alpha))^{\rho,\alpha}=d_{\alpha}^{j,k}(\rho,\bar{\rho}) $$ 

for  $ k \leq j $. For  $ k > j $ the scalar product is zero, of course.