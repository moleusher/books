### 2.1 Techniques in One Spatial Dimension Revisited

Starting in 1989, Deuflhard and Wulkow [10, 33] have developed adaptive discrete Galerkin techniques, both global and localized spectral methods, with and without weighting, for use in polymer chemistry. In that application field, one spatial dimension, the polymer chain length, say, arose naturally. In the present section, we want to revisit these techniques in view of their applicability for CME simulations, leaving the multiple dimensional case to the subsequent Section 2.2. For the sake of completeness, we want to mention that, in 2006, Engblom [13] has developed a subset of comparable techniques in the setting of MOL, obviously without knowledge of the earlier references.

The following setup is defined in terms of a weight function  $ \psi(x;\rho) $, where  $ x \in \mathbf{N} $ is a discrete variable and  $ \rho $ a characterizing parameter, which may be time dependent in the so-called “moving weight function” concept, see [10], so that then  $ \rho = \rho(t) $. This weight function gives rise to the inner product

 $$ \begin{array}{r c l}{\langle u,v\rangle_{\psi}}&{=}&{\displaystyle\sum_{x\in\mathbf{N}^{d}}u(x)v(x)\psi(x;\rho).}\\ \end{array} $$ 

inducing some weighted norm  $ \|u\|_{\psi}^2 = \langle u, u \rangle_\psi $ thus defining some discrete Hilbert space (sequence space)

 $$ \begin{array}{r l r}{\mathcal{H}_{\psi}}&{=}&{\left\{u:\mathbf{N}\rightarrow\mathbf{R}:\|u\|_{\psi}<\infty\right\}.}\end{array} $$ 

As a basis in this Hilbert space, we may define orthogonal polynomials  $ \{q_{k}\} $ such that

 $$ \langle q_{k},q_{l}\rangle_{\psi}=\gamma_{k}\delta_{k l} $$ 

with normalizing constants  $ \gamma_{k} > 0 $.

Examples of weight functions and orthogonal polynomials. In [10], the weight function

 $$ \begin{array}{r c l}{\psi(x,\rho)}&{=}&{(1-\rho)\rho^{x},\quad\rho<1\;,}\\ \end{array} $$ 

has been suggested, giving rise to so-called discrete Laguerre polynomials. In  $ [10, 13] $, so-called Charlier polynomials have been worked out corresponding to the weight function

 $$ \begin{array}{r c l}{\psi(x,\rho)}&{=}&{e^{-\rho}\cdot\frac{\rho^{x}}{x!},\quad\rho>0\;.}\\ \end{array} $$ 