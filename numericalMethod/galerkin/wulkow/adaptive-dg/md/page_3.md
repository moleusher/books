## Chapter 2

## Mathematical Polyreaction Models

The efficient numerical simulation of chemical reactions between polymers is certainly a challenging task in the field of chemical engineering. Polyreaction mechanisms include

● chain addition polymerization, e.g. anionic polymerization or free radical polymerization

● reversible polymerization, which is just the above mechanism but now including the reverse direction as well

• polymer degradation

• coagulation or irreversible polycondensation.

In all of these cases the mathematical modelling on the basis of chemical kinetics laws leads to a system of (countably) infinitely many ordinary differential equations — see e.g. [13]. Only in extremely simplified situations such differential systems can be solved analytically in closed form. Moreover, these processes typically do not arise in an isolated form but in a larger context of further reaction rate equations or thermodynamic equations. Therefore the standard situation is that a numerical solution is inevitable. In order to give a vague first impression of the complexity of such problems in a real life setting, we start with a rather recent example.

Example 1: Biopolymerization. This problem arises in the attempt to recycle waste of synthetic materials in an ecologically satisfactory way — which is certainly an important problem of modern industrial societies. An attractive idea in this context would be to look out for a synthetic material, which is both produced and eaten by bacteria — under different environmental conditions, of course. An example of such a biological recycling is the use of the Alcalignes eutrophus H16—bacteria which use fructose as a chemical basis to produce polyester (PHB) — compare [6]. The different chemical macromolecular reaction steps of production and degradation of PHB can be summarized in the following