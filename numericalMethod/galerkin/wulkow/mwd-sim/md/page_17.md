## Galerkin equations and Gauss summation

For a given node-order-pattern a Galerkin matrix  $ \boldsymbol{G} = (g_{jk}) $ has to be constructed which is in principle the product of the operator Jacobian  $ A = f_u(\varphi) $ times the solution  $ u $ expressed in terms of the chosen basis functions  $ t_j(s) $. This is the central point of a Galerkin method and requires numerical summations of the form (special indices of the h-p-method omitted)

 $$ g_{jk}=\sum_{s=1}^{s_{\max}}At_{k}\left(s\right)t_{j}\left(s\right) $$ 

With the matrix  $ \boldsymbol{G} = (g_{jk}) (k, j \text{ counting the basis functions } t_k, t_j \text{ of all intervals of the grid}) \text{ the Galerkin equations for the solution vector } \boldsymbol{a} \text{ of all expansion coefficients read} $

 $$ G a=(\sum_{s=1}^{s_{\max}}b_{s}t_{j}(s))_{j} $$ 

In the h-p-algorithm all such summations are performed by an algorithm of Gaussian type directly induced by the  $ t_{j}(s) $. We replace a sum on an interval I

 $$ S^{I}=\sum_{l}f(s) $$ 

by an approximation

 $$ S_{k}^{I}=\sum_{j=1}^{k+1}\omega_{j}^{I}f\left(s_{j}^{I}\right) $$ 

with nodes  $ s_j' $ and weights  $ w_j' $ chosen, such that  $ S' = S_k' $ if  $ f(s) $ is a polynomial of order  $ 2k + 1 $. It is well known from the theory of Gauss quadrature that here the nodes are just the zeros of the discrete Chebyshev polynomials on interval  $ I $. The nodes and weights can easily be computed for a given  $ k $ by applying the QR-algorithm to a triangular eigenvalue problem, which contains terms of the three-term recurrence formula of the polynomials (see, e.g., ref. $ ^{29} $). The Gauss summation captures exactly the structure of the approach and requires only slight additional computations. It has been shown in ref. $ ^{9} $ that the perturbation introduced by the Gauss summation does not affect the quality of a Galerkin approximation of order  $ n $, whenever at least  $ n + 1 $ Gauss nodes are used (see also ref. $ ^{30} $) for continuous finite elements). This nice feature allows even the treatment of chain-length dependent termination processes (double sums) with relatively few function evaluations.

Finally we want to note that for the entries of the Galerkin matrix, the edges of an interval require additional considerations.

The above explanations show that the PredICI concept is not a simple algorithm. In particular what is sketched above for a single distribution has to be done for a list of distributions in interesting problems. For the treatment of the most reaction steps, two or more different node-order-patterns have to be connected, because each distribution