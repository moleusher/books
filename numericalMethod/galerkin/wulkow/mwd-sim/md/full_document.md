Feature Article

# The simulation of molecular weight distributions in polyreaction kinetics by discrete Galerkin methods

Michael Wulkow

CiT — Computing in Technology GmbH, Pater-Kolbe-Straße 7, D-26180 Rastede, Germany

(Received: November 23, 1995)

## SUMMARY:

This article describes the development of a comprehensive solver for the differential equations arising from the modeling of molecular weight distributions in polyreactions. Based on a series of numerical developments, the software package PREDIC1 combines new directions in mathematics, chemical computing and implementation. The algorithm is based on a so-called discrete Galerkin h-p-method, which allows the efficient treatment of numerous polymerization reaction types. The abilities of the new concept are demonstrated on challenging examples.

## Introduction

With the increased production of special polymers the understanding and optimization of polyreaction processes by kinetic models has become of even greater interest. Improvement of measurement methods and the power of modern computer hardware give principally the chance for extended computer simulations in this field, for that a researcher or technician wishes to model a process according to his imagination of the reaction and not according to computational restrictions. In particular, the dynamic analysis of molecular weight distributions as an important product property can provide important insight in the kinetic scheme.

However, the kinetic steps of polyreactions describing the full molecular weight distributions of the arising polymer usually lead to such high-dimensional systems of differential equations (sometimes up to several million components) that they cannot be solved with standard solvers or even analytical methods — the fast and efficient verification of new kinetic models by computer simulation is sometimes prevented by the enormous computational effort.

Therefore model reductions and simplifying assumptions are employed in order to use special numerical algorithms. These developments may also be time-consuming and often restrict the insight into the process. Nevertheless, there are numerous methods of merit developed for such special purposes as, e.g., the method of moments $ ^{1)} $ and special iteration methods for closed problems $ ^{37)} $, lumping $ ^{2)} $, statistical or Monte-Carlo simulation $ ^{3,4,36)} $, continuous modelling $ ^{5,6)} $, discrete Fourier transforms $ ^{7)} $, discrete weighted Galerkin $ ^{8,9)} $ and discrete collocation methods $ ^{10)} $. A comprehensive and efficient approach to a real wide range of problems is not provided by one of these methods.

The rate equations describing molecular weight distributions look like high-dimensional systems of differential equations, but it turned out  $ {}^{[9,11,12]} $ that they are something like discrete partial differential equations in nature. This hidden structure might be the reason that the difficulties for calculating the numerical solution of such systems have been widely underestimated in the mathematical research for years and it is understandable that nearly all progress and attempts in solving these equations have been done in a chemical context.

In this paper, the outcome of a numerical research program – started by Deuflhard and Wulkow $ ^{8)} $ — will be presented, which has always been oriented to the chemical application. The goal has been the complete, flexible and efficient solution of polyreaction kinetics of very different kind, i.e. the intention was the treatment of models with

● arbitrary number of species and chain length distributions

● treatment of arbitrary reaction steps, e.g. chain-length dependent steps

• arbitrary number of reaction steps

● no restriction on the form of the molecular weight distributions

● no necessity of model reductions as steady-state assumptions.

In order to achieve these requirements even on personal computers, the development of various new concepts and — not to forget — an appropriate implementation in the programming language C++ was necessary. The resulting algorithm consists of different approximation techniques reducing the computational complexity as far as possible. The article will also show, how the author worked through the different approaches and — looking back things are always much easier — how the new algorithm can be motivated.

The resulting discrete h-p-method combines the demand for minimization of used internal variables with an adaptive treatment of reaction steps and automatic error control mechanisms. The method has been implemented in the software package PREDIC $ ^{\circledR} $ which is now used in industry and at universities.

Because it is not possible to collect and describe all the details of the approach here, we refer to ref. $ ^{8} $ for some basics about the preceding discrete weighted Galerkin method and its motivation and ref. $ ^{9} $ for the mathematical theory of countable systems in sequence spaces. In the first part a brief survey of these methods is presented, which made — in some way — contributions to the final algorithm. In the second part the h-p-method and its implementation is described in an informal way. The numerical section presents several examples from different fields of polymerization.

## Differential equations from polyreactions

## Problems

In order to illustrate the class of problems we are dealing with we consider the simple reaction system

The simulation of molecular weight distributions in polyreaction kinetics ...

 $$ \begin{aligned}&I+M\quad\xrightarrow{k_{s}}\quad P_{1}\\&P_{s}+M\quad\xrightarrow{k_{p}}\quad P_{s+1}\\&P_{s}+P_{r}\quad\xrightarrow{k_{t}}\quad D_{s+r}\\ \end{aligned} $$ 

describing a polymerization with initiation, propagation and recombination. The dimension of the related system of differential equations

 $$ \begin{aligned}\frac{\mathrm{d}I(t)}{\mathrm{d}t}&=-\boldsymbol{k}_{s}I(t)M(t)\\\frac{\mathrm{d}M(t)}{\mathrm{d}t}&=-\boldsymbol{k}_{s}I(t)M(t)-\boldsymbol{k}_{\mathrm{p}}M(t)\sum_{r}P_{r}(t)\\\frac{\mathrm{d}P_{1}(t)}{\mathrm{d}t}&=+\boldsymbol{k}_{s}I(t)M(t)-\boldsymbol{k}_{\mathrm{p}}M(t)P_{1}(t)-\boldsymbol{k}_{\mathrm{t}}M(t)P_{1}(t)\sum_{r}P_{r}(t)\\\frac{\mathrm{d}P_{s}(t)}{\mathrm{d}t}&=-\boldsymbol{k}_{\mathrm{p}}M(t)(P_{s}(t)-P_{s-1}(t))-\boldsymbol{k}_{\mathrm{t}}P_{s}(t)\sum_{r}P_{r}(t)\qquad s\geq2\\\frac{\mathrm{d}D_{s}(t)}{\mathrm{d}t}&=\frac{1}{2}k_{t}\sum_{r=1}^{s-1}P_{r}(t)P_{s-r}(t)\end{aligned} $$ 

depends on the reaction rate coefficients and the concentrations of the involved species and varies with time. The time-evolution of the chain-length distributions  $ (P_{\beta})_{s} $ and  $ (D_{\beta})_{s} $ and the concentrations of initiator I and monomer M have to be computed. The difficulty is that only for relative simple reaction schemes, as e. g. living polymerization (without chain termination) or certain radical polymerization processes (with an additional Bodenstein quasi-steady-state assumption), analytical solutions can be derived. On the other hand, a direct numerical integration of the above nonlinear and stiff system may take hours of computing time on a supercomputer for realistic dimensions. Interesting models additionally require the treatment of temperature and volume, the modeling of the operation mode of the reactor, the consideration of feed, mix and split strategies, grafting, branching and cross-linking. Some of these aspects can be incorporated in a model in terms of kinetic reaction steps, other require additional differential or algebraic equations or a posteriori analysis.

However, even the simple looking process (1) has complicated properties. The chain addition step propagates a given distribution to higher chain lengths whereas the maximum of the distribution decreases. Each elemental propagation reaction connects only the concentrations of molecules with neighbouring chain lengths. In the termination step all chains may interact (global behavior) leading to a smoothing of the whole distribution. The dynamic combination of various reaction steps can lead to very different forms of distributions for  $ P_s $ and  $ D_s $ dependent on the input concentrations and the reaction mode.

As a consequence of the above described difficulties, the numerical solution of equations as (2) requires some kind of approximation procedure including all distri-

butions, reaction steps and additional effects. For a formal approach we write Eq. (2) in the form of a countable system of ordinary differential equations

 $$ u_{s}^{\prime}(t)=f_{s}(u_{1}(t),\ldots,u_{s_{\mathrm{t o t}}^{-}}(t))\qquad\quad s=1,\ldots s_{\mathrm{t o t}} $$ 

The vector of the  $ u_s(t) $ will be called  $ u(t) $. In the above example the variables  $ u_s(t) $ are the concentrations of macromolecules  $ P_r $ and  $ D_r $ with chain length  $ r $ at a time  $ t $ and the concentrations of initiator and monomer. In contrast to ordinary differential equations the upper index  $ s_{\text{tot}} $ (i.e. the dimension of the complete system) may be very large ( $ 10^3 - 10^6 $ in practical examples). If for computational reasons such a large system has to be truncated at a smaller chain length  $ s_{\text{max}} $, a suitable value is rarely known a priori and may vary with time  $ t $ by orders of magnitude (closing problem). Thus a system (3) cannot be treated by standard numerical methods for ordinary differential equations in general. The theory of countable systems shows that their behavior is quite different from that of a high dimensional system of ordinary differential equations. The theoretical techniques for providing existence and uniqueness of solutions — in particular the choice of appropriate function spaces — resembles more the theoretical treatment of partial differential equations. A survey on this field is given in ref. $ ^9 $

## The modular approach — some reaction steps

As pointed out in the introduction, the aim of this research was to solve problems with arbitrary reaction steps leading to arbitrary distributions. Thus it should be possible to combine reaction steps from a comprehensive list. The following Tab. 1 shows typical reaction patterns and their difficulties. An algorithm has to be measured by its capability to treat such modules.

## Approaches to polyreaction kinetics — the way to the discrete h-p-method

A review of methods for the computation of molecular weight distributions has to consider efficiency and flexibility. We will give a brief, incomplete survey on popular and recent methods here. For all approaches details may be found in the literature. Thus we will only present some structural information, which lead to the motivation of the proposed Galerkin method of this article. Our selection of references only wants to give some hints. There are many important contributions which are not mentioned here.

## Model reduction by additional assumptions — quasi-steady-state assumption

Whenever it is known that the complete reaction system — or at least components of the system — can be considered as quasi-stationary (i.e. the respective derivatives can be set to zero), the kinetic equations may be simplified. For example, in radical polymerization the computation of the molecular weight distributions can be reduced to a quadrature of selected fractions (concentrations of the distribution at certain nodes of the chain length axis) of the dead polymer  $ {}^{13} $. Between the fractions the result can

