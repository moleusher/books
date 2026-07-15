Proof.

(i) This is clear from the theory of weighted sequence spaces (e.g. [11]).

(ii) The inclusions follow from the definitions of the weight function  $ \Psi_{\rho,\alpha} $ and the norms  $ \|\cdot\|_{\rho,\alpha} $. The estimates (1.32) and (1.33) can be calculated essentially using the definition of the normalizing constants  $ C^{\rho,\alpha} $. The embeddings are dense, since the set

 $$ M:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid u_{s}=0\mathrm{~f o r~a l l~b u t~f i n i t e l y~m a n y~}s\right\} $$ 

is dense in all spaces  $ H_{\rho,\alpha} $.

In order to clarify the role of the parameters  $ \rho $ and  $ \alpha $, properties of the  $ H_{\rho,\alpha} $ spaces will be summarized now.

LEMMA 1.3. For  $ 0 < \varepsilon < \rho < 1 $ let  $ u \in H_{\rho-\varepsilon,0} $. Then for all polynomials p of degree j we have  $ p \cdot u \in H_{\rho,\alpha} $ for  $ \alpha > -1 $.

Proof. From  $ u \in H_{\rho-\varepsilon,0} $ we have by definition

 $$ \sum_{s=1}^{\infty}u(s)^{2}\;e^{(\lambda+\bar{\varepsilon})s}\;<\;\infty\;, $$ 

if we write  $ \rho = e^{-\lambda} $,  $ \rho - \varepsilon = e^{-\lambda - \bar{\varepsilon}} $ in terms of  $ \lambda > 0 $,  $ \bar{\varepsilon} > 0 $. Then there is an  $ \bar{s} \geq 1 $ with

 $$ e^{(\lambda+\bar{\varepsilon})s}>p(s)^{2}e^{\lambda s} $$ 

for all  $ s > \bar{s} $. Thus  $ \|pu\|_{\rho,0} $ is bounded, if

 $$ \sum_{s=1}^{\infty}u(s)^{2}p(s)^{2}e^{\lambda s}\leq\sum_{s=1}^{\bar{s}}u(s)^{2}p(s)^{2}e^{\lambda s}+\sum_{s=\bar{s}+1}^{\infty}u(s)^{2}e^{(\lambda+\bar{\varepsilon})s} $$ 

is bounded. This is the case for  $ u \in H_{\rho-\varepsilon,0} $. As

 $$ \begin{pmatrix}s-1+\alpha\\ s-1\end{pmatrix}^{-1}\leq1\quad for\quad\alpha\geq0 $$ 

and

 $$ \begin{pmatrix}s-1+\alpha\\ s-1\end{pmatrix}^{-1}\leq\frac{s}{1+\alpha}\quad for\quad-1<\alpha<0 $$ 

we can derive  $ u \in H_{\rho,\alpha} $ and  $ pu \in H_{\rho,\alpha} $ for all  $ \alpha > -1 $.

With Lemma 1.3 we can prove the important