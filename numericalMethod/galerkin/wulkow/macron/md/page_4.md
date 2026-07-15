## INTRODUCTION

Macromolecular reaction systems generally involve different types of kinetic steps. The first kind are elemental reactions between chemical species A, B, C, D of the form

 $$ A+B\xrightarrow{k_{p}}C+D\;, $$ 

with a reaction rate coefficient  $ k_{p} $. The simulation of large reaction systems of this kind can be performed by a program package as LARKIN [7]. It is started by the user via a chemical input, which is entered in terms of chemical reactions. Macromolecular reactions are described by certain basic steps. For example the notation

 $$ P_{s}+M\xrightarrow{k_{p}}P_{s+1},s=1,\ldots,s_{\max}, $$ 

models a chain addition of polymer consisting of  $ s_{max} $ elemental reactions. The associated set of differential equations is called a countable (infinite) system of ordinary differential equations (CODE), because each interesting chain length (degree, index) has to be treated separately. The size of  $ s_{max} $ is a priori not known. Thus the computational task is to solve an infinite system in principle. A mixing of the above reaction types arises in many reaction systems of interest. A complete chemical process may contain many reactions and invoke some types of macromolecular species. An example is the following free radical polymerization system (numerically treated in [2]):

 $$ I\quad\xrightarrow{k_{d}}\quad2R $$ 

 $$ R+M\quad\xrightarrow{k_{i}}\quad P_{1} $$ 

 $$ P_{s}+M\xrightarrow{k_{p}}P_{s+1} $$ 

 $$ P_{s}+M\quad\xrightarrow{k_{f}}\quad P_{s+1} $$ 

 $$ P_{s}+S\quad\xrightarrow{\kappa_{f s}}\quad P_{s+1} $$ 

 $$ P_{r}+P_{s}\quad\xrightarrow{k_{t_{c}}}\quad D_{s+r} $$ 

 $$ P_{r}+P_{s}\quad\xrightarrow{\kappa_{t_{d}}}\quad D_{r}+D_{s} $$ 

Generally, the associated differential equations describe the concentration of the species involved in the elemental (standard) reactions and e.g. the chain length distribution (CLD) of the macromolecules. Such systems turn out to be of very high or even infinite dimension, thus an efficient numerical solution by standard ODE software seems hopeless in general (see Section 3).

In the last years the discrete Galerkin method (DEUFLHARD/WULKOW [8]) has been developed as an efficient numerical approach to CODE's. By this method the solution of a CODE is approximated by an error-controlled expansion into orthogonal polynomials of a discrete variable.