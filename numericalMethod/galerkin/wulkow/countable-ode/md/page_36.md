Finally a fundamental difference formula is taken from [42], serving as a basic relation in Section 2.2:

 $$ l_{n}(s+1;\rho,\alpha)-l_{n}(s;\rho,\alpha)=(\rho-1)l_{n-1}(s;\rho,\alpha+1)~. $$ 

Note that by  $ (2.23) $ the forward difference operator induces a shift in the  $ \alpha $ - scale.

### 2.2 BASIC PROPERTIES OF THE POLYNOMIALS

The approximation of solutions of infinite dimensional linear systems in a most suited space  $ H_{\rho,\alpha} $ requires transformations between the polynomial sets  $ \{l_j(s; \rho, \alpha)\} $ and  $ \{l_j(s; \bar{\rho}, \bar{\alpha})\} $ for  $ \alpha \neq \bar{\alpha} $,  $ \rho \neq \bar{\rho} $. Moreover, the weight function fitting condition derived in Section 3.2 has to be fulfilled. As it is more convenient, the transformation will be done for both parameters separately. We begin with the parameter  $ \rho $.

LEMMA 2.2. The transformation between  $  l_j(s; \rho, \alpha)  $ and  $  l_j(s; \bar{\rho}, \alpha)  $ can be expressed by

 $$ \begin{array}{r c l}{l_{j}(s;\bar{\rho},\alpha)}&{=}&{\displaystyle\sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})\:l_{k}(s;\rho,\alpha)\quad,\quad0<\bar{\rho}<1\quad,}\\ {d_{\alpha}^{j,k}(\rho,\bar{\rho})}&{:=}&{\displaystyle\frac{(\bar{\rho}-\rho)^{j-k}}{(1-\rho)^{j}}(1-\bar{\rho})^{k}\left(\begin{matrix}{j+\alpha}\\ {j-k}\\ \end{matrix}\right)\quad,\quad j\geq k\geq0\quad,}\\ \end{array} $$ 

Proof. After inserting the series representation (2.21) of the  $ l_k(s; \rho, \alpha) $ and the definition of the  $ d_{\alpha}^{j,k}(\rho, \bar{\rho}) $ a reordering of the summations leads to

 $$ \begin{array}{r l}{\displaystyle\sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})\:l_{k}(s;\rho,\alpha)=\left(\frac{\bar{\rho}-\rho}{1-\rho}\right)^{j}}&{\displaystyle\sum_{k=0}^{j}\left(\frac{\rho-1}{\rho}\right)^{k}\binom{s-1}{k}\binom{j+\alpha}{j-k}\times}\\ {\times}&{\displaystyle\sum_{\nu=k}^{j}\binom{j-k}{\nu-k}\left((\bar{\rho}-\rho)(1-\bar{\rho})\rho\right)^{\nu}\;.}\end{array} $$ 

With the relation  $ [46] $, p. 3)

 $$ \begin{pmatrix}j\\ \nu\end{pmatrix}\begin{pmatrix}\nu\\ k\end{pmatrix}=\begin{pmatrix}j\\ k\end{pmatrix}\begin{pmatrix}j-k\\ \nu-k\end{pmatrix} $$ 

and the Binomial theorem we end up (after a few manipulations) with

 $$ \sum_{k=0}^{j}d_{\alpha}^{j,k}(\rho,\bar{\rho})l_{k}(s;\rho,\alpha)=\sum_{k=0}^{j}\binom{j+\alpha}{j-k}\binom{s-1}{k}(\bar{\rho}-1)^{k}\bar{\rho}^{j-k}=l_{j}(s;\bar{\rho},\alpha) $$ 