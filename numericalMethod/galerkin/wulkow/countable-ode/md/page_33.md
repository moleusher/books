Proof. First we evaluate the difference on the right-hand side of  $ (2.9) $.

 $$ \Delta^{n}\left\{C^{\rho,\alpha}\rho^{s-1}\binom{s-1+\alpha}{s-1-n}\right\}=C^{\rho,\alpha}\sum_{k=0}^{n}\binom{n}{k}\left(-1\right)^{n-k}\rho^{s-1+k}\binom{s-1+k+\alpha}{s-1+k-n} $$ 

using the binomial theorem after representing  $ \Delta^{n} = (S_{+} - I)^{n} $ in terms of the forward shift operator  $ S_{+} $ and the identity operator I. As

 $$ \begin{pmatrix}s-1+k+\alpha\\ s-1+k-n\end{pmatrix}=\begin{pmatrix}s-1+\alpha\\ s-1\end{pmatrix}\frac{(s-1+k+\alpha)\cdots(s+\alpha)(s-1)\cdots(s-n+k)}{(1+\alpha)\cdots(n+\alpha)} $$ 

we obtain

 $$ l_{n}(s)=\sum_{k=0}^{n}\left(-1\right)^{n-k}\rho^{k}\left(\begin{array}{c}s-1+k+\alpha\\ k\end{array}\right)\left(\begin{matrix}s-1\\ n-k\end{matrix}\right), $$ 

which obviously is a polynomial of degree n.

 $$ (l_{m}\;,\;l_{n})^{\rho,\alpha}=0\;\mathrm{~f o r~}\;m\neq n\;, $$ 

In order to show that

assume n > m (for m > n the argumentation remains the same).

 $$ (l_{m}\;,\;l_{n})^{\rho,\alpha}=C^{\rho,\alpha}\;\frac{(1+\alpha)_{n}}{n!}\sum_{s=1}^{\infty}l_{m}(s)\;\Delta^{n}\;\left\{\rho^{s-1}\;\binom{s-1+\alpha}{s-1-n}\right\}\;, $$ 

where the Rodrigues formula has been inserted. From [42], p. 107, an iterated summation by parts formula

 $$ \begin{array}{r c l}{\displaystyle\sum_{s=A}^{s=B}f(s)\Delta^{n}g(s)}&{=}&{\displaystyle(-1)^{n}\displaystyle\sum_{s=A}^{s=B}g(s+n)\Delta^{n}f(s)}\\ {}&{+}&{\displaystyle\sum_{k=0}^{n-1}(-1)^{k}\Delta^{k}f(s)\Delta^{n-1-k}g(s+k)\bigg|_{s=A}^{s=B}}\\ \end{array} $$ 

can be derived for finite or infinite summation bounds A and B. Application of this formula to (2.12) yields

 $$ \begin{array}{r c l}{(l_{m},l_{n})^{\rho,\alpha}}&{=}&{(-1)^{n}C^{\rho,\alpha}\frac{(1+\alpha)_{n}}{n!}\displaystyle\sum_{s=1}^{\infty}\rho^{s-1+n}\binom{s-1+\alpha+n}{s-1}\Delta^{n}l_{m}(s)+}\\ {}&{+}&{C^{\rho,\alpha}\frac{(1+\alpha)_{n}}{n!}\displaystyle\sum_{k=0}^{n-1}(-1)^{k}\Delta^{k}l_{m}\;\Delta^{n-1-k}\left\{\rho^{s-1+k}\binom{s-1+k+\alpha}{s-1+k-n}\right\}\Bigg|_{s=1}^{\infty}.}\\ \end{array} $$ 