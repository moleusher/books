Terms in the above right-hand side where the argument  $ (x - \nu_m) $ contains negative entries, have to be omitted. Hence, for convenience we set

 $$ \alpha_{m}(x)=0\quad\mathrm{a n d}\quad p(t,x)=0\quad\mathrm{f o r~a l l}\quad x\not\in\mathbf{N}^{d}. $$ 

Upon defining the infinitesimal generator

 $$ \begin{array}{r c l}{\big(\mathcal{A}p(t,\cdot)\big)(x)}&{=}&{\displaystyle\sum_{m=1}^{M}\alpha_{m}(x-\nu_{m})p(t,x-\nu_{m})-\alpha_{m}(x)p(t,x),}\\ \end{array} $$ 

and setting  $ p(t) = p(t, \cdot) $, the CME can be rewritten in operator form as the abstract Cauchy problem

 $$ \begin{array}{r c l c r}{\partial_{t}p(t)}&{=}&{\mathcal{A}p(t),}&{\quad p(0)=\phi\;.}\\ \end{array} $$ 

In mathematical terms, the CME may be understood either as a countable system of ODEs (often abbreviated as CODEs) or, equivalently, as a discrete partial differential equation (PDE), wherein the continuous derivatives are replaced by discrete differences. The theory of CODEs strongly indicates that they are structurally quite distant from ODE systems, even of high dimension, but quite close to PDEs.

Upon adopting the discrete PDE point of view, we are naturally led to consider adaptive discrete Galerkin methods as first introduced by Deuflhard and Wulkow [10, 36] and later pursued by Wulkow in his thesis [33, 34]. Surveys on the development of the topic since then can be found in [35, 11]. However, the numerical challenge in solving the CME is its high-dimensionality, even for reaction systems with a relatively small number d of species. Therefore, modifications of the original ideas of discrete Galerkin methods will be necessary in the present context. For later purposes we already note that the equations (1.1) or (1.3) for the probability distributions are linear, a special structure that will be useful for the construction of algorithms.

### 1.2 Dynamic State Space Adaptivity

Assume the exact CME solution p is contained in some Hilbert space H and can be represented in terms of basis functions  $ \{q_k\} $, which span H, so that

 $$ \begin{array}{r c l}{p(t,x)}&{=}&{\displaystyle\sum_{k=0}^{\infty}a_{k}(t)q_{k}(t,x)\in\mathcal{H}.}\\ \end{array} $$ 