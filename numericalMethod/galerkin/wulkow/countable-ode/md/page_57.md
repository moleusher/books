The estimator  $ [\epsilon_{k+1,k}] $ will replace  $ [\epsilon_{k+1,k}]_{\text{Sd}} $ in the time-step prediction formula (4.13). First we can state

 $$ \begin{array}{r l r}{[\epsilon_{k+1,k}]_{\mathrm{S D}}}&{\leq}&{||\mathcal{\bar{U}}_{k+1,k}-\mathcal{\bar{U}}_{k+1,k+1}||_{\rho,\alpha}}\\ &{+}&{||\delta_{k+1,k}-\delta_{k+1,k+1}||_{\rho,\alpha}.}\end{array} $$ 

Under the assumption that we are able to estimate the perturbations

 $$ \delta_{k+1,k}\;,\;\delta_{k+1,k+1}\;,\;\delta_{k+1,k}\;-\;\delta_{k+1,k+1} $$ 

we define

 $$ \left[\epsilon_{k+1,k}\right]:=\left|\left|\bar{\mathcal{U}}_{k+1,k}-\bar{\mathcal{U}}_{k+1,k+1}\right|\right|_{\rho,\alpha}+\left[\delta_{k+1,k}-\delta_{k+1,k+1}\right], $$ 

which is a completely computable quantity. It is reasonable to ask for

 $$ \begin{aligned}&a)\quad[\delta_{k+1,k}],[\delta_{k+1,k+1}]\quad\leq\quad TOL/2\\&b)\quad[\epsilon_{k+1,k}]\quad\leq\quad TOL,\\ \end{aligned} $$ 

for given local tolerance TOL. By examination of the propagation of the errors  $ \delta_{j1} $ in the table we get

 $$ \delta_{j k}=\sum_{i=j-k+1}^{j}\beta_{j k}^{i}\delta_{i1}~, $$ 

where the coefficients  $ \beta_{jk}^{i} $ only depend on the chosen subdividing sequence F. Substituting the  $ \delta_{jk} $ by estimates

 $$ [\delta_{j k}:=\sum_{i=j-k+1}^{j}|\beta_{j k}^{i}|\;[\delta_{i1}] $$ 

we need

 $$ [\delta_{j1}]\leq\alpha_{j}^{k}\mathrm{T O L}, $$ 

where the coefficients  $ \alpha_j^k $ can be computed once at the beginning, only depending on  $ \mathcal{F} $. The coefficients can be optimized if the amount of work for the computation of  $ \mathcal{U}_{j_1} $ is known. The building of the extrapolation table up to row  $ k $ requires – according to (4.16) – the computation of the  $ \tilde{\mathcal{U}}_{j_1} $ with error not exceeding  $ \alpha_j^k $ TOL. This is done by solving  $ j $ CAE's (performing  $ j $ projections), the implicit (explicit) Euler steps. The  $ i $-th of them produces its own error  $ \tilde{\Delta}_i $ and the exact problem propagates the previous error  $ \Delta_{i-1} $ by a propagation operator  $ \pi $, thus leading to

 $$ \Delta_{i}=\bar{\Delta}_{i}+\pi\Delta_{i-1}\;. $$ 

The role of  $ \pi $ can be controlled in some cases. As the following result is not a specific property of  $ H_{\rho,\alpha} $, we assume a Banach space X with norm  $ \|\cdot\| $.