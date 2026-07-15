which is just the product of two 1d Galerkin sums for shift operators. Using Gauss-Christoffel summation we get the approximation

 $$ \begin{array}{r c l}{\tilde{S}_{2}}&{=}&{\displaystyle\sum_{\beta=1}^{n_{2}}v_{\beta}\;\alpha_{2}(y_{\beta})T_{j}^{(m,2)}(x_{\beta})T_{l}^{(n,2)}(y_{\beta}+1)}\\ {\tilde{S}}&{=}&{\displaystyle\sum_{\gamma=1}^{n_{1}}w_{\gamma}\;\alpha_{1}(x_{\gamma})T_{i}^{(m,1)}(x_{\gamma})T_{k}^{(n,1)}(x_{\gamma}-1)\cdot\tilde{S}_{2}}\\ \end{array} $$ 

Here  $ \{w_\gamma, x_\gamma\} $ and  $ \{v_\beta, y_\beta\} $ denote the  $ n_1, n_2 $ weights and nodes of the Gauss-Christoffel summation on  $ I_S^1 $ and  $ I_S^2 $, respectively. This approximation is exact, if the  $ a_i $ are polynomials and the number of nodes is chosen accordingly. The structure of  $ \tilde{S} $ shows that starting from a non-uniform, n-dimensional grid the final treatment of operators can be reduced to a one-dimensional evaluation on single discrete intervals.

However, the situation is more complicated for the second scenario, where we assume that the propensity  $ \alpha = \alpha(x, y) $ cannot be factorized. Then the evaluation has to be performed in two steps. First, for all Gauss-Christoffel nodes of the first direction, the second sum has to be computed for all j and l:

 $$ \tilde{S}_{2}(x_{\gamma})=\sum_{\beta=1}^{n_{2}}v_{\beta}\alpha(x_{\gamma},y_{\beta})T_{j}^{(m,2)}(y_{\beta})T_{l}^{(n,2)}(y_{\beta}+1). $$ 

Then the first sum can be expressed in terms of the intermediate approximations  $ \tilde{S}_{2} $:

 $$ \tilde{S}=\sum_{\gamma=1}^{n_{1}}w_{\gamma}\alpha(x_{\gamma},y_{\beta})T_{i}^{(m,1)}(x_{\gamma})T_{k}^{(n,1)}(x_{\gamma}-1)\tilde{S}_{2}(x_{\gamma}) $$ 

This strategy might look as a minor aspect of the practical realization, but it is crucial for the whole tensor product approach (compare (2.25)). Based on this strategy, all terms of the equations presented in Sec. 3 can be treated in a structural way.

## 3 Numerical Examples

In this section, we illustrate the above described adaptive discrete Galerkin approach at two examples. The first one, a genetic toggle switch, has been selected for comparison purposes, since it has already been used as a test