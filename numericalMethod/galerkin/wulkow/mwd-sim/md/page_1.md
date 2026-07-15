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