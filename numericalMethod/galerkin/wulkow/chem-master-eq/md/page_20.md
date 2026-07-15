1)/(x_{max,i} + 1), where y_{max,i} denotes the new estimate. At the same time care has to be taken that all resulting  $ L^{(m,i)} $ and  $ U^{(m,i)} $ are still defined as natural numbers. Finally, when compressing the whole grid  $ \Delta_d $, it has to be ensured that no degenerated domains  $ D^{(m)} $ arise.

Given some initial element-order pattern  $ \Delta_{d} $ (e.g., from the previous time step), the algorithm comprises the following steps:

1. Coarse the grid by decrease of orders or merging of elements.

2. Compute new  $ x_{max,i} $ and stretch or compress the domain.

3. Project the current Galerkin approximation onto the new grid.

4. Set up the Galerkin equations (see below) and solve for coefficients on all elements  $ D^{(m)} $.

5. Compute error estimates for the whole domain, all elements and directions.

6. If global error below tolerance, complete Rothe time step and go back to 1, otherwise:

7. Examine the single element axes in view of order or refinement actions based on error estimates and predictions.

8. Select elements for refinement based on work-oriented error control.

9. Create new grid and go back to 3.

Efficient evaluation of Galerkin matrix entries. In order to illustrate how the setup of the Galerkin equations works in 2d, we consider the special operator

 $$ (\mathcal{A}p)(x,y)=\alpha(x-1,y+1)p(t,x-1,y+1) $$ 

as it appears as a typical term in the CME (see Sec. 3) with propensity $a$ and distribution $p(t)$. For ease of reading, we choose $(x,y)$ instead of $(x_{1},x_{2})$. The arrows in Figure 2 show the flow of information for a single domain $D^{(m)}.$

For the treatment within the Galerkin method, the operator A has to be applied to all basis functions  $ T_{k}^{(n)} = T_{k}^{(n,1)} T_{l}^{(n,2)} $ of all ansatz elements