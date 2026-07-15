P. DEUFLHARD $ ^{1} $ W. HUISINGA $ ^{2} $ T. JAHNKE $ ^{3} $ M. WULKOW $ ^{4} $

# Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation

# Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation¶

P. Deuflhard W. Huisinga T. Jahnke M. Wulkow

April 5, 2007

## Abstract

In systems biology, the stochastic description of biochemical reaction kinetics is increasingly being employed to model gene regulatory networks and signalling pathways. Mathematically speaking, such models require the numerical solution of the underlying evolution equation, also known as the chemical master equation (CME). Up to now, the CME has almost exclusively been treated by Monte-Carlo techniques, the most prominent of which is the simulation algorithm suggested by Gillespie in 1976. The paper presents an alternative, which focuses on the discrete partial differential equation (PDE) structure of the CME and thus allows to adopt ideas from adaptive discrete Galerkin methods as first suggested by Deuflhard and Wulkow in 1989 for polyreaction kinetics and independently redetected for the CME by Engblom in 2006. Among the two different options of discretizing the CME as a discrete PDE, Engblom had chosen the method of lines approach (first space, then time), whereas we strongly advise to use the Rothe method (first time, then space) for clear theoretical and algorithmic reasons. Numerical findings at two rather challenging problems illustrate the promising features of the proposed method and, at the same time, indicate lines of necessary further improvement of the method worked out here.

Keywords. adaptive discrete Galerkin methods, adaptive Rothe method, discrete Chebyshev polynomials, stochastic reaction kinetics, chemical master equation

## Contents

Introduction 3  
  
1 Preliminary Considerations 4  
1.1 Chemical Master Equation as Discrete PDE 5  
1.2 Dynamic State Space Adaptivity 6  
  
2 Realization of Discrete Galerkin Methods 10  
2.1 Techniques in One Spatial Dimension Revisited 11  
2.2 A Tensor Product Approach to Multiple Dimensions 16  
  
3 Numerical Examples 22  
3.1 Bistable Toggle Switch 23  
3.2 A Challenging Test Problem 29  
  
Conclusion 32  
  
References 33

## Introduction

In recent years, based on the insight that stochastic effects are of crucial importance in the understanding of gene regulatory networks and signalling cascades, an increasingly growing interest in stochastic modelling approaches to chemical reaction kinetics arose [12, 29, 26, 27]. As a consequence, the design of efficient numerical techniques and reliable approximations schemes for the solution of the chemical master equation (CME) is now an active field of research. Almost exclusively, these approaches treat the CME via Monte-Carlo techniques, generating a statistically large ensemble of realizations of the associated continuous-time / discrete-state-space Markov jump process. The most prominent of these approaches is the stochastic simulation algorithm due to Gillespie in [20, 17]. This algorithm, however, requires an update of the system at each time when one of the reaction channels fires, thus causing enormous computational cost in the case of highly reactive systems. Therefore, research has mainly concentrated on how to improve the efficiency of this kind of algorithm (cf. [16, 19, 5, 28, 1, 21, 6, 30]). In contrast to this line of research, a method for solving the CME by a dynamical low-rank approximation has recently been introduced by Jahnke and Huisinga [24].

The present paper deals with an alternative idea based on a change of perspective. In fact, from a mathematical point of view, the CME may be understood as a countable system of ordinary differential equations (CODE) or, equivalently, as a discrete partial differential equation (PDE). For its numerical treatment, the main challenge is the fact that each single state of the state space corresponds to one degree of freedom in the CME. Even in case of a small system containing, e.g., only three molecular species and at most  $ 10^2 $ copy numbers per species, a total number of  $ (10^2)^3 = 10^6 $ coupled ordinary differential equations (ODEs) has to be solved.

This situation is comparable to the one in polyreaction kinetics: There, too, single molecules (monomers) are linked together to long chains whose dynamical mathematical description gives rise to huge numbers of ODEs, say up to  $ 10^4 - 10^6 $ in realistic examples, sometimes even not known in advance. Among the present authors, Deuflhard and Wulkow have a long standing expertise in modelling and efficient simulation of polymer kinetics [10, 33, 36, 34, 23, 11, 35], which have materialized in a number of comprehensive numerical solvers and user-friendly software tools, which certainly are among the best in the field [7, 35]; in fact, there were speed-up factors of about  $ 10^4 $. However, as a distinguishing feature, polymerization systems possess a natural coordinate, the polymer chain length. For this reason, the

techniques used in polyreaction kinetics will need some thorough reconsideration in our present context. A first step in this direction has been performed recently by Engblom [13], obviously unaware of the above quoted more general work. He has worked out a method of lines (MOL) approach, i.e. first state space discretization, then time discretization, so that one is left with a system of ordinary differential equations (ODEs). In what follows, we propose an approach in the frame of a Rothe method (ROM), i.e. first time discretization, then state space discretization, which leads to a sequence of boundary value problems and thus conveniently allows for adaptively chosen state subspaces. This so-called adaptive Rothe method has been introduced by Bornemann [4, 2] in 1990 for scalar parabolic equations and extended by Lang to parabolic systems of reaction-diffusion type up to challenging real life problems [25]. Already in 1992, Wulkow had transferred the approach to polyreaction kinetics in his thesis [33, 34]. The ROM will be combined with a Galerkin h-p-mehod in higher dimensions which already has been successfully applied to similar problems with continuous property coordinates [22].

The article is organized as follows. In Section 1, we first set the scene and introduce the chemical master equation focusing on its discrete PDE structure. Moreover, we discuss the two possible discretization options for this discrete PDE, the MOL and the ROM, in view of adaptivity with respect to state space. On this basis, in Section 2, we work out details of discrete Galerkin methods for the CME. Adaptive Galerkin methods in one dimension are recalled to necessary detail and extended via a tensor product approach to multiple dimensions. For the arising reduced linear systems to be solved, they require the efficient numerical evaluation of matrix elements and right-hand sides, where Gauss-Christoffel summation plays an important role. Finally, in Section 3, we apply our approach to two challenging model problems exhibiting typical features of stochastic reaction kinetics of variable degree.

## 1 Preliminary Considerations

In this section, we first formulate the chemical master equation (CME) and reveal its structure as a discrete partial differential equation (PDE). From this perspective, we then discuss two options concerning the order of time and state space discretization in view of adaptivity.

### 1.1 Chemical Master Equation as Discrete PDE

Consider a well-mixed system of volume V with d chemical species  $ S_1, \ldots, S_d $ involved in M reactions  $ R_1, \ldots, R_M $. The state of the system is characterized by the numbers  $ X_i(t) $ of molecules of  $ S_i $. In the stochastic modelling approach treated here, the discrete variable

 $$ X(t)=(X_{1}(t),\cdots,X_{d}(t)) $$ 

is understood to be random. The reaction probability for each reaction  $ R_j $ is specified by the propensity function  $ \alpha_j = \alpha_j(X(t), t) $, which is equal to the product of a rate constant  $ c_j $ and the number of possible combinations of reactant molecules involved in reaction  $ R_j $. The most frequently arising reaction types are listed in Table 1.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>chemical reaction</td><td style='text-align: center; word-wrap: break-word;'>$ \alpha_{j} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} + S_{b} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t)X_{b}(t) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} + S_{a} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t)(X_{a}(t)-1)/2 $</td></tr></table>

<div style="text-align: center;">Table 1: Stochastic propensity functions</div>


Once a reaction  $ R_j $ takes place, the number of molecules for each species changes according to the stoichiometric vector  $ \nu_j \in \mathbf{N}^d $, i.e.,  $ X(t) \to X(t) + \nu_j $. Note that the first two propensity terms above have the same form as in the continuous case, while the third one clearly reveals the discrete nature of the process.

Following [20, 18, 14], the time evolution of the probability distribution function (PDF)

 $$ \begin{array}{r l r}{p(t,x)}&{=}&{\mathrm{P}\big[X_{1}(t)=x_{1},\dots,X_{d}(t)=x_{n}\big],\quad x\in\mathbf{N}^{d}}\end{array} $$ 

of the random variable  $ X(t) $ is described by the chemical master equation (CME)

 $$ \begin{array}{r c l}{\partial_{t}p(t,x)}&{=}&{\displaystyle\sum_{m=1}^{M}\alpha_{m}(x-\nu_{m})p(t,x-\nu_{m})-\alpha_{m}(x)p(t,x)\;.}\\ \end{array} $$ 

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

where  $ \Gamma_r \in \mathbf{R}^{r \times r} $ denotes the “mass” matrix,  $ A \in \mathbf{R}^{r \times r} $ is a “stiffness” matrix representing the Galerkin discretization of the generator  $ \mathcal{A} $, the vectors  $ \eta_i $,  $ i = 0, 1, \in \mathbf{R}^r $ contain the Galerkin coefficients, and  $ \Delta \eta_0 = \eta_1 - \eta_0 $ is the corresponding difference. Note that the given initial values  $ \eta_0 $ correspond to some  $ p_r(t) \in \mathcal{H}_r $. However, there is no guarantee that  $ \eta_1 $ can also be associated with some  $ p_r(t + \tau) \in \mathcal{H}_r $. If necessary, the stepsize  $ \tau $ must be reduced until this condition can be satisfied.

