The simulation of molecular weight distributions in polyreaction kinetics ...

 $$ \begin{aligned}(\mathbf{I}-\tau A)\boldsymbol{\eta}_{1}&=-\frac{1}{2}\tau^{2}A f\left(\varphi\right)\\u_{2}&=u_{1}+\eta_{1}\end{aligned} $$ 

such that no additional linear system has to be treated. Besides, the approximation  $ u_{2} $ is of the increased order 2. Whenever a time step with (old) step size  $ \tau $ has been performed with the schemes (7) and (8), a new step size  $ \tau_{new} $ can be computed by

 $$ \tau_{\mathrm{new}}=\tau\sqrt{\frac{\mathrm{Tol}}{\kappa\left|\left|\boldsymbol{\eta}_{1}\right|\right|}} $$ 

where  $ \kappa < 1 $ is a safety factor. Further details of this kind of a Rothe method can be found in ref. $ ^{21} $, a (complete adaptive) algorithm for kinetic equations in polyreactions based on this theory, but with global, less flexible basis functions than proposed here, is described in ref. $ ^{9} $

Up to this point, it is not yet prescribed how the solutions of Eqs. (7) and (8) actually should be computed or approximated. The following time control is a general one for ordinary, partial and countable differential equations and can also be extended to algebraic systems. Moreover, with slight changes, an inexact Newton method for computing stationary solutions can be easily derived.

## Algorithm I, time control

Given: approximation  $ \varphi $ of  $ u(t) $, (time) error estimate  $ \varepsilon_{T}(t) $.

1. Compute new time step length by Eq. (9), where  $ \|\eta_1\| = \varepsilon_T(t) $.

2. Solve system (7) within accuracy to  $ L \cdot (1/16) $ using Algorithm II → finite representation of the solution.

3. Solve system (8): Use the representation for the solution obtained in 2.

4. Estimate: Compute a new time estimate.

5. Loop control: If the error is smaller than TOL set  $ \varphi = u_{2}, t = t + \tau $, and start next step in 1, otherwise reduce stepsize and start in 2.

## Approximation of distributions within a time step

After generally describing the time discretization it “remains” to solve Eq. (7) within a certain accuracy. We write the stationary linear problems in Eqs. (7) and (8) as

 $$ Bu=b\quad 爻 \quad B=\mathbf{I}-\tau A $$ 

where the high dimensional vector  $ \boldsymbol{b} $ (resp.  $ \boldsymbol{u} $) contains all components of the kinetic equations or their numerical representation at time  $ t(t + \tau) $.

The task is now to find an approximation  $ u_n $ of  $ u $, with  $ \|u_u - u\| < \mathrm{tol}_S $. Here, we want to approximate the solution of Eq. (7) by means of the following finite element type Galerkin method: