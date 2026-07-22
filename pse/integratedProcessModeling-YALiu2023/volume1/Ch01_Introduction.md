# 1. Introduction to Integrated Process Modeling

<!-- PDF page 49 -->

## Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing

This chapter begins by introducing the segment-based modeling of polymerization processes developed by Aspen Technology in US Patent 5,687,090 in 1997 by Chau-Chyun Chen and Michael Barrera et al. [1]. We are happy to note that the second author of this groundbreaking patent, Michael Barrera, was a student of senior design and undergraduate research courses at Virginia Tech taught by the senior author of this book. Section 1.1 explains the component types in polymer process modeling, the concept of moments, and some basic polymer attributes (such as the number-average molecular weight, MWN, the weight-average molecular weight, MWW, and the polydispersity index, PDI). Section 1.2 presents a hands-on workshop on using Aspen Plus (which includes Aspen Polymers) to find the resulting stream attributes after mixing two copolymer streams. Section 1.3 presents a workshop for a simplified simulation model of a slurry high-density polyethylene (HDPE) process. We explain the workflow for developing a polymer process simulation model. In explaining this development, we pose motivating questions that demonstrate the significant advantages of having a process simulation model as the quantitative foundation for sustainable design and optimization, process improvement, capacity expansion, and new product design. Section 1.4 covers some examples of industrial and potential applications of polymer process modeling, advanced control, and data analytics, along with their integrated applications to optimizing polyolefin manufacturing. This chapter ends with a reference section.

### 1.1 Segment-Based Modeling of Polymerization Processes: Component Characterization and Polymer Attributes

#### 1.1.1 Component Types in Polymer Process Modeling

There are three types of components in simulating a polymer processes.

(1) Segments: They represent a repeat unit, end group, or branch point and have a well-defined molecular structure. You can see all the segments available using Aspen Plus online help and searching for “Segment databank components.”

---

<!-- PDF page 50 -->

 $$ \begin{aligned}\left|\begin{array}{c}\mathrm{CH}_{2}-\mathrm{CH}_{2}\\\end{array}\right|-\mathrm{CH}_{2}-\mathrm{CH}_{2}\left|\begin{array}{c}\mathrm{CH}_{2}-\mathrm{CH}_{2}\\\end{array}\right|-\mathrm{CH}_{2}-\mathrm{CH}_{2}\left|\begin{array}{c}\mathrm{CH}_{2}-\mathrm{CH}_{2}\\\end{array}\right|\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_137_805_476.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">Figure 1.1 (a) REPEAT segment: Ethylene-R; (b) END segment: Ethylene-E; (c) BRANCH3 segment: Segment S1 (end type), S1e, reacts with segment 2 (repeat unit), S2r, and converts the repeat unit, S2r, to a branch point with three branches, S2b3, and a repeat unit, S4r; (d) BRANCH4 segment: Butadiene-R-3.</div>


• Type REPEAT (-R): Repeat units within the polymer chain. Example: C2H4R or Ethylene-R in polyethylene. See Figure 1.1a

• Type END (-E): End units terminating the polymer chain. Example: C2H5-E or Ethylene-E in polyethylene. See Figure 1.1b

- Type BRANCH3: Branch points attached to three branches. Branch formation occurs when a polymer molecule attaches to another polymer chain, converting a repeat unit to a branch point. Monomers can also react with repeat units to initiate branch formation. Aspen Plus online help gives the illustration in Figure 1.1c.

• Type BRANCH4: Branch points attached to four branches. Example: C4H6-R-2 or butadiene-R-3 in polybutadiene. See Figure 1.1d

(2) Oligomers: They have a fixed structure or contain a known number of segments. They do not have changing properties during a simulation and do not require component attributes. To specify an oligomer in Aspen Polymers, we follow the path: Properties → Components, including the oligomer as a component → Polymers → Oligomers → Identify the name of oligomer specified in Components and add the number of segments.

(3) Polymers: After defining your name for the polymer, identify the polymer component name and alias by searching the Aspen Plus online help for “Polymer databank components”; if the desired component is not available within the databank, specify the component name as “generic-polymer-component” and use an alias of “polymer” (see an illustration in Workshop 2.2).

We note that polymers do not have fixed molecular weights. It is typical to use an apparent molecular weight equal to the molecular weight of a polymer repeat unit. To avoid confusion, we should specify and view polymer properties on a mass basis. This implies that we should choose the flow basis as “mass” when we open a

---

<!-- PDF page 51 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_150_781_364.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.2 Setting a mass flow basis for polymer process simulation.</div>


new Aspen Plus simulation by following the path: Aspen Plus → New → Chemical with Metric Units → Create → Simulation Environment → Setup → (1) Global unit set = METCBAR; (2) Flow basis = Mass. See Figure 1.2.

#### 1.1.2 Concept of Moments and Some Basic Polymer Attributes

Figure 1.3 shows the structures of the repeat units for polyethylene (PE) and ethylene-vinyl-acetate (EVA) copolymer. In the figure, PE is a homopolymer and contains only one type of repeat unit, and copolymer EVA includes two types of repeat units.

In a mixture of PE molecules, each PE molecule may have a different number of repeat units, n. Some have a large n (or degree of polymerization, DP), meaning that they are very long polymer chains; some have a small n, meaning that they are short polymer chains. Particularly short polymers, say,  $ n \leq 10 $, are called oligomers.

We typically represent the molecular weight distribution (MWD) by a plot of weight fraction versus molecular weight ( $ w_{i} $ versus  $ M_{i} $). We quantify the molecular weight distribution using moments of the distribution [2].

What are moments? Consider a polymer sample illustrated in Figure 1.4 in which each circle in a polymer chain represents a repeat unit, such as  $ -C_{2}H_{4}- $.

One chain has three segments, one has four, and one has five. We use  $ P_{n} $ to describe each polymer chain, where n is the number of segments in a chain. So, our sample

<div style="text-align: center;">Figure 1.3 Repeat units for polyethylene (PE) and ethylene-vinyl-acetate (EVA) copolymer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_434_990_799_1110.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Figure 1.4 A polymer sample.</div>


---

<!-- PDF page 52 -->

contains $P_{3}$, $P_{4}$, and $P_{5}$. We use a bracket to represent the concentration for each polymer chain. In our example, we have $[P_{3}]=[P_{4}]=[P_{5}]=1$, because we only have one for each chain. What is the number-average degree of polymerization (DPN) of our sample? We write:

 $$ \mathrm{DPN}=\frac{\text{total number of segments}}{\text{total number of chains}}=\frac{3+4+5}{3}=4 $$ 

Another way to write this equation is

 $$ \mathrm{DPN}=\frac{3\times\left[P_{3}\right]+4\times\left[P_{4}\right]+5\times\left[P_{5}\right]}{\left[P_{3}\right]+\left[P_{4}\right]+\left[P_{5}\right]}=\frac{3\times1+4\times1+5\times1}{3}=4 $$ 

We can generalize this equation to write

 $$ \mathrm{DPN}=\frac{\sum_{n}n[P_{n}]}{\sum_{n}[P_{n}]}=\frac{3\times[P_{3}]+4\times[P_{4}]+5\times[P_{5}]}{[P_{3}]+[P_{4}]+[P_{5}]}=\frac{3\times1+4\times1+5\times1}{3}=4 $$ 

This defining equation for DPN based on a summation ratio works for any sample of polymer chains. Let us now define a moment of molecular weight distribution as

 $$ \mu_{i}=\sum_{n}n^{i}\big[P_{n}\big] $$ 

We can rewrite the DPN equation in terms of moments now:

 $$ \mathrm{DPN}=\frac{\sum_{n}n[P_{n}]}{\sum_{n}[P_{n}]}=\frac{\sum_{n}n^{1}[P_{n}]}{\sum_{n}n^{0}[P_{n}]}=\frac{\mu_{1}}{\mu_{0}} $$ 

In practice, we only use at most three moments in polymer process modeling. These are

 $$ \mathrm{Zeroth moment~(ZMOM):}\mu_{0}=\sum_{n}\left[P_{n}\right] $$ 

 $$  First moment(FMOM):\mu_{1}=\sum_{n}n\big[P_{n}\big] $$ 

 $$ \mathrm{Second moment~(SMOM):}\mu_{2}=\sum_{n}n^{2}\big[P_{n}\big] $$ 

The zeroth moment adds up the number of all chains in the system, so it is a total polymer concentration or a total mole flow of the polymer. The first moment is the total number of chain segments or total segment concentration or the total segment mole flow in the system. The second moment is similar to the first moment, but the longer chain concentrations are weighted more because the number of segments, n, is squared.

For our example, we find:

 $$ \mu_{0}=\sum_{n}\left[P_{n}\right]=1+1+1=3 $$ 

 $$ \mu_{1}=\sum_{n}n\big[P_{n}\big]=3\times1+4\times1+5\times1=12 $$ 

 $$ \mu_{2}=\sum_{n}n^{2}\big[P_{n}\big]=3^{2}\times1+4^{2}\times1+5^{2}\times1=50 $$ 

---

<!-- PDF page 53 -->

We define the weight-averaged degree of polymerization (DPW) as

 $$ \mathrm{DPW}=\frac{\sum_{n}n^{2}[P_{n}]}{\sum_{n}n^{1}[P_{n}]}=\frac{\mu_{2}}{\mu_{1}}=\frac{50}{12}=4.17 $$ 

We define the PDI as

 $$ \mathrm{PDI}=\frac{\mathrm{DPW}}{\mathrm{DPN}}=\frac{\mu_{2}/\mu_{1}}{\mu_{1}/\mu_{0}}=\frac{\mu_{2}\mu_{0}}{\mu_{1}^{2}}=\frac{50\times3}{12^{2}}=1.04 $$ 