By construction, the subspace  $ \mathcal{H}_r $ has to be kept unchanged over the integration step in this approach. A change of the subspace after an integration step is possible, but a rather subtle task requiring a careful control of interpolation errors. Moreover, earlier computations in polyreaction kinetics have confirmed the undesirable experience that, already after one integration step, the approximation tends to “leave” the preassigned subspace  $ \mathcal{H}_r $ with the consequence of either extremely small timesteps or oscillatory numerical artifacts. For this reason, a “moving weight function” concept has been introduced in [10] which results in adaptive time dependent basis functions  $ \{q_k(t)\} $. A comparable approach has also recently been introduced by Engblom [13] in his special case without knowing about the earlier more general results in [10]. However, on the basis of numerical experience and theoretical investigations in [33], the MOL approach as a whole has turned out to be not sufficiently robust for complex polyreaction kinetics. For the same reason, we abandon this approach in the present context.

Rothe method (ROM): first time, then space. This approach has been introduced and theoretically backed for parabolic PDEs by Bornemann in his thesis [4, 2] and immediately transferred to polyreaction kinetics by Wulkow in his thesis [33, 34]. After discretization in time first, we are left with a sequence of continuous boundary value problems.

For linear problems, as the discrete PDEs of interest here, Bornemann [3] had even designed a special time integration scheme, which we recall for the convenience of the reader. We start from the abstract Cauchy problem (1.3) in terms of the generator  $ \mathcal{A} $ and given values  $ u_0 = p_r(t) \in \mathcal{H}_r $ for some Hilbert space  $ \mathcal{H}_r $ associated with the previous time point  $ t $. Let  $ u_i $,  $ i = 1, 2 $, denote approximations  $ p_r' \in \mathcal{H}_r' $ for some Hilbert space  $ \mathcal{H}_r' $ associated with the new time point  $ t + \tau $. A distinguishing feature between MOL and ROM is that, in the ROM, the Galerkin subspace  $ \mathcal{H}_r' $ can be adapted to the PDF solution  $ p(t + \tau) $, with  $ r' \neq r $ in general. In [3], several implicit time discretizations have been described in terms of some discrete time evolution  $ R(\tau \mathcal{A}) $ (for this notation compare, e.g., the textbook [8]). There is a more

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

wherein  $ \rho < 1 $ is an additional safety factor. This timestep control can be used for finite-dimensional ODE systems as well as for infinite dimensional CODEs.

The trick in the infinite dimensional case is that all arising norms of state space terms can be approximated to prescribed accuracy within the Galerkin setting. Suppose we are given some Galerkin subspace  $ \mathcal{H}_r $; then we may compute an associated spatial error estimate (details to be worked out in the Section 2 below)

 $$ \left\| \mathbf{p}_{r}-\mathbf{p} \right\|\leq TOL_{p}. $$ 

Here TOL $ _{p} $ is an imposed spatial error tolerance. In [3], Bornemann linked this error tolerance to the user-specified tolerance TOL, on the basis of approximation theory, as

 $$ \mathrm{TOL}_{p}=c\frac{1}{8}\mathrm{TOL} $$ 

to ensure reliable working of the time step control The factor  $ c < 1 $ can be considered as a safety factor, a choice of  $ c = 1/4 $ covers linear and quadratic problems with sufficient accuracy.

As already mentioned above, the ROM permits an easy adaptation of Galerkin subspaces for the solution of the arising boundary value problems (1.8) or (1.9). Moreover, this method is also clearly preferable for theoretical reasons that are elaborated in [4, 33]. Numerical evidence in polyreaction kinetics simulations clearly confirms that the above mentioned difficulty of “leaving” the subspace (as apparent in MOL) is significantly reduced, see again [33]. In connection with the “moving weight function” concept, ROM turned out to be both robust and extremely well-suited for spatial and temporal adaptivity in complex real life problems. On this basis, we suggest this approach also for the present context of the CME.

## 2 Realization of Discrete Galerkin Methods

In this section, we work out details on the choice of basis functions  $ \{q_k\} $. Given an inner product associated with the Hilbert spaces  $ \mathcal{H}_r \subset \mathcal{H} $, which may be weighted or unweighted, we arrive at orthogonal systems of polynomials of discrete variables. For this purpose, we partly recall material already given in [10, 33] and modify it for use in the present CME context.

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

In [36, 34], a two-parameter family of polynomials has been designed to be associated with the two-parameter weight function

 $$ \begin{array}{r c l}{\psi(x)}&{=}&{(1-\alpha)^{1+\beta}\left(\begin{matrix}{x_{i}+\beta}\\ {x}\\ \end{matrix}\right)\alpha^{x},}&{0<\alpha<1,\beta>-1.}\\ \end{array} $$ 

All these choices need to be combined with the so-called “moving weight function” condition that roughly requires the solution to be “similar to the weight function in some prescribed sense, see [10] for general weight function and [13] for the special case. As a consequence, the thus constructed global Galerkin methods are well-suited for monomodal solutions, but less appropriate to bimodal functions, which, however, do arise in important applications. For that reason, Wulkow [34] turned to localized unweighted polynomials, discrete Chebychev polynomials formally corresponding to the weight function

 $$ \psi(x)\quad\equiv\quad1\;. $$ 

It is this latter setting which paved the way to the extreme success of discrete Galerkin methods in polymer chemistry. On this basis, we will suggest the same choice for the CME context—to be treated in the next section for more than one spatial dimension.

Spatial error estimation. Recall the type of global expansion (1.4) for the exact solution p and (1.5) for the Galerkin approximation  $ p_r $. Of course, we will choose the induced Hilbert space norm to get an error estimate  $ \|p_r - p\|_{\psi} $. If the coefficients  $ \{a_k\} $ are independent of the truncation index r, we obtain the exact expression

 $$ \begin{array}{r c l}{\displaystyle\|p_{r}-p\|_{\psi}}&{=}&{\displaystyle\left\|\displaystyle\sum_{k=r+1}^{\infty}a_{k}q_{k}(x;\rho)\right\|_{\psi}=\left(\displaystyle\sum_{k=r+1}^{\infty}|a_{k}|^{2}\gamma_{k}\right)^{1/2}.}\\ \end{array} $$ 

Otherwise, which is the typical case, a straightforward modification can be applied, see [10]. Since, in this norm, the expansion coefficients tend to zero for  $ k \to \infty $, the following spatial error estimate may serve the purpose

 $$ \mathrm{e p s}_{r}=\|p_{r+1}-p_{r}\|_{\psi}=|a_{r+1}|\sqrt{\gamma_{r+1}}. $$ 

Clearly, this error estimate will work fine whenever the expansion coefficients decrease sufficiently fast. Otherwise, the expansion has to be continued a few steps beyond the step  $ r + 1 $.

Algebraic Galerkin equations. At the core of discrete Galerkin methods, algebraic equations must be constructed. For simplicity, we choose the implicit Euler operator equation (1.8) for the first order approximation  $ u_1 = u_0 + \Delta u_0 $. Let the Galerkin approximation of  $ \Delta u_0 $ in  $ \mathcal{H}_r $ be defined in terms of the coefficients  $ \Delta \eta_0 = ((\Delta \eta_0)_1, \ldots, (\Delta \eta_0)_r) $. Upon applying inner products with each orthogonal polynomial, we arrive at the formal relations

 $$ \left\langle\sum_{k=0}^{r}(q_{k}-\tau\mathcal{A}q_{k})(\Delta\eta_{0})_{k},q_{l}\right\rangle_{\psi}=\langle\tau\mathcal{A}u_{0},q_{l}\rangle_{\psi}. $$ 

From this, using orthogonality properties, we obtain algebraic systems of the kind (1.6) already shown in the context of the MOL, i.e.

 $$ \begin{array}{r c l}{(\Gamma_{r}-\tau A)\Delta\eta_{0}}&{=}&{b}\end{array} $$ 

in terms of the  $ r \times r $-matrices

 $$ \Gamma_{r}=\mathrm{diag}(\gamma_{k})\quad and\quad A=(\langle\mathcal{A}q_{k},q_{l}\rangle_{\psi})_{kl} $$ 

and with right-hand side coefficients  $  b = (b_1, \ldots, b_r)  $. In a similar way we obtain coefficients  $ \Delta\eta_1 $ for the Galerkin approximation of the correction  $ \Delta u_1 $. The solution of these linear equations is usually not difficult, since they are of low dimension  $ r $. The difficulty, however, lies in the computation of the matrix elements for  $ \Gamma $,  $ A $ and the vector elements  $ b $, which require infinite sums to be approximated.

