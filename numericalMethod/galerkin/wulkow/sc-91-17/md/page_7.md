### 1.2 A Two-Parameter Scale of Hilbert Spaces

We construct weighted sequence spaces, which allow a theory of countable systems as well as an efficient numerical treatment of interesting problems.

DEFINITION 1.1. Define the weighted sequence spaces  $ H_{\rho,\alpha} $ by

 $$ H_{\rho,\alpha}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid||u||_{\rho,\alpha}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}\Psi_{\rho,\alpha}(s)^{-1}<\infty\right\}, $$ 

where the weight function  $ \Psi_{\rho,\alpha}(s) > 0 $ is given for  $ s \in \mathbb{N} $ by

 $$ \Psi_{\rho,\alpha}(s)=C^{\rho,\alpha}\left({}_{s-1}^{s-1+\alpha}\right)\rho^{s-1},0<\rho<1,\alpha>-1, $$ 

with the constant  $ C^{\rho,\alpha} = (1 - \rho)^{1+\alpha} $ chosen such that  $ \|\Psi_{\rho,\alpha}\|_{\rho,\alpha} = 1 $.

Remarks.

(i) Due to the normalization of the  $ \Psi_{\rho,\alpha} $, these weight functions can also be regarded as probability distributions. For  $ \alpha = 0 $ the weight function  $ \Psi_{\rho,\alpha} $ reduces to the geometric distribution. For  $ \alpha \gg 1 $, we obtain a narrow distribution; if we set  $ \alpha = \lambda/\rho $,  $ \Psi_{\rho,\lambda/\rho} $ converges pointwise to the Poisson distribution with parameter  $ \lambda $ for  $ \rho \to 0 $. A hyperbola of the form  $ 1/s^{\alpha} $ is approximated well by choosing  $ \alpha < 0 $ and  $ \rho $ close to one.

(ii) For  $ 0 < \rho < 1 $ and  $ \alpha > -1 $ the space  $ H_{\rho,\alpha} $ is equipped with the scalar product

 $$ (u,v)_{\rho,\alpha}:=\sum_{s=1}^{\infty}u(s)v(s)\Psi_{\rho,\alpha}(s)^{-1},u,v\in H_{\rho,\alpha}. $$ 

(iii) The embeddings

 $$ H_{\rho,\alpha}\hookrightarrow H_{\bar{\rho},\alpha}\quad,\quad0<\rho<\bar{\rho}<1\quad, $$ 

and

 $$ H_{\rho,\alpha}\hookrightarrow H_{\rho,\beta}\quad,\quad-1<\alpha<\beta\quad, $$ 

are dense and continuous.

LEMMA 1.2. For  $ 0 < \varepsilon < \rho < 1 $ let  $ u \in H_{\rho-\varepsilon,0} $. Then for all polynomials  $ p $ of degree  $ j $ we have  $ p \cdot u \in H_{\rho,\alpha} $ for  $ \alpha > -1 $.