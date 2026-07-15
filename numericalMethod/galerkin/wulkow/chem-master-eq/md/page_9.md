costly L-stable family and a cheaper, only A-stable one. On the basis of extensive numerical tests in polyreaction kinetics, we select the A-stable one characterized by the rational stability function

 $$ \begin{array}{r l r}{R(z)}&{=}&{\frac{1}{1-z}\left(1-\frac{1}{2}\frac{z^{2}}{1-z}\right).}\end{array} $$ 

It is easy to verify that  $ R(z) $ is of second order for  $ \tau \to 0 $ and exhibits A-stability, but not L-stability, since  $ R(\infty) \neq 0 $. Let  $ u_2 $ denote the second order PDF approximation which is obtained by

 $$ \begin{array}{r l r}{u_{2}}&{=}&{R(\tau\mathcal{A})u_{0}=(\mathcal{I}-\tau\mathcal{A})^{-1}u_{0}-\frac{1}{2}(\mathcal{I}-\tau\mathcal{A})^{-2}(\tau\mathcal{A})^{2}u_{0},}\end{array} $$ 

where I denotes the identity operator. Formally, this equation is a continuous boundary value problem that can be treated by adaptive Galerkin discretization thus finally leading to algebraic systems of the kind as in (1.6).

The above time discretization scheme is not solved in the clumsy form  $ (1.7) $, but in a modified form that incorporates an easily accessible temporal error estimate. To derive this form,  $ u_{2} $ is split into two parts according to

 $$ \begin{array}{r l r}{u_{2}}&{{}=}&{u_{1}+\Delta u_{1},}\end{array} $$ 

where  $ u_1 $ is the solution of the implicit Euler scheme  $ (\mathcal{I} - \tau \mathcal{A}) u_1 = u_0 $, or equivalently

 $$ \begin{array}{r c l}{(\mathcal{I}-\tau\mathcal{A})\Delta u_{0}}&{=}&{\tau\mathcal{A}\;u_{0},}\\ {u_{1}}&{=}&{u_{0}+\Delta u_{0},}\\ \end{array} $$ 

and  $ \Delta u_{1} $ is the solution of

 $$ (\mathcal{I}-\tau\mathcal{A})\Delta u_{1}\quad=\quad-\frac{1}{2}(\mathcal{I}-\tau\mathcal{A})^{-1}(\tau\mathcal{A})^{2}\;u_{0}\quad=\quad-\frac{\tau}{2}\mathcal{A}\;\Delta u_{0}. $$ 

Since  $ u_{2} $ is of second order, while  $ u_{1} $ is of first order, we may use

 $$ \begin{array}{r l r}{\mathrm{e p s}_{T}}&{=}&{\|\Delta u_{1}\|,}\end{array} $$ 

defined in some suitable norm, as a cheaply available temporal error estimate. As in the finite dimensional ODE case, a new time step  $ \tau_{new} $ is then proposed on the basis of an old timestep  $ \tau $; with temporal error estimate  $ \epsilon_{T} $ and prescribed error tolerance TOL we arrive at the estimate for the new timestep

 $$ \begin{array}{r l r}{\tau_{\mathrm{n e w}}}&{=}&{\sqrt{\rho\frac{\mathrm{T O L}}{\mathrm{e p s}_{T}}}\tau,}\end{array} $$ 