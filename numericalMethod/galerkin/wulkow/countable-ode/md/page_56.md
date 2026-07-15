is reasonable. As in DEUFLHARD [15] Section 1.2 we are thus led to the subdi-

agonal error criterion

 $$ \epsilon_{k+1,k}\doteq||\mathcal{U}_{k+1,k}-\mathcal{U}_{k+1,k+1}||=:[\epsilon_{k+1,k}]_{\mathrm{S D}} $$ 

as a reasonable (semi-discrete) estimator.

Notation: A single quantity in square brackets denotes a computable estimator for this quantity.

Summarizing, the basic time-step for achieving a prescribed tolerance TOL in line  $ j+1 $ of the extrapolation table is given as

 $$ T_{j+1,j}:=\left(\frac{\mathrm{T O L}}{\left[\epsilon_{j+1,j}\right]_{s d}}\right)^{1/(k+1)}T, $$ 

T the present basic time-step.

In the fully discrete case we have to approximate the solution of the countable systems of algebraic equations (CAE's) arising in each (semi-) implicit Euler step, respectively the application of the operator to an element from  $ H_{\rho,\alpha} $ in the explicit case. This will be done by means of the discrete Galerkin method as suggested in Chapter 3. In both cases we obtain the perturbed extrapolation table

 $$ \begin{array}{ccc} \mathcal{U}_{11}+\delta_{11} & \searrow& \\ \downarrow& & \\ \vdots & & \ddots \end{array} $$ 

 $$ \mathcal{U}_{k1}+\delta_{k1}\quad\rightarrow\quad\ldots\quad\searrow\quad\mathcal{U}_{k k}+\delta_{k k}\quad, $$ 

instead of (4.7), where the  $ \delta_{j1} $ are produced by successive (numerical) solution of the CAE's (or by numerical projection) and the  $ \delta_{jk} $,  $ k > 1 $, are the propagated errors in the table. Let  $ \tilde{U}_{jk} := U_{jk} + \delta_{jk} $. The task now is to give a criterion for the accuracy of the discrete sub-problems (CAE, projection), such that the propagation of the introduced errors in the extrapolation table leads only to negligible errors in the semi-discrete problem. Therefore we need

(i) a fully discrete estimator  $ [\epsilon_{k+1,k}] $ with

 $$ [\epsilon_{k+1,k}]_{\mathrm{S D}}\stackrel{\cdot}{\leq}[\epsilon_{k+1,k}] $$ 

and

(ii) a control of  $ \delta_{k+1,k+1} $, such that

 $$ \bar{\mathcal{U}}_{k+1,k+1}\mathrm{~i s~a~t o l e r a b l e~a p p r o x i m a t i o n}. $$ 