Lastly, we can relate DPN and DPW to MWN and MWW by multiplying the average segment molecular weight (MWSEG):

 $$ \mathrm{MWN}=\mathrm{DPN}\times\mathrm{MWSEG} $$ 

 $$ \mathrm{MWW}=\mathrm{DPW}\times\mathrm{MWSEG} $$ 

Combining Eqs. (1.11) and (1.12) gives the standard definition of PDI:

 $$ \mathrm{PDI}=\frac{\mathrm{DPW}}{\mathrm{DPN}}=\frac{\mathrm{MWW}}{\mathrm{MWN}} $$ 

Aspen Polymers includes a large set of polymer attributes that are used by specific polymerization kinetic models [1]. We will discuss additional polymer attributes for different types of polymerization processes beginning in Chapter 4.

#### 1.1.3 Stream Initialization and Basic Polymer Attributes

Following [1], we illustrate some basic stream initialization calculations for a feed stream of EVA (ethylene-vinyl-acetate) copolymer. The feed flow rate is 1 kg/s; the copolymer contains 60 mol% of ethylene (E2) and 40 mol% of vinyl acetate (VA); and the copolymer molecular weights are MWN = 20,000 and MWW = 90,000.

Given the molecular weights of E2 and VA being 28.05 and 86.09 g/mol, respectively, and the segment mole fractions (SFRAC $ _{i} $)

 $$ x_{\mathrm{E}2}=0.6\qquad x_{\mathrm{V A}}=0.4 $$ 

we find the average segment molecular weight (MWSEG) as

 $$ \begin{aligned}MWSEG&=\sum_{i}SFRAC_{i}M_{i}=0.6\times28.05+0.4\times86.09=51.266g/mol\\&=51.266kg/kmol\end{aligned} $$ 

We find the mole flow of each segment as follows:

 $$ \mathrm{SFLOW(E2)=[(1\mathrm{~kg/s})/(51.266\mathrm{~kg/kmol)}]\times0.6=0.011704\mathrm{~kmol/s}} $$ 

 $$ \mathrm{SFLOW(VA)}=[(1\mathrm{kg/s})/(51.266\mathrm{kg/kmol})]\times0.4=0.007802\mathrm{kmol/s} $$ 

The first moment of polymer (FMOM) or  $ \lambda_{1}= $ total segment mole flow rate = 0.019506 kmol/s.

Next, given MWN = 20,000 and MWW = 90,000 kg/kmol, we find the PDI as

 $$ \mathrm{PDI}=\mathrm{MWW}/\mathrm{MWN}=90,000/20,000=4.5 $$ 

---

<!-- PDF page 54 -->

To find the DPN, we use Eq. (1.11):

 $$ \mathrm{MWN}=\mathrm{DPN}\times\mathrm{MWSEG}\quad20,000=\mathrm{DPN}\times51.266\rightarrow\mathrm{DPN}=390.12 $$ 

Likewise, we find the weight-average molecular weight using Eq. (1.12):

 $$ \mathrm{MWW}=\mathrm{DPW}\times\mathrm{MWSEG}\quad90,000=\mathrm{DPW}\times51.266\rightarrow\mathrm{DPW}=1755.55 $$ 

We relate the DPN to the zeroth and first moments according to Eq. (1.5), noting that the zeroth moment  $ \mu_{0} $ represents the total polymer mole flow rate:

 $$ \mathrm{DPN}=\frac{\mu_{1}}{\mu_{0}}\rightarrow390.12=0.019506/\mu_{0}\rightarrow\mu_{0}=0.00005\mathrm{kmol/s} $$ 

Similarly, we find the second moment of polymer (SMOM) or  $ \mu_{2} $ by Eq. (1.9):

 $$ \mathrm{DPW}=\frac{\mu_{2}}{\mu_{1}}=\frac{\mu_{2}}{0.19506}=1755.55 $$ 

This gives  $ \mu_{2} $ or SMOM as 34.2438 kmol/s.

This example also enables us to demonstrate that we can calculate the total polymer molar flow rate (that is, zeroth moment  $ \mu_{0} $) in a stream from the mass flow rate of the stream and the MWN:

 $$ \begin{aligned}\mu_{0}&=\frac{mass flow rate of the polymer stream}{number-average molecular weight}\\&=\frac{1kg/s}{20,000kg/kmol}=0.00005kmol/s\end{aligned} $$ 

We summarize the stream initialization results in Table 1.1.

<div style="text-align: center;">Table 1.1 Stream initialization results for EVA copolymer example</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream variable</td><td style='text-align: center; word-wrap: break-word;'>Value</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/s)</td><td style='text-align: center; word-wrap: break-word;'>1 (given)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DPN</td><td style='text-align: center; word-wrap: break-word;'>390.12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DPW</td><td style='text-align: center; word-wrap: break-word;'>1755.55</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'>4.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'>20,000 (given)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'>90,000 (given)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZMOM (kmol/s)</td><td style='text-align: center; word-wrap: break-word;'>0.00005</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FMOM (kmol/s)</td><td style='text-align: center; word-wrap: break-word;'>0.019506</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SMOM (kmol/s)</td><td style='text-align: center; word-wrap: break-word;'>34.2438</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFLOW (kmol/s), E2</td><td style='text-align: center; word-wrap: break-word;'>0.011704</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFLOW (kmol/s), VA</td><td style='text-align: center; word-wrap: break-word;'>0.007802</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFRAC, E2</td><td style='text-align: center; word-wrap: break-word;'>0.6 (given)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFRAC, VA</td><td style='text-align: center; word-wrap: break-word;'>0.4 (given)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWSEG (kg/kmol)</td><td style='text-align: center; word-wrap: break-word;'>51.260</td></tr></table>

---

<!-- PDF page 55 -->

#### 1.2 Workshop 1.1: Finding the Resulting Stream Attributes After Mixing Two Copolymer Streams

#### 1.2.1 Objective

This workshop demonstrates how to use Aspen Plus to do stream initialization calculations that we did manually in Section 1.1.3, and how to find the stream attributes (e.g. MWN, MWW, and PDI) resulting from manipulating (e.g. mixing) two or more streams.

#### 1.2.2 Problem Statement

Consider mixing two EVA copolymer streams at 150 °C and 1 bar: (1) stream EVA80: ethylene segment mole fraction = 0.8; mass flow rate = 1.0 kg/s; MWN = 2000 and MWW = 5000. (2) stream EVA50: ethylene segment mole fraction = 0.5; mass flow rate = 1.0 kg/s; MWN = 20,000 and MWW = 50,000. Find the polymer attributes (MWN, MWW, and PDI) of the resulting mixed stream (EVAMIXED). Investigate the effect of varying the mass flow rate of stream EVA60 from 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.33, 0.5, 0.7, 1, 2.5, 5, 7.5, 10, 50, 100, 200, 500, 1000, 2000, and 10,000 on the resulting MWN, MWW, and PDI.

#### 1.2.3 Process Flowsheet

Figure 1.5 shows a simple mixing flowsheet. We save the simulation file as WS 1.1 Stream Attribute Calculations.bkp.

We note that the flowsheet uses our own stream names, EVA80 and EVA50, and block name MIXER. To make this happen, we follow the path: File → Options → Flowsheet → Stream and block labels → Unclick “Automatically assign block label with prefix B” and “Automatically assign stream label with prefix S” → Apply. See Figure 1.6.

#### 1.2.4 Unit System, Components, and Characterization of Copolymers

We choose the unit system METCBAR and define the components as seen in Figure 1.7. To access or create the unit set METCBAR, we follow the path: Properties → Setup → Unit Set → New: Create new ID → Enter ID “METCBAR” → Standard → Copy from MET → Change temperature unit from K to C and change pressure unit from atm to bar (see Figure 1.7). After these changes, we follow the

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_1093_619_1222.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 1.5 Process flowsheet.</div>


---

<!-- PDF page 56 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_146_598_359.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 1.6 Option to assign your own stream and block names.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_443_811_657.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.7 Creating a METCBAR unit set based on a MET unit set.</div>


path to specify the unit set: Setup→Specifications→Global unit set→Choose "METCBAR."

This workshop deals with segment-based species accounting and calculation of basic polymer attributes and does not involve polymerization kinetics. We do not include other required components for free radical polymerization of the EVA copolymer, such as the initiator. We discuss EVA copolymerization in Chapter 4.

Figure 1.8 shows the component specification and the enterprise databases that we choose pure component databank PURE37, segment and polymer databanks (SEGMENT and POLYMER), and polymer perturbed-chain statistical fluid theory equation of state (POLYPCSF) as our property method. We will discuss POLYPCSF in Chapter 2.

Next, we follow the path:

Properties → Components → Polymers → Characterization → Segments → Specify both E2-R and VA-R as repeat units. See Figure 1.9.

Continuing with the path: Polymers → Characterization → Polymers, we choose the built-in attribute group, free-radical selection for our copolymer, POLYEVA, as seen in Figure 1.10.

We see in Figure 1.10 the “Edit” button. Clicking on the button shows a complete listing and selection option for polymer attributes for free radical polymerization. We specifically choose the following attributes that we explained in Sections 1.1.2 and 1.1.3: SFRAC, SFLOW, DPN, DPW, MWN, MWW, ZMON, FMON, and SMON by canceling the selections of LDPN, LZMON, ..., LPFRAC and then clicking on the

---

<!-- PDF page 57 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_147_782_589.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.8 Component specifications and enterprise database selection.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_657_564_859.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">Figure 1.9 Specification of segment type.</div>


“Close” button. This results in our desired polymer attribute selection as seen on the left side of Figure 1.11.

#### 1.2.5 Property Method and Property Parameters for Components

As we will discuss in detail in Chapter 2, Aspen Plus refers to a property method as a collection of models and methods for calculating phase equilibria and various physical properties, such as density, enthalpy, viscosity, and thermal conductivity. For modeling the EVA copolymer production at typically very high pressures (see Table 4.10), we recommend the use of the polymer perturbed chain, statistical fluid theory (POLYPCSF) equation of state as our property method, which we will discuss in detail in Sections 2.8 and 2.9. This property method requires some pure-component parameters and binary interaction parameters between two components. However, as the current workshop focuses only on stream initialization,