<div style="text-align: center;">Tab. 1. Some important reaction steps in polymer systems</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Closed moments</td><td style='text-align: center; word-wrap: break-word;'>Characteristics</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propagation</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + M \xrightarrow{k} P_{s+1} $</td><td style='text-align: center; word-wrap: break-word;'>yes</td><td style='text-align: center; word-wrap: break-word;'>leads to Poisson distribution, local structure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Termination</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + P_{r} \xrightarrow{k(s,r)} D_{s+r}/D_{s} $</td><td style='text-align: center; word-wrap: break-word;'>yes/no depending on the structure of  $ k(s, r) $</td><td style='text-align: center; word-wrap: break-word;'>costly, global structure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transition</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + A \xrightarrow{k(s)} Q_{s} + B $</td><td style='text-align: center; word-wrap: break-word;'>yes/no depending on the structure of  $ k(s) $</td><td style='text-align: center; word-wrap: break-word;'>general step, local structure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Statistical degradation</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} \xrightarrow{k(s,r)} P_{r} + P_{s-r} $</td><td style='text-align: center; word-wrap: break-word;'>no</td><td style='text-align: center; word-wrap: break-word;'>may lead to high polydispersity, global structure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reversible polymerization</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} \xrightarrow{k} P_{s-1} + M $</td><td style='text-align: center; word-wrap: break-word;'>no</td><td style='text-align: center; word-wrap: break-word;'>local structure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transfer to polymer, long chain branching</td><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + D_{r} \xrightarrow{k \cdot r} D_{s} + P_{r} $</td><td style='text-align: center; word-wrap: break-word;'>no</td><td style='text-align: center; word-wrap: break-word;'>may lead to very high polydispersity, global structure</td></tr></table>

be interpolated. Because of the small computational effort of the quadrature, a rough knowledge of the maximum chain length and of the form of the distributions is sometimes sufficient. The disadvantage of model reductions is that a lot of insight into the process is required. QSSA only works for a very restricted class of problems — often related to radical polymerization. For the study of a new model a premature reduction of the modeling ideas is not desirable, of course.

## Lumping, continuous modeling

In a lumping process, certain components of the scheme are lumped together to a superspecies, which is also described by a differential equation. The lumping scheme must fit to the reaction scheme and its solution and requires a lot of insight into the process to be treated. A (difficult) change of the lumping mechanism during the time integration can be necessary. Besides, in most cases there is no error control of the chosen lumping. In refs. $ ^{2,14} $ lumping procedures are performed for a complicated degradation process reflecting how difficult and specialized lumping can be.

In a continuous modeling the discrete set of kinetic differential equations is expanded in a partial differential equation for large chain lengths, which is considered as a continuous variable. For such an expansion an unknown modeling error is introduced, which cannot be estimated — in particular for short polymer chains. Moreover, the resulting partial differential equation is often more complicated to solve than the original discrete problem and may include additional undesirable properties $ ^{6} $. Nevertheless, the continuous approach has been quite popular for a while. The reason is that techniques already developed for partial differential equations could be

applied to the converted discrete systems. However, the continuous equivalents to countable systems are partial integro-differential equations with convection and diffusion and for this class of problems (in particular when more than one polymer species has to be treated in a model) efficient and flexible numerical techniques are also missing (see the review article $ ^{15} $).

## Statistical methods

The statistical simulation of polyreaction kinetics has been tried for several years and is still quite popular. These methods are relatively flexible concerning the form of the arising distributions, but are rather time-consuming $ ^{3)} $, even if additional assumptions comparable to the QSSA are employed $ ^{16)} $. Moreover, there is no reliable error estimate controlling the truncation of the number of molecules or of the number of events. A recent thesis $ ^{17)} $ presents a comparison between Monte-Carlo-simulations and the Galerkin h-p-method for the polymer degradation of polylactid and it shows that the results are quite the same in this case, but the computing times differ by a factor of about 20.

## Approximations by means of moments

Actually, the method of moments is not an approach to compute distributions, but only describes certain aspects of distributions expressed in terms of the statistical moments  $ \mu_{k} $:

 $$ \mu_{k}(t)\left[P\right]:=\sum_{s=1}^{\infty}s^{k}P_{s}(t)\qquad k=0,1,\cdots $$ 

Nevertheless, the method of moments is the most popular approach and reflects some of the basic problems of polyreactions, e.g. analytical preprocessing, closing problem, method of lines (see below).

In general, the complete distribution can only be reconstructed by its moments, if all (infinite) moments are known. Otherwise, additional assumptions are required, which are usually based on the expected type of the molecular weight distribution. The choice of a basic distribution is the crucial point in such a method, of course. Thus, the moments are mainly used to compute the different mean values of a distribution. However, there are situations, where the method of moments can be a tool:

There is a theoretical evidence that the considered reaction scheme leads to a certain type of distribution. For example, a living polymerization leads to a Poisson distribution for long reaction times, in a radical polymerization the living polymer is close to a Schulz-Flory distribution over wide ranges of the process.

● There is practical experience (e.g. from measurements) that the solution is “close” to a chosen distribution function.

● An analysis of the mean values lets expect a distribution of a certain type.

If there are hints that some of the assumptions above are valid and if the moments of a given system can be computed (which is not always the case), only a few differential equations (sometimes numerically ill-conditioned) have to be solved.

The following disadvantages argue against a computation of distributions from moments:

● Distributions obtained by the method of moments do not permit an estimation, whether an assumed basis distribution has been correctly selected. A parameterized basis function always looks very smooth — even if it is absolutely wrong.

● The method of moments can only be recommended, if the considered process is already well studied and thus no surprises are to be expected. However, this is just not the case for models to be developed.

● A distribution computed by moments contains the moment information only. Additional findings cannot be obtained.

● Sometimes the differential equations for the moments cannot be derived in a closed form $ ^{1)} $.

Summarizing, the method of moments is helpful to adjust parameters of a model and for a first overview, but is problematic for reaction schemes resulting in complicated distributions and for chain-length dependent reaction steps of any kind.

## The discrete weighted Galerkin method

The development of this method in ref. $ ^{8} $ was based on the following considerations

● the polymer degree s is a discrete variable,

● the chain length distributions in typical processes are looking like familiar probability distributions,

• degrees of freedom have to be reduced as far as possible,

● an error estimation is required.

Starting point is an expansion of a chain length distribution  $ P_{s} $ into certain orthogonal polynomials, which are constructed by means of a weight function:

 $$ P_{s}(t)=\psi(s;\rho)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s;\rho) $$ 

The weight function  $ \psi $, depending on one or more parameters  $ \rho $, is chosen to describe the solution  $ P_{s} $ as well as possible. Then a truncation of Eq. (5) at an index m leads to a Galerkin approximation

 $$ P_{s}^{m}(t)=\psi(s,\rho)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s,\rho) $$ 

which should be close to $P_s$ for small $m$ (small means here: <20–50). The expansion coefficients $a_k(t)$ (called generalized moments) are computed by means of differential equations, which are derived by use of analytical relations of the polynomials $l_k(s; \rho)$. Defining a weighted inner product

 $$ \left(f,g\right)_{\psi}:=\sum_{s=1}^{\infty}f(s)g\left(s\right)\psi\left(s\right)^{-1} $$ 

the related orthogonal polynomials fulfill

 $$ (l_{k},l_{j})_{\psi}:=\delta_{k,j}\gamma_{j}\qquad\quad\gamma_{j}>0 $$ 

An expansion (5) is possible, if

 $$ \left|\left|P\right|\right|_{\psi}^{2}:=(P,P)_{\psi}<\infty $$ 

In this case, the expansion coefficients  $ a_{j} $ are tending to zero with a certain asymptotic behavior. This motivates an error estimate  $ \varepsilon_{m} $ for an approximation  $ P^{m} $ by

 $$ \varepsilon_{m}^{2}:=\left|\left|P^{m+1}-P^{m}\right|\right|_{\psi}^{2}=a_{m+1}^{2}\gamma_{m+1} $$ 

which works fine as long as the expansion coefficients are decreasing fast enough. If

 $$ \varepsilon_{m+1}\leq C\varepsilon_{m}\quad\mathrm{f o r}\quad m\geq m_{0}\mathrm{a n d}C<1 $$ 

we have $ ^{9)} $

 $$ \varepsilon_{m}\leq\bar{\varepsilon}_{m}\leq\left(\frac{1}{1-C}\right)^{1/2}\varepsilon_{m} $$ 

where  $ \varepsilon_m $ denotes the “true” error. The relation (6) is important, because it clearly shows the bounds and possibilities of the method. If, e.g.,  $ C < 0.8 $ the error estimate is quite reasonable (underestimation smaller than a factor 2), but if there are hints that  $ C $ is larger than 0.9 for one or a few pairs of coefficients, the attempt to approximate a distribution with the above expansion has to be dropped — the chosen weight function is not appropriate (note that in the h-p-method below, the situation of  $ C $ close to one is avoided, because the set of (local, unweighted) basis functions is switched by refining a grid). In order to make the approach as efficient as possible, the weight function has been adapted with time by changing its parameter(s) (moving weight function).

## Example

When  $ \psi $ is the Schulz-Flory distribution

 $$ \psi(s;\;\rho(t))\;=\;(1\;-\;\rho(t))\rho(t))^{s-1} $$ 

the orthogonal polynomials are the discrete Laguerre polynomials $ ^{8)} $. The moving weight function condition for  $ \rho = \rho(t) $ is then

 $$ \left(1-\rho(t)\right)^{-1}=\frac{\mu_{1}(t)\left[P\right]}{\mu_{0}(t)\left[P\right]} $$ 

In contrast to the method of moments, the following advantages of the discrete weighted Galerkin method can be noted:

● The computation of the generalized moments can be done numerically stable, the statistical moments can directly be obtained from the generalized moments. The weighted Galerkin method is somewhat like a pre-conditioner for the method of moments.

● The quality of the weight function and the approximation can be estimated.

● There is a global representation of the molecular weight distribution.

● The closing-problem of the moment equation for certain processes (e.g. polymer degradation) is solved in a natural way.

But resuming, the weighted Galerkin method is not flexible enough for a general treatment of polyreactions and requires too much insight again. The number of expansion coefficients has to be set a priori, no change is possible during the time integration (drawback of a method of lines, see below).

In order to overcome these problems (a part of them at least), Wulkow $ ^{9} $ extended the family of weight functions to

 $$ \psi\left(s;\rho,\alpha\right):=\left(1-\rho\right)^{1-\alpha}\binom{s-1-\alpha}{s-1}\rho^{s-1}\qquad0<\rho<1\qquad\alpha>-1 $$ 

including Schulz-Flory ( $ \alpha = 0 $) and Poisson distributions with parameter  $ \lambda $ ( $ \rho \cdot \alpha = \lambda $,  $ \rho $ small) as special cases. In combination with a time discretization of Rothe's type (see below), the extended method allows the treatment of nearly all types of reaction steps without analytical preprocessing, but was still restricted to distributions of a certain form. So after all, the situation was unsatisfactory for a general purpose solver, even if some interesting problems could be solved $ ^{9,18,19} $.

Related to the discrete weighted Galerkin-methods are discrete weighted collocation methods, where certain basis functions are chosen in a way that the kinetic equations are exactly fulfilled at nodes n of the chain length axis and the error for the residual is minimized $ ^{10} $. The transformation of the original balance equations into a numerical algorithm may be easier for collocation methods than for Galerkin methods, but there are difficulties with the change of the collocation nodes with time — in particular for strongly varying distributions. The computation of the collocation nodes depends on the choice of a weight function again.

