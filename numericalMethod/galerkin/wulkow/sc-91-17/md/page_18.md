and the Parseval equality yields

 $$ ||u||_{\rho,\alpha}^{2}=\sum_{k=0}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha}. $$ 

The orthogonal projection to the n - dimensional subspace

 $$ H_{\rho,\alpha}^{n}=\mathrm{s p a n}\left\{\psi_{0}(\rho,\alpha),\ldots,\psi_{n}(\rho,\alpha)\right\}\subset H_{\rho,\alpha} $$ 

is defined by

 $$ \mathcal{P}_{n}^{\rho,\alpha}u(s)=\Psi_{\rho,\alpha}(s)\sum_{k=0}^{n}a_{k}l_{k}(s;\rho,\alpha)\;. $$ 

The associated projection error is

 $$ \mathcal{Q}_{n}^{\rho,\alpha}\dot{u}(s):=u(s)-\mathcal{P}_{n}^{\rho,\alpha}u(s)=\Psi_{\rho,\alpha}(s)\sum_{k=n+1}^{\infty}a_{k}l_{k}(s;\rho,\alpha)\;. $$ 

Obviously we have  $ \|u - \mathcal{P}_n^{\rho,\alpha} u\|_p, \alpha \to 0 $ for  $ n \to \infty $ for all  $ u \in H_{\rho, \alpha} $ and  $ \|\mathcal{P}_n^{\rho,\alpha}\|_p, \alpha \leq 1 $. We want to estimate the norm of the projection error in terms of higher differences of  $ u $ (analogue to the use of higher derivatives in the continuous case), which should be a measure of the smoothness of  $ u $ in  $ H_{\rho, \alpha} $. In the polynomial spanned space  $ H^{\rho, \alpha} $ we could use the standard forward difference operator  $ \Delta $. Because  $ \Delta $ applied to  $ l_k(\rho, \alpha) $ shifts the  $ \alpha $-scale (2.7), the following definition seems to be natural in  $ H_{\rho, \alpha} $.

DEFINITION 2.7. Let for  $ u \in H_{\rho,\alpha} $ the weighted difference operator

 $$ \Delta_{\alpha}:H_{\rho,\alpha}\to H_{\rho,\alpha+1} $$ 

be defined by

 $$ \Delta_{\alpha}u=T_{\rho,\alpha+1}\Delta T_{\rho,\alpha}^{-1}u $$ 

in terms of the isomorphism  $ (2.2) $. Higher weighted differences are inductively given by

 $$ \Delta_{\alpha}^{m}u:=\Delta_{\alpha+m-1}\Delta_{\alpha+m-2}\ldots\Delta_{\alpha}u~. $$ 

COROLLARY 2.8. For  $ u \in H_{\rho,\alpha} $ with a representation (2.13) the m-th weighted higher difference can be written as

 $$ \Delta_{\alpha}^{m}u(s)=\Psi_{\rho,\alpha+m}(s)\sum_{k=0}^{\infty}a_{k+m}\left(\rho-1\right)^{m}l_{k}(s;\rho,\alpha+m)\;. $$ 