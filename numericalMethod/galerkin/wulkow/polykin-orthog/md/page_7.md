### 1. Mathematical Polyreaction Models

### 1.1 Kinetic Equations for Selected Mechanisms

Let $P_s(t)$ denote the concentration of polymers of chain length $s$ (also: polymer degree $s$) at time $t$, and $N_s(t)$ the number of polymers of length $s$ at time $t$. For ease of writing, the notation does not distinguish between the chemical species $P_s$ and its concentration $P_s(t)$ — the notation will be clear enough from the context. If a polyreaction mechanism is known in sufficient detail, then the associated system of ordinary differential equations can be generated, in principle. Throughout the paper, attention is focused on simple model problems to illustrate the special features of the new method to be proposed.

Chain addition polymerization. Examples of this mechanism are e.g. anionic polymerization or free radical polymerization. Let M denote a monomer and  $ P_{s} $ the polymer. Then the associated reaction mechanism is:

 $$ P_{s}+M\quad\xrightarrow{k_{p}}\quad P_{s+1}\quad s=1,2,\dots\quad, $$ 

where  $ k_{p}^{~>~0} $ denotes the reaction rate coefficient. The kinetics of the reaction (1.1) is modelled by a system of ordinary differential equations of the form:

 $$ \begin{array}{r c l}{P_{1}^{\prime}}&{=}&{-k_{p}M P_{1}}\\ {P_{s}^{\prime}}&{=}&{-k_{p}M\left(P_{s}-P_{s-1}\right)\quad s=2,3,\dots}\\ {M^{\prime}}&{=}&{-k_{p}M\displaystyle\sum_{s=1}^{\infty}P_{s}}\\ \end{array} $$ 

with the given initial values

 $$ \begin{array}{r c l c l}{P_{1}(0)}&{=}&{P_{10}}\\ {\begin{array}{r c l c l}{P_{s}(0)}&{=}&{0}\\ \end{array},}&{}&{}&{s=2,3,\dots}\\ {M(0)}&{=}&{M_{0}}\\ \end{array} $$ 

Following RAY [18], the time variable t may be rescaled according to

 $$ t\to\underset{\emptyset}{\overset{\cdot}{\int}}k_{p}M(\tau)d\tau\;. $$ 