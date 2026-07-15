<div style="text-align: center;"><img src="imgs/img_in_image_box_330_279_808_583.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">Figure 5: Time evolution of the weight distribution in a degradation process</div>


a result in [38] ( $ \cdots $), of the new (—) and of the old ( $ \cdots $) version of CODEX [39] shows, that the solution seems to be very reasonable (Figure 4). The computing times are comparable to Table 2. Figure 5 presents the time evolution of the weight distribution  $ s \cdot u_s(t) $ (chosen for ease of representation) of this process, where each line represents one time step.

### 4.3 Soot Formation

In the last example we show, that very general types of reactions can be treated by using the techniques derived in this paper.

Coagulation (combination) processes are described in the chemical notation by

 $$ P_{r}+P_{s}\xrightarrow{k_{r s}}P_{r+s}, $$ 

where  $ P_s $ may denote a polymer molecule or a soot (smog) particle of size  $ s $. This reaction module appears frequently in applications - distinguished by different modelings of the reaction rate coefficients  $ k_{rs} = k_{sr} $. It can also be considered as the reverse process of a degradation (4.3). In polymer chemistry often moment dependent rate coefficients are in use, whereas the modeling of surface effects of the combination of smog particles leads to coefficients dependent on the size of the reacting molecules. The CODE of a coagulation process reads in general