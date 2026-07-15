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