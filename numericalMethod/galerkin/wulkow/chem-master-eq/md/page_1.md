# Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation¶

P. Deuflhard W. Huisinga T. Jahnke M. Wulkow

April 5, 2007

## Abstract

In systems biology, the stochastic description of biochemical reaction kinetics is increasingly being employed to model gene regulatory networks and signalling pathways. Mathematically speaking, such models require the numerical solution of the underlying evolution equation, also known as the chemical master equation (CME). Up to now, the CME has almost exclusively been treated by Monte-Carlo techniques, the most prominent of which is the simulation algorithm suggested by Gillespie in 1976. The paper presents an alternative, which focuses on the discrete partial differential equation (PDE) structure of the CME and thus allows to adopt ideas from adaptive discrete Galerkin methods as first suggested by Deuflhard and Wulkow in 1989 for polyreaction kinetics and independently redetected for the CME by Engblom in 2006. Among the two different options of discretizing the CME as a discrete PDE, Engblom had chosen the method of lines approach (first space, then time), whereas we strongly advise to use the Rothe method (first time, then space) for clear theoretical and algorithmic reasons. Numerical findings at two rather challenging problems illustrate the promising features of the proposed method and, at the same time, indicate lines of necessary further improvement of the method worked out here.

Keywords. adaptive discrete Galerkin methods, adaptive Rothe method, discrete Chebyshev polynomials, stochastic reaction kinetics, chemical master equation