LEMMA 6.1. For  $ r \in I $ the interpolation error  $ \epsilon_I^n(r) $ is given by

 $$ \epsilon_{I}^{n}(r):=f(r)-D_{n}(r)=\omega_{n+1}(r)\;f[s_{0},\dots,s_{n},r]\;. $$ 

Proof. The representation of  $ D_{n}^{s_{0},\ldots,s_{n}}(s) $ in terms of divided differences leads to

 $$ \begin{array}{rcl}f(r)-D_{n}^{s_{0},\ldots,s_{n}}(r)&=&D_{n+1}^{s_{0},\ldots,s_{n},r}(r)-D_{n}^{s_{0},\ldots,s_{n}}(r)\\&=&{\omega_{n+1}}(r)f[s_{0},\ldots,s_{n},r]\end{array} $$ 

using (6.4).

Lemma 6.1 shows, that the ‘smoothness’ of grid functions is measured in the present context by the value of the maximum of the divided differences  $ f[s_0,\ldots,s_n,r] $ on  $ I $. The theorem ensures that for a moderate bound of this difference the behavior of the interpolation will be comparable to the continuous case.

Summation formulas. The construction of summation rules can be done analogue to the derivation of quadrature formulas. For given nodes  $ s_0, \ldots, s_n $ the interpolation polynomial  $ D_n^{s_0, \ldots, s_n}(s) $ is summed from  $ s = s_0 $ to  $ s = s_n $. For the multilevel algorithm we restrict ourselves to low-order summation rules – comparable to the Trapezoidal rule and the Simpson rule in numerical quadrature.

Discrete Trapezoidal rule. Consider the discrete interval $\{s_0, s_0+1, \ldots, s_1\}$ with $s_1 := s_0 + \delta$, $\delta \in \mathbb{N}$. Let $f_0 := f(s_0)$ and $f_1 := f(s_1)$. Then the trapezoidal sum $T(\delta)$ of $\sum_{s=s_0}^{s_1} f(s)$ turns out to be

 $$ T(\delta)=\frac{\delta+1}{2}\left(f_{0}+f_{1}\right). $$ 

The difference to the continuous Trapezoidal rule arises from the fact, that edge points have to be considered separately. Insertion of the interpolation error from Lemma 6.1 lets expect the summation error  $ \epsilon_{\delta} $ to behave like

 $$ \epsilon_{\delta}\doteq C\;\delta\;,\;C\;\mathrm{~c o n s t a n t~}. $$ 

Note that for a repeated application of a summation rule the role of the bounds of the sub-intervals has to be kept in mind.