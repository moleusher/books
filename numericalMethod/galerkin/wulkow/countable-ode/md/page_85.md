Refinement strategy [5]. It is reasonable to equilibrate the local errors on each grid  $ \Delta^i $. Let  $ \Delta^{i-1} $ and  $ \Delta^i $ be constructed with  $ n_{i-1} $ respectively  $ n_i $ subintervals and errors  $ \varepsilon_k^{i-1} $ and  $ \varepsilon_j^i $. If we refine an interval  $ I_j^i $ again, we can expect from (6.7) that the errors  $ \varepsilon_m^{i+1} $ and  $ \varepsilon_{m+1}^{i+1} $ on the new generated intervals  $ I_m^{i+1} $ and  $ I_{m+1}^{i+1} $ will be approximately

 $$ \tilde{\varepsilon}_{j}^{i+1}:=\left(\varepsilon_{k}^{i-1}\right)^{2}/\varepsilon_{j}^{i}\;, $$ 

under the assumption, that the associated intervals have been bisected. Then we compute a cut value by

 $$ \mathrm{c u t}_{i+1}=\operatorname*{m a x}_{j=1,\ldots,n_{i}}\tilde{\varepsilon}_{j}^{i+1}, $$ 

and intervals  $ I_j^i $ with  $ \varepsilon_j^i \geq \text{cut}_{i+1} $ will be refined only.

Algorithm. In short form the algorithm reads as follows:

(1) Choice of a start grid with an odd number of points (at least three), i.e. an even number of subintervals.

(2) Approximation of the sums on all intervals with discrete Trapezoidal and Simpson rule. Computation of the global sum, refinement of all intervals.

(3) Local and global error estimation, where the global error is estimated by comparison of the approximations of the global sums on the last two refinement levels.

(4) if global error (scaled) < TOL : stop.

if not: refinement of all intervals with error larger than the cut value.

(5) Evaluation of the new sums; back to (3).

If the value of the sum turns out to be small (< 1), an absolute scaling is used. The algorithm has been implemented in the language C, using concepts and data structures from the finite element codes KASKADE [47], [48] and KASTIX [7].

Example 6.1. As a first example we consider the computation of the truncated harmonic series

 $$ \sum_{s=1}^{s_{\operatorname*{m a x}}}\frac{1}{s}. $$ 

This sum is a challenging test for the algorithm, because the harmonic series diverges logarithmically in  $ s_{max} $. So we have to expect, that the nodes chosen by