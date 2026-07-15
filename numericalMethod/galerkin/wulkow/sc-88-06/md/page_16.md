(b) open systems.

Summarizing, it is computationally more reliable to determine a truncation index N in the discrete Galerkin method than in the statistical moment method. Of course, a sophisticated choice of the weight function  $ \Psi $ will help to decrease the number of terms needed.

Moving weight functions. The weight functions of special interest typically contain at least one free parameter — compare Section 4. A proper choice of this parameter will also help to keep the truncation index N small. For this purpose, define the statistical moments of  $ \Psi $ by

 $$ \nu_{k}:=\sum_{s=1}^{\infty}s^{k}\Psi(s)~=~\langle s^{k},\Psi\rangle\quad\equiv\quad(s^{k},1)\quad. $$ 

Note that a sufficient condition for the existence of an orthogonal polynomial basis for  $ \Psi $ is that all the  $ \nu_{k} $ are bounded.

Throughout the paper, the normalization

 $$ \nu_{0}:=1 $$ 

will be imposed — thus making  $ \Psi $ a probability density function. Then a sophisticated choice of  $ \Psi $ will aim at certain similarities between  $ P_s(t) $ and  $ \mu_0(t) $  $ \Psi(s) $. With (2.24), both distributions have  $ \mu_0(t) $ in common. The free parameter can then be determined from the natural condition

 $$ \mu_{1}(t)=\mu_{0}(t)\;\nu_{1}\;. $$ 

Example: Moving exponential weight function in the continuous model (Section 1.2).

In this case, one starts from the continuous inner product

 $$ (f,g):=\int\limits_{s=0}^{\infty}f(s)g(s)\Psi(s)ds $$ 

where  $ \Psi $, in view of (2.24) and (1.17), is defined as

 $$ \Psi(s):=\beta~e^{-\beta s}\quad,\quad\cdot\cdot\beta>0 $$ 

From this, one concludes that

 $$ \nu_{1}=\frac{1}{\beta}\:. $$ 