Proof. (i) This can easily be proven by use of the Banach fixed-point theorem and the Neumann series.

(ii) The infinitesimal generator A of a  $ C_{0} $ - semigroup of contractions is characterized by the Lumer-Phillips theorem ([34], Theorem 4.3):

A is dissipative, i.e.  $ (Au, u) \leq 0 $ and for a  $ \lambda_0 > 0 $ the range of  $ \lambda_0I - A $ is  $ H_{\rho,\alpha} $. For  $ \tilde{u}^n \in H_{\rho,\alpha}^n $ it follows from

that  $ \mathcal{P}_n^{\rho,\alpha} $ A is also dissipative and the range condition is fulfilled in  $ H_{\rho,\alpha}^n $ because of (3.13). Hence  $ \mathcal{P}_n^{\rho,\alpha} $ A generates a contractive  $ C_0 $ - semigroup too.

 $$ \left(\mathcal{P}_{n}^{\rho,\alpha}A\tilde{u}^{n},\;\tilde{u}^{n}\right)_{\rho,\alpha}=\left(A\tilde{u}^{n},\;\tilde{u}^{n}\right)_{\rho,\alpha} $$ 

Error estimation. In view of Theorem 3.3 the numerical implementation of the discrete Galerkin method requires an estimate of the projection error at least.

LEMMA 3.4. Define an error estimate  $ \varepsilon_{n} $ of the projection error (3.11) by

 $$ \varepsilon_{n}^{2}:=||u^{n+1}-u^{n}||^{2}=a_{n+1}^{2}\gamma_{n+1}^{\rho,\alpha}, $$ 

and assume that there exist C < 1 and  $ n_{0} \geq 1 $ such that for  $ n > n_{0} $ the relation

 $$ \varepsilon_{n+1}\leq C\varepsilon_{n} $$ 

holds. Then

 $$ \varepsilon_{n}\leq\bar{\varepsilon}_{n}\leq\left(\frac{1}{1-C^{2}}\right)^{1/2}\varepsilon_{n},n\geq n_{0}. $$ 

Proof. Obviously

 $$ \varepsilon_{n}^{2}\leq\bar{\varepsilon}_{n}^{2}=\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha} $$ 

since  $ \gamma_{k}^{\rho,\alpha} > 0 $. On the other hand it follows from (3.15) for  $ n \geq n_{0} $ that

 $$ \bar{\varepsilon}_{n}^{2}=\sum_{k=n+1}^{\infty}\varepsilon_{k-1}^{2}\leq\varepsilon_{n}^{2}\sum_{k=0}^{\infty}C^{2k}=\frac{1}{1-C^{2}}~.\quad▪ $$ 

The actual value of C can be estimated in the algorithm by considering successive error estimates for increasing n. Whenever C turns out to be near or larger than one, a warning is given by the program. In applications the projection error has to be measured in a scaled norm, of course.