Summarizing, the discrete weighted Galerkin and collocation methods have not been extensively applied to processes resulting in multi-modal or complex distributions because of restrictions induced by the weight functions.

## The method of lines' drawback

The most methods described above are methods of lines (MOL): a time-dependent distribution  $ P_s(t) $,  $ s $ “large”, is approximated by variables  $ a_j(t) $,  $ j $ “small”. A certain approximation scheme leads to differential equations for the  $ a_j $’s and the resulting system is numerically solved by a standard ODE-solver (ODE: ordinary differential equation). A reformulation of the approximation — change of number of  $ a_j $’s, reformulation of lumping scheme, new grid, etc. — during the time-integration is not possible or very difficult (regridding problem, often described by algebraic conditions on the coefficients  $ a_j(t) $). In many interesting cases, the equations for the  $ a_j $’s cannot

be given analytically, e.g. if complicated chain-length-dependent reaction coefficients are in the kinetic scheme. Then the right-hand side of the differential equation must be evaluated numerically. A sophisticated ODE-solver, however, detects the errors and disturbances of a numerical right-hand side as a non-smoothness of the differential equation and will fail or shrink down step sizes to unrealistic values, respectively. To avoid this, one could drop the adaptive error control (undesirable) or approximate the right-hand side close to machine accuracy (unrealistic). Thus, many attempts to find a general method for polyreactions ended at the bounds given by the method of lines: whenever analytical preprocessing of any kind is possible, some methods are equivalent, if not, none of the methods above will work.

## Summing up

If we reflect advantages and disadvantages of the methods described above, we get the following picture:

● If the solution distribution is close to a well-known basis function, the most efficient approximation can be obtained by a global approach (global means here: the complete chain length axis is modeled by one set of equations, one weight function). The reason is the global structure of many reaction steps.

● Some kind of a local approach is necessary to resolve the fine structure of a distribution (multiple maxima, steep flanks).

● The derivation of differential equations for any kind of “substitute variables” (moments, generalized moments, lumping parameters, fractions etc.) often requires certain analytical properties depending on the reaction steps in connection with the chosen approach. This analytical preprocessing must be replaced by a general numerical procedure for not restricting the class of problems to the usual ones (this prohibits a method of lines).

• An error estimation is necessary.

● Weight functions, clusters or grids have to be adapted with reaction time.

● No additional assumptions (as, e.g., QSSA) should be necessary.

● The interesting range of the chain length must be given by the method, not by a priori knowledge.

● The computational effort should not (strongly) depend on the degree of polymerization.

A connection of the positive and the prevention of the negative aspects, respectively, by means of new numerical techniques has led to a new numerical method (cf. Tab. 2.), which is called discrete Galerkin h-p-method (h-p: variable grid — variable order).

## The discrete Galerkin h-p-method

## Time discretization

Instead of a method of lines we use a time discretization by means of a Rothe method. This technique was introduced by Bornemann $ ^{20,21} $ for parabolic differential equations and was transferred and extended to polyreaction kinetics in ref. $ ^{9} $. We consider again Eq. (3). The idea is to discretize the countable system as an abstract

<div style="text-align: center;">Tab. 2. Progress of discrete Galerkin methods (rating quite subjective, of course)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Scheme</td><td style='text-align: center; word-wrap: break-word;'>Time discretization</td><td style='text-align: center; word-wrap: break-word;'>Preprocessing</td><td style='text-align: center; word-wrap: break-word;'>Distributions</td><td style='text-align: center; word-wrap: break-word;'>Reaction steps</td><td style='text-align: center; word-wrap: break-word;'>Surviving concepts</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>weighted I $ ^{8)} $</td><td style='text-align: center; word-wrap: break-word;'>weight functions, 1 parameter</td><td style='text-align: center; word-wrap: break-word;'>MOL</td><td style='text-align: center; word-wrap: break-word;'>analytical</td><td style='text-align: center; word-wrap: break-word;'>$ - $</td><td style='text-align: center; word-wrap: break-word;'>$ -/0 $</td><td style='text-align: center; word-wrap: break-word;'>discrete approach, type of error estimate, treatment of orthogonal functions</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>weighted II $ ^{9)} $</td><td style='text-align: center; word-wrap: break-word;'>weight function with two parameters</td><td style='text-align: center; word-wrap: break-word;'>Rothe</td><td style='text-align: center; word-wrap: break-word;'>numerical</td><td style='text-align: center; word-wrap: break-word;'>$ -/+ $</td><td style='text-align: center; word-wrap: break-word;'>+</td><td style='text-align: center; word-wrap: break-word;'>Rothe&#x27;s method, adaptive Gauss summation, general theory</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>h-p-method</td><td style='text-align: center; word-wrap: break-word;'>approximation on adaptive grid, no weight function</td><td style='text-align: center; word-wrap: break-word;'>Rothe</td><td style='text-align: center; word-wrap: break-word;'>numerical</td><td style='text-align: center; word-wrap: break-word;'>++</td><td style='text-align: center; word-wrap: break-word;'>++</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

