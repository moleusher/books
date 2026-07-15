As seen in Section 3.1, the computational realization of (semi-) implicit Euler steps requires the solution of equations of the type

 $$ \left(I-\tau A\right)u=\varphi. $$ 

Assuming that the solution of (3.7) has a basis expansion in $H_{\rho,\alpha}$ and inserting it into the equation, we can derive (by analytical or numerical manipulations) a linear (also infinite) system, which defines the expansion coefficients. Truncation of this system at dimension $n+1$, then called the Galerkin equations, leads to a Galerkin approximation

 $$ \tilde{u}^{n,l}=\sum_{k=0}^{n}\tilde{a}_{k}^{l}\psi_{k}(s;\rho,\alpha)\in H_{\rho,\alpha}^{n},\;n\geq0, $$ 

of u, where the  $ \tilde{a}_{k}^{l} $ are not necessarily the expansion coefficients  $ a_{k} $ of u, because:

(i) the Galerkin equations may be not self-closing, i.e. the entries of the linear system are depending on coefficients  $ a_{k} $,  $ k > n $ implying a dependency of the solution  $ a_{k} $ on the truncation index. This effect is denoted by a tilde

(ii) in many problems the matrix entries and the right-hand side have to be approximated numerically. The superscript $l$ characterizes the accuracy of the associated algorithm.

For fixed n the Galerkin equations can be written as

 $$ \left(\mathcal{P}_{n}^{\rho,\alpha}(\tilde{u}^{n,l}-\tau A\tilde{u}^{n,l}),\psi_{j}\right)_{\rho,\alpha}=\left(\mathcal{P}_{n}^{\rho,\alpha}\varphi,\psi_{j}\right)_{\rho,\alpha},\;\tilde{u}^{n,l}\in H_{\rho,\alpha}^{n}\;, $$ 

for $j = 0, \ldots, n$. After insertion of the basis expansion we obtain an $n + 1$-dimensional linear system

 $$ \left(I-\tau B\right)a=b, $$ 

with the matrix  $ B := (b_{jk}) $.

 $$ b_{j k}:=(A\psi_{k},\psi_{j})_{\rho,\alpha}^{l}\quad, $$ 

and the right-hand side  $  b = (b_{0}^{l}, \ldots, b_{n}^{l})^{T}  $,

 $$ b_{j}=(\varphi,\psi_{j})_{\rho,\alpha}^{l}. $$ 

The vector  $ a = (\tilde{a}_0^l, \ldots, \tilde{a}_n^l)^T $ contains the coefficients of  $ \tilde{u}^{n,l} $. As said before, the superscript  $ l $ indicates, that the scalar products may be not evaluated exactly. For given coefficients  $ a $, the approximation  $ \tilde{u}^{n,l} $ is pointwise computed in the program by a fast algorithm [15].

In the following we have to deal with three errors: