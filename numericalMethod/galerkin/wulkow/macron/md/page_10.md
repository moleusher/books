the analytical preprocessing and the numerical integration are necessary to use the discrete Galerkin method for such a specific reaction system. But the effort pays off. The efficiency of the method has been impressively demonstrated for this model (and similar ones). MACRON performs all preparations automatically for an arbitrary reaction system and we exemplify the MACRON input file for this well discussed model. This should give only an idea of the usage of MACRON, especially if the user is confused by the detailed informations collected in the Appendix.

The input file shown in Table 1 must have the name CHEMIN and contains in general all information to define a reaction system. It is divided in several input blocks, every input block is opened by a specific keyword and ends when a new input block is opened. Detailed information about every keyword can be found in the Appendix.

Here the first input block is opened by the keyword *HEAD. The following lines will be interpreted as text to identify the reaction system. The block is closed after 3 text lines by the keyword *MODEL PARAMETER opening the next block. The 1 in the first input line of this block determines a model parameter (constant temperature). The following blocks *ELEMENTS and *SPECIES may be omitted, because they contain no further input lines. The unit system 3 is chosen in the next block.

The reaction equations in the block *REACTION SYSTEM are most important. The internal system of differential equations will be constructed according to an analysis of standard and macromolecular kinetics. Macromolecular reactions are characterized by involved macromolecular species (here P[N] and D[N]). This is familiar to every chemist. The chemical compiler works only on the level of chemical equations. The resulting differential equations are not available for the user. This is not as restrictive as it seems to be, actually. The language of chemical reaction kinetics can be used to construct differential equations, which do not result from the analysis of standard kinetics.

For example, in [2] a quasi stationary state approximation (QSSA) for the initiation reaction leads to the contributions

 $$ \begin{array}{r l r}{I^{\prime}=}&{{}-k_{d}I}&{{}+{\ldots}}\end{array} $$ 

 $$ M^{\prime}=~-2f k_{d}I\quad+\ldots $$ 

with the efficiency factor  $ f = 0.3 $ and reaction constant  $ k_{d} = 1.5 \cdot 10^{-5} $. The reaction

 $$ I\quad\Rightarrow $$ 

just produces (2.1), whereas

 $$ \begin{array}{ccc} I & \longrightarrow &  I \quad + \quad M \end{array} $$ 