---

<!-- PDF page 58 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_150_743_401.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 1.10 Default selection of polymer attributes for free radical polymerization.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_466_743_818.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 1.11 Selection of desired polymer attributes.</div>


simple mass balance, and basic polymer attribute calculations, instead of phase equilibrium as well as energy balance calculations, we do not need to input these property parameter values.

Figure 1.12 illustrates all we need in regard to specifying the property method for the current workshop.

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_1027_599_1221.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 1.12 Specification of property method.</div>


---

<!-- PDF page 59 -->

#### 1.2.6 Specifications of Streams and Blocks

Following the path: Simulation → Streams → EVA80 → Specifications and Component Attributes, we complete the inputs for EVA80 copolymer. See Figure 1.13.

We specify EVA50 copolymer in the same way. Figure 1.14 shows the specification of the mixer block.

In Aspen Plus, a pressure specification of zero means that both the inlet and outlet pressures of the mixer are identical, and there is a zero pressure drop. Should this pressure specification be a positive value, it indicates an outlet pressure.

Next, we define a sensitivity analysis by following the path: Simulation → Model Analysis Tools → Sensitivity → New → S-1 → Input → (1) Vary → New → Manipulated (independent) variable 1 → See Figure 1.15 (we input the manipulated

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_454_782_657.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.13 Specifications of EVA80 copolymer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_720_497_891.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Figure 1.14 Specification of the mixer block with zero pressure drop.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_959_781_1205.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.15 Step 1 of a sensitivity analysis – define the manipulated (independent) variable.</div>


---

<!-- PDF page 60 -->

variable limits as “list of values,” specifically 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.33, 0.5, 0.7, 1, 2.5, 5, 7.5, 10, 50, 100, 200, 500, 1000, 2000, and 10,000); (2) Define → New → (2a) Define dependent variable name MWN → See Figure 1.16; repeat this step to define dependent variables MWW and PDI following Figure 1.16, using the attribute names to MWW and PDI, respectively. (2b) Define dependent variable name FEVA80 → See Figure 1.17; repeat doing this step to define dependent variable FEVA50 following Figure 1.17 but change stream name to EVA50. (3) Tabulate → See Figure 1.18, where tabulated variable 4,

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_372_813_721.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.16 Step 2a of a sensitivity analysis – define the dependent variable MWN.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_787_811_1244.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.17 Step 2b of a sensitivity analysis – define the dependent variable FEVA80.</div>


---

<!-- PDF page 61 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_149_498_364.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Figure 1.18 Step 3 of a sensitivity analysis – define the tabulated variables.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_431_782_783.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.19 Control panel message of the completed simulation.</div>


FEVA80/(FEVA80 + FEVA50), calculates the mass fraction of copolymer EVA80 in the feed mixture of (EVA80 + EVA50).

To run the simulation, we follow the path: Home→Control panel→Run. The simulation completes easily, as seen in Figure 1.19.

To view the sensitivity analysis result, we follow the path: Simulation → Model analysis tools → Sensitivity → S-1 → Results. Figure 1.20 shows the tabulated

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1024_782_1246.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.20 Tabulated sensitivity analysis results.</div>


---

<!-- PDF page 62 -->

results. We note that the unit of the independent variable, Vary 1, is in kg/hr, instead of kg/sec. This follows that the default time unit for the unit system METCBAR is hour.

Next, we click the Custom button within the plot on the upper right corner of Figure 1.20 and specify the X-axis and Y-axis according to Figure 1.21 and then click OK. This gives the plot of Figure 1.22.

We can change the Y-axis to a single scale by placing our mouse in the middle of the plot on the computer screen, right-clicking to show a plot option box (as we see in Figure 1.22), and then choosing "Y-Axis Map," followed by choosing "Single Y-Axis" and "OK." This gives the plot of Figure 1.23.

Following the procedure to plot Figure 1.21, we plot PDI versus the mass flow rate of EVA copolymer in Figure 1.24. We click on the X-axis of Figure 1.24 to show the format (Min, Max, and Scale) of the X-axis above the plot. Changing the X-axis scale from “Linear” to “Log” gives the plot of Figure 1.25.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_531_647_796.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 1.21 Specifying a plot of MWN and MWW versus the mass fraction of EVA80 in the feed mixture of  $ (EVA80 + EVA50) $.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Feature</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Main Forecast</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Forecast</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Value</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate Rate Rate Rate Rate Rate</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>Max Outer Cover Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate Rate</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.22 MWN and MWW versus the mass fraction of EVA80 in the feed mixture of  $ (EVA80 + EVA50) $.</div>


---

<!-- PDF page 63 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>0.00</th><th style='text-align: center;'>S-1 - Results</th><th style='text-align: center;'>100</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.23 MWN and MWW versus the mass fraction of EVA80 in the feed mixture of  $ (EVA80 + EVA50) $ in a single Y-axis.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Parameter</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Min Number of Bands</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>Max Number of Bands</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.24 PDI versus the mass flow rate of EVA polymer.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Lig</th><th style='text-align: center;'>5</th><th style='text-align: center;'>5</th><th style='text-align: center;'>1</th><th style='text-align: center;'>5</th><th style='text-align: center;'>5</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.25 PDI versus log (the mass flow rate of EVA polymer).</div>


---

<!-- PDF page 64 -->

This concludes the current workshop. We save the simulation file as WS 1.1 Stream Attribute Calculations.bkp.

#### 1.3 Workshop 1.2: A Simplified Simulation Model for a Slurry HDPE Process and the Workflow for Developing a Polymer Process Simulation Model

#### 1.3.1 Objective

The objective of the current workshop is to demonstrate the steps involved in developing a polymer process simulation model using an example of a simplified slurry HDPE process. We identify specific tasks involved in each step and illustrate their relevance to optimizing polyolefin manufacturing.

#### 1.3.2 Step 1: Problem Setup

We begin by creating a “blank simulation” (Figure 1.26). Clicking “Create” will show the Components-Specifications folder within the Properties environment in Figure 1.27. We follow the path: File → Save as → Aspen Plus Backup → Save

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_677_812_932.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.26 Creating a blank simulation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1000_600_1222.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 1.27 Components specifications within the Properties environment.</div>


---

<!-- PDF page 65 -->

the simulation file as WS 1.2 An overview of a polymer process simulation model_HDPE.bkp. It is important to always save the simulation as a backup file as new versions of Aspen Plus in future years can open our saved backup file (*.bkp), but not any other file types such as Aspen Plus document file (*.apw). The document file, however, would be useful when you wish to store the converged simulation inputs and results of a complex simulation problem.

We do not enter the components yet. Instead, we follow the order of different folders within the Properties environment and complete the essential folders sequentially: Properties → Setup (Specifications, Unit Sets) → Components (Specifications, Polymers) → Methods (Specifications, Parameters).

Figure 1.28 shows the completed setup within the Properties environment.

We need to take care of one more setup issue within the setup-global folder of the Simulation environment. As the average molecular weight of a growing polymer chain keeps changing, it is difficult to quantify the component mole fraction in a polymer-containing stream. Therefore, we recommend carrying out the material balance of a polymer process based on a mass flow rate and a component mass fraction. We do this by following the path: Simulation → Setup → Specifications → Global → Flow basis = mass (see Figure 1.29).

We note the user-defined, global unit set US-1 in Figures 1.28 and 1.29. We create this new unit set based on the SI unit set by replacing the temperature unit from K to °C, pressure unit from N/sqm to kPa, and time unit from sec to hr, following the example of Figure 1.7. However, finding the time unit within a unit set in Aspen Plus is a little tricky to a new user. Specifically, we follow the path: Properties → Setup → Unit set → New → Create New ID: Enter ID = US-1 → (1)

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_793_618_926.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 1.28 Completed setup-global folder within Properties environment.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1007_783_1222.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.29 Specifying a mass flow basis for polymer process simulation.</div>


---

<!-- PDF page 66 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_811_468.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.30 Replacing the time unit of the SI unit set from sec to hr within the "Concentration" folder.</div>


Standard: replace temperature unit K with °C, and pressure unit N/sqm with kPa;

(2) Concentration → Time related → replace sec with hr (see Figure 1.30).

#### 1.3.3 Step 2: Component Specifications

Before specifying segment and polymer components, we need to choose the corresponding enterprise databases. See Figure 1.31 for a list of databases that we often use in polyolefin process modeling. INITIATO represents the database for initiator decomposition rate constant parameters for free radical polymerization, such as polystyrene (PS) and high-pressure LDPE processes (see Section 4.2.1); EOS-LIT includes the property parameters for equations of state (EOSs); PC-SAFT and POLYPCSF include the property parameters for applying the Perturbed-Chain Statistical Fluid Theory (PC-SAFT) EOS and the Polymer Perturbed-Chain Statistical Fluid Theory (POLYPCSF) EOS (see Section 2.8) for modeling HDPE, PP, and LLDPE processes.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_983_598_1217.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">Figure 1.31 Selected databases.</div>


---

<!-- PDF page 67 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_148_616_447.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 1.32 Component specifications.</div>


Figure 1.32 shows the component specifications. We will discuss in detail the slurry HDPE process in Section 5.6. Here, ethylene and 1-butene are monomer and comonomer, respectively, with each having a repeated segment. TICl4 is catalyst, and TEAL (triethyl aluminum) is cocatalyst. Hydrogen is chain-transfer agent, and hexane is solvent. Nitrogen is a purge gas.

Next, we characterize the polymer and its attributes by following the path: Properties → Component → Polymers → Characterization → (1) Segments: R-C2H4 and R-C4H8 – Repeat type; (2) Polymers: Polymer ID – HDPE; Built-in attribute group – Choose Ziegler-Natta selection; (3) Site-based species: see Figure 1.33.

