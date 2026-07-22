# 6. Free Radical and Ionic Polymerizations: PS and SBS Rubber

<!-- PDF page 315 -->

## Free Radical and Ionic Polymerizations: PS and SBS Rubber

This chapter covers the modeling of manufacturing processes for polystyrene (PS) using free radical polymerization, and for poly(styrene–butadiene–styrene) rubber, or SBS rubber, using ionic polymerization.

Although some polyolefin textbooks (e.g. [1]) exclude PS from their discussion, we include PS in this book for the following reasons.

According to the classic polymerization book by Odian [2]: “Low- and high-density polyethylene, propylene and polymers of other alkene (olefin) monomers constitute the polyolefin family of polymers.” One could argue for the inclusion of polystyrene based on its useful properties and its huge annual production. Odian states that “Although completely amorphous (glass transition temperature  $ T_{g}=85^{\circ}\mathrm{C} $), its bulky rigid chains (due to phenyl-phenyl interactions) impart good strength with high-dimensional stability (only 1–3% elongation); polystyrene is a typical rigid plastic. About 2 billion pounds of styrene homopolymer are produced annually in the United States.”

Schaller [3] states that “Resonance delocalization in its reactive intermediates makes styrene amenable to almost any method of polymerization, including anionic, cationic, radical, and Ziegler-Natta methods.” Likewise, Lohse [4] writes: “In general, polyolefins are defined as polymers made from olefins, which are principally ethylene and propylene, but also 1-butene, 1-hexene, 1-octene, isobutylene, and other monomers. (By this definition, one could also include polymers made from styrene as polyolefins).”

From a chemistry perspective, styrene polymerization to form polystyrene is always covered as a polyolefin, but in a context that may not be obvious from looking at the table of contents of textbooks. Usually, the context is chain polymerization, olefin polymerization, or specific methods such as radical polymerization [2, 4–7]. In fact, Odian has included styrene polymerization to form polystyrene in a table of chain polymerization by various unsaturated monomers in Table 3-1, p. 200 of his textbook [2].

