## 4 NUMERICAL REALIZATION OF THE ALGORITHM

In this chapter we describe the essential details of the algorithm:

• time-step and order control, extrapolation

• realization of the discrete Galerkin method

### 4.1 REALIZATION OF THE TIME-STEP CONTROL

In this section, which follows the presentation of Chapter 3 in [8], it will be explained, that the usual results for extrapolation-methods with some modifications still hold in  $ H_{\rho,\alpha} $, instead of  $ |R^n $. In the fully-discrete case (i.e. time discretization and approximation in  $ H_{\rho,\alpha} $ by means of orthogonal polynomials) the requirements of the original problem have to be taken into account.

We use the implicit (explicit, semi-implicit) Euler discretization in time and a time–step and order control of the method by extrapolation following the ideas of DEUFLHARD [15] for ODE's and of BORNEMANN [8] for parabolic PDE's. As pointed out in Section 1.4, the explicit Euler discretization is applied only to bounded operators, the implicit Euler scheme only to linear problems. For the nonlinear case (see Example 5.4) the semi-implicit Euler scheme [16] is applied:

 $$ \begin{array}{r c l}{(I-\tau\;A)\;\Delta u(t)}&{=}&{\tau\;f(u(t))~,}\\ {u_{\tau}(t+\tau)}&{:=}&{u(t)+\Delta u(t)~,}\\ \end{array} $$ 

with  $ A = f_u(u(t)) $ the Frechét derivative of the right-hand side  $ f(u) $ in problem (1.1) at time  $ t $. Obviously the implicit Euler discretization is identical with the semi-implicit Euler scheme in the linear case. The extrapolation on the basis of one of these schemes works as follows:

The algorithm suggests an outer time step T > 0 for which

 $$ \mathcal{U}_{i1}:=u_{\tau_{i}}(T)\;, $$ 

the Euler discretizations with time-step  $ \tau_i = \frac{T}{n_i} $ as introduced in Section 1.4, are computed for a given sequence of increasing  $ n_i $:

 $$ \mathcal{F}=\left\{n_{1},n_{2},\ldots\right\}\;. $$ 

Since  $ \lim_{\tau\downarrow0}u_{\tau}(T)=u(T) $, the values  $ (\mathcal{U}_{11},\ldots,\mathcal{U}_{k1}) $ are extrapolated to  $ \tau=0 $, getting an hopefully better approximation than the  $ \mathcal{U}_{i1} $. This will be explained now. We compute the interpolation polynomial with values in  $ H_{\rho,\alpha} $

 $$ p_{j k}(\tau)=e_{0}+e_{1}\tau+\ldots+e_{k-1}\tau^{k-1}~, $$ 