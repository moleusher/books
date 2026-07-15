LEMMA 2.10. For  $ s \geq 1 $ we have

 $$ (2.34)\sum_{r=1}^{s-1}l_{k}(r)l_{j}(s-r)=\frac{1}{1-\rho}\left[\rho l_{k+j}(s)-l_{k+j+1}(s)\right],l_{k}(s)=l_{k}(s;\rho,0), $$ 

Proof. Induction over s again.

### 2.3 APPROXIMATION PROPERTIES

Let  $ u \in H_{\rho,\alpha} $ be expanded in the orthogonal basis  $ \{\psi_k(\rho,\alpha)\} = \{\Psi_{\rho,\alpha} l_k(\rho,\alpha)\} $ of  $ H_{\rho,\alpha} $ by

 $$ u(s)=\Psi_{\rho,\alpha}(s)\sum_{k=0}^{\infty}a_{k}l_{k}(s;\rho,\alpha)\quad, $$ 

where the $\{l_k(\rho, \alpha)$} are the modified discrete Laguerre polynomials. The expansion coefficients $a_k$ can be expressed by

 $$ a_{k}=\frac{1}{\gamma_{k}^{\rho,\alpha}}\sum_{s=1}^{\infty}u(s)l_{k}(s;\rho,\alpha), $$ 

and it is well known by the Parseval equality that

 $$ ||u||_{\rho,\alpha}^{2}=\sum_{k=0}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}. $$ 

The orthogonal projection to the n - dimensional subspace

 $$ H_{\rho,\alpha}^{n}=\mathrm{s p a n}\left\{\psi_{0}(\rho,\alpha),\ldots,\psi_{n}(\rho,\alpha)\right\}\subset H_{\rho,\alpha} $$ 

is defined by

 $$ \begin{array}{r c l}{\mathcal{P}_{n}^{\rho,\alpha}u(s)}&{:=}&{\displaystyle\sum_{k=0}^{n}\frac{1}{\gamma_{k}^{\rho,\alpha}}\left(u,\psi_{k}(s;\rho,\alpha)\right)_{\rho,\alpha}\psi_{k}(\rho,\alpha)}\\ {}&{=}&{\displaystyle\Psi_{\rho,\alpha}(s)\sum_{k=0}^{n}a_{k}l_{k}(s;\rho,\alpha)\;.}\\ \end{array} $$ 

The projection error is easily seen to be

 $$ \mathcal{Q}_{n}^{\rho,\alpha}u(s):=u(s)-\mathcal{P}_{n}^{\rho,\alpha}u(s)=\Psi_{\rho,\alpha}(s)\sum_{k=n+1}^{\infty}a_{k}l_{k}(s;\rho,\alpha)\;. $$ 

Obviously we have  $ \|u - \mathcal{P}_n^\rho, \alpha \, u\|_{\rho, \alpha} \to 0 $ as  $ n \to \infty $ for all  $ u \in H_{\rho, \alpha} $ and  $ \|\mathcal{P}_n^\rho, \alpha\|_{\rho, \alpha} \leq 1 $. We want to estimate the norm of the projection error  $ \|\mathcal{Q}_n^\rho, \alpha \, u\|_{\rho, \alpha} $