ordinary differential equation in an appropriate sequence space. The theoretical reason for such an approach is given by semigroup theory  $ {}^{22} $. For an approximation  $ u_1 $ of the solution  $ u(t + \tau) $ after a time step from  $ t $ to  $ t + \tau $, we apply the semi-(linear)-implicit Euler  $ {}^{23} $ scheme

 $$ \begin{array}{l} (I - \tau A)\Delta u  =  \tau f(\varphi)\\ \\ u_{1}=(\varphi + \Delta u \end{array} $$ 

with  $ \varphi = u(t) $, A the derivative  $ f_u(\varphi) $ and I the identity matrix. We obtain a linear system which seems as difficult to be solved as the original differential equation (3) because of its high dimension. Moreover, each time discretization introduces a certain time error  $ \varepsilon_T $ which an adaptive stepsize control tries to keep below a tolerance  $ \tau_L $. For standard differential equations, system (7) can be solved within the machine accuracy, so the time steps have to be chosen only with respect to  $ \tau_L $. The idea of Bornemann is that the trajectory of the solution  $ u(t) $ in an abstract space  $ X $ (e.g. a function or sequence space) may be slightly perturbed without affecting stepsizes and accuracy (Fig. 1).

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_599_573_872.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Fig. 1. Idea of the Rothe method. The sizes of the ellipses denote the stationary tolerance for an in-exact method, their centers indicate the results of “exact” time steps</div>


If we assume, that the solution of Eq. (7) can only be approximated, the time error  $ \varepsilon_{\mathrm{T}} $ and the stationary error  $ \varepsilon_{\mathrm{S}} $ can be matched such that the complete time step is within accuracy  $ \tau_{0} $. It is the special feature of the Rothe method, that the stationary tolerance  $ \tau_{0} $ for the error  $ \varepsilon_{\mathrm{S}} $ need not be too small, when an appropriate discretization scheme is used. Bornemann's multiplicative error correction (MEC) (given by the formulas (7) and (8)) is here the method of choice, because it avoids differences at the computation of the error estimates. The theory for linear systems leads to  $ \tau_{0} $s = 1/8  $ \tau_{0} $l (instead of  $ \tau_{0} $s = 0.001  $ \tau_{0} $l for extrapolation methods); for nonlinear systems, the setting  $ \tau_{0} $s = 1/16  $ \tau_{0} $l has been sufficient for a large range of problems (a reasonable value for  $ \tau_{0} $l is here between 0.1–0.01).

The required estimate  $ \eta_1 $ of the time error  $ \|u_1 - u(t + \tau)\| $ ( $ | \dots | $ an appropriate norm) can be computed by solving a correction equation with the same left-hand side matrix as in Eq. (7)

The simulation of molecular weight distributions in polyreaction kinetics ...

 $$ \begin{aligned}(\mathbf{I}-\tau A)\boldsymbol{\eta}_{1}&=-\frac{1}{2}\tau^{2}A f\left(\varphi\right)\\u_{2}&=u_{1}+\eta_{1}\end{aligned} $$ 

such that no additional linear system has to be treated. Besides, the approximation  $ u_{2} $ is of the increased order 2. Whenever a time step with (old) step size  $ \tau $ has been performed with the schemes (7) and (8), a new step size  $ \tau_{new} $ can be computed by

 $$ \tau_{\mathrm{new}}=\tau\sqrt{\frac{\mathrm{Tol}}{\kappa\left|\left|\boldsymbol{\eta}_{1}\right|\right|}} $$ 

where  $ \kappa < 1 $ is a safety factor. Further details of this kind of a Rothe method can be found in ref. $ ^{21} $, a (complete adaptive) algorithm for kinetic equations in polyreactions based on this theory, but with global, less flexible basis functions than proposed here, is described in ref. $ ^{9} $

Up to this point, it is not yet prescribed how the solutions of Eqs. (7) and (8) actually should be computed or approximated. The following time control is a general one for ordinary, partial and countable differential equations and can also be extended to algebraic systems. Moreover, with slight changes, an inexact Newton method for computing stationary solutions can be easily derived.

## Algorithm I, time control

Given: approximation  $ \varphi $ of  $ u(t) $, (time) error estimate  $ \varepsilon_{T}(t) $.

1. Compute new time step length by Eq. (9), where  $ \|\eta_1\| = \varepsilon_T(t) $.

2. Solve system (7) within accuracy to  $ L \cdot (1/16) $ using Algorithm II → finite representation of the solution.

3. Solve system (8): Use the representation for the solution obtained in 2.

4. Estimate: Compute a new time estimate.

5. Loop control: If the error is smaller than TOL set  $ \varphi = u_{2}, t = t + \tau $, and start next step in 1, otherwise reduce stepsize and start in 2.

## Approximation of distributions within a time step

After generally describing the time discretization it “remains” to solve Eq. (7) within a certain accuracy. We write the stationary linear problems in Eqs. (7) and (8) as

 $$ Bu=b\quad 爻 \quad B=\mathbf{I}-\tau A $$ 

where the high dimensional vector  $ \boldsymbol{b} $ (resp.  $ \boldsymbol{u} $) contains all components of the kinetic equations or their numerical representation at time  $ t(t + \tau) $.

The task is now to find an approximation  $ u_n $ of  $ u $, with  $ \|u_u - u\| < \mathrm{tol}_S $. Here, we want to approximate the solution of Eq. (7) by means of the following finite element type Galerkin method:

Using a multi-level algorithm we have to construct a sub-division of the s-axis (chain-length-axis) as shown in Fig. 2 and on each interval I we use a (local) expansion  $ u_s^j $ of  $ u_s $ given by

 $$ \boldsymbol{u}_{s}^{j}\bigg|_{I_{t}^{j}}=\sum_{k=0}^{p_{t}^{j}}a_{k l}^{j}t_{k,l}^{j}\left(s\right) $$ 

(j: no. of level, l: no. of interval), where the polynomials  $ t_{k,l}^{j} $ are the well-known discrete Chebyshev polynomials of degree  $ k^{24,25} $. The number of expansion coefficients  $ p_{l}^{j} $ may differ from interval to interval, such that the form of a chain length distribution can be resolved by varying grid and order. The node-order-distribution on the final grid

 $$ \varDelta_{F}=\{(I_{l},p_{l})\;\ldots(I_{m},p_{m})\} $$ 

has to be chosen such that the amount of work necessary to compute the whole approximation is as small as possible. The construction is started with one initial grid  $ \Delta_0 $ on the interval  $ [0, s_{\max}] $,  $ s_{\max} $ possibly very large, and proceeds from level to level by refinement or increasing of the order, where information from the previous levels is used. An example of the refinement strategy for two successive levels is shown in Fig. 3.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>(i_1, p_i)</th><th style='text-align: center;'>(i_2, p_i^2)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>95</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>75</td><td style='text-align: center;'>65</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>55</td><td style='text-align: center;'>45</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>40</td><td style='text-align: center;'>30</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>28</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>18</td><td style='text-align: center;'>12</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>12</td><td style='text-align: center;'>8</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>8</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>5</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>3</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 2. General h-p-pattern</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Point</th><th style='text-align: center;'>(l₁, p₁)</th><th style='text-align: center;'>(l₂, p₂)</th><th style='text-align: center;'>(l₃, p₃)</th><th style='text-align: center;'>(l₄, p₄)</th><th style='text-align: center;'>(l₅, p₅)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>(1, 1)</td><td style='text-align: center;'>(1, 1)</td><td style='text-align: center;'>(1, 1)</td><td style='text-align: center;'>(1, 1)</td><td style='text-align: center;'>(1, 1)</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>(1, 2)</td><td style='text-align: center;'>(1, 2)</td><td style='text-align: center;'>(1, 2)</td><td style='text-align: center;'>(1, 2)</td><td style='text-align: center;'>(1, 2)</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>(1, 3)</td><td style='text-align: center;'>(1, 3)</td><td style='text-align: center;'>(1, 3)</td><td style='text-align: center;'>(1, 3)</td><td style='text-align: center;'>(1, 3)</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>(1, 4)</td><td style='text-align: center;'>(1, 4)</td><td style='text-align: center;'>(1, 4)</td><td style='text-align: center;'>(1, 4)</td><td style='text-align: center;'>(1, 4)</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>(1, 5)</td><td style='text-align: center;'>(1, 5)</td><td style='text-align: center;'>(1, 5)</td><td style='text-align: center;'>(1, 5)</td><td style='text-align: center;'>(1, 5)</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>(1, 6)</td><td style='text-align: center;'>(1, 6)</td><td style='text-align: center;'>(1, 6)</td><td style='text-align: center;'>(1, 6)</td><td style='text-align: center;'>(1, 6)</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>(1, 7)</td><td style='text-align: center;'>(1, 7)</td><td style='text-align: center;'>(1, 7)</td><td style='text-align: center;'>(1, 7)</td><td style='text-align: center;'>(1, 7)</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>(1, 8)</td><td style='text-align: center;'>(1, 8)</td><td style='text-align: center;'>(1, 8)</td><td style='text-align: center;'>(1, 8)</td><td style='text-align: center;'>(1, 8)</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>(1, 9)</td><td style='text-align: center;'>(1, 9)</td><td style='text-align: center;'>(1, 9)</td><td style='text-align: center;'>(1, 9)</td><td style='text-align: center;'>(1, 9)</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>(1, 10)</td><td style='text-align: center;'>(1, 10)</td><td style='text-align: center;'>(1, 10)</td><td style='text-align: center;'>(1, 10)</td><td style='text-align: center;'>(1, 10)</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>(1, 11)</td><td style='text-align: center;'>(1, 11)</td><td style='text-align: center;'>(1, 11)</td><td style='text-align: center;'>(1, 11)</td><td style='text-align: center;'>(1, 11)</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>(1, 12)</td><td style='text-align: center;'>(1, 12)</td><td style='text-align: center;'>(1, 12)</td><td style='text-align: center;'>(1, 12)</td><td style='text-align: center;'>(1, 12)</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>(1, 13)</td><td style='text-align: center;'>(1, 13)</td><td style='text-align: center;'>(1, 13)</td><td style='text-align: center;'>(1, 13)</td><td style='text-align: center;'>(1, 13)</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>(1, 14)</td><td style='text-align: center;'>(1, 14)</td><td style='text-align: center;'>(1, 14)</td><td style='text-align: center;'>(1, 14)</td><td style='text-align: center;'>(1, 14)</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>(1, 15)</td><td style='text-align: center;'>(1, 15)</td><td style='text-align: center;'>(1, 15)</td><td style='text-align: center;'>(1, 15)</td><td style='text-align: center;'>(1, 15)</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>(1, 16)</td><td style='text-align: center;'>(1, 16)</td><td style='text-align: center;'>(1, 16)</td><td style='text-align: center;'>(1, 16)</td><td style='text-align: center;'>(1, 16)</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>(1, 17)</td><td style='text-align: center;'>(1, 17)</td><td style='text-align: center;'>(1, 17)</td><td style='text-align: center;'>(1, 17)</td><td style='text-align: center;'>(1, 17)</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>(1, 18)</td><td style='text-align: center;'>(1, 18)</td><td style='text-align: center;'>(1, 18)</td><td style='text-align: center;'>(1, 18)</td><td style='text-align: center;'>(1, 18)</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>(1, 19)</td><td style='text-align: center;'>(1, 19)</td><td style='text-align: center;'>(1, 19)</td><td style='text-align: center;'>(1, 19)</td><td style='text-align: center;'>(1, 19)</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>(1, 20)</td><td style='text-align: center;'>(1, 20)</td><td style='text-align: center;'>(1, 20)</td><td style='text-align: center;'>(1, 20)</td><td style='text-align: center;'>(1, 20)</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>(1, 21)</td><td style='text-align: center;'>(1, 21)</td><td style='text-align: center;'>(1, 21)</td><td style='text-align: center;'>(1, 21)</td><td style='text-align: center;'>(1, 21)</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>(1, 22)</td><td style='text-align: center;'>(1, 22)</td><td style='text-align: center;'>(1, 22)</td><td style='text-align: center;'>(1, 22)</td><td style='text-align: center;'>(1, 22)</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>(1, 23)</td><td style='text-align: center;'>(1, 23)</td><td style='text-align: center;'>(1, 23)</td><td style='text-align: center;'>(1, 23)</td><td style='text-align: center;'>(1, 23)</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>(1, 24)</td><td style='text-align: center;'>(1, 24)</td><td style='text-align: center;'>(1, 24)</td><td style='text-align: center;'>(1, 24)</td><td style='text-align: center;'>(1, 24)</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>(1, 25)</td><td style='text-align: center;'>(1, 25)</td><td style='text-align: center;'>(1, 25)</td><td style='text-align: center;'>(1, 25)</td><td style='text-align: center;'>(1, 25)</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>(1, 26)</td><td style='text-align: center;'>(1, 26)</td><td style='text-align: center;'>(1, 26)</td><td style='text-align: center;'>(1, 26)</td><td style='text-align: center;'>(1, 26)</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>(1, 27)</td><td style='text-align: center;'>(1, 27)</td><td style='text-align: center;'>(1, 27)</td><td style='text-align: center;'>(1, 27)</td><td style='text-align: center;'>(1, 27)</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>(1, 28)</td><td style='text-align: center;'>(1, 28)</td><td style='text-align: center;'>(1, 28)</td><td style='text-align: center;'>(1, 28)</td><td style='text-align: center;'>(1, 28)</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>(1, 29)</td><td style='text-align: center;'>(1, 29)</td><td style='text-align: center;'>(1, 29)</td><td style='text-align: center;'>(1, 29)</td><td style='text-align: center;'>(1, 29)</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>(1, 30)</td><td style='text-align: center;'>(1, 30)</td><td style='text-align: center;'>(1, 30)</td><td style='text-align: center;'>(1, 30)</td><td style='text-align: center;'>(1, 30)</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>(1, 31)</td><td style='text-align: center;'>(1, 31)</td><td style='text-align: center;'>(1, 31)</td><td style='text-align: center;'>(1, 31)</td><td style='text-align: center;'>(1, 31)</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>(1, 32)</td><td style='text-align: center;'>(1, 32)</td><td style='text-align: center;'>(1, 32)</td><td style='text-align: center;'>(1, 32)</td><td style='text-align: center;'>(1, 32)</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>(1, 33)</td><td style='text-align: center;'>(1, 33)</td><td style='text-align: center;'>(1, 33)</td><td style='text-align: center;'>(1, 33)</td><td style='text-align: center;'>(1, 33)</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>(1, 34)</td><td style='text-align: center;'>(1, 34)</td><td style='text-align: center;'>(1, 34)</td><td style='text-align: center;'>(1, 34)</td><td style='text-align: center;'>(1, 34)</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>(1, 35)</td><td style='text-align: center;'>(1, 35)</td><td style='text-align: center;'>(1, 35)</td><td style='text-align: center;'>(1, 35)</td><td style='text-align: center;'>(1, 35)</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>(1, 36)</td><td style='text-align: center;'>(1, 36)</td><td style='text-align: center;'>(1, 36)</td><td style='text-align: center;'>(1, 36)</td><td style='text-align: center;'>(1, 36)</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>(1, 37)</td><td style='text-align: center;'>(1, 37)</td><td style='text-align: center;'>(1, 37)</td><td style='text-align: center;'>(1, 37)</td><td style='text-align: center;'>(1, 37)</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>(1, 38)</td><td style='text-align: center;'>(1, 38)</td><td style='text-align: center;'>(1, 38)</td><td style='text-align: center;'>(1, 38)</td><td style='text-align: center;'>(1, 38)</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>(1, 39)</td><td style='text-align: center;'>(1, 39)</td><td style='text-align: center;'>(1, 39)</td><td style='text-align: center;'>(1, 39)</td><td style='text-align: center;'>(1, 39)</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>(1, 40)</td><td style='text-align: center;'>(1, 40)</td><td style='text-align: center;'>(1, 40)</td><td style='text-align: center;'>(1, 40)</td><td style='text-align: center;'>(1, 40)</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>(1, 41)</td><td style='text-align: center;'>(1, 41)</td><td style='text-align: center;'>(1, 41)</td><td style='text-align: center;'>(1, 41)</td><td style='text-align: center;'>(1, 41)</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>(1, 42)</td><td style='text-align: center;'>(1, 42)</td><td style='text-align: center;'>(1, 42)</td><td style='text-align: center;'>(1, 42)</td><td style='text-align: center;'>(1, 42)</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>(1, 43)</td><td style='text-align: center;'>(1, 43)</td><td style='text-align: center;'>(1, 43)</td><td style='text-align: center;'>(1, 43)</td><td style='text-align: center;'>(1, 43)</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>(1, 44)</td><td style='text-align: center;'>(1, 44)</td><td style='text-align: center;'>(1, 44)</td><td style='text-align: center;'>(1, 44)</td><td style='text-align: center;'>(1, 44)</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>(1, 45)</td><td style='text-align: center;'>(1, 45)</td><td style='text-align: center;'>(1, 45)</td><td style='text-align: center;'>(1, 45)</td><td style='text-align: center;'>(1, 45)</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>(1, 46)</td><td style='text-align: center;'>(1, 46)</td><td style='text-align: center;'>(1, 46)</td><td style='text-align: center;'>(1, 46)</td><td style='text-align: center;'>(1, 46)</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>(1, 47)</td><td style='text-align: center;'>(1, 47)</td><td style='text-align: center;'>(1, 47)</td><td style='text-align: center;'>(1, 47)</td><td style='text-align: center;'>(1, 47)</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>(1, 48)</td><td style='text-align: center;'>(1, 48)</td><td style='text-align: center;'>(1, 48)</td><td style='text-align: center;'>(1, 48)</td><td style='text-align: center;'>(1, 48)</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>(1, 49)</td><td style='text-align: center;'>(1, 49)</td><td style='text-align: center;'>(1, 49)</td><td style='text-align: center;'>(1, 49)</td><td style='text-align: center;'>(1, 49)</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>(1, 50)</td><td style='text-align: center;'>(1, 50)</td><td style='text-align: center;'>(1, 50)</td><td style='text-align: center;'>(1, 50)</td><td style='text-align: center;'>(1, 50)</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>(1, 51)</td><td style='text-align: center;'>(1, 51)</td><td style='text-align: center;'>(1, 51)</td><td style='text-align: center;'>(1, 51)</td><td style='text-align: center;'>(1, 51)</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>(1, 52)</td><td style='text-align: center;'>(1, 52)</td><td style='text-align: center;'>(1, 52)</td><td style='text-align: center;'>(1, 52)</td><td style='text-align: center;'>(1, 52)</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>(1, 53)</td><td style='text-align: center;'>(1, 53)</td><td style='text-align: center;'>(1, 53)</td><td style='text-align: center;'>(1, 53)</td><td style='text-align: center;'>(1, 53)</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>(1, 54)</td><td style='text-align: center;'>(1, 54)</td><td style='text-align: center;'>(1, 54)</td><td style='text-align: center;'>(1, 54)</td><td style='text-align: center;'>(1, 54)</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>(1, 55)</td><td style='text-align: center;'>(1, 55)</td><td style='text-align: center;'>(1, 55)</td><td style='text-align: center;'>(1, 55)</td><td style='text-align: center;'>(1, 55)</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>(1, 56)</td><td style='text-align: center;'>(1, 56)</td><td style='text-align: center;'>(1, 56)</td><td style='text-align: center;'>(1, 56)</td><td style='text-align: center;'>(1, 56)</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>(1, 57)</td><td style='text-align: center;'>(1, 57)</td><td style='text-align: center;'>(1, 57)</td><td style='text-align: center;'>(1, 57)</td><td style='text-align: center;'>(1, 57)</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>(1, 58)</td><td style='text-align: center;'>(1, 58)</td><td style='text-align: center;'>(1, 58)</td><td style='text-align: center;'>(1, 58)</td><td style='text-align: center;'>(1, 58)</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>(1, 59)</td><td style='text-align: center;'>(1, 59)</td><td style='text-align: center;'>(1, 59)</td><td style='text-align: center;'>(1, 59)</td><td style='text-align: center;'>(1, 59)</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>(1, 60)</td><td style='text-align: center;'>(1, 60)</td><td style='text-align: center;'>(1, 60)</td><td style='text-align: center;'>(1, 60)</td><td style='text-align: center;'>(1, 60)</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>(1, 61)</td><td style='text-align: center;'>(1, 61)</td><td style='text-align: center;'>(1, 61)</td><td style='text-align: center;'>(1, 61)</td><td style='text-align: center;'>(1, 61)</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>(1, 62)</td><td style='text-align: center;'>(1, 62)</td><td style='text-align: center;'>(1, 62)</td><td style='text-align: center;'>(1, 62)</td><td style='text-align: center;'>(1, 62)</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>(1, 63)</td><td style='text-align: center;'>(1, 63)</td><td style='text-align: center;'>(1, 63)</td><td style='text-align: center;'>(1, 63)</td><td style='text-align: center;'>(1, 63)</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>(1, 64)</td><td style='text-align: center;'>(1, 64)</td><td style='text-align: center;'>(1, 64)</td><td style='text-align: center;'>(1, 64)</td><td style='text-align: center;'>(1, 64)</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>(1, 65)</td><td style='text-align: center;'>(1, 65)</td><td style='text-align: center;'>(1, 65)</td><td style='text-align: center;'>(1, 65)</td><td style='text-align: center;'>(1, 65)</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>(1, 66)</td><td style='text-align: center;'>(1, 66)</td><td style='text-align: center;'>(1, 66)</td><td style='text-align: center;'>(1, 66)</td><td style='text-align: center;'>(1, 66)</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>(1, 67)</td><td style='text-align: center;'>(1, 67)</td><td style='text-align: center;'>(1, 67)</td><td style='text-align: center;'>(1, 67)</td><td style='text-align: center;'>(1, 67)</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>(1, 68)</td><td style='text-align: center;'>(1, 68)</td><td style='text-align: center;'>(1, 68)</td><td style='text-align: center;'>(1, 68)</td><td style='text-align: center;'>(1, 68)</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>(1, 69)</td><td style='text-align: center;'>(1, 69)</td><td style='text-align: center;'>(1, 69)</td><td style='text-align: center;'>(1, 69)</td><td style='text-align: center;'>(1, 69)</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>(1, 70)</td><td style='text-align: center;'>(1, 70)</td><td style='text-align: center;'>(1, 70)</td><td style='text-align: center;'>(1, 70)</td><td style='text-align: center;'>(1, 70)</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>(1, 71)</td><td style='text-align: center;'>(1, 71)</td><td style='text-align: center;'>(1, 71)</td><td style='text-align: center;'>(1, 71)</td><td style='text-align: center;'>(1, 71)</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>(1, 72)</td><td style='text-align: center;'>(1, 72)</td><td style='text-align: center;'>(1, 72)</td><td style='text-align: center;'>(1, 72)</td><td style='text-align: center;'>(1, 72)</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>(1, 73)</td><td style='text-align: center;'>(1, 73)</td><td style='text-align: center;'>(1, 73)</td><td style='text-align: center;'>(1, 73)</td><td style='text-align: center;'>(1, 73)</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>(1, 74)</td><td style='text-align: center;'>(1, 74)</td><td style='text-align: center;'>(1, 74)</td><td style='text-align: center;'>(1, 74)</td><td style='text-align: center;'>(1, 74)</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>(1, 75)</td><td style='text-align: center;'>(1, 75)</td><td style='text-align: center;'>(1, 75)</td><td style='text-align: center;'>(1, 75)</td><td style='text-align: center;'>(1, 75)</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>(1, 76)</td><td style='text-align: center;'>(1, 76)</td><td style='text-align: center;'>(1, 76)</td><td style='text-align: center;'>(1, 76)</td><td style='text-align: center;'>(1, 76)</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>(1, 77)</td><td style='text-align: center;'>(1, 77)</td><td style='text-align: center;'>(1, 77)</td><td style='text-align: center;'>(1, 77)</td><td style='text-align: center;'>(1, 77)</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>(1, 78)</td><td style='text-align: center;'>(1, 78)</td><td style='text-align: center;'>(1, 78)</td><td style='text-align: center;'>(1, 78)</td><td style='text-align: center;'>(1, 78)</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>(1, 79)</td><td style='text-align: center;'>(1, 79)</td><td style='text-align: center;'>(1, 79)</td><td style='text-align: center;'>(1, 79)</td><td style='text-align: center;'>(1, 79)</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>(1, 80)</td><td style='text-align: center;'>(1, 80)</td><td style='text-align: center;'>(1, 80)</td><td style='text-align: center;'>(1, 80)</td><td style='text-align: center;'>(1, 80)</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>(1, 81)</td><td style='text-align: center;'>(1, 81)</td><td style='text-align: center;'>(1, 81)</td><td style='text-align: center;'>(1, 81)</td><td style='text-align: center;'>(1, 81)</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>(1, 82)</td><td style='text-align: center;'>(1, 82)</td><td style='text-align: center;'>(1, 82)</td><td style='text-align: center;'>(1, 82)</td><td style='text-align: center;'>(1, 82)</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>(1, 83)</td><td style='text-align: center;'>(1, 83)</td><td style='text-align: center;'>(1, 83)</td><td style='text-align: center;'>(1, 83)</td><td style='text-align: center;'>(1, 83)</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>(1, 84)</td><td style='text-align: center;'>(1, 84)</td><td style='text-align: center;'>(1, 84)</td><td style='text-align: center;'>(1, 84)</td><td style='text-align: center;'>(1, 84)</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>(1, 85)</td><td style='text-align: center;'>(1, 85)</td><td style='text-align: center;'>(1, 85)</td><td style='text-align: center;'>(1, 85)</td><td style='text-align: center;'>(1, 85)</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>(1, 86)</td><td style='text-align: center;'>(1, 86)</td><td style='text-align: center;'>(1, 86)</td><td style='text-align: center;'>(1, 86)</td><td style='text-align: center;'>(1, 86)</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>(1, 87)</td><td style='text-align: center;'>(1, 87)</td><td style='text-align: center;'>(1, 87)</td><td style='text-align: center;'>(1, 87)</td><td style='text-align: center;'>(1, 87)</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>(1, 88)</td><td style='text-align: center;'>(1, 88)</td><td style='text-align: center;'>(1, 88)</td><td style='text-align: center;'>(1, 88)</td><td style='text-align: center;'>(1, 88)</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>(1, 89)</td><td style='text-align: center;'>(1, 89)</td><td style='text-align: center;'>(1, 89)</td><td style='text-align: center;'>(1, 89)</td><td style='text-align: center;'>(1, 89)</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>(1, 90)</td><td style='text-align: center;'>(1, 90)</td><td style='text-align: center;'>(1, 90)</td><td style='text-align: center;'>(1, 90)</td><td style='text-align: center;'>(1, 90)</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>(1, 91)</td><td style='text-align: center;'>(1, 91)</td><td style='text-align: center;'>(1, 91)</td><td style='text-align: center;'>(1, 91)</td><td style='text-align: center;'>(1, 91)</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>(1, 92)</td><td style='text-align: center;'>(1, 92)</td><td style='text-align: center;'>(1, 92)</td><td style='text-align: center;'>(1, 92)</td><td style='text-align: center;'>(1, 92)</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>(1, 93)</td><td style='text-align: center;'>(1, 93)</td><td style='text-align: center;'>(1, 93)</td><td style='text-align: center;'>(1, 93)</td><td style='text-align: center;'>(1, 93)</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>(1, 94)</td><td style='text-align: center;'>(1, 94)</td><td style='text-align: center;'>(1, 94)</td><td style='text-align: center;'>(1, 94)</td><td style='text-align: center;'>(1, 94)</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>(1, 95)</td><td style='text-align: center;'>(1, 95)</td><td style='text-align: center;'>(1, 95)</td><td style='text-align: center;'>(1, 95)</td><td style='text-align: center;'>(1, 95)</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 3. Example for a transition in a h-p-multilevel method</div>


Whereas on the intervals  $ I_{1} $ and  $ I_{4} $ the order of the (local) approximation is increased by one,  $ I_{3} $ is bisected and the new orders are set to one (acetually, the choice of the order p on the next level is a question of the refinement strategy). The remaining intervals are not changed.

The motivation for this algorithm can be illustrated by considering the approximation of a (pointwise) given chain length distribution. If such a distribution is very

smooth (in an optic sense) we can expect that a polynomial expansion with only a few expansion terms might be sufficient. However, such global solutions are only obtained in certain special processes (e.g. radical homopolymerization). For distributions  $ u_s $ with steep flanks or for multimodal distributions, we require an automatic local adaptation to avoid bad and inefficient approximations. On the other hand, a purely local approximation scheme as, e.g., a discrete analogue to finite elements with linear basis functions is not the appropriate choice here, since it leads to too many degrees of freedom. Thus we suggest a mixture of local and global approaches, which is in the literature on the numerical solution of partial differential equations known as h-p-method $ ^{[26]} $.

The practical implementation of this basis scheme requires the treatment of many aspects, which cannot be explained here in all details. Thus we restrict ourselves to the main modules of the h-p-algorithm.

Algorithm II, approximation (finite representation) of the solution for one time step

Given: approximation $\varphi$ of $u(t)$, represented by a node-order-pattern $\varLambda$ and a maximal chain length $s_{\max}$, stepsize $\tau$ and tolerance $\mathrm{TOL}_{s}$.

1. Predict a new maximal chain length.

1. Predict a new maximal chain length.

2. Propagation of grids. Extract an initial node-order-pattern from the representation of  $ \varphi $.

3. New representation. Build up a new node-order-pattern, such that  $ \varepsilon_{S} < \mathrm{tol}_{s} \Rightarrow $ Algorithm III

## Maximal chain length — truncation index

In contrast to direct simulation methods, the truncation of the chain length is not a crucial task here. Even if the truncation index is overestimated by orders of magnitude, there is no dramatic increase of computational effort. Nevertheless, the following device gives a reliable estimate of a sufficient truncation index. If a distribution has been approximated up to chain length  $ s_{\text{max}}^{\text{old}} $, the new truncation index  $ s_{\text{max}}^{\text{new}} $ can be computed by

 $$ s_{\max}^{\mathrm{new}}=\frac{\mu_{1}}{\mu_{0}}+\kappa\sqrt{\frac{\mu_{2}}{\mu_{0}}-\left(\frac{\mu_{1}}{\mu_{0}}\right)^{2}}\quad\kappa=10 $$ 

with a safety factor  $ \kappa $ and the moments  $ \mu_{0}, \mu_{1}, \mu_{2} $ of the given distribution.

This formula is a result of the Chebyshev inequality of statistics $ ^{27} $ applied to the chain length distribution. It can be used for estimating how much of the total concentration ( $ \mu_0 $) of a distribution is not in an interval  $ [1, s_{\max}] $. If one wants to compute truncation indices for weight- or  $ w(\log s) $-distributions, the moments  $ \mu_0, \mu_1, \mu_2 $ above have to be replaced by  $ \mu_k, \mu_{k+1}, \mu_{k+2}, k = 1, 2 $, respectively.

Example: For a Schulz-Flory distribution with parameter rho = 0.99 we obtain  $ s_{\max} \approx 1100 $, for a Poisson distribution with mean value 100 we obtain  $ s_{\max} \approx 200 $.

Even for distributions with high polydispersity this device works quite reliable as shown in the numerical section.

Remark: The dynamic of the integration process can additionally be captured by setting

 $$ s_{\mathrm{m a x}}^{\mathrm{n c w}}=s_{\mathrm{m a x}}^{\mathrm{n e w}}+c(s_{\mathrm{m a x}}^{\mathrm{n e w}}-s_{\mathrm{m a x}}^{\mathrm{o l d}})\quad c>0 $$ 

after evaluation of Eq. (11).

## Grid propagation

The most simple way to start the multilevel process would be a node-order-pattern of the form

 $$ \varDelta_{0}=\{([1,s_{\operatorname*{m a x}}],2)\} $$ 

But this would imply the loss of all information obtained in previous time steps resulting in too much refinement levels. The other extreme is to start with the final pattern from the last time step, but this leads to an increasing number of variables. Thus we need an heuristic, which keeps as much information as possible but is also able to delete nodes or to decrease orders. A simple device for that is:

## Heuristic 1

1. Take the final grid of the last step.

2. Eliminate each second interval.

3. Reduce all remaining orders by a certain number (e.g. by 1).

This strategy has turned out to be a very stable and reliable one, in particular for moving distributions, where old grid points have to be eliminated by time. However, when a distribution does not change its form in a time step, the reconstruction of the optimal grid can take a few levels longer than apparently necessary. An improvement of heuristic 1 is obtained by

## Heuristic 2

1. Take the final grid of the last step.

2. Eliminate all intervals with low order, i.e. intervals which are possibly not necessary.

3. Add an eliminated interval to the neighborhood interval with lower order.

The experiences with many attempts for such devices show that the grid propagation should not depend on error estimates, because in this case the algorithm has less chance to recover if an estimate fails.

Now we turn to the inner loop of the h-p-algorithm, where the multilevel process is performed.

## Algorithm III, building up the final node-order-pattern

Given: a starting grid and an error estimate of the local expansion on intervals  $ I_{i} $ of the grid.

1. Type of improvement: Decide, whether an interval  $ I_{i} $ has to be bisected or the present polynomial order p has to be increased. For that, the behavior of the error of the local expansion is compared to an error prediction model.

2. Cut-value: Compute a threshold value to decide which intervals have to be changed (bisection or increase of order).

3. Assemble and solve: Build up the Galerkin equations which describe the expansion coefficients on all intervals for all distributions and solve them.

4. Estimate: Estimate the error of the obtained solution. This works comparable to the weighted Galerkin method by considering the (local) expansion coefficients  $ a_{n+1}^{l} $.

5. Loop control: If the error is smaller than the required tolerance stop, otherwise go back to 1.

## Refinement strategy

The refinement strategy has to reduce not only the number of degrees of freedom but also the number of levels to obtain the final node-order-pattern. This can be done by a work-oriented device. For that, the following questions have to be answered:

● How does the error behave, if an interval is refined?

● How does the error behave, if the order is increased?

● How large is the effort to perform one of the above operations related to the obtained error and the required error?

● Which intervals will be improved?

We exemplify this part of the algorithm by the following situation: given an interval with width h, order p and error  $ \varepsilon(h, p) $. Let us assume that we also know the errors  $ \varepsilon(h, p - 1) $,  $ \varepsilon(2h, p - 1) $ and  $ \varepsilon(2h, p) $. Then the error predictions  $ \varepsilon(h/2, p - 1) $ and  $ \varepsilon(h, p + 1) $ can be obtained by extrapolation

 $$ \varepsilon(h/2,p-1)=\frac{\varepsilon(h,p-1)^{2}}{\varepsilon(2h,p-1)}\quad\varepsilon(h,p+1)=\frac{\varepsilon(h,p)^{2}}{\varepsilon(h,p-1)} $$ 

For the amount of work  $ w(p) $ to treat an interval with order  $ p $, we assume  $ w(p) \sim p $. However, not the absolute work  $ w(p) $ is important, but the effort to obtain the required accuracy. So for our possible decisions (increase  $ p $ by one or bisect the interval setting the order to  $ p - 1 $) we compare the normalized work  $ w(p + 1)\varepsilon(h, p + 1) $ and  $ 2w(p - 1)\varepsilon(h/2, p - 1) $. The alternative with a minimal normalized work will be chosen. In a more general setting, one may try to examine more alternatives, but this would lead too far here.

Finally we have to take care that the error on the complete grid is equilibrated. For that, a cutting value is computed by the maximum of all error predictions and only these intervals are improved whose error is beyond the cutting value. More details for such refinement strategies can be found in refs. $ ^{21,26,28} $

## Galerkin equations and Gauss summation

For a given node-order-pattern a Galerkin matrix  $ \boldsymbol{G} = (g_{jk}) $ has to be constructed which is in principle the product of the operator Jacobian  $ A = f_u(\varphi) $ times the solution  $ u $ expressed in terms of the chosen basis functions  $ t_j(s) $. This is the central point of a Galerkin method and requires numerical summations of the form (special indices of the h-p-method omitted)

 $$ g_{jk}=\sum_{s=1}^{s_{\max}}At_{k}\left(s\right)t_{j}\left(s\right) $$ 

With the matrix  $ \boldsymbol{G} = (g_{jk}) (k, j \text{ counting the basis functions } t_k, t_j \text{ of all intervals of the grid}) \text{ the Galerkin equations for the solution vector } \boldsymbol{a} \text{ of all expansion coefficients read} $

 $$ G a=(\sum_{s=1}^{s_{\max}}b_{s}t_{j}(s))_{j} $$ 

In the h-p-algorithm all such summations are performed by an algorithm of Gaussian type directly induced by the  $ t_{j}(s) $. We replace a sum on an interval I

 $$ S^{I}=\sum_{l}f(s) $$ 

by an approximation

 $$ S_{k}^{I}=\sum_{j=1}^{k+1}\omega_{j}^{I}f\left(s_{j}^{I}\right) $$ 

with nodes  $ s_j' $ and weights  $ w_j' $ chosen, such that  $ S' = S_k' $ if  $ f(s) $ is a polynomial of order  $ 2k + 1 $. It is well known from the theory of Gauss quadrature that here the nodes are just the zeros of the discrete Chebyshev polynomials on interval  $ I $. The nodes and weights can easily be computed for a given  $ k $ by applying the QR-algorithm to a triangular eigenvalue problem, which contains terms of the three-term recurrence formula of the polynomials (see, e.g., ref. $ ^{29} $). The Gauss summation captures exactly the structure of the approach and requires only slight additional computations. It has been shown in ref. $ ^{9} $ that the perturbation introduced by the Gauss summation does not affect the quality of a Galerkin approximation of order  $ n $, whenever at least  $ n + 1 $ Gauss nodes are used (see also ref. $ ^{30} $) for continuous finite elements). This nice feature allows even the treatment of chain-length dependent termination processes (double sums) with relatively few function evaluations.