For an engineering perspective, common polyolefins, such as HDPE, PP, LLDPE, and their copolymers (e.g. poly(ethylene–vinyl acetate [EVA] copolymer), represent approximately 50–55% of commercial polymer production, and step-growth polymers (e.g. polyethylene terephthalate [PET], nylon, and polylactide [PLA]) represent

---

<!-- PDF page 316 -->

approximately 20% of the commercial polymer production [8]. By contrast, PS and its related copolymers, such as styrene-butadiene block copolymer (SBC), represent approximately 10% of commercial polymer production, which is indeed a significant fraction. Secondly, PS is typically made by free radical polymerization in bulk, solution, or suspension processes [2].

Modeling commercial PS processes to match production targets and polymer properties, however, is a challenging task, mostly because of the presence of significant oligomer formation [9–11]. We are not aware of any published studies that demonstrate how to quantitatively incorporate oligomer formation in the modeling of PS.

A significant commercial copolymer of styrene is the poly(styrene-butadiene-styrene) rubber, or SBS rubber, using ionic polymerization. In particular, SBS rubber is the only example of large-volume styrene anionic polymerization with living organolithium initiators. It is similar to the use of metallocene catalysts for polyolefins, which exhibit living polymerization characteristics, and the tacticity element of PS would also relate to the importance of tacticity for PP.

Therefore, this chapter covers both free radical and ionic polymerizations for producing PS and SBS rubber. Section 6.1 presents a hands-on workshop on the simulation of polystyrene with gel effect and oligomer formation. We explain the representation and characterization of components, oligomers, and polymers; the selection of appropriate thermodynamic methods; the estimation of essential property parameters; the kinetics of free radical polymerization, oligomer formation, and copolymerization for PS; and the simulation of commercial stirred autoclave reactors with multiple feed ports and of polymer product separation and monomer recycling. Section 6.2 covers a hands-on workshop on the production of poly(styrene–butadiene–styrene) or SBS rubber by ionic polymerization. We discuss the kinetics of anionic polymerization for SBS rubber and the simulation of batch and semi-batch reactors for anionic copolymerization of styrene and butadiene to produce SBS rubber. We use the simulation software Aspen Polymers for this study. The chapter also presents a reference section.

#### 6.1 Workshop 6.1: Simulation of Polystyrene Reactors with Gel Effect and Oligomer Formation

#### 6.1.1 Objective

This workshop expands the fundamentals and practice of free radical polymerization presented in Chapter 4. In particular, we demonstrate how to deal with gel effect (Section 4.2.6) and oligomer formation in polymerization kinetics.

Aspen Polymers has an example of PS bulk polymerization by thermal initiation [12], which includes the gel effect. However, when applying this model to simulate a commercial PS process, we find that the calculated mass balance and polymer properties do not match the plant data. This follows because the Aspen Polymers PS model has ignored the significant oligomer formation in commercial PS production. An objective of this workshop is to demonstrate the details of simulating oligomer

---

<!-- PDF page 317 -->

formation based on the published reaction information in references [9–11]. We illustrate how to draw the molecular structure of oligomers, how to generate functional groups to characterize the oligomers and estimate their property parameters, and how to define the relevant oligomer-formation reactions. We also demonstrate how to use the data-fit tool to estimate relevant kinetic parameters to match plant data for PS production rate, MWN, and MWW. This detailed illustration of how to include the oligomer formation distinguishes our work from all previous studies of PS simulation in the literature.

#### 6.1.2 Process Flowsheet

Figure 6.1 shows a simplified schematic diagram of the three-reactor system of a commercial process for producing general-purpose polystyrene (GPPS) homopolymer.

In the system, we see two, three, and three reaction zones within the three reactors in series. We use continuous stirred-tank reactor (CSTR) model to represent each reaction zone. Figure 6.2 shows an Aspen Polymers simulation flowsheet for the reactor system, with each CSTR representing a reaction zone within the three reactors in series. We save the simulation file as WS6.1_WithOligomer_BaseCase.bkp. In doing this workshop, please make sure to save the simulation file as soon as we have completed the input for a given folder.

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_687_666_921.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 6.1 A schematic diagram of the three-reactor system of a polystyrene process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_989_787_1201.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.2 A simulation flowsheet of the three-reactor system for producing GPSS homopolymer.</div>


---

<!-- PDF page 318 -->

#### 6.1.3 Unit System, Components, and Characterization of Polymer

We define a unit system METCMPA by copying most units from MET system, except to replace temperature unit by  $ ^{\circ} $C and pressure unit by MPa. See Figure 6.3.

Figures 6.4 and 6.5 show the enterprise databanks and components used in the simulation of the GPPS and other free radical polymerization processes.

STY and STY-SEG are styrene monomer and styrene segment (repeat type). PS is a polystyrene product. INIT is the chain initiator, di-t-butyl-peroxide (DTBP), which is available within the Aspen Polymers initiator database. CINIT is the co-initiator, which is a hypothetical component required to activate the thermal initiation reaction in the model [12]. We use STY to represent CINIT and set its mass flow rate in the feed to be zero. EB (ethyl benzene) and DDM (n-dodecyl mercaptan) are chain-transfer agents. INHIB and RETARDER are inhibitor and retarder, which are presented by STY.

Figure 6.6 shows the definition of STY-SEG, and Figure 6.7 displays polymer attributes in the free radical polymerization and the attribute selection.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_570_814_718.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.3 Defining a unit system METCMPA by copying most units from MET system.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_794_813_953.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.4 Selected databanks used in the simulation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1028_813_1222.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.5 Component specifications.</div>


---

<!-- PDF page 319 -->

#### 6.1 Workshop 6.1: Simulation of Polystyrene Reactors with Gel Effect and Oligomer Formation

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_783_357.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.6 Definition of STY-SEG.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_422_783_639.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.7 Free Radical polymer-attribute selection.</div>


We characterize the oligomers DCB, 1-phenyltetralin (1PT), cyclic trimer (CT), and ZO in the following section.

#### 6.1.4 Characterization of Oligomers

Figure 6.8 illustrates the formation of four oligomers and intermediates identified by references [9–11]. These components are not available in the Aspen Polymers databases. In the following, we demonstrate how to draw the molecular structure, characterize the structure by atoms and by functional groups, and estimate the required property parameters for the simulation. Figures 6.9a–6.9d show the steps to use the drawing tools within Aspen Polymers to draw the 1,2-diphenylcyclobutane (DCB) molecular structure.

We save the molecular structure drawn in Figure 6.9d as a molecular file, DCB.mol, and close the drawing window. (Note: In Section 4.4.3, Figures 4.18, 4.19a, and 4.19b, we demonstrate how to search for the molecular file, *.mol, of our component molecule that is not available within the Aspen Polymers databank but may be available on the Internet. If it is available, we can download the *.mol and import it directly into Aspen Polymers. This will save us time by not going through the steps illustrated in Figures 6.9a–6.9d). Next, we see the “Calculate Bonds” button, as displayed in Figure 6.9e.

After clicking on the “Calculate Bonds” button, Aspen Polymers automatically completes the “General” structure folder, and the “Functional Group” folder. Figure 6.9f shows the general structure.

---

<!-- PDF page 320 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_149_643_722.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 6.8 Formation of oligomers and intermediates in styrene polymerization [9, 10]. We use DCB to represent 1,2-diphenylcyclobutane, 1PT to represent 1-phenyltetralin, ZO (instead of Z in the figure) to represent dimer (intermediate), and CT to represent cyclic trimer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_850_768_1080.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.9a Click on the Draw/Import/Edit button within the DCB molecular structure window to draw the structure.</div>


To understand the atom number and the connectivity in Figure 6.9f, we note that from atom 1 to atom 6, and from atom 7 to atom 12, each connectivity represents a benzene structure. Aspen Polymers specifies a clockwise 360-degree benzene structure, with the upper top carbon atom and lower bottom carbon atom occupying the

---

<!-- PDF page 321 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_155_738_406.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.9b Drawing the DCB structure – Step 1. Click on the benzene ring within Fragments and paste it twice into the drawing plane, and then cancel the benzene ring within Fragments.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_513_739_792.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.9c Drawing the DCB structure – Step 2. Click on the carbon atom "C" within Atoms and paste it four times into the drawing plane, and then cancel the carbon atom.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_877_739_1176.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.9d Drawing the DCB structure – Step 3. Click on the single bond within Bonds and Charges, connect carbon atoms with straight lines six times into the drawing plane, and then cancel the single bond.</div>


---

<!-- PDF page 322 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_150_768_335.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.9e The DCB molecular structure and the "Calculate Bonds" button.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_404_814_632.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.9f The molecular structure automatically defined by Aspen Polymers based on the chemical structure of Figure 6.9d.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_712_815_926.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.9g Search results for "PCES functional groups."</div>


0° and 180° locations, respectively. For two connected benzene rings, the first atom is at 240° location.

Based on the molecular structure displayed in Figure 6.9d, Aspen Polymers also automatically specifies the numbers of UNIFAC and JOBACK functional groups for the structure in order for the PCES (Physical Constant Estimation System) to estimate the required property parameters for the structure. To understand the details of the UNIFAC and JOBACK functional groups, we search for the functional group numbers: Aspen Polymers → Help → Search for “PCES functional groups” → Results: PCES functional groups and UNIFAC functional groups, as seen in Figure 6.9g. Table 3.5 within “PCES functional groups” of Aspen Polymers online help specifies the JOBACK functional group numbers, and Table 3.12 within

---

<!-- PDF page 323 -->

“UNIFAC functional groups” of Aspen Polymers online help specifies the UNIFAC functional group numbers.

We summarize the resulting numbers of UNIFAC and JOBACK functional groups for our four oligomers in Table 6.1. We also show the molecular structures of 1PT (1-phenyltetralin), ZO (dimer), and CT (cyclic trimer) in Figures 6.10a–6.10c. Because of the largest number of UNIFAC functional groups available within the Aspen Polymers databank, two different combinations of UNIFAC group numbers may represent the same molecular structure. For example, Aspen Polymers uses UNIFAC functional group 1050 (C=C) instead of functional groups 1005 (>CH-) and 1100 (>CH2) as in Table 6.1 to represent ZO (dimer). In other words, the correct listing of functional group numbers is not unique. As long as we have drawn the correct molecular structure, we can simply let Aspen Polymers define the functional group combination for a given molecule.

<div style="text-align: center;">Table 6.1 Numbers of UNIFAC and JOBACK functional groups within the molecular structures of oligomers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Functional groups</td><td style='text-align: center; word-wrap: break-word;'>&gt;CH−</td><td style='text-align: center; word-wrap: break-word;'>=C&lt;</td><td style='text-align: center; word-wrap: break-word;'>−CH3</td><td style='text-align: center; word-wrap: break-word;'>&gt;CH2</td><td style='text-align: center; word-wrap: break-word;'>=CH−</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UNIFAC group Number</td><td style='text-align: center; word-wrap: break-word;'>1005</td><td style='text-align: center; word-wrap: break-word;'>1010</td><td style='text-align: center; word-wrap: break-word;'>1015</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>1105</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>JOBACK group Number</td><td style='text-align: center; word-wrap: break-word;'>111</td><td style='text-align: center; word-wrap: break-word;'>114</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>110</td><td style='text-align: center; word-wrap: break-word;'>113</td></tr></table>

<div style="text-align: center;">Number of Functional Groups in the molecular structure</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>DDB</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1PT</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZO</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CT</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>14</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_931_738_1222.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.10a Molecular structure of 1PT (1-phenyltetralin).</div>


---

<!-- PDF page 324 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_768_397.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.10b Molecular structure of ZO (dimer).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_482_769_873.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.10c Molecular structure of CT (cyclic trimer).</div>


#### 6.1.5 Thermodynamic Method and Property Parameters for Components and Oligomers

We choose POLYNRTL thermodynamic method (see Section 2.1 and Table 4.3) for the PS simulation. See Figure 6.11.

Based on references [10, 11], we enter the following pure-component parameters for oligomers: Properties → Methods → Parameters → Pure Components → New → Scalar → Change Name from Pure-1 to Oligomer → Enter values as in Figure 6.12.

Following the same procedure as for Figure 6.12, we enter the pure-component parameters for PS as in Figure 6.13.

Next, we assume a high boiling point for our initiator, INIT. Aspen Polymers databank does not have our initiator, 1,1-(di-tert-butylperoxy) cyclohexane (CAS no. 3006-86-8, molecular weight = 260.37). We approximate INIT with a known

---

<!-- PDF page 325 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_782_346.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.11 Selection of POLYNRTL thermodynamic method for PS simulation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_415_783_564.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.12 Enter pure-component parameters for oligomers: DHVLB (enthalpy of vaporization at boiling point), VB (liquid molar volume at boiling point), RKTZRA (parameter for Rackett liquid molar volume model), VLSTD (standard liquid molar volume at 60°F), and MW (molecular weight).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_687_784_858.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.13 Enter pure-component parameters for PS.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_921_783_1080.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.14 Enter the assumed boiling point and the correct molecular weight of INIT.</div>


initiator, DTBP, but must enter the correct molecular weight of 260.27 for INIT. See Figure 6.14.

To ensure that PS does not vaporize and stays in the liquid phase, we specify the first parameter in the T-dependent liquid vapor pressure correlation PLXANT-1 for PS to a large negative number like -40. This makes the vapor pressure of

---

<!-- PDF page 326 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_813_286.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.15 Enter the first parameter of the liquid vapor pressure correlation for PS to a large negative number of -40 to ensure that PS does not vaporize. Clicking on "Help" will show the detail of the extended Antoine equation for the liquid vapor pressure with parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_404_813_516.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.16 Enter the parameters of the Andrade liquid viscosity correlation for PS [12].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_579_811_813.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.17 Enter the NRTL binary interaction parameters for oligomers.</div>


PS extremely small (4.24 E-23 Bar) [13]. To do so, we follow the path: Properties → Methods → Parameters → Pure Components → New → T-dependent correlation → liquid vapor pressure → PLXANT-1 → Use default name: PLXANT-1 → Enter values as in Figure 6.15.

We enter the parameters for the Andrade liquid viscosity correlation for PS by following the path: Properties → Methods → Parameters → Pure Components → New → T-dependent correlation → liquid viscosity → MULAND-1 → Use default name: MULAND-1 → Enter values [12] as in Figure 6.16.

Next, we enter the NRTL binary interaction parameters for oligomers by using the value for the SEG-STY and STY component pair. See Figure 6.17.

#### 6.1.6 PCES (Physical Constant Estimation System) for Estimating Property Parameters for Oligomers

Based on the molecular structures of oligomers defined in Section 6.1.4, we estimate the missing property parameters using the PCES system. See Figure 6.18.

---

<!-- PDF page 327 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_149_777_309.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.18 Specification of property estimation for selected missing parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_373_778_487.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.19 Specification of estimation of TC (critical temperature) for oligomers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_546_737_688.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.20 Estimation of pure-component property parameters for oligomers.</div>


Figure 6.19 specifies the estimation of scalar parameter TC (critical temperature) for oligomers using the Joback method. We do the same to estimate PC (critical pressure), VC (critical volume), DHFORM (standard enthalpy of formation for ideal gas at 25 °C), DGFORM (standard Gibbs free energy of formation for ideal gas at 25 °C), and TB (normal boiling point). We also estimate scalar parameters Omega (acentric factor) and ZC (critical compressibility factor) by choosing the definition for the parameter, DEFINITI. See Figure 6.20.

We estimate the parameters of temperature-dependent correlations of CPlG (ideal-gas heat capacity; Joback method), PL (liquid vapor pressure; Riedel method), DHVL (enthalpy of vaporization; definition method), MUV (vapor viscosity; Reichenberg method), MUL (liquid viscosity; Orrick-Erbar method), KL (liquid thermal conductivity; Sato-Riedel method), and Sigma (surface tension; Brook-Bird method). See Figure 6.21.

Lastly, we estimate the unknown binary interaction parameters using UNIFAC method. See Figure 6.22.

#### 6.1.7 Defining Free Radical Reactions and Oligomer Reactions

Figure 6.23 shows the molecular structure of INIT or DTBP. The initiator decomposition reaction will break the bond between two oxygen atoms, producing two free radicals.

---

<!-- PDF page 328 -->

<div style="text-align: center;">Figure 6.21 Estimation of temperature-dependent property parameters for oligomers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_150_788_573.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 6.22 Estimation of NRTL binary interaction parameters using UNIFAC method.</div>


Following Table 4.4, we summarize in Table 6.2 the relevant free radical polymerization reactions for our PS simulation. For our process without adding an inhibitor, we can set the pre-exponential factor of the inhibition reaction-rate constant to zero.

To generate these reactions within Aspen Polymers, follow the path: Reactions→New: R-1 FREE-RAD type→OK. See Figures 6.24–6.29. Based on the species defined in Figure 6.25, we click on the “generate reactions” button displayed in Figure 6.26. Aspen

<div style="text-align: center;"><img src="imgs/img_in_image_box_616_634_825_752.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">Figure 6.23 Initiator decomposition breaks the bond between two oxygen atoms to produce two free radicals.</div>


Polymers automatically generates the 10 reactions in Figure 6.26. For our current simulation, we delete reaction 8 (termination by disproportionation) and reaction 10 (inhibition reaction). This results in the reaction shown in Figure 6.27. For the reaction-rate constants in Figure 6.28, we use the pre-exponential factor and activation energy for the reaction-rate constant from Ref. [6] as our initial values. For the initiator decomposition-rate parameters, we can also follow Section 4.4.6 and Figures 4.25a–4.25b to retrieve the same values as in Figure 6.28 from Aspen Polymers initiator database [14]. For reaction calculations, we do not assume the quasi-steady-state approximation; for reaction 2, we specify the dependence of special (thermal) initiation reaction rate (see Section 4.2.2) on the third power of the monomer concentration [9]. We demonstrate both aspects in Figure 6.29.

Next, we consider the gel effect on the free radical polymerization reactions and the resulting polymer molecular weights. Specifically, as the monomer conversion to PS increases, the viscosity of the liquid reaction mixture continues to increase. The termination and other reactions eventually become diffusion limited. This affects the

---

<!-- PDF page 329 -->

<div style="text-align: center;">Table 6.2 Free radical polymerization reactions for the PS workshop.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Representation</td><td style='text-align: center; word-wrap: break-word;'>Notes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Initiator decomposition</td><td style='text-align: center; word-wrap: break-word;'>Initiator  $ \rightarrow $ RadicalsINIT  $ \rightarrow $  $ \varepsilon $ n R $ ^{*} $ + aA + bB(no byproducts A and B for this initiator)</td><td style='text-align: center; word-wrap: break-word;'>$ \varepsilon $ is the decomposition efficiency, typically assumed to be 0.8. Our INIT or DTBP (di-t-butyl peroxide) generates two radicals (n = 2).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Special (thermal) initiation</td><td style='text-align: center; word-wrap: break-word;'>Monomer + Coinitiator  $ \rightarrow $ Growing monomerSTY + CINIT  $ \rightarrow $ P1[STY-SEG]</td><td style='text-align: center; word-wrap: break-word;'>P1[STY-SEG] is a growing polymer chain of length 1 having an active STY segment. Thermal initiation reaction rate is proportional to the monomer concentration to the third power [4].</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Chain initiation</td><td style='text-align: center; word-wrap: break-word;'>Monomer + Radical  $ \rightarrow $ Growing monomerSty + R $ ^{*} $  $ \rightarrow $ P1[Sty]</td><td rowspan="2">Pn[STY] is a growing polymer chain of length n having an active STY segment</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. Chain propagation</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer  $ \rightarrow $ Propagating polymer chainPn[Sty] + Sty  $ \rightarrow $ Pn + 1[Sty]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. Chain transfer to monomer</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer  $ \rightarrow $ Dead chain + Growing monomerPn[Sty] + Sty  $ \rightarrow $ Dn + R $ ^{*} $</td><td style='text-align: center; word-wrap: break-word;'>Dn is a dead polymer chain of length n that does not have an attached radical.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6. Chain transfer to agent</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + transfer agent  $ \rightarrow $ Dead chain + Growing monomerPn[Sty] + A  $ \rightarrow $ Dn + R $ ^{*} $</td><td rowspan="3">A represents the chain-transfer agent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7. Chain termination by combination</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chainPm + growing polymer chain Pn  $ \rightarrow $ Dead polymer chainDm + n Pn[Sty] + Pm[Sty]  $ \rightarrow $ Dn + m</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8. Inhibition reaction</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + inhibition agent  $ \rightarrow $ Dead polymer chainPn[Sty] + X  $ \rightarrow $ Dn</td></tr></table>

---

<!-- PDF page 330 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_160_767_297.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.24 Create free radical polymerization reactions.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_379_813_535.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.25 Specification of species for generating free radical polymerization reactions for PS.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_628_807_930.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.26 Ten free radical reactions generated automatically by Aspen Polymers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1008_813_1208.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.27 Final free radical polymerization reactions for the current PS simulation.</div>


---

<!-- PDF page 331 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_148_781_315.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.28 Initial values of pre-exponential factors and activation energies, together with the number of radicals and initiator decomposition efficiency [9].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_404_782_571.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.29 Specification of no quasi-steady-state assumption and special (thermal) initiation dependency on monomer concentration to the third power (Coeff B = 3).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_658_782_853.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.30 Entering parameter values for gel-effect correlation number 2.</div>


polymerization rate and polymer molecular weight [2]. Aspen Polymers multiplies the reaction-rate constant without gel effect, k, by a correction factor GF to obtain the effective reaction-rate constant  $ k_{eff} $ and presents two correlations for GF as a function of conversion  $ X_{p} $. We use correlation two and input the values of parameters  $ a_{1}-a_{10} $ provided by the Aspen Polymers online help by following the path: Help → Search “Gel effect” → correlation two.

 $$ \begin{aligned}&\text{Correlation Number2:}k_{\mathrm{eff}}=k^{*}GF\quad&\text{GF}=([A/(1-a_{9}X_{\mathrm{p}})]\exp[-(BX_{\mathrm{p}}+CX_{\mathrm{p}}^{2}\\&+DX_{\mathrm{p}}^{3})])^{a}_{10}\end{aligned} $$ 

 $$ \bullet \quad \mathrm{With}\;A=a_{1}+a_{2}T,\;B=a_{3}+a_{4}T,\;C=a_{5}+a_{6}T,\;D=a_{7}+a_{8}T $$ 

Figure 6.30 shows our input of the recommended parameter values of a1−a10 [3, 6].

Finally, we define the oligomer-formation reactions. We specify a power-law type of reactions named oligomer (see Figure 6.31), and then define the first kinetic reaction, 2 STY → DCB, and quantify its kinetics according to reaction information in

---

<!-- PDF page 332 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_145_813_361.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.31 Defining a power-law type of reactions named Oligomer.</div>


<div style="text-align: center;">Table 6.3 Specification of six oligomer reactions [9, 10].</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction number</td><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Reaction rate</td><td style='text-align: center; word-wrap: break-word;'>Pre-exponential factor</td><td style='text-align: center; word-wrap: break-word;'>Activation energy (cal/mol)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2 STY  $ \rightarrow $ DCB</td><td style='text-align: center; word-wrap: break-word;'>$ R_{1} = K_{1} C^{2}_{STY} $</td><td style='text-align: center; word-wrap: break-word;'>1.8E7</td><td style='text-align: center; word-wrap: break-word;'>28,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1 DCB  $ \rightarrow $ 2 STY</td><td style='text-align: center; word-wrap: break-word;'>$ R_{2} = K_{2} C_{DCB} $</td><td style='text-align: center; word-wrap: break-word;'>1E10</td><td style='text-align: center; word-wrap: break-word;'>28,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>2 STY  $ \rightarrow $ 1 ZO</td><td style='text-align: center; word-wrap: break-word;'>$ R_{3} = K_{3} C^{2}_{STY} $</td><td style='text-align: center; word-wrap: break-word;'>3,909</td><td style='text-align: center; word-wrap: break-word;'>20,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1 ZO  $ \rightarrow $ 2 STY</td><td style='text-align: center; word-wrap: break-word;'>$ R_{4} = K_{4} C_{ZO} $</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1 ZO + STY  $ \rightarrow $ CT</td><td style='text-align: center; word-wrap: break-word;'>$ R_{5} = K_{5} C_{ZO} C_{STY} $</td><td style='text-align: center; word-wrap: break-word;'>1E7</td><td style='text-align: center; word-wrap: break-word;'>20,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>1 ZO  $ \rightarrow $ 1 IPT</td><td style='text-align: center; word-wrap: break-word;'>$ R_{6} = K_{6} C_{ZO} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>20,000</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_752_813_958.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.32 Stoichiometry of oligomer reaction no. 1.</div>


Table 6.3. See Figures 6.32–6.34. The pre-exponential factor for oligomer reaction number 6 is assumed to be zero, indicating that we ignore this reaction.

#### 6.1.8 Specification of Inlet Process Streams and Unit Operation and Reactor Blocks

Table 6.4 shows the inlet stream specifications. Table 6.5 gives the specifications for unit operation and reactor blocks. For each reactor, we need to activate the relevant reactions. See Figure 6.35. Additionally, for reactor simulation, we do not assume quasi-steady-state approximation (see Figure 6.29) and use Broyden method.

---

<!-- PDF page 333 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_166_783_368.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.33 Kinetics of oligomer reaction no. 1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_454_783_587.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.34 Stoichiometry of six oligomer reactions.</div>


<div style="text-align: center;">Table 6.4 Specifications of inlet process streams.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Input specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T2</td><td style='text-align: center; word-wrap: break-word;'>12°C, 2.033 MPa, mass flow (kg/hr): STY = 5915, EB = 144.306</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R2</td><td style='text-align: center; word-wrap: break-word;'>12°C, 2.033 MPa, mass flow (kg/hr): STY = 615, DCB = 1, EB = 2, DDM = 2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2</td><td style='text-align: center; word-wrap: break-word;'>12°C, 7.033 MPa, mass flow (kg/hr): INIT = 1, CINIT = 1, EB = 2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A6</td><td style='text-align: center; word-wrap: break-word;'>12°C, 5.033 MPa, mass flow (kg/hr): STY = 55, EB = 2</td></tr></table>

<div style="text-align: center;">Table 6.5 Specifications of unit operation and reactor blocks.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>R1A</td><td style='text-align: center; word-wrap: break-word;'>R1B</td><td style='text-align: center; word-wrap: break-word;'>R2A</td><td style='text-align: center; word-wrap: break-word;'>R2B</td><td style='text-align: center; word-wrap: break-word;'>R2C</td><td style='text-align: center; word-wrap: break-word;'>R3A</td><td style='text-align: center; word-wrap: break-word;'>R3B</td><td style='text-align: center; word-wrap: break-word;'>R3C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Volume ( $ m^{3} $)</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'>5.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature ( $ ^\circ $C)</td><td style='text-align: center; word-wrap: break-word;'>112</td><td style='text-align: center; word-wrap: break-word;'>113</td><td style='text-align: center; word-wrap: break-word;'>115</td><td style='text-align: center; word-wrap: break-word;'>118</td><td style='text-align: center; word-wrap: break-word;'>123</td><td style='text-align: center; word-wrap: break-word;'>135</td><td style='text-align: center; word-wrap: break-word;'>152</td><td style='text-align: center; word-wrap: break-word;'>160</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (MPa)</td><td style='text-align: center; word-wrap: break-word;'>5.233</td><td style='text-align: center; word-wrap: break-word;'>5.233</td><td style='text-align: center; word-wrap: break-word;'>4.833</td><td style='text-align: center; word-wrap: break-word;'>4.833</td><td style='text-align: center; word-wrap: break-word;'>4.833</td><td style='text-align: center; word-wrap: break-word;'>3.833</td><td style='text-align: center; word-wrap: break-word;'>3.833</td><td style='text-align: center; word-wrap: break-word;'>3.833</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Phase</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reacting phase</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>L</td></tr></table>

Other blocks: (1) E1: 90°C, 0 MPa (no pressure drop); (2) P1: exit pressure, 5.233 MPa; (3) V1: 4.533 MPa, 0 MPa; and (4) V2: 3.833 MPa, 0 MPa.

---

<!-- PDF page 334 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_813_264.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.35 Specification of reactions for each reactor.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_327_812_490.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.36 Specification of reactor convergence method and initiation by integration.</div>


for convergence calculation with 500 iterations and initialize the calculation by integration (see Figure 6.36).

#### 6.1.9 Kinetic Parameter Estimation and Model Validation

Table 6.6 lists the major kinetic parameters and independent variables affecting the simulation targets for free radical polymerization for our kinetic parameter estimation below.

Table 6.6 results from the following kinetic relationship for degree of polymerization (DPN) for free radical polymerization [2]:

 $$ 1/\mathrm{MWN}\propto1/\mathrm{DPN}=k_{\mathrm{tr,m}}/k_{\mathrm{p}}+\left(k_{\mathrm{tr,A}}^{*}{C_{\mathrm{A}}}\right)/\left(k_{\mathrm{p}}^{*}C_{\mathrm{m}}\right) $$ 

where the subscripts p, tr, m, and tr,A represent propagation, chain transfer to monomer, and chain transfer to chain-transfer agent, respectively;  $ C_{A} $ and  $ C_{m} $ represent the concentrations of chain-transfer agent and monomer, respectively. This relationship suggests that as  $ k_{p} $ increases and as  $ k_{tr,m} $ and  $ k_{tr,A} $ decrease, MWN and MWW increase. We find this guidance to be sufficient for the kinetic parameter estimation for the current PS simulation using the data fit tool. Previously, in Section 4.4.8, Figure 4.26, we presented an expanded list of major affecting

<div style="text-align: center;">Table 6.6 Major kinetic parameters and independent variables affecting simulation targets of free radical polymerization of PS.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Simulation target</td><td style='text-align: center; word-wrap: break-word;'>Major affecting kinetic parameters and independent variables</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Production rate or monomer conversion</td><td style='text-align: center; word-wrap: break-word;'>Propagation-rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. MWN, MWW</td><td style='text-align: center; word-wrap: break-word;'>Rate constants for chain transfer to monomer and to chain-transfer agent; mass flow rate of chain-transfer agent</td></tr></table>

---

<!-- PDF page 335 -->

parameters for free radical polymerization of high-pressure LDPE, considering a different set of reactions involved.

We define three datasets for our simulation targets. Figures 6.37 and 6.38 show how to define two datasets (point data), namely, PS production rate (dataset DS-1) and PS MWN (dataset DS-2). Following Figure 6.38, we define the dataset DS-3 for PS MWW by choosing the attribute MWW. We then define data regression run DR-1 for dataset DS-1 and data regression run DR-2 for datasets DS-2 and DS-3 together. See Figures 6.39 and 6.40.

We increase the number of iterations and flowsheet passes for both regression runs, DR-1 and DR-2. See Figure 6.41.

Table 6.7 lists the computed manipulated variables and fitted data from regression runs. Figure 6.42 shows the final kinetic parameters for the base case.

This concludes our base-case model development, and we save the simulation as WS6.1_With Oligomers_BaseCase.bkp.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_523_784_667.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.37 Defining the dataset DS-1 for PS production rate.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_739_782_932.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.38 Defining the dataset DS-2 for PS MWN.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_1002_783_1221.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.39 Defining data regression DR-1 for PS production rate.</div>


---

<!-- PDF page 336 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_149_808_494.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.40 Defining data regression DR-2 for PS MWN (dataset DS-2) and MWW (dataset DS-3).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_602_812_925.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.41 Increasing the number of iterations and flowsheet passes in data regression runs.</div>


#### 6.1.10 Model Applications

A PS simulation model validated by plant data can have many useful applications. The model will be useful for the capacity expansion of the current plant. We can use the validated model to study the effects of changes in key independent variables on production targets.

As an example, we study the effects of varying the mass flow rate of chain-transfer agent EB in feed stream S1 from 105 to 420 kg/hr, with an increment of 105 kg/hr, on the PS mass flow rate, and MWN and MWW of product stream P4 exiting reactor V3C. See Figures 6.43–6.45.

---

<!-- PDF page 337 -->

<div style="text-align: center;">Table 6.7 Comparison of simulation targets (datasets) with model results.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>PS production rate, kg/hr (DS-1)</td><td style='text-align: center; word-wrap: break-word;'>PS MWN (DS-2)</td><td style='text-align: center; word-wrap: break-word;'>PS MWW (DS-3)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Simulation target</td><td style='text-align: center; word-wrap: break-word;'>5950</td><td style='text-align: center; word-wrap: break-word;'>89,000</td><td style='text-align: center; word-wrap: break-word;'>256,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Model result</td><td style='text-align: center; word-wrap: break-word;'>5926</td><td style='text-align: center; word-wrap: break-word;'>92,645</td><td style='text-align: center; word-wrap: break-word;'>250,635</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Error</td><td style='text-align: center; word-wrap: break-word;'>0.4%</td><td style='text-align: center; word-wrap: break-word;'>4.1%</td><td style='text-align: center; word-wrap: break-word;'>2.1%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. Key manipulated variables</td><td style='text-align: center; word-wrap: break-word;'>Pre-exponential factor for propagation reaction-rate constant</td><td colspan="2">Pre-exponential factors for rate constant for chain transfer to: (1) monomer STY, (2) to chain-transfer agent EB, and (3) to chain-transfer agent DDM. (4) Mass flow rate of chain-transfer agent EB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. Variable range</td><td style='text-align: center; word-wrap: break-word;'>5E8 to 5E10 1/hr</td><td colspan="2">2E5 to 5E8 1/hr; (2) 5E6 to 5E8 1/hr; (3) 5E5 to 5E8 1/hr; (4) 1 to 250 kg/hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6. Data-regression result</td><td style='text-align: center; word-wrap: break-word;'>1.3411E9 1/hr</td><td colspan="2">(1) 2E5 1/hr; (2) 2.33272E7 1/hr; (3) 5E5 1/hr; (4) 143.376 kg/hr</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_603_781_827.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.42 Kinetic parameter values of base-case model.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_882_780_1215.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.43 Defining the independent variable ("Vary") of sensitivity study S-1.</div>


---

<!-- PDF page 338 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_812_574.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.44 Defining the dependent variables ("Define") of sensitivity study S-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_668_743_939.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 6.45 Defining the dependent variables to be tabulated in sensitivity study S-1.</div>


We see from Figures 6.46 and 6.47 that the mass flow rate of chain-transfer agent EB has only a minor effect on the mass flow rate and PDI of PS in the product polymer, stream P4, but it has a significant effect on the resulting MWN and MWW. We save the simulation file as WS6.1_With Oligomers_Good PS Production_MWN and MWN (Final). bkp

As another example, we investigate the interactive effect of varying the INIT mass flow within feed stream C2 from 1 to 4kg/hr and varying the mass flow rate of

---

<!-- PDF page 339 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>S-1</th><th style='text-align: center;'>130000</th><th style='text-align: center;'>130000</th><th style='text-align: center;'>130000</th><th style='text-align: center;'>130000</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.46 Effect of mass flow rate of chain-transfer agent EB on the MWN and MWW of product polymer, stream P4.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>WAV 1.52</th><th style='text-align: center;'>WAV 1.520</th><th style='text-align: center;'>WAV 1.525</th><th style='text-align: center;'>WAV 1.530</th><th style='text-align: center;'>WAV 1.535</th><th style='text-align: center;'>WAV 1.540</th><th style='text-align: center;'>WAV 1.545</th><th style='text-align: center;'>WAV 1.550</th><th style='text-align: center;'>WAV 1.555</th><th style='text-align: center;'>WAV 1.560</th><th style='text-align: center;'>WAV 1.565</th><th style='text-align: center;'>WAV 1.570</th><th style='text-align: center;'>WAV 1.575</th><th style='text-align: center;'>WAV 1.580</th><th style='text-align: center;'>WAV 1.585</th><th style='text-align: center;'>WAV 1.590</th><th style='text-align: center;'>WAV 1.595</th><th style='text-align: center;'>WAV 1.600</th><th style='text-align: center;'>WAV 1.605</th><th style='text-align: center;'>WAV 1.610</th><th style='text-align: center;'>WAV 1.615</th><th style='text-align: center;'>WAV 1.620</th><th style='text-align: center;'>WAV 1.625</th><th style='text-align: center;'>WAV 1.630</th><th style='text-align: center;'>WAV 1.635</th><th style='text-align: center;'>WAV 1.640</th><th style='text-align: center;'>WAV 1.645</th><th style='text-align: center;'>WAV 1.650</th><th style='text-align: center;'>WAV 1.655</th><th style='text-align: center;'>WAV 1.660</th><th style='text-align: center;'>WAV 1.665</th><th style='text-align: center;'>WAV 1.670</th><th style='text-align: center;'>WAV 1.675</th><th style='text-align: center;'>WAV 1.680</th><th style='text-align: center;'>WAV 1.685</th><th style='text-align: center;'>WAV 1.690</th><th style='text-align: center;'>WAV 1.695</th><th style='text-align: center;'>WAV 1.700</th><th style='text-align: center;'>WAV 1.705</th><th style='text-align: center;'>WAV 1.710</th><th style='text-align: center;'>WAV 1.715</th><th style='text-align: center;'>WAV 1.720</th><th style='text-align: center;'>WAV 1.725</th><th style='text-align: center;'>WAV 1.730</th><th style='text-align: center;'>WAV 1.735</th><th style='text-align: center;'>WAV 1.740</th><th style='text-align: center;'>WAV 1.745</th><th style='text-align: center;'>WAV 1.750</th><th style='text-align: center;'>WAV 1.755</th><th style='text-align: center;'>WAV 1.760</th><th style='text-align: center;'>WAV 1.765</th><th style='text-align: center;'>WAV 1.770</th><th style='text-align: center;'>WAV 1.775</th><th style='text-align: center;'>WAV 1.780</th><th style='text-align: center;'>WAV 1.785</th><th style='text-align: center;'>WAV 1.790</th><th style='text-align: center;'>WAV 1.795</th><th style='text-align: center;'>WAV 1.800</th><th style='text-align: center;'>WAV 1.805</th><th style='text-align: center;'>WAV 1.810</th><th style='text-align: center;'>WAV 1.815</th><th style='text-align: center;'>WAV 1.820</th><th style='text-align: center;'>WAV 1.825</th><th style='text-align: center;'>WAV 1.830</th><th style='text-align: center;'>WAV 1.835</th><th style='text-align: center;'>WAV 1.840</th><th style='text-align: center;'>WAV 1.845</th><th style='text-align: center;'>WAV 1.850</th><th style='text-align: center;'>WAV 1.855</th><th style='text-align: center;'>WAV 1.860</th><th style='text-align: center;'>WAV 1.865</th><th style='text-align: center;'>WAV 1.870</th><th style='text-align: center;'>WAV 1.875</th><th style='text-align: center;'>WAV 1.880</th><th style='text-align: center;'>WAV 1.885</th><th style='text-align: center;'>WAV 1.890</th><th style='text-align: center;'>WAV 1.895</th><th style='text-align: center;'>WAV 1.900</th><th style='text-align: center;'>WAV 1.905</th><th style='text-align: center;'>WAV 1.910</th><th style='text-align: center;'>WAV 1.915</th><th style='text-align: center;'>WAV 1.920</th><th style='text-align: center;'>WAV 1.925</th><th style='text-align: center;'>WAV 1.930</th><th style='text-align: center;'>WAV 1.935</th><th style='text-align: center;'>WAV 1.940</th><th style='text-align: center;'>WAV 1.945</th><th style='text-align: center;'>WAV 1.950</th><th style='text-align: center;'>WAV 1.955</th><th style='text-align: center;'>WAV 1.960</th><th style='text-align: center;'>WAV 1.965</th><th style='text-align: center;'>WAV 1.970</th><th style='text-align: center;'>WAV 1.975</th><th style='text-align: center;'>WAV 1.980</th><th style='text-align: center;'>WAV 1.985</th><th style='text-align: center;'>WAV 1.990</th><th style='text-align: center;'>WAV 1.995</th><th style='text-align: center;'>WAV 2.000</th><th style='text-align: center;'>WAV 2.005</th><th style='text-align: center;'>WAV 2.010</th><th style='text-align: center;'>WAV 2.015</th><th style='text-align: center;'>WAV 2.020</th><th style='text-align: center;'>WAV 2.025</th><th style='text-align: center;'>WAV 2.030</th><th style='text-align: center;'>WAV 2.035</th><th style='text-align: center;'>WAV 2.040</th><th style='text-align: center;'>WAV 2.045</th><th style='text-align: center;'>WAV 2.050</th><th style='text-align: center;'>WAV 2.055</th><th style='text-align: center;'>WAV 2.060</th><th style='text-align: center;'>WAV 2.065</th><th style='text-align: center;'>WAV 2.070</th><th style='text-align: center;'>WAV 2.075</th><th style='text-align: center;'>WAV 2.080</th><th style='text-align: center;'>WAV 2.085</th><th style='text-align: center;'>WAV 2.090</th><th style='text-align: center;'>WAV 2.095</th><th style='text-align: center;'>WAV 2.100</th><th style='text-align: center;'>WAV 2.105</th><th style='text-align: center;'>WAV 2.110</th><th style='text-align: center;'>WAV 2.115</th><th style='text-align: center;'>WAV 2.120</th><th style='text-align: center;'>WAV 2.125</th><th style='text-align: center;'>WAV 2.130</th><th style='text-align: center;'>WAV 2.135</th><th style='text-align: center;'>WAV 2.140</th><th style='text-align: center;'>WAV 2.145</th><th style='text-align: center;'>WAV 2.150</th><th style='text-align: center;'>WAV 2.155</th><th style='text-align: center;'>WAV 2.160</th><th style='text-align: center;'>WAV 2.165</th><th style='text-align: center;'>WAV 2.170</th><th style='text-align: center;'>WAV 2.175</th><th style='text-align: center;'>WAV 2.180</th><th style='text-align: center;'>WAV 2.185</th><th style='text-align: center;'>WAV 2.190</th><th style='text-align: center;'>WAV 2.195</th><th style='text-align: center;'>WAV 2.200</th><th style='text-align: center;'>WAV 2.205</th><th style='text-align: center;'>WAV 2.210</th><th style='text-align: center;'>WAV 2.215</th><th style='text-align: center;'>WAV 2.220</th><th style='text-align: center;'>WAV 2.225</th><th style='text-align: center;'>WAV 2.230</th><th style='text-align: center;'>WAV 2.235</th><th style='text-align: center;'>WAV 2.240</th><th style='text-align: center;'>WAV 2.245</th><th style='text-align: center;'>WAV 2.250</th><th style='text-align: center;'>WAV 2.255</th><th style='text-align: center;'>WAV 2.260</th><th style='text-align: center;'>WAV 2.265</th><th style='text-align: center;'>WAV 2.270</th><th style='text-align: center;'>WAV 2.275</th><th style='text-align: center;'>WAV 2.280</th><th style='text-align: center;'>WAV 2.285</th><th style='text-align: center;'>WAV 2.290</th><th style='text-align: center;'>WAV 2.295</th><th style='text-align: center;'>WAV 2.300</th><th style='text-align: center;'>WAV 2.305</th><th style='text-align: center;'>WAV 2.310</th><th style='text-align: center;'>WAV 2.315</th><th style='text-align: center;'>WAV 2.320</th><th style='text-align: center;'>WAV 2.325</th><th style='text-align: center;'>WAV 2.330</th><th style='text-align: center;'>WAV 2.335</th><th style='text-align: center;'>WAV 2.340</th><th style='text-align: center;'>WAV 2.345</th><th style='text-align: center;'>WAV 2.350</th><th style='text-align: center;'>WAV 2.355</th><th style='text-align: center;'>WAV 2.360</th><th style='text-align: center;'>WAV 2.365</th><th style='text-align: center;'>WAV 2.370</th><th style='text-align: center;'>WAV 2.375</th><th style='text-align: center;'>WAV 2.380</th><th style='text-align: center;'>WAV 2.385</th><th style='text-align: center;'>WAV 2.390</th><th style='text-align: center;'>WAV 2.395</th><th style='text-align: center;'>WAV 2.400</th><th style='text-align: center;'>WAV 2.405</th><th style='text-align: center;'>WAV 2.410</th><th style='text-align: center;'>WAV 2.415</th><th style='text-align: center;'>WAV 2.420</th><th style='text-align: center;'>WAV 2.425</th><th style='text-align: center;'>WAV 2.430</th><th style='text-align: center;'>WAV 2.435</th><th style='text-align: center;'>WAV 2.440</th><th style='text-align: center;'>WAV 2.445</th><th style='text-align: center;'>WAV 2.450</th><th style='text-align: center;'>WAV 2.455</th><th style='text-align: center;'>WAV 2.460</th><th style='text-align: center;'>WAV 2.465</th><th style='text-align: center;'>WAV 2.470</th><th style='text-align: center;'>WAV 2.475</th><th style='text-align: center;'>WAV 2.480</th><th style='text-align: center;'>WAV 2.485</th><th style='text-align: center;'>WAV 2.490</th><th style='text-align: center;'>WAV 2.495</th><th style='text-align: center;'>WAV 2.500</th><th style='text-align: center;'>WAV 2.505</th><th style='text-align: center;'>WAV 2.510</th><th style='text-align: center;'>WAV 2.515</th><th style='text-align: center;'>WAV 2.520</th><th style='text-align: center;'>WAV 2.525</th><th style='text-align: center;'>WAV 2.530</th><th style='text-align: center;'>WAV 2.535</th><th style='text-align: center;'>WAV 2.540</th><th style='text-align: center;'>WAV 2.545</th><th style='text-align: center;'>WAV 2.550</th><th style='text-align: center;'>WAV 2.555</th><th style='text-align: center;'>WAV 2.560</th><th style='text-align: center;'>WAV 2.565</th><th style='text-align: center;'>WAV 2.570</th><th style='text-align: center;'>WAV 2.575</th><th style='text-align: center;'>WAV 2.580</th><th style='text-align: center;'>WAV 2.585</th><th style='text-align: center;'>WAV 2.590</th><th style='text-align: center;'>WAV 2.595</th><th style='text-align: center;'>WAV 2.600</th><th style='text-align: center;'>WAV 2.605</th><th style='text-align: center;'>WAV 2.610</th><th style='text-align: center;'>WAV 2.615</th><th style='text-align: center;'>WAV 2.620</th><th style='text-align: center;'>WAV 2.625</th><th style='text-align: center;'>WAV 2.630</th><th style='text-align: center;'>WAV 2.635</th><th style='text-align: center;'>WAV 2.640</th><th style='text-align: center;'>WAV 2.645</th><th style='text-align: center;'>WAV 2.650</th><th style='text-align: center;'>WAV 2.655</th><th style='text-align: center;'>WAV 2.660</th><th style='text-align: center;'>WAV 2.665</th><th style='text-align: center;'>WAV 2.670</th><th style='text-align: center;'>WAV 2.675</th><th style='text-align: center;'>WAV 2.680</th><th style='text-align: center;'>WAV 2.685</th><th style='text-align: center;'>WAV 2.690</th><th style='text-align: center;'>WAV 2.695</th><th style='text-align: center;'>WAV 2.700</th><th style='text-align: center;'>WAV 2.705</th><th style='text-align: center;'>WAV 2.710</th><th style='text-align: center;'>WAV 2.715</th><th style='text-align: center;'>WAV 2.720</th><th style='text-align: center;'>WAV 2.725</th><th style='text-align: center;'>WAV 2.730</th><th style='text-align: center;'>WAV 2.735</th><th style='text-align: center;'>WAV 2.740</th><th style='text-align: center;'>WAV 2.745</th><th style='text-align: center;'>WAV 2.750</th><th style='text-align: center;'>WAV 2.755</th><th style='text-align: center;'>WAV 2.760</th><th style='text-align: center;'>WAV 2.765</th><th style='text-align: center;'>WAV 2.770</th><th style='text-align: center;'>WAV 2.775</th><th style='text-align: center;'>WAV 2.780</th><th style='text-align: center;'>WAV 2.785</th><th style='text-align: center;'>WAV 2.790</th><th style='text-align: center;'>WAV 2.795</th><th style='text-align: center;'>WAV 2.800</th><th style='text-align: center;'>WAV 2.805</th><th style='text-align: center;'>WAV 2.810</th><th style='text-align: center;'>WAV 2.815</th><th style='text-align: center;'>WAV 2.820</th><th style='text-align: center;'>WAV 2.825</th><th style='text-align: center;'>WAV 2.830</th><th style='text-align: center;'>WAV 2.835</th><th style='text-align: center;'>WAV 2.840</th><th style='text-align: center;'>WAV 2.845</th><th style='text-align: center;'>WAV 2.850</th><th style='text-align: center;'>WAV 2.855</th><th style='text-align: center;'>WAV 2.860</th><th style='text-align: center;'>WAV 2.865</th><th style='text-align: center;'>WAV 2.870</th><th style='text-align: center;'>WAV 2.875</th><th style='text-align: center;'>WAV 2.880</th><th style='text-align: center;'>WAV 2.885</th><th style='text-align: center;'>WAV 2.890</th><th style='text-align: center;'>WAV 2.895</th><th style='text-align: center;'>WAV 2.900</th><th style='text-align: center;'>WAV 2.905</th><th style='text-align: center;'>WAV 2.910</th><th style='text-align: center;'>WAV 2.915</th><th style='text-align: center;'>WAV 2.920</th><th style='text-align: center;'>WAV 2.925</th><th style='text-align: center;'>WAV 2.930</th><th style='text-align: center;'>WAV 2.935</th><th style='text-align: center;'>WAV 2.940</th><th style='text-align: center;'>WAV 2.945</th><th style='text-align: center;'>WAV 2.950</th><th style='text-align: center;'>WAV 2.955</th><th style='text-align: center;'>WAV 2.960</th><th style='text-align: center;'>WAV 2.965</th><th style='text-align: center;'>WAV 2.970</th><th style='text-align: center;'>WAV 2.975</th><th style='text-align: center;'>WAV 2.980</th><th style='text-align: center;'>WAV 2.985</th><th style='text-align: center;'>WAV 2.990</th><th style='text-align: center;'>WAV 2.995</th><th style='text-align: center;'>WAV 3.000</th><th style='text-align: center;'>WAV 3.005</th><th style='text-align: center;'>WAV 3.010</th><th style='text-align: center;'>WAV 3.015</th><th style='text-align: center;'>WAV 3.020</th><th style='text-align: center;'>WAV 3.025</th><th style='text-align: center;'>WAV 3.030</th><th style='text-align: center;'>WAV 3.035</th><th style='text-align: center;'>WAV 3.040</th><th style='text-align: center;'>WAV 3.045</th><th style='text-align: center;'>WAV 3.050</th><th style='text-align: center;'>WAV 3.055</th><th style='text-align: center;'>WAV 3.060</th><th style='text-align: center;'>WAV 3.065</th><th style='text-align: center;'>WAV 3.070</th><th style='text-align: center;'>WAV 3.075</th><th style='text-align: center;'>WAV 3.080</th><th style='text-align: center;'>WAV 3.085</th><th style='text-align: center;'>WAV 3.090</th><th style='text-align: center;'>WAV 3.095</th><th style='text-align: center;'>WAV 3.100</th><th style='text-align: center;'>WAV 3.105</th><th style='text-align: center;'>WAV 3.110</th><th style='text-align: center;'>WAV 3.115</th><th style='text-align: center;'>WAV 3.120</th><th style='text-align: center;'>WAV 3.125</th><th style='text-align: center;'>WAV 3.130</th><th style='text-align: center;'>WAV 3.135</th><th style='text-align: center;'>WAV 3.140</th><th style='text-align: center;'>WAV 3.145</th><th style='text-align: center;'>WAV 3.150</th><th style='text-align: center;'>WAV 3.155</th><th style='text-align: center;'>WAV 3.160</th><th style='text-align: center;'>WAV 3.165</th><th style='text-align: center;'>WAV 3.170</th><th style='text-align: center;'>WAV 3.175</th><th style='text-align: center;'>WAV 3.180</th><th style='text-align: center;'>WAV 3.185</th><th style='text-align: center;'>WAV 3.190</th><th style='text-align: center;'>WAV 3.195</th><th style='text-align: center;'>WAV 3.200</th><th style='text-align: center;'>WAV 3.205</th><th style='text-align: center;'>WAV 3.210</th><th style='text-align: center;'>WAV 3.215</th><th style='text-align: center;'>WAV 3.220</th><th style='text-align: center;'>WAV 3.225</th><th style='text-align: center;'>WAV 3.230</th><th style='text-align: center;'>WAV 3.235</th><th style='text-align: center;'>WAV 3.240</th><th style='text-align: center;'>WAV 3.245</th><th style='text-align: center;'>WAV 3.250</th><th style='text-align: center;'>WAV 3.255</th><th style='text-align: center;'>WAV 3.260</th><th style='text-align: center;'>WAV 3.265</th><th style='text-align: center;'>WAV 3.270</th><th style='text-align: center;'>WAV 3.275</th><th style='text-align: center;'>WAV 3.280</th><th style='text-align: center;'>WAV 3.285</th><th style='text-align: center;'>WAV 3.290</th><th style='text-align: center;'>WAV 3.295</th><th style='text-align: center;'>WAV 3.300</th><th style='text-align: center;'>WAV 3.305</th><th style='text-align: center;'>WAV 3.310</th><th style='text-align: center;'>WAV 3.315</th><th style='text-align: center;'>WAV 3.320</th><th style='text-align: center;'>WAV 3.325</th><th style='text-align: center;'>WAV 3.330</th><th style='text-align: center;'>WAV 3.335</th><th style='text-align: center;'>WAV 3.340</th><th style='text-align: center;'>WAV 3.345</th><th style='text-align: center;'>WAV 3.350</th><th style='text-align: center;'>WAV 3.355</th><th style='text-align: center;'>WAV 3.360</th><th style='text-align: center;'>WAV 3.365</th><th style='text-align: center;'>WAV 3.370</th><th style='text-align: center;'>WAV 3.375</th><th style='text-align: center;'>WAV 3.380</th><th style='text-align: center;'>WAV 3.385</th><th style='text-align: center;'>WAV 3.390</th><th style='text-align: center;'>WAV 3.395</th><th style='text-align: center;'>WAV 3.400</th><th style='text-align: center;'>WAV 3.405</th><th style='text-align: center;'>WAV 3.410</th><th style='text-align: center;'>WAV 3.415</th><th style='text-align: center;'>WAV 3.420</th><th style='text-align: center;'>WAV 3.425</th><th style='text-align: center;'>WAV 3.430</th><th style='text-align: center;'>WAV 3.435</th><th style='text-align: center;'>WAV 3.440</th><th style='text-align: center;'>WAV 3.445</th><th style='text-align: center;'>WAV 3.450</th><th style='text-align: center;'>WAV 3.455</th><th style='text-align: center;'>WAV 3.460</th><th style='text-align: center;'>WAV 3.465</th><th style='text-align: center;'>WAV 3.470</th><th style='text-align: center;'>WAV 3.475</th><th style='text-align: center;'>WAV 3.480</th><th style='text-align: center;'>WAV 3.485</th><th style='text-align: center;'>WAV 3.490</th><th style='text-align: center;'>WAV 3.495</th><th style='text-align: center;'>WAV 3.500</th><th style='text-align: center;'>WAV 3.505</th><th style='text-align: center;'>WAV 3.510</th><th style='text-align: center;'>WAV 3.515</th><th style='text-align: center;'>WAV 3.520</th><th style='text-align: center;'>WAV 3.525</th><th style='text-align: center;'>WAV 3.530</th><th style='text-align: center;'>WAV 3.535</th><th style='text-align: center;'>WAV 3.540</th><th style='text-align: center;'>WAV 3.545</th><th style='text-align: center;'>WAV 3.550</th><th style='text-align: center;'>WAV 3.555</th><th style='text-align: center;'>WAV 3.560</th><th style='text-align: center;'>WAV 3.565</th><th style='text-align: center;'>WAV 3.570</th><th style='text-align: center;'>WAV 3.575</th><th style='text-align: center;'>WAV 3.580</th><th style='text-align: center;'>WAV 3.585</th><th style='text-align: center;'>WAV 3.590</th><th style='text-align: center;'>WAV 3.595</th><th style='text-align: center;'>WAV 3.600</th><th style='text-align: center;'>WAV 3.605</th><th style='text-align: center;'>WAV 3.610</th><th style='text-align: center;'>WAV 3.615</th><th style='text-align: center;'>WAV 3.620</th><th style='text-align: center;'>WAV 3.625</th><th style='text-align: center;'>WAV 3.630</th><th style='text-align: center;'>WAV 3.635</th><th style='text-align: center;'>WAV 3.640</th><th style='text-align: center;'>WAV 3.645</th><th style='text-align: center;'>WAV 3.650</th><th style='text-align: center;'>WAV 3.655</th><th style='text-align: center;'>WAV 3.660</th><th style='text-align: center;'>WAV 3.665</th><th style='text-align: center;'>WAV 3.670</th><th style='text-align: center;'>WAV 3.675</th><th style='text-align: center;'>WAV 3.680</th><th style='text-align: center;'>WAV 3.685</th><th style='text-align: center;'>WAV 3.690</th><th style='text-align: center;'>WAV 3.695</th><th style='text-align: center;'>WAV 3.700</th><th style='text-align: center;'>WAV 3.705</th><th style='text-align: center;'>WAV 3.710</th><th style='text-align: center;'>WAV 3.715</th><th style='text-align: center;'>WAV 3.720</th><th style='text-align: center;'>WAV 3.725</th><th style='text-align: center;'>WAV 3.730</th><th style='text-align: center;'>WAV 3.735</th><th style='text-align: center;'>WAV 3.740</th><th style='text-align: center;'>WAV 3.745</th><th style='text-align: center;'>WAV 3.750</th><th style='text-align: center;'>WAV 3.755</th><th style='text-align: center;'>WAV 3.760</th><th style='text-align: center;'>WAV 3.765</th><th style='text-align: center;'>WAV 3.770</th><th style='text-align: center;'>WAV 3.775</th><th style='text-align: center;'>WAV 3.780</th><th style='text-align: center;'>WAV 3.785</th><th style='text-align: center;'>WAV</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.47 Effect of mass flow rate of chain-transfer agent EB on the PS mass flow rate and PDI of product polymer, stream P4.</div>


chain-transfer agent EB within feed stream S2 from 105 to 420 kg/hr on the PDI of PS in the product stream P4. We make a parametric plot of the result, with X-variable being the INIT mass flow in stream S2, parametric variable being the mass flow of chain-transfer agent EB in stream C2, and Y-variable being the PDI of PS in product P4. See Figures 6.48 and 6.49.

This concludes the current workshop for PS simulation with gel effect and oligomer formation.

---

<!-- PDF page 340 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_148_811_529.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.48 Defining the parametric plot of sensitivity analysis result.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Main Profile</th><th style='text-align: center;'>5.2</th><th style='text-align: center;'>5.2</th><th style='text-align: center;'>5.2</th><th style='text-align: center;'>5.2</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.49 PDI of PS in product P4 does not change much when INIT varies from 1 to 4 kg/hr but drops when mass flow of chain-transfer agent EB increases from 105 to 420 kg/hr.</div>


#### 6.2 Workshop 6.2: Production of Poly(Styrene–Butadiene–Styrene) or SBS Rubber by Ionic Polymerization

#### 6.2.1 Motivation and Objective for Modeling Ionic Polymerization Processes

As discussed previously, polystyrene is an important class of unsaturated polyolefins. PS and its copolymers, such as SBS rubber, represent approximately 10%

---

<!-- PDF page 341 -->

of commercial polymer production. In two classic papers, Chang et al. [15, 16] presented a convincing argument to study the fundamental modeling of anionic polymerization processes, using SBS rubber as an example. We summarize their reasoning below.

Elastomers refer to natural or synthetic polymers having elastic properties, such as rubber. Ziegler-Natta catalysts, discussed in Chapter 5, are widely used to produce elastomers of given stereo-specific microstructure (e.g. isotactic, syndiotactic, and atactic aspects) that are relatively insensitive to process variations and environmental impurities. However, it is difficult to produce customized polymers for new or unique applications. Fortunately, significant research achievements by polymer chemists on living anionic polymerization systems, especially with alkyllithium initiators, have opened doors for highly customized polymer architectures. We note that a living polymerization refers to a polymerization without any termination reactions taking place. Specifically, the tire and rubber industries have tailor-made elastomers of controlled molecular weight and molecular weight distribution, microstructure, sequence distribution, and branching in order to meet the market's requirements for tire and rubber qualities.

Living anionic polymerization systems with alkylithium initiators are sensitive to many process and chemistry variables, such as temperature, catalyst modifier, and the type and configuration of reactor systems, among others. The need to control many variables presents problems of reproducibility and scale-up for research chemists and process engineers. Chang et al. [15, 16] were among the first to demonstrate the power of fundamental process modeling to accurately predict conversion, microstructure, molecular weights, and distributions as a function of process and chemistry variables.

#### 6.2.2 Reactor Configurations and Copolymer Products

Anionic copolymerization of styrene and butadiene takes place in batch, semi-batch, or continuous reactors from 50 to 100 °C using n-, sec-, or tert-butyllithium initiators in hydrocarbon solvents, such as hexane and cyclohexane. Activators, such as tetrahydrofuran (THF), are also introduced into the reactor. THF promotes initial increases in chain propagation rate of the polymerization. It also serves as a chain-transfer agent. Chain termination is very rare in anionic polymerization, but can occur at the very end of a process to prevent any further polymer growth by adding a small amount of a chain-terminating agent, such as water.

There are three different types of styrene-butadiene copolymers produced by anionic polymerization [17, 18].

##### 6.2.2.1 Tapered Block Copolymer

In a batch reactor with styrene, butadiene, and alkylithium, a tapered block copolymer is formed. One block would be a butadiene-styrene (B/S) copolymer with only a small amount of styrene, and the other a polystyrene (S) block, resulting in an overall B/S-S structure.

---

<!-- PDF page 342 -->

##### 6.2.2.2 Di-/Tri-Block Copolymer and a Star-Shaped Block Copolymer

In a semi-batch reactor with sequential addition of styrene and butadiene, we can produce a di-/tri-block copolymer by first polymerizing styrene to form the “S” block, followed by addition of half of butadiene to form the half “B” block. We then add a di-functional coupling agent, such as iodine, to link the living polymer chains and form a tri-block copolymer, SBS.

We note that a star-shaped block copolymer could be produced by adding a tetravalent coupling agent such as silicone tetrachloride (SiCl₄) to unite two living di-blocks and form a star-shaped styrenic block copolymer (SBC). A star-shaped polymer is the simplest class of branched polymers, with a general structure consisting of several (at least three) linear chains connected to a central core. The core, or center, of the polymer can be an atom, molecule, or macromolecule; the chains, or “arms,” consist of variable-length organic chains.

##### 6.2.2.3 Random Copolymer

In a continuous reactor, polymerization of styrene and butadiene produces a random copolymer. The copolymer composition varies with flow rates of styrene and butadiene feeds.

#### 6.2.3 Components, Segments, and Polymer in Anionic Copolymerization of Styrene and Butadiene

Table 6.8 summarizes the relevant species in the anionic copolymerization.

Figure 6.50 shows the component specifications for anionic copolymerization of styrene and butadiene in Aspen Polymers.

#### 6.2.4 Thermodynamic Method and Property Parameters of Components and Polymer

Following Figure 6.11, we choose POLYNRTL thermodynamic method (Section 2.2.4 and Table 4.3) for anionic copolymerization of styrene and butadiene. To validate the accuracy of the POLYNRTL model in predicting the pure-component properties, we use the “Analysis” tool within the Properties environment of Aspen Polymers to predict the densities and ideal-gas heat capacities of styrene, butadiene, and THF and compare the predicted values with experimental data from the Design Institute for Physical Property Research (DIPPR) [19]. Figures 6.51–6.53 show the analysis input and predicted results for butadiene density at 1 atm from 100 to 400 K with 20 increments.

Figures 6.54–6.56 compare the predicted property values with experimental data from DIPPR [13]. The POLYNRTL thermodynamic method gives accurate prediction.

We also use molecular structures to estimate all missing property parameters. First, to define the molecular structure of BULI-6, currently represented by diisooctyl phthalate, we follow the procedure previously demonstrated in Figures 4.18, 4.19a–4.19c. Specifically, we search for the component on the website of

---

<!-- PDF page 343 -->

<div style="text-align: center;">Table 6.8 Component specification in anionic copolymerization of styrene and butadiene.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Component ID</td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Component name</td><td style='text-align: center; word-wrap: break-word;'>Alias in Aspen Polymers</td><td style='text-align: center; word-wrap: break-word;'>Function</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Styrene</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Styrene</td><td style='text-align: center; word-wrap: break-word;'>$ C_{8}H_{8} $</td><td style='text-align: center; word-wrap: break-word;'>Monomer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sty-seg</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>Styrene-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{8}H_{8}-R $</td><td style='text-align: center; word-wrap: break-word;'>Monomer segment</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Butadiene</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>1,3-Butadiene</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{6}-4 $</td><td style='text-align: center; word-wrap: break-word;'>Monomer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>But-seg</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>Butadiene-R-1</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{6}-R-1 $</td><td style='text-align: center; word-wrap: break-word;'>Monomer segment</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SBR</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>Styrene-Butadiene-Rubber</td><td style='text-align: center; word-wrap: break-word;'>SBR</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Buli-6</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Butyl-lithium-hexamer $ ^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>$ C_{24}H_{38}O_{4}-D1^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>Associated initiator</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Buli-1</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>n-Butyl-lithium $ ^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{9}Cl-D1^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>Initiator</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hexane</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>n-Hexane</td><td style='text-align: center; word-wrap: break-word;'>$ C_{6}H_{14}- $</td><td style='text-align: center; word-wrap: break-word;'>Solvent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cyclohex</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Cyclohexane</td><td style='text-align: center; word-wrap: break-word;'>$ C_{6}H_{12}-1 $</td><td style='text-align: center; word-wrap: break-word;'>Solvent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>THF</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Tetrahydrofuran</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{80}-4 $</td><td style='text-align: center; word-wrap: break-word;'>Activator, or chain-transfer agent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>I2</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Iodine</td><td style='text-align: center; word-wrap: break-word;'>I2</td><td style='text-align: center; word-wrap: break-word;'>Coupling agent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>StarCoup</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Silica-tetrachloride</td><td style='text-align: center; word-wrap: break-word;'>SiCl4</td><td style='text-align: center; word-wrap: break-word;'>Star-shaped coupling agent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2O</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>Water</td><td style='text-align: center; word-wrap: break-word;'>H2O</td><td style='text-align: center; word-wrap: break-word;'>Terminating agent</td></tr></table>

a) Buli-6 and Buli-1 are both not available within Aspen Polymers databank. Use diisooctyl-phthalate (C24H38O4-D1) to represent Buli-6 and specify its molecular weight as 384 (true molecular weight of Buli-6); and use isobutyl chloride (C4H9Cl-D1) to represent Buli-1 and specify its molecular weight as 64 (true molecular weight of BuLi-1).

