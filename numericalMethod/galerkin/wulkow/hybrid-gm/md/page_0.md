# A Hybrid Galerkin–Monte-Carlo Approach to Higher-Dimensional Population Balances in Polymerization Kinetics

Christof Schütte,* Michael Wulkow*

Population balance models describing not only the chain-length distribution of a polymer but also additional properties like branching or composition are still difficult to solve numerically. For simulation of such systems two essentially different approaches are discussed in the

Population balance models describing not only the also additional properties like branching or compo For simulation of such systems two essentially literature: deterministic solvers based on rate equations and stochastic Monte-Carlo (MC) strategies based on chemical master equations. The paper presents a novel hybrid approach to polymer reaction kinetics that combines the best of these two worlds. We discuss the theoretical conditions of the algorithm, describe its numerical realization, and show that, if applicable, it is more efficient than full-scale MC approaches and leads to more detailed information in additional property indices than deterministic solvers.

<div style="text-align: center;"><img src="imgs/img_in_image_box_665_584_1101_909.jpg" alt="Image" width="36%" /></div>


## Introduction

The modeling and simulation of polymer reactions still bears various challenges regarding formulation and numerical solution of the underlying population balances. A recent overview is given in ref. $ ^{[1]} $ An issue of special interest of such systems is the treatment of more than one property coordinate, i.e., a description of polymer chains including not only the chain length, but also composition, branching, etc. Even then it is straightforward to derive rate equations, however, these systems will form a higher-dimensional set of countable systems prohibitively complex for more than two or three independent properties. Apart from direct higher-dimensional discretization approaches for such systems, $ ^{[1-3]} $ a special calculus (based on so-called balance distributions or distributed moments) has been developed in the context of the discrete Galerkin h-p-method, $ ^{[4,5]} $ where the additional properties are computed as averages with respect to chain-length. This leads to very detailed and often sufficient information within reasonable computation times, since the original n-dimensional system can be replaced by n one-dimensional countable systems (where a countable system itself is represented by an infinite or very large set of differential equations). A disadvantage of this approach is the fact, that the preparation of such distributed moment systems requires some insight regarding the population balances and a sophisticated use of the discretization method handling the single reaction steps. Regarding the results, sometimes it would be helpful to get information not only on chain-length dependent mean values of additional properties, but full distributions of such, e.g.,

