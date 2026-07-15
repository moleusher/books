Due to the bistability of the toggle switch, the solution of the corresponding CME is a bimodal PDF. Bimodality is of prime importance in many biological applications since it indicates the presence of two different scenarios or macro-states, and it is crucial that a numerical method constructed for solving the CME captures the bimodality correctly.

In [31], the parametrisation

 $$ \begin{array}{r c l c r c l c r c l}{c_{1}}&{=}&{c_{4}}&{=}&{3\cdot10^{3}s^{-1},}&{}&{c_{2}}&{=}&{c_{5}}&{=}&{1.1\cdot10^{4},}\\ {c_{3}}&{=}&{c_{6}}&{=}&{0.001s^{-1},}&{}&{\beta}&{=}&{\gamma}&{=}&{2}\\ \end{array} $$ 

has been used, and both the stationary distribution and the time-dependent solution in the interval  $ [0, 10^{4}] $ have been computed on the domain  $ [0, 399] \times [0, 399] $. Instead of solving the full discrete CME, however, the authors presented an approximation of the Fokker-Planck equation, a PDE known to be, in some sense, the continuous counterpart of the CME (see, e.g., [14]). In the case of the genetic toggle switch, this may yield a reasonable approximation, but in situations where the discrete nature of the reaction system is crucial (cf. [24, 32]), replacing the CME by the Fokker-Planck equation causes a large modelling error in addition to the numerical approximation error. Hence, the approach proposed in [31] can actually not be considered as a viable method for the CME, but rather as a method for the Fokker-Planck equation.

The genetic toggle switch has been investigated again in [13]. There, a computation based on the full CME has been presented, but the computational domain had to be decreased to approximately  $ [0, 200] \times [0, 200] $ by a rescaling of the parameters. Note that, by construction, our adaptive discrete Galerkin method does not require any such downscaling.

The following simulations have been performed with a special 2d-version of the program package PREDICI $ ^{\circledR} $. In our first example, the full CME of (3.26) with parameters (3.28) was solved up to a predefined tolerance of 0.03. As an initial distribution, the product Gaussian

 $$ \frac{1}{2\pi\sigma_{1}\sigma_{2}}\exp\left(-\frac{(x_{1}-\mu_{1})^{2}}{2\sigma_{1}^{2}}\right)\exp\left(-\frac{(x_{2}-\mu_{2})^{2}}{2\sigma_{2}^{2}}\right) $$ 

has been evaluated and normalized on the discrete state space for  $ \mu_1 = \mu_2 = 133 $ and  $ \sigma_1 = \sigma_2 = \sqrt{133} $. Figure 3 shows the PDF at  $ t = 6 \cdot 10^4 $. By this time, the PDF has almost converged to the stationary distribution, and a comparison of Figure 3 with the right panel of Figure 3 in [31] shows indeed a very good agreement. The bimodality is clearly visible and indicates the relevant biological information, namely the bistability of the toggle switch.