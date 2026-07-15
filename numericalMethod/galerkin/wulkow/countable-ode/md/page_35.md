It is easily seen that this is the principle the modified discrete Laguerre polynomials with another normalization and a different lower summation bound in the scalar product. In fact, the  $ l_n(s;\rho,\alpha) $ are connected with the Meixner polynomials  $ m_n(s;\rho,\gamma) $ as given in [24] by

 $$ l_{n}(s;\rho,\alpha):=\frac{\rho^{n}}{n!}m_{n}(s-1;\rho,1+\alpha)\;, $$ 

which in turn can be expressed by means of the hypergeometric function

 $$ {}_{2}F_{1}(a,b,c;z):=\sum_{k=0}^{\infty}\frac{(a)_{k}(b)_{k}}{(c)_{k}k!}z^{k}\;, $$ 

such that

 $$ m_{n}(s;\rho,\gamma)=(1+\alpha)_{n\;2}F_{1}(-n,-s,\gamma;1-\frac{1}{\rho})\;. $$ 

For  $ \gamma = 1 + \alpha $ and with  $ s \to (s - 1) $ thus we have

 $$ \begin{array}{r c l}{l_{n}(s;\rho,\alpha)}&{=}&{\rho^{n}\frac{(1+\alpha)_{n}}{n!}\displaystyle\sum_{k=0}^{n}\frac{(-n)_{k}(-s+1)_{k}}{(1+\alpha)_{k}k!}\left(1-\frac{1}{\rho}\right)^{k}}\\ {}&{=}&{\displaystyle\sum_{k=0}^{n}\rho^{n-k}\left(\rho-1\right)^{k}\binom{n+\alpha}{n-k}\binom{s-1}{k}.}\\ \end{array} $$ 

This series representation is more convenient than  $ (2.11) $ and will be used in Section 2.2.

There are many properties of the several polynomials mentioned above, but we restrict ourselves to properties to be applied in the present context. Additional information about Meixner and related polynomials can be found in the literature referred to above. The modified discrete Laguerre polynomials with  $ \alpha = 0 $ have been used for the solution of CODE's in [18] and [9]. In [52], the parameter  $ \alpha $ already has been introduced in order to realize a discrete Galerkin method for certain so-called heterogeneous processes. Contrary to that, in this work the parameter  $ \alpha $ is used for extending the approximation properties of the suggested approach. An application in statistics (not associated to the discrete Galerkin method) is presented in [41].

An important tool for the generation of orthogonal polynomials is the three-term-recurrence relation. For the modified discrete Laguerre polynomials the recurrence is started with  $ l_{-1} = 0 $ and  $ l_{0} = 1 $. Using a relation for Meixner polynomials in [42], we obtain with (2.18):

 $$ \begin{array}{rcl}(2.22)^{\left(n+1\right)l_{n+1}(s;\rho,\alpha)}&=&[(n+\alpha+1)\rho+n-(1-\rho)(s-1)]l_{n}(s;\rho,\alpha)\\&&-(n+\alpha)\rho l_{n-1}(s;\rho,\alpha).\end{array} $$ 