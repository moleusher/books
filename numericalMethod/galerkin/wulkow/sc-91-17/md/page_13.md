## 2 MODIFIED DISCRETE LAGUERRE POLYNOMIALS

In this section, an orthogonal basis of the spaces  $ H_{\rho,\alpha} $ is described in view of a Galerkin method in this spaces. The basis functions are given in terms of the modified discrete Laguerre polynomials. Important properties of these polynomials are presented in Section 2.2. The approximation of an element  $ u \in H_{\rho,\alpha} $ by the orthogonal basis is analyzed in Section 2.3. A Gauss summation in  $ H_{\rho,\alpha} $ is described in Section 2.4. As not stated otherwise, we always assume  $ 0 < \rho < 1 $ and  $ \alpha > -1 $.

### 2.1 CONSTRUCTION OF THE POLYNOMIALS

First, we try to find polynomials  $ \{l_{k}\} $, which are orthogonal with respect to the scalar product

 $$ (u\;,\;v)^{\rho,\alpha}:=\sum_{s=1}^{\infty}u(s)\;v(s)\;\Psi_{\rho,\alpha}(s)\quad, $$ 

where $u$, $v$ : $\mathbb{N} \to \mathbb{R}$ can be interpreted as sequences or as grid functions on $\mathbb{N}$. The isometric isomorphism

 $$ T_{\rho,\alpha}:H^{\rho,\alpha}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid(u,u)^{\rho,\alpha}<\infty\right\}\longrightarrow H_{\rho,\alpha} $$ 

defined by

 $$ (T_{\rho,\alpha}u)(s)=u(s)\;\Psi_{\rho,\alpha}(s) $$ 

Transforms the polynomial basis  $ \{l_k(\rho, \alpha)\} $ of  $ H^{\rho, \alpha} $ to the basis  $ \{\psi_k(\rho, \alpha)\} := \{\Psi_{\rho, \alpha} l_k(\rho, \alpha)\} $ of  $ H_{\rho, \alpha} $.

Fortunately the polynomials  $ l_{k}(\rho,\alpha) $ can be found in the literature, such that only special settings and properties have to be worked out here. We write the forward product as

 $$ \left(a\right)_{n}:=a\left(a+1\right)\cdots\left(a+n-1\right),\ a\in\mathbb{R}, $$ 

and denote the forward difference operator by

 $$ (\Delta\;u)_{s}=u_{s+1}-u_{s}\;,\;s=1,\;2,\ldots. $$ 

THEOREM 2.1.

(i) The Rodrigues formula

 $$ l_{n}(s;\rho,\alpha)=\frac{(1+\alpha)_{n}}{n!}\Psi_{\rho,\alpha}(s)^{-1}\Delta^{n}\left\{C^{\rho,\alpha}\rho^{s-1}\binom{s-1+\alpha}{s-1-n}\right\} $$ 