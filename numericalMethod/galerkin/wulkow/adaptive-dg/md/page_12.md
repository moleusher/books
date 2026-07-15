Of course, in this two parameter case, the three statistical moments  $ \nu_0, \nu_1, \nu_2 $ of the weight function  $ \Psi_{\rho, \alpha} $ can be forced to be linearly dependent on the three moments  $ \mu_0, \mu_1, \mu_2 $ of the unknown distribution  $ u $. As a consequence, the parameters  $ \rho, \alpha $ appear to be time dependent.

Wulkow recognized the basic importance and usefulness of  $ \Psi_{\rho,\alpha} $ for general  $ \alpha > -1 $, which led him to employ it for introducing a corresponding scale of discrete Hilbert spaces  $ H_{\rho,\alpha} $. To start with, we slightly redefine the above inner product (3.2) in the form

 $$ (u,v)_{\rho,\alpha}=\sum_{s=1}^{\infty}u(s)v(s)\Psi_{\rho,\alpha}^{-1}. $$ 

This induces an associated norm  $ \|\cdot\|_{\rho,\alpha} $ and the scale of weighted sequence spaces

 $$ \begin{array}{r l}{H_{\rho,\alpha}:=\{u\in\mathbb{R}^{\mathbb{N}}|}&{{}||u||_{\rho,\alpha}=\displaystyle\sum_{s=1}^{\infty}u(s)^{2}\Psi_{\rho,\alpha}^{-1}<\infty\}.}\end{array} $$ 

In this notation the solution sequence u to be approximated must satisfy the condition

 $$ u\in H_{\rho,\alpha}. $$ 

The corresponding embeddings for the scale of spaces are

 $$ H_{\rho,\alpha}\hookrightarrow H_{\bar{\rho},\alpha},\quad0<\rho<\bar{\rho}<1, $$ 

and

 $$ H_{\rho,\alpha}\hookrightarrow H_{\rho,\beta},\quad-1<\alpha<\beta. $$ 

As it turns out, the parameter  $ \rho $ is needed to guarantee existence, uniqueness and regularity of the solution, whereas the parameter  $ \alpha $ characterizes the “distance” to the geometric distribution in terms of  $ \rho $. In order to understand why not a single Hilbert space is enough to characterize the solvability of a CODE, just consider the operator

 $$ (A_{1}u)_{s}=-(s-1)u_{s} $$ 

which appears in the above Example 1. It is an easy task to verify that the linear operator  $ A_1 $ is not bounded in  $ H_{\rho,0} $ for fixed parameter  $ \rho $, but Lipschitz continuous over the scale of spaces  $ H_{\rho,0} $ for varying  $ \rho $ in the sense that

 $$ ||A_{1}u||_{\rho,\theta}\leq\frac{C}{\epsilon}||u||_{\rho-\epsilon,\theta}\qquad,\qquad\epsilon>0\quad. $$ 

As a consequence, nonlinear operators will not be expected to be characterizable via a traditional Lipschitz condition, but rather by an extension of the above property (4.7). This motivates the following theorem due to [18, 19].