Finally we want to note that for the entries of the Galerkin matrix, the edges of an interval require additional considerations.

The above explanations show that the PredICI concept is not a simple algorithm. In particular what is sketched above for a single distribution has to be done for a list of distributions in interesting problems. For the treatment of the most reaction steps, two or more different node-order-patterns have to be connected, because each distribution

has its own independent representation. Therefore, the software implementation of PredICI was performed in the object-oriented programming language C++. All components of the reaction system — coefficients, species, distributions, reactors, reaction steps — are organized in classes, which allow the modular extension of the above algorithm to nearly arbitrary reaction systems.

## Some applications of the discrete h-p-method in polyreactions

This section is divided into two parts: first, a problem from radical polymerization will be presented, exemplifying that the new h-p-algorithm is able to handle long-chain branching and chain length dependent reaction rate coefficients. Then some applications of the discrete h-p-method by other authors will briefly be summarized.

## A note on error control

In all simulation runs the global tolerance 0.025 was used. Tests with higher (and lower) accuracy turned out that the results are of the prescribed accuracy, which is in the range of the graphical resolution. Moreover, each single module (= reaction step) in PREDICI has been tested on examples were reference solutions are known. It shows that the required tolerance was obtained in very good concordance — the error control does not only work in a relative error scale. The complete algorithm has been tested over more than two years on very different examples. Additional checks for the specific problems in this article are:

● For the transfer-to-polymer example, there must be the same number of radicals and the same conversion than without the transfer. This has been checked and was fulfilled.

● For all examples an additional mass balance has been performed, which checks the conservation of the first moment of the distributions and the monomer.

## Special considerations in a radical system

We consider an extended reaction scheme (1) for radical polymerization.

 $$ \begin{aligned}I\quad&+M\quad\xrightarrow{k_{s}}\quad P_{1}\\P_{s}\quad&+M\quad\xrightarrow{k_{p}}\quad P_{s+1}\\P_{s}\quad&+P_{r}\quad\xrightarrow{k_{uc}^{sr}}\quad D_{s+r}\\P_{s}\quad&+P_{r}\quad\xrightarrow{k_{td}^{sr}}\quad D_{s}+D_{r}\\P_{s}\quad&+D_{r}\quad\xrightarrow{k_{1}\cdot r}\quad D_{s}+P_{r}\\P_{s}\quad&+M\quad\xrightarrow{k_{\ell}}\quad D_{s}+P_{1}\end{aligned} $$ 

This system contains transfer to monomer, chain-length dependent termination coefficients and long-chain branching (transfer to polymer) now. In contrast to Eq. (2), the differential equations for  $ P_{s} $ and  $ D_{s} $ have to be extended to

 $$ \begin{aligned}\frac{\mathrm{d}P_{1}\left(t\right)}{\mathrm{d}t}&=k_{\mathrm{s}}IM-\left(k_{\mathrm{p}}+k_{\mathrm{f}}\right)MP_{1}-P_{1}\sum_{r}\left(k_{\mathrm{ic}}^{1,r}+k_{\mathrm{id}}^{1,r}\right)P_{r}-k_{1}P_{l}\sum_{r}rD_{r}+\left(k_{1}D_{s}+k_{\mathrm{f}}M\right)\sum_{r}P_{r}\\\frac{\mathrm{d}P_{s}\left(t\right)}{\mathrm{d}t}&=-\left(k_{\mathrm{p}}+k_{\mathrm{f}}\right)MP_{s}+k_{\mathrm{p}}MP_{s-1}-P_{s}\sum_{r}\left(k_{\mathrm{ic}}^{s,r}+k_{\mathrm{id}}^{s,r}\right)P_{r}-k_{1}P_{s}\sum_{r}rD_{r}+k_{1}sD_{s}\sum_{r}P_{r}\\\frac{\mathrm{d}D_{s}\left(t\right)}{\mathrm{d}t}&=k_{\mathrm{f}}MP_{s}+P_{s}\sum_{r}k_{\mathrm{id}}^{s,r}P_{r}+\frac{1}{2}\sum_{r=1}^{1}k_{\mathrm{tc}}^{r,s-r}P_{r}P_{s-r}+\mathbf{k}_{1}P_{s}\sum_{r}rD_{r}-k_{1}sD_{s}\sum_{r}P_{r}\end{aligned} $$ 