In Figure 1.33, we assume that the catalyst TICl4 has five active sites, as determined from a deconvolution analysis of GPC (Gel Permeation Chromatography) measurement of polymer molecular weight distribution (see Section 5.5.2.3). We also assume a site concentration of 0.00172 mol of sites per gram of catalyst; this value typically varies between 1E-5 and 1E-3 [3]. To understand the meanings of attributes, click on one of the attributes, and you will see a table of attributes

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_938_713_1219.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 1.33 Characterization of site-based catalyst species TICl4.</div>


---

<!-- PDF page 68 -->

selection on the right of the figure, explaining each attribute. We discuss more about Ziegler–Natta polymerization in Chapter 5.

#### 1.3.4 Step 3: Property Method

The next step is to choose a property method, which is a collection of models and methods for calculating phase equilibria and various physical properties, such as density, heat capacity, liquid vapor pressure, and heat of vaporization, that are required for doing mass and energy balances. We discuss the details of useful property methods for modeling polyolefin processes and their selection guidelines in Chapter 2. For simulating a slurry HDPE process, we can choose a POLYSL (Polymer Sanchez-Lacombe) EOS [3] discussed in Section 2.6 or a POLYPCSF Theory EOS [4] presented in Section 2.8. Figure 1.34 shows the specification of the POLYSL EOS within the Properties environment for our slurry HDPE process.

#### 1.3.5 Step 4: Property Parameters – Obtaining Values from Databanks and Estimating Missing Parameters

With each property method, we require some property parameters to do phase-equilibrium calculations and mass and energy balances. These include (1) pure component parameters, which could be scalar values (such as molecular weight and normal boiling point) or parameter values of temperature-dependent correlations of physical properties (such as liquid vapor pressure, ideal gas heat capacity, and heat of vaporization) and (2) binary interaction parameters between two components, which impact phase-equilibrium calculations. We see in Figure 1.34 the folders of pure component parameters and binary interaction parameters within property methods.

In Chapter 2, we explain in detail the essential property parameters required for phase-equilibrium calculations and mass and energy balances; we show how to obtain property parameters from Aspen enterprise databanks and to estimate

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_963_811_1221.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 1.34 Specification of POLYSL property method.</div>


---

<!-- PDF page 69 -->

missing property parameters and demonstrate the procedures through hands-on workshops. We do not repeat our discussion in Chapter 2 here.

#### 1.3.6 Step 5: Verification of the Accuracy of the Selected Property Method by Comparing Predicted Pure-Component Property Values with Report Experimental Data

A key question that a model developer must ask is: Could our selected property method accurately predict both the scalar and temperature-dependent, pure-component properties over the range of operating temperatures and pressures of our polyolefin process being simulated?

There are two approaches to answering this question.

(1) Search the literature for relevant publications that include validation of the recommended property methods by comparison of predicted property values with published experimental data.

As an example, for modeling the slurry HDPE process, accurate predictions of property values by the POLYSL property method [3] and the POLYPCSF property method [4] have been verified by reported experimental data. Figure 1.35 gives examples of the published verification of the POLYSL [3] and POLYPCSF [4] property methods. The sources of experimental data in these figures are HDPE heat capacity [5], hydrogen vapor density [6], ethylene vapor heat capacity [7], and propane heat capacity [8]. In Section 2.9.1, we give references

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature (K)</th><th style='text-align: center;'>HDPE heat capacity (kJ/kmoK)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>292.0</td><td style='text-align: center;'>61.8</td></tr>
    <tr><td style='text-align: center;'>315.0</td><td style='text-align: center;'>62.7</td></tr>
    <tr><td style='text-align: center;'>325.0</td><td style='text-align: center;'>63.5</td></tr>
    <tr><td style='text-align: center;'>340.0</td><td style='text-align: center;'>64.3</td></tr>
    <tr><td style='text-align: center;'>350.0</td><td style='text-align: center;'>65.2</td></tr>
    <tr><td style='text-align: center;'>365.0</td><td style='text-align: center;'>66.2</td></tr>
    <tr><td style='text-align: center;'>375.0</td><td style='text-align: center;'>67.2</td></tr>
    <tr><td style='text-align: center;'>380.0</td><td style='text-align: center;'>68.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature (K)</th><th style='text-align: center;'>Hydrogen vapor density (kg/m³)</th><th style='text-align: center;'>Propane heat capacity (kJ/kmol/K)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>98</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>98</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>330</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>580</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>385</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>1.50</td><td style='text-align: center;'>160</td></tr>
    <tr><td style='text-align: center;'>395</td><td style='text-align: center;'>1.75</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>1.90</td><td style='text-align: center;'>140</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature (K)</th><th style='text-align: center;'>0.1 MPa</th><th style='text-align: center;'>1.0 MPa</th><th style='text-align: center;'>6.0 MPa</th><th style='text-align: center;'>PC-SAFT</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>46.0</td><td style='text-align: center;'>73.0</td><td style='text-align: center;'>71.0</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>48.5</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>69.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>49.5</td><td style='text-align: center;'>48.0</td><td style='text-align: center;'>66.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>50.5</td><td style='text-align: center;'>49.0</td><td style='text-align: center;'>64.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>51.5</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>63.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>52.5</td><td style='text-align: center;'>51.0</td><td style='text-align: center;'>62.5</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>53.5</td><td style='text-align: center;'>52.0</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>54.5</td><td style='text-align: center;'>53.0</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 1.35 (a) Verification of property values predicted by POLYSL with reported experimental data. (b) Verification of property values predicted by POLYPCSF with reported experimental data.</div>


---

<!-- PDF page 70 -->

for sources of data for vapor–liquid equilibrium and thermophysical properties for polyolefin process modeling. The verification of the accuracy of applying the POLYPCSF property method to simulating the PP process appears in [9, 10], and to simulating the LDPE process is available in [11].

(2) If we cannot find the published reports of verification of property values with experimental data, do the verification study by applying the property set and property analysis tool of Aspen Plus (see Section 2.5).

#### 1.3.7 Step 6: Regress Component Liquid Density Data and Binary Vapor–Liquid Equilibrium (TPXY) Data to Estimate Missing Pure-component and Binary Interaction Parameters of Selected Property Method and Verify Predicted VLE Results with Experimental Data

See Sections 2.7 and 2.9 for two hands-on workshops for carrying out this step for applying the POLYSL and POLYPCSF property methods to a slurry HDPE process, respectively.

#### 1.3.8 Step 7: Develop Correlations for Polymer Product Quality Indices, Such as Density and Melt Index (Melt Flow Rate) Based on Plant Data

Refer to Sections 2.10.1 and 2.10.2 for details.

#### 1.3.9 Step 8: Define the Polymerization Reactions and Enter the Initial Reaction Rate Constants

We discuss in detail the types of polymerization kinetic model reactions and the estimation of their reaction rate constants from experimental or plant data in Chapters 3–6. Chapter 4 introduces free radical polymerization kinetics for LDPE and EVA copolymer; Chapter 5 focuses on Ziegler–Natta polymerization kinetics for HDPE, PP, LLDPE, and EPDM (ethylene–propylene–diene terpolymer); and Chapter 6 covers free radical polymerization for polystyrene (PS) and ionic polymerization for poly(styrene-butadiene-styrene) rubber or SBS rubber. These chapters also give initial values of reaction rate constants based on the literature in terms of preexponential factor  $ k_{0} $ and activation energy E according to the standard Arrhenius equation:

 $$ k=k_{0}*e^{-\frac{E}{R}\left(\frac{1}{T}-\frac{1}{T_{\mathrm{r}}}\right)} $$ 

where R is the ideal gas constant, T is the temperature of the reaction system, and  $ T_{r} $ is the reference temperature.

We follow the path: Simulation → Reactions → (1) Species - see Figure 1.36; (2) Reactions - see Figure 1.37; and (3) Rate Constants - see Figure 1.38. In Figure 1.36, monomer C2H4 and comonomer C4H8 go to repeated segments R-C2H4 and R-C4H8. TICI4 is the catalyst, and TEAL is the cocatalyst. HX (n-hexane) is the solvent, and H2 is the chain-transfer agent. Other polyolefin processes may also involve a poisoning agent and an electron donor agent.

---

<!-- PDF page 71 -->

<div style="text-align: center;">Figure 1.36 Species specifications of Ziegler–Natta polymerization reactions for a slurry HDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_426_148_799_410.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">Figure 1.37 A partial list of the generated Ziegler–Natta polymerization reactions for a slurry HDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_364_456_799_820.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 1.37 shows a partial list of the generated reactions for five active catalyst sites specified in Figure 1.33. Figure 1.38 gives a partial list of the initial preexponential factor and activation energy of the generated reactions according to Eq. (1.14). For this example, we have a total of 70 reactions. These include (1) 5 catalyst site activation reactions by cocatalyst (Act-Cocat) with one reaction by active catalyst site; (2) 10 chain initiation reactions (Chain-Ini) by monomer C2H4 and comonomer C4H8, with two reactions per active catalyst site; (3) 20 chain propagation reactions (PROP) of reacting polymer chain Pn[C2H4] with C2H4 and C4H8 and polymer chain Pn[C4H8] with C2H4 and C4H8, totaling five reactions per active catalyst site; (4) 20 reactions of chain transfer to monomer (CHAT-MON) by reacting polymer chain Pn[C2H4] with C2H4 and C4H8 and polymer chain Pn[C4H8] with C2H4 and C4H8, with five reactions per active catalyst site; (5) 10 reactions of chain transfer to hydrogen (CHAT-H2) by reacting polymer chain Pn[C2H4] with H2 and polymer chain Pn[C4H8] with H2, with two reactions per active catalyst site; and (6) 5 spontaneous catalyst deactivation reactions (DEACT-SPON), with one reaction per active catalyst site type. In Section 5.2, we discuss in detail all the</div>


---

