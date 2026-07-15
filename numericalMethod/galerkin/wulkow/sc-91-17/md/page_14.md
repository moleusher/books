generates polynomials  $ l_{n}(s) = l_{n}(s; \rho, \alpha) $ which are orthogonal with respect to the scalar product (2.1) for  $ 0 < \rho < 1 $ and  $ \alpha > -1 $. The orthogonality relation reads

 $$ (l_{m}\;,\;l_{n})^{\rho,\alpha}=\delta_{n m}\;\gamma_{n}^{\rho,\alpha}\;,\;\gamma_{n}^{\rho,\alpha}:=\rho^{n}\;\binom{n+\alpha}{n}\;. $$ 

The polynomials  $ l_{n}(s;\rho,\alpha) $ will be called modified discrete Laguerre polynomials.

(ii) The polynomials  $  l_{n}(s; \rho, \alpha)  $ have a series representation

 $$ l_{n}(s;\rho,\alpha)=\sum_{k=0}^{n}\rho^{n-k}\left(\rho-1\right)^{k}\binom{n+\alpha}{n-k}\binom{s-1}{k}. $$ 

(iii) The three-term-recurrence for the modified discrete Laguerre polynomials is

 $$ \begin{array}{rcl}(n+1)l_{n+1}(s;\rho,\alpha)&=&[(n+\alpha+1)\rho+n-(1-\rho)(s-1)]l_{n}(s;\rho,\alpha)\\&&-(n+\alpha)\rho l_{n-1}(s;\rho,\alpha),\end{array} $$ 

started with  $ l_{-1}=0 $ and  $ l_{0}=1 $.

(iv) The forward difference operator  $ \Delta $ applied to  $ l_{n}(s;\rho,\alpha) $ induces a shift in the  $ \alpha $-scale:

 $$ (2.7)\Delta l_{n}(s;\rho,\alpha)=l_{n}(s+1;\rho,\alpha)-l_{n}(s;\rho,\alpha)=(\rho-1)\;l_{n-1}(s;\rho,\alpha+1)\;. $$ 

Proof. The only task is to find a formulation of results in the literature, which corresponds to the definition of  $ H^{\rho,\alpha} $ here. This is done in [39]. Basically, for part (i) results from [30] and [31] can be taken. The other parts are basing on [33], using that the modified discrete Laguerre polynomials are related to the Meixner polynomials  $ m_{n}(s;\rho,\gamma) $ as given in [24] by

 $$ l_{n}(s;\rho,\alpha):=\frac{\rho^{n}}{n!}m_{n}(s-1;\rho,1+\alpha). $$ 

Remark. The classical discrete Laguerre polynomials associated to the geometric distribution (i.e.  $ \alpha = 0 $) have been studied by GOTTLIEB [25] in 1938. For the modified discrete Laguerre polynomials we refer to LESKY [30], [31] and to the textbook of NIKIFOROV and UVAROV [33], which gives a modern survey on orthogonal polynomials. Properties of discrete orthogonal polynomials are proven e.g. by ASKEY and GASPER [2], [3], [24]. The modified discrete Laguerre polynomials with  $ \alpha = 0 $ have been used for the solution of CODE's in [19] and [10]. In [38], the parameter  $ \alpha $ already has been introduced in order to realize a discrete Galerkin method for certain so-called heterogeneous processes.