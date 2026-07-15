Realization of the Extrapolation. The extrapolation can be performed in two ways, depending on the approximation of the Euler steps.

(i) Assume that the initial value  $ u(t) $ for a global time step T is given in  $ H_{\rho,\alpha} $ and that Galerkin approximations of the  $ U_{j1}, j = 1, \ldots, k $, are also computed in  $ H_{\rho,\alpha} $:

 $$ \mathcal{U}_{11}=\sum_{i=0}^{n^{11}}a_{i}^{11}\psi_{i}(\rho,\alpha)\;, $$ 

 $$ \mathcal{U}_{k1}=\sum_{i=0}^{n^{k1}}a_{i}^{k1}\psi_{i}(\rho,\alpha)\;, $$ 

with  $ n^{j+1,1} \geq n^{j,1} $,  $ 1 \leq j \leq k-1 $. Then the extrapolation table can be built up in  $ H_{\rho,\alpha} $ by applying the Aitken-Neville scheme to the expansion coefficients  $ a_{i}^{k1} $ leading to

 $$ u_{T}^{\bar{n}}(t+T):=\mathcal{U}_{k k}=\sum_{i=0}^{\bar{n}}a_{i}^{k k}\psi_{i}(\rho,\alpha),\bar{n}=n^{k k}. $$ 

Finally  $ u_{\tau}^{n}(t+T) $ is transformed to a space  $ H_{\bar{\rho},\alpha} $ due to the weight function fitting condition (3.23) derived in Section 3.2. The procedure above has the advantage that there are no transformations necessary between  $ H_{\rho,\alpha} $ - spaces necessary during the global time step. Furthermore we know from the theory that extrapolation in the basic space  $ H_{\rho,\alpha} $ is possible, whereas changing the space for each Euler step can lead to non feasible transformations. This reliability is paid by requiring possibly more expansion coefficients for the single Euler steps, since the space might be not ‘optimal’, i.e. not chosen due to the fitting condition (3.22).

(ii) In a second approach the  $ U_{j1} $ are computed in spaces chosen by a weight function fitting in each step:

 $$ \mathcal{U}_{11}=\sum_{i=0}^{n^{11}}a_{i}^{11}\psi_{i}(\rho^{11},\alpha^{11})~, $$ 

 $$ \mathcal{U}_{k1}=\sum_{i=0}^{n^{k1}}a_{i}^{k1}\;\psi_{i}(\rho^{k1},\alpha^{k1})\;. $$ 

In order to extrapolate the coefficients, now we have to transform the expansion of  $ \mathcal{U}_{j1} $ in  $ H_{\rho^{j1},\alpha^{j1}} $ to the space  $ H_{\rho^{j+1,1},\alpha^{j+1,1}} $ first. As the table is built up row by row, the final space is not known a priori, hence up to  $ k-1 $ transformations are