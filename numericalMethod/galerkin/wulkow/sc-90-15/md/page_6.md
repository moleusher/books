(e.g. characterized by the dispersion coefficient) with a Schulz-Flory distribution. For other types of processes at least the statistical moments and hints about the form of the distribution can be gained (see discussion and examples in [1]). In order to obtain more reliability, the modified weight function  $ \Psi_{\rho,\alpha}(s) $ from Section 3 below can be used for an additional a posteriori error control.

The realization of the above ideas requires an insight into analytical and numerical details of the method, which can not be expected from a user in a field of application. Thus the program package MACRON (MACROmolecular reaction kiNetics) $ ^{[1]} $ has been developed. The package is written in FORTRAN and available for workstations and personal computers. MACRON combines the discrete Galerkin techniques for the simulation of macromolecular reaction with standard software for the treatment of chemical reactions. In particular the chemical compiler from the simulation package LARKIN by DEUFLHARD/NOWAK  $ [4] $, which has originally been written for LARge chemical KINetics, has been extended. The reaction equations, standard kinetics as well as polymerization steps, can be entered by the user in the chemical formalism. The analytical preprocessing required to perform the discrete Galerkin method is done automatically. The numerical standard of the routines build within the package (solution of ordinary differential equations by high sophisticated ODE solvers, pointwise evaluation of the Galerkin approximation by a stable summation algorithm, appropriate scaling and error norms) make the program very efficient. The application of MACRON is in particular recommended, if a repeated computation of a fixed process has to be done.

A part of an input file for MACRON is presented next.

 $$ \begin{array}{ccc} I & \longrightarrow &  \text{R} + \text{R} \end{array} $$ 

 $$ \begin{array}{ccc} I & & \rightarrow \\ \end{array} $$ 

 $$ \begin{array}{ccc} \mathrm{I}+\mathrm{S} & \longrightarrow &  \mathrm{IS} \end{array} $$ 

 $$ \begin{array}{ccc} \mathrm{IS} & & \rightarrow \quad \mathrm{I}+\mathrm{S} \end{array} $$ 

 $$ \mathrm{R}+\mathrm{M}\qquad\qquad\rightarrow\quad\mathrm{P}[1] $$ 

 $$ \mathrm{P}[\mathrm{N}]+\mathrm{M}\qquad\rightarrow\quad\mathrm{P}[\mathrm{N}+1] $$ 

 $$ \mathrm{P}[\mathrm{N}]+\mathrm{M}\qquad\rightarrow\quad\mathrm{D}[\mathrm{N}]+\mathrm{P}[1]\quad(1.8\mathrm{d}-2) $$ 

 $$ \mathrm{P}[\mathrm{N}]+\mathrm{S}\qquad\rightarrow\quad\mathrm{D}[\mathrm{N}]+\mathrm{P}[1]\quad(3.3\mathrm{d}-2) $$ 

 $$ \mathrm{P}[\mathrm{N}]+\mathrm{P}[\mathrm{M}]\quad\rightarrow\quad\mathrm{D}[\mathrm{N}+\mathrm{M}]\qquad(2.4\mathrm{d}7) $$ 

 $$ \mathrm{P}[\mathrm{N}]+\mathrm{P}[\mathrm{M}]\quad\rightarrow\quad\mathrm{D}[\mathrm{N}]+\mathrm{D}[\mathrm{M}]\quad(1.0\mathrm{d}7) $$ 

<div style="text-align: center;">Free radical polymerization system, part of a MACRON input</div>


In this example, P[N] denotes a radical polymer of degree N, D[N] denotes a dead polymer. The actual notation is left to the user and not restricted. For reversible reactions the reverse rate coefficient can be computed via the equilibrium constant, whenever no kinetic parameters are explicitly given and thermodynamic data are available. By choosing an appropriate model parameter, thermodynamic