Gauss-Christoffel summation. In order to compute the inner products  $ \langle\cdot,\cdot\rangle_{\psi} $ we have to approximate infinite sums. In [9, Section 9.7], an adaptive discrete multigrid algorithm (code SUMMATOR), which has been developed by Wulkow, has been presented to approximate large sums efficiently. In the course of further improvement of the polyreaction algorithms, discrete Gauss-Christoffel methods have been worked out intimately linked to the structure of the weighted inner products. For the trivial weight  $ \psi\equiv1 $, which we suggest to apply in the CME context, this leads to a discrete Gauss-Legendre quadrature, i.e., to a high-order summation technique. On the basis of the theory for Gauss-Christoffel quadrature, the nodes and weights can easily be computed also in the discrete case: Given a truncation index r, a triangular eigenvalue problem must be solved, for details see, e.g., [9]. It has been shown in [34] that the “aliasing error” introduced by the Gauss-Christoffel summation does not affect the quality of a Galerkin approximation of order r, if only at least  $ r+1 $ nodes are used.

Localization and the Galerkin h-p-method in 1d. In practice the global approach outlined above has proven to be too restrictive, in particular when dealing with multi-modal distributions. The herein reviewed Galerkin h-p-method therefore abandons the global approximation strategy—rather, it is based on a localization principle by decomposing the state space into intervals. Furthermore, it chooses the weight function to be the constant function  $ \psi \equiv 1 $. The Hilbert space corresponding to  $ \psi \equiv 1 $ is  $ \mathcal{H}_{\psi} = l^2 $. Square summable distributions  $ p(t) \in l^2 $ do in general not possess bounded statistical moments, which is a desirable property. In order to guarantee bounded statistical moments, we consider the family of Hilbert spaces  $ \mathcal{H}_{\psi}(\cdot, \rho) $ with weight function  $ \psi(x, \rho) = (1 - \rho) \rho^x $ for  $ x \in \mathbb{N} $. It can be shown that the infinitesimal generators corresponding to the CME are typically discrete shift operators that have unique solutions within this family of Hilbert spaces. Basically such operators are Lipschitz-continuous within the scale, but not within one fixed  $ \mathcal{H}_{\psi(\cdot, \rho)} $. Now, if we require  $ p(0) \in \mathcal{H}_{\psi(\cdot, \rho)} $, we can ensure that  $ p(t) $ has bounded statistical moments for  $ t > 0 $.

Consider a partition of the state space N given by

 $$ \begin{array}{r l}{\textbf{N}=}&{{}\left[L^{(1)},U^{(1)}\right]\cup\cdots\cup\left[L^{(M)},U^{(M)}\right]\cup\left[L^{(M+1)},\infty\right)}\end{array} $$ 

with finite discrete intervals  $ I^{(m)} = [L^{(m)}, U^{(m)}] = \{L^{(m)}, L^{(m)} + 1, \ldots, U^{(m)}\} $ and the semi-infinite interval  $ I_{\infty} = [L_{M+1}, \infty) = \{L_{M+1}, \ldots\} $. We assume that  $ L^{(i)} \leq U^{(i)} < L^{(j)} \leq U^{(j)} $ for  $ i < j $, and set  $ L^{(0)} = 0 $ and  $ L^{(m+1)} = U^{(m)} + 1 $. In the sequel, we will describe how to approximate  $ p(t) $ locally on each interval  $ I^{(m)} $. Define  $ p_r^{(m)}(t) $ to be the Galerkin approximation of order  $ r $ to  $ p(t) $ on  $ I^{(m)} $. In general,  $ r $ will depend on the interval  $ I^{(m)} $.

We first consider the semi-infinite interval  $ I^{(\infty)} $. Choosing  $ p_{0}^{(\infty)}(t) \equiv 0 $, the resulting approximation error on  $ I^{(\infty)} $ is

 $$ \begin{array}{r c l}{\displaystyle|p(t)-p_{0}^{(\infty)}(t)|_{I^{(\infty)}}}&{=}&{\displaystyle\sum_{x\in I^{(\infty)}}|p(t,x)|^{2}.}\\ \end{array} $$ 

By assumption, the distribution  $ p(t) $ possesses bounded zero, first and second statistical moments  $ \mu_0 $,  $ \mu_1 $ and  $ \mu_2 $, respectively. Consequently, the above approximation error will get arbitrarily small, if  $ x_{max} = L^{(M+1)} - 1 $ is chosen large enough. It has been shown in [35] that

 $$ x_{max}=\frac{\mu_{1}}{\mu_{0}}+\kappa\cdot\sqrt{\frac{\mu_{2}}{\mu_{0}}-\left(\frac{\mu_{1}}{\mu_{0}}\right)^{2}} $$ 

is a reasonable choice, where  $ \kappa $ is a safety factor with a typical value of  $ \kappa = 10 $. The expression (2.24) can be derived by applying the Chebyshev inequality of statistics to the probability, that  $ p(t, x) > \varepsilon $ with  $ \varepsilon > 0 $, and  $ x > x_{\max} $. Hence, effectively we have restricted the semi-infinite approximation problem to a finite approximation problem on  $ [0, x_{\max}] $. It is important to remark that  $ x_{\max} $ depends on the time evolution of the system and is not known a priori. For the discussion of a single time step in the context of the ROM, however, the value can be considered as known and fixed. The adaptation of  $ x_{\max} $ from time step to time step will be discussed in the next section.

It remains to characterize the Galerkin approximations on the finite intervals  $ I^{(m)} $ for  $ m = 1, \ldots, M $. Consider the orthogonal basis  $ \{T_k^{(m)} : k = 0, \ldots, (U^{(m)} - L^{(m)})\} $ of discrete Chebyshev polynomials satisfying

 $$ \left\langle T_{k}^{(m)},T_{j}^{(m)}\right\rangle_{I^{(m)}}=\sum_{x\in I^{(m)}}T_{k}^{(m)}(x)T_{j}^{(m)}(x)=\gamma_{j}^{(m)}\delta_{k,j}. $$ 

Then, we can represent  $ p(t) $ on  $ I^{(m)} $ in terms of the Chebyshev polynomials

 $$ p(t,x)=\sum_{k=0}^{U^{(m)}-L^{(m)}}a_{k}^{(m)}T_{k}^{(m)}(x). $$ 

For simplicity, we ignore the time-dependence of the coefficients and the polynomials and write  $ a_k^{(m)} $ and  $ T_k^{(m)}(x) $ instead of  $ a_k^{(m)}(t) $ and  $ T_k^{(m)}(t,x) $. Again the Galerkin approximation  $ p_r^{(m)}(t) $ to  $ p(t) $ on  $ I^{(m)} $ is defined by some suitable truncation of the above expansion

 $$ p_{r}^{(m)}(t,x)=\sum_{k=0}^{r}a_{k}^{(m)}T_{k}^{(m)}(x) $$ 

with polynomial order  $ r \leq U^{(m)} - L^{(m)} $, which in general will depend on  $ I_m $. The resulting error may be estimated by

 $$ \begin{array}{r l r}{\mathrm{e p s}_{r}^{(m)}}&{=}&{\|p_{r+1}^{(m)}(t)-p_{r}^{(m)}(t)\|_{I^{(m)}}=\left|a_{r+1}^{(m)}\right|\sqrt{\gamma_{r+1}^{(m)}}.}\end{array} $$ 

In brief, we summarize the resulting decomposition and polynomial approximations by the element-order pattern

 $$ \Delta_{1}=\left\{(I_{1},r_{1}),(I_{2},r_{2}),\ldots,(I_{M},r_{M})\right\}. $$ 

We expect that for an efficient approximation  $ r_m \ll U^{(m)} - L^{(m)} $ on most of the elements. The whole approach using local refinement and higher order approximations is called Galerkin h-p-method. For rather smoothly looking distributions, we can expect that only a few intervals with moderate polynomial orders are sufficient. However, for distributions with steep flanks or for multi-modal distributions, the approach allows an automated local adaptation to avoid bad and inefficient approximation. By that one can get a nearly exponential convergence rate. This, in particular, is the reason for abandoning the global approach based on a weighted Galerkin ansatz space.

### 2.2 A Tensor Product Approach to Multiple Dimensions

Domains in $d$ dimensions. After these preparations we can extend the approach to higher dimensions. Analogous to the $1d$ case, we restrict the semi-infinite domain $\mathbf{N}^{d}$ to a finite domain

 $$ D=[0,x_{max,1}]\otimes\cdots\otimes[0,x_{max,d}], $$ 

where  $ x_{max,i} $ denotes the upper bound along the ith dimension. Next we decompose  $ D $ into disjoint rectangles  $ \{D^{(m)} : m = 1, \ldots M\} $ such that

 $$ D=\bigcup_{m=1}^{M}D^{(m)}\qquad\mathrm{w i t h}\quad D^{(m)}=[L^{(m,1)},U^{(m,1)}]\otimes\cdots\otimes[L^{(m,d)},U^{(m,d)}]. $$ 

This tensor ansatz allows us to directly make use of the one-dimensional h-p-method. Given the multi-index  $ k = (k_1, \ldots, k_d) $, we define

 $$ \begin{array}{r l r}{T_{k}^{(m)}(x)}&{=}&{T_{k_{1}}^{(m,1)}(x_{1})\cdots T_{k_{d}}^{(m,d)}(x_{d})}\end{array} $$ 

as the product of the discrete Chebyshev polynomials  $ T_{k_i}^{(m,i)} $ on the intervals  $ [L^{(m,i)}, U^{(m,i)}] $ in the ith dimension. Again we have to take care that the boundaries of the rectangles appear only once (see Figure 1 for illustration). A Galerkin approximation on a rectangle  $ D^{(m)} $ is then given by

 $$ p_{r}^{(m)}(t,x)=\sum_{k=1}^{r^{(m)}}a_{k}^{(m)}T_{k}^{(m)}(x) $$ 

