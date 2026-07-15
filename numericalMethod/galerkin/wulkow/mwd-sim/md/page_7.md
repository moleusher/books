 $$ (l_{k},l_{j})_{\psi}:=\delta_{k,j}\gamma_{j}\qquad\quad\gamma_{j}>0 $$ 

An expansion (5) is possible, if

 $$ \left|\left|P\right|\right|_{\psi}^{2}:=(P,P)_{\psi}<\infty $$ 

In this case, the expansion coefficients  $ a_{j} $ are tending to zero with a certain asymptotic behavior. This motivates an error estimate  $ \varepsilon_{m} $ for an approximation  $ P^{m} $ by

 $$ \varepsilon_{m}^{2}:=\left|\left|P^{m+1}-P^{m}\right|\right|_{\psi}^{2}=a_{m+1}^{2}\gamma_{m+1} $$ 

which works fine as long as the expansion coefficients are decreasing fast enough. If

 $$ \varepsilon_{m+1}\leq C\varepsilon_{m}\quad\mathrm{f o r}\quad m\geq m_{0}\mathrm{a n d}C<1 $$ 

we have $ ^{9)} $

 $$ \varepsilon_{m}\leq\bar{\varepsilon}_{m}\leq\left(\frac{1}{1-C}\right)^{1/2}\varepsilon_{m} $$ 

where  $ \varepsilon_m $ denotes the “true” error. The relation (6) is important, because it clearly shows the bounds and possibilities of the method. If, e.g.,  $ C < 0.8 $ the error estimate is quite reasonable (underestimation smaller than a factor 2), but if there are hints that  $ C $ is larger than 0.9 for one or a few pairs of coefficients, the attempt to approximate a distribution with the above expansion has to be dropped — the chosen weight function is not appropriate (note that in the h-p-method below, the situation of  $ C $ close to one is avoided, because the set of (local, unweighted) basis functions is switched by refining a grid). In order to make the approach as efficient as possible, the weight function has been adapted with time by changing its parameter(s) (moving weight function).

## Example

When  $ \psi $ is the Schulz-Flory distribution

 $$ \psi(s;\;\rho(t))\;=\;(1\;-\;\rho(t))\rho(t))^{s-1} $$ 

the orthogonal polynomials are the discrete Laguerre polynomials $ ^{8)} $. The moving weight function condition for  $ \rho = \rho(t) $ is then

 $$ \left(1-\rho(t)\right)^{-1}=\frac{\mu_{1}(t)\left[P\right]}{\mu_{0}(t)\left[P\right]} $$ 

In contrast to the method of moments, the following advantages of the discrete weighted Galerkin method can be noted: