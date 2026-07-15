Finally an algorithm is derived, which allows even the treatment of problems without knowledge of analytical properties.

It turns out, that the algorithm works well for a wide class of problems with solutions having structural similarities to the family of weight functions.

In Chapter 1 some general results from the theory concerning CODE's are collected. Some opening considerations introduce operators arising in typical examples and motivate the choice of certain sequence spaces  $ H_{\rho,\alpha} $. These sequence spaces will be the key to the connection between the theory about existence and uniqueness of solutions of CODE's and the numerical approximation of solutions. Asymptotic expansions of Euler discretizations in  $ H_{\rho,\alpha} $ are given next. Chapter 2 contains the construction of the basis functions of  $ H_{\rho,\alpha} $, which are determined by the so-called modified discrete Laguerre polynomials. Important properties of these polynomials are included. Discrete Galerkin methods for projections in  $ H_{\rho,\alpha} $ and approximate solutions of countable systems of algebraic equations (CAE's), both arising from Euler discretizations of CODE's, are described in Chapter 3. The numerical realization of the algorithm is documented in Chapter 4 and Chapter 5 illustrates on numerical results the efficiency of the algorithm developed herein. As an appendix the concept of the multi-level summation algorithm SUMMATOR, which is the heart of the numerical preprocessing suggested in Chapter 3, is explained in Chapter 6.

Acknowledgements. In the first place I want to thank Prof. Dr. P. Deuflhard. He lead me to this subject and supported my research all the time. Many of the ideas and concepts he taught me in the last years have entered in this work. I thank Folkmar Bornemann for numerous discussions, hints, ideas and suggestions concerning the subject and the manuscript. My program could be implemented very fast on the basis of his code KASTIX.

Many thanks to Dr. Jörg Ackermann. The discussions with him gave me a lot of insight, in particular in view of the numerical examples.

Many discussions with and encouragement by Dr. Ralf Kornhuber were very helpful for me.

The interaction of the persons in the several groups of the Konrad-Zuse Zentrum has been very important for this work. In particular I want to mention all members of the numeric group and the symbolic group, without whose version of REDUCE a lot of the results in Chapter 2 could not (or only with difficulties) have been found out.

Last but not least I want to thank Regina Telgmann for all her encouragement, listening and her repeated reading of the manuscript.