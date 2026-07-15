smooth (in an optic sense) we can expect that a polynomial expansion with only a few expansion terms might be sufficient. However, such global solutions are only obtained in certain special processes (e.g. radical homopolymerization). For distributions  $ u_s $ with steep flanks or for multimodal distributions, we require an automatic local adaptation to avoid bad and inefficient approximations. On the other hand, a purely local approximation scheme as, e.g., a discrete analogue to finite elements with linear basis functions is not the appropriate choice here, since it leads to too many degrees of freedom. Thus we suggest a mixture of local and global approaches, which is in the literature on the numerical solution of partial differential equations known as h-p-method $ ^{[26]} $.

The practical implementation of this basis scheme requires the treatment of many aspects, which cannot be explained here in all details. Thus we restrict ourselves to the main modules of the h-p-algorithm.

Algorithm II, approximation (finite representation) of the solution for one time step

Given: approximation $\varphi$ of $u(t)$, represented by a node-order-pattern $\varLambda$ and a maximal chain length $s_{\max}$, stepsize $\tau$ and tolerance $\mathrm{TOL}_{s}$.

1. Predict a new maximal chain length.

1. Predict a new maximal chain length.

2. Propagation of grids. Extract an initial node-order-pattern from the representation of  $ \varphi $.

3. New representation. Build up a new node-order-pattern, such that  $ \varepsilon_{S} < \mathrm{tol}_{s} \Rightarrow $ Algorithm III

## Maximal chain length — truncation index

In contrast to direct simulation methods, the truncation of the chain length is not a crucial task here. Even if the truncation index is overestimated by orders of magnitude, there is no dramatic increase of computational effort. Nevertheless, the following device gives a reliable estimate of a sufficient truncation index. If a distribution has been approximated up to chain length  $ s_{\text{max}}^{\text{old}} $, the new truncation index  $ s_{\text{max}}^{\text{new}} $ can be computed by

 $$ s_{\max}^{\mathrm{new}}=\frac{\mu_{1}}{\mu_{0}}+\kappa\sqrt{\frac{\mu_{2}}{\mu_{0}}-\left(\frac{\mu_{1}}{\mu_{0}}\right)^{2}}\quad\kappa=10 $$ 

with a safety factor  $ \kappa $ and the moments  $ \mu_{0}, \mu_{1}, \mu_{2} $ of the given distribution.

This formula is a result of the Chebyshev inequality of statistics $ ^{27} $ applied to the chain length distribution. It can be used for estimating how much of the total concentration ( $ \mu_0 $) of a distribution is not in an interval  $ [1, s_{\max}] $. If one wants to compute truncation indices for weight- or  $ w(\log s) $-distributions, the moments  $ \mu_0, \mu_1, \mu_2 $ above have to be replaced by  $ \mu_k, \mu_{k+1}, \mu_{k+2}, k = 1, 2 $, respectively.

Example: For a Schulz-Flory distribution with parameter rho = 0.99 we obtain  $ s_{\max} \approx 1100 $, for a Poisson distribution with mean value 100 we obtain  $ s_{\max} \approx 200 $.