with multi-index  $ r^{(m)} = (r_1^{(m)}, \ldots, r_d^{(m)}) \in N^d $. This is a highly non-uniform and flexible structure, since for each axis on each element an independent polynomial system is used. The resulting element-order pattern is given by

 $$ \Delta_{d}=\{(D^{(1)},r^{(1)}),\dots,(D^{(M)},r^{(M)})\}. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_368_476_859_1024.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Figure 1: Example of a h-p-grid. The numbers indicate the maximal order of the polynomial basis.</div>


It should be noted that the evaluation of the approximation for a given  $ x \in D $ can be efficiently performed by expressing  $ p_r^{(m)}(t) $ as the result of a sequence of 1d-Galerkin approximations (which in turn can be computed by fast summation based on the three-term recurrence of the polynomials [9]). For example in 2d we can write for a given  $ x = (x_1, x_2) $:

 $$ \begin{array}{rcl}c(x_{2};k_{1})&=&\displaystyle\sum_{k_{2}=0}^{r_{2}^{(m)}}a_{(k_{1},k_{2})}^{(m)}\cdot T_{k_{2}}^{(m,2)}(x_{2})\\p_{r}^{(m)}(t,x)&=&\displaystyle\sum_{k_{1}=0}^{r_{1}^{(m)}}c(x_{2};k_{1})\cdot T_{k_{1}}^{(m,1)}(x_{1})\end{array} $$ 

requiring the evaluation of  $ r_{1} + 1 $ sums only. Similar reformulations can be used for the computation of higher moments, projections, norms and operators in n dimensions.

Refinement strategy. Our aim is to find local approximations  $ p_{r}^{(m)}(t) $ on each domain  $ D^{(m)} $ such that the overall approximation

 $$ p_{r}(t,x)=\sum_{m=1}^{M}p_{r}^{(m)}(t,x)\cdot1_{D^{(m)}}(x) $$ 

satisfies

 $$ \mathrm{eps}_{D}=\|p_{r}-p\|_{D}=\left(\sum_{m=1}^{M}\left\|p(t)-p_{r}^{(m)}(t)\right\|_{D^{(m)}}^{2}\right)^{1/2}\leq\mathrm{TOL}_{X}. $$ 

Since the general structure of the tensor product approach has now become apparent, we restrict the following considerations to two dimensions for sake of clarity.

An element-order pattern  $ \Delta_2 $ as shown in Figure 1 has to be generated by a multi-level algorithm using certain refinement strategies. Based on an initial pattern it has to be decided step-by-step how to change elements or polynomial orders. To do so, directional error estimates are necessary, which can be used to predict the approximation errors after increase of the polynomial order or refinement of (some of) the intervals. Recalling that  $ r^{(m)} = r = (r_1, r_2) $ and setting  $ e_1 = (1, 0) $ and  $ e_2 = (0, 1) $, we define the

error estimates to predict the effect of increasing polynomial order by

 $$ \begin{array}{r c l}{\mathrm{e p s}_{1}^{(m)}}&{=}&{\left\|p_{r+e_{1}}^{(m)}(t)-p_{r}^{(m)}(t)\right\|_{D^{(m)}}=\left(\gamma_{r_{1}+1}^{(m,1)}\displaystyle\sum_{k=0}^{r_{2}}\gamma_{k}^{(m,2)}\left(a_{r_{1}+1,k}^{(m)}\right)^{2}\right)^{1/2}}\end{array} $$ 

and analogously

 $$ \begin{array}{r c l}{\mathrm{e p s}_{2}^{(m)}}&{=}&{\left\|p_{r+e_{2}}^{(m)}(t)-p_{r}^{(m)}(t)\right\|_{D^{(m)}}=\left(\gamma_{r_{2}+1}^{(m,2)}\displaystyle\sum_{k=0}^{r_{1}}\gamma_{k}^{(m,1)}\left(a_{k,r_{2}+1}^{(m)}\right)^{2}\right)^{1/2}}\end{array} $$ 

Having in mind that the elements  $ D^{(m)} $ are just tensor products of 1d intervals  $ I^{(m,1)} $ and  $ I^{(m,2)} $ the techniques described in [35] can directly be applied to the single coordinate axes. In view of an efficient algorithmic realization, the domain-order-pattern is chosen and changed such that the amount of work necessary to compute the final approximation is as small as possible. Therefore only rectangles are changed with a local error larger than some threshold. The threshold is computed based on all error predictions such that the errors within the decomposition are equilibrated. However, one cannot set up a local tolerance for single domains a priori, since the number of domains on the final level is not known beforehand. Additionally all refinement steps are chosen in view of the obtained (and necessary) gain of accuracy per work.

From time step to time step of the ROM, the grid has to be coarsened in some sense, since otherwise moving peaks or changing shapes would lead to a monotone increase of expansion coefficients. For the coarsening the error estimates and the now available average error per element are used: All domains having a local error lower than a certain percentage of the average error will be changed by reducing the polynomial order by one. If a minimal polynomial order is reached, such elements  $ D^{(m)} $ will be merged with neighbors  $ D^{(n)} $ with  $ L^{(m,i)} = L^{(n,i)} \wedge U^{(m,i)} = U^{(n,i)} $ for at least one dimension i. This strategy is grid-conservative and flexible at the same time. Additionally, the number of levels required to fulfill the stationary tolerance of the next time step is kept small.

Adaptation of overall discretization domain. In the one-dimensional case an update of  $ x_{\text{max}} $ can easily be realized by adding or deleting intervals at the right boundary. This is more complicated for the higher-dimensional case, since here all directions are affected simultaneously. Therefore all coordinate directions are stretched or compressed by the factor  $ f_i = (y_{\text{max},i} +  $

1)/(x_{max,i} + 1), where y_{max,i} denotes the new estimate. At the same time care has to be taken that all resulting  $ L^{(m,i)} $ and  $ U^{(m,i)} $ are still defined as natural numbers. Finally, when compressing the whole grid  $ \Delta_d $, it has to be ensured that no degenerated domains  $ D^{(m)} $ arise.

Given some initial element-order pattern  $ \Delta_{d} $ (e.g., from the previous time step), the algorithm comprises the following steps:

1. Coarse the grid by decrease of orders or merging of elements.

2. Compute new  $ x_{max,i} $ and stretch or compress the domain.

3. Project the current Galerkin approximation onto the new grid.

4. Set up the Galerkin equations (see below) and solve for coefficients on all elements  $ D^{(m)} $.

5. Compute error estimates for the whole domain, all elements and directions.

6. If global error below tolerance, complete Rothe time step and go back to 1, otherwise:

7. Examine the single element axes in view of order or refinement actions based on error estimates and predictions.

8. Select elements for refinement based on work-oriented error control.

9. Create new grid and go back to 3.

Efficient evaluation of Galerkin matrix entries. In order to illustrate how the setup of the Galerkin equations works in 2d, we consider the special operator

 $$ (\mathcal{A}p)(x,y)=\alpha(x-1,y+1)p(t,x-1,y+1) $$ 

as it appears as a typical term in the CME (see Sec. 3) with propensity $a$ and distribution $p(t)$. For ease of reading, we choose $(x,y)$ instead of $(x_{1},x_{2})$. The arrows in Figure 2 show the flow of information for a single domain $D^{(m)}.$

For the treatment within the Galerkin method, the operator A has to be applied to all basis functions  $ T_{k}^{(n)} = T_{k}^{(n,1)} T_{l}^{(n,2)} $ of all ansatz elements

<div style="text-align: center;"><img src="imgs/img_in_image_box_428_253_789_537.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">Figure 2: Sketch of the flow of information for one single domain.</div>


$$D^{(n)} = I^{(n,1)} \otimes I^{(n,2)},\ \text{and to be tested with all such pairs from test elements } D^{(m)} = I^{(m,1)} \otimes I^{(m,2)}.\ \text{Thus we have to compute double sums } S = S(i,j,k,l;n,m)\ \text{of the form}$$

 $$ S=\sum_{x\in I^{(n,1)}}\sum_{y\in I^{(n,2)}}T_{i}^{(m,1)}(x)T_{j}^{(m,2)}(y)\alpha(x-1,y+1)T_{k}^{(n,1)}(x-1)T_{l}^{(n,2)}(y+1) $$ 

for all $i,j,k,l$ and $1 \leq m,n \leq M$. Here, the complexity is reduced by the fact that only neighboring elements can lead to non-zero $S$. The intersection of the edges of neighboring elements will be denoted by

 $$ \begin{array}{r c l}{I_{S}^{1}}&{=}&{[\operatorname*{m a x}(L^{(m,1)},L^{(n,1)}-1),\operatorname*{m i n}(U^{(m,1)},U^{(n,1)}-1)]}\\ {I_{S}^{2}}&{=}&{[\operatorname*{m a x}(L^{(m,2)},L^{(n,2)}+1),\operatorname*{m i n}(U^{(m,2)},U^{(n,2)}+1)].}\\ \end{array} $$ 

