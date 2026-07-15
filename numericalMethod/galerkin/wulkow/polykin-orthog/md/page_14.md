Then (2.11) implies

 $$ \|\bar{P}_{s}^{(N)}-\bar{P}_{s}\|_{\Psi}=\operatorname*{m i n}_{\tilde{P}\in\Pi_{N}}\|\tilde{P}-\bar{P}_{s}\|_{\Psi}\;. $$ 

In this case, the associated approximation error can be represented by

 $$ \|\bar{P}_{s}^{(N)}-\bar{P}_{s}\|_{\Psi}=\left[\sum_{k=N+1}^{\infty}a_{k}^{2}(t)\gamma_{k}\right]^{1/2} $$ 

For any  $ \Psi $ such that (2.6) holds, one thus obtains for self-closing systems:

 $$ \operatorname*{l i m}_{N\to\infty}P_{s}^{(N)}(t)=P_{s}(t)\;. $$ 

For open systems, however, the situation is much more complicated. On the basis of (2.12), there the associated approximation error is

 $$ \|\bar{P}_{s}^{(N)}-\bar{P}_{s}\|_{\Psi}=\left[\sum_{k=0}^{N}\left(a_{k}^{(N)}-a_{k}\right)^{2}\gamma_{k}\doteq\sum_{k=N+1}^{\infty}a_{k}^{2}\gamma_{k}\right]^{1/2}. $$ 

A theoretical convergence analysis for this kind of approximation is beyond the scope of the present paper. A rather general scheme for such a convergence analysis may be found in DEIMLING [6]. In view of an algorithmic control of the truncation index N, the truncation error estimates

 $$ \|\bar{P}_{s}^{(N)}-\bar{P}_{s}^{(N+1)}\|_{\Psi}\doteq\left(a_{N+1}^{2}\gamma_{N+1}\right)^{1/2} $$ 

in the case  $ (2.11) $ or

 $$ \|\bar{P}_{s}^{(N)}-\bar{P}_{s}^{(N+1)}\|_{\Psi}\doteq\left[\sum_{k=0}^{N}\left(a_{k}^{(N)}-a_{k}^{(N+1)}\right)^{2}\gamma_{k}+\left(a_{N+1}^{(N+1)}\right)^{2}\gamma_{N+1}\right]^{1/2} $$ 

in the case  $ (2.12) $ might be useful.

### 2.2 Connection with Statistical Moments

Recall the definition (1.13) for the statistical moments  $ \mu_k(t) $, which is also based on the assumption of a discrete variable s. For given orthogonal basis  $ \{l_j(s)\} $, the following expansion is easily established:

 $$ s^{k}=\sum_{m=0}^{k}b_{k m}\;l_{m}(s)\quad,\quad k=0,1,\cdots. $$ 