Chemical Book (www.chemicalbook.com). We Google for the entry “Chemical Book, diisooctyl phthalate,” and see the component ACS number 27554-26-2 together with the molecular file 27554-26-3.mol. We download and save the molecular structure file and import it into Aspen Polymers by following the path: Properties → Components → Molecular Structure → BULI-6 → Structure (Graphical Structure) → Draw/Import/Edit → Molecule Editor → Import Mol File → 27554-26-3.mol → Structure shown in Figure 6.57.

We follow Figures 4.19a–4.19c to quantify the structure of BULI-6 in terms of atoms C, H, and O. After defining all the molecular structures, we estimate the missing property parameters. See Figures 6.58–6.60.

#### 6.2.5 Kinetics of Anionic Copolymerization of Styrene and Butadiene

##### 6.2.5.1 Initiator Disassociation (INIT-DISSOC)

For anionic polymerization, the active species is the initiator in a dissociated form [21–23]. We observe the association and disassociation of initiator in an alkylithium

---

<!-- PDF page 344 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="6">Select components</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Component ID</td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Component name</td><td style='text-align: center; word-wrap: break-word;'>Alias</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>STY-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>STYRENE-R</td><td style='text-align: center; word-wrap: break-word;'>C8H8-R</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'>C8H8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BUT-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>BUTADIENE-R-1</td><td style='text-align: center; word-wrap: break-word;'>C4H6-R-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BUTADIEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>1,3-BUTADIENE</td><td style='text-align: center; word-wrap: break-word;'>C4H6-4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SBR</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>STYRENE-BUTADIENE-RUBBER</td><td style='text-align: center; word-wrap: break-word;'>SBR</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BULI-1</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>ISOBUTYL-CHLORIDE</td><td style='text-align: center; word-wrap: break-word;'>C4H9Cl-D1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BULI-6</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>DIISOCOTYL-PHTHALATE</td><td style='text-align: center; word-wrap: break-word;'>C24H38O4-D1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEXANE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>N-HEXANE</td><td style='text-align: center; word-wrap: break-word;'>C6H14-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CYCLOHEX</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>CYCLOHEXANE</td><td style='text-align: center; word-wrap: break-word;'>C6H12-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ACTIVATO</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>TETRAHYDROFURAN</td><td style='text-align: center; word-wrap: break-word;'>C4H8O-4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>IODINE</td><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>STARCOUP</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>SILICON-TETRACHLORIDE</td><td style='text-align: center; word-wrap: break-word;'>SICL4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WATER</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>WATER</td><td style='text-align: center; word-wrap: break-word;'>H2O</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 6.50 Component specifications for anionic copolymerization of styrene and butadiene.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_651_811_944.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.51 Analysis input for predicting the density of butadiene.</div>