The initial concentrations are set to  $ I(0) = 0.01 $ and  $ M(0) = 10 $. The values of the reaction rate coefficients are chosen to reflect a typical and interesting behavior:  $ k_{\mathrm{s}} = 10^{-4} $,  $ k_{\mathrm{p}} = 200 $,  $ k_{\mathrm{f}} = 0.01 $. The combination and the disproportionate coefficients are set to  $ k_{\mathrm{tc}} = (2/3) k_{\mathrm{t}} $ and  $ k_{\mathrm{td}} = (1/3) k_{\mathrm{t}} $ in the following.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>10⁻³, Time/s</th><th style='text-align: center;'>P_n, P_w</th><th style='text-align: center;'>Conversion</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.000000</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.000008</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.000015</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.000022</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.000030</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.000038</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.000045</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.000050</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.000052</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.000053</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.000054</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.000055</td><td style='text-align: center;'>0.000000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 4. Number-average  $ (-\cdot-\cdot) $ and weight-average  $ \left(\cdots\right) $ degrees of polymerization  $ \left(P_{n}, P_{w}\right) $ of dead polymer, and conversion of monomer  $ (\text{—}) $</div>


<div style="text-align: center;">Neglecting any type of gel-effect first, we simulate the system with  $ k_t = 3 \cdot 10^7 $ up to about 52% conversion of monomer ( $ t = 150000 $ s). The resulting molecular weight distribution  $ D_s $ has the dispersity index 2.77 (computed directly from the distribution) and is presented as  $ w(\log M) $-distribution ( $ D_s \cdot s \cdot s $, comparable to gel permeation chromatography) in Fig. 5 (dotted line). Note that more than 50000 size classes had to be resolved. For this model the discrete h-p-method used about 120 degrees of freedom (for both distributions  $ P_s $ and  $ D_s $), a computing time (CPU) of about 10 minutes on a Pentium 90 MHz Computer (32 bit program) was necessary to simulate the complete dynamic process. In order to show how sensitive the algorithm works, the straight line in Fig. 5 shows the result of the same model, but with a slight gel-effect model of the form</div>


 $$ k_{\mathrm{t}}=k_{\mathrm{t,0}}\exp(-X_{\mathrm{M}})\qquad,\quad X_{\mathrm{M}}\mathrm{m o n o m e r c o n v e r s i o n} $$ 

In the next step, we replace the constant termination coefficient  $ k_{t} $ by the function

 $$ k_{\mathrm{t}}^{\mathrm{s},\mathrm{r}}=k_{\mathrm{t}}(s,r)=\frac{k_{\mathrm{t},0}}{(s+r)^{\alpha}}\qquad\quad\alpha=0.4\qquad\quad k_{\mathrm{t},0}=5\cdot10^{8} $$ 

which is chosen such that we obtain nearly the same time-conversion graph as before. Actually, there are many models for  $ k_{t}(s, r) $ in discussion and the h-p-algorithm has

<div style="text-align: center;">Fig. 5. Molecular weight distributions for model (12), without (…) and with slight gel-effect (—)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Degree of polymerization</th><th style='text-align: center;'>W(log M)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.3</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.6</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>2.7</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>2.7</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>2.3</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>2.1</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>1.9</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>1.7</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>1.3</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>1.1</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>0.7</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>0.3</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4200</td></tr>
  </tbody>
</table>

nearly no restrictions on the type of these formulas. Simulating system (12) with the  $ k_{t}(s, r) $ defined above, we obtain a molecular weight distribution, which has much higher dispersity (Fig. 6, see also Tab. 3). It turns out that the effect of chain-length dependent termination coefficients should be kept in mind in advanced models.

Next we consider the effect of the transfer-to-polymer step. We set the transfer rate coefficient to  $ k_1 = 0.5 $, such that a visible effect of the chain transfer can be observed (now the  $ k_t(s, r) $ are constant with  $ k_t = 3 \cdot 10^7 $ again).

<div style="text-align: center;">Fig. 6. Molecular weight distributions for model (12) with chain length dependent  $ k_{t} $ (—) compared to the model with constant termination coefficient ( $ \cdots $)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Degree of polymerization</th><th style='text-align: center;'>W(log M)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.6</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>1.6</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>2.4</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>2.6</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>2.7</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>2.9</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>2.7</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>2.6</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>2.4</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>2.3</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>2.1</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>1.9</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>1.7</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>1.6</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>1.3</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>1.1</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.7</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>0.6</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0.3</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3210</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3220</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3230</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3240</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3250</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3260</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3270</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3280</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3290</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3300</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3310</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3320</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3330</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3340</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3350</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3360</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3370</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3380</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3390</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3410</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3420</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3430</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3440</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3450</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3460</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3470</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3480</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3490</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3510</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3520</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3530</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3540</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3550</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3560</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3570</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3580</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3590</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3610</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3620</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3630</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3640</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3650</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3660</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3670</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3680</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3690</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3700</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3710</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3720</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3730</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3740</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3750</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3760</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3770</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3780</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3790</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3810</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3820</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3830</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3840</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3850</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3860</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3870</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3880</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3890</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3900</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3910</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3920</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3930</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3940</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3950</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3960</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3970</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3980</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3990</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4000</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4010</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4020</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4030</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4040</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4050</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4060</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4070</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4080</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4090</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4100</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4110</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4120</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4130</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4140</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4150</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4160</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4170</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4180</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4190</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4200</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Tab. 3. Comparison of all runs, the last column contains the number of internal variables to approximate both distributions by the h-p-algorithm</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Example</td><td style='text-align: center; word-wrap: break-word;'>$ k(s, r) $</td><td style='text-align: center; word-wrap: break-word;'>$ k_{1} $</td><td style='text-align: center; word-wrap: break-word;'>$ P_{n} $</td><td style='text-align: center; word-wrap: break-word;'>$ P_{w} $</td><td style='text-align: center; word-wrap: break-word;'>$ D = P_{w}/P_{n} $</td><td style='text-align: center; word-wrap: break-word;'>Variables (h-p)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Basic model</td><td style='text-align: center; word-wrap: break-word;'>constant</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>751</td><td style='text-align: center; word-wrap: break-word;'>2080</td><td style='text-align: center; word-wrap: break-word;'>2.77</td><td style='text-align: center; word-wrap: break-word;'>112</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Gel-effect</td><td style='text-align: center; word-wrap: break-word;'>$ k_{1} \cdot (1 - X_{M}) $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>830</td><td style='text-align: center; word-wrap: break-word;'>2400</td><td style='text-align: center; word-wrap: break-word;'>2.89</td><td style='text-align: center; word-wrap: break-word;'>122</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Termination</td><td style='text-align: center; word-wrap: break-word;'>$ k_{1}/(s + r)^{a} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>733</td><td style='text-align: center; word-wrap: break-word;'>3244</td><td style='text-align: center; word-wrap: break-word;'>4.43</td><td style='text-align: center; word-wrap: break-word;'>124</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transfer</td><td style='text-align: center; word-wrap: break-word;'>constant</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>751</td><td style='text-align: center; word-wrap: break-word;'>3188</td><td style='text-align: center; word-wrap: break-word;'>4.25</td><td style='text-align: center; word-wrap: break-word;'>146</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Closing relation</td><td style='text-align: center; word-wrap: break-word;'>constant</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>749</td><td style='text-align: center; word-wrap: break-word;'>3081</td><td style='text-align: center; word-wrap: break-word;'>4.11</td><td style='text-align: center; word-wrap: break-word;'>moments only</td></tr></table>

