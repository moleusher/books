since  $ \gamma_{k}^{\rho,\alpha} > 0 $. On the other hand it follows from (3.17) for  $ n \geq n_{0} $ that

 $$ \bar{\varepsilon}_{n}^{2}=\sum_{k=n+1}^{\infty}\varepsilon_{k-1}^{2}\leq\varepsilon_{n}^{2}\sum_{k=0}^{\infty}C^{2k}=\frac{1}{1-C^{2}}.\quad\blacksquare $$ 

The underestimation of the true error depending on C can be numerically controlled by setting a safety factor. In applications the projection error has to be measured in a scaled norm, of course.

Example 3.3. It is easily seen that in Example 3.1, u approximated in  $ H_{\rho,1} $

 $$ \frac{\varepsilon_{n+1}}{\varepsilon_{n}}\leq\frac{3}{5},\mathrm{~f o r~}n\geq6, $$ 

hence the underestimation of the error is smaller than 5/4. A comparison between true and estimated error for this example can be found in [18], Table 1.

Now assume, that there is an algorithm producing successive approximations  $ a_k^m $ of  $ a_k - e.g $ by setting  $ m = \tilde{n} = n, n + 1, \ldots $, in (3.7) or by a refinement strategy during the numerical summation with  $ m $ the refinement level or the index of a tolerance. Then the following error estimation will be applied

 $$ \varepsilon_{n,m}^{2}:=\varepsilon_{T,n,m}^{2}+\varepsilon_{P,n,m}^{2}:=\sum_{k=0}^{n}\left(a_{k}^{m}-a_{k}^{m+1}\right)^{2}\gamma_{k}^{\rho,\alpha}+\left(a_{n+1}^{m+1}\right)^{2}\gamma_{n+1}^{\rho,\alpha}. $$ 

We are only interested in a truncation error (respectively its estimation)  $ \varepsilon_{T,n,m} $ being just a little smaller than the projection error  $ \varepsilon_{P,n,m} $. To be more precise, we require that

 $$ \left|\left|u^{n+1,m(n+1)}-u^{n+1}\right|\right|_{\rho,\alpha}<\kappa\left|\left|u^{n,m(n)}-u\right|\right|_{\rho,\alpha} $$ 

with some safety factor  $ 0 < \kappa < 1 $ (see also [17], (1.26)). In actual computations, the terms on both sides are replaced by the estimates suggested in (3.19),  $ \kappa $ is set to 1/4.

### 3.2 Weight Function Fitting

In order to minimize the computational effort of the discrete Galerkin method, a good choice of the parameters  $ \rho $ and  $ \alpha $ is crucial. Strictly speaking, for  $ u \in H_{\rho,\alpha} $ and  $ \varepsilon > 0 $ it would be optimal to find  $ \bar{\rho} $,  $ \bar{\alpha} $ such that  $ u \in H_{\bar{\rho},\bar{\alpha}} $ and

 $$ ||u-u^{n}||_{\bar{\rho},\bar{\alpha}}<\varepsilon~,~u^{n}=\mathcal{P}_{\bar{\rho},\bar{\alpha}}u~, $$ 

for $n$ as small as possible. However, even if the error $\|u - u^n\|\$ is computable, the estimation of $\bar{\rho}, \bar{\alpha}$ turns out to be a nonlinear minimization problem, since