In [36, 34], a two-parameter family of polynomials has been designed to be associated with the two-parameter weight function

 $$ \begin{array}{r c l}{\psi(x)}&{=}&{(1-\alpha)^{1+\beta}\left(\begin{matrix}{x_{i}+\beta}\\ {x}\\ \end{matrix}\right)\alpha^{x},}&{0<\alpha<1,\beta>-1.}\\ \end{array} $$ 

All these choices need to be combined with the so-called “moving weight function” condition that roughly requires the solution to be “similar to the weight function in some prescribed sense, see [10] for general weight function and [13] for the special case. As a consequence, the thus constructed global Galerkin methods are well-suited for monomodal solutions, but less appropriate to bimodal functions, which, however, do arise in important applications. For that reason, Wulkow [34] turned to localized unweighted polynomials, discrete Chebychev polynomials formally corresponding to the weight function

 $$ \psi(x)\quad\equiv\quad1\;. $$ 

It is this latter setting which paved the way to the extreme success of discrete Galerkin methods in polymer chemistry. On this basis, we will suggest the same choice for the CME context—to be treated in the next section for more than one spatial dimension.

Spatial error estimation. Recall the type of global expansion (1.4) for the exact solution p and (1.5) for the Galerkin approximation  $ p_r $. Of course, we will choose the induced Hilbert space norm to get an error estimate  $ \|p_r - p\|_{\psi} $. If the coefficients  $ \{a_k\} $ are independent of the truncation index r, we obtain the exact expression

 $$ \begin{array}{r c l}{\displaystyle\|p_{r}-p\|_{\psi}}&{=}&{\displaystyle\left\|\displaystyle\sum_{k=r+1}^{\infty}a_{k}q_{k}(x;\rho)\right\|_{\psi}=\left(\displaystyle\sum_{k=r+1}^{\infty}|a_{k}|^{2}\gamma_{k}\right)^{1/2}.}\\ \end{array} $$ 

Otherwise, which is the typical case, a straightforward modification can be applied, see [10]. Since, in this norm, the expansion coefficients tend to zero for  $ k \to \infty $, the following spatial error estimate may serve the purpose

 $$ \mathrm{e p s}_{r}=\|p_{r+1}-p_{r}\|_{\psi}=|a_{r+1}|\sqrt{\gamma_{r+1}}. $$ 

Clearly, this error estimate will work fine whenever the expansion coefficients decrease sufficiently fast. Otherwise, the expansion has to be continued a few steps beyond the step  $ r + 1 $.