Note that the  $ I_{S}^{i} $ may consist of a single point, which will contribute to the summation. Depending on the structure of the propensity function  $ \alpha = \alpha(x, y) $ two different scenarios are discussed below.

For the first scenario we assume that the propensity factorizes according to  $ \alpha(x,y)=\alpha_{1}(x)a_{2}(y) $. Then we obtain

 $$ \begin{array}{r c l}{S}&{=}&{\displaystyle\sum_{x\in I_{S}^{1}}\alpha_{1}(x)T_{i}^{(m,1)}(x)T_{k}^{(n,1)}(x-1)\cdot}\\ {}&{}&{\displaystyle\sum_{y\in I_{S}^{2}}\alpha_{2}(y)T_{j}^{(m,2)}(y)T_{l}^{(n,2)}(y+1)}\\ \end{array} $$ 

which is just the product of two 1d Galerkin sums for shift operators. Using Gauss-Christoffel summation we get the approximation

 $$ \begin{array}{r c l}{\tilde{S}_{2}}&{=}&{\displaystyle\sum_{\beta=1}^{n_{2}}v_{\beta}\;\alpha_{2}(y_{\beta})T_{j}^{(m,2)}(x_{\beta})T_{l}^{(n,2)}(y_{\beta}+1)}\\ {\tilde{S}}&{=}&{\displaystyle\sum_{\gamma=1}^{n_{1}}w_{\gamma}\;\alpha_{1}(x_{\gamma})T_{i}^{(m,1)}(x_{\gamma})T_{k}^{(n,1)}(x_{\gamma}-1)\cdot\tilde{S}_{2}}\\ \end{array} $$ 

Here  $ \{w_\gamma, x_\gamma\} $ and  $ \{v_\beta, y_\beta\} $ denote the  $ n_1, n_2 $ weights and nodes of the Gauss-Christoffel summation on  $ I_S^1 $ and  $ I_S^2 $, respectively. This approximation is exact, if the  $ a_i $ are polynomials and the number of nodes is chosen accordingly. The structure of  $ \tilde{S} $ shows that starting from a non-uniform, n-dimensional grid the final treatment of operators can be reduced to a one-dimensional evaluation on single discrete intervals.

However, the situation is more complicated for the second scenario, where we assume that the propensity  $ \alpha = \alpha(x, y) $ cannot be factorized. Then the evaluation has to be performed in two steps. First, for all Gauss-Christoffel nodes of the first direction, the second sum has to be computed for all j and l:

 $$ \tilde{S}_{2}(x_{\gamma})=\sum_{\beta=1}^{n_{2}}v_{\beta}\alpha(x_{\gamma},y_{\beta})T_{j}^{(m,2)}(y_{\beta})T_{l}^{(n,2)}(y_{\beta}+1). $$ 

Then the first sum can be expressed in terms of the intermediate approximations  $ \tilde{S}_{2} $:

 $$ \tilde{S}=\sum_{\gamma=1}^{n_{1}}w_{\gamma}\alpha(x_{\gamma},y_{\beta})T_{i}^{(m,1)}(x_{\gamma})T_{k}^{(n,1)}(x_{\gamma}-1)\tilde{S}_{2}(x_{\gamma}) $$ 

This strategy might look as a minor aspect of the practical realization, but it is crucial for the whole tensor product approach (compare (2.25)). Based on this strategy, all terms of the equations presented in Sec. 3 can be treated in a structural way.

## 3 Numerical Examples

In this section, we illustrate the above described adaptive discrete Galerkin approach at two examples. The first one, a genetic toggle switch, has been selected for comparison purposes, since it has already been used as a test

problem in [31] and [13]. The second one is an artificial test problem constructed to generate special difficulties for any kind of tensor product approaches, since there the dynamics asymptotically collapses to the diagonal between two sources.

### 3.1 Bistable Toggle Switch

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Plot</th><th style='text-align: center;'>X-Axis Label</th><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>Y-Axis Label</th><th style='text-align: center;'>Y-Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.02</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.08</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.10</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.12</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.18</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.22</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.28</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.30</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.32</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.35</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.38</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.42</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.48</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.50</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.52</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.55</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.58</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.60</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.62</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.65</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.68</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.70</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.72</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.75</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.78</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.82</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.85</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.88</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.92</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>1.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.02</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.05</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.08</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.10</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.12</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.15</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.18</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.20</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.22</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.25</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.28</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.32</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.35</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.38</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.40</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.42</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.45</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.48</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.50</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.52</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.55</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.58</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.60</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.62</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.65</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.68</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.70</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.75</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.78</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.80</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.82</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.85</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.88</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.92</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>2.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.02</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.05</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.08</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.10</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.12</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.15</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.18</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.20</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.22</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.25</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.28</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.30</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.32</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.35</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.38</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.40</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.42</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.45</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.48</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.50</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.52</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.55</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.58</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.60</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.62</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.65</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.68</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.70</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.72</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.75</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.78</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.82</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.85</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.88</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.92</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.02</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.05</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.08</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.10</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.12</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.15</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.18</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.20</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.22</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.25</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.28</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.30</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.32</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.35</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.38</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.40</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.42</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.45</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.48</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.50</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.52</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.55</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.58</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.60</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.62</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.65</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.68</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.70</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.72</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.75</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.78</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.80</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.82</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.85</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.88</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.92</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>4.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.02</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.05</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.08</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.10</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.12</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.15</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.18</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.20</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.22</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.25</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.28</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.30</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.32</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.35</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.38</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.40</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.42</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.45</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.48</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.50</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.52</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.55</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.58</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.60</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.62</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.65</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.68</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.70</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.72</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.75</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.78</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.80</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.82</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.85</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.88</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.90</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.92</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.95</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>5.98</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3.80</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>6.00</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>3</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3: Stationary distribution of the genetic toggle switch (3.26), (3.28) obtained from a dynamic simulation on the time-interval  $ [0, 6 \cdot 10^{4}] $. The boxes and numbers indicate the h-p-grid and the maximal order of the polynomial basis.</div>


As a first application, we consider a model for the simulation of a genetic toggle switch in E. coli; cf. [15]. The model consists of two competing repressors, A and B, transcribed by two constitutive promoters. Each of the two repressors can inhibit the production of the competing repressor by binding to the corresponding genetic control sequences of the promoter.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>0.00e+00</th><th style='text-align: center;'>0.00e+00</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 4: Three-dimensional plot of the stationary distribution (cf. Figure 3).</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time t</th><th style='text-align: center;'>TOL=0.01</th><th style='text-align: center;'>TOL=0.03</th><th style='text-align: center;'>TOL=0.1</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1750</td><td style='text-align: center;'>1750</td><td style='text-align: center;'>1750</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2950</td><td style='text-align: center;'>1900</td><td style='text-align: center;'>1250</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>2650</td><td style='text-align: center;'>1650</td><td style='text-align: center;'>1100</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>2500</td><td style='text-align: center;'>1600</td><td style='text-align: center;'>1100</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>2350</td><td style='text-align: center;'>1550</td><td style='text-align: center;'>1100</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>1450</td><td style='text-align: center;'>1100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5: Total number of degrees of freedom as a function of time for the tolerances 0.1, 0.03, 0.01.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_241_249_971_1186.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 6: “Movie” of the PDF of the genetic toggle switch (3.26), (3.28). The panels show the solution at different times. In the lower right panel the solution at  $ t = 16000 $ is depicted in logarithmic greyscale.</div>


The system includes the following reactions:

 $$ \left.\begin{array}{r c c c c c}{R_{1}:}&{\star}&{\longrightarrow}&{A,}&{\alpha_{1}(x)}&{=}&{c_{1}/(c_{2}+x_{2}^{\beta})}\\ {R_{2}:}&{A}&{\longrightarrow}&{\star,}&{\alpha_{2}(x)}&{=}&{c_{3}x_{1}}\\ {R_{3}:}&{\star}&{\longrightarrow}&{B,}&{\alpha_{3}(x)}&{=}&{c_{4}/(c_{5}+x_{1}^{\gamma})}\\ {R_{4}:}&{B}&{\longrightarrow}&{\star,}&{\alpha_{4}(x)}&{=}&{c_{6}x_{2}}\\ \end{array}\right\} $$ 

The positive constants  $ c_1 $,  $ c_2 $ and  $ c_3 $,  $ c_4 $ determine the maximal rate of synthesis of the repressors A and B, respectively. The degradation rates of the repressors are denoted by  $ c_5 $ and  $ c_6 $, while coefficients  $ \beta > 1 $ and  $ \gamma > 1 $ specify the cooperativity of the two promoters. With subscripts i and j indicating the molecule numbers of the two species, these reactions may be written as follows:

 $$ \begin{aligned}&R_{1}:\quad(A_{i},B_{j})\quad\xrightarrow{\frac{c_{1}}{c_{2}+x_{2}^{\beta}}}\quad(A_{i+1},B_{j})\\&R_{2}:\quad(A_{i},B_{j})\quad\xrightarrow{c_{3}x_{1}}\quad(A_{i-1},B_{j})\\&R_{3}:\quad(A_{i},B_{j})\quad\xrightarrow{\frac{c_{4}}{c_{5}+x_{1}^{\gamma}}}\quad(A_{i},B_{j+1})\\&R_{4}:\quad(A_{i},B_{j})\quad\xrightarrow{c_{6}x_{2}}\quad(A_{i},B_{j-1})\\ \end{aligned} $$ 