<!-- PDF page 72 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_147_768_476.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 1.38 A partial list of the initial preexponential factor and activation energy of the generated reactions.</div>


potential reactions in Ziegler–Natta polymerization and the guidelines for including specific reactions for different polyolefins.

#### 1.3.10 Step 9: Draw the Open-Loop Process Flowsheet and Enter the Inputs for Streams and Blocks

We may switch the order of Steps 8 and 9; that is, we may draw the process flowsheet first as soon as we have completed Properties environment (Steps 1–7) and enter the Simulation environment. Figure 1.39 shows our open-loop flowsheet for our simplified slurry HDPE process.

To speed up the convergence of phase-equilibrium calculations and mass and energy balances of a polyolefin process, we recommend beginning with an open-loop process flowsheet by breaking up selected streams exiting downstream

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_917_817_1246.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Figure 1.39 A simplified slurry HDPE process.</div>


---

<!-- PDF page 73 -->

separators that are recycled back to the reactor inlets. Compare the flowsheets in Figures 5.20 (open loop) and 5.45 (closed loop) for a commercial slurry HDPE process and Figures 5.51a and 5.51b (open loop) with Figures 5.66a and 5.66b (closed loop) for a commercial gas-phase stirred-bed PP process. Through the hands-on workshops in Sections 5.6 and 5.7, we demonstrate the guidelines to achieving convergence in complex closed-loop polyolefin process simulations.

#### 1.3.11 Step 10: Run the Initial Open-loop Process Simulation and Check if the Simulation Results Are Reasonable

Figure 1.40 shows the stream results of the open-loop simulation based on the initial set of kinetic parameters.

We see that the monomer (ethylene) conversion to HDPE appears to be too high (5684.82/5700 = 99.73%) based on industrial experience, and the MWN of 2.794E6 and the MWW of 7.194163E6 both seem high as well. A key question of polymer process modeling is: How do we fine-tune the initial values of kinetic parameters to match production targets or plant data?

In Section 5.5, we present an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient software tools available within Aspen Plus, including sensitivity analysis, design specification, and data fit [12]. Sensitivity analysis quantifies the effect of varying kinetic parameters on the production targets. Design specification finds the desired kinetic parameters to match the specified production targets. Data fit is an efficient nonlinear regression tool that determines statistically acceptable, kinetic parameters from constant, time-varying, or temperature-dependent laboratory

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_791_712_1246.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 1.40 Stream results of the open-loop simulation.</div>


---

<!-- PDF page 74 -->

measurements or from matching the process simulation to production targets. We briefly illustrate sensitivity analysis in Section 1.2 in Figures 1.15–1.25. In Sections 3.9 and 3.10, we demonstrate the use of data fit to estimate kinetic parameters for styrene polymerization.

Table 5.4 of Section 5.5.2.1 and Table 5.9 of Section 5.5.2.3 identify the factors affecting production targets using single- and multiple-site Ziegler–Natta catalysts.

For example, according to Table 5.4, the rate constant parameters for chain propagation are among the factors that significantly affect the monomer conversion or polymer production rate. What happens if we reduce all the preexponential factors for chain propagation reactions illustrated in part in Figure 1.38 by 10-fold and run the simulation again? This results in a monomer (ethylene) conversion to HDPE of 5525.38/5700 or 97.94%, an MWN of 2.71533E6, and the MWW of 6.94027E6.

We can continue to fine-tune the kinetic parameters to match production targets or plant data within a closed recycled loop in the following step.

#### 1.3.12 Step 11: Close the Recycled Loops, Finalize a Converged Closed-loop Steady-state Simulation Model, and Investigate Applications to Improving Process Operations and Identifying Operating Conditions for New Product Design

Sections 5.6.9–5.6.11 and 5.7.8 illustrate how to close the recycle loop for the commercial slurry HDPE process and for the gas-phase stirred-bed PP process. Sections 5.6–5.8 give detailed illustrations of the efficient software tools, particularly sensitivity analysis, design specification, and data fit. The resulting polyolefin process simulation models present the quantitative foundation for sustainable design and optimization, process improvement, capacity expansion, and new product design. We give examples of potential and industrial applications in Section 1.4.

#### 1.3.13 Step 12: Convert the Steady-state Simulation Model in Aspen Plus to a Dynamic Simulation Model in Aspen Plus Dynamics; Add Appropriate Controllers; and Investigate Process Operability, Control, and Grade Changes

We present details in Chapter 7 for improved polymer process operability and control through Aspen Plus and Aspen Plus Dynamics models.

### 1.4 Industrial and Potential Applications of Integrated Process Modeling, Advanced Control, and Data Analytics to Optimizing Polyolefin Manufacturing

#### 1.4.1 Industrial and Potential Applications of Process Modeling to Optimizing Polyolefin Manufacturing

The senior author has been a founder and an instructor of the SINOPEC Simulation Training Center in Beijing, cosponsored by Aspen Technology and Virginia Tech

---

<!-- PDF page 75 -->

from 1997 to 2015. He (during university breaks) and the instructors he trained have taught over 7500 practicing engineers in Greater China to use software tools to promote process simulation and advanced control and energy and water savings. Under his guidance, his trainees have completed the process simulation models for over 300 petrochemical processes from 2001 to 2015 for energy savings, waste minimization, and sustainable design and optimization, enhancing the sustainability and generating significant economic and environmental benefits. According to a published SINOPEC report in February 2014 [13], these projects have resulted in an annual payback of over US$115.5 million (including energy savings of US$ 57.3 million) for a total investment of less than US$ 10 million from 2002 to 2012.

As an example, during 2012–2014, the project teams have completed the Aspen Polymers simulation models for 38 polyolefin processes, including 23 PP processes, 5 LLDPE processes, 3 HDPE processes, and 7 LDPE processes. These models, validated by accurate predictions of plant data, provide the quantitative foundation to optimize the reactor fluid level and density; reaction temperature; flow rates and feed ratios of monomers and comonomers; flow rates and feed ratios of catalysts, cocatalysts, and electron donor agents; hydrogen mass flow; copolymer composition; and separation system operation. These result in improved single-pass conversions of monomers; increased polymer production; reduced consumptions of catalysts, cocatalysts, and electron donor agents; lowered energy consumptions and unnecessary monomer vent loss; less off-specification transitional materials during grade changes; and identification of optimum operating conditions for new product grades. These 38 Aspen Polymers simulation models have generated an annual payback of US$ 5.7 million, averaging about US$ 150K per process, for a total investment of less than US$ 10K per process.

Tremblay [14], Aspen Technology [15], and Morse and Tremblay [16] present several success stories of applying Aspen Polymers to industrial polymerization processes. Among those relating to polyolefins include the following:

(1) Polymer process design, Chemical Business, SCG, Thailand: The company wanted to design a new HDPE manufacturing plant with a production capacity of 400K ton/hr and reduced HDPE product design and development time. By applying Aspen Polymers, the company saved over US$ 1 million in capital cost for the new plant and US$ 300K by reducing plant trials for new product grades and was able to apply the model for process operational debottlenecking.

(2) Operation decision support, Hanwha Solutions Chemical Division, South Korea: The company faced the challenge of having a lack of insight into the high-pressure LDPE process, resulting in low production rates, suboptimal product quality, and difficulty in making operation decisions in the plant. By applying Aspen Polymers to develop a simulation model for the tabular reactor to predict the temperature profile and polymer properties and deploying the model with Excel-based Aspen Simulation Workbook, the company was able to identify inherently safe operating conditions to increase rate by 5–7% per year.

---

<!-- PDF page 76 -->

while improving product quality and consistency. Engineering studies using the simulation model provide insights leading to further plant improvement and allow plant engineers to understand how operating conditions influence product quality.

(3) Accelerating New Product Grade Development, Qenos, Australia: The company wanted to supply custom-tailored products to the market faster than the competition and to optimize HDPE processes to meet customized specifications. Using Aspen Polymers and process data from plant historian to develop simulation models, the company reduced side reactions in the batch processes that produced off-specification material and completed the plant trials for a new product grade six months ahead of schedule, saving US$ 135K per year.

(4) Reducing Batch Cycle Time for Overall Time-to-Market for New Products, Dow Chemical, USA: Dow was able to speed time to market and reduce batch cycle time by 24% using Aspen Polymers and Aspen Plus Dynamics to adjust process conditions. Examining insights from the simulation model, engineers were able to develop quantitative relationships between a polymer's application properties and its chemical structure. This enabled the engineers to fine-tune the process design to produce the polymer product with the desired application property, thus reducing the overall time-to-market for new products.

#### 1.4.2 Industrial and Potential Applications of Advanced Process Control to Optimizing Polyolefin Manufacturing

Marlin [17], Camacho and Bordons [18], and Lahiri [19], among others, have presented the fundamentals and industrial applications of advanced process control (APC) methodologies based on model-predictive control (MPC) schemes. In this book, we focus on a general class of MPC called dynamic matrix control (DMC) that was first proposed by Cutler and Ramaker in 1979 [20]. Over the years, Aspen Technology has continued to further develop the DMC technology. The current version is a third-generation DMC technology, called DMC3 [21, 22]. Braskem, Latin America's largest petrochemical company in São Paulo, Brazil, has reported its success in deploying Aspen DMC3 controllers in just two weeks and immediately accruing benefits [23]. ExxonMobil [24], among others, has shared their positive experiences in implementing the new DMC3 controllers in their petrochemical plants.

To understand the potential and industrial applications of the new DMC3 technology to polymer manufacturing, particularly applied to polymer grade transitions, let us first review some historical development and industrial applications.

In the early 1990s, there were growing interests in developing MPC technology for chemical processes using neural network models in the literature [25, 26]. Turner et al. were the first [27, 28] to point out two significant difficulties in applying conventional neural network models to MPC applied to polymer manufacturing: (1) Conventional neural network architectures intrinsically contain regions where the partial derivative of a dependent variable (a process variable, PV) with respect

