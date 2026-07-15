The time-dependence of the basis functions is realized, e.g., by parametrization with respect to a time-dependent variable or by an adaptive discretization of space in each step. Upon formally truncating this expansion, we naturally arrive at some approximation  $ p_r(t) \in \mathcal{H}_r \subset \mathcal{H} $ called the Galerkin approximation

 $$ \begin{array}{r c l}{p_{r}(t,x)}&{=}&{\displaystyle\sum_{k=0}^{r}a_{k}^{[r]}(t)q_{k}(t,x)\in\mathcal{H}_{r}\subset\mathcal{H}.}\\ \end{array} $$ 

In special cases, one can even guarantee that  $ a_{k}^{[r]} = a_{k} $, i.e. that the coefficients are independent of the truncation index. For ease of writing we will drop this notational difference whenever it is clear enough from the context.

Crucial details to be set in this approximation frame are:

• choice of basis functions  $ \{q_{k}\} $,

• choice of truncation index r,

- computation of expansion coefficients  $ \{a_k^{[r]}(t)\} $ via the discrete PDE (1.3).

In what follows, we will only discuss the last two points. The first point is left to the subsequent Section 2.

Method of lines (MOL): first space, then time. This approach is the most popular one to tackle PDEs. After discretization of the state space, we are left with a sequence of finite dimensional initial value problems for ODEs.

Given a fixed truncation subspace  $ \mathcal{H}_r $, we insert the corresponding representation (1.5) into the CME (1.1), which leads us to evolution equations for the expansion coefficients  $ a_k(t) $. For details, the reader may refer to [10]. In chemical reaction kinetics, the resulting ODEs are typically stiff and must therefore be solved by some implicit numerical integration scheme; note that, due to the linearity of the discrete PDE, there is no difference between implicit and linearly implicit integration schemes. For example, the implicit Euler method for stepsize  $ \tau $ leads to a linear algebraic system of the kind

 $$ \begin{array}{r c l}{(\Gamma_{r}-\tau A)\Delta\eta_{0}}&{=}&{\tau A\;\eta_{0},}\\ {\eta_{1}}&{=}&{\eta_{0}+\Delta\eta_{0},}\\ \end{array} $$ 