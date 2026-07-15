The first sum is equal to zero since  $ \Delta^n l_m(s) = 0 $ for  $ n > m $, in the second sum we look at the difference expression

 $$ \begin{array}{r l}&{\Delta^{n-1-k}\left\{\rho^{s-1-k}\binom{s-1+k+\alpha}{s-1+k-n}\right\}=}\\ {=}&{\sum_{\nu=0}^{n-1-k}\binom{n-1-k}{\nu}(-1)^{n-1-k-\nu}\rho^{s-1+k+\nu}\binom{s-1+k+\nu+\alpha}{s-1+k+\nu-n}\;.}\end{array} $$ 

The terms in this sum tend to zero for $s \to \infty$, because $0 < \rho < 1$. For $s = 1$ we have to consider $\binom{k+\nu+\alpha}{k+\nu-n}$, which is zero for $\nu \leq n-1-k$ and $\alpha > -1$. Now we compute the orthogonality factors

 $$ \gamma_{n}^{\rho,\alpha}=(l_{n}\;,\;l_{n})^{\rho,\alpha}\;. $$ 

For $n = m$ the second sum in (2.14) again can be seen to be zero, whereas for the evaluation of the first sum we need the difference $\Delta^n l_n(s)$. We use the fact that

 $$ \Delta^{n}s^{k}=0~,~k<n~\mathrm{a n d}~\Delta^{n}s^{n}=n!, $$ 

implying that in the series representation (2.11) only the coefficient of  $ s^{n} $ has to be considered, so that

 $$ \Delta^{n}l_{n}(s)=(\rho-1)^{n}\;. $$ 

From the normalization (2.1) of the weight function  $ \Psi_{\rho,\alpha} $ we know that

 $$ \sum_{s=1}^{\infty}\rho^{s-1}\binom{s-1+\alpha+n}{s-1}=\frac{1}{(1-\rho)^{1+\alpha+n}}\;. $$ 

Summarizing (2.14), (2.15), (2.16) we get the result

 $$ \left(l_{n},l_{n}\right)^{\rho,\alpha}=\rho^{n}\frac{\left(1+\alpha\right)_{n}}{n!}=\rho^{n}\begin{pmatrix}n+\alpha\\ n\end{pmatrix}. $$ 

The modified discrete Laguerre polynomials can be regarded as special Meixner polynomials. This can be seen by writing

 $$ \begin{pmatrix}s-1+\alpha\\ s-1\end{pmatrix}=\frac{\Gamma(s+\alpha)}{\Gamma(s)\Gamma(1+\alpha)} $$ 

in terms of the Gamma-function  $ \Gamma $. In [42] the Meixner polynomials are shown to be orthogonal with respect to the weight function

 $$ \Psi(s)=\frac{\rho^{s}\Gamma(\gamma+s)}{\Gamma(1+s)\Gamma(\gamma)},\gamma>0,0<\rho<1,s=0,1,\cdots. $$ 