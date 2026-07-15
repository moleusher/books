 $ e_0, \ldots, e_{k-1} \in H_{\rho, \alpha} $, such that

 $$ p_{j k}(\tau_{i})=\mathcal{U}_{i1}\mathrm{~f o r~}i=j,j-1,\dots,j-k+1\;. $$ 

This can be done in  $ H_{\rho,\alpha} $, since the  $ e_j $ can be determined as linear combinations of the  $ \mathcal{U}_{i1} $, as we will see later on. Now extrapolation to  $ \tau \downarrow 0 $ leads to

 $$ \mathcal{U}_{j k}:=p_{j k}(0)=e_{0}\;\in H_{\rho,\alpha}\;. $$ 

The values  $ U_{jk} $ can easily be computed in the extrapolation table

 $$ \begin{array}{ccc}\mathcal{U}_{11}&&\\\downarrow&\searrow&\\\mathcal{U}_{21}&\rightarrow&\mathcal{U}_{22}\\\downarrow&&\downarrow\\\vdots&&\\\mathcal{U}_{k1}&\rightarrow&\cdots\quad\mathcal{U}_{k,k-1}\quad\rightarrow\quad\mathcal{U}_{kk}\end{array} $$ 

using the Aitken–Neville algorithm:  $ j \geq 2 $

 $$ \mathcal{U}_{j k}=\mathcal{U}_{j,k-1}+\frac{\mathcal{U}_{j,k-1}-\mathcal{U}_{j-1,k-1}}{\frac{n_{j}}{n_{j-k+1}}-1},\quad k=2,\ldots,j, $$ 

which can also be performed in  $ H_{\rho,\alpha} $.

The error  $ \|u(T) - \mathcal{U}_{jk}\|_{\rho,\alpha} $ will be examined in the following

THEOREM 4.1. For  $ u_0 \in H_{\rho,\alpha} $ we have

 $$ \epsilon_{j k}:=||u(T)-\mathcal{U}_{j k}||_{\rho,\alpha}\leq\gamma_{j k}T^{k+1}, $$ 

where asymptotically

 $$ \gamma_{j k}\doteq[n_{j-k+1}\dots n_{j}]^{-1}C~, $$ 

C depending on the problem, on the initial value and on F.

Proof. Follows as usual from Theorem 1.13. For instance take the proof of Theorem II. 9.1 in [27].

By these remarks and the fact that in general  $ \gamma_{jk} $ decreases for increasing k we see, that the assumption

 $$ \epsilon_{j,k+1}\leq c\epsilon_{j k},\quad c<1, $$ 