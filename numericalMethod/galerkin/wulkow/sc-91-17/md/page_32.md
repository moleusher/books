## 4 NUMERICAL EXAMPLES

The considerations of this paper led to the program CODEX written in the language C. Details of the implementation can be found in [39] for the case of extrapolation in time. The use of the multiplicative correction formula as time discretization lets the structure of the program in principle unchanged.

In this chapter some numerical results are presented featuring:

• the time discretization (linear and nonlinear)

• the adaptivity of the method with respect to the parameters  $ \rho $,  $ \alpha $

● the adaptivity with respect to the truncation index n

- the numerical preprocessing with Gauss summation.

All computations have been performed on a SPARC-station 1+ using double precision. The computing times (CPU) are given in seconds.

### 4.1 CHAIN ADDITION POLYMERIZATION

We consider the backward difference equation from Example 1.1:

 $$ u^{\prime}(t)=-\nabla u(t)\;,\;u(0)=\varphi\;, $$ 

which is the (normalized) CODE of the reaction step  $ P_s + M \stackrel{\leftrightarrow}{P}_s P_{s+1} $. The Galerkin equations can be derived analytically by applying Corollary 2.5. The process is started with the geometric distribution  $ \varphi = \Psi_{\rho,0} \in H_{\rho,0} $ and has been integrated here up to  $ t_{end} = 50 $ sec. The choice  $ \rho_0 = 0.3 $ is made to illustrate the parameter control of the algorithm. From (1.4) the solution  $ u(t) $ is expected to be similar to a Poisson distribution with parameter  $ \lambda = t $. As the weight function  $ \Psi_{\rho,\alpha} $ tends to such a Poisson distribution for  $ \rho \to 0 $ and  $ \alpha = t/\rho $, we can expect to obtain Galerkin approximations in spaces  $ H_{\rho,\alpha} $ with  $ \rho \ll \rho_0 $ and  $ \alpha $ large. It turns out actually, that the parameter  $ \rho $ decreases to  $ \rho(t_{end}) = 3.6 \cdot 10^{-3} $, whereas the parameter  $ \alpha $ increases from zero to  $ \alpha(t_{end}) = 13844.4 $ - this is presented in Figure 1 (logarithmic scale). Table 1 reflects the behavior of the time-step control, where it can be seen, that the maximum true error (computed in  $ H_{\rho,\alpha} = H_{\rho(t),\alpha(t)} $, using (1.4)) over all time steps fits to the required accuracy TOL. Throughout this chapter  $ n_{\text{max}} $ may denote the maximum of the number of expansion coefficients in  $ H_{\rho(t),\alpha(t)} $ required to represent the solution after a global time step. Figure 2 shows the time layers chosen by the algorithm.