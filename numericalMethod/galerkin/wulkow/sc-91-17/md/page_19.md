Proof. Repeated application of the difference relation  $ (2.7) $.

As a consequence of Corollary 2.8 we can easily derive, that

 $$ ||\Delta_{\alpha}^{m}u||_{\rho,\alpha+m}^{2}=\sum_{k=m}^{\infty}a_{k}^{2}\left(1-\rho\right)^{2m}\gamma_{k-m}^{\rho,\alpha+m}<\infty~. $$ 

DEFINITION 2.9. For  $ u \in H_{\rho,\alpha} $,  $ m \geq 1 $, define the m-th weighted difference norm  $ \|u\|_{\rho,\alpha,m} $ by

 $$ ||u||_{\rho,\alpha,m}^{2}:=\;||u||_{\rho,\alpha}^{2}+||\Delta_{\alpha}^{m}u||_{\rho,\alpha+m}^{2}\;. $$ 

For m = 0 set

 $$ ||u||_{\rho,\alpha,0}\;:=\;||u||_{\rho,\alpha}\;. $$ 

Remark. This norms can be considered as discrete weighted Sobolev norms.

THEOREM 2.10. For  $ u \in H_{\rho,\alpha} $ and  $ n+1 \geq m \geq 1 $ the approximation error  $ Q_n^{\rho,\alpha} $ can be estimated by

 $$ ||\mathcal{Q}_{n}^{\rho,\alpha}u||_{\rho,\alpha}\leq C(\rho,\alpha,m)M(n,m)||u||_{\rho,\alpha,m}, $$ 

with a constant

 $$ C(\rho,\alpha,m)^{2}=\frac{\rho^{m}}{(1-\rho)^{2m}}(1+\alpha)(2+\alpha)\cdots(m+\alpha) $$ 

and the term

 $$ M(n,m)^{2}=\frac{1}{(n+1)n\cdots(n-m+2)}, $$ 

describing the asymptotic behavior.

Proof. Inserting (2.18) we start with

 $$ \begin{array}{r l}{\|u\|_{\rho,\alpha,m}^{2}}&{=\displaystyle\sum_{k=0}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}+\displaystyle\sum_{k=m}^{\infty}a_{k}^{2}\left(1-\rho\right)^{2m}\gamma_{k-m}^{\rho,\alpha+m}}\\ &{\geq\displaystyle\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}\left[1+\frac{(1-\rho)^{2m}}{\rho^{m}}\frac{k(k-1)\ldots(k-m+1)}{(1+\alpha)\ldots(m+\alpha)}\right]\quad,}\end{array} $$ 

using

 $$ \gamma_{k-m}^{\rho,\alpha+m}=\rho^{k-m}\binom{k+\alpha}{k-m}=\gamma_{k}^{\rho,\alpha}\rho^{-m}\frac{k(k-1)\dots(k-m+1)}{(1+\alpha)\dots(m+\alpha)}\;. $$ 