The reaction  $ R_1 $ is constructed in such a way that the corresponding propensity  $ \alpha_1(x) $ is small whenever  $ x_2 $ is large. Hence, the transcription of  $ A $ is inhibited if many copies of  $ B $ are present. Conversely, a large copy number of  $ A $ inhibits the production of new  $ B $ since  $ x_1 \gg 1 $ implies  $ \alpha_3(x) \ll 1 $. These two scenarios (large number of  $ A $ and small number of  $ B $, or large number of  $ B $ and small number of  $ A $) correspond to the two stable steady states of the traditional reaction rate equations

 $$ \begin{array}{rcl}\dot{y}_{1}&=&\frac{c_{1}}{c_{2}+y_{2}^{\beta}}-c_{3}y_{1}\\\dot{y}_{2}&=&\frac{c_{4}}{c_{5}+y_{1}^{\gamma}}-c_{6}y_{2}\end{array} $$ 

(cf. [15]). The solution of (3.27), however, does not provide an appropriate description since a single trajectory can only converge to one of the steady states, whereas in the real biological system flipping between stable states due to chemical or thermal induction is possible (cf. [15]). This switching behavior can only be reproduced by a stochastic description including fluctuations which can induce transitions from one steady state to the other one.

Due to the bistability of the toggle switch, the solution of the corresponding CME is a bimodal PDF. Bimodality is of prime importance in many biological applications since it indicates the presence of two different scenarios or macro-states, and it is crucial that a numerical method constructed for solving the CME captures the bimodality correctly.

In [31], the parametrisation

 $$ \begin{array}{r c l c r c l c r c l}{c_{1}}&{=}&{c_{4}}&{=}&{3\cdot10^{3}s^{-1},}&{}&{c_{2}}&{=}&{c_{5}}&{=}&{1.1\cdot10^{4},}\\ {c_{3}}&{=}&{c_{6}}&{=}&{0.001s^{-1},}&{}&{\beta}&{=}&{\gamma}&{=}&{2}\\ \end{array} $$ 

has been used, and both the stationary distribution and the time-dependent solution in the interval  $ [0, 10^{4}] $ have been computed on the domain  $ [0, 399] \times [0, 399] $. Instead of solving the full discrete CME, however, the authors presented an approximation of the Fokker-Planck equation, a PDE known to be, in some sense, the continuous counterpart of the CME (see, e.g., [14]). In the case of the genetic toggle switch, this may yield a reasonable approximation, but in situations where the discrete nature of the reaction system is crucial (cf. [24, 32]), replacing the CME by the Fokker-Planck equation causes a large modelling error in addition to the numerical approximation error. Hence, the approach proposed in [31] can actually not be considered as a viable method for the CME, but rather as a method for the Fokker-Planck equation.

The genetic toggle switch has been investigated again in [13]. There, a computation based on the full CME has been presented, but the computational domain had to be decreased to approximately  $ [0, 200] \times [0, 200] $ by a rescaling of the parameters. Note that, by construction, our adaptive discrete Galerkin method does not require any such downscaling.

The following simulations have been performed with a special 2d-version of the program package PREDICI $ ^{\circledR} $. In our first example, the full CME of (3.26) with parameters (3.28) was solved up to a predefined tolerance of 0.03. As an initial distribution, the product Gaussian

 $$ \frac{1}{2\pi\sigma_{1}\sigma_{2}}\exp\left(-\frac{(x_{1}-\mu_{1})^{2}}{2\sigma_{1}^{2}}\right)\exp\left(-\frac{(x_{2}-\mu_{2})^{2}}{2\sigma_{2}^{2}}\right) $$ 

has been evaluated and normalized on the discrete state space for  $ \mu_1 = \mu_2 = 133 $ and  $ \sigma_1 = \sigma_2 = \sqrt{133} $. Figure 3 shows the PDF at  $ t = 6 \cdot 10^4 $. By this time, the PDF has almost converged to the stationary distribution, and a comparison of Figure 3 with the right panel of Figure 3 in [31] shows indeed a very good agreement. The bimodality is clearly visible and indicates the relevant biological information, namely the bistability of the toggle switch.

Along with the contour lines, the h-p-grid is depicted; the numbers indicate the maximal order of the polynomial basis. As desired, the discrete Galerkin method refines either the subdivision of space or the polynomial order or both in regions where the solution changes significantly, and the grid shows a nearly perfect symmetry. The number of degrees of freedom of this h-p-grid is about 1600. A three-dimensional mesh plot of the solution is given in Figure 4. It reveals that the two modes are linked by a “tunnel” or transition path which allows for switching between the two states.

Figure 5 shows the time-evolution of the degrees of freedom for the tolerances 0.1, 0.03, 0.01. It can be nicely seen how the adaptive strategies refine the approximation according to the requirements of the changing distribution. It can also be recognized that the number of variables increases more or less linearly with the required tolerance - a sign for nearly exponential convergence rate of the discrete h-p-method. It should be pointed out that even when the desired accuracy is rather high, only about 3000 degrees of freedom have to be handled, whereas a naïve computation of the PDF would require the solution of  $ 350^2 = 122500 $ ODEs. This corresponds to a reduction of more than 97.5%.

Next, in order to study an asymmetric and more challenging situation, we chose  $ \mu_1 = 100 $,  $ \mu_2 $,  $ \sigma_1 = 10 $, and  $ \sigma_2 = 3 $ in (3.29). The initial domain has been chosen to  $ [0, 150] \times [0, 20] $. In the course of the integration this range is extended adaptively. The panels of Figure 6 show the time evolution of the PDF. First, the main part of the probability mass is attracted by the lower steady state since it is closer to the center of the initial PDF than the upper one. At  $ t = 16000 $ the distribution is stretched a bit, and the additional grid refinements around (50, 200) seem to be dispensable. However, the coloured contour plot (here plotted in logarithmic greyscale) indicates that some of the probability mass already leaks to the other stationary state. As time evolves, more and more probability mass fluctuates very slowly from the lower to the upper steady state until finally an equilibrium between both states is reached in the stationary distribution. This simulation has been performed with tolerance 0.01 and a maximum of 2700 variables at intermediate states. The h-p-grid is nearly symmetric at the final stage. This example shows how the h-p-algorithm and the ROM automatically capture the dynamics and the structure of distributions. More pictures would lead too far off here, but, e.g., by setting  $ \mu = 10^{-4} $ or even  $ \mu = 10^{-5} $, intermediate distributions with maximal particle numbers up to several thousands occurred and could equally well be represented.

### 3.2 A Challenging Test Problem

As a second example, we chose a comparatively simple model problem which, however, represents a real challenge for any numerical method based on a tensor product ansatz. The corresponding reaction system (with species A, B, C) reads

 $$ \left.\begin{array}{l l l l}{{{R_{1}:}}}&{{{A}}}&{{{\xrightarrow{c_{1}}}}}&{{{B,}}} \\{{{R_{2}:}}}&{{{B}}}&{{{\xrightarrow{c_{2}}}}}&{{{A,}}} \\{{{R_{3}:}}}&{{{C}}}&{{{\xrightarrow{c_{3}}}}}&{{{A,}}} \\{{{R_{4}:}}}&{{{A+B}}}&{{{\xrightarrow{c_{4}}}}}&{{{B+B,}}} \\{{{R_{5}:}}}&{{{A+B}}}&{{{\xrightarrow{c_{5}}}}}&{{{A+A}}}\end{array}\right\} $$ 

or, in different notation,

 $$ \begin{aligned}&R_{1}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{1}}\quad(A_{i-1},B_{j+1},C_{k})\\&R_{2}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{2}}\quad(A_{i+1},B_{j-1},C_{k})\\&R_{3}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{(N-i-j)\cdot c_{3}}\quad(A_{i+1},B_{j},C_{k-1})\\&R_{4}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{4}}\quad(A_{i-1},B_{j+1},C_{k})\\&R_{5}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{5}}\quad(A_{i+1},B_{j-1},C_{k})\\ \end{aligned} $$ 

where again the indices refer to the molecule numbers. Since there are three species involved, the state space is actually three dimensional, but since the total number N of molecules remains invariant in all reactions, the molecule numbers of one of the species, say C, can be expressed in terms of the other ones:

 $$ x_{3}=N-x_{1}-x_{2}. $$ 

