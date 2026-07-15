is a reasonable choice, where  $ \kappa $ is a safety factor with a typical value of  $ \kappa = 10 $. The expression (2.24) can be derived by applying the Chebyshev inequality of statistics to the probability, that  $ p(t, x) > \varepsilon $ with  $ \varepsilon > 0 $, and  $ x > x_{\max} $. Hence, effectively we have restricted the semi-infinite approximation problem to a finite approximation problem on  $ [0, x_{\max}] $. It is important to remark that  $ x_{\max} $ depends on the time evolution of the system and is not known a priori. For the discussion of a single time step in the context of the ROM, however, the value can be considered as known and fixed. The adaptation of  $ x_{\max} $ from time step to time step will be discussed in the next section.

It remains to characterize the Galerkin approximations on the finite intervals  $ I^{(m)} $ for  $ m = 1, \ldots, M $. Consider the orthogonal basis  $ \{T_k^{(m)} : k = 0, \ldots, (U^{(m)} - L^{(m)})\} $ of discrete Chebyshev polynomials satisfying

 $$ \left\langle T_{k}^{(m)},T_{j}^{(m)}\right\rangle_{I^{(m)}}=\sum_{x\in I^{(m)}}T_{k}^{(m)}(x)T_{j}^{(m)}(x)=\gamma_{j}^{(m)}\delta_{k,j}. $$ 

Then, we can represent  $ p(t) $ on  $ I^{(m)} $ in terms of the Chebyshev polynomials

 $$ p(t,x)=\sum_{k=0}^{U^{(m)}-L^{(m)}}a_{k}^{(m)}T_{k}^{(m)}(x). $$ 

For simplicity, we ignore the time-dependence of the coefficients and the polynomials and write  $ a_k^{(m)} $ and  $ T_k^{(m)}(x) $ instead of  $ a_k^{(m)}(t) $ and  $ T_k^{(m)}(t,x) $. Again the Galerkin approximation  $ p_r^{(m)}(t) $ to  $ p(t) $ on  $ I^{(m)} $ is defined by some suitable truncation of the above expansion

 $$ p_{r}^{(m)}(t,x)=\sum_{k=0}^{r}a_{k}^{(m)}T_{k}^{(m)}(x) $$ 

with polynomial order  $ r \leq U^{(m)} - L^{(m)} $, which in general will depend on  $ I_m $. The resulting error may be estimated by

 $$ \begin{array}{r l r}{\mathrm{e p s}_{r}^{(m)}}&{=}&{\|p_{r+1}^{(m)}(t)-p_{r}^{(m)}(t)\|_{I^{(m)}}=\left|a_{r+1}^{(m)}\right|\sqrt{\gamma_{r+1}^{(m)}}.}\end{array} $$ 

In brief, we summarize the resulting decomposition and polynomial approximations by the element-order pattern

 $$ \Delta_{1}=\left\{(I_{1},r_{1}),(I_{2},r_{2}),\ldots,(I_{M},r_{M})\right\}. $$ 