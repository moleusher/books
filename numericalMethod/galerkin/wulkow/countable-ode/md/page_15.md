where the weight function  $ \Psi_{\rho,\alpha}(s) > 0 $ is given for  $ s \in \mathbb{N} $ by

 $$ \Psi_{\rho,\alpha}(s)=C^{\rho,\alpha}\binom{s-1+\alpha}{s-1}\rho^{s-1},0<\rho<1,\alpha>-1, $$ 

with the constant  $ C^{\rho,\alpha} = (1 - \rho)^{1+\alpha} $ chosen such that  $ \|\Psi_{\rho,\alpha}\|_{\rho,\alpha} = 1 $.

Remark. Due to the normalization of the  $ \Psi_{\rho,\alpha} $, these weight functions will be regarded as probability distributions. It will be pointed out in the introduction of Chapter 2 and in Section 3.2, that the family of distributions  $ \Psi_{\rho,\alpha} $ can approximate distributions with sharp peaks as well as broad distributions. In particular for  $ \alpha = 0 $ the weight function  $ \Psi_{\rho,\alpha} $ reduces to the geometric distribution

 $$ \Psi_{\rho}(s)=\left(1-\rho\right)\rho^{s-1},0<\rho<1, $$ 

used in [18], [9] in the context of the discrete Galerkin method. In this case we will omit the parameter  $ \alpha $. Note that

 $$ \Psi_{\rho,\alpha}\in H_{\bar{\rho},\alpha}\mathrm{~f o r~}\bar{\rho}>\rho^{2}. $$ 

THEOREM 1.2.

(i) For  $ 0 < \rho < 1 $ and  $ \alpha > -1 $ the space  $ H_{\rho,\alpha} $ equipped with the scalar product

 $$ (u,v)_{\rho,\alpha}:=\sum_{s=1}^{\infty}u(s)v(s)\Psi_{\rho,\alpha}(s)^{-1},u,v\in H_{\rho,\alpha}, $$ 

is a separable Hilbert space.

(ii) The embeddings

 $$ H_{\rho,\alpha}\hookrightarrow H_{\bar{\rho},\alpha}\quad{f o r\quad}0<\rho<\bar{\rho}<1; $$ 

and

 $$ H_{\rho,\alpha}\hookrightarrow H_{\rho,\beta}\quad{f o r\quad}-1<\alpha<\beta\;, $$ 

are dense and continuous with

 $$ \left\|u\right\|_{\rho,\beta}\leq(1-\rho)^{(\alpha-\beta)/2}\left\|u\right\|_{\rho,\alpha} $$ 

for  $ u \in H_{\rho,\alpha} $,  $ \beta \geq \alpha $ and

 $$ \|u\|_{\rho,\alpha}\leq\left(\frac{1-\bar{\rho}}{1-\rho}\right)^{(1+\alpha)/2}\|u\|_{\bar{\rho},\alpha} $$ 

for u ∈ Hₒ, α , ρ < ρ .