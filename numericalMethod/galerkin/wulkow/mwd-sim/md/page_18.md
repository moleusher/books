has its own independent representation. Therefore, the software implementation of PredICI was performed in the object-oriented programming language C++. All components of the reaction system — coefficients, species, distributions, reactors, reaction steps — are organized in classes, which allow the modular extension of the above algorithm to nearly arbitrary reaction systems.

## Some applications of the discrete h-p-method in polyreactions

This section is divided into two parts: first, a problem from radical polymerization will be presented, exemplifying that the new h-p-algorithm is able to handle long-chain branching and chain length dependent reaction rate coefficients. Then some applications of the discrete h-p-method by other authors will briefly be summarized.

## A note on error control

In all simulation runs the global tolerance 0.025 was used. Tests with higher (and lower) accuracy turned out that the results are of the prescribed accuracy, which is in the range of the graphical resolution. Moreover, each single module (= reaction step) in PREDICI has been tested on examples were reference solutions are known. It shows that the required tolerance was obtained in very good concordance — the error control does not only work in a relative error scale. The complete algorithm has been tested over more than two years on very different examples. Additional checks for the specific problems in this article are:

● For the transfer-to-polymer example, there must be the same number of radicals and the same conversion than without the transfer. This has been checked and was fulfilled.

● For all examples an additional mass balance has been performed, which checks the conservation of the first moment of the distributions and the monomer.

## Special considerations in a radical system

We consider an extended reaction scheme (1) for radical polymerization.

 $$ \begin{aligned}I\quad&+M\quad\xrightarrow{k_{s}}\quad P_{1}\\P_{s}\quad&+M\quad\xrightarrow{k_{p}}\quad P_{s+1}\\P_{s}\quad&+P_{r}\quad\xrightarrow{k_{uc}^{sr}}\quad D_{s+r}\\P_{s}\quad&+P_{r}\quad\xrightarrow{k_{td}^{sr}}\quad D_{s}+D_{r}\\P_{s}\quad&+D_{r}\quad\xrightarrow{k_{1}\cdot r}\quad D_{s}+P_{r}\\P_{s}\quad&+M\quad\xrightarrow{k_{\ell}}\quad D_{s}+P_{1}\end{aligned} $$ 

This system contains transfer to monomer, chain-length dependent termination coefficients and long-chain branching (transfer to polymer) now. In contrast to Eq. (2), the differential equations for  $ P_{s} $ and  $ D_{s} $ have to be extended to