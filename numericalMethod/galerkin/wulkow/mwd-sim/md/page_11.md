ordinary differential equation in an appropriate sequence space. The theoretical reason for such an approach is given by semigroup theory  $ {}^{22} $. For an approximation  $ u_1 $ of the solution  $ u(t + \tau) $ after a time step from  $ t $ to  $ t + \tau $, we apply the semi-(linear)-implicit Euler  $ {}^{23} $ scheme

 $$ \begin{array}{l} (I - \tau A)\Delta u  =  \tau f(\varphi)\\ \\ u_{1}=(\varphi + \Delta u \end{array} $$ 

with  $ \varphi = u(t) $, A the derivative  $ f_u(\varphi) $ and I the identity matrix. We obtain a linear system which seems as difficult to be solved as the original differential equation (3) because of its high dimension. Moreover, each time discretization introduces a certain time error  $ \varepsilon_T $ which an adaptive stepsize control tries to keep below a tolerance  $ \tau_L $. For standard differential equations, system (7) can be solved within the machine accuracy, so the time steps have to be chosen only with respect to  $ \tau_L $. The idea of Bornemann is that the trajectory of the solution  $ u(t) $ in an abstract space  $ X $ (e.g. a function or sequence space) may be slightly perturbed without affecting stepsizes and accuracy (Fig. 1).

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_599_573_872.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Fig. 1. Idea of the Rothe method. The sizes of the ellipses denote the stationary tolerance for an in-exact method, their centers indicate the results of “exact” time steps</div>


If we assume, that the solution of Eq. (7) can only be approximated, the time error  $ \varepsilon_{\mathrm{T}} $ and the stationary error  $ \varepsilon_{\mathrm{S}} $ can be matched such that the complete time step is within accuracy  $ \tau_{0} $. It is the special feature of the Rothe method, that the stationary tolerance  $ \tau_{0} $ for the error  $ \varepsilon_{\mathrm{S}} $ need not be too small, when an appropriate discretization scheme is used. Bornemann's multiplicative error correction (MEC) (given by the formulas (7) and (8)) is here the method of choice, because it avoids differences at the computation of the error estimates. The theory for linear systems leads to  $ \tau_{0} $s = 1/8  $ \tau_{0} $l (instead of  $ \tau_{0} $s = 0.001  $ \tau_{0} $l for extrapolation methods); for nonlinear systems, the setting  $ \tau_{0} $s = 1/16  $ \tau_{0} $l has been sufficient for a large range of problems (a reasonable value for  $ \tau_{0} $l is here between 0.1–0.01).

The required estimate  $ \eta_1 $ of the time error  $ \|u_1 - u(t + \tau)\| $ ( $ | \dots | $ an appropriate norm) can be computed by solving a correction equation with the same left-hand side matrix as in Eq. (7)