pubs.acs.org/IECR

# Predici as a Polymer Engineers' Tool for the Synthesis of Polymers via Anionic Polymerization

Felix Kandelhard and Prokopios Georgopanos $ ^{*} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_120_361_161_405.jpg" alt="Image" width="3%" /></div>


Cite This: Ind. Eng. Chem. Res. 2021, 60, 11373–11384

<div style="text-align: center;"><img src="imgs/img_in_image_box_645_362_687_405.jpg" alt="Image" width="3%" /></div>


Read Online

## ACCESS

Metrics & More

<div style="text-align: center;"><img src="imgs/img_in_image_box_564_443_593_467.jpg" alt="Image" width="2%" /></div>


Article Recommendations

<div style="text-align: center;"><img src="imgs/img_in_image_box_880_443_904_467.jpg" alt="Image" width="1%" /></div>


Supporting Information

ABSTRACT: In this study, the potential of a combined reaction kinetics model and a heat transfer model for the process development and scale-up of polystyrene synthesis via anionic polymerization, which is later extended to copolymerization with isoprene, is presented. In an innovative way, the program Predici was utilized to describe the requirements needed in the modeling of polymerization in a larger scale. This model combines the precise description of the polymerization reaction kinetics and the prediction of macromolecular properties offered by the program Predici with a heat transfer model to predict safety-relevant parameters such as the temperature and pressure profiles of the reaction system. In this way, it enables the precise investigation of

<div style="text-align: center;"><img src="imgs/img_in_image_box_650_489_1128_739.jpg" alt="Image" width="38%" /></div>


interactions between process parameters and product properties as well as opens the path to optimal process control. Furthermore, changes associated with the scale-up of the process were studied using the model. The developed model was successfully applied to all of these tasks and could be used for fast screening in the development of polymer synthesis.

## INTRODUCTION

Modeling and simulation are important tools in chemical process development that have gradually gained more importance over the last decades. $ ^{1,2} $ They can assist the development of processes in different areas ranging from product properties to heat and mass transfer behavior, which is influenced by the reactor type and geometry. One of these areas is the kinetics of the chemical reactions, which determines the reaction rates and product selectivity. In some cases, e.g., polymer synthesis, it even has an impact on the physical properties of the products. $ ^{3} $ If the reaction is an exothermic, the kinetics are directly linked to the rate of heat generation, which is one of the most important safety-relevant parameters. $ ^{4} $ As all important polymerizations are exothermic reactions, $ ^{5} $ they are often accompanied by a strong increase in the reaction temperature. This phenomenon is known for many polymerization systems, especially in the case of polymerization of vinyl monomers such as acrylates, $ ^{6} $ dienes, or styrene. $ ^{7} $ The strong temperature increases can result in thermal runaway situations, making the heat generation rate a crucial safety parameter for polymerization processes. $ ^{7} $

Many different programs and tools are used for modeling and simulation in research and industry. This includes specialized solutions developed in programming languages such as Fortran, C++, or Python; open-source applications, e.g., OpenFoam, $ ^{8,9} $ as well as commercial software like COMSOL Multiphysics, $ ^{10} $ Aspen, or Ansys. $ ^{4,11,12} $ One of these commercial simulation tools is the program Predici, which was developed by M. Wulkow and was first introduced in the early 1990s for the modeling of polymerization kinetics. $ ^{13} $ It uses the discrete Galerkin method to calculate the molar weight distributions of polymers $ ^{14} $ and was extended by a hybrid Monte Carlo approach $ ^{15} $ as well as functions for parameter estimation and optimization of process parameters. $ ^{16} $ The program Predici was successfully used in the past to model polymerization reactions ranging from free-radical polymerization performed in bulk, $ ^{17-20} $ solution, $ ^{21} $ suspension, $ ^{22} $ or emulsion; $ ^{23,24} $ controlled-radical polymerizations; $ ^{25-27} $ living anionic; $ ^{28,29} $ and step-growth polymerizations. $ ^{30,31} $ Anionic polymerizations were investigated by further model-based studies for various reactor types and monomers. $ ^{32-38} $



The focus of Predici lies on the modeling of the material balance with the associated chemical reaction kinetics but it also offers the possibility to integrate heat balances. $ ^{16} $ In a recent study, the anionic polymerization of isoprene in cyclohexane carried out in laboratory and industrial scale was modeled with a different approach. $ ^{39} $ It is stated that Predici does not satisfy the requirements to model an industrial scale polymerization process, especially in the estimation of the

<div style="text-align: center;"><img src="imgs/img_in_image_box_1044_1369_1130_1490.jpg" alt="Image" width="6%" /></div>