---

<!-- PDF page 77 -->

to an independent variable (a manipulative variable, MV) becomes zero, and the resulting zero model gain would lead to an infinite controller gain, and (2) conventional neural network models cannot cope with the extrapolative demands of predictive control over polymer grade transitions.

To avoid those difficulties, Turner et al. have proposed a new state-space bounded derivative network (SSBDN) as the foundation for MPC with neural network models  $ [27, 28] $. This work led to the development of the Aspen Apollo controller. When used together with the Aspen IQ for developing inferential property models and with the Aspen Transition Manger for grade transition management, Aspen Apollo controller became the core component of the Aspen-integrated polymer production control solution.

SABIC Polyolefine GmBH's polyethylene production facility at Gelsenkirchen, Germany, was the first commercial polymer producer to successfully implement the Aspen Apollo controller to achieve two objectives  $ [29] $: (1) grade objectives: maintaining the polymer product quality within product specifications; maximizing polymer production; and reducing waste and production cost, and (2) minimizing transition time and loss of production during transitions and decreasing production of-specification product polymer.

In 2004, polyolefin producers in China began to implement the Aspen Apollo controller in a growing number of applications involving HDPE, PP, and LLDPE processes for controlling the polymer qualities (melt index and density) and production rate and for optimizing grade transitions [30-35]. At that time, the senior author was devoting his university breaks to training APC project engineers within the SINOPEC Simulation Training Center in Beijing and was familiar with this application development. In all these applications, the overall control strategy is similar, as illustrated in Figure 1.41 [30]. This figure shows: (1) two cascaded controllers for the quality control and for the concentration and production rate control; (2) the grade transition management to provide quality targets for the quality controller and the tuning limits for the concentration and production rate controller; and (3) the inferential property models to provide the instantaneous and reactor bed-average property predictions, which represent the quality predictions based on process variables for the grade transition management, and based on targets for the two cascaded controllers. In Chapter 8, we discuss the development of this controller in detail.

As an example, Table 1.2 illustrates the transition specifications for producing grade A and grade B in a slurry HPDE process with a production rate of 240,000 ton/yr in China. Note the changes in reactor temperature and pressure, target polymer melt index, percentage of monomer feed to each reactor, and the addition of comonomer feed as well as the change in H2 to monomer ratio. Figure 1.42 illustrates the automated changes in the reactor pressure, H2/C2H4 ratio, and H2 flow rate for reactor R1 to transition from grade A to grade B implemented by the Aspen-integrated polymer production control solution. The Aspen Apollo controller increased the production rate by 2.9%, reduced catalyst consumption by 6.4%, lowered hydrogen consumption by 21.7%, and decreased the ethylene vent loss by 3.5 kg/ton of HDPE. With an APC online rate of 90%, the

---

<!-- PDF page 78 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_805_565.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 1.41 Aspen Apollo controller structure for controlling polymer qualities, production rate, and grade transitions.</div>