type of initiators in nonpolar solvents.

 $$  INIT-DISSOC:Buli-6\leftrightarrow6Buli-1 $$ 

BuLi-6 is the associated initiator. 6 is the degree of ionization. Buli-1 is the disassociated initiator.

##### 6.2.5.2 Chain Initiation (CHAIN-INI)

The ionic polymerization model within Aspen Polymers adopts the same kinetic framework as in the Ziegler–Natta multisite kinetic model. In the ionic polymerization model, each active site refers to a unique type of active species, which

---

<!-- PDF page 345 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_172_782_513.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.52 Predicted density of butadiene. Clicking on Plot → Property on the upper right corner will show the plot of Figure 6.75.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature (°C)</th><th style='text-align: center;'>RHD (°C)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>15.25</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>14.75</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>14.45</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>14.15</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>13.85</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>13.55</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>13.25</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>13.00</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>12.75</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>12.50</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>12.25</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>12.00</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>11.75</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.53 Predicted density of butadiene as a function of temperature.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>T (K)</th><th style='text-align: center;'>Density (kmol/cum)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>13.8</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>13.6</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>13.4</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>13.2</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>12.8</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>12.6</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>12.4</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>11.8</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>11.6</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>11.4</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>11.2</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>10.8</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>10.6</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>10.4</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>10.2</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>9.8</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>9.6</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>9.4</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>9.2</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>8.8</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.54 Comparing experimental data with PolyNRTL predictions for the densities of 1,3-butadiene. The literature values are from DIPPR. Source: Adapted from Bokis et al. [13].</div>


