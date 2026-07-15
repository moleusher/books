The norm of the projection error can be written as

 $$ ||\mathcal{Q}_{n}^{\rho,\alpha}\mathcal{U}||_{1\rho,\alpha}^{2}=\sum_{k=n+1}^{\infty}a_{k}^{2}\gamma_{k}^{\rho,\alpha} $$ 

and it can be seen that

 $$ \begin{aligned}1&\leq\quad\frac{\rho^{m}}{(1-\rho)^{2m}}\frac{(1+\alpha)(2+\alpha)\ldots(m+\alpha)}{(n+1)n\ldots(n+1-(n\imath-1))}\times\\&\quad\times\quad\left[1+\frac{(1-\rho)^{2m}}{\rho^{m}}\frac{k(k-1)\ldots(k-m+1)}{(1+\alpha)\ldots(m+\alpha)}\right]\end{aligned} $$ 

for  $ n+1 \leq k $. Combining (2.21) and (2.22) gives the assertion (2.20).

### 2.4 Summation of Gaussian Type

In the context of the discrete Galerkin method, the numerical evaluation of scalar products in  $ H_{\rho,\alpha} $ is necessary, which can be written in the form

 $$ S=\sum_{s=1}^{\infty}u(s)v(s),\frac{u v}{\Psi_{\rho,\alpha}}\in H^{\rho,\alpha}. $$ 

Thus it is natural to construct a summation formula of Gaussian type [33], which uses the special structure of such sums. We replace a sum

 $$ S=\sum_{s=1}^{\infty}f(s) $$ 

by an approximation

 $$ \tilde{S}=\sum_{j=1}^{k+1}\omega_{j}\;f(s_{j}) $$ 

with nodes $s_j$ and weights $\omega_j$ chosen, such that $S = \bar{S}$ if $f \in H_{\rho,\alpha}^{2k+1}$, i.e. if it can be written as the product of a polynomial of degree $2k + 1$ and $\Psi_{\rho,\alpha}$. It is well known from the theory of quadrature, that then the nodes are just the zeros of the modified discrete Laguerre polynomials. The nodes and weights can be computed easily for a given $k$ by applying the QR-algorithm to a triangular eigenvalue problem, which contains terms from the three-term-recurrence formula of the modified discrete Laguerre polynomials (see the textbook [18], Chapter 9.3.). This makes a Gauss summation very efficient, even when the nodes have to be updated very often.

The Gauss summation captures exactly the structure of the approach and does not require any truncation of the s-axis. Moreover, in Example 4.2 and Example 4.3 double sums are evaluated by this technique very efficiently.