<div style="text-align: center;">Table 1.2 Grade transition specifications</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Grade</td><td colspan="2">A (R1 and R2 in parallel)</td><td colspan="2">B (R1 and R2 in series)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reactor</td><td style='text-align: center; word-wrap: break-word;'>R1</td><td style='text-align: center; word-wrap: break-word;'>R2</td><td style='text-align: center; word-wrap: break-word;'>R1</td><td style='text-align: center; word-wrap: break-word;'>R2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>78</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (MPa)</td><td style='text-align: center; word-wrap: break-word;'>0.4-0.6</td><td style='text-align: center; word-wrap: break-word;'>0.4-0.6</td><td style='text-align: center; word-wrap: break-word;'>0.60-0.75</td><td style='text-align: center; word-wrap: break-word;'>0.20-0.30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Slurry concentration (g/l)</td><td style='text-align: center; word-wrap: break-word;'>360</td><td style='text-align: center; word-wrap: break-word;'>360</td><td style='text-align: center; word-wrap: break-word;'>360</td><td style='text-align: center; word-wrap: break-word;'>360</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Melt index (g/10 min)</td><td style='text-align: center; word-wrap: break-word;'>4.4-6.9</td><td style='text-align: center; word-wrap: break-word;'>4.4-6.9</td><td style='text-align: center; word-wrap: break-word;'>130-230</td><td style='text-align: center; word-wrap: break-word;'>1.2-1.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>% of total feed</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>54.68</td><td style='text-align: center; word-wrap: break-word;'>45.32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Monomer feed (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>5750</td><td style='text-align: center; word-wrap: break-word;'>5750</td><td style='text-align: center; word-wrap: break-word;'>5800</td><td style='text-align: center; word-wrap: break-word;'>4557</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Comonomer feed (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>250</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2 to C2H4 ratio</td><td style='text-align: center; word-wrap: break-word;'>1.4-1.6</td><td style='text-align: center; word-wrap: break-word;'>1.4-1.6</td><td style='text-align: center; word-wrap: break-word;'>3.8-4.2</td><td style='text-align: center; word-wrap: break-word;'>0.20-0.25</td></tr></table>

annual economic payback was US$ 2.7 million for an investment of 0.9 million, resulting in a payback period of four months.

Reports of successful commercial applications of the Aspen-integrated polymer production control solution have continued to appear in the literature from petrochemical producers within China. See, for example, HDPE [30], PP [31–34], and LLDPE [35]. According to a published SINOPEC report in February 2014 [13], there were 142 APC implementations in its refining and chemical processes at the end of 2013, generating an annual economic payback of US$ 80 million per year for an investment of approximately US$ 20 million.

---

<!-- PDF page 79 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>C2H4</th><th style='text-align: center;'>H2</th><th style='text-align: center;'>Pressure</th><th style='text-align: center;'>H2/C2H4</th><th style='text-align: center;'>Catalyst</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>08:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>09:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>09:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>10:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>10:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>11:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>11:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>12:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>12:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>13:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>13:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>14:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>14:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>15:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>15:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>15:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>16:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>16:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>16:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>16:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>17:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>17:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>17:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>17:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>18:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>18:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>18:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>18:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>19:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>19:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>19:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>19:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>20:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>20:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>20:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>20:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>21:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>21:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>21:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>21:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>22:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>22:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>22:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>22:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>23:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>23:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>23:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>23:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>24:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>24:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>24:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>24:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>25:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>25:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>25:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>25:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>26:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>26:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>26:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>26:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>27:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>27:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>27:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>27:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>28:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>28:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>28:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>28:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>29:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>29:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>29:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>29:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>30:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>30:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>30:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>30:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>00:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>00:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>00:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>00:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>01:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>01:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>01:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>01:45:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>02:00:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>02:15:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.3063</td><td style='text-align: center;'>0.2204</td></tr>
    <tr><td style='text-align: center;'>02:30:00</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.421</td><td style='text-align: center;'>0.3063</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.42 An illustration of the automated changes in reactor pressure, H2/C2H4 ratio, and H2 flow rate for reactor R1 to change from grade A to grade B.</div>


Currently, the latest extension of Aspen Apollo is called Aspen Nonlinear Controller; the corresponding extension of Aspen IQ is called Aspen Inferential Qualities. Both are parts of the third-generation, dynamic matric control suite of APC software tools, DMC3, with many demonstrated successes in controlling and optimizing refining and chemical processes, including polymer operations. In Chapter 8, we present the principles, industrial practice, and hands-on workshops of the latest Aspen polymer production control solution using DMC3.

#### 1.4.3 Industrial and Potential Applications of Data Analytics to Optimizing Polyolefin Manufacturing

Beginning in the late 1980 to early 1990, chemical engineers have been paying greater attention to the emerging topics of artificial intelligence, neural computing, machine learning and big data analytics, and their applications to bioprocessing and chemical industries [26, 31, 36–38]. McGregor and others have demonstrated the significant applications of multivariate statistical analysis and big data analytics to optimizing the manufacturing of LDPE, HDPE, Nylon 6, and other polymers [39–43]. Multivariate statistical analysis [44–47] and its software implementation by Aspen ProMV [48] find many applications to polymer manufacturing, such as (1) data quality deviation analysis; (2) unit yield analysis; (3) production capacity degradation analysis; (4) offline production optimization (discovery and optimization of key variables); (5) online process monitoring and troubleshooting; and (6) batch process variable analysis.

Chapters 9–11 of this book cover the current and emerging applications of machine learning and big data analytics to optimizing polyolefin manufacturing. We focus on the principles and applications of neural networks, machine-learning,

---

<!-- PDF page 80 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_147_800_574.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 1.43 A schematic diagram of a slurry HDPE process with parallel reactors.</div>


and multivariate statistical analysis to optimizing polymer manufacturing [45–47]. We also demonstrate their software implementations through hands-on workshops using Python and Aspen ProMV [48].

In Section 2.10, we explain the correlation of polymer product quality indices, such as the melt index (MI) or melt flow index (MFI). In what follows, we illustrate a simple data-based sensor for predicting the MI from a slurry HDPE process with two reactors in parallel using actual plant data from LG Petrochemicals in South Korea [43]. Figure 1.43 shows a schematic diagram of a general slurry HPDE process with parallel reactors [3].

Park et al. [43] correlate the MI data by considering the following independent variables: (1) C2: monomer ethylene feed flow rate; (2) C4: comonomer 1-butene flow rate; (3) CAT: catalyst flow rate; (4) H2: chain-transfer agent hydrogen flow rate; (5) HX: solvent n-hexane flow rate; (6) H2/C2: ratio of feed flow rates of H2 and C2; (7) T: reactor temperature; and (8) P: reactor pressure.

Figure 1.44 illustrates the application of Aspen ProMV to data quality deviation analysis, such as identifying the outliers in the measured MI data of [43]. Note the data points above the horizontal line labeled by the confidence limits of 0.99 and 0.96. We could remove those outliers.

Figure 1.45 compares the measured time-dependent MI data for the slurry HPDE process from [48] with grade transitions to the predictions from a regressed model based on the multivariate statistical analysis with partial least squares (PLS), and Figure 1.46 shows the same comparison using a regressed model developed by a machine learning (ML) method called random forest algorithm of Section 10.3.2 [49] using Python. In general, we evaluate the relative accuracy of different regression models using the root mean square error (RMSE). We note that the PLS

---

<!-- PDF page 81 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>HT[2] [×14]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2900</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3100</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3300</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3700</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3900</td><td style='text-align: center;'>2.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.44 Data quality deviation analysis by multivariate statistical analysis using Aspen ProMV.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Predicted MI (PLS)</th><th style='text-align: center;'>Actual MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>17.5</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.45 Development of a soft sensor of MI based on multivariate statistical analysis with partial least squares using Aspen ProMV.</div>


model has a large RMSE of 1.08, while the random forest ML model has a much smaller RMSE of 0.12.

We encourage our readers to refer to McGregor and Brewer [41] for an excellent presentation of optimization of processed and products using historical data, including applications of multivariate statistical analysis and Aspen ProMV to an optimization of batch polymerization done at Air Products and Chemicals.

Appendix A of this book gives a review of matrix algebra in multivariate data analysis and model predictive control in MATLAB and Python. Appendix B presents a tutorial of using Python, and Chapters 9–11 present the details of

---

<!-- PDF page 82 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Predicted MI</th><th style='text-align: center;'>Actual MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>17.5</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>19.8</td><td style='text-align: center;'>19.8</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>5.2</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>4.8</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>2.3</td><td style='text-align: center;'>2.3</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.46 Development of a soft sensor of MI based on machine learning techniques with the random forest algorithm using Python.</div>


applying multivariate statistical analysis, machine learning techniques, and big data analytics to optimizing polyolefin manufacturing.

#### 1.4.4 Hybrid Modeling: Integrated Applications of Process Modeling, Advanced Control, and Data Analytics to Optimizing Polyolefin Manufacturing

This section first reviews the historical and recent development of hybrid modeling in bioprocessing and chemical industries. We then illustrate the significant advantages of hybrid modeling in broadening the applicable ranges of process variables for the resulting predictive model with a slurry HDPE process of Figure 1.43.

Modeling of any physical system requires complete knowledge of physics of the system which is not always feasible for complex processes. We make some assumptions when modeling the system with first principles that ultimately leads to some gaps in describing the original system. Even for the systems where the physical knowledge is sufficient to model the system, there are too many parameters to estimate. Data-based models have been applied to study the systems where physical data are available since they are more accurate in predictions. However, data-based or machine-learning (ML) models are black-box models which can overfit the data and produce scientifically inconsistent results. For better accuracy, ML models require more data, which are not always feasible for all problems. Hence, combining physics-based knowledge and the data-based information has become increasingly important for an accurate and scientifically consistent prediction, which we will refer to as a Hybrid Modeling or Science-Guided Machine Learning (SGML) Approach [50].

One of the earliest applications of hybrid modeling in bioprocessing and chemical industries was in the area of process control where Psichogios and Ungar [51] used

---

<!-- PDF page 83 -->

the neural networks to estimate parameters of a physical model for model-based control. This semiparametric model was later applied to a bioprocess to improve the accuracy of prediction compared to a stand-alone neural network model [52]. Agarwal [53] was among the first to discuss the different hybrid modeling frameworks with series or parallel configuration based on the way the outputs of the science-based model and the ML model are combined.

Over the years, there have been growing applications of hybrid modeling in different areas of bioprocessing and chemical industries as a part of advances in smart manufacturing [54]. Von Stosch et al. [55] have classified the hybrid modeling in chemical industries into different areas according to their applications, namely in bioprocess [56, 57], chemical and petrochemical process industries [58], process control [59], design of experiments [60], process development and scale-up [61], and process optimization [62].

Some of the key advantages of hybrid modeling in chemical process industry identified by Von Stosch et al. [55] are in the prediction of scientifically consistent results beyond the experimentally tested process conditions. This is crucial for process development and scale-up, control, and optimization, while also requiring less data for implementing the data-based models. They also identified some challenges. For example, incorrect fundamental knowledge in a science-based model would impose bias on predictions; thus, the underlying assumptions used in a model are important for analysis. Also, time and accuracy of parameter estimation is critical when deciding on a hybrid modeling strategy.

Based on their experience in applying hybrid modeling to chemical industries, Aspen Technology [63, 64] has classified hybrid modes into three categories: (1) AI-driven modeling, (2) first-principle-driven modeling, and (3) reduced-order modeling. The AI-driven hybrid model is an empirical model based on plant or experimental data and uses first principles, constraints, and domain knowledge to create a more accurate model. An example of AI-driven models can be inferential sensors or online equipment models. The first-principle-driven model is an existing first-principle model augmented with data and AI to improve model's accuracy and predictability, which has seen many applications in bioprocess modeling. Lastly, to develop a reduced-order model, we first use machine learning to create an empirical model based on data from numerous simulation runs, augmented with constraints and domain expertise, to build a fit-for-purpose model that can run more quickly. This reduced-order modeling technique is usually used for building plant-wide models which often need to be deployed fast.

Let us consider the prediction of MI from a slurry HDPE process with two reactors in parallel using actual plant data from LG Petrochemicals in South Korea [43], which we illustrate previously in Figures 1.43–1.46. In Chapter 7, we show how to convert a steady-state simulation model based on Aspen Plus to a dynamic (time-dependent) simulation model using Aspen Plus Dynamics. The resulting dynamic simulation model has similar independent variables as those for Figures 1.43–1.46. Both steady-state and dynamic simulation models are developed from first principles such as phase-equilibrium calculations and mass and energy balances. Therefore, they are scientifically consistent models.

---

<!-- PDF page 84 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Model MI</th><th style='text-align: center;'>Hybrid MI</th><th style='text-align: center;'>Plant MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>2.2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1.47 Melt index prediction of a combined direct hybrid model compared to the first-principles model and plant data.</div>


Figure 1.47 compares the predictions of the first-principle-based dynamic simulation model (in red) with the plant data with grade transitions (in green). We see much deviation between the model predictions and the plant data. We compare the MI values from the model with the plant data and calculate the error residuals. The RMSE value of the model residual is 1.5 for the actual MI data with a standard deviation of 5.1.

To improve the accuracy of model predictions, we develop a regression model to predict the error residues as a function of independent process variables based on an ML method called random forest algorithm [49; Section 10.3.2] with Python. This leads to a hybrid model that predicts the MI value as a sum of the dynamic simulation model prediction (first-principle based) and the predicted error residual (data based) corresponding to a given set of independent process variable values. Figure 1.47 shows that the hybrid model predictions in blue match the plant data much better than a first-principle-based dynamic simulation model alone.

We note that a data-based model alone also has a similar accuracy, but it may give scientifically inconsistent results for predictions beyond process operating data which the model uses. Thus, the hybrid model is not only accurate but also gives scientifically consistent results beyond current operating range. In Chapter 11, we present the fundamentals, applications, and hands-on workshops of hybrid modeling in optimizing polyolefin manufacturing [50].

## References

1 Chen, C.C., Barrera, M., Ko, G. et al. (1997). Polymer component characterization method and process simulation apparatus. US Patent 5,687,090, 11 November 1997.

2 Seavey, K.C. and Liu, Y.A. (2008). Step-Growth Polymerization Process Modeling and Product Design, 61–64. New York: Wiley.

---

<!-- PDF page 85 -->

3 Khare, N.P., Seavey, K.C., Liu, Y.A. et al. (2002). Steady-state and dynamic modeling of commercial slurry high-density polyethylene (HDPE) processes. Industrial and Engineering Chemistry Research 41: 5601.

4 Chen, K., Tian, Z., Luo, N., and Liu, B. (2014). Modeling and simulation of borstar bimodal polyethylene process based on a rigorous PC-SAFT equation of state model. Industrial and Engineering Chemistry Research 53: 19905.

5 Gaur, U. and Wunderlich, B. (1981). Heat capacity and other thermodynamic properties of linear macromolecules. II. Polyethylene. Journal of Physical and Chemical Reference Data 10: 119.

6 Beaton, C.F. and Hewitt, G.F. (1989). Physical Property Data for the Design Engineer. New York: Hemisphere Publishing Corp.

7 Jahangiri, M., Jacobson, R.T., Stewart, R.B., and McCarthy, R.D. (1986). Thermodynamic properties of ethylene from the freezing line to 450K at pressure of 260 MPa. Journal of Physical and Chemical Reference Data 15: 593.

8 Yesavage, V.F., Katz, D.L., and Powers, J.E. (1969). Thermal properties of propane. Journal of Chemical & Engineering Data 14: 197.

9 Khare, N.P., Lucas, B., Seavey, K.C. et al. (2004). Steady-state and dynamic modeling of commercial gas-phase polypropylene processes using stirred-bed reactors. Industrial and Engineering Chemistry Research 43: 884.

10 Zheng, Z.W., Shi, D.P., Su, P.L. et al. (2011). Steady-state and dynamic modeling of the basell multireactor olefin polymerization process. Industrial and Engineering Chemistry Research 50: 322.

11 Bokis, C.P., Ramanathan, S., Franjione, J. et al. (2002). Physical properties, reactor modeling, and polymerization kinetics in the low-density polyethylene tubular reactor process. Industrial and Engineering Chemistry Research 41: 1017.

12 Sharma, N. and Liu, Y.A. (2019). 110th Anniversary: an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient software tools. Industrial and Engineering Chemistry Research 58: 14209.

13 Li, D. and Suo, H. (2014). Accelerating the process of smart plant and promoting ecological civilization construction. CIESC Journal 65: 374.

14 Tremblay, D. (2020). Improve sustainability and increase profits in polymers with digitalization. AspenTech White Paper. https://www.aspentech.com/en/resources/white-papers/improve-sustainability-and-increase-profits-in-polymers-with-digitalization (accessed 4 June 2021).

15 Aspen Technology, Inc. (2020). Daicel accelerates innovation and reduces the number of experiments with Aspen polymers. AspenTech Case Study. https://www.aspentech.com/en/resources/case-studies/daicel-accelerates-innovation-and-reduces-the-number-of-experiments-with-aspen-polymers (accessed 4 June 2021).

16 Morse, P. and Tremblay, D. (2020). Accelerate innovation and improve sustainability through polymer process modeling. AspenTech webinar. https://www.aspentech.com/en/resources/on-demand-webinars/accelerate-innovation-and-improve-sustainability-through-polymer-process-modeling (accessed 4 June 2021).

---

<!-- PDF page 86 -->

17 Marlin, T.E. (2000). Process Control: Designing Processes and Control Systems for Dynamic Performance, 2e. New York: McGraw-Hill.

18 Camacho, E.F. and Alba, C.B. (2013). Model Predictive Control, 2e. London: Springer-Verlag.

19 Lahiri, S.K. (2017). Multivariable Predictive Control: Applications in Industry. New York: Wiley.

20 Cutler, C.R. and Ramaker, B.L. (1979). Dynamic Matrix Control – A Computer Control Algorithm. Houston, TX: AIChE National Meeting.

21 Golightly, R. (2016). The Aspen DMC3 difference. AspenTech white paper. https://www.aspentech.com/en/resources/white-papers/the-aspen-dmc3-difference (accessed 9 June 2021).

22 Kalafatis, A., Harmse, M., and Campbell, J. (2017). Next generation MPC: where is the technology headed? 8th CPC Conference (10 January 2017). https://www.focapo-cpc.org/pdf/Kalafatis.pdf (accessed 4 June 2021).

23 Tizzo, L. (2018). Braskem implements Aspen DMC3 to deploy controllers in just two weeks and immediately accrues benefits. https://www.aspentech.com/en/resources/case-studies/braskem-implements-dmc3-to-deploy-controllers-in-just-two-weeks-and-immediately-accrues-benefits (accessed 9 June 2021).

24 Hokanson, D. and D'Hooghe, P. (2018). DMC builder experience in ExxonMobil. AspenTech webinar. https://www.aspentech.com/en/resources/on-demand-webinars/experiences-with-aspen-dmc3-builder-featuring-exxonmobil (accessed 9 June 2021).

25 Saint-Donat, J., Bhat, N., and McAvoy, T.J. (1991). Neural-net based model-predictive control. International Journal of Control 54: 1453.

26 Baughman, D.R. and Liu, Y.A. (1995). Neural Networks in Bioprocessing and Chemical Engineering, 228–364. San Diego, CA: Academic Press, Inc.

27 Turner, P., Guiver, J., and Lines, B. (2003). Introducing the bounded derivative network for commercial transition control. Proceedings of American Control Conference, Denver, Colorado (4–6 June 2003), 5400.

28 Turner, P. and Guiver, J. (2005). Introducing the bounded derivative network – superceding the application of neural networks in control. International Journal of Control 15: 407.

29 Aspen Technology, Inc. (2002). Innovative AspenTech solution delivers new levels of manufacturing performance to polymers industry. http://ir.aspentech.com/news-releases/news-release-details/innovative-aspentech-solution-delivers-new-levels-manufacturing (accessed 9 June 2021).

30 Zhu, Y.Q., Zhang, Y.J., and Xu, X.W. (2006). Application of advanced process control technology to a high-density polyethylene process. Petrochemical Technology 5: 469.

31 Wu, B.Y. (2006). Application of advanced control techniques in gas-phase process for polymerization of propylene. Sino-Global Energy 11 (1): 82.

32 Guo, X.J. (2007). Application of nonlinear controllers to polypropylene loop reactor process. Technology and Economics in Petrochemicals 23 (2): 31.

33 Wang, S.Q. (2015). Application of advanced process control to a gas-phase polypropylene process. Chemical and Pharmaceutical Engineering 36: 51.

---

<!-- PDF page 87 -->

34 Zhou, T.M., Zheng, X.C., Jiang, F.Y. et al. (2017). Advanced process control system for a polypropylene process and its applications. Computers and Applied Chemistry 34: 957.

35 Chi, L. (2010). Application of advanced process control to a gas-phase linear low-density polyethylene (LLDPE) process. Computers and Applied Chemistry 27 (8): 1049.

36 Quantrille, T.E. and Liu, Y.A. (1991). Artificial Intelligence in Chemical Engineering. San Diego, CA: Academic Press.

37 Qin, S.J. (2014). Process data analytics in the era of big data. AIChE Journal 60: 3092.

38 Chiang, L., Lu, B., and Castillo. (2017). Big data analytics in chemical engineering. Annual Reviews of Chemical and Bimolecular Engineering 8: 63.

39 Skagerberg, B., MacGregor, J.F., and Kiparissides, C. (1992). Multivariate data analysis applied to low-density polyethylene reactors. Chemometrics and Intelligent Laboratory Systems 14: 341.

40 McGregor, J.F. (1997). Using on-line process data to improve quality: challenges for statisticians. International Statistical Review 65: 309.

41 McGregor, J.F. and Brewer, M.J. (2017). Optimization of processes and products using historical data. FOCAPO/CPC (Foundation of Computer-Aided Process Operation/Chemical Process Control) Conference (8–12 January 2017), Tucson, Arizona. http://www.focapo-cpc.org/pdf/MacGregor.pdf (accessed 14 June 2021).

42 Munoz, S.G. and McGregor, J.F. (2016). Big data: success stories in the process industries. Chemical Engineering Progress 112 (3): 36.

43 Park, T.C., Kim, T.Y., and Yeo, Y.K. (2010). Prediction of the melt flow index using partial least squares and support vector regression in high-density polyethylene (HDPE) process. Korean Journal of Chemical Engineering 27: 1562.

44 Haykin, S. (2009). Neural Networks and Learning Machines, 3e. Hoboken, NJ: Pearson Education, Inc.

45 Johnson, R.A. and Wichern, D.W. (2013). Applied Multivariate Statistical Analysis, 6e. Hoboken, NJ: Pearson Education, Inc.

46 Dunn, K. (2019). Process improvement using data. https://learnche.org/pid/PID.pdf (accessed 11 June 2021).

47 Dunn, K. (2019). OpenMV.net Datasets. https://openmv.net (accessed 11 June 2021).

48 Aspen Technology, Inc. (2018). Aspen ProMV Brochure. https://www.aspentech.com/en/resources/brochure/aspen-promv-brochure (accessed 14 June 2021).

49 Breiman, L. (2001). Random forests. Machine Learning 45 (1): 5.

50 Sharma, N. and Liu, Y.A. (2022). A hybrid science-guided machine learning approach to modeling chemical processes: a review. AIChE Journal https://doi.org/10.10021/aic.17609.

51 Psichogios, D.C. and Ungar, L.H. (1992). A hybrid neural network-first principles approach to process modeling. AIChE Journal 38: 1499.

52 Thompson, M.L. and Kramer, M.A. (1994). Modeling chemical processes using prior knowledge and neural networks. AIChE Journal 40: 1328.

---

<!-- PDF page 88 -->

53 Agarwal, M. (1997). Combining neural and conventional paradigms for modelling, prediction and control. International Journal of Systems Science 28: 65.

54 Yang, S., Navarathna, P., Ghosh, S., and Bequette, B.W. (2020). Hybrid modeling in the era of smart manufacturing. Computers and Chemical Engineering 140: 106874.

55 Von Stosch, M., Oliveira, R., Peres, J., and de Azevedo, S.F. (2014). Hybrid semi-parametric modeling in process systems engineering: past, present and future. Computers and Chemical Engineering 60: 86.

56 O'Brien, C.M., Zhang, Q., Daoutidis, P., and Hu, W.-S. (2021). A hybrid mechanistic-empirical model for in silico mammalian cell bioprocess simulation. Metabolic Engineering 66: 31.

57 Pinto, J., de Azevedo, C.R., Oliveira, R., and von Stosch, M. (2019). A bootstrap-aggregated hybrid semi-parametric modeling framework for bioprocess development. Bioprocess and Biosystems Engineering 42: 1853.

58 Iwama, R. and Kaneko, H. (2020). Design of ethylene oxide production process based on adaptive design of experiments and bayesian optimization. https://www.authorea.com/doi/full/10.22541/au.160091365.52756748 (accessed 18 June 2021).

59 Madar, J., Abonyi, J., and Szeifert, F. (2005). Feedback linearizing control using hybrid neural networks identified by sensitivity approach. Engineering Applications of Artificial Intelligence 18: 343.

60 Rodriguez-Granrose, D., Jones, A., Loftus, H. et al. (2021). Design of experiment (DOE) applied to artificial neural network architecture enables rapid bioprocess improvement. Bioprocess and Biosystems Engineering 44: 1301.

61 Bollas, G., Papadokonstadakis, S., Michalopoulos, J. et al. (2003). Using hybrid neural networks in scaling up an FCC model from a pilot plant to an industrial unit. Chemical Engineering and Processing: Process Intensification 42: 697.

62 Asprion, N., Böttcher, R., Pack, R. et al. (2019). Gray-box modeling for the optimization of chemical processes. Chemie Ingenieur Technik 91: 305.

63 Beck, R. (2020). Hybrid modeling: the next generation of process simulation technology. https://www.aspentech.com/en/resources/blog/aspen-hybrid-models-the-next-generation-of-process-simulation-technology (accessed 18 June 2021).

64 Beck, R. and Munoz, G. (2020). Hybrid modeling: AI and domain expertise combine to optimize assets. https://www.aspentech.com/en/resources/white-papers/hybrid-modeling-ai-and-domain-expertise-combine-to-optimize-assets/?src=blog-global-wpt (accessed 18 June 2021).