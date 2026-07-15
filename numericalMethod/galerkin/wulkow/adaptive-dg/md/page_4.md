<div style="text-align: center;"><img src="imgs/img_in_image_box_247_162_949_465.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 2.1: Example biopolymerization. Schematic cut through bacteria cells (white areas : polyester granules).</div>


chemical reaction model

 $$ \begin{array}{rcl}&&E\quad\xrightarrow{k_{a}}&A\\A&+&M\quad\xrightarrow{k_{i}}P_{1}\\P_{s}&+&M\quad\xrightarrow{k_{p}}P_{s+1}\\&&P_{s}\quad\xrightarrow{k_{t}}D_{s}\quad+E\\&&D_{s+r}\quad\xrightarrow{k_{d}}D_{s}\quad+D_{r}\\\end{array} $$ 

with $s, r = 1, 2, \ldots$. Herein $M$ denotes the monomer (fructose), $E$ the enzyme, $A$ the activated enzyme, $P_{s}$ the produced or so-called “living” polymer and $D_{s}$ the “dead” PHB-polymer of length $s$. A schematic illustration of the process is given in Fig. 2.1.

In mathematical terms the above process can be represented by the following system of ordinary differential equations

 $$ \begin{array}{rcl}E^{\prime}&=&-k_{a}E+k_{t}\displaystyle\sum_{r=1}^{s_{max}}P_{r}\\A^{\prime}&=&+k_{a}E-k_{i}AM\\M^{\prime}&=&-k_{p}M\displaystyle\sum_{r=1}^{s_{max}}P_{r}-k_{i}AM\\P_{1}^{\prime}&=&-k_{p}MP_{1}+k_{i}AM-k_{t}P_{1}\\P_{s}^{\prime}&=&-k_{p}M(P_{s}-P_{s-1})-k_{d}P_{s}\quad&,&s=2,3,\ldots,s_{max}\\D_{s}^{\prime}&=&+k_{t}P_{s}-k_{d}(s-1)D_{s}+2k_{d}\displaystyle\sum_{r=s+1}^{s_{max}}D_{r}\quad,&s=1,2,\ldots,s_{max}.\end{array} $$ 