This actually reduces the three-dimensional problem to a two-dimensional one. The corresponding CME reads

 $$ \begin{aligned}\frac{\partial}{\partial t}P(t,x_{1},x_{2})\quad&=\quad c_{1}(x_{1}+1)P(t,x_{1}+1,x_{2}-1)-c_{1}x_{1}P(t,x_{1},x_{2})\quad(3.31)\\&+c_{2}(x_{2}+1)P(t,x_{1}-1,x_{2}+1)-c_{2}x_{2}P(t,x_{1},x_{2})\\&+c_{3}(N-x_{1}-x_{2}+1)P(t,x_{1}-1,x_{2})-c_{3}(N-x_{1}-x_{2})P(t,x_{1},x_{2})\\&+c_{4}(x_{1}+1)(x_{2}-1)P(t,x_{1}+1,x_{2}-1)-c_{4}x_{1}x_{2}P(t,x_{1},x_{2})\\&+c_{5}(x_{1}-1)(x_{2}+1)P(t,x_{1}-1,x_{2}+1)-c_{5}x_{1}x_{2}P(t,x_{1},x_{2}).\end{aligned} $$ 

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Plot</th><th style='text-align: center;'>X-Axis</th><th style='text-align: center;'>Y-Axis</th><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>Y-Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>1.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.88</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.82</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.68</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.62</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.52</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.48</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.10</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>0.32</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.30</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.35</td><td style='text-align: center;'>0.22</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.50</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.55</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.60</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.65</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.70</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.75</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.85</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.90</td><td style='text-align: center;'>-0.02</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>1.95</td><td style='text-align: center;'>-0.04</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>-0.06</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.05</td><td style='text-align: center;'>-0.08</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.10</td><td style='text-align: center;'>-0.10</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.15</td><td style='text-align: center;'>-0.12</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.20</td><td style='text-align: center;'>-0.14</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.25</td><td style='text-align: center;'>-0.16</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>-0.18</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.35</td><td style='text-align: center;'>-0.20</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.40</td><td style='text-align: center;'>-0.22</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.45</td><td style='text-align: center;'>-0.24</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.50</td><td style='text-align: center;'>-0.26</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.55</td><td style='text-align: center;'>-0.28</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.60</td><td style='text-align: center;'>-0.30</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.65</td><td style='text-align: center;'>-0.32</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.70</td><td style='text-align: center;'>-0.34</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.75</td><td style='text-align: center;'>-0.36</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.80</td><td style='text-align: center;'>-0.38</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.85</td><td style='text-align: center;'>-0.40</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>-0.42</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>2.95</td><td style='text-align: center;'>-0.44</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>-0.46</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.05</td><td style='text-align: center;'>-0.48</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.10</td><td style='text-align: center;'>-0.50</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.15</td><td style='text-align: center;'>-0.52</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.20</td><td style='text-align: center;'>-0.54</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.25</td><td style='text-align: center;'>-0.56</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.30</td><td style='text-align: center;'>-0.58</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.35</td><td style='text-align: center;'>-0.60</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.40</td><td style='text-align: center;'>-0.62</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.45</td><td style='text-align: center;'>-0.64</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.50</td><td style='text-align: center;'>-0.66</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.55</td><td style='text-align: center;'>-0.68</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.60</td><td style='text-align: center;'>-0.70</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.65</td><td style='text-align: center;'>-0.72</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.70</td><td style='text-align: center;'>-0.74</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.75</td><td style='text-align: center;'>-0.76</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.80</td><td style='text-align: center;'>-0.78</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.85</td><td style='text-align: center;'>-0.80</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.90</td><td style='text-align: center;'>-0.82</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>3.95</td><td style='text-align: center;'>-0.84</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.00</td><td style='text-align: center;'>-0.86</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.05</td><td style='text-align: center;'>-0.88</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.10</td><td style='text-align: center;'>-0.90</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.15</td><td style='text-align: center;'>-0.92</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.20</td><td style='text-align: center;'>-0.94</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.25</td><td style='text-align: center;'>-0.96</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.30</td><td style='text-align: center;'>-0.98</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.35</td><td style='text-align: center;'>-1.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.40</td><td style='text-align: center;'>-1.02</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.45</td><td style='text-align: center;'>-1.04</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.50</td><td style='text-align: center;'>-1.06</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.55</td><td style='text-align: center;'>-1.08</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.60</td><td style='text-align: center;'>-1.10</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.65</td><td style='text-align: center;'>-1.12</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.70</td><td style='text-align: center;'>-1.14</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.75</td><td style='text-align: center;'>-1.16</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.80</td><td style='text-align: center;'>-1.18</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.85</td><td style='text-align: center;'>-1.20</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.90</td><td style='text-align: center;'>-1.22</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>4.95</td><td style='text-align: center;'>-1.24</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.00</td><td style='text-align: center;'>-1.26</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.05</td><td style='text-align: center;'>-1.28</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.10</td><td style='text-align: center;'>-1.30</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.15</td><td style='text-align: center;'>-1.32</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.20</td><td style='text-align: center;'>-1.34</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.25</td><td style='text-align: center;'>-1.36</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.30</td><td style='text-align: center;'>-1.38</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.35</td><td style='text-align: center;'>-1.40</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.40</td><td style='text-align: center;'>-1.42</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.45</td><td style='text-align: center;'>-1.44</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.50</td><td style='text-align: center;'>-1.46</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.55</td><td style='text-align: center;'>-1.48</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.60</td><td style='text-align: center;'>-1.50</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.65</td><td style='text-align: center;'>-1.52</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.70</td><td style='text-align: center;'>-1.54</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.75</td><td style='text-align: center;'>-1.56</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.80</td><td style='text-align: center;'>-1.58</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.85</td><td style='text-align: center;'>-1.60</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.90</td><td style='text-align: center;'>-1.62</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>5.95</td><td style='text-align: center;'>-1.64</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.00</td><td style='text-align: center;'>-1.66</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.05</td><td style='text-align: center;'>-1.68</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.10</td><td style='text-align: center;'>-1.70</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.15</td><td style='text-align: center;'>-1.72</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.20</td><td style='text-align: center;'>-1.74</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.25</td><td style='text-align: center;'>-1.76</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.30</td><td style='text-align: center;'>-1.78</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.35</td><td style='text-align: center;'>-1.80</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.40</td><td style='text-align: center;'>-1.82</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.45</td><td style='text-align: center;'>-1.84</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.50</td><td style='text-align: center;'>-1.86</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.55</td><td style='text-align: center;'>-1.88</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.60</td><td style='text-align: center;'>-1.90</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.65</td><td style='text-align: center;'>-1.92</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.70</td><td style='text-align: center;'>-1.94</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.75</td><td style='text-align: center;'>-1.96</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.80</td><td style='text-align: center;'>-1.98</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.85</td><td style='text-align: center;'>-2.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.90</td><td style='text-align: center;'>-2.02</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>6.95</td><td style='text-align: center;'>-2.04</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.00</td><td style='text-align: center;'>-2.06</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.05</td><td style='text-align: center;'>-2.08</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.10</td><td style='text-align: center;'>-2.10</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.15</td><td style='text-align: center;'>-2.12</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.20</td><td style='text-align: center;'>-2.14</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.25</td><td style='text-align: center;'>-2.16</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.30</td><td style='text-align: center;'>-2.18</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.35</td><td style='text-align: center;'>-2.20</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.40</td><td style='text-align: center;'>-2.22</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.45</td><td style='text-align: center;'>-2.24</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.50</td><td style='text-align: center;'>-2.26</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.55</td><td style='text-align: center;'>-2.28</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.60</td><td style='text-align: center;'>-2.30</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.65</td><td style='text-align: center;'>-2.32</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.70</td><td style='text-align: center;'>-2.34</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.75</td><td style='text-align: center;'>-2.36</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.80</td><td style='text-align: center;'>-2.38</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.85</td><td style='text-align: center;'>-2.40</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.90</td><td style='text-align: center;'>-2.42</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>7.95</td><td style='text-align: center;'>-2.44</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.00</td><td style='text-align: center;'>-2.46</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.05</td><td style='text-align: center;'>-2.48</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.10</td><td style='text-align: center;'>-2.50</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.15</td><td style='text-align: center;'>-2.52</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.20</td><td style='text-align: center;'>-2.54</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.25</td><td style='text-align: center;'>-2.56</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.30</td><td style='text-align: center;'>-2.58</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.35</td><td style='text-align: center;'>-2.60</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.40</td><td style='text-align: center;'>-2.62</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.45</td><td style='text-align: center;'>-2.64</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.50</td><td style='text-align: center;'>-2.66</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.55</td><td style='text-align: center;'>-2.68</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.60</td><td style='text-align: center;'>-2.70</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.65</td><td style='text-align: center;'>-2.72</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.70</td><td style='text-align: center;'>-2.74</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.75</td><td style='text-align: center;'>-2.76</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td><td style='text-align: center;'><2</td><td style='text-align: center;'>8.80</td><td style='text-align: center;'>-2.78</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(4E2)</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7: Solution of the CME (3.31), (3.32) for N = 100 and TOL = 0.02 at t = 5. At this time, almost the entire probability mass is concentrated on the line  $ x_{1} + x_{2} = N $. In the lower plot, only the h-p-grid is shown.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Category</th><th style='text-align: center;'>(mH)</th><th style='text-align: center;'>(mH) Error Bar</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>97</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>99</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>[0.040, 0.120]</td></tr>
  </tbody>
</table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_384_270_820_1142.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">Figure 8: Solution of the CME (3.31), (3.32). In contrast to Figure 7, the state space has been increased considerably by choosing N = 10000 (TOL = 0.05), but the PDF is shown at time t = 4 instead of t = 5. In the lower panel, the probability distribution is visualized in three dimensions (top view).</div>


