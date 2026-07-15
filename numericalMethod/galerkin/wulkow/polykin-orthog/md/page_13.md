With this notation, (2.6) is readily seen to be equivalent to

 $$ \sum_{k=0}^{\infty}a_{k}^{2}(t)\gamma_{k}<\infty. $$ 

For given  $ P_{s}(t) $, the coefficients  $ \{a_{j}\} $ can be obtained from the relation

 $$ a_{j}(t)=\frac{1}{\gamma_{j}}\langle l_{j},\;P_{s}(t)\rangle\quad,\quad j=0,1\;\ldots\;. $$ 

This means that the $\{a_j\}$ may be interpreted as generalized moments with respect to the orthogonal basis $\{l_j\}$.

In passing, one may note that mass conservation in the form  $ (1.11') $ can be written as

 $$ \langle1,P_{s}(t)\rangle\;=\;\langle1,P_{s}(0)\rangle\;. $$ 

This directly implies

 $$ \begin{array}{r c l c l}{a_{0}(t)}&{=}&{\displaystyle\frac{1}{\gamma_{0}}\langle l_{0},P_{s}(t)\rangle}&{=}&{\displaystyle\frac{l_{0}}{\gamma_{0}}\langle1,P_{s}(t)\rangle}\\ {}&{=}&{\displaystyle\frac{l_{0}}{\gamma_{0}}\langle1,P_{s}(0)\rangle}&{=}&{a_{0}(0)\;.}\\ \end{array} $$ 

The alternative condition (1.12') in terms of  $ N_{s}(t) $ does not lead to a comparably simple condition, if  $ N_{s}(t) $ has a representation of the form (2.7).

Appropriate treatment of the kinetic equations (Section 1.1) by means of the above formalism leads to a system of ordinary differential equations for the generalized moments — as worked out in Section 4 for the special functions to be derived in Section 3. Truncation of the expansion (2.7) after N terms will lead to a Galerkin approximation of the type

 $$ P_{s}^{(N)}(t):=\Psi(s)\sum_{k=0}^{N}a_{k}(t)l_{k}(s) $$ 

for self-closing systems or of the type

 $$ P_{s}^{(N)}(t):=\Psi(s)\sum_{k=0}^{N}a_{k}^{(N)}(t)\stackrel{}{\boldsymbol{l}_{k}(s)} $$ 

for open systems — see Section 4 for examples of both types.

For the type (2.11), a minimization property is known to hold: let $\Pi_N$ denote the space of polynomials in $s$ of maximum degree $N$ over the grid $\{1, 2, \ldots\}$ and define

 $$ \bar{P}_{s}^{(N)}(t):=\frac{P_{s}^{(N)}(t)}{\Psi(s)}\in\Pi_{N}\;. $$ 