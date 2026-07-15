## 2 Using MACRON

The structure of the program package MACRON can be schematically described by the following diagram, which roughly prescribes the organization of this section:

<div style="text-align: center;"><img src="imgs/img_in_image_box_252_400_908_842.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 1: Schematic diagram of MACRON.</div>


In Section 2.1, some hints are given in addition to the syntax description of the input file CHEMIN (see Appendix). CHEMIN contains in particular the chemical reaction system and will be analyzed by the chemical compiler. In case of successful compilation, the user can start the simulation of his model. After a simulation run, the user may modify the chemical input (this is possible without interruption of the program, if a window system is used). Since working with the numerical algorithm requires some experience, in Section 2.2 we try to give an idea of how to proceed with MACRON in view of the approximation of chain length distributions.

Different possibilities are given in order to produce an appropriate output. A choice can be made by the input parameter IPRINT or interactively.

### 2.1 INPUT FILE

In [2], the discrete Galerkin method is applied to the free radical polymerization system shown in the introduction of this paper. A lot of preparations concerning