We suppose that at t = 0 there are N molecules of C and no molecules of A or B such that the initial distribution is given by

 $$ \begin{array}{l l l}{P(0,x_{1},x_{2})}&{=}&{\left\{\begin{array}{l l}{1}&{\mathrm{i f~}x_{1}=x_{2}=0,}\\ {0}&{\mathrm{e l s e.}}\end{array}\right.}\\ \end{array} $$ 

It is easy to see that in the limit  $ t \longrightarrow 0 $ all molecules of C disappear and that the exchange between A and B reaches an equilibrium. In the special case

 $$ c_{1}=\cdots=c_{5}=1, $$ 

it can be shown that the stationary distribution is the uniform distribution on the line  $ \left\{(x_1, x_2) \in \mathbf{N}^2 : x_1 + x_2 = N\right\} $, i.e.

 $$ \bar{P}(x_{1},x_{2})=\lim_{t\to\infty}P(t,x_{1},x_{2})=\left\{\begin{array}{cc}1/(N+1)&if x_{1}+x_{2}=N,\\0&else.\end{array}\right. $$ 

This distribution is the worst case for any tensor product ansatz, because an exact representation of  $ \bar{P} $ requires  $ N+1 $ basis functions although  $ \bar{P} $ contains only  $ N+1 $ nonzero elements. Moreover, all nonzero elements have the same value such that any truncation produces the same error.

Figure 7 (upper panel) shows the result for N=100 at t=5 computed with TOL = 0.02. At that time, the distribution is nearly reduced to the line  $ x_{1} + x_{2} = N $, and obviously this leads to difficulties regarding the domain decomposition into reactangles, cf. the lower panel of Figure 7. About 2500 variables are necessary to compute the solution. In comparison to the maximum number of about 10000, this is not a convincing reduction, and for smaller N, the reduction is even less efficient. However, if we do not try to approximate the final end of the process, but stop a bit earlier, the pay-off can be drastically. Figure 8 shows the solution at t=4, but with N increased to N = 10000. To obtain a tolerance of TOL = 0.05 on the state space with  $ 10000 \times 10000 $ states, only about 2600 variables are required, which corresponds to a reduction of 0.999974%! A 3d-plot shot from the top (cf. the lower panel in Figure 8) shows how narrow even then the front already is.

## Conclusion

We present an adaptive discrete Galerkin method for use in the chemical master equation (CME). In one state space dimension, such methods have

had an impressive influence on the modelling of polyreaction kinetics. For the CME, however, the step towards multiple dimensions turns out to be crucial. The paper clearly shows that discrete Galerkin methods allow an efficient treatment of CME. In particular, examples as the one presented in the last Figure, could not be solved up to now - not even in two dimensions. However, the challenging second example makes it apparent that there is still a complexity barrier in view of more complicated cases and higher dimensions. Future research will therefore have to focus on how to overcome these difficulties. Nevertheless, the results presented here will lay a measure for any future improvements.

## References

[1] A. Alfonsi, E. Cancès, G. Turinici, B. Di Ventura, and W. Huisinga. Adaptive simulation of hybrid stochastic and deterministic models for biochemical systems. ESAIM Proceeding, 14:1–13, 2005.

[2] F. Bornemann. An adaptive multilevel approach to parabolic equations: I. general theory and 1d implementation. IMPACT Comput Sci Eng, 2:279–317, 1990.

[3] F. Bornemann. An adaptive multilevel approach to parabolic equations: II. variable-order time discretization based on a multiplicative error correction. IMPACT Comput Sci Eng, 3:93–122, 1991.

[4] F. Bornemann. An adaptive multilevel approach to parabolic equations in two space dimensions. PhD thesis, Freie Universität Berlin, 1991.

[5] K. Burrage and T. Tian. Poisson Runge-Kutta methods for chemical reaction systems. In Y. Lu W. Sun and T. Tang, editors, Advances in Scientific Computing and Applications, pages 82–96. Science Press, Beijing/New York, 2004.

[6] K. Burrage, T. Tian, and P. Burrage. A multi-scaled approach for simulating chemical reaction systems. Progress in Biophysics and Molecular Biology, 85:217–234, 2004.

[7] Computing in Technology GmbH (CiT). http://www.cit-wulkow.de.

[8] P. Deuflhard and F. Bornemann. Scientific Computing with Ordinary Differential Equations, volume 42 of Texts in Applied Mathematics. Springer, 2002.

[9] P. Deuflhard and A. Hohmann. Numerical Analysis in Modern Scientific Computing: An Introduction, volume 43 of Texts in Applied Mathematics. Springer, 2003.

[10] P. Deuflhard and M. Wulkow. Computational treatment of polyreaction kinetics by orthogonal polynomials of a discrete variable. IMPACT Comput Sci Eng, 1:269–301, 1989.

[11] P. Deuflhard and M. Wulkow. Simulationsverfahren in der Polymerchemie. In Mathematik in der Praxis, pages 117–136. Springer International, 1995.

[12] M. B. Elowitz, E. D. Siggia, P. S. Swain, and A. J. Levine. Stochastic gene expression in a single cell. Science, 297:1183–1186, 2002.

[13] S. Engblom. A discrete spectral method for the chemical master equation. Submitted, 2006.

[14] C. W. Gardiner. Handbook of Stochastic Methods. Springer, Berlin, 2nd enlarged edition edition, 1985.

[15] Timothy S. Gardner, Charles R. Cantor, and James J. Collins. Construction of a genetic toggle switch in Escherichia coli. Nature, 403:339–342, 2000.

[16] M. A. Gibson and J. Bruck. Efficient exact stochastic simulation of chemical systems with many species and many channels. J. Phys. Chem. A, 104:1876–1889, 2000.

[17] D. T. Gillespie. Exact stochastic simulation of coupled chemical reactions. J. Phys. Chem., 81:2340–2361, 1977.

[18] D. T. Gillespie. A rigorous derivation of the chemical master equation. Physica A, 188:404–425, 1992.

[19] D. T. Gillespie. Approximate accelerated stochastic simulation of chemically reacting systems. Journal of Chemical Physics, 115(4):1716–1733, 2001.

[20] D.T. Gillespie. A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. J. Comput. Phys., 22:403–434, 1976.

[21] E. L. Haseltine and J. B. Rawlings. Approximate simulation of coupled fast and slow reactions for stochastic chemical kinetics. Journal of Chemical Physics, 117(15):6959–6969, 2002.

[22] Harald Horn and Michael Wulkow. Simulation von Wachstum und Abtrag von Biomasse - Eine exemplarische Betrachtung für eine 2d-Modellierung. Chemie Ingenieur Technik, 77(4), 2005.

[23] P. D. Iedema, M. Wulkow, and H. C. J. Hoefsloot. Modelling molecular weight and degree of branching distribution of low-density polyethylene. Macromolecules, 33:7173–7184, 2000.

[24] T. Jahnke and W. Huisinga. A dynamical low-rank approach to the chemical master equation. Submitted, 2007.

[25] J. Lang. Adaptive Multilevel Solution of Nonlinear Parabolic PDE Systems, volume 16 of Lecture Notes in Computational Science and Engineering. Springer, 2001.

[26] H. H. McAdams and A. P. Arkin. Stochastic mechanisms in gene expression. PNAS, 94:814–819, 1997.

[27] H. H. McAdams and A. P. Arkin. It’s a noisy business! Genetic regulation at the nanomolar scale. Trends Genet, 15:65–69, 1999.

[28] C. V. Rao and A. P. Arkin. Stochastic chemical kinetics and the quasi-steady-state assumption: Application to the Gillespie algorithm. J. Chem. Phys., 118(11):4999–5010, 2003.

[29] J. M. Raser and E. K. O'Shea. Control of stochasticity in eukaryotic gene expression. Science, 304:1811–1814, 2004.

[30] H. Salis and Y. Kaznessis. Accurate hybrid simulation of a system of coupled chemical or biochemical reactions. J. Chem. Phys., 122, 2005.

[31] P. Sjöberg, P. Lötstedt, and J. Elf. Fokker-Planck approximation of the master equation in molecular biology. Comput. Vis. Sci., 2007.

[32] R. Srivastava, L. You, J. Summers, and J. Yin. Stochastic vs. deterministic modeling of intracellular viral kinetics. J. theor. Biol., 218:309–321, 2002.

[33] M. Wulkow. Numerical Treatment of countable systems of ordinary differential equations. Doctoral thesis, Freie Universität Berlin, 1990.

[34] M. Wulkow. Adaptive treatment of polyreactions in weighted sequence spaces. IMPACT Comput Sci Eng, 4:153–193, 1992.

[35] M. Wulkow. The simulation of molecular weight distribution in polyre-action kinetics by discrete Galerkin methods. Macromol Theory Simul, 5:393–416, 1996.

[36] M. Wulkow and P. Deufhard. Towards an efficient computational treatment of heterogeneous polymer reactions. In S. O. Fatunla, editor, Computational Ordinary Differential Equations, pages 287–306. University Press PLC, Ibadan, 1992.