---

<!-- PDF page 346 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>T (K)</th><th style='text-align: center;'>exp styrene (kmol/cum)</th><th style='text-align: center;'>PolyNRTL styrene (kmol/cum)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>980</td><td style='text-align: center;'>980</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>960</td><td style='text-align: center;'>960</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>940</td><td style='text-align: center;'>940</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>920</td><td style='text-align: center;'>920</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>880</td><td style='text-align: center;'>880</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>860</td><td style='text-align: center;'>860</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>840</td><td style='text-align: center;'>840</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>820</td><td style='text-align: center;'>820</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>780</td><td style='text-align: center;'>780</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>760</td><td style='text-align: center;'>760</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>740</td><td style='text-align: center;'>740</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>720</td><td style='text-align: center;'>720</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>680</td><td style='text-align: center;'>680</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>660</td><td style='text-align: center;'>660</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>640</td><td style='text-align: center;'>640</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>620</td><td style='text-align: center;'>620</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>580</td><td style='text-align: center;'>580</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>560</td><td style='text-align: center;'>560</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>540</td><td style='text-align: center;'>540</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.55 Comparing experimental data with PolyNRTL predictions for the densities of styrene and THF. The literature values are from DIPPR. Source: Adapted from Ref. [19].</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature (K)</th><th style='text-align: center;'>PolyNRTL styrene (J/kmol K)</th><th style='text-align: center;'>PolyNRTL butadiene (J/kmol K)</th><th style='text-align: center;'>PolyNRTL THF (J/kmol K)</th><th style='text-align: center;'>exp styrene (J/kmol K)</th><th style='text-align: center;'>exp butadiene (J/kmol K)</th><th style='text-align: center;'>exp THF (J/kmol K)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>100000</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>99000</td><td style='text-align: center;'>99000</td><td style='text-align: center;'>99000</td><td style='text-align: center;'>99000</td><td style='text-align: center;'>99000</td><td style='text-align: center;'>99000</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>98000</td><td style='text-align: center;'>98000</td><td style='text-align: center;'>98000</td><td style='text-align: center;'>98000</td><td style='text-align: center;'>98000</td><td style='text-align: center;'>98000</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>97000</td><td style='text-align: center;'>97000</td><td style='text-align: center;'>97000</td><td style='text-align: center;'>97000</td><td style='text-align: center;'>97000</td><td style='text-align: center;'>97000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>96000</td><td style='text-align: center;'>96000</td><td style='text-align: center;'>96000</td><td style='text-align: center;'>96000</td><td style='text-align: center;'>96000</td><td style='text-align: center;'>96000</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>95000</td><td style='text-align: center;'>95000</td><td style='text-align: center;'>95000</td><td style='text-align: center;'>95000</td><td style='text-align: center;'>95000</td><td style='text-align: center;'>95000</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>94000</td><td style='text-align: center;'>94000</td><td style='text-align: center;'>94000</td><td style='text-align: center;'>94000</td><td style='text-align: center;'>94000</td><td style='text-align: center;'>94000</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>93000</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>92000</td><td style='text-align: center;'>92000</td><td style='text-align: center;'>92000</td><td style='text-align: center;'>92000</td><td style='text-align: center;'>92000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>91000</td><td style='text-align: center;'>91000</td><td style='text-align: center;'>91000</td><td style='text-align: center;'>91000</td><td style='text-align: center;'>91000</td><td style='text-align: center;'>91000</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>90000</td><td style='text-align: center;'>90000</td><td style='text-align: center;'>90000</td><td style='text-align: center;'>90000</td><td style='text-align: center;'>90000</td><td style='text-align: center;'>90000</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>89000</td><td style='text-align: center;'>89000</td><td style='text-align: center;'>89000</td><td style='text-align: center;'>89000</td><td style='text-align: center;'>89000</td><td style='text-align: center;'>89000</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>88000</td><td style='text-align: center;'>88000</td><td style='text-align: center;'>88000</td><td style='text-align: center;'>88000</td><td style='text-align: center;'>88000</td><td style='text-align: center;'>88000</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>87000</td><td style='text-align: center;'>87000</td><td style='text-align: center;'>87000</td><td style='text-align: center;'>87000</td><td style='text-align: center;'>87000</td><td style='text-align: center;'>87000</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>86000</td><td style='text-align: center;'>86000</td><td style='text-align: center;'>86000</td><td style='text-align: center;'>86000</td><td style='text-align: center;'>86000</td><td style='text-align: center;'>86000</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>85000</td><td style='text-align: center;'>85000</td><td style='text-align: center;'>85000</td><td style='text-align: center;'>85000</td><td style='text-align: center;'>85000</td><td style='text-align: center;'>85000</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>84000</td><td style='text-align: center;'>84000</td><td style='text-align: center;'>84000</td><td style='text-align: center;'>84000</td><td style='text-align: center;'>84000</td><td style='text-align: center;'>84000</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>83000</td><td style='text-align: center;'>83000</td><td style='text-align: center;'>83000</td><td style='text-align: center;'>83000</td><td style='text-align: center;'>83000</td><td style='text-align: center;'>83000</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>82000</td><td style='text-align: center;'>82000</td><td style='text-align: center;'>82000</td><td style='text-align: center;'>82000</td><td style='text-align: center;'>82000</td><td style='text-align: center;'>82000</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>81000</td><td style='text-align: center;'>81000</td><td style='text-align: center;'>81000</td><td style='text-align: center;'>81000</td><td style='text-align: center;'>81000</td><td style='text-align: center;'>81000</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>80000</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>79000</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>77000</td><td style='text-align: center;'>77000</td><td style='text-align: center;'>77000</td><td style='text-align: center;'>77000</td><td style='text-align: center;'>77000</td><td style='text-align: center;'>77000</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>76000</td><td style='text-align: center;'>76000</td><td style='text-align: center;'>76000</td><td style='text-align: center;'>76000</td><td style='text-align: center;'>76000</td><td style='text-align: center;'>76000</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>75000</td><td style='text-align: center;'>75000</td><td style='text-align: center;'>75000</td><td style='text-align: center;'>75000</td><td style='text-align: center;'>75000</td><td style='text-align: center;'>75000</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>74000</td><td style='text-align: center;'>74000</td><td style='text-align: center;'>74000</td><td style='text-align: center;'>74000</td><td style='text-align: center;'>74000</td><td style='text-align: center;'>74000</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>73000</td><td style='text-align: center;'>73000</td><td style='text-align: center;'>73000</td><td style='text-align: center;'>73000</td><td style='text-align: center;'>73000</td><td style='text-align: center;'>73000</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>72000</td><td style='text-align: center;'>72000</td><td style='text-align: center;'>72000</td><td style='text-align: center;'>72000</td><td style='text-align: center;'>72000</td><td style='text-align: center;'>72000</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>71000</td><td style='text-align: center;'>71000</td><td style='text-align: center;'>71000</td><td style='text-align: center;'>71000</td><td style='text-align: center;'>71000</td><td style='text-align: center;'>71000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.56 Comparing experimental data with PolyNRTL predictions for heat capacity of styrene, butadiene, and tetrahydrofuran. Source: The literature values are adapted from Caruthers et al. [20].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_725_816_982.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.57 Structure of diisooctyl phthalate, representing the associated initiator BULI-6.</div>