The number-average chain-length is the same as in the basic model, but there are much more long chains now — the weight mean increases (cf. Fig. 7). This effect is even much more pronounced at high temperatures or under high pressure.

We are also able now to compare a popular moment closing relation to the full distribution simulation. We use the formula of Hulburt and Katz $ ^{35)} $

 $$ \mu_{3}=\frac{\mu_{2}(2\mu_{2}\mu_{0}-\mu_{1}\mu_{1})}{\mu_{1}\mu_{0}} $$ 

and solve the moment equations of the system (12). As can be seen in Tab. 3, the deviations between both results are not large, so in this case the closing relation works. Generally, the h-p-algorithm can be used to check moment closures of any kind without additional assumptions.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Degree of polymerization</th><th style='text-align: center;'>W(log M) (Solid Line)</th><th style='text-align: center;'>W(log M) (Dashed Line)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.6</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.3</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.6</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>1.9</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.3</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 7. Molecular weight distributions for model (12) with transfer to polymer (—) compared to the model with  $ k_{1} = 0 $ ( $ \cdots $)</div>


All distributions are looking simple in the chosen graphical representation, but are quite broad and difficult to approximate. If the distributions were shown with respect to a linear chain length axis and as number or weight distribution  $ (D_s \text{ or } D_s \cdot s) $, only a sharp layer for small degrees of polymerization could be seen.

## Selection of further examples

The above example is only a test model to show how general the discrete h-p-algorithm can work. There are some publications using this algorithm for realistic problems, where also experimental data have been obtained.

## ● Pulsed-laser polymerization

In ref. $ ^{31)} $, Buback et al. describe the simulation of pulsed laser polymerization experiments with up to 2000 (!) laser flashes (time periods). There also the effect of chain-length dependent termination coefficient is studied with the h-p-method.

## • Precipitation polymerization

In a PhD-thesis $ ^{32} $, Fengler studied the precipitation polymerization of acrylic acid with PREDICI. He used a two-phase model describing molecular weight distributions, reaction velocity, number of particles and conversion and could fit the model to experimental data.

## ● Anionic polymerization

In ref. $ ^{33} $), Hungenberg et al. modeled an anionic polymerization of styrene in order to estimate kinetic parameters. The arising molecular weight distributions are partly trimodal.

☑ Polymerization with bifunctional initiator

In ref. $ ^{34} $), Krispin et al. describe the influence of bifunctional initiator on a radical system with gel-effect. In particular they fitted conversion and mean values to experimental data. In Fig. 8, we present a typical molecular weight distribution of their model, which is bimodal — but it turned out that the bimodality was only induced by the gel-effect.

<div style="text-align: center;">Fig. 8. Molecular weight distributions for a model with strong gel-effect</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Degree of polymerization</th><th style='text-align: center;'>W/log M</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.07</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1010</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1020</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1030</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1040</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1050</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1060</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1070</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1080</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1090</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1110</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1120</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1130</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1140</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1150</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1160</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1170</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1180</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1190</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1210</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1220</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1230</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1240</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1250</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1260</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1270</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1280</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1290</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1310</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1320</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1330</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1340</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1350</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1360</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1370</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1380</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1390</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1410</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1420</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1430</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1440</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1450</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1460</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1470</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1480</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1490</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1510</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1520</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1530</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1540</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1550</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1560</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1570</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1580</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1590</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1610</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1620</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1630</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1640</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1650</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1660</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1670</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1680</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1690</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1710</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1720</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1730</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1740</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1750</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1760</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1770</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1780</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1790</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1810</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1820</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1830</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1840</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1850</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1860</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1870</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1880</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1890</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1910</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1920</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1930</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1940</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1950</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1960</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1970</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1980</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1990</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2010</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2020</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2030</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2040</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2050</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2060</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2070</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2080</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2090</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2110</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2120</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2130</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2140</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2150</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2160</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2170</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2180</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2190</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2210</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2220</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2230</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2240</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2260</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2270</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2280</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2290</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2310</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2320</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2330</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2340</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2350</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2360</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2370</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2380</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2390</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2410</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2420</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2430</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2440</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2450</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2460</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2470</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2480</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2490</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2510</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2520</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2530</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2540</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2550</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2560</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2570</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2580</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2590</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2610</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2620</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2630</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2640</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2650</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2660</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2670</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2680</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2690</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2710</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2720</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2730</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2740</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2750</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2760</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2770</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2780</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2790</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2810</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2820</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2830</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2840</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2850</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2860</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2870</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2880</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2890</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2900</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2910</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2920</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2930</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2940</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2950</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2960</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2970</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2980</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2990</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3010</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3020</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3030</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3040</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3050</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3060</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3070</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3080</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3090</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3100</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3110</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3120</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3130</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3140</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3150</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3160</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3170</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3180</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3190</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3210</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3220</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3230</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3240</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3250</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3260</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3270</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3280</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3290</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3300</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3310</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3320</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3330</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3340</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3350</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3360</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3370</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3380</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3390</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3410</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3420</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3430</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3440</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3450</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3460</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3470</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3480</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3490</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3510</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3520</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3530</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3540</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3550</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3560</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3570</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3580</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3590</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3610</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3620</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3630</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3640</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3650</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3660</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3670</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3680</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3690</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3700</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3710</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3720</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3730</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3740</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3750</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3760</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3770</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3780</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3790</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3810</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3820</td></tr>
  </tbody>
</table>

 $ ^{1)} $ M. Frenklach, S. J. Harris, J. Colloid Interface Sci. 118 (1987)

2) A. M. Basedow, K. H. Ebert, H. J. Ederer, Macromolecules 11, 774 (1978)

 $ ^{3)} $ H. P. Breuer, J. Honerkamp, F. Petruccione, Comput. Polym. Sci. 1, 233 (1991)

 $ ^{4} $ J. Lu, H. Zhang, Y. Yang, Makromol. Chem., Theory Simul. 2, 747 (1993)

5) S. Katz, G. M. Seidel, AIChE 13, 319 (1967)

 $ ^{6)} $ H. Gajewski, K. Zacharias, Math. Nachr. 109, 135 (1982)

7) F. D. Magalhaes, M. R. N. Costa, in “Polymer Reaction Engineering”, K.-H. Reichert, W. Geiseler, Eds., VCH, Weinheim 1989

8) P. Deuflhard, M. Wulkow, IMPACT Comput. Sci. Eng. 1, 269 (1989)

 $ ^{9} $ M. Wulkow, IMPACT Comput. Sci. Eng. 4, 153 (1992)

 $ ^{10} $ P. Canu, W. H. Ray, Comput. Chem. Eng. 15, 549 (1991)

 $ ^{11} $ E. Hille, Ann. Math. Pura. Anal. 55, 133 (1961)

 $ ^{12} $ K. Deimling, “Differential Equations in Banach Spaces”, Lecture Notes in Mathematics 596, Springer Verlag, Berlin 1977

 $ ^{13} $ W. H. Ray, J. Macromol. Sci.-Rev. Macromol. Chem. C8, 1 (1972)

 $ ^{14} $ M. Ballauff, B. A. Wolf, Macromolecules 14, 654 (1981)

 $ ^{15} $ D. Ramkrishna, Rev. Chem. Eng. 3, 49 (1985)

 $ ^{16} $ M. Seeßelberg, M. Thorn, Makromol. Theory Simul. 3, 825 (1994)

 $ ^{17} $ O. Wachsen, PhD Thesis, TU Berlin 1995

18) U. Budde, M. Wulkow, Chem. Eng. Sci. 46, 497 (1991)

19) J. Ackermann, M. Wulkow, Konrad-Zuse-Zentrum Berlin, Preprint SC-90-14 (1990)

 $ ^{20} $ F. Bornemann, IMPACT Comput. Sci. Eng. 2, 279 (1990)

 $ ^{21} $ F. Bornemann, IMPACT Comput. Sci. Eng. 3, 93 (1991)

 $ ^{22} $ A. Pazy, “Semigroups of Linear Operators and Applications to Partial Differential Equations”, Springer, Berlin, New York 1983

 $ ^{23} $ P. Deuflhard, SIAM Rev. 27, 505 (1985)

 $ ^{24} $ T. Chebyshev J. Math. Ser. 2, 3 (1878)

25) A. F. Nikiforov, V. B. Uvarov, “Special Functions of Mathematical Physics”, Birkhäuser, Basel 1988

 $ ^{26} $ W. Gui, I. Babushka, Numer. Math. 49 (1991)

27) I. N. Bronstein, K. A. Semendajew, “Taschenbuch der Mathematik”, Verlag Harri Deutsch, Frankfurt/M. 1980

 $ ^{28} $ A. Hohmann, PhD Thesis, FU Berlin 1993

29) P. Deuflhard, A. Hohmann, “Numerical Mathematics I”, W. de Gruyter, Berlin 1995

 $ ^{30} $ P. G. Ciarlet, “The Finite Element Method for Elliptic Problems”, North-Holland, Amsterdam/New York/Oxford 1978

31) M. Buback, M. Busch, R. Lämmel, in "Polymer Reaction Engineering", K.-H. Reichert, H.-U. Moritz, Eds., VCH, Weinheim 1995

 $ ^{32} $ S. Fengler, PhD Thesis, TU Berlin 1995

33) K. D. Hungenberg, K. Knoll, L. Janko, F. Bandermann, in "Polymer Reaction Engineering", K.-H. Reichert, H.-U. Moritz, Eds., VCH, Weinheim 1995

34) I. Krispin, W. Pauer, I. Fresen, H.-U. Moritz, in "Polymer Reaction Engineering", K.-H. Reichert, H.-U. Moritz Eds., VCH, Weinheim 1995

 $ ^{35} $ H. M. Hulburt, S. Katz, Chem. Eng. Sci. 19, 555 (1964)

 $ ^{36} $ K. F. O'Driscoll, M. E. Kuindersma, Macromol. Theory Simul. 3, 469 (1994)

 $ ^{37} $ C. V. Freyer, J. Manz, O. Nuyken, Macromol. Theory Simul. 3, 845 (1994)