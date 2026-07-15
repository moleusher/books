Example 3.2: Backward difference operator. We evaluate

 $$ \left(-\nabla u,\psi_{j}\right)_{\rho,\alpha}=-\sum_{s=1}^{\infty}u_{s}\triangle l_{j}(s)\;. $$ 

Then

 $$ \begin{array}{r c l}{(-\nabla u,\psi_{j})_{\rho,\alpha}}&{=}&{\displaystyle\sum_{k=0}^{\infty}a_{k}\displaystyle\sum_{\nu=0}^{j-1}(\rho-1)\rho^{j-1-\nu}\left(l_{\nu},l_{j}\right)^{\rho,\alpha}}\\ {}&{=}&{\displaystyle\frac{1-\rho}{\rho\binom{j+\alpha}{i}}\gamma_{j}^{\rho,\alpha}\displaystyle\sum_{k=0}^{j-1}a_{k}\binom{k+\alpha}{k}}\\ \end{array} $$ 

by use of (2.31), the orthogonality of the $l_{j}$ and the definition of $\gamma_{j}^{\rho,\alpha}$. With $\varphi = \sum_{k=0}^{\infty} b_{k} \psi_{k}$ the Galerkin equations for $(I + \tau \nabla)u = \varphi$ are

 $$ a_{j}+\tau\frac{1-\rho}{\rho\binom{j+\alpha}{j}}\sum_{k=0}^{j-1}a_{k}\binom{k+\alpha}{k}=b_{j},j=0,1,\cdots,n, $$ 

and can be solved recursively in this case. Generally, Gauss elimination has to be applied.

Error estimation. The numerical implementation of the discrete Galerkin method requires error estimations of the projection and the truncation error. A computable (and cheap) estimation of the projection error is available.

LEMMA 3.3. Define an error estimation  $ \varepsilon_{n} $ by

 $$ \varepsilon_{n}^{2}:=\|u^{n+1}-u^{n}\|^{2}=a_{n+1}^{2}\gamma_{n+1}^{\rho,\alpha}, $$ 

and assume that there exist C < 1 and  $ n_{0} \geq 1 $ such that for  $ n > n_{0} $ the relation

 $$ \varepsilon_{n+1}\leq C\varepsilon_{n} $$ 

holds. Then

 $$ \varepsilon_{n}\leq\bar{\varepsilon}_{n}\leq\left(\frac{1}{1-C^{2}}\right)^{1/2}\varepsilon_{n},n\geq n_{0}. $$ 

Proof. Obviously

 $$ \varepsilon_{n}^{2}\leq\bar{\varepsilon}_{n}^{2}=\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha} $$ 