corresponds to an initiator in a disassociated form. For example, to model three propagating species for an initiator, the model considers three active sites or active species (particularly active site or species 1 for free ions, 2 for ion pairs, and 3 for dormant esters) with each corresponding to a unique propagating active species type. We consider three types of chain-initiation reactions.

CHAIN-INI-1 The initiator in a disassociated form is an active species with a chain length of zero, Po[1], which can react with a monomer to form a propagating species (a live polymer molecular chain) with a unit chain length, P1[1,Sty-Seg] or

---

<!-- PDF page 347 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_781_342.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.58 Estimation of all missing parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_408_781_625.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.59 Estimated pure-component property parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_691_782_879.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.60 Estimated binary interaction parameters NRTL-1.</div>


P1[1,But-Seg], with an active segment, Sty-Seg or But-Seg, attached to it. Here, “1” refers to active site or active species 1, which corresponds to a free ion. Thus, this chain-initiation reaction involves a monomer and an active species.

 $$ \mathrm{Po}[1]+\mathrm{Styrene}\rightarrow\mathrm{P1}[1,\mathrm{Sty-Seg}] $$ 

 $$ \mathrm{P o[1]+B u t a d i e n e\rightarrow P1[1,B u t-S e g]} $$ 

CHAIN-INI-2 This chain-initiation reaction involves a monomer and a disassociated initiator, and it may produce a C-ion (when the stoichiometric coefficient d is not zero). A C-ion represents a counter ion that accompanies an ionic species in order to maintain electric neutrality. As an example, in table salt, the sodium ion is the counter ion for the chlorine ion, and vice versa. We commonly call a counter ion as an anion or a cation, depending on whether it is negatively or positively charged.

---

<!-- PDF page 348 -->

We note that for the anionic copolymerization of styrene and butadiene, more ion pairs (type 2 active species or site) are initiated than free ions (type 1 active species or site) [21].

 $$ \mathrm{Buli-1}+\mathrm{Styrene}\rightarrow\mathrm{P1}[1,\mathrm{Sty-Seg}]+\mathrm{d}\cdot\mathrm{C}-\mathrm{Ion} $$ 

 $$ \mathrm{Buli-1}+\mathrm{Butadiene}\rightarrow\mathrm{P1[1,But-Seg]}+\mathrm{d}\cdot\mathrm{C}-\mathrm{Ion} $$ 

CHAIN-INI-T The third chain-initiation reaction involves a monomer and a transfer active species, PTo[1], which results from a chain-transfer reaction of a growing polymer chain (see Section 6.2.5.5 below), to form a propagating species with a unit chain length with an active segment, Sty-Seg or But-Seg, attached to it.

 $$ \mathrm{PTo[1]+Styrene\rightarrow P1[1,Sty-Seg]} $$ 

 $$ \mathrm{P T o[1]+B u t a d i e n e\rightarrow P1[1,B u t-S e g]} $$ 

##### 6.2.5.3 Chain Propagation (PROPAGATION)

Polymer chains grow by means of chain propagation. A growing polymer, with an active species at the end of the chain, propagates through the addition of monomer to create longer polymer chains. Increasing the amount of monomer in the system yields larger polymer chains.

 $$  PROPAGATION:Pn[1,Sty-Seg]+Styrene\rightarrow Pn+1[1,Sty-Seg] $$ 

 $$ \mathrm{Pn}[1,\mathrm{Sty-Seg}]+\mathrm{Butadiene}\rightarrow\mathrm{Pn}+1[1,\mathrm{But-Seg}] $$ 

 $$ \mathrm{Pn}[1,\mathrm{But-Seg}]+\mathrm{Styrene}\rightarrow\mathrm{Pn}+1[1,\mathrm{Sty-Seg}] $$ 

 $$ \mathrm{Pn}[1,\mathrm{But-Seg}]+\mathrm{Butadiene}\rightarrow\mathrm{Pn}+1[1,\mathrm{But-Seg}] $$ 

The propagation reaction accounts for the total amount of polymer produced. We observe that an increase in the rate constant results in a linear increase in polymer molecular weight.

##### 6.2.5.4 Association or Aggregation (ASSOCIATION)

In anionic polymerization by alkylithium-type initiators, propagating species also exhibit an association phenomenon like the initiator. The association of the live polymer species is usually dimeric and creates the associate polymers, Qn+m[1,Sty-Seg] and Qn+m[1,But-Seg]. The associated polymer does not participate in any other reactions.

 $$ \mathrm{ASSOCIATION:Pn[1,Sty-Seg]+Pm[1,Sty-Seg]}\quad\leftrightarrow\mathrm{Qn+m[1,Sty-Seg]} $$ 

 $$ \begin{array}{r l}{\mathrm{P n}[1,\mathrm{B u t-S e g}]+\mathrm{P m}[1,\mathrm{B u t-S e g}]}&{{}\leftrightarrow\mathrm{Q n}+\mathrm{m}[1,\mathrm{B u t-S e g}]}\end{array} $$ 

---

<!-- PDF page 349 -->

##### 6.2.5.5 Chain Transfer (CHAT)

Chain transfer can lead to the formation of dead polymer chains,  $ D_n $. This process limits the molecular weight of the polymer. We also fine-tune chain-transfer rate constants to match the MWW. Specifically, we consider three types of chain-transfer reactions. The first reaction we incorporate is a reaction with an activator or a chain-transfer agent, CHAT-AGENT. For anionic copolymerization of styrene and butadiene, our activator (“Activato”) or chain-transfer agent is tetrahydrofuran (THF).

We also consider the spontaneous chain transfer, CHAT-SPON, and the chain transfer to monomer, CHAT-MONOMER. We ignore the chain-transfer reaction that leads to the formation of dormant polymer (CHAT-DORM-P) [17].

CHAT-AGENT A growing polymer chain, Pn[1, Sty-Seg] or Pn[1,But-Seg], can be transferred to an activator or a chain-transfer agent, leading to the formation of a dead polymer chain of n segments, Dn, and a transfer active species, PTo[1], of the same type. PTo[1] can then participate in a new chain-initiation reaction, CHAIN-INI-T. See Eqs. (6.7) and (6.8).

 $$ \mathrm{Pn[1,Sty-Seg]+Activato^{^\wedge}order\rightarrow Dn[1]+PTo[1]} $$ 

 $$ \mathrm{Pn}[1,\mathrm{But}-\mathrm{Seg}]+\mathrm{Activato}^{\wedge}\mathrm{order}\rightarrow\mathrm{Dn}[1]+\mathrm{PTo}[1] $$ 

The reaction order with respect to the activator or chain-transfer agent, “order,” is set by the user.

CHAT-SPON A spontaneous chain transfer is the third type of chain transfer in our model. This reaction leads to the formation of a dead polymer molecule Dn[1] and a polymer active species Po[1] by proton loss.

 $$ \mathrm{Pn}[1,\mathrm{Sty-Seg}]\rightarrow\mathrm{Dn}[1]+\mathrm{Po}[1] $$ 

 $$ \mathrm{Pn}[1,\mathrm{But-Seg}]\rightarrow\mathrm{Dn}[1]+\mathrm{Po}[1] $$ 

CHAT-MONOMER This reaction results in the formation of a dead polymer molecule Dn[1] and a propagating species with a unit chain length with an active segment, Sty-Seg or But-Seg, attached to it, that is, P1[1,Sty-Seg] or P1[1,But-Seg].

 $$ \mathrm{Pn}[1,\mathrm{Sty-Seg}]+\mathrm{Styrene}\rightarrow\mathrm{Dn}[1]+\mathrm{P1}[1,\mathrm{Sty-Seg}] $$ 

 $$ \mathrm{Pn}[1,\mathrm{Sty-Seg}]+\mathrm{Butadien}\rightarrow\mathrm{Dn}[1]+\mathrm{P1}[1,\mathrm{Sty-Seg}] $$ 

 $$ \mathrm{Pn[1,But-Seg]+Styrene\rightarrow Dn[1]+P1[1,But-Seg]} $$ 

 $$ \mathrm{Pn}[1,\mathrm{But-Seg}]+\mathrm{Butadien}\rightarrow\mathrm{Dn}[1]+\mathrm{P1}[1,\mathrm{But-Seg}] $$ 

---

<!-- PDF page 350 -->

##### 6.2.5.6 Chain Termination (TERM-AGENT)

Chain-termination reaction is very rare in anionic polymerization reactions, but it can occur at the very end of a process to prevent any further polymer growth. We can use water as a terminating agent to terminate a growing polymer Pn[1, Sty-Seg] or Pn[1,But-Seg], thus creating a dead polymer chain Dn[1].

 $$  TERM-AGENT:Pn[1,Sty-Seg]+T_{m}\rightarrow Dn[1] $$ 

 $$ \mathrm{Pn}[1,\mathrm{But-Seg}]+T_{\mathrm{m}}\rightarrow\mathrm{Dn}[1] $$ 

 $ T_{m} $ is the termination agent, and in our workshop, it is water. Since the number of initiators far exceeds the amount of water in the system, we disregard this reaction in our model. There is 369 ppm of initiators entering the system and only 30 ppm of water in the system. We assume that the initiation rate is of the same order as the termination rate.

##### 6.2.5.7 Equilibrium with Counter-Ion or Reversible Ionization (EQUILIB-CION)

The following reactions represent the equilibrium between free ions (active site or species type 1) and ion pairs (active site or species type 2), hence the name equilibrium with counter ion.

 $$ \mathrm{EQUILIB-CION}:\mathrm{Pn}[2,\mathrm{Sty-Seg}]\leftrightarrow\mathrm{Pn}[1,\mathrm{Sty-Seg}]+\mathrm{C-Ion} $$ 

 $$ \mathrm{Pn}[2,\mathrm{But-Seg}]\leftrightarrow\mathrm{Pn}[1,\mathrm{But-Seg}]+\mathrm{C-Ion} $$ 

Table 6.9 summarizes our reactions for the anionic copolymerization of styrene and butadiene.

Figures 6.61 and 6.62 show how to implement these reactions within Aspen Polymers and our selected reactions for our workshop of styrene–butadiene copolymerization below. Depending on our feeds and reactor type, we may add or delete some reactions in the examples below.

Figure 6.63 shows the initial values of the reaction-rate constants and activation energies [16].

Research [17] shows that the order of propagation rate constants for anionic polymerization of styrene and butadiene, reactions 8–11, in Figure 6.63, is as follows:  $ k_{SB} $ (Sty-Seg-Butadiene) >  $ k_{SS} $ (Sty-Seg-Styrene) >  $ k_{BB} $ (But-Seg-Butadiene) >  $ k_{BS} $ (But-Seg-Butadiene), or 10 > 5 > 2.5 > 0.1389. In the figure, we purposely set the pre-exponential factors for TERM-AGENT reactions to zero. Water is the termination agent in this batch reaction; however, since the number of initiators far exceeds the amount of water in the system, we can disregard the two termination reactions in our model. As discussed previously, there is 369 ppm of initiators entering our industrial process, and only 30 ppm of water entering the process.

##### 6.2.5.8 Batch Reactor for Producing a Tapered Block Copolymer

Reactor Flowsheet and Feed and Operating Conditions Figure 6.64 shows the simple batch-reactor flowsheet for producing a tapered block polymer. We save the simulation file as WS6.2_SBC Batch.bkp.

---

<!-- PDF page 351 -->

