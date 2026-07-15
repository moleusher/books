We expect that for an efficient approximation  $ r_m \ll U^{(m)} - L^{(m)} $ on most of the elements. The whole approach using local refinement and higher order approximations is called Galerkin h-p-method. For rather smoothly looking distributions, we can expect that only a few intervals with moderate polynomial orders are sufficient. However, for distributions with steep flanks or for multi-modal distributions, the approach allows an automated local adaptation to avoid bad and inefficient approximation. By that one can get a nearly exponential convergence rate. This, in particular, is the reason for abandoning the global approach based on a weighted Galerkin ansatz space.

### 2.2 A Tensor Product Approach to Multiple Dimensions

Domains in $d$ dimensions. After these preparations we can extend the approach to higher dimensions. Analogous to the $1d$ case, we restrict the semi-infinite domain $\mathbf{N}^{d}$ to a finite domain

 $$ D=[0,x_{max,1}]\otimes\cdots\otimes[0,x_{max,d}], $$ 

where  $ x_{max,i} $ denotes the upper bound along the ith dimension. Next we decompose  $ D $ into disjoint rectangles  $ \{D^{(m)} : m = 1, \ldots M\} $ such that

 $$ D=\bigcup_{m=1}^{M}D^{(m)}\qquad\mathrm{w i t h}\quad D^{(m)}=[L^{(m,1)},U^{(m,1)}]\otimes\cdots\otimes[L^{(m,d)},U^{(m,d)}]. $$ 

This tensor ansatz allows us to directly make use of the one-dimensional h-p-method. Given the multi-index  $ k = (k_1, \ldots, k_d) $, we define

 $$ \begin{array}{r l r}{T_{k}^{(m)}(x)}&{=}&{T_{k_{1}}^{(m,1)}(x_{1})\cdots T_{k_{d}}^{(m,d)}(x_{d})}\end{array} $$ 

as the product of the discrete Chebyshev polynomials  $ T_{k_i}^{(m,i)} $ on the intervals  $ [L^{(m,i)}, U^{(m,i)}] $ in the ith dimension. Again we have to take care that the boundaries of the rectangles appear only once (see Figure 1 for illustration). A Galerkin approximation on a rectangle  $ D^{(m)} $ is then given by

 $$ p_{r}^{(m)}(t,x)=\sum_{k=1}^{r^{(m)}}a_{k}^{(m)}T_{k}^{(m)}(x) $$ 

with multi-index  $ r^{(m)} = (r_1^{(m)}, \ldots, r_d^{(m)}) \in N^d $. This is a highly non-uniform and flexible structure, since for each axis on each element an independent polynomial system is used. The resulting element-order pattern is given by

 $$ \Delta_{d}=\{(D^{(1)},r^{(1)}),\dots,(D^{(M)},r^{(M)})\}. $$ 