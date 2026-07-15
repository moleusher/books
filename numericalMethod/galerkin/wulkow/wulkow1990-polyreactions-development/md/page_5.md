## 2 Discrete Galerkin Method I – MACRON

Let  $ u_s(t) $ denote the concentration (or number) of macromolecules (e.g. polymer molecules) of chain length or size s at a time t. The sequence  $ u_1(t) $,  $ u_2(t) $, ..., can be considered as a chain length distribution. The kinetics of a macromolecular reaction process (neglecting additional chemical reactions) can be expressed by a countable system of ordinary differential equations of the form (the prime denotes the derivative with respect to the time t):

 $$ u_{s}^{\prime}(t)=f_{s}(u_{1}(t),u_{2}(t),\ldots)\quad,s=1,2,\ldots, $$ 

in terms of right-hand side functions  $ f_s $. An initial distribution  $ u_s(0) $ is given. The index  $ s $ may formally range up to infinity and is set to about  $ 10^4 - 10^6 $ in realistic examples.

Assume that the distribution  $ u_{s}(t) $ can be expanded in a series

 $$ u_{s}(t)=\Psi_{\rho}(s)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s;\rho),s=1,2,\cdots, $$ 

where  $ \Psi_{\rho}(s) $ is a positive weight function with a (possibly time-depending) real parameter  $ \rho $ and the  $ l_{k}(s;\rho) $,  $ k=0,1,\ldots $, are polynomials of a discrete variable s. These polynomials are associated with  $ \Psi_{\rho}(s) $ by the orthogonality relation

 $$ \sum_{s=1}^{\infty}l_{j}(s;\rho)l_{k}(s;\rho)\Psi_{\rho}(s)=\left\{\begin{array}{c c}{\gamma_{k}^{\rho},}&{\mathrm{i f~}j=k}\\ {0,}&{\mathrm{i f~}j\neq k}\\ \end{array}\right.,\quad\gamma_{k}^{\rho}>0,\quad j,k=0,1,2,\ldots. $$ 

Truncation of the expansion (2) after n+1 terms leads to a Galerkin approximation

 $$ u_{s}^{n}(t):=\Psi_{\rho}(s)\sum_{k=0}^{n}a_{k}(t)l_{k}(s;\rho),s=1,2,\cdots, $$ 

depending on the parameter  $ \rho $ and the truncation index n. As pointed out in [5], the (projection) error of the approximation (4) can be efficiently estimated.

By inserting expansion (2) into the system (1) and by use of certain analytical properties of the orthogonal polynomials (see e.g. [6]), a (comparatively small) system of ordinary differential equations (ODE's) for the expansion coefficients  $ a_k(t) $ can be derived. This procedure is called analytical preprocessing.

In many applications the weight function  $ \Psi_{\rho}(s) $ can be chosen as the geometric (in polymer chemistry also called Schulz-Flory) distribution with parameter  $ \rho $. This distribution is associated with the discrete Laguerre polynomials. The selection of the parameter  $ \rho = \rho(t) $ is done adaptively on the basis of the so-called moving weight function concept [5], [6]. This leads to small truncation indices ( $ n \approx 10 $) in many cases and to a fast and efficient treatment of reactions connected in some way