<div style="text-align: center;">Table 6.9 Reactions for the anionic copolymerization of styrene and butadiene.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Equation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>INIT-DISSOC: initiator disassociation</td><td style='text-align: center; word-wrap: break-word;'>(6.2)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-1: active species-styrene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.3)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-1: active species-butadiene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.4)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-2: initiator-styrene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.5)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-2: initiator-butadiene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.6)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-T: transfer active species-styrene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.7)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI-T: transfer active species-butadiene chain initiation</td><td style='text-align: center; word-wrap: break-word;'>(6.8)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>PROPAGATION: styrene-styrene propagation</td><td style='text-align: center; word-wrap: break-word;'>(6.9)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>PROPAGATION: styrene-butadiene-propagation</td><td style='text-align: center; word-wrap: break-word;'>(6.10)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>PROPAGATION: butadiene-styrene propagation</td><td style='text-align: center; word-wrap: break-word;'>(6.11)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>PROPAGATION: butadiene-butadiene propagation</td><td style='text-align: center; word-wrap: break-word;'>(6.12)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>ASSOCIATION: styrene segment association</td><td style='text-align: center; word-wrap: break-word;'>(6.13)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>ASSOCIATION: butadiene segment association</td><td style='text-align: center; word-wrap: break-word;'>(6.14)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>CHAT-AGENT: styrene segment chain transfer by THF</td><td style='text-align: center; word-wrap: break-word;'>(6.15)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>CHAT-AGENT: butadiene segment chain transfer by THF</td><td style='text-align: center; word-wrap: break-word;'>(6.16)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>TERM-AGENT: styrene segment chain termination by water</td><td style='text-align: center; word-wrap: break-word;'>(6.23)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>TERM-AGENT: butadiene segment chain termination by water</td><td style='text-align: center; word-wrap: break-word;'>(6.24)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>EQUILIB-CION: equilibrium between free ions and ions pairs (styrene segment)</td><td style='text-align: center; word-wrap: break-word;'>(6.25)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>19</td><td style='text-align: center; word-wrap: break-word;'>EQUILIB-CION: equilibrium between free ions and ion pairs (butadiene segment)</td><td style='text-align: center; word-wrap: break-word;'>(6.26)</td></tr></table>

We use the METCBAR unit system, and Figure 6.65 specifies our feed.

We specify the reactor at constant temperature of 50 °C, with the valid phases being the reactor phase with liquid only. We fix the reactor pressure at 0 bar (meaning no pressure drop). There is 0 kg of catalyst loading. We set the reaction set as R1 (see Figures 6.61 and 6.62). For the batch-reactor operation, our specifications for stop criteria and operating times appear in Figures 6.66 and 6.67.

Simulation Results Figure 6.68 shows the calculated mass balance and polymer molecular weights based on the kinetic polymerization of Figures 6.61–6.63.

We see that 86.8% of monomers, styrene and butadiene, are converted to SBR polymer with an MWN of 89,983, an MWW of 108,580, and a PDI of 1.2066. In the next example, we will use a semi-batch reactor with sequential additions of monomers to produce a tri-block copolymer. We will also fine-tune the reaction kinetics to match plant data.

Figure 6.69 shows the composition profiles of styrene, butadiene, and SBR block polymer versus the batch reaction time. Figure 6.70 shows the MWW and PDI of the SBR block polymer versus batch reaction time.

---

<!-- PDF page 352 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_157_812_535.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.61 Species specification of the ionic reaction set R-1 for anionic copolymerization of styrene and butadiene.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_626_813_1192.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.62 Reactions for anionic copolymerization of styrene and butadiene following Table 6.9 and ignoring CHAT-SPON, CHAT-MONOMER, and TERM-AGENT reactions.</div>


---

<!-- PDF page 353 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_155_780_479.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.63 Initial values of pre-exponential factors and activation energies.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_539_740_788.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 6.64 A batch reactor for producing a tapered block copolymer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_855_781_1213.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.65 Feed specifications.</div>


---

<!-- PDF page 354 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_813_459.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.66 Stop criteria for batch-reactor operation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_544_812_859.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.67 Operation times for the batch reactor.</div>


##### 6.2.5.9 Semi-Batch Reactor for Producing a Tri-Block SBS Copolymer by an Industrial Batch-Sequence Recipe

Reactor Flowsheet and Feed and Operating Conditions Figure 6.71 shows the simple semi-batch reactor flowsheet for producing a tri-block SBS copolymer. We save the simulation file as WS6.2_SBC Semi-Batch.bkp.

Figure 6.72 specifies the solvent mixture as our initial charge to the semi-batch reactor.

Table 6.10 shows the specifications for continuous feeds.

Figure 6.73a shows the specifications of the semi-batch reactor. Remember to specify the valid phases as reactor phase, liquid-only. Specify the reaction set R-1 (Figure 6.62).

Figure 6.73b illustrates the stopping criterion and operation times for the batch-reactor simulation.

---

<!-- PDF page 355 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Units</td><td style='text-align: center; word-wrap: break-word;'>FEED</td><td style='text-align: center; word-wrap: break-word;'>PROD</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Molar Density</td><td style='text-align: center; word-wrap: break-word;'>mol/cc</td><td style='text-align: center; word-wrap: break-word;'>0.00963198</td><td style='text-align: center; word-wrap: break-word;'>0.00969401</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass Density</td><td style='text-align: center; word-wrap: break-word;'>gm/cc</td><td style='text-align: center; word-wrap: break-word;'>0.771856</td><td style='text-align: center; word-wrap: break-word;'>0.795784</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Enthalpy Flow</td><td style='text-align: center; word-wrap: break-word;'>cal/sec</td><td style='text-align: center; word-wrap: break-word;'>$ -1.27574 \times 10^{6} $</td><td style='text-align: center; word-wrap: break-word;'>$ -1.82686 \times 10^{6} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Average MW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>80.1348</td><td style='text-align: center; word-wrap: break-word;'>82.0903</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ - $ Mass Flows</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>90718.5</td><td style='text-align: center; word-wrap: break-word;'>90722.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>4031.47</td><td style='text-align: center; word-wrap: break-word;'>1329.42</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BUTDIENE</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>6047.2</td><td style='text-align: center; word-wrap: break-word;'>14.3193</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SBR</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>8749.88</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BULI-6</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>10.4818</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BULI-1</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEXANE</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>80629.3</td><td style='text-align: center; word-wrap: break-word;'>80629.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CYCLOHEX</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ACTIVATO</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>I2</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>STARCOUP</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WATER</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \checkmark $ LSSFRAC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \checkmark $ LSSMOM</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>89982.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>108580</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.20668</td></tr></table>

<div style="text-align: center;">Figure 6.68 Simulated results of tapered SBR block polymer using a batch reactor.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time/y</th><th style='text-align: center;'>Batch (Batch)</th><th style='text-align: center;'>Profiles (Profiles)</th><th style='text-align: center;'>Control Panel (Control Panel)</th><th style='text-align: center;'>Reactions (Reactions)</th><th style='text-align: center;'>Batch (Batch)</th><th style='text-align: center;'>Stream Results (Stream Results)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.002</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.003</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.004</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.005</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.006</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.007</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.008</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.009</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.010</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.011</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.012</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.013</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.014</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.015</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.016</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.017</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.018</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.019</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.020</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.021</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.022</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.023</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.024</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.026</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.027</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.028</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.029</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.030</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.031</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.032</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.033</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.034</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.036</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.037</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.038</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.039</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.040</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.041</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.042</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.043</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.044</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.045</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.046</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.047</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.048</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.049</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.050</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.051</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.052</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.053</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.054</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.056</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.057</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.058</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.059</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.060</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.061</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.062</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.063</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.064</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.065</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.066</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.067</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.068</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.069</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.070</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.071</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.072</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.073</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.074</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.075</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.076</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.077</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.078</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.079</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.080</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.081</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.082</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.083</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.084</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.69 Composition profiles of styrene, butadiene, and SBR block polymer versus batch reaction time.</div>


Figure 6.73c shows the sequential addition of continuous feeds as a function of operation times.

Table 6.11 shows an industrial batch-sequence recipe for this workshop. Because of the sequential addition of continuous feeds, the component mass flows of essential feed components, as illustrated in Figure 6.73c, represent the actual mass flows to the semi-batch reactor at different times. These values take precedence over the mass flow rate entered in the stream input form (Figure 6.72) or specified in Table 6.11.

---

<!-- PDF page 356 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>100.00</th><th style='text-align: center;'>0.04</th><th style='text-align: center;'>0.08</th><th style='text-align: center;'>0.10</th><th style='text-align: center;'>0.15</th><th style='text-align: center;'>0.20</th><th style='text-align: center;'>0.25</th><th style='text-align: center;'>0.30</th><th style='text-align: center;'>0.35</th><th style='text-align: center;'>0.40</th><th style='text-align: center;'>0.45</th><th style='text-align: center;'>0.50</th><th style='text-align: center;'>0.55</th><th style='text-align: center;'>0.60</th><th style='text-align: center;'>0.65</th><th style='text-align: center;'>0.70</th><th style='text-align: center;'>0.75</th><th style='text-align: center;'>0.80</th><th style='text-align: center;'>0.85</th><th style='text-align: center;'>0.90</th><th style='text-align: center;'>0.95</th><th style='text-align: center;'>1.00</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.42</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.44</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.48</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.52</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.54</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.70 MWW and PDI of the SBR block polymer as a function of the batch reaction time.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_505_770_896.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 6.71 A semi-batch reactor for producing a triblock SBS copolymer.</div>


Simulation Results We wish to fine-tune kinetic parameters of the model to match the average plant data of SBS mass production of 910 kg/min, MWN of 104,310, and MWW of 108,800. Figure 6.74 illustrates our methodology for kinetic parameter estimation for the anionic polymerization of styrene and butadiene to produce SBS block copolymer.

Following this methodology to fine-tune the kinetic parameters, we obtain the simulation results along with their comparison with plant data in Table 6.12. Figure 6.75 shows the resulting set of kinetic parameters. We note that fine-tuning the kinetic parameters to match both MWW and MWN exactly is a challenging task. While we can easily find the set of kinetic parameters to match either MWN or MWN exactly, it is difficult to identify the set of kinetic parameters to match both MWW and MWN exactly.

---

<!-- PDF page 357 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_161_781_520.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.72 Specification of the initial charge stream, CHARGE.</div>


<div style="text-align: center;">Table 6.10 Specifications of continuous feeds.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (atm)</td><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/min)</td><td style='text-align: center; word-wrap: break-word;'>Composition (mass fraction)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Styrene</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>12.667</td><td style='text-align: center; word-wrap: break-word;'>Styrene = 0.99998, water = 2E-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Butadiene</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>19</td><td style='text-align: center; word-wrap: break-word;'>Butadiene = 0.999988, water = 1.2E-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Initiator</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2.06</td><td style='text-align: center; word-wrap: break-word;'>buli-6 = 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Solvent</td><td style='text-align: center; word-wrap: break-word;'>53</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.667</td><td style='text-align: center; word-wrap: break-word;'>hexane = 0.3, cyclohex = 0.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Activato</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>activator = 0.99997, water = 3E-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Water</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.38</td><td style='text-align: center; word-wrap: break-word;'>Water = 1</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_936_782_1208.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.73a Specifications of the semi-batch reactor.</div>


---

<!-- PDF page 358 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_150_812_385.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.73b Specification of stopping criterion and operation times of batch-reactor simulation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_460_811_707.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.73c Sequential addition of continuous feeds as a function of operation times.</div>


<div style="text-align: center;">Table 6.11 Batch-sequence recipe.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Sequence number</td><td style='text-align: center; word-wrap: break-word;'>Process step</td><td style='text-align: center; word-wrap: break-word;'>Time (min)</td><td style='text-align: center; word-wrap: break-word;'>Added amount (kg/min)</td><td style='text-align: center; word-wrap: break-word;'>Temperature control (°C)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Add styrene</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>82.5</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Add activator (THF)</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>5.5</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>Add wash solvent</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Add initiator (BuLi6)</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>50.8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>Add wash solvent</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>Step 1: SLi formation</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Below 57.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>Add butadiene</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>318</td><td style='text-align: center; word-wrap: break-word;'>55.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>Add wash solvents</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>Step 2: SB-Li formation</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Below 91.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>Add styrene</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>82.5</td><td style='text-align: center; word-wrap: break-word;'>90.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>Add wash solvents</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>Step 3: SBS-Li+ formation</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Below 90.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>Add water</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<!-- PDF page 359 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_158_717_572.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 6.74 Methodology for kinetic parameter estimation for anionic polymerization of styrene and butadiene to produce SBS block copolymer.</div>


<div style="text-align: center;">Table 6.12 Comparison of simulation results with plant data.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Simulation target</td><td style='text-align: center; word-wrap: break-word;'>Plant data</td><td style='text-align: center; word-wrap: break-word;'>Simulation result</td><td style='text-align: center; word-wrap: break-word;'>Error (%)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW (g/mol)</td><td style='text-align: center; word-wrap: break-word;'>108,800</td><td style='text-align: center; word-wrap: break-word;'>116,461</td><td style='text-align: center; word-wrap: break-word;'>6.96</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN (g/mol)</td><td style='text-align: center; word-wrap: break-word;'>104,310</td><td style='text-align: center; word-wrap: break-word;'>99,507</td><td style='text-align: center; word-wrap: break-word;'>4.60</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SBS production rate (kg/min)</td><td style='text-align: center; word-wrap: break-word;'>910</td><td style='text-align: center; word-wrap: break-word;'>900.95</td><td style='text-align: center; word-wrap: break-word;'>0.99</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_891_781_1213.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 6.75 Final kinetic parameters for the tri-block SBS copolymer.</div>


---

<!-- PDF page 360 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>MSE (Basis)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-5</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>-4</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>97</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>99</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>101</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>102</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>103</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>104</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>106</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>107</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>108</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>109</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>111</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>112</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>113</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>114</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>116</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>117</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>118</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>119</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>900</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.76a Feed mass flow rate profiles for styrene and butadiene.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (min)</th><th style='text-align: center;'>188.04000 (kWh)</th><th style='text-align: center;'>188.04000 (kWh/min)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>22500</td><td style='text-align: center;'>40000</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>22500</td><td style='text-align: center;'>40000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>22500</td><td style='text-align: center;'>40000</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>22500</td><td style='text-align: center;'>40000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>22500</td><td style='text-align: center;'>40000</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>16000</td><td style='text-align: center;'>38000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>40000</td><td style='text-align: center;'>60000</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>80000</td><td style='text-align: center;'>85000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>100000</td><td style='text-align: center;'>90000</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>108000</td><td style='text-align: center;'>92000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.76b MWW and MWN of tri-block SBS copolymer.</div>


By plotting selected items from the RBATCH profile results, we see in Figures 6.76a–6.76d: (1) feed mass flow rate profiles of styrene and butadiene; (2) MWW and MWN of the resulting copolymer; (3) variation of mole composition of monomers and SBS copolymer within the reactor as a function of reaction times; and (4) accumulated mass of monomers and SBS copolymer within the reactor as a function of reaction times. We save the completed simulation as WS6.2 SBC_Semi-Batch_Good.bkp.

Model Application What happens if we change the amount of initiator addition in Figure 6.73c during minutes 11 to 12 of the batch? Table 6.13 compares the results.

Increasing the initiator addition significantly decreases the resulting molecular weights of the SBS copolymer, but it only slightly affects the mass flow rate of copolymer produced.

---

