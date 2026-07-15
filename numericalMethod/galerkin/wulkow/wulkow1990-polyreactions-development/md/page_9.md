with parameters 0 <  $ \rho $ < 1 and  $ \alpha > -1 $ has the following properties for special choices of  $ \rho $ and  $ \alpha $:

For  $ \alpha = 0 $,  $ \Psi_{\rho,\alpha}(s) $ is the Schulz-Flory distribution.

For  $ \alpha = \lambda/\rho $ and  $ \rho \to 0 $,  $ \Psi_{\rho,\alpha}(s) $ converges to a Poisson distribution with parameter  $ \lambda $.

For  $ \alpha < 0 $ and  $ \rho \to 1 $,  $ \Psi_{\rho,\alpha}(s) $ approximates a hyperbola of the form  $ 1/s^{\alpha} $.

An examination of the dispersion coefficient  $ d $ of  $ \Psi_{\rho,\alpha}(s) $ turns out, that it is possible to vary  $ d $ continuously from  $ d = 1 + \varepsilon $,  $ \varepsilon > 0 $, to  $ d \to \infty $ dependent on  $ \rho $ and  $ \alpha $. The truncation index  $ n $ can be kept small by a choice of  $ \rho $ and  $ \alpha $ based on an extended moving weight function concept. The weight function (7) generates the so-called modified discrete Laguerre polynomials  $ l_k(s; \rho, \alpha) $ by an expression similar to (3).

Insertion of the expansion

 $$ \tilde{u}_{s}^{n}:=\Psi_{\rho,\alpha}(s)\sum_{k=0}^{n}a_{k}l_{k}(s;\rho,\alpha), $$ 

into (6) leads to an algebraic linear system (called Galerkin equations) for the coefficients  $ a_k $. In each time-step the index  $ n $ and the parameters  $ \rho $ and  $ \alpha $ are adapted due to an error control mechanism. The total error  $ \varepsilon_n $ of the Galerkin approximation (8) and the error of the time integration can be controlled separately. Moreover, if one splits  $ \varepsilon_n $ into two parts by writing:

 $$ \varepsilon_{n}^{2}=\varepsilon_{n,P}^{2}+\varepsilon_{n,C}^{2} $$ 

where  $ \varepsilon_{n,P} $ denotes the pure projection error and  $ \varepsilon_{n,C} $ an error introduced by possible perturbations of the coefficients  $ a_k $, it is obvious that  $ \varepsilon_{n,C} > 0 $ does not affect the time-control and the extrapolation as far as the condition  $ \varepsilon_n < TOL $ is fulfilled. This implies the important fact, that analytical properties of the orthogonal polynomials can be replaced by numerical approximations and makes the discrete Galerkin method II applicable to general classes of problems. The required numerical evaluations of very large or infinite sums as in (3) are performed by an adaptive multilevel summation algorithm called SUMMATOR described in [6].

The program CODEX (Countable systems of Ordinary Differential Equations by eXtrapolation) is a research code written in the language C and has the following features:

- order- and step-size control in time

– global error control of the solution