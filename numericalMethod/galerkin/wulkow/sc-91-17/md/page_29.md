Proof. For all  $ v \in H_{\rho,\alpha} $ and  $ p \in H_{\rho,\alpha}^l $ we may write

 $$ |f(v)|=|f(v+p)|\leq||f||_{\rho,\alpha}||v+p||_{\rho,\alpha} $$ 

and thus

 $$ |f(v)|\leq||f_{1}|_{\rho,\alpha}\operatorname*{i n f}_{p\in H_{\rho,\alpha}^{t}}||v+p||_{\rho,\alpha}\;. $$ 

The expression on the right-hand side can be estimated by

 $$ \operatorname*{i n f}_{p\in H_{\rho,\alpha}^{l}}||v+p||_{\rho,\alpha}=||v-\mathcal{P}_{l}^{\rho,\alpha}v||_{\rho,\alpha}\leq C(\rho,\alpha,m)\;M(l,m)\;||v||_{\rho,\alpha,m} $$ 

for  $ l+1 \geq m \geq 1 $ using Theorem 2.10.

LEMMA 3.6. For  $ w^n \in H_{\rho,\alpha}^n $ the summation error  $ E^l(u w^n \Psi_{\rho,\alpha}^{-1}) $,  $ l \geq n $, can be estimated by

 $$ |E^{l}(u w^{n}\Psi_{\rho,\alpha}^{-1})|\leq C_{S}\left\||w^{n}|\right|C(\rho,\alpha,m)\;M(l-n,m)\left\||u\|_{\rho,\alpha,m}\right., $$ 

where  $ C_{S} $ is a constant depending on the summation rule.

Proof. For fixed  $ w^n \in H_{\rho,\alpha}^n $ we define a linear form

 $$ \begin{array}{r l}{f:}&{{}H_{\rho,\alpha}\to\mathbb{R}\;,}\\ {}&{{}u\mapsto E^{l}(u w^{n}\Psi_{\rho,\alpha}^{-1})\;,}\\ \end{array} $$ 

which is continuous in $u$ and has the norm $C_S \|w^n\|$. Moreover we have $f(u) = 0$ for $u \in H_{\rho,\alpha}^{l-n}$. Then application of Lemma 3.5 gives the assertion.

Finally we insert Theorem 2.10 and Lemma 3.6 into (3.22) and obtain

THEOREM 3.7. If equation (3.21) is solved by applying a summation rule, which is exact in  $ H_{\rho,\alpha}^{l} $,  $ l \geq n $, the error of  $ u^{n,l} $ can be estimated by

 $$ \left\|u-u^{n,l}\right\|\leq C(\rho,\alpha,m)\left\|u\right\|_{\rho,\alpha,m}\left(M(n,m)+C_{S}M(l-n,m)\right). $$ 

Theorem 3.7 shows, that the summation formula has to be of order  $ l = 2n $, such that the pure and perturbed projection have the same asymptotic behavior. Thus we use a Gauss summation with  $ n + 1 $ nodes in  $ H_{\rho,\alpha}^n $ leading to

 $$ l=2n+1\;. $$ 

Theorem 3.7 also shows, that for fixed n

 $$ ||u^{n}-u^{n,l}||\to0\mathrm{~f o r~}l\to\infty. $$ 