<!-- PDF page 361 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-axis</th><th style='text-align: center;'>27182ME</th><th style='text-align: center;'>30743EN</th><th style='text-align: center;'>3200</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>97</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>99</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>101</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>102</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>103</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>104</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>106</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>107</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>108</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>109</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>111</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>112</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>113</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>114</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>116</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>117</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>118</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>119</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.76c Variation of mole compositions of monomers and SBS copolymer within the reactor as a function of reaction times.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (min)</th><th style='text-align: center;'>371959.1g</th><th style='text-align: center;'>817429.9g</th><th style='text-align: center;'>100.0000</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.76d Accumulated mass of monomers and SBS copolymer within the reactor as a function of reaction times.</div>


<div style="text-align: center;">Table 6.13 Effect of the amount of initiator BuLi-6 addition on simulation results.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Initiator BuLi-6 addition from 11 to 12 min (kg)</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW (g/mol)</td><td style='text-align: center; word-wrap: break-word;'>116,461</td><td style='text-align: center; word-wrap: break-word;'>61,977</td><td style='text-align: center; word-wrap: break-word;'>43,667</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN (g/mol)</td><td style='text-align: center; word-wrap: break-word;'>99,507</td><td style='text-align: center; word-wrap: break-word;'>49,671</td><td style='text-align: center; word-wrap: break-word;'>34,460</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SBS copolymer production (kg/min)</td><td style='text-align: center; word-wrap: break-word;'>900.95</td><td style='text-align: center; word-wrap: break-word;'>901.818</td><td style='text-align: center; word-wrap: break-word;'>902.795</td></tr></table>

##### 6.2.5.10 Semi-Batch Reactor for Producing a Tri-Block SBS Copolymer by a Literature Batch-Sequence Recipe

Sirohi and Ravindranath [18] simulated the batch-sequence recipe of Hsieh [17, 24] to produce a tri-block SBS copolymer consisting of the following batch-sequence

---

<!-- PDF page 362 -->

recipe: (1) charge the batch reactor with styrene and solvent; (2) add a BuLi initiator and allow styrene to polymerize for an hour; (3) add butadiene and let it also polymerize for an hour; (4) add a coupling agent (COUPLING), such as iodine, and allow 40 minutes for coupling; and (5) add a terminating agent or a short stopper (S-STOP), such as water, to kill the remaining initiator and live polymer chains. We simulate this semi-batch reactor operation below.

Component List, Reactor Flowsheet, and Feed and Operating Conditions We open the file, WS6.2 SBC_Semi-Batch_Good.bkp, and save it with a new name, WS6.2 SBC_Semi-Batch_Hsieh.bkp. We slightly modify the flowsheet as shown in Figure 6.77.

Figure 6.78 shows the modified component list. Note the coupling agent (COU-PLING), iodine, and the terminating agent or short stopper (S-STOP), water. We use the unit system of METCATM, with temperature at °C and pressure at atm.

Table 6.14 specifies our initial charge and continuous feeds to the batch reactor.

Figures 6.79a–6.79c specify the semi-batch reactor. The valid reactor phase is the liquid phase. The reaction set is R-1, displayed in Figures 6.80a and 6.80b.

After running the simulation, we can plot the time-dependent profiles of feeds and SBS copolymer product by plotting the “profiles” section of the semi-batch reactor, BATCH. Figures 6.81a and 6.81b illustrate the profiles of the mass flow rates of feed components.

Figure 6.82 shows the accumulated reactor mass varying with time, and Figure 6.83 illustrates the resulting MWN and MWW of the SBS copolymer product.

This concludes the current workshop. We save the simulation as WS7.2 SBC_Semi-Batch_Hsieh.bkp.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_829_763_1204.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 6.77 A modified flowsheet with the addition of feed streams, COUPLING and S-STOP.</div>


---

<!-- PDF page 363 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_159_782_575.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.78 Modified component list for WS6.2 SBC_Semi-Batch_Hsieh.</div>


<div style="text-align: center;">Table 6.14 Stream specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (atm)</td><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Composition (mass fraction)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Charge</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>25,000</td><td style='text-align: center; word-wrap: break-word;'>styrene = 0.04762, solvent = 0.95238</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Styrene</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>760.02</td><td style='text-align: center; word-wrap: break-word;'>styrene = 0.99998, s-stop = 2E-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Butadiene</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1136</td><td style='text-align: center; word-wrap: break-word;'>butadiene = 0.995, s-stop = 0.005</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Initiator</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>13.75</td><td style='text-align: center; word-wrap: break-word;'>buLi-6 = 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Solvent</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>40.02</td><td style='text-align: center; word-wrap: break-word;'>hexane = 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Coupling</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>22.264</td><td style='text-align: center; word-wrap: break-word;'>coupling = 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Activator</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>72</td><td style='text-align: center; word-wrap: break-word;'>modifier = 0.99997, s-stop = 3E-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S-Stop</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>s-stop = 1</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1033_783_1214.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.79a Specifications of the semi-batch reactor.</div>


---

<!-- PDF page 364 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_157_813_396.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.79b Specifications of stop criterion and operational times.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_447_811_658.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 6.79c Sequential addition of continuous feeds as a function of operational time.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_709_623_1231.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 6.80a Specifications of Species for the reaction set.</div>


---

<!-- PDF page 365 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Main Flowsheet</td><td style='text-align: center; word-wrap: break-word;'>Batch-Batch1</td><td style='text-align: center; word-wrap: break-word;'>Profile</td><td style='text-align: center; word-wrap: break-word;'>Control Panel</td><td style='text-align: center; word-wrap: break-word;'>Batch-Batch2</td><td style='text-align: center; word-wrap: break-word;'>Setup</td><td style='text-align: center; word-wrap: break-word;'>Reactions R1 (DMCs)</td><td colspan="7">+</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>☑ Spokes</td><td style='text-align: center; word-wrap: break-word;'>☑ Reactions</td><td style='text-align: center; word-wrap: break-word;'>☑ False Contents</td><td style='text-align: center; word-wrap: break-word;'>Options</td><td style='text-align: center; word-wrap: break-word;'>Comments</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Site 1</td><td style='text-align: center; word-wrap: break-word;'>Camp 1</td><td style='text-align: center; word-wrap: break-word;'>Site 2</td><td style='text-align: center; word-wrap: break-word;'>Camp 2</td><td style='text-align: center; word-wrap: break-word;'>Site 3</td><td style='text-align: center; word-wrap: break-word;'>Pre-Exp (1)</td><td style='text-align: center; word-wrap: break-word;'>Act-Temp (1)</td><td style='text-align: center; word-wrap: break-word;'>Pre-Exp (2)</td><td style='text-align: center; word-wrap: break-word;'>Act-Temp (2)</td><td style='text-align: center; word-wrap: break-word;'>Ref. Temp</td><td style='text-align: center; word-wrap: break-word;'>Other</td><td style='text-align: center; word-wrap: break-word;'>Asso. No.</td><td style='text-align: center; word-wrap: break-word;'>Coat &amp; Coat &amp;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Enter</td><td style='text-align: center; word-wrap: break-word;'>col/med</td><td style='text-align: center; word-wrap: break-word;'>L/fr</td><td style='text-align: center; word-wrap: break-word;'>col/med</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>INF-DISSOC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BUU-6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BUU-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>2e+26</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 SYTRENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUTADEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BUTADEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUTADEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN-1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 SYTRENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>PROORGATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 STY-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BUTADEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>PROORGATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>PROORGATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BUTADEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>PROORGATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>STYRENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.1788</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>ASSOCIATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 STY-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>ASSOCIATION</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>EXCH-AGENT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 STY-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3 COUPUNG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>EXCH-AGENT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3 COUPUNG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>TERM-AGENT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 STY-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5-STOP</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>TERM-AGENT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 BUL-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5-STOP</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 6.80b Specifications of reaction-rate constants.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Mass-flow (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>11500</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.81a Profiles of the mass flow rates of feed components.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Mass-flow (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>115</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.81b Profiles of the mass flow rates of feed components (continued).</div>


---

<!-- PDF page 366 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>STYRENE kg</th><th style='text-align: center;'>BUTADIEN kg</th><th style='text-align: center;'>SBR kg</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1100</td><td style='text-align: center;'>1100</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>800</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1200</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>600</td><td style='text-align: center;'>1300</td><td style='text-align: center;'>1300</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>400</td><td style='text-align: center;'>1400</td><td style='text-align: center;'>1400</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>200</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>100</td><td style='text-align: center;'>1600</td><td style='text-align: center;'>1600</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1700</td><td style='text-align: center;'>1700</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1900</td><td style='text-align: center;'>1900</td></tr>
    <tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2100</td><td style='text-align: center;'>2100</td></tr>
    <tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2400</td><td style='text-align: center;'>2400</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2500</td><td style='text-align: center;'>2500</td></tr>
    <tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2600</td><td style='text-align: center;'>2600</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2700</td><td style='text-align: center;'>2700</td></tr>
    <tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2800</td><td style='text-align: center;'>2800</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>2900</td><td style='text-align: center;'>2900</td></tr>
    <tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3000</td><td style='text-align: center;'>3000</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3100</td><td style='text-align: center;'>3100</td></tr>
    <tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3200</td><td style='text-align: center;'>3200</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3400</td><td style='text-align: center;'>3400</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3500</td><td style='text-align: center;'>3500</td></tr>
    <tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3600</td><td style='text-align: center;'>3600</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3700</td><td style='text-align: center;'>3700</td></tr>
    <tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3800</td><td style='text-align: center;'>3800</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3900</td><td style='text-align: center;'>3900</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.82 The accumulated reactor mass varying with time.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>SBR MWN MWN</th><th style='text-align: center;'>SBR MWW MWN</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>27500</td><td style='text-align: center;'>27500</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>44500</td><td style='text-align: center;'>44500</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>46000</td><td style='text-align: center;'>46000</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>45500</td><td style='text-align: center;'>45500</td></tr>
    <tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>44500</td><td style='text-align: center;'>44500</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>47000</td><td style='text-align: center;'>47000</td></tr>
    <tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>50500</td><td style='text-align: center;'>50500</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>51500</td><td style='text-align: center;'>51500</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>51500</td><td style='text-align: center;'>51500</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>52500</td><td style='text-align: center;'>52500</td></tr>
    <tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>54000</td><td style='text-align: center;'>54000</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>55500</td><td style='text-align: center;'>55500</td></tr>
    <tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>57000</td><td style='text-align: center;'>57000</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>58500</td><td style='text-align: center;'>58500</td></tr>
    <tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>60000</td><td style='text-align: center;'>60000</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>61500</td><td style='text-align: center;'>61500</td></tr>
    <tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>63000</td><td style='text-align: center;'>63000</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>64500</td><td style='text-align: center;'>64500</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>65500</td><td style='text-align: center;'>65500</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>66500</td><td style='text-align: center;'>66500</td></tr>
    <tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>67500</td><td style='text-align: center;'>67500</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>68000</td><td style='text-align: center;'>68000</td></tr>
    <tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>68500</td><td style='text-align: center;'>68500</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>69000</td><td style='text-align: center;'>69000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6.83 The MWN and MWW of the SBS copolymer product. Note the noticeable effects of adding butadiene from 1 to 1.1 hr and terminating agent (S-Stop) from 2.65 to 2.68 hr. The effect of adding a coupling agent (COUPLING) from 2 to 2.1 hr is not noticeable.</div>


## References

1 Soares, J.B.P. and McKenna, T.F.L. (2012). Polyolefin Reaction Engineering. Weinheim: Wiley-VCH.

2 Odian, G. (2004). Principles of Polymerization, 4e. New York: Wiley.

3 Schaller, C. (2021). Synthetic Methods in Polymer Chemistry. https://employees.csbsju.edu/cschaller/Advanced/Polymers/SAanionic.html (accessed 4 June 2021).

4 Lohse, D.J. (2000). Polyolefins. In: Applied Polymer Science:21st Century, Chapter 6 (ed. C. Craver and C. Carraher), 73–91. New York: Elsevier.

5 Carraher, C. (2017). Carraher's Polymer Chemistry, 10e. Boca Raton, FL: CRC Press.

6 Stevens, M. (1998). Polymer Chemistry. Oxford: Oxford University Press.

7 Lodge, T.P. and Hiemenz, P.C. (2020). Polymer Chemistry, 3e. London: Taylor & Francis.

---

<!-- PDF page 367 -->

8 Seavey, K.C. and Liu, Y.A. (2009). Step-Growth Polymerization Process Modeling and Product Design. New York: Wiley.

9 Hui, A.W. and Hamielec, A.E. (1972). Thermal polymerization of styrene at high conversions and temperatures: an experimental study. Journal of Applied Polymer Science 16: 749.

10 Kirchner, K. and Riederle, K. (1983). Thermal polymerization of styrene - the formation of oligomers and intermediates, 1. Discontinuous polymerization up to high conversions. Die Angewandte Makromolekulare Chemie 111: 1–16.

11 Reintelen, T., Riederle, K., and Kirchner, K. (1983). Transfer of kinetics models from batch to continuous reactors with special regard to the formation of oligomers and the effect of retards during styrene polymerization. In: Polymer Reaction Engineering: Influence of Reaction Engineering on Polymer Properties (ed. K.H. Reinchert and W. Geisseler), 271–286. New York: Hanser Publishers.

12 Aspen Technology, Inc. (2017). Application B1 - Polystyrene Bulk Polymerization by Thermal Initiation. Aspen Polymers V8.4: Examples and Applications, pp. 97–108.

13 Boks, C.P., Orbey, H., and Chen, C.C. (1999). Properly model polymer processes. Chemical Engineering Progress 95 (4): 39.

14 Aspen Technology, Inc. (2021). Initiator Decomposition Rate Parameters. Aspen Polymers V12.1.

15 Chang, C.C., Miller, J.W., and Schorr, G.R. (1990). Fundamental modeling in anionic polymerization processes. Journal of Applied Polymer Science 39: 2395–2417.

16 Chang, C.C., Halasa, A.F., Miller, J.W., and Hsu, J.W. (1994). Modeling studies of the controlled anionic copolymerization of butadiene and styrene. Polymer International 33: 151–159.

17 Hsieh, H.L. and Quirk, R.P. (1996). Anionic Polymerization – Principles and Practical Applications. New York: Marcel Dekker, Inc.

18 Sirohi, A. and Ravindranath, K. (1999). Modeling of Ionic Polymerization Processes: Styrene and Butadiene. Houston, TX: AIChE Spring Meeting.

19 Design Institute for Physical Property Research (DIPPR), American Institute of Chemical Engineer (2003). Evaluated Process Design Data, DIPPR Project 801. New York: AIChE.

20 Caruthers, J.M., Choa, L.C., Venkatasubramanian, V. et al. (1998). Handbook of Diffusion and Thermal Properties of Polymers and Polymer Solutions. New York: American Institute of Chemical Engineers.

21 Aspen Technology, Inc. (2017). Application B6 – Styrene Butadiene Ionic Polymerization Processes. Aspen Polymers V8.4: Examples and Applications, pp. 159–166.

22 Aspen Technology, Inc. (2021). Aspen Polymers V12.1, Reaction Kinetic Scheme (Ionic), online help.

23 Brandup, J., Immergut, E.H., and Grulke, E.A. (ed.) (1999). Polymer Handbook. New York: Wiley.

24 Hsieh, H.H. (1976). Synthesis of radial thermoplastic elastomers. Rubber Chemistry and Technology 49: 1305–1310.

---

<!-- PDF page 368 — MISSING, not yet parsed -->
