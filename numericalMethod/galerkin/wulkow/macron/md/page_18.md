## 3 EXAMPLE: QUASI LIVING RADICAL POLYMERIZATION

During the development of MACRON, the package has been tested on realistic problems :

– the workhorse example ‘Free Radical Polymerization’, which has been treated in [2] with the discrete Galerkin method. As could be seen in that publication, a lot of preparations have been necessary to start with the simulation. Now, the program can be started with the input file shown in Figure 1.

– the formation of soot in flames. This is a difficult task, because a lot of (>300) chemical reactions have to be considered before the macromolecular steps come into play. The combination of both has been tested with MACRON.

– a recent model for biological polymerization. The model has been simulated using the concepts described in [1]. As a result, first principle considerations and model assumptions could be checked.

– a ‘Quasi Living Radical Polymerization’ model published in [9]. Despite very extensive computations on supercomputers and several approximations, up to now the simulation of this model was only possible by a direct integration of a large-scale ODE system. Thereby restrictions on the reaction constants and the reaction times had to be accepted. By MACRON the reaction system can treated very fast on a workstation without these restrictions.

We do not want to feature all examples in detail, since it would be out of the scope of this paper. But we choose the last example to show that an enormous reduction of computing time and an increase of quality can be obtained by MACRON.

Quasi Living Radical Polymerization. We compare an application of MACRON with the results of CH. H. J. JOHNSON et al. in [9].

In [9] a program has been developed to solve directly the complete set of coupled differential equations resulting from an analysis of polymerization kinetics. The program was written to make full use of the speed and power of modern