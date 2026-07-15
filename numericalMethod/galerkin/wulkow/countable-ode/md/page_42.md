which is an expansion of  $ \Delta_{\alpha}u $ in  $ H_{\rho,\alpha+1} $. Now induction leads to (2.43).

As a consequence of Corollary 2.12 we can easily compute  $ \|\Delta_\alpha^m u\|_{\rho,\alpha+m} $. Using the orthogonality of the polynomials  $ \{l_k(\rho,\alpha)\} $ we obtain

 $$ \left\|\Delta_{\alpha}^{m}u\right\|_{\rho,\alpha+m}^{2}=\sum_{k=m}^{\infty}a_{k}^{2}\left(1-\rho\right)^{2m}\gamma_{k-m}^{\rho,\alpha+m}<\infty\;. $$ 

The following definition prepares the proof of an approximation result.

DEFINITION 2.13. For  $ u \in H_{\rho,\alpha} $,  $ m \geq 1 $, define the m-th weighted difference norm  $ \|u\|_{\rho,\alpha,m} $ by

 $$ ||u||_{\rho,\alpha,m}^{2}:=\;||u||_{\rho,\alpha}^{2}+||\Delta_{\alpha}^{m}u||_{\rho,\alpha+m}^{2}\;. $$ 

For m = 0 set

 $$ ||u||_{\rho,\alpha,0}\;:=\;||u||_{\rho,\alpha}\;. $$ 

Remark. This norms can be regarded as discrete weighted Sobolev norms.

THEOREM 2.14. For  $ u \in H_{\rho,\alpha} $ and  $ n + 1 \geq m \geq 1 $ the approximation error  $ Q_n^{\rho,\alpha} $ can be estimated by

 $$ \left\|\mathcal{Q}_{n}^{\rho,\alpha}u\right\|_{\rho,\alpha}^{2}\leq\frac{\rho^{m}}{(1-\rho)^{2m}}\frac{(1+\alpha)(2+\alpha)\cdots(m+\alpha)}{(n+1)n\cdots(n+1-(m-1))}\left\|u\right\|_{\rho,\alpha,m}^{2}. $$ 

Proof. Inserting (2.44) we start with

 $$ \begin{array}{r l}{\|u\|_{\rho,\alpha,m}^{2}}&{=\displaystyle\sum_{k=0}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}+\displaystyle\sum_{k=m}^{\infty}a_{k}^{2}\left(1-\rho\right)^{2m}\gamma_{k-m}^{\rho,\alpha+m}}\\ {17)}&{\geq\displaystyle\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}\left[1+\frac{(1-\rho)^{2m}}{\rho^{m}}\frac{k(k-1)\ldots(k-m+1)}{(1+\alpha)\ldots(m+\alpha)}\right]\;,}\end{array} $$ 

using

 $$ \gamma_{k-m}^{\rho,\alpha+m}=\rho^{k-m}\binom{k+\alpha}{k-m}=\gamma_{k}^{\rho,\alpha}\rho^{-m}\frac{k(k-1)\dots(k-m+1)}{(1+\alpha)\dots(m+\alpha)}\;. $$ 

The norm of the projection error can be written as

 $$ \left\|\mathcal{Q}_{n}^{\rho,\alpha}u\right\|_{\rho,\alpha}^{2}=\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha} $$ 