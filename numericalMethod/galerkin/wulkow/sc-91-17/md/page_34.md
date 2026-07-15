initial step size is  $ 10^{-3} $ and increases in time to a scale of 1. It can be shown, that

 $$ ||\nabla||_{\rho,\alpha}\to\infty\mathrm{~,~}\alpha\mathrm{~f i x e d,~}\rho\to0\mathrm{~.~} $$ 

This would result in time steps tending to zero in general cases, but insertion of  $ \rho\alpha = t $ (the parameter of the Poisson distribution) shows, that the step sizes may tend to one. The behavior of the error estimation compared to the true error for TOL=0.1 is presented in Figure 3.

<div style="text-align: center;"><img src="imgs/img_in_image_box_346_560_817_855.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">Figure 2: Moving Poisson distribution emerging from an initial geometric distribution</div>


Remark. Due to the properties of the Gauss summation, it does not matter to replace the analytical properties (here: Corollary 2.5) of the discrete Laguerre polynomials applied to the difference operator by a numerical summation. Then the example can be extended to a reversible process with s-dependent reaction probabilities. In [26], p. 292, a master equation describing a birth-death-process from chemistry is given by

 $$ u_{s}(t)=w(s-1,s-2)u_{s-1}(t)+w(s-1,s)u_{s+1}(t)-(w(s,s-1)+w(s-2,s-1))u_{s}(t) $$ 

with transition probabilities

 $$ \begin{array}{r c l}{w(s,s-1)}&{=}&{a k_{1}(s-1)+k_{2}^{\prime}c\;,}\\ {w(s,s+1)}&{=}&{k_{1}^{\prime}(s+1)s+k_{2}b(s+1)}\\ \end{array} $$ 