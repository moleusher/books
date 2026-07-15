to the inner sum of the second term we can rewrite

 $$ \begin{array}{r c l}{\left\|D A_{C}(u)\:v\right\|_{\rho}^{2}}&{\leq}&{2\displaystyle\sum_{r=1}^{\infty}v(r)\:\rho^{-r}\displaystyle\sum_{k=1}^{r}\left|v(k)\right|\left(u\:,\:S_{+}^{r-k}u\right)_{\rho}}\\ {}&{\leq}&{2\left\|u\right\|_{\rho}^{2}\left[\displaystyle\sum_{r=1}^{\infty}v(r)\:\sqrt{\rho}^{-r}\displaystyle\sum_{k=1}^{r}\left|v(k)\right|\sqrt{\rho}^{-k}\right]}\\ {}&{\leq}&{2\left\|u\right\|_{\rho}^{2}\left(\displaystyle\sum_{r=1}^{\infty}\left|v(r)\right|\sqrt{\rho}^{-r}\right)^{2}\leq\displaystyle\frac{1}{\varepsilon}2(1-\rho+\varepsilon)\left\|u\right\|_{\rho}^{2}\left\|v\right\|_{\rho-\varepsilon}^{2}\;,}\\ \end{array} $$ 

with the norm of the shift operator from (1.41) and Corollary 1.7 (using  $ \|v\|_{\rho,\alpha} = \|\|v\|\|_{\rho,\alpha} $). Application of the mean-value theorem gives (1.48) with  $ \gamma = 1/2 $.

### 1.4 DISCRETIZATION AND EXTRAPOLATION

We apply the idea of a discretization in time of an abstract Cauchy problem in an appropriate Hilbert space. Consider a linear, homogeneous abstract Cauchy problem

 $$ \frac{\mathrm{d}u(t)}{\mathrm{d}t}=A u(t),u(0)=\varphi. $$ 

This differential equation can be discretized for given t by the implicit Euler scheme leading to

 $$ \frac{u_{n}\left(\frac{j t}{n}\right)-u_{n}\left(\frac{(j-1)t}{n}\right)}{\frac{t}{n}}=A u_{n}\left(\frac{j t}{n}\right),u_{n}(0)=\varphi, $$ 

for  $ j = 1, \ldots, n $, which can be written as

 $$ u_{n}(t)=\left(I-\frac{t}{n}A\right)^{-n}\varphi\;. $$ 

For bounded operators we can also apply the explicit Euler scheme and obtain

 $$ u_{n}(t)=\left(I+\frac{t}{n}A\right)^{n}\varphi. $$ 

By  $ u_{\tau}(t) $ we denote the implicit (explicit) Euler approximation (1.54), (1.55) with time step  $ \tau = t/n $. For A a bounded (Lipschitz continuous) operator in a Hilbert space  $ H $ ( $ H = H_{\rho,\alpha} $ here, of course) we then know