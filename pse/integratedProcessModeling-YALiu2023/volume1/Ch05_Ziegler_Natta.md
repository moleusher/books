# 5. Ziegler-Natta Polymerization: HDPE, PP, LLDPE, and EPDM

<!-- PDF page 211 -->

## Ziegler–Natta Polymerization: HDPE, PP, LLDPE, and EPDM

This chapter deals with modeling of high-density polyethylene (HDPE), polypropylene (PP), linear low-density polyethylene (LLDPE), and ethylene-propylene-diene terpolymer (EPDM) manufacturing processes using Ziegler–Natta (ZN) catalyst. We use the simulation software Aspen Polymers for this study. We deal with the methodology and procedure to model the ZN polymerization kinetics.

We present an effective methodology for estimating the kinetic parameters based on plant data for the development of simulation and optimization models for commercial polyolefin processes using efficient software tools. We cover conceptual development, modeling methodology, illustrative examples, and hands-on workshops.

Section 5.1 introduces ZN polymerization. Section 5.2 discusses ZN polymerization kinetics. We cover catalyst-site activation, chain initiation, chain propagation, chain transfer, catalyst inhibition and deactivation, and copolymerization kinetics. Section 5.3 presents modeling considerations, including reactor types, polymer types, process flowsheets, molecular weight distributions (MWD), multimodal distributions, thermodynamics, and global kinetics versus local kinetics. Section 5.4 describes commercial polyolefin production targets, including general and polymer-specific production targets. Section 5.5 demonstrates an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient software tools, including data fit, sensitivity analysis, and design specification. This section also illustrates the applications of simulation models validated by plant data to process improvement. Section 5.6 presents a detailed hands-on workshop to develop the simulation model for the slurry HDPE process. Section 5.7 is a hands-on workshop to illustrate how to simulate and optimize a gas-phase PP process using stirred-bed reactors. Section 5.8 gives a hands-on workshop on producing LLDPE using a condensed mode cooling operation of a fluidized-bed process. Section 5.9 presents a hands-on workshop to simulate an ethylene-propylene rubber copolymer (EPM) or an EPDM by a metallocene catalyst system. The chapter also includes a Reference section.

---

<!-- PDF page 212 -->

### 5.1 Ziegler-Natta (ZN) Polymerization

#### 5.1.1 Introduction

ZN catalyst is one of the most widely used catalysts for manufacturing commercial HDPE, PP, LLDPE, and EPDM. Polyethylene and polypropylene are two commodity polymers with the highest demands. Polyolefins have a wide range of applications requiring different properties with different MWDs and branching distributions. The polymerization follows the coordination mechanism, which is different from the free radical polymerization mechanism used for producing high-pressure LDPE. The microstructure of polyolefins made with coordination catalysts is different from that made with free radical kinetics. The LDPE made using the free radical mechanism consists of both short-chain branching (SCB) and long-chain branching (LCB), while that made using the coordination mechanism consists of only SCB. Thus, catalyst design plays an important role in polyolefin processes. Different process types with different reactors and phases are other variables able to modify polyolefin properties. The process for producing polyolefins can be in three phases, including solution, slurry, and gas phase. Autoclaves/CSTR, loop reactors, and fluidized-bed reactors (FBRs) are some of the main reactors used for polyolefin processes in different phases. For example, the loop reactors are used for slurry-phase processes and FBRs are used for gas-phase processes. The book by Soares and McKenna [1] covers different polyolefin processes in detail.

The modeling of the ZN kinetics is complex because of the multiple active catalyst sites in the ZN catalyst. The most common type of ZN catalyst is titanium tetrachloride ( $ TiCl_{4} $) supported on  $ MgCl_{2} $ or  $ SiO_{2} $, which is heterogeneous in nature. ZN catalysts have high activity and productivity. Multiple active sites of the ZN catalyst enable the production of polymers with broad MWDs and allow good polymer microstructural control.

This chapter focuses mostly on ZN catalysts; other catalyst types, such as Phillips, metallocene, and late transition metal catalysts are discussed in chapters 3 and 5 of Soares and McKenna [1]. Phillips catalyst is similar to the ZN catalyst with multiple active sites and is used for producing HDPE consisting of chromium compounds like  $ CrO_{3} $ supported on  $ SiO_{2} $. Metallocene catalyst and late transition metal catalysts are used to produce HDPE/LLDPE with uniform properties and narrow MWD. The metallocene catalysts are considered to be single-site and homogeneous, i.e. soluble in the reaction medium. In Section 5.9, we present a hands-on workshop to simulate an EPM by a metallocene catalyst system. This chapter also does not deal with any processes that may use more than one catalyst type. Our limitation results from the lack of sufficient published plant data that would enable us to develop an effective methodology for kinetic parameter estimation for other catalyst types.

#### 5.1.2 Ziegler-Natta Catalysts

The ZN catalyst (Figure 5.1) requires a cocatalyst, AlR₃, such as triethyl aluminum (TEAL), Al(C₂H₅)₃, for activation. As shown in Figure 5.2, the cocatalyst is used

---

<!-- PDF page 213 -->

<div style="text-align: center;">Figure 5.1 The structure of ZN catalyst. Source: Soares and McKenna [1].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_391_146_801_332.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">Figure 5.2 ZN catalyst mechanism.</div>


 $$ \begin{array}{r l r}{\binom{\mathrm{L}\setminus\mathrm{A}\setminus\mathrm{X}}{\mathrm{L}\setminus\mathrm{X}}+\mathrm{~A I R}_{3}}&{{}\longrightarrow}&{\binom{\mathrm{L}\setminus\mathrm{A}^{\oplus}\mathrm{R}}{\mathrm{L}\setminus\mathrm{A}^{\oplus}}+\mathrm{~A I R}_{2}\mathrm{X}_{2}^{\ominus}}\end{array} $$ 

to alkylate the Ti salt to yield an active site. The catalyst and cocatalyst react in a series of reactions to form a complex. The cocatalyst extracts the chlorine atoms and transfers the alkyl group to the catalyst. Thus, the cocatalyst acts as a reducing agent, and the electron-deficient site acts as the active site initiating the polymerization.

### 5.2 Ziegler–Natta Polymerization Kinetics

The most important reactions in the ZN kinetics are the same as in any polymerization kinetics, namely, the chain initiation, propagation, and chain-transfer reactions, which can be with a monomer, hydrogen, or solvent. The ZN catalyst consists of different catalyst-site types, with each having its own relative reactivity because of variations in the local chemical composition of each site type. The catalyst activation, deactivation, and inhibition reactions are also specific to ZN catalyst. Site-activation reactions convert potential sites into active sites, while site-deactivation reactions convert active sites into dead sites. As discussed previously, Aspen Polymers builds the kinetic model in terms of repeating units or segments. We summarize the main reactions in ZN kinetics as follows.

#### 5.2.1 Catalyst Activation (ACT)

The catalyst site-activation step involves the generation of reactive, vacant, active sites from potential sites. There are several different site-activation reactions included in the built-in kinetic scheme. They include site activation by cocatalysts, electron donors, hydrogen, monomers, and spontaneous site activation (ACT-SPON). Different catalyst systems tend to be activated by a different subset of the reactions. The  $ TiCl_{4} $ catalyst is usually activated using TEAL cocatalyst or by spontaneous activation.

(1a) ACT-SPON: Spontaneous catalyst activation ( $ P_{0,i} $ is vacant site of type i):

 $$ \mathrm{CAT}_{i}\xrightarrow{k_{as,i}}\mathrm{P}_{0,i} $$ 

(1b) ACT-COCAT: Catalyst site activation by cocatalyst:

 $$ \mathrm{CAT}_{i}+\mathrm{COCAT}\xrightarrow{k_{act,i}}\mathrm{P}_{0,i} $$ 

---

<!-- PDF page 214 -->

(1c) ACT-H2: Catalyst site activation by hydrogen:

 $$ \mathrm{CAT}_{i}+\mathrm{H}_{2}\xrightarrow{k_{a c t h,i}}\mathrm{P}_{0,i} $$ 

#### 5.2.2 Chain Initiation (CHAIN-INI)

Chain initiation involves the reaction of a monomer molecule at a vacant active site to form a live polymer molecule of one unit length at that site. This reaction converts a vacant active site to a propagation site.

(2) CHAIN-INI: Chain initiation by monomer (M) ( $ P_{1,i} $ is a propagation site of type i with an attached polymer chain containing one segment):

 $$ \mathbf{P}_{0,i}+\mathbf{M}\xrightarrow{k_{ini,i}}\mathbf{P}_{1,i} $$ 

 $ (2') $ CHAIN-INI: Chain initiation by monomer  $ j(M_j) $ for copolymerization:

 $$ \mathrm{P}_{0,i}+\mathrm{M}_{j}\xrightarrow{k_{\mathrm{i n},i}^{j}}\mathrm{P}_{1,i}^{j} $$ 

#### 5.2.3 Chain Propagation (PROP)

The live polymer at each active site type grows or propagates through the addition of monomer molecules to form long polymer chains.

(3a) PROP: Chain propagation by monomer (M):

 $$ \mathrm{P}_{n,i}+\mathrm{M}\xrightarrow{k_{p,i}}\mathrm{P}_{n+1,i} $$ 

 $ P_{n,i} $ and  $ P_{n+1,i} $ are polymer chains of length n and  $ n+1 $ segments.

(3b) ATACT-PROP: Atactic propagation is a reaction considered in Aspen Polymers, accounting for the formation of atactic polymer (see Section 2.10.1 about tacticity and Figure 2.63), while the main propagation reaction represents the formation of all polymers, including isotactic or atactic.

 $$ \mathrm{P}_{n,i}+\mathrm{M}\xrightarrow{k_{\mathrm{p a},i}}\mathrm{P}_{n+1,i} $$ 

 $ k_{pa,i} $ is the rate constant for atactic chain propagation at site type i. We define the atactic fraction by dividing the amount of polymer produced by atactic propagation by that produced by total propagation:

 $$ \mathrm{A t a c t i c~f r a c t i o n}=(\mathrm{r a t e~o f~a t a c t i c~p r o p a g a t i o n})/(\mathrm{r a t e~o f~t o t a l~p r o p a g a t i o n}) $$ 

It is not possible to determine the rate constants for chain initiation and propagation separately because of the limited types of data measurements available from experiments. Therefore, we set the rate constant for ethylene or propylene monomer chain initiation equal to the rate constant for propagation of ethylene or propylene monomer on ethylene or propylene active segments. Likewise, we set rate constants for comonomer chain initiation equal to the rate constants for homopropagation of these monomers.

---

<!-- PDF page 215 -->

#### 5.2.4 Chain-Transfer Reaction (CHAT)

Chain transfer to monomer, solvent, or chain-transfer agent usually involves the extraction of hydrogen from the small molecule by the active site and leads to the termination of the live chain. At the same time, a new vacant site is formed, which can undergo chain initiation to start polymerization.

(4a) CHAT-MON: Chain transfer to monomer  $ (k_{\mathrm{tm},i}^{jk}) $ is the rate constant for chain transfer to a monomer of type k reacting with a growing chain transfer ending with a monomer unit of type j at site type i):

 $$ \mathrm{P}_{n,i}^{j}+\mathrm{M}_{k}\xrightarrow{k_{\mathrm{tm},i}^{jk}}\mathrm{D}_{n}+\mathrm{P}_{1,i}^{k} $$ 

(4b) CHAT-H2: Chain transfer to hydrogen (chain transfer to hydrogen generates a vacant site of type i,  $ P_{0,i} $.  $ D_n $ is a dead polymer chain of length n).

 $$ \mathrm{P}_{n,i}+\mathrm{H}_{2}\xrightarrow{k_{\mathrm{th},i}}\mathrm{D}_{n}+\mathrm{P}_{0,i} $$ 

(4b') CHAT-H2: Chain transfer to hydrogen for copolymerization (chain transfer to hydrogen and other transfer reactions generates a vacant site of type i,  $ P_{0,i} $.  $ D_n $ is a dead polymer chain of length n).

 $$ \mathrm{P}_{n,i}^{j}+\mathrm{H}_{2}\xrightarrow{k_{\mathrm{th},i}^{j}}\mathrm{D}_{n}+\mathrm{P}_{0,i}^{j} $$ 

#### 5.2.5 Catalyst Deactivation (DEACT)

The catalyst site deactivation involves the deactivation of active sites, vacant and propagation, to form dead sites. The catalyst site deactivation can occur spontaneously or by agents like cocatalyst, electron donors, hydrogen, monomers, or poisons. Different catalyst systems tend to be deactivated by different subsets of these reactions, but spontaneous catalyst deactivation is most common.

(5) DEACT-SPON: Spontaneous catalyst deactivation (DCAT $ _{i} $ is deactivated catalyst site of type i.  $ D_{n} $ is a dead polymer chain of n segments):

 $$ \mathrm{P}_{0,i}\xrightarrow{k_{\mathrm{d s},i}}\mathrm{DCAT}_{i} $$ 

 $$ \mathrm{P}_{n,i}\xrightarrow{k_{\mathrm{d s},i}}\mathrm{D}_{n}+\mathrm{DCAT}_{i} $$ 

#### 5.2.6 Catalyst Inhibition (INH)

Inhibited sites have small molecules such as hydrogen or poisons attached. As a result, inhibited sites are temporarily blocked from becoming propagation sites. The site-inhibition reaction is reversible. Therefore, the small molecule may dissociate from an inhibited site, which then becomes a vacant site once again.

---

<!-- PDF page 216 -->

(6) FSINH-H2 and RFINH-H2: Forward and reverse catalyst inhibitions by hydrogen (ICATi is the inhibited catalyst of site type i):

 $$  CAT_{i}+xH_{2}\xrightarrow{k_{finh,i}}ICAT_{i} $$ 

 $$  ICAT_{i}\xrightarrow{k_{rinh,i}}CAT_{i}+xH_{2} $$ 

#### 5.2.7 Copolymerization Kinetics

Comonomers are used to produce polyolefins of varying densities. We assume that the rate of propagation of a monomer (or comonomer) depends only on the active segment (last monomer added to the chain) and the propagating monomer. This is commonly referred to as the terminal model for copolymerization kinetics.

(7) COMONOMER-PROP: For a system with two monomers, we write the propagation reactions as follows  $ (k_{p,i}^{jk} $ is the rate constant for propagation, associated with site type i, for a monomer of type k adding to a chain with an active segment of type j):

 $$ \mathrm{P}_{n,i}^{1}+\mathrm{M}_{1}\xrightarrow{\stackrel{k_{\mathrm{p},i}^{11}}{\longrightarrow}}\mathrm{P}_{n+1,i}^{1} $$ 

 $$ \mathrm{P}_{n,i}^{1}+\mathrm{M}_{2}\xrightarrow{\stackrel{k_{\mathrm{p},i}^{12}}{\longrightarrow}}\mathrm{P}_{n+1,i}^{2} $$ 

 $$ \mathrm{P}_{n,i}^{2}+\mathrm{M}_{1}\xrightarrow{\stackrel{k_{\mathrm{p},i}^{21}}{\mathrm{P}_{n+1,i}^{1}}}\mathrm{P}_{n+1,i}^{1} $$ 

 $$ \mathrm{P}_{n,i}^{2}+\mathrm{M}_{2}\xrightarrow{\stackrel{k_{\mathrm{p},i}^{22}}{\mathrm{P}_{n+1,i}}}\mathrm{P}_{n+1,i}^{2} $$ 

We note that the reaction rate constants listed in the chemical reactions above have the following standard Arrhenius form:

 $$ k=k_{0}*\mathrm{e}^{-\frac{E}{R}\left(\frac{1}{T}-\frac{1}{T_{\mathrm{r}}}\right)} $$ 

where  $ k_{0} $ is the pre-exponential factor, E is the activation energy, R is the ideal-gas constant, T is the temperature of the reaction system, and  $ T_{r} $ is the reference temperature.

We discuss below our reasoning for including certain model reactions and our simplification in ignoring other model reactions [1].

(1) Touloupidis [2] and Zacca and Ray [3] include the catalyst site activation by monomer (ACT-MON) and by electron donor (ACT-EDONOR) in their modeling studies. These reactions are available within the ZN kinetic model in Aspen Polymers when needed.

---

<!-- PDF page 217 -->

(2) Chain transfer to transfer agent (CHAT-AGENT), to solvent (CHAT-SOL), to cocatalyst (CHAT-COCAT), to electron donor (CHAT-EDONOR) follows a similar reaction to (4b), chain transfer to hydrogen (CHAT-H2). These reactions are available within the ZN kinetic model in Aspen Polymers. We ignore them as in Refs. [4, 5].

(3) Zhang et al. [6] include the beta-hydride elimination in their slurry HDPE modeling study. Soares and McKenna [1, p. 162] state that this reaction produces metal hydride sites that are indistinguishable from those made by chain transfer to hydrogen. Therefore, it would be appropriate to consider only the reaction of chain transfer to hydrogen, without the reaction of beta-hydride elimination, as in Refs. [4, 5].

(4) After considering chain-transfer reactions, Touloupidis [2] includes site-transformation reactions that convert one vacant catalyst-site type to another by means of specific reactions, such as transformation to hydrogen, to cocatalyst, to solvent, and to poison, as well as spontaneous site transformation. Touloupidis further states that “site transformation reactions do not seem to play an important role, as they are rarely employed. Moreover, they pose difficulties on the way site transformation can be experimentally measured and validated” [2, p. 518]. Therefore, we ignore site-transformation reactions.

(5) As explained in Ref. [7], by adding hydrogen to polyolefin processes with ethylene as a monomer, the rate of polymerization decreases. We can model this effect by including the forward and backward catalyst site-inhibition reactions because of hydrogen (FSINH-H2 and RFINH-H2). The rate constants of these inhibition reactions affect the polymer production rate. The Aspen Polymers model also calculates the equilibrium mole of inhibited catalyst sites (CISFRAC).

(6) In certain polyolefin systems, such as HDPE [4], we may get a bimodal homopolymer from a single reactor. This is different from the bimodal copolymer produced in a reactor series for HDPE [6, 8, 9], PP [10, 11], or LLDPE [12] because of the difference in the hydrogen concentrations of the two reactors in series. We can model this bimodal copolymer by the forward and reverse catalyst–hydrogen-inhibition reactions (FSINH-H2 and RFINH-H2) [4]. The Aspen Polymers model also calculates the equilibrium mole fraction of inhibited catalyst sites (CISFRAC).

(7) Many HDPE [4, 6, 8, 9, 13], PP [5, 10, 11] and LLDPE [12] models include the reaction of spontaneous catalyst deactivation (DEACT-SPON). For PP, the tacticity-control agent deactivates a portion of the catalyst sites that produce atactic polymer. We account for this by the reaction of catalyst deactivation by tacticity-control agent (DEACT-TCA) [5]. The Aspen Polymers model also includes catalyst deactivation reactions by hydrogen (DEACT-H2), by cocatalyst (DEACT-COCAT), by monomer (DEACT-MON), by poison (DEACT-POISON), and by electron donor (DEACT-EDONOR), as listed in Ref. [2]. In our workshops, we include DEACT-POISON and DEACT-H2 reactions.

---

<!-- PDF page 218 -->

<div style="text-align: center;">Table 5.1 Examples of common reactors for producing polyolefins.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>Stirred autoclave, or continuous stirred-tank reactor (CSTR)</td><td style='text-align: center; word-wrap: break-word;'>Slurry-loop reactors (SLRs)</td><td style='text-align: center; word-wrap: break-word;'>Fluidized-bed reactors (FBRs)</td><td style='text-align: center; word-wrap: break-word;'>SLRs + FBRs</td><td style='text-align: center; word-wrap: break-word;'>Stirred-bed reactors (SBRs)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE</td><td style='text-align: center; word-wrap: break-word;'>Mitsui slurry process [4, 6, 8]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Borstar bimodal process [9, 13]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Loop reactor series [14, 15]</td><td style='text-align: center; word-wrap: break-word;'>Univation UNIPOL [16]</td><td style='text-align: center; word-wrap: break-word;'>Basell Spheripol process [5, 10, 11], HYPOL process [19, 20]</td><td style='text-align: center; word-wrap: break-word;'>Innovene [5]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LLDPE</td><td style='text-align: center; word-wrap: break-word;'>DOWLEX solution process [1, 17]</td><td style='text-align: center; word-wrap: break-word;'>Loop reactor series [12]</td><td style='text-align: center; word-wrap: break-word;'>Basell Spherilene [17], Univation UNIPOL [18]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

### 5.3 Modeling Considerations

#### 5.3.1 Reactor Types

Chapter 4 of Soares and McKenna [1] describes the various types of reactors used for polyolefin processes, depending on the type of polyolefin, process technology, and reactant phase. The most common reactors used in polyolefin processes are stirred autoclave or continuous stirred-tank reactor (CSTR), loop reactor, fluidized-bed reactor (FBR), and horizontal stirred-bed reactor (HSBR). The modeling of the reactors requires certain assumptions.

Table 5.1 gives examples of common reactor types in commercial polyolefin processes. We can model the stirred autoclave reactors in the Mitsui slurry HDPE process [4, 6, 8] and in the DOWLEX solution LLDPE process [17] as CSTRs. Loop reactors are used in the Borstar slurry HDPE process [1, p. 120; 9, 13] as well as the Basell Spheripol [1, 10, 11, p. 106] and Mitsui HYPOL [14, 19] PP processes. In the modeling of a loop reactor, when the recycle ratio is 30 or higher, as calculated by Zacca and Ray [3], we can simulate the loop reactor as a CSTR. High recycle ratios give very low axial concentration gradient of the reactant and uniform temperature and residence time distribution (RTD), so that we can model a loop reactor as a CSTR. The loop reactors have a higher space–time yield and a high ratio of heat transfer per unit volume. Luo et al. [14], Zheng [15], among others, have modeled the loop reactor series as CSTRs for PP production.

FBRs are mainly used for gas-phase and mixed-phase processes, such as the Borstar bimodal HDPE [8, 9], Basell Spheripol PP [10, 11], Mitsui HYPOL PP [19, 20], Basell Spherilene [17], and Univation UNIPOL [18] LLDPE processes. FBRs have a high overall conversion as well as high heat-removal capacity. FBRs are mostly used as a finishing reactor for making copolymers in a serial polyolefin

---

<!-- PDF page 219 -->

process, as varying levels of comonomers can be added without any solubility issues. The high recycle ratios of the recycle gas lead to uniform temperatures and low concentration gradients in the FBRs, making it reasonable to model the FBR as a CSTR. Chen et al. [13] and Zhao et al. [9] have modeled the FBR as a CSTR in the finishing reactor for making bimodal HDPE.

The HSBR has been used for gas-phase polymerization processes, such as the Innovene (formerly BP Amoco) PP process [5]. It has a plug-flow characteristic and can be used for fast grade change and making a wide variety of products. We can simulate the HSBR as a series of CSTRs to approximate the RTD of the plug flow [5].

#### 5.3.2 Process Flowsheets

Figures 5.3–5.8 illustrate the simplified flowsheets of several commercial polyolefin production processes that we use below to demonstrate our methodology for kinetic parameter estimation from plant data using simulation software tools.

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_533_776_797.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.3 Mitsui slurry HDPE process: serial reactor configuration. Source: Khare et al. [4]/American Chemical Society.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_130_885_776_1180.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.4 Borstar bimodal HDPE process with a prepolymerization reactor, a slurry-loop reactor (SLR), a flash unit, and a finishing fluidized-bed reactor (FBR). Source: Adapted from Zhao et al. [9]/American Chemical Society.</div>


---

<!-- PDF page 220 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_143_811_411.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.5 Polymerization section of the Mitsui HYPOL PP process: C201, C202, and C203 – compressors; D201 and D202 – slurry polymerization reactor (SLR); D203 – fluidized-bed reactor (FBR); D221, D222, and D228 – flash drum; E201, E202, E203, and E208 – heat exchanger. Source: Adapted from Luo et al. [20]/Elsevier publishers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_542_808_917.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.6 Basell Spheripol PP process using two slurry-loop reactors (SLRs), followed by a flash unit and a fluidized-bed reactor (FBR) for copolymerization. Source: Adapted from Soares and McKenna [1] Wiley-VCH.</div>


#### 5.3.3 Polymer Types

HDPE, PP, and LLDPE are mostly made using ZN catalysts. The strategy for process modeling and kinetic parameter estimation does not change when considering different polymers. We only need to include certain reactions specific to the polymers. For HDPE processes, it is appropriate to consider the forward and reverse catalyst-inhibition reactions by hydrogen (FSINH-H2 and RFINH-H2) since the rate of polymerization for ethylene polymer decreases with the addition of hydrogen. For PP processes, we may consider the atactic propagation reaction (ATACT-PROP), depending on the atactic content of the polymer. The atactic

---

<!-- PDF page 221 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_127_782_547.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.7 Innovene gas-phase PP process using a horizontal stirred-bed reactor. Source: Khare et al. [5]/American Chemical Society.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_636_772_981.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.8 Univation UNIPOL LLDPE process using a fluidized-bed reactor. Source: Adapted from Seavey et al. [21] American Chemical Society.</div>


polymer is amorphous and has a low commercial value; it is desirable to have a high isotactic PP (see Figure 2.63).

#### 5.3.4 Molecular Weight Distribution (MWD) and Multi-Modal Distributions

The MWD of the polymer can be unimodal or multimodal, depending on the operating conditions. The kinetic estimation and modeling strategy remain the same,

---

<!-- PDF page 222 -->

whether the MWD distribution is unimodal or bimodal. The homopolymer MWD is usually unimodal.

For obtaining bimodal MWD in many polyolefin processes, the catalyst is exposed to two different operating conditions in a cascade of reactors. We can use two reactors in series to produce bimodal HDPE. The first reactor makes a low-MWN HDPE with the help of a high hydrogen concentration, while the second reactor has a low hydrogen concentration and produces a high-molecular-weight polymer. A comonomer alpha olefin is often added to make a copolymer. Chen et al. [13] and Meng et al. [8] have modeled the Borstar HDPE process to predict the bimodal MWD. In the Borstar process, the low-molecular-weight homopolymer is made in the slurry-loop reactor (SLR) and the high-molecular-weight copolymer is made in the FBR. There can be other reasons for obtaining a bimodal MWD apart from operating conditions if we obtain a bimodal MWD in a single reactor. The other reasons for bimodal MWD can be different types of reacting sites in the catalyst, inhibition of catalyst sites because of hydrogen or other poisoning, and nonideal mixing in the reactor [22].

#### 5.3.5 Thermodynamics

Thermodynamics is an essential part of process modeling. The polymer perturbed-chain statistical fluid theory (POLYPCSF) is one of the most useful thermodynamic models for simulating polyolefin processes [5, 22]. The POLYPCSF model is based on perturbation theory. The underlying idea is to divide the total intermolecular forces into repulsive and attractive contributions. The model uses a hard-chain reference system to account for the repulsive interactions. The attractive forces are further divided into different contributions, including dispersion, polar, and association.

Another popular model for phase equilibrium in polyolefin processes is the Polymer Sanchez-Lacombe (POLYSL) equation of state [23–25]. It is based on the lattice theory, which states that fluids are mixtures of molecules and holes that are confined to sites in a lattice.

We refer our readers to Chapter 2 for the details of the POLYSL (Section 2.6) and POLYPCSF (Section 2.8) models, and the guidelines for the selection of thermodynamic models for polymer process simulation.

A correct thermodynamic model is very important in predicting certain commercial targets like the polymer solution density (not the polymer pellet density, which depends on weight-average molecular weight [MWW] and SCB content [8, 26]). We use the polymer solution density to match the reactor residence time before estimating the kinetic parameters.

#### 5.3.6 Global Kinetics Versus Local Kinetics

Reaction kinetics, like thermodynamics, is expected to be a global phenomenon [27]. If the same catalyst is used in all the reactors, a good model should be capable of covering the full range.

---

<!-- PDF page 223 -->

Using different kinetics in different reactors significantly raises the degrees of freedom in the problem, which is already quite complex. We should instead treat the data from the different stages of the process as a sort of “natural experiment” to further confirm a single set of rate parameters.

If we had samples after each stage, we could use the MWD to further enrich our understanding of what is happening within the process.

We have seen projects where engineers have used different kinetics in different reactors or different kinetics for different product grades. We have also seen in some cases of force-fitting the kinetics that the concentration of catalyst sites per unit mass of catalyst (max sites) is not realistic (outside of the range of 1E-5 to 1E-3 mol of sites per gram of catalyst [4]), or the inhibition reaction and catalyst poisoning reaction rate constants may not be correct, resulting in the incorrect catalyst activity predicted by the model. We always consider these as symptoms of an imperfect model. Using local kinetic models may be “over-fitting” the limited available data, which can lead to bad extrapolations away from the base-case conditions. Since the goal of modeling is usually to optimize the process to increase throughput, improve quality, or reduce energy consumption, it is important to be able to predict behavior outside the current operating envelope.

Additionally, when fitting a kinetic model, we should always use the reference temperature form of the kinetic expression, Eq. (5.1). This form makes the pre-exponential factor  $ k_{0} $ and the activation energy E independent of each other at  $ T_{r} $. Otherwise, small changes to E overwhelm the data fitting of the k values, and the fitting algorithm usually fails. We also find it easier to compare rate constants when they are on a consistent reference temperature basis.

### 5.4 Commercial Polyolefin Production Targets

The important commercial production targets for kinetic parameter estimation of polyolefin processes are as follows.

#### 5.4.1 General Production Targets

##### 5.4.1.1 Production Rate

We use the mass flow rate of polymer within the outlet stream from each reactor for a process with reactors in series for kinetic parameter estimation. It is an essential production target for process modeling since the production rates are important when considering production rate expansion for a process. The propagation reaction determines the polymerization rate and hence directly affects the production rate.

##### 5.4.1.2 MWN

The MWN of the polymer is an important target. MWN varies for different polymer grades. The reaction rate constants for chain transfer to  $ H_{2} $ (CHAT-H2) and to monomer (CHAT-MON) significantly affect the molecular weight of the polymer since the reactions lead to breaking growing polymer chains and forming dead polymer chains.

---

<!-- PDF page 224 -->

##### 5.4.1.3 MI

In the literature, most empirical correlations for polyolefin melt index (MI) with broad MWD or large polydispersity index (PDI) are based on the MWW. For example, a general MI correlation with MWW is in the form of [21, 28]:

 $$ \mathrm{MI}=a(\mathrm{MWW})^{-b} $$ 

where a and b are correlating parameters. For PP, the MI may depend on the MWW as well as the atactic fraction (ATFRAC), calculated by the atactic chain-propagation reaction (ATACT-PROP) [29].

##### 5.4.1.4 Conversion

The conversion percentages of the monomer and the comonomer are required to determine the yield of the process.

##### 5.4.1.5 PDI

The PDI is the ratio of the weight-average molecular weight to the number-average molecular weight (MWW/MWN). It is an important polyolefin property. It is measured by performing gel-permeation chromatography (GPC) on the polyolefin sample obtained at the product outlet or at each reactor outlet in a process with reactors in series.

##### 5.4.1.6 SMWN and SPFRAC

SMWN represents the MWN produced at each active catalyst site. SPFRAC is the weight fraction of polymer produced at each active site. They are determined by deconvolution of the polymer GPC curve and are required for estimating individual site-specific kinetic parameters. See Section 5.5.2.3.

##### 5.4.1.7 SFRAC and SCB

SFRAC is the mole fraction of segments of the comonomer and is usually determined by the short chain branching distribution (SCBD). The use of online Fourier transform infrared spectroscopy (FTIR) with GPC permits the detection of the SCB as a function of the MWW [26]. We use this simulation target to predict the comonomer content in the copolymer. SFRAC depends on the comonomer kinetics.

##### 5.4.1.8 Rho

The polymer density is usually measured for the pellets and correlated as a function of the MWW. For copolymerization, we often correlate the polymer density as a function of mole fraction of the comonomer and the MWW [8, 26]. In Ref. [8], the HDPE density obtained from ethylene copolymerization with comonomer 1-butene follows the following correlation:

 $$ \rho=(1-0.009165x\mathrm{B}^{0.148895})\times[1.137247-0.014314\ln(\mathrm{MWW})] $$ 

where xB is the mole fraction of 1-butene. In Ref. [28], we see an example of correlating the polymer density to MWW and SCB content for a bimodal HDPE

---

<!-- PDF page 225 -->

copolymer process:

 $$ \rho=1.0748-0.0241\log MWW-0.01145\left(\frac{\sum_{j=1}^{N}m(j)SCB(j)w_{\log MWW}(j)}{\sum_{j=1}^{N}m(j)w_{\log MWW}(j)}\right)^{2} $$ 

where  $ m(j) $ is mass fraction of polymer formed at active site j,  $ SCB(j) $ is the average SCB in copolymers formed at active site j, and  $ w_{\log MWW}(j) $ is the weight chain length distribution (WCLD) of the polymer formed at active site j.

##### 5.4.1.9 Residence Time

This refers to the reactor’s residence time. It can be the residence time of each reactor in a process with a series of reactors. It is an important target affecting the polymer properties. The residence time is dependent on the polymer solution density, which depends on the thermodynamic property parameters.

#### 5.4.2 Polymer-Specific Targets

##### 5.4.2.1 CISFRAC

It is the ratio of the moles of the inhibited catalyst sites to the total number of moles of the catalyst sites. It may be considered a target for the HDPE process when catalyst-inhibition reactions are considered.

##### 5.4.2.2 ATFRAC

It is the ratio of the atactic propagation to the total propagation. It is a commercial target for atactic PP production.

Table 5.2 gives examples of production targets for kinetic parameter estimation for modeling commercial polyolefin processes from plant data.

We conclude this section, noting two points.

(1) Not all production targets are fully independent of each other. As an example, MI typically depends on MWW for most polyolefins and depends on atactic fraction (ATFRAC) for PP. In our simulation, we use a FORTRAN (“Calculator”) block to calculate the MI based on a correlation developed from past plant data using MWW and compare the calculated MI value with the current plant data. If the resulting deviation between the calculated and measured MI values is not acceptable, we would fine-tune the simulation parameters for better MWW predictions and possibly update the MI–MWW correlation with new plant data.

(2) Not all suggested production targets in reported modeling studies have the relevant plant data for model validation. Depending on the intended purposes for using the resulting simulation model and the accuracy requirements of model predictions, the model developers must decide if they wish to make a serious effort to collect plant data for certain production targets for validating the simulation model. Alternatively, they could use available data for relevant process variables or the values of simulation output variables as independent variables to develop soft sensors or inferential models (such as those based on neural networks [32]) for production targets (e.g. MI and ATFRAC) that are not routinely measured.

---

<!-- PDF page 226 -->

<div style="text-align: center;">Table 5.2 Examples of production targets for kinetic parameter estimation for modeling commercial polyolefin processes from plant data.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Polymer [References]</td><td style='text-align: center; word-wrap: break-word;'>Production rate</td><td style='text-align: center; word-wrap: break-word;'>MWN and MI</td><td style='text-align: center; word-wrap: break-word;'>Conversion</td><td style='text-align: center; word-wrap: break-word;'>SFRAC</td><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'>Rho</td><td style='text-align: center; word-wrap: break-word;'>SMWN and SPFRAC</td><td style='text-align: center; word-wrap: break-word;'>Resolution time</td><td style='text-align: center; word-wrap: break-word;'>Polymer specific</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Khare et al. [4]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chen et al. [13]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Zhang et al. [6]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Meng et al. [8]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Zhao et al. [9]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Khare et al. [5]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Zheng et al. [10]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Luo et al. [14]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>You and Li [19]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Luo et al. [20]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Kou et al. [30, 31]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LLDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Touloupidis et al. [12]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LLDPE,</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Kashani et al. [18]</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

### 5.5 Methodology for Polyolefin Kinetic Estimation

Table 5.3 summarizes the important commercial production targets that we have considered for kinetic parameter estimation. The number of targets that can be used for estimation depends on data availability. In our strategy for estimating kinetic parameters, we first try to match some production targets in a single-catalyst-site model, and we fit the remaining targets after converting the single-site model

---

<!-- PDF page 227 -->

<div style="text-align: center;">Table 5.3 Production targets for single-site and multisite models.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Single-site targets</td><td style='text-align: center; word-wrap: break-word;'>Multisite targets</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Production rate</td><td style='text-align: center; word-wrap: break-word;'>PDI of polymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN overall</td><td style='text-align: center; word-wrap: break-word;'>MWN produced at catalyst site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Monomer conversion</td><td style='text-align: center; word-wrap: break-word;'>Mass fraction for polymer produced at each site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Comonomer conversion or SFRAC</td><td style='text-align: center; word-wrap: break-word;'>Atactic fraction (ATFRAC) for each site for PP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polymer solution density</td><td style='text-align: center; word-wrap: break-word;'>Catalyst site-inhibition fraction CISFRAC for each site for HDPE</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Residence time</td><td style='text-align: center; word-wrap: break-word;'>Rho/Polymer pellet density</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Atactic fraction (ATFRAC) for PP</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

into a multisite model. In this procedure, we consider the rate constants for all the reactions involved in the ZN polyolefin kinetics, including catalyst activation, initiation, propagation, chain transfer, deactivation, and other polymer-specific reactions. The kinetic rate constants follow the Arrhenius form given in Eq. (5.1). As mentioned in Section 4.4.8, for polyolefin reactors operating in a small temperature range, we only estimate the pre-exponential factor  $ k_{0} $ and keep the activation energy E constant with values from the literature. Our methodology for kinetic parameter estimation does allow us to estimate the activation energy if necessary.

#### 5.5.1 Efficient Use of Software Tool: Data Fit

We develop models using Aspen Polymers and fit the kinetic parameters to plant data using the data-fit tool, previously introduced in Chapter 3. Data fit is an efficient nonlinear regression tool that allows the user to determine statistically acceptable kinetic parameters from constant, time-varying, or temperature-dependent laboratory measurements or from matching the process simulation to plant targets. We can use point data or time-profile data for regression. We need to define the data with reconciled input variables and a standard deviation. We estimate the model parameters using the data within the specified range. We refer the reader to Section 3.8 for more discussion of the principle of data fit and will illustrate its application in Section 5.5.2.1 below.

#### 5.5.2 Flowchart of the Methodology for Kinetic Parameter Estimation

Figure 5.9a shows our methodology for estimating kinetic parameters for polyolefin process models from plant data using simulation software tools, and Figure 5.9b shows an expanded version of the methodology. In the following, we discuss the details of the algorithm and present illustrative applications to commercial polyolefin processes. We also give some useful suggestions based on our experiences in guiding practicing engineers to apply the methodology to several dozen commercial HDPE, PP, LLDPE, and EPDM processes in the Asia-Pacific.

---

<!-- PDF page 228 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_806_417.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.9a The methodology for kinetic parameter estimation for polyolefin process models from plant data using simulation software tools.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_511_817_994.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.9b An expanded version of the methodology for kinetic parameter estimation for polyolefin process models from plant data using simulation software tools.</div>


##### 5.5.2.1 Multiple Product Grades and Single Active Catalyst Site

We first make a single-site model and try to estimate the kinetic parameters based on single-site production targets for multiple product grades. Using the production rate data for multiple grades, the data-fit tool enables us to simultaneously regress the reaction rate constants for catalyst activation (ACT-SPON, ACT-COCAT, and ACT-H2), propagation (PROPAGATION) reactions for monomers, deactivation (DEAC-SPON) reactions, and any inhibition (FSINH-H2 and RSINH-H2) reactions.

---

<!-- PDF page 229 -->

if considered. This is different from most of the previous studies, including our previous work [4, 5], which sequentially estimates these reaction rate constants.

Before matching the production rates, we must ensure that the residence time matches plant data. We can adjust the PC-SAFT thermodynamic parameters and change the mixing model equation to adjust the polymer solution density. The residence time of the reactor depends on the solution density.

We estimate the rate constants for propagation (PROPAGATION) reactions for the monomer using the production rate for the homopolymer and monomer conversion. We use the production rate for the copolymer and the ratio of the reaction rates of comonomer to monomer (SFRAC) or conversion of comonomer to estimate the rate constants of the propagation reactions for the comonomer.

For PP, we need to ensure that the isotacticity of the homopolymer matches the plant data. We do so by including the atactic propagation (ATACT-PROP) reaction and estimating the rate constant using the atactic fraction (ATFRAC), which is the ratio of the atactic polymer formed over the total polymer. We want the calculated ATRAC to be close to  $ [1 - \text{isotacticity}/100] $.

For HDPE, we also consider the inhibition of the catalyst because of the polymers since the rate of polymerization decreases with hydrogen concentration for ethylene-based polymer reactions. We usually estimate the forward inhibition and backward inhibition (FSINH-H2 and RSINH-H2) reactions using the MWN. In the single-site model, we can also match the MWWs and use them to estimate the rate constants of chain transfer to hydrogen and monomer/comonomer.

Depending on the available data, the melt index of polymer is also useful in matching the molecular weight of polymer. Melt index is usually a function of MWW, but in the case of polypropylene homopolymer, it is also a function of atactic fraction (ATFRAC). See Section 2.10.1.

In case SFRAC and comonomer content data are not available, we may use the final polymer pellet density to estimate the comonomer propagation rate constants, as the polymer density depends on the SCB and comonomer content.

Table 5.4 shows the major kinetic parameters that significantly affect the single-site production targets.

We illustrate the application of the methodology to estimating the kinetic parameters for modeling a commercial Mitsui HYPOL PP process.  $ \underline{\text{Supplement 5.1 [29]}} $ gives details of six polyolefin process modeling examples, including the process description, polymerization reactions, production targets, estimated rate constants, sensitivity analysis, and model validations.

We demonstrate below the efficient use of data-fit tool for the simultaneous estimation of kinetic parameters.

Table 5.5 lists the plant data for single-site modeling for a commercial Mitsui HYPOL PP process of Figure 5.5, and Figure 5.10 shows an Aspen Polymers simulation flowsheet of the process with the addition of one more fluidized-bed reactor, D204.

To simplify the kinetic parameter estimation, we begin by setting some kinetic parameters to be equal. For example, we make the pre-exponential factors for propagation (PRPRE-EXP) from ethylene segment (C2-SEG) and from propylene segment

---

<!-- PDF page 230 -->

<div style="text-align: center;">Table 5.4 Major kinetic parameters affecting the single-site production target.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Single-site target</td><td style='text-align: center; word-wrap: break-word;'>Major kinetic parameters affecting the target</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Production rate</td><td style='text-align: center; word-wrap: break-word;'>Max sites parameter, propagation rate constant, catalyst activation, inhibition reaction</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN overall</td><td style='text-align: center; word-wrap: break-word;'>Chain-transfer reactions - monomer and  $ H_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Monomer conversion</td><td style='text-align: center; word-wrap: break-word;'>Monomer propagation rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Comonomer conversion or SFRAC</td><td style='text-align: center; word-wrap: break-word;'>Comonomer propagation rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reactor residence time</td><td style='text-align: center; word-wrap: break-word;'>Polymer solution density and thermodynamic property parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ATFRAC</td><td style='text-align: center; word-wrap: break-word;'>Atactic propagation rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Melt Index</td><td style='text-align: center; word-wrap: break-word;'>Chain-transfer reactions and ATF-RAC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polymer pellet density</td><td style='text-align: center; word-wrap: break-word;'>Comonomer content/comonomer propagation rate constants</td></tr></table>

<div style="text-align: center;">Table 5.5 Plant data for kinetic modeling a commercial Mitsui HYPOL PP process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Dataset</td><td style='text-align: center; word-wrap: break-word;'>Process parameters</td><td style='text-align: center; word-wrap: break-word;'>Reactor</td><td style='text-align: center; word-wrap: break-word;'>Grade 1 Production target</td><td style='text-align: center; word-wrap: break-word;'>Grade 2 Production target</td></tr><tr><td rowspan="3">PROD123</td><td rowspan="3">Polymer production rate (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>1560</td><td style='text-align: center; word-wrap: break-word;'>1560</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>3120</td><td style='text-align: center; word-wrap: break-word;'>3120</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>6240</td><td style='text-align: center; word-wrap: break-word;'>6240</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROD4</td><td rowspan="4">Number-average molecular weight (MWN)</td><td style='text-align: center; word-wrap: break-word;'>D-204</td><td style='text-align: center; word-wrap: break-word;'>8600</td><td style='text-align: center; word-wrap: break-word;'>8600</td></tr><tr><td rowspan="3">MWN123</td><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>60,000</td><td style='text-align: center; word-wrap: break-word;'>76,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>63,000</td><td style='text-align: center; word-wrap: break-word;'>83,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>77,000</td><td style='text-align: center; word-wrap: break-word;'>88,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN4</td><td rowspan="2">Ethylene content in copolymer (mole fraction)</td><td style='text-align: center; word-wrap: break-word;'>D-204</td><td style='text-align: center; word-wrap: break-word;'>80,000</td><td style='text-align: center; word-wrap: break-word;'>96,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFRAC4</td><td style='text-align: center; word-wrap: break-word;'>D-204</td><td style='text-align: center; word-wrap: break-word;'>0.145</td><td style='text-align: center; word-wrap: break-word;'>0.15</td></tr><tr><td rowspan="4">PDI</td><td rowspan="4">Polydispersity index</td><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>5.50</td><td style='text-align: center; word-wrap: break-word;'>5.60</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>5.52</td><td style='text-align: center; word-wrap: break-word;'>5.70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>5.54</td><td style='text-align: center; word-wrap: break-word;'>5.80</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-204</td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'>6.20</td></tr><tr><td rowspan="3">H2/C3H6 mole ratio  $ \times $ 10E3</td><td rowspan="3">H2/monomer mole ratio in reactor overhead</td><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>188</td><td style='text-align: center; word-wrap: break-word;'>17</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>209</td><td style='text-align: center; word-wrap: break-word;'>9.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>1.7</td></tr></table>

Source: Adapted from You [33].

---

<!-- PDF page 231 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_153_783_422.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.10 An Aspen Polymers simulation flowsheet of the Mitsui HYPOL PP process.</div>


(C3-SEG) to ethylene comonomer (C2H4) equal. Therefore, we use a Calculator (FORTRAN block) to make PRPRE-EXP PROPAGATION (C2-SEG/C2H4) equal to PRPRE-EXP PROPAGATION (C3-SEG/C2H4). Supplement 5.1a gives additional details about this simplification.

Our data fit application includes the simultaneous execution of two regression runs for the first three reactors, D201–D203, and a regression run for the fourth reactor, D204, that focuses on copolymer production. First, regression run RPROD123 varies the pre-exponential factors for spontaneous site activation (ACT-SPON), catalyst activation by cocatalyst (ACT-COCAT), propagation (PROPAGATION) reactions for monomer, and deactivation (DEAC-SPON) reactions to match dataset PROD123 listed in Table 5.6. Next, regression RMWN123 varies the pre-exponential factors for chain transfer of propylene segment and of ethylene segment to H2 and to propylene monomer to match dataset MWN123. Lastly, regression RD204 varies the pre-exponential factors for chain propagation of propylene segment and from ethylene segment to comonomer C2H4 and chain transfer from propylene segment and from ethylene segment to comonomer C2H4 to match the datasets PROD4, MWN4, and SFRAC4.

Table 5.6 demonstrates that the data-fit tool enables us to accurately estimate the kinetic parameters for the single-site model that have the most impacts on specific production targets (see Table 5.4) for the Mitsui HYPOL PP process. The comparison between model predictions and production targets shows minimum errors of 0.37–3.22%.

##### 5.5.2.2 Multisite Model and Deconvolution Analysis

We now convert our single-site model into a multisite model by changing the specified number of sites in the model. We then make use of the gel permeation chromatography (GPC) analysis of the polymer samples.

Using the GPC characterization data, we apply the deconvolution procedure first presented by Soares and Hamielec [34]. We deconvolute the MWD to determine the most probable CLD for each active catalyst site. We assume that the CLD of the polyolefins produced by each active site of ZN catalyst follows the Flory distribution.

---

<!-- PDF page 232 -->

<div style="text-align: center;">Comparison of single-site model predictions with production targets obtained by data fit.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Polymer production (kg/hr)</td><td colspan="4">Grade one</td><td colspan="3">Grade two</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D201</td><td style='text-align: center; word-wrap: break-word;'>D202</td><td style='text-align: center; word-wrap: break-word;'>D203</td><td style='text-align: center; word-wrap: break-word;'>D201</td><td style='text-align: center; word-wrap: break-word;'>D202</td><td style='text-align: center; word-wrap: break-word;'>D203</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Plant data</td><td style='text-align: center; word-wrap: break-word;'>1560</td><td style='text-align: center; word-wrap: break-word;'>3120</td><td style='text-align: center; word-wrap: break-word;'>6240</td><td style='text-align: center; word-wrap: break-word;'>1560</td><td style='text-align: center; word-wrap: break-word;'>3120</td><td style='text-align: center; word-wrap: break-word;'>6240</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prediction</td><td style='text-align: center; word-wrap: break-word;'>1541</td><td style='text-align: center; word-wrap: break-word;'>3153</td><td style='text-align: center; word-wrap: break-word;'>6151</td><td style='text-align: center; word-wrap: break-word;'>1538</td><td style='text-align: center; word-wrap: break-word;'>3211</td><td style='text-align: center; word-wrap: break-word;'>6236</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>% Error</td><td style='text-align: center; word-wrap: break-word;'>1.18%</td><td style='text-align: center; word-wrap: break-word;'>0.76%</td><td style='text-align: center; word-wrap: break-word;'>0.83%</td><td style='text-align: center; word-wrap: break-word;'>2.17%</td><td style='text-align: center; word-wrap: break-word;'>2.39%</td><td style='text-align: center; word-wrap: break-word;'>0.37%</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.37%</td><td style='text-align: center; word-wrap: break-word;'>D201</td><td style='text-align: center; word-wrap: break-word;'>D202</td><td style='text-align: center; word-wrap: break-word;'>D203</td><td style='text-align: center; word-wrap: break-word;'>D201</td><td style='text-align: center; word-wrap: break-word;'>D202</td><td style='text-align: center; word-wrap: break-word;'>D203</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Plant data</td><td style='text-align: center; word-wrap: break-word;'>60,000</td><td style='text-align: center; word-wrap: break-word;'>63,000</td><td style='text-align: center; word-wrap: break-word;'>70,000</td><td style='text-align: center; word-wrap: break-word;'>80,000</td><td style='text-align: center; word-wrap: break-word;'>83,000</td><td style='text-align: center; word-wrap: break-word;'>88,000</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prediction</td><td style='text-align: center; word-wrap: break-word;'>61,797</td><td style='text-align: center; word-wrap: break-word;'>61,511</td><td style='text-align: center; word-wrap: break-word;'>68,598</td><td style='text-align: center; word-wrap: break-word;'>80,547</td><td style='text-align: center; word-wrap: break-word;'>82,693</td><td style='text-align: center; word-wrap: break-word;'>85,167</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>% Error</td><td style='text-align: center; word-wrap: break-word;'>3.06%</td><td style='text-align: center; word-wrap: break-word;'>2.36%</td><td style='text-align: center; word-wrap: break-word;'>2.00%</td><td style='text-align: center; word-wrap: break-word;'>0.68%</td><td style='text-align: center; word-wrap: break-word;'>0.37%</td><td style='text-align: center; word-wrap: break-word;'>3.22%</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>D204 production (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>D204 MWN (mole fraction)</td><td style='text-align: center; word-wrap: break-word;'>D204 SFRAC (mole fraction)</td><td style='text-align: center; word-wrap: break-word;'>D204 production (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>D204 MWN (mole fraction)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Plant data</td><td style='text-align: center; word-wrap: break-word;'>8600</td><td style='text-align: center; word-wrap: break-word;'>80,000</td><td style='text-align: center; word-wrap: break-word;'>0.145</td><td style='text-align: center; word-wrap: break-word;'>8600</td><td style='text-align: center; word-wrap: break-word;'>96,000</td><td style='text-align: center; word-wrap: break-word;'>0.150</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prediction</td><td style='text-align: center; word-wrap: break-word;'>8812</td><td style='text-align: center; word-wrap: break-word;'>78,004</td><td style='text-align: center; word-wrap: break-word;'>0.142</td><td style='text-align: center; word-wrap: break-word;'>8730</td><td style='text-align: center; word-wrap: break-word;'>95,099</td><td style='text-align: center; word-wrap: break-word;'>0.152</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>% Error</td><td style='text-align: center; word-wrap: break-word;'>2.45%</td><td style='text-align: center; word-wrap: break-word;'>2.49%</td><td style='text-align: center; word-wrap: break-word;'>1.80%</td><td style='text-align: center; word-wrap: break-word;'>1.51%</td><td style='text-align: center; word-wrap: break-word;'>0.94%</td><td style='text-align: center; word-wrap: break-word;'>1.60%</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<!-- PDF page 233 -->

We represent the instantaneous WCLD by averaging the distribution of each catalyst site in Eq. (5.5)

 $$ W[\log M]=\sum_{i=1}^{n}w_{i}\left(2.30268\times M^{2}\tau_{i}^{2}\mathrm{e}^{-M\tau_{i}}\right) $$ 

In the equation,  $ W[\log M] $ is the mass fraction of the chains of polymer having molecular weight  $ M $ in logarithmic scale;  $ n $ is the total number of active sites;  $ w_i $ is the mass fraction of polymer formed at each site  $ i $;  $ \tau_i $ is the fitting parameter for each site  $ i $, which is equal to the inverse of the MWN of polymer formed at each site, that is,  $ \tau_i = 1/MWN_i $. Here,  $ w_i $ and  $ MWN_i $ are equivalent to the production targets SPFRAC and SMWN defined previously.

##### 5.5.2.3 GPC Data and Deconvolution Analysis to Estimate the Number of Active Catalyst Sites

GPC is a method of characterization used to determine the MWD of a polymer. A polymer sample travels down a tube containing a porous gel. The longer polymer chains reach the end of the tube relatively quickly, while the shorter chains take longer because they become trapped in the pores of the gel. Data collection consists of time of elution versus molecular weight. These data yield a curve for the MWD.

We fit the model in Eq. (5.5) to the experimental GPC data and estimate the parameters by minimizing the difference between the model and experimental values. We estimate the minimum number of Flory distributions, n, required to describe the experimental MWD, which in turn gives the minimum number of active catalyst sites. We also estimate the MWN of polymer produced at each active catalyst site,  $ MWN_i $, and the mass fraction of polymer produced at each active site,  $ w_i $.

Supplement 5.2, “An Illustration of Using Deconvolution Excel Spreadsheet,” gives an Excel spreadsheet and a detailed illustrative example for implementing the deconvolution of GPC data from MWD that our readers may download for use in their polyolefin processes. This supplement illustrates the procedure to develop the deconvolution results summarized in Table 5.7 from a homopolymer MWD from a UNIPOL LLDPE process. Supplement 5.1e presents details of our kinetic model and kinetic parameter estimation, including the reaction rate constants chosen and their initial values for this slurry LLDPE process. Section 5.8.5 gives another example of using the deconvolution Excel spreadsheet to determine the number of active catalysts for sites from GPC data from a commercial LLDPE process.

<div style="text-align: center;">Table 5.7 Deconvolution results for a representative LLDPE homopolymer sample demonstrated in the Excel spreadsheet of Supplement 5.2.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Active catalyst site type,  $ i $</td><td style='text-align: center; word-wrap: break-word;'>Polymer weight fraction,  $ w_{i} $</td><td style='text-align: center; word-wrap: break-word;'>$ \tau_{i} $ (or 1/MWN $ _{i} $)</td><td style='text-align: center; word-wrap: break-word;'>MWN $ _{i} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.562</td><td style='text-align: center; word-wrap: break-word;'>3.156E-5</td><td style='text-align: center; word-wrap: break-word;'>31685</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0.299</td><td style='text-align: center; word-wrap: break-word;'>9.17E-6</td><td style='text-align: center; word-wrap: break-word;'>109012</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0.139</td><td style='text-align: center; word-wrap: break-word;'>1.28E-4</td><td style='text-align: center; word-wrap: break-word;'>7763</td></tr></table>

---

<!-- PDF page 234 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>log M</th><th style='text-align: center;'>Plant</th><th style='text-align: center;'>Model</th><th style='text-align: center;'>Site 1</th><th style='text-align: center;'>Site 2</th><th style='text-align: center;'>Site 3</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.11 GPC deconvolution of a homopolymer sample from a UNIPOL LLDPE process.</div>


<div style="text-align: center;">Table 5.8 Comparison of multisite model predictions with production targets obtained by data fit.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">PDI</td><td colspan="4">Grade one</td><td colspan="4">Grade two</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>D-204</td><td style='text-align: center; word-wrap: break-word;'>D-201</td><td style='text-align: center; word-wrap: break-word;'>D-202</td><td style='text-align: center; word-wrap: break-word;'>D-203</td><td style='text-align: center; word-wrap: break-word;'>D-204</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Plant data</td><td style='text-align: center; word-wrap: break-word;'>5.50</td><td style='text-align: center; word-wrap: break-word;'>5.52</td><td style='text-align: center; word-wrap: break-word;'>5.54</td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'>5.60</td><td style='text-align: center; word-wrap: break-word;'>5.70</td><td style='text-align: center; word-wrap: break-word;'>5.80</td><td style='text-align: center; word-wrap: break-word;'>6.20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Model prediction</td><td style='text-align: center; word-wrap: break-word;'>5.48</td><td style='text-align: center; word-wrap: break-word;'>5.50</td><td style='text-align: center; word-wrap: break-word;'>5.64</td><td style='text-align: center; word-wrap: break-word;'>5.95</td><td style='text-align: center; word-wrap: break-word;'>5.62</td><td style='text-align: center; word-wrap: break-word;'>5.67</td><td style='text-align: center; word-wrap: break-word;'>5.76</td><td style='text-align: center; word-wrap: break-word;'>6.26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>% Error</td><td style='text-align: center; word-wrap: break-word;'>0.25%</td><td style='text-align: center; word-wrap: break-word;'>0.37%</td><td style='text-align: center; word-wrap: break-word;'>1.84%</td><td style='text-align: center; word-wrap: break-word;'>0.67%</td><td style='text-align: center; word-wrap: break-word;'>0.33%</td><td style='text-align: center; word-wrap: break-word;'>1.42%</td><td style='text-align: center; word-wrap: break-word;'>0.68%</td><td style='text-align: center; word-wrap: break-word;'>1.03%</td></tr></table>

Figure 5.11 plots the WCLD as given in Eq. (5.5) for the example of Table 5.7. The figure shows the WCLD for each catalyst active site and distribution of the plant data. The sum of the three individual distributions of the catalyst site weighted with the mass fraction of polymer formed for each site predicts the CLD of the polymer.

We use the rate constants from single-site modeling and the deconvolution results in Table 5.8 to further calculate the rate constants for the multisite kinetics. We calculate the pre-exponential factors for catalyst-activation reactions (ACT-SPON, ACT-COCAT, and ACT-H2) at each site  $ k_{al} $ from the single-site value  $ k_{a} $,

 $$ k_{ai}=\frac{k_{a}}{n} $$ 

Equation (5.6) results from the fact that the concentration of potential catalyst sites is identical for both single-site and multisite models, but the concentration of vacant catalyst sites must be divided by the number of site types, n. We resolve this issue by dividing the pre-exponential factors for catalyst-activation reactions by the number of catalyst-site types, n [29].

---

<!-- PDF page 235 -->

We estimate the pre-exponential factor for the chain-initiation reaction (CHAIN-INI) at each site by

 $$ k_{ii}=k_{i}*w_{i}*n $$ 

We calculate the pre-exponential factor for the propagation reaction (PROPAGA-TION) at each site by

 $$ k_{p i}=k_{p}*w_{i}*n $$ 

Equations (5.6)–(5.8) give the actual values of the activation, chain initiation, and propagation rate constants for the multisite model directly. Based on our modeling experience with polyolefin processes, we find that further data-fit runs that vary these reaction constants, obtained from applying Eqs. (5.6)–(5.8), to match the relevant datasets for production rate, MWN, SFRAC, etc. within the multisite model, would produce only minimum or no changes to the reaction rate constant values.

We calculate the initial value for pre-exponential factor for the chain-transfer reactions (CHAT-MON and CHAT-H2) at each site by

 $$ k_{ci}=k_{c}*w_{i}*n $$ 

It is important to maintain the same relative contributions of chain transfer to hydrogen (CHAT-H2) and to monomer (CHAT-MON) from the same single-site model in the multisite model to preserve the sensitivity of these reactions to the concentrations of hydrogen and monomer [29]. We do this by using a Calculator (FORTRAN block) in Aspen Polymers.

To estimate the rate constants for chain transfer to H2 and to monomer for each site, we regress the PDI and MWN data for the polymer stream exiting each reactor along with the SMWN results from GPC analysis. For more accurate estimates of these kinetic parameters, it is helpful to have these data obtained with varying H2 and monomer flow rates. In the example presented in Tables 5.5 and 5.8, we use the measured PDI and MWN data for the polymer stream exiting each reactor to estimate the chain-transfer rate constants. We should also make sure that the measured MWD matches the model MWD by matching the SMWN and SFRAC values obtained from GPC analysis.

The other rate constants, such as the deactivation rate constants (DEACT-ACT and DEACT-TCA) and inhibition reactions (FSINH-H2 and RSING-H2), are all identical to those of the single-site model. If we consider the catalyst-inhibition reactions (FSINH-H2 and RSING-H2), we must ensure that the total CISFRAC for the multisite model is the sum of CISFRAC for all single sites. Also, for the PP model, the ATFRAC considered should be the same for each site and match the plant data. After updating all the rate constants, the multisite model matches all the targets.

We continue to demonstrate our methodology for kinetic parameter estimation for multisite model for the Mitsui HYPOL PP process in Figure 5.5 and Supplement 5.1a that we presented previously in Tables 5.5 and 5.6 in Section 5.5.2.1. In the supplement, we see that the deconvolution analysis of GPC data gives four active catalyst sites for the process.

---

<!-- PDF page 236 -->

To simplify the kinetic parameter estimation, we begin by setting some kinetic parameters to be equal. We make the pre-exponential factors for chain transfer (CTPRE-EXP) from ethylene segment (C2-SEG) and from propylene segment (C3-SEG) to propylene monomer (C3H6) and to ethylene comonomer (C2H4) equal. Therefore, we use a Calculator (FORTRAN block) to make PRPRE-EXP CHAT-MON (C2-SEG/C3H6) equal to PRPRE-EXP CHAT-MON (C3-SEG/C3H6) and make PRPRE-EXP CHAT-MON (C2-SEG/C2H4) equal to PRPRE-EXP CHAT-MON (C3-SEG/C2H4). We can see the pre-exponential factor and activation energy values for these reaction rate constants in Section A6 of Supplement 5.1a.

We apply data fit to execute a regression run RPDI that varies the reaction rate constants for chain transfer to hydrogen (CHAT-H2) and to monomer C3H6 and comonomer C2H4 (CHAT-MON) in order to match the dataset PDI (and hence the MWW data) given in Table 5.5 from reactors D201 to D204 for two grades with different H2/C3H6 ratios in the reactor overheads. Section A6 of Supplement 5.1a shows the resulting reaction rate constants for the multisite model, and we note that the resulting pre-exponential factors for chain transfer to hydrogen and to monomer are indeed different. Table 5.8 compares minimum errors between the model predictions and plant data for PDIs. We note the percent errors between our model predictions and plant data in Table 5.6 (0.37–3.06%) and Table 5.8 (0.25–1.84%) are equivalent to or smaller than those in reported modeling studies for polyolefin processes (approximately 5% in our previous work for HDPE [7] and for PP [29]).

Table 5.9 shows the different reaction constants that have a major effect on the production targets in a multisite model. We can use sensitivity analysis, as described in Section 5.5.3, to quantify the effect of varying kinetic parameters on the simulation targets.

#### 5.5.3 Efficient Use of Software Tools: Sensitivity Analysis

Sensitivity analysis enables us to quantify the dependence of the production targets on the reaction kinetic parameters. The analysis helps us in deciding which directions to vary the operating conditions to match the production targets. Sensitivity analysis also helps in validating the kinetic estimation procedure.

<div style="text-align: center;">Table 5.9 Major kinetic parameters affecting the multisite simulation targets.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Multisite targets</td><td style='text-align: center; word-wrap: break-word;'>Major affecting kinetic parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. PDI of polymer</td><td style='text-align: center; word-wrap: break-word;'>Chain-transfer reaction rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. MWN produced at catalyst site and overall MWN</td><td style='text-align: center; word-wrap: break-word;'>Chain-transfer reaction rate constant for each site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Mass fraction for polymer produced at each site and overall production rate</td><td style='text-align: center; word-wrap: break-word;'>Propagation reactions for each site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. ATFRAC for each site</td><td style='text-align: center; word-wrap: break-word;'>Atactic propagation reaction rate constant</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. Polymer solution density</td><td style='text-align: center; word-wrap: break-word;'>Comonomer rate constants</td></tr></table>

---

<!-- PDF page 237 -->

for polyolefins. We illustrate below some examples of sensitivity analysis of the different polyolefin processes that we have modeled and estimated kinetics using our procedure.

Supplement 5.1e gives details of our kinetic model and kinetic parameter estimation, including the reaction rate constants chosen and their initial values for the Unipol LLDPE process of Figure 5.8. Applying the sensitivity analysis, we illustrate in Figure 5.12a how varying the reaction rate constant for chain transfer to hydrogen,  $ k_{th,i} $ of just one of the three active sites affects the final LLDPE polymer properties, including the PDI, the MWN at the chosen catalyst site SMWN, and the overall MWN. As we increase the reaction rate constant for chain transfer to hydrogen, both the SMWN and MWN decrease, while the PDI increases gradually. In other words, we can vary the hydrogen flow rate to change the rate of chain-transfer reactions to achieve the desired MWN and PDI.

As another example, for the Mitsui Hypol PP process of Figure 5.5 and Supplement 5.1a, Figure 5.12b illustrates that varying the reaction rate constant for chain transfer to monomer,  $ k_{tm,i} $ results in similar trends of changes in PDI, SMWN, and MWN as with the chain transfer to hydrogen. The similar trends

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_m,i (1/s)</th><th style='text-align: center;'>SMWN</th><th style='text-align: center;'>MWN</th><th style='text-align: center;'>PDI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>50000</td><td style='text-align: center;'>33000</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>39000</td><td style='text-align: center;'>29000</td><td style='text-align: center;'>3.8</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>31000</td><td style='text-align: center;'>27000</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>29000</td><td style='text-align: center;'>25000</td><td style='text-align: center;'>3.2</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>26000</td><td style='text-align: center;'>23000</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>21000</td><td style='text-align: center;'>21000</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>19000</td><td style='text-align: center;'>20000</td><td style='text-align: center;'>2.6</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>17000</td><td style='text-align: center;'>19000</td><td style='text-align: center;'>2.4</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>15000</td><td style='text-align: center;'>18000</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>13000</td><td style='text-align: center;'>17000</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>12000</td><td style='text-align: center;'>16000</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>11000</td><td style='text-align: center;'>15000</td><td style='text-align: center;'>1.6</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>14000</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>9000</td><td style='text-align: center;'>13000</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>12000</td><td style='text-align: center;'>1.3</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>7000</td><td style='text-align: center;'>11000</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>1.1</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>9000</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>3000</td><td style='text-align: center;'>7000</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>0.7</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_tm,i (1/s)</th><th style='text-align: center;'>MWN (b)</th><th style='text-align: center;'>SMWN (b)</th><th style='text-align: center;'>PDI (b)</th><th style='text-align: center;'>MWN (c)</th><th style='text-align: center;'>SMWN (c)</th><th style='text-align: center;'>PDI (c)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>79000</td><td style='text-align: center;'>93000</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>64000</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>17.5</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>53000</td><td style='text-align: center;'>65000</td><td style='text-align: center;'>19.0</td><td style='text-align: center;'>53000</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>19.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>45000</td><td style='text-align: center;'>48000</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>45000</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>38000</td><td style='text-align: center;'>35000</td><td style='text-align: center;'>21.0</td><td style='text-align: center;'>38000</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>21.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>32000</td><td style='text-align: center;'>30000</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>32000</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>28000</td><td style='text-align: center;'>25000</td><td style='text-align: center;'>23.0</td><td style='text-align: center;'>28000</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>25000</td><td style='text-align: center;'>22000</td><td style='text-align: center;'>24.0</td><td style='text-align: center;'>25000</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>24.0</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>23000</td><td style='text-align: center;'>20000</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>23000</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>21000</td><td style='text-align: center;'>18000</td><td style='text-align: center;'>26.0</td><td style='text-align: center;'>21000</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>26.0</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>19000</td><td style='text-align: center;'>16000</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>19000</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>18000</td><td style='text-align: center;'>15000</td><td style='text-align: center;'>28.0</td><td style='text-align: center;'>18000</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>17000</td><td style='text-align: center;'>14000</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>17000</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>16000</td><td style='text-align: center;'>13000</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>16000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>30.0</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>15000</td><td style='text-align: center;'>12000</td><td style='text-align: center;'>31.0</td><td style='text-align: center;'>15000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>31.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>14000</td><td style='text-align: center;'>11000</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>14000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>32.0</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>13000</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>33.0</td><td style='text-align: center;'>13000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>33.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>12000</td><td style='text-align: center;'>9000</td><td style='text-align: center;'>34.0</td><td style='text-align: center;'>12000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>34.0</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>11000</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>11000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>7000</td><td style='text-align: center;'>36.0</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>36.0</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>9000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>37.0</td><td style='text-align: center;'>9000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>37.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>38.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 5.12 Sensitivity of the PDI, MWN, and SMWN for the Unipol LLDPE process on the pre-exponential factor of the reaction rate constant for (a) chain transfer to hydrogen and (b) chain transfer to monomer.</div>


---

<!-- PDF page 238 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>`k_o,i` (1/s)</th><th style='text-align: center;'>PROD (kg/hr)</th><th style='text-align: center;'>SPFRAC (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10,000</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>0.33</td></tr>
    <tr><td style='text-align: center;'>15,000</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>20,000</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>25,000</td><td style='text-align: center;'>2400</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>30,000</td><td style='text-align: center;'>2600</td><td style='text-align: center;'>0.48</td></tr>
    <tr><td style='text-align: center;'>35,000</td><td style='text-align: center;'>2800</td><td style='text-align: center;'>0.51</td></tr>
    <tr><td style='text-align: center;'>40,000</td><td style='text-align: center;'>3000</td><td style='text-align: center;'>0.54</td></tr>
    <tr><td style='text-align: center;'>45,000</td><td style='text-align: center;'>3200</td><td style='text-align: center;'>0.57</td></tr>
    <tr><td style='text-align: center;'>50,000</td><td style='text-align: center;'>3400</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>55,000</td><td style='text-align: center;'>3600</td><td style='text-align: center;'>0.63</td></tr>
    <tr><td style='text-align: center;'>60,000</td><td style='text-align: center;'>3800</td><td style='text-align: center;'>0.66</td></tr>
    <tr><td style='text-align: center;'>65,000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>0.69</td></tr>
    <tr><td style='text-align: center;'>70,000</td><td style='text-align: center;'>4200</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'>75,000</td><td style='text-align: center;'>4400</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>80,000</td><td style='text-align: center;'>4600</td><td style='text-align: center;'>0.77</td></tr>
    <tr><td style='text-align: center;'>85,000</td><td style='text-align: center;'>4800</td><td style='text-align: center;'>0.79</td></tr>
    <tr><td style='text-align: center;'>90,000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>95,000</td><td style='text-align: center;'>5200</td><td style='text-align: center;'>0.81</td></tr>
    <tr><td style='text-align: center;'>100,000</td><td style='text-align: center;'>5400</td><td style='text-align: center;'>0.82</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_pa,j (1/s)</th><th style='text-align: center;'>ATFRAC</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.16</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>0.24</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>0.32</td></tr>
    <tr><td style='text-align: center;'>4000</td><td style='text-align: center;'>0.36</td></tr>
    <tr><td style='text-align: center;'>4500</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>5000</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'>5500</td><td style='text-align: center;'>0.48</td></tr>
    <tr><td style='text-align: center;'>6000</td><td style='text-align: center;'>0.52</td></tr>
    <tr><td style='text-align: center;'>6500</td><td style='text-align: center;'>0.56</td></tr>
    <tr><td style='text-align: center;'>7000</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>7500</td><td style='text-align: center;'>0.64</td></tr>
    <tr><td style='text-align: center;'>8000</td><td style='text-align: center;'>0.68</td></tr>
    <tr><td style='text-align: center;'>8500</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'>9000</td><td style='text-align: center;'>0.76</td></tr>
    <tr><td style='text-align: center;'>9500</td><td style='text-align: center;'>0.79</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 5.13 (a) The sensitivity of the production rate and SPFRAC for the Unipol LLDPE process to changes in the propagation reaction rate constant. (b) The sensitivity of the atactic fraction ATFRAC to changes in the atactic propagation reaction rate constant for the Spheripol PP process.</div>


observed in Figures 5.12a,b, 5.13a,b, and 5.14a,b below support our approach of applying the same methodology for kinetic parameter estimation for modeling different commercial polyolefin processes from plant data.

We demonstrate the further use of sensitivity analysis for the Unipol LLDPE process of Figure 5.8 and Supplement 5.1e. Figure 5.13a shows how increasing the per-exponential factor of the propagation rate constant,  $ k_{p,i} $ for one of the three active sites increases the production rate and mass fraction of polymer produced at that site (SPFRAC).

Supplement 5.1d gives details of our kinetic model and kinetic parameter estimation, including the reaction rate constants chosen and their initial values for the Basell Spheripol PP process of Figure 5.6. In Figure 5.13b, we show how increasing the atactic propagation rate constant increases the atactic fraction (ATFRAC) for the Spheripol PP process.

For the Mitsui slurry HDPE process with serial reactor configuration of Figure 5.3 and Supplement 5.1b, we show in Figure 5.14a,b the sensitivity of the polymer production rate to changes in the reaction rate constants for catalyst activation by

---

<!-- PDF page 239 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_act,i (1/s)</th><th style='text-align: center;'>Prod. rate (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>2400</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>2550</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>2750</td></tr>
    <tr><td style='text-align: center;'>0.15</td><td style='text-align: center;'>2880</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>2980</td></tr>
    <tr><td style='text-align: center;'>0.25</td><td style='text-align: center;'>3080</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>3150</td></tr>
    <tr><td style='text-align: center;'>0.35</td><td style='text-align: center;'>3200</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>3250</td></tr>
    <tr><td style='text-align: center;'>0.45</td><td style='text-align: center;'>3300</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>3350</td></tr>
    <tr><td style='text-align: center;'>0.55</td><td style='text-align: center;'>3400</td></tr>
    <tr><td style='text-align: center;'>0.60</td><td style='text-align: center;'>3450</td></tr>
    <tr><td style='text-align: center;'>0.65</td><td style='text-align: center;'>3480</td></tr>
    <tr><td style='text-align: center;'>0.70</td><td style='text-align: center;'>3500</td></tr>
    <tr><td style='text-align: center;'>0.75</td><td style='text-align: center;'>3520</td></tr>
    <tr><td style='text-align: center;'>0.80</td><td style='text-align: center;'>3550</td></tr>
    <tr><td style='text-align: center;'>0.85</td><td style='text-align: center;'>3580</td></tr>
    <tr><td style='text-align: center;'>0.90</td><td style='text-align: center;'>3600</td></tr>
    <tr><td style='text-align: center;'>0.95</td><td style='text-align: center;'>3620</td></tr>
    <tr><td style='text-align: center;'>1.00</td><td style='text-align: center;'>3650</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_d,i (1/s)</th><th style='text-align: center;'>Prod. rate (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>2530</td></tr>
    <tr><td style='text-align: center;'>0.50E+00</td><td style='text-align: center;'>2460</td></tr>
    <tr><td style='text-align: center;'>1.00E+00</td><td style='text-align: center;'>2400</td></tr>
    <tr><td style='text-align: center;'>1.50E+00</td><td style='text-align: center;'>2340</td></tr>
    <tr><td style='text-align: center;'>2.00E-03</td><td style='text-align: center;'>2290</td></tr>
    <tr><td style='text-align: center;'>2.50E-03</td><td style='text-align: center;'>2240</td></tr>
    <tr><td style='text-align: center;'>3.00E-03</td><td style='text-align: center;'>2190</td></tr>
    <tr><td style='text-align: center;'>3.50E-03</td><td style='text-align: center;'>2150</td></tr>
    <tr><td style='text-align: center;'>4.00E-03</td><td style='text-align: center;'>2120</td></tr>
    <tr><td style='text-align: center;'>4.50E-03</td><td style='text-align: center;'>2080</td></tr>
    <tr><td style='text-align: center;'>5.00E-03</td><td style='text-align: center;'>2050</td></tr>
    <tr><td style='text-align: center;'>5.50E-03</td><td style='text-align: center;'>2020</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.14 The sensitivity of the production rate for the slurry HDPE process to changes in the reaction rate constant for (a) catalyst activation by cocatalyst and (b) spontaneous catalyst deactivation.</div>


cocatalyst,  $ k_{act,i} $, and for spontaneous catalyst deactivation  $ k_{ds,i} $ for one of the five active catalyst sites.

Figure 5.15 illustrates the sensitivity of the MWD from a Mitsui slurry HDPE process of Figure 5.3 and Supplement 5.1b to changes in the reaction rate constant for forward catalyst inhibition by hydrogen,  $ k_{\text{finh},i} $, for two different of the five active catalyst sites. The MWD of the HDPE produced from a single reactor can change from unimodal to bimodal. This happens since there is a difference in the rate of inhibition for different catalyst sites.

Figure 5.16 shows the effect on the production rates for the two horizontal bed reactors (represented as P1, P2 in the figure) in the Innovene gas-phase PP process of Figure 5.7 by varying the pre-exponential rate constant of propagation reaction for a particular active site. The details of the process are available in Supplement 5.1c.

#### 5.5.4 Efficient Use of Software Tools: Design Specification

Design specification (design spec) is an important tool that supports process modeling and kinetic estimation. While sensitivity analysis quantifies an increasing or

---

<!-- PDF page 240 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>DP (log scale)</th><th style='text-align: center;'>k_flnh,i = 6e5</th><th style='text-align: center;'>k_flnh,i = 6e3</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>97</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>99</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>101</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>102</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>103</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>104</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>106</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>107</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>108</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>109</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>111</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>112</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>113</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>114</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>116</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>117</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>118</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>119</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>121</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>122</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>123</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>124</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>126</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>127</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>128</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>129</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>131</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>132</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>133</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>134</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>136</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>137</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>138</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>139</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>141</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>142</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>143</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>144</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>146</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>147</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>148</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>149</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>151</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>152</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>153</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>154</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>156</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>157</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>158</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>159</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>161</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>162</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>163</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>164</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>166</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>167</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>168</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>169</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>171</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>172</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>173</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+00</td></tr>
    <tr><td style='text-align: center;'>174</td><td style='text-align: center;'>0.00E+00</td><td style='text-align: center;'>0.00E+0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.15 Sensitivity of the MWD from a Mitsui slurry HDPE process to changes in the reaction rate constant for catalyst inhibition for two different of the five active catalyst sites.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>k_p,i (1/s)</th><th style='text-align: center;'>P1 (kg/hr)</th><th style='text-align: center;'>P2 (kg/hr)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>16500</td><td style='text-align: center;'>20500</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>17500</td><td style='text-align: center;'>21500</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>18500</td><td style='text-align: center;'>22500</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>20000</td><td style='text-align: center;'>23500</td></tr>
    <tr><td style='text-align: center;'>1250</td><td style='text-align: center;'>21000</td><td style='text-align: center;'>24500</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>22000</td><td style='text-align: center;'>25500</td></tr>
    <tr><td style='text-align: center;'>1750</td><td style='text-align: center;'>23000</td><td style='text-align: center;'>26500</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>24000</td><td style='text-align: center;'>27500</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>25000</td><td style='text-align: center;'>28500</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>26000</td><td style='text-align: center;'>29500</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.16 The sensitivity of the production rate from an Innovene gas-phase PP process to changes in the propagation reaction rate constant.</div>


decreasing trend of a production target when varying a reaction rate constant within a chosen range of values, applying the design spec enables us to identify the reaction rate constant value within the chosen range to reach a specific production target.

Design spec is particularly useful in converging models of polyolefin processes having recycle loops. We can fix a particular ratio of components in a recycle stream, and the model can vary input flow rates to maintain the ratio. As an illustration, in the Spheripol PP process of Figure 5.6 and Supplement 5.1d, we can use a design spec to maintain the ratio of ethylene to propylene in a recycle stream into the fluidized-bed reactor where the stream is a combination of the overall recycle stream and a feed of ethylene and hydrogen. Design spec varies the flow rates of ethylene (comonomer) and hydrogen to maintain the desired ratio of ethylene and propylene in the recycle stream. Similarly, we can use another design spec for the recycle flow into the loop reactor by varying the flow of the propylene and hydrogen in the feed stream. Figure 5.17 shows a flowsheet of the Spheripol PP process with the design specs [35].

---

<!-- PDF page 241 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_47_509_923_797.jpg" alt="Image" width="90%" /></div>


<div style="text-align: center;">Figure 5.17 Spheripol PP process flowsheet indicating the design specification.</div>


---

<!-- PDF page 242 -->

<div style="text-align: center;">Table 5.10 Design specification for the Spheripol PP process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Design specification</td><td style='text-align: center; word-wrap: break-word;'>Target value</td><td style='text-align: center; word-wrap: break-word;'>Model result</td><td style='text-align: center; word-wrap: break-word;'>Initial vary (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Final vary (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Range set (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4e-5</td><td style='text-align: center; word-wrap: break-word;'>3.9e-5</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.16</td><td style='text-align: center; word-wrap: break-word;'>0.01-10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.48</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>3250</td><td style='text-align: center; word-wrap: break-word;'>5-1000</td></tr></table>

Specifically, for the Spheripol PP model, we define the design specs as follows:

(1) Design specification for the hydrogen mass fraction in the recycle stream entering the loop reactor, while the manipulated variable is the make-up hydrogen flow rate.

(2) Design specification for ratio of propene to ethylene in the recycle stream entering the fluidized-bed reactor, while the manipulated variable is the flow rate of ethane.

Table 5.10 shows the design spec results.

#### 5.5.5 Model Applications

A polyolefin process model validated by plant data can have many useful applications. The model will be helpful for the capacity expansion of the current plant. The model will also be useful in the process development stage of a new plant. We can use the validated model to study the effect of changes in process variables on production targets.

We can use the model to change certain production targets while maintaining the same value for other targets. As an example, we can vary certain process conditions to make polymer grades of different MWNs for the same throughput, as shown in Figure 5.18. It shows a sensitivity analysis for the effect of changes in hydrogen flow rates on MWN, while the production rate remains the same for the UNIPOL LLDPE process.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Hydrogen flow rate (kg/hr)</th><th style='text-align: center;'>PROD (kg/hr)</th><th style='text-align: center;'>MWN (MWN)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>3750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>4000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>4250</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>4500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>4750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>5000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>5250</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>5500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>5750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>6000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>6250</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>6500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>6750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>7000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>7250</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>7500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>7750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>8000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>8250</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>8500</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>8750</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
    <tr><td style='text-align: center;'>9000</td><td style='text-align: center;'>2550</td><td style='text-align: center;'>32500</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.18 Sensitivity analysis of the MWN and production rate on changes in hydrogen flow rates on the Unipol LLDPE process.</div>


---

<!-- PDF page 243 -->

<div style="text-align: center;">Table 5.11 Design specification for the UNIPOL LLDPE process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Target MWN</td><td style='text-align: center; word-wrap: break-word;'>Model MWN</td><td style='text-align: center; word-wrap: break-word;'>Initial H2 flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Final H2 flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Range set (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>29,194</td><td style='text-align: center; word-wrap: break-word;'>29,217</td><td style='text-align: center; word-wrap: break-word;'>4938</td><td style='text-align: center; word-wrap: break-word;'>7515</td><td style='text-align: center; word-wrap: break-word;'>3000-9000</td></tr></table>

In another application of the model, we can increase the throughput while keeping the same MWN using design specification, and we demonstrate this on the UNIPOL LLDPE process as well. We use design specification to vary the hydrogen flow rate to keep the same MWN at around 29,000 while increasing the production rate of LLDPE from 2400 to 3200 kg/hr. Table 5.11 summarizes the results of the UNIPOL process design specification. Lastly, when combined with process control and optimization techniques, a validated model can be useful for polymer quality control and effective polymer grade changes.

#### 5.6 Workshop 5.1: Simulation of a Slurry HDPE Process

#### 5.6.1 Objective

In this workshop, we simulate a slurry HDPE process [1]. The process consists of two CSTRs in series. The workshop is based on HDPE production process of a petrochemical company in the Asia-Pacific region. We simulate a simplified open-loop flowsheet of the plant, focusing more on the ZN reaction part. In this workshop, the kinetic rate constants and the minimum number of active catalyst sites are available. So, the focus is on building a HDPE process model and not estimating kinetic parameters. We also convert our simple open-loop model to a closed-loop plant model and perform sensitivity analysis.

#### 5.6.2 Process Flowsheet

Figure 5.19 shows a simulation flowsheet of a complete process, and Figure 5.20 displays a simplified simulation flowsheet for the current workshop. In Figure 5.20, D201 and D221 are CSTRs, and 201F and 221F are flash units. We save the simulation file for Figure 5.20 as WS5.1a HDPE_Open Loop.bkp and continue the current workshop with this file.

#### 5.6.3 Unit System, Components, and Characterization of Oligomer, Polymer, and Site-Based Species

We use METCBAR unit system for this process. Figures 5.21a and 5.21b show the components used in the simulation of the slurry HDPE process and the associated enterprise databases chosen.

Ethylene and 1-butene are monomer and comonomer, respectively, with each having a repeated segment, and we assume the oligomer, LP, contains 19 repeated ethylene segments (Figure 5.22). TICl4 is catalyst, and TEAL is cocatalyst. Hydrogen is chain-transfer agent, and hexane is solvent. Nitrogen is a purge gas, and CH4, C2H6, and C4H10 are impurities.

---

<!-- PDF page 244 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_48_514_921_847.jpg" alt="Image" width="90%" /></div>


<div style="text-align: center;">Figure 5.19 A complete simulation flowsheet of a slurry HDPE process in a series configuration.</div>


---

<!-- PDF page 245 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_171_784_384.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.20 A simplified open-looped simulation flowsheet of a slurry HDPE process in a series configuration for workshop 5.1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_500_777_839.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.21a Component specifications.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_938_604_1200.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">Figure 5.21b Enterprise databases chosen.</div>


---

<!-- PDF page 246 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_149_808_346.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.22 Definition of segments and representation of oligomer LP.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_411_648_689.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.23 Characterization of Ziegler–Natta polymer attributes.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_757_807_1052.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.24 Characterization of ZN catalyst and attribute selection.</div>


To characterize the polymer, HDPE, we choose the default attributes for ZN selection. See Figure 5.23.

Figure 5.24 shows the characterization of the ZN catalyst, TiCl $ _{4} $, under site-based species. To understand the meanings of the attributes, click on one of the attribute names, and you will see a table of attribute selection on the right of the figure, explaining each attribute.

---

<!-- PDF page 247 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_145_781_366.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.25 A comparison between the actual slurry system and the modeling assumption that the polymer is dissolved in the liquid phase with the solvent.</div>


#### 5.6.4 The Role of Solid Polymer in Phase-Equilibrium Calculations

In the reactor, ethylene molecules react to form long polymer chains. In the slurry process, the reactor temperature (70–85 °C) is below the melting point of the polymer (140 °C). The polymer molecules solidify upon formation, creating a slurry system.

In the actual process, the solid polymer does not interact thermodynamically with the other components in the reactor. Our primary assumption in phase calculations is that the polymer is dissolved in the liquid phase with the solvent, as would be the case in solution polymerization of ethylene, where the reactor temperature would be above the melting point of the polymer. Although this modeling simplification does not represent the physical picture of what is happening in the slurry polymerization of ethylene, the effect of it in the thermodynamic modeling is relatively small. Figure 5.25 illustrates the difference between the actual conditions and the modeling assumption [4].

In Ref. [4], we have presented quantitative evidence to demonstrate that we can make this assumption without undermining the robustness of the reactor model.

#### 5.6.5 Thermodynamic Model and Parameters

We use the POLYSL equation of state, presented previously in Section 2.6, for the slurry HDPE process [7]. The model is given by:

 $$ \overline{\rho}^{2}+\overline{P}+\overline{T}\left[\ln(1-\overline{\rho})+\left(1-\frac{1}{r}\right)\overline{\rho}\right]=0 $$ 

where

 $$ \overline{\rho}=\frac{\rho}{\rho^{*}},\quad\overline{P}=\frac{P}{P^{*}},\quad\overline{T}=\frac{T}{T^{*}} $$ 

are the reduced density, pressure, and temperature, respectively; and  $ \rho^{*} $,  $ P^{*} $, and  $ T^{*} $ are the scale factors that completely characterize each pure fluid. They correspond to pure-component (unary) parameters SLRSTR, SLPSTR, and SLTSTR within Aspen Polymers. See Figure 5.26 for entering the parameter values according to the online help for “Sanchez-Lacombe unary parameters” in Aspen Polymers.

To model the copolymer production, we include binary interaction parameters. Through the online help for “Sanchez-Lacombe binary parameters” in Aspen

---

<!-- PDF page 248 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_807_251.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.26 Pure-component parameters for POLYSL thermodynamic model: Properties → Methods → Parameters → Pure Components → PURE-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_350_807_706.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.27 Binary interaction parameters for POLYSL thermodynamic model. Source: Dotson et al. [7]/John Wiley & Sons.</div>


Polymers, we see the temperature-dependent expressions for two binary interaction parameters:

 $$ k_{ij}=a_{ij}+\frac{b_{ij}}{T_{r}}+c_{ij}\ln T_{r}+d_{ij}T_{r}+e_{ij}T_{r}^{2} $$ 

 $$ \eta_{ij}=a^{\prime}_{ij}+\frac{b^{\prime}_{ij}}{T_{r}}+c^{\prime}_{ij}\ln T_{r}+d^{\prime}_{ij}T_{r}+e^{\prime}_{ij}T_{r}^{2} $$ 

where  $ T_r $ is the reduced temperature defined by  $ T/T_{\text{ref}} $, and the default value of reference temperature  $ T_{\text{ref}} $ is 298.15 K. We enter the parameter values of these two equations (see tables 5 and 6 in [7]) in Aspen Polymers following the path: Properties → Methods → Parameters → Binary Interaction → SLKIJ-1 and SLETIJ-1. See Figure 5.27.

#### 5.6.6 Pure-Component Parameters

To extract the property parameters for pure components from the Aspen Polymers databases, we follow the path: Properties → Components → Specifications → Review (see Figure 5.28):

---

<!-- PDF page 249 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_148_715_531.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.28 Review of property parameters for pure components.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_600_778_862.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.29 Extraction of pure-component property values from Aspen Polymers databanks.</div>


We then see the listing of parameter values by following the path: Properties → Methods → Parameters → Pure Components → Review-1. See Figure 5.29.

We need to input several other scalar and temperature-dependent parameters for pure components. First, we enter the estimated or literature values of scalar pure-component parameters that are not available within the Aspen Polymer databases: Properties → Parameters → Pure Components → New → Scalar → Enter parameter name and value. Figure 5.30 shows the assumed values of critical temperature (TC) and critical pressure (PC) for our catalysts.

We also enter the estimates of the critical parameters for the oligomer LP: Properties → Parameters → Pure Components → New → Scalar → Name: LPCrit → Enter parameter name, unit, and value (see Figure 5.31).

Next, to ensure that polymer HDPE, oligomer LP, and catalysts TiCl $ _{4} $ and TEAL do not valorize, we can specify the first parameter in the T-dependent liquid vapor

---

<!-- PDF page 250 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_147_627_345.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 5.30 Assumed values of critical pressure PC and critical temperature TC for ZN catalyst TiCl₄ and cocatalyst triethyl aluminum (TEAL).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_466_598_739.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 5.31 Assumed values of critical pressure PC, critical temperature TC, and compressibility factor ZC for oligomer LP.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_798_807_999.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.32 Setting the first parameter of the T-dependent liquid vapor pressure correlation PLXANT-1 to a large negative number of -40 to ensure the selected components remain in the liquid phase.</div>


pressure correlation, PLXANT-1, to a large negative number like -40. This will make the vapor pressure of these four components extremely small (4.24E-23 bar) [36]. See Figure 5.32.

Lastly, it is important that we compare the predictions of thermophysical properties of components using the POLYSL thermodynamic method with the reported experimental data in order to validate our selection of POLYSL as an accurate

---

<!-- PDF page 251 -->

<div style="text-align: center;">Table 5.12 Specifications of feed streams.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>T (°C)</td><td style='text-align: center; word-wrap: break-word;'>P (bar)</td><td style='text-align: center; word-wrap: break-word;'>Flow</td><td style='text-align: center; word-wrap: break-word;'>Mass fraction</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>5588 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4} = 0.9998 $;  $ C_{2}H_{6} = 0.0001 $;  $ CH_{4} = 0.0001 $;  $ H_{2} = 1E-6 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>255 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ TiCl_{4} = 0.005 $;  $ TEAL = 0.005 $;  $ HX = 0.99 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>1.0125</td><td style='text-align: center; word-wrap: break-word;'>36 cum/hr</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2} = 0.9773 $;  $ CH_{4} = 0.0227 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>3500 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ HX = 1 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML1</td><td style='text-align: center; word-wrap: break-word;'>67</td><td style='text-align: center; word-wrap: break-word;'>14.5</td><td style='text-align: center; word-wrap: break-word;'>5300 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>LP = 0.05;  $ HX = 0.95 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C4</td><td style='text-align: center; word-wrap: break-word;'>116</td><td style='text-align: center; word-wrap: break-word;'>13.4</td><td style='text-align: center; word-wrap: break-word;'>96 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{8} = 0.983 $;  $ C_{4}H_{10} = 0.017 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C22</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>5412 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4} = 0.9998 $;  $ C_{2}H_{6} = 0.0001 $;  $ CH_{4} = 0.0001 $;  $ H_{2} = 1E-6 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H22</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>1.0125</td><td style='text-align: center; word-wrap: break-word;'>8.68 cum/hr</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2} = 0.9773 $;  $ CH_{4} = 0.0227 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX2</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>2000 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ HX = 1 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML2</td><td style='text-align: center; word-wrap: break-word;'>240</td><td style='text-align: center; word-wrap: break-word;'>1.45e6</td><td style='text-align: center; word-wrap: break-word;'>8780 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>LP = 0.05;  $ HX = 0.95 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>N2</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>20 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>$ N_{2} = 1 $</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4} $</td><td style='text-align: center; word-wrap: break-word;'>$ C_{4}H_{8} $</td><td style='text-align: center; word-wrap: break-word;'>TEAL</td><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>LP</td><td style='text-align: center; word-wrap: break-word;'>$ N_{2} $</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{6} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML1</td><td style='text-align: center; word-wrap: break-word;'>2.27</td><td style='text-align: center; word-wrap: break-word;'>4.53</td><td style='text-align: center; word-wrap: break-word;'>0.19</td><td style='text-align: center; word-wrap: break-word;'>5023.31</td><td style='text-align: center; word-wrap: break-word;'>267.862</td><td style='text-align: center; word-wrap: break-word;'>0.70</td><td style='text-align: center; word-wrap: break-word;'>1.14</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML2</td><td style='text-align: center; word-wrap: break-word;'>3.77</td><td style='text-align: center; word-wrap: break-word;'>7.52</td><td style='text-align: center; word-wrap: break-word;'>0.32</td><td style='text-align: center; word-wrap: break-word;'>8320.55</td><td style='text-align: center; word-wrap: break-word;'>444.752</td><td style='text-align: center; word-wrap: break-word;'>1.19</td><td style='text-align: center; word-wrap: break-word;'>1.9</td></tr></table>

Unit: kg/hr.

Both ML1 and ML2 at  $ 67^{\circ} $C, 14.5 bar.

Total mass flow: ML1 = 5300 kg/hr; ML2 = 8780 kg/hr.

thermodynamic method for the slurry HDPE process simulation [4]. We refer the reader to WS 2.3, Section 2.7, for this validation.

#### 5.6.7 Feed Streams

The feed to the first reactor consists of the ethylene monomer (C2), catalyst (CAT), solvent (HX), hydrogen (H2), and oligomer stream recycled from the separation section (ML1), which are combined in a mixer (M1) before entering the first reactor (D201) in series.

The feed to the second reactor (D221) consists of the outlet from the first reactor and the comonomer butane (C4), ethylene monomer (C2), hydrogen (H2), solvent (HX), and oligomer (ML2) streams.

We input the essential data for these feed streams specified in Table 5.12 under Simulation → Streams:

Referring to Figure 5.24 where we define the site-based species attributes for catalyst TiCl4, we show below how to enter the initial attribute values for stream CAT. See Figures 5.33 and 5.34.

---

<!-- PDF page 252 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_806_335.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.33 Specification of initial site-based species attributes for CAT stream: Setting potential-site mole flow (CPSFLOW) to zero. Do the same for potential-site mole fraction (CPSFRAC), dead-site mole flow (CDSFLOW) and dead-site mole fraction (CDSFRAC).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_464_806_653.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.34 Specification of initial site-based species attributes for CAT stream: Setting the mole flow of the first inhibited site S_1 (CISFLOW) to zero. Do the same for the mole fraction of first inhibited site S_1 (CPSFRAC), mole flow of the first vacant site S_1 (CVSFLOW), and mole fraction of the first vacant site S_1 (CVSFRAC).</div>


#### 5.6.8 Ziegler–Natta Kinetics Specifications

We create a ZN reaction set, named ZN: Reactions→New→ID = ZN, Reaction type = Ziegler-Nat→Species (see Figure 5.35):

We have previously specified in Figure 5.24 the number of active catalyst sites as 5. We generate the reactions by including:

(1) Five catalyst site activation by cocatalyst reactions (ACT-COACT), with one reaction per active catalyst site;

(2) 10 chain-initiation reactions by monomer C2H4 and by comonomer C4H8, with two reactions per active catalyst site;

(3) 20 chain-propagation reactions (PROP) of reacting polymer chain Pn[C2H4] with C2H4 and C4H8, and reacting polymer chain Pn[C4H8] with C2H4 and C4H8, totaling four reactions per active catalyst site;

(4) 10 reactions of chain transfer to hydrogen (CHAT-H2) by reacting polymer chain  $  \text{Pn}[\text{C}_2\text{H}_4]  $ with H2 and reacting polymer chain  $  \text{Pn}[\text{C}_4\text{H}_8]  $ with H2, with two reactions per active catalyst site; and

(5) Five spontaneous catalyst-deactivation reactions (DEACT-SPON), with one reaction per active catalyst-site type; and

---

<!-- PDF page 253 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_617_480.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.35 ZN kinetics reaction species specification.</div>


<div style="text-align: center;">Figure 5.36a ZN reactions for HDPE – part 1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_546_572_798_955.jpg" alt="Image" width="26%" /></div>


(6) Five forward and five reverse catalyst inhibitions by hydrogen (FSINH-H2 and RFINH-H2), with one reaction per active catalyst-site type. Figures 5.36a and 5.36b show the 60 reactions generated.

To specify the reaction rate constants, we follow the standard Arrhenius form, Eq. (5.1).  $ \text{Supplement 5.1b} $ gives the numerical values of the pre-exponential factor  $ k_{0} $ and the activation energy E for each reaction.

In Ref. [7], we developed the oligomer reactions for both reactors D201 and D221 based on plant data. We include the same empirical reaction in the current simulation. See Figures 5.37a and 5.37b:

---

<!-- PDF page 254 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_161_429_701.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">Figure 5.36b ZN reactions for HDPE – part 2.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_160_791_743_1034.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.37a Stoichiometry for oligomer reaction WAX1 for first reactor D201 and for oligomer reaction WAX2 for second reactor D221.</div>


---

<!-- PDF page 255 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_695_396.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 5.37b Specification of kinetic parameters for oligomer reaction WAX1. For oligomer reaction WAX2, k = 4.2, and E = 1.6172 cal/mol.</div>


#### 5.6.9 Specifications of Unit Operations and Chemical Reactor Blocks

###### 5.6.9.1 Mixers (Figure 5.38)

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_582_617_767.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.38 Specification of no pressure drop for mixer M1. Same specification for mixer M2.</div>


####### 5.6.9.2 Reactors (Figures 5.39–5.41)

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_940_744_1179.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 5.39 Specification of the first reactor D201. For second reactor D221, change pressure to 3.5 bar and temperature to 80°C.</div>


---

<!-- PDF page 256 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_146_649_462.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.40 Specification of reactions R1 and WAX1 for the first reactor D201. For second reactor D221, replace reaction WAX1 with reaction WAX2.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_537_808_814.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.41 Specification of mass-balance convergence scheme (Newton) and number of maximum iterations (200) for both reactors D201 and D221.</div>


###### 5.6.9.3 Specification of Flash Drums (Figure 5.42)

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_965_744_1254.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.42 Specification for flash drum 201F. For flash drum 221F, change temperature to 80°C.</div>


---

<!-- PDF page 257 -->

<div style="text-align: center;">Table 5.13 Simulation results from the open-loop HPDE flowsheet of Figure 5.20.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Feed</td><td style='text-align: center; word-wrap: break-word;'>D201OUT</td><td style='text-align: center; word-wrap: break-word;'>Slurry</td><td style='text-align: center; word-wrap: break-word;'>Feed2</td><td style='text-align: center; word-wrap: break-word;'>D221OUT</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Total stream (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>14,646.3</td><td style='text-align: center; word-wrap: break-word;'>14,646.3</td><td style='text-align: center; word-wrap: break-word;'>14,646.3</td><td style='text-align: center; word-wrap: break-word;'>16,308.8</td><td style='text-align: center; word-wrap: break-word;'>30,927.6</td></tr><tr><td colspan="6">Selected component (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>5589.15</td><td style='text-align: center; word-wrap: break-word;'>14.6007</td><td style='text-align: center; word-wrap: break-word;'>12.2919</td><td style='text-align: center; word-wrap: break-word;'>5414.68</td><td style='text-align: center; word-wrap: break-word;'>35.982</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C4H8</td><td style='text-align: center; word-wrap: break-word;'>4.53</td><td style='text-align: center; word-wrap: break-word;'>4.53</td><td style='text-align: center; word-wrap: break-word;'>4.32593</td><td style='text-align: center; word-wrap: break-word;'>101.945</td><td style='text-align: center; word-wrap: break-word;'>106.271</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5374.93</td><td style='text-align: center; word-wrap: break-word;'>5374.93</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>10574.9 $ ^{a)} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LP</td><td style='text-align: center; word-wrap: break-word;'>267.862</td><td style='text-align: center; word-wrap: break-word;'>470.17</td><td style='text-align: center; word-wrap: break-word;'>470.17</td><td style='text-align: center; word-wrap: break-word;'>444.752</td><td style='text-align: center; word-wrap: break-word;'>1006.66</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>8776.24</td><td style='text-align: center; word-wrap: break-word;'>8776.24</td><td style='text-align: center; word-wrap: break-word;'>8752.46</td><td style='text-align: center; word-wrap: break-word;'>10,320.6</td><td style='text-align: center; word-wrap: break-word;'>19073</td></tr><tr><td colspan="6">Component attribute</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>7769.51</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>15,038.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>110,123</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>80,781.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>14.1737</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>53.7154</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Feed</td><td style='text-align: center; word-wrap: break-word;'>D201OUT</td><td style='text-align: center; word-wrap: break-word;'>Slurry</td><td style='text-align: center; word-wrap: break-word;'>Feed2</td><td style='text-align: center; word-wrap: break-word;'>D221OUT</td></tr></table>

a) Ethylene conversion to HDPE = 10,574.9/(5589.15 + 5414.68) = 96.10%.

#### 5.6.10 Simulation Results

Table 5.13 shows the simulation results. For Aspen Polymers to show the computed component attributes such as MWW and PDI and display the flow rate in mass unit, we follow the path: stream summary → display option → full option (showing component attributes) → flow: mass, composition: mass.

We use the mass-balance results of Table 5.13 to share a tip to speed up the convergence of some reactor simulations. Previously, we demonstrated in Figure 5.43 how to increase the number of maximum iterations to 200. On the same convergence input form as Figure 5.43, we see the “estimate” folder. Based on the mass flow rate of FEED stream to the first reactor D201 and the total mass flow rate of D201OUT and Feed2 entering the second reactor D221, and assuming a C2H4 conversion of 97% to HDPE and a negligible vaporization of HX within the reactor, we can estimate the key component mass flows exiting both reactors in streams D201OUT and D221OUT. See Figure 5.43.

For the current workshop, we find that adding these mass flow estimates is not necessary, but for more difficult reactor simulation problems (such as the closed-loop simulations below), this approach could speed up the convergence of reactor simulation.

#### 5.6.11 Sensitivity Analysis

We vary the hydrogen flow rate to the second reactor, D221, and investigate its effects on the MWN, MWW, and mass flow rate of the HDPE product. See Figures 5.44a–5.44e. As expected, increasing the hydrogen mass flow rate results in

---

<!-- PDF page 258 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_148_808_554.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.43 Estimate of key-component mass flow rates exiting reactors D201 and D221 to speed up convergence of reactor simulations.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_658_756_936.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 5.44a Define the independent variable for sensitivity analysis S-1.</div>


an increase in the chair-transfer reactions, smaller molecular weights (MWN and MWW), and HDPE production rate.

#### 5.6.12 Closing the Recycle Loops

We first save the open-loop simulation file, WS5.1a HDPE_Open Loop.bkp, as WS5.1b HDPE_Close Loop Converged.bkp, and begin to modify the flowsheet. Specifically, we add two essentially identical recycle loops. This loop includes coolers (exchangers E201 and E221), flash drums (D205 and D225), compressors (C201

---

<!-- PDF page 259 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_167_776_430.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.44b Define the dependent variables for sensitivity analysis S-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_520_778_811.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.44c Define the display variables for sensitivity analysis S-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_899_776_1227.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.44d Effect of hydrogen inlet flow rate to reactor D221 on the product molecular weights.</div>


---

<!-- PDF page 260 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>WAVY 1-R22</th><th style='text-align: center;'>S-1- Results Summary</th><th style='text-align: center;'>S-1- Results Summary - Plot 1</th><th style='text-align: center;'>S-1- Results Summary - Plot 2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.73</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>1.00</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>8000</td><td style='text-align: center;'>8000</td></tr>
    <tr><td style='text-align: center;'>1.25</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td></tr>
    <tr><td style='text-align: center;'>1.50</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td></tr>
    <tr><td style='text-align: center;'>1.75</td><td style='text-align: center;'>3500</td><td style='text-align: center;'>3500</td><td style='text-align: center;'>3500</td></tr>
    <tr><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2800</td><td style='text-align: center;'>2800</td><td style='text-align: center;'>2800</td></tr>
    <tr><td style='text-align: center;'>2.25</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td></tr>
    <tr><td style='text-align: center;'>2.50</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td></tr>
    <tr><td style='text-align: center;'>2.75</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td></tr>
    <tr><td style='text-align: center;'>3.00</td><td style='text-align: center;'>1250</td><td style='text-align: center;'>1250</td><td style='text-align: center;'>1250</td></tr>
    <tr><td style='text-align: center;'>3.25</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>3.50</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>3.75</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>4.00</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td></tr>
    <tr><td style='text-align: center;'>4.25</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td></tr>
    <tr><td style='text-align: center;'>4.50</td><td style='text-align: center;'>280</td><td style='text-align: center;'>280</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>4.75</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>5.00</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>5.25</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>5.50</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td></tr>
    <tr><td style='text-align: center;'>5.75</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>6.00</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>6.25</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>6.50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>6.75</td><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td></tr>
    <tr><td style='text-align: center;'>7.00</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td></tr>
    <tr><td style='text-align: center;'>7.25</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>7.50</td><td style='text-align: center;'>15</td><td style='text-align: center;'>15</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>7.75</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>8.00</td><td style='text-align: center;'>8</td><td style='text-align: center;'>8</td><td style='text-align: center;'>8</td></tr>
    <tr><td style='text-align: center;'>8.25</td><td style='text-align: center;'>6</td><td style='text-align: center;'>6</td><td style='text-align: center;'>6</td></tr>
    <tr><td style='text-align: center;'>8.50</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>8.75</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td></tr>
    <tr><td style='text-align: center;'>9.00</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>9.25</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>9.50</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>9.75</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>10.00</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.44e Effect of hydrogen inlet flow rate to reactor D221 on the HDPE product mass flow.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_577_809_841.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.45 A closed-loop flowsheet of the slurry HDPE process.</div>


and C221), stream splitters (S1 and S2), pumps (P201 and P202), plus makeup hexane steams HX1 and HX4 to flash drums and HX3 and HX5 to pumps. Figure 5.45 shows the closed-loop flowsheet.

Table 5.14 specifies the new unit operation blocks. All the HX makeup streams have a mass fraction of hexane (HX) of 1.0. The mass flow rates are: HX201 – 440 kg/hr, HX205 – 584 kg/hr, HX221 – 115 kg/hr, and HX225 – 120 kg/hr (all for HX makeup streams are at 40°C and 1 bar).

To speed up the simulation convergence, we follow Figure 5.43 and enter the estimates of key-component mass flow rates exiting reactors D201 and D221. We change the flash options of recycle coolers E201 and E221, following Figure 5.46.

We also change the method for tear convergence to Broyden. See Figure 5.47.

We then run the simulation, which does converge. We save the simulation file as WS5.1b HDPE_Closed Loop Converged.bkp. Table 5.15 shows the resulting mass balance of key components and their attributes.

---

<!-- PDF page 261 -->

<div style="text-align: center;">Table 5.14 Specifications of unit operations.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Equipment</td><td style='text-align: center; word-wrap: break-word;'>Block names</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Compressor</td><td style='text-align: center; word-wrap: break-word;'>C201, C221</td><td style='text-align: center; word-wrap: break-word;'>Isentropic, discharge pressure = 5.8 bar (C201); 4.37 bar (C221); isentropic efficiency = 0.8, mechanical efficiency = 0.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flow splitter</td><td style='text-align: center; word-wrap: break-word;'>S1, S2</td><td style='text-align: center; word-wrap: break-word;'>Flow fraction = 0.635 (201RG); 0.5625 (221RG)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flash drum</td><td style='text-align: center; word-wrap: break-word;'>D205, D225, 201F, 221F</td><td style='text-align: center; word-wrap: break-word;'>D205: Output temperature = 80 °C, 5.8 bar; D225: 80 °C, 3.3 bar. 201F: 85 °C, 3.5 bar; 221F: 80 °C, 3.5 bar</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Recycle cooler</td><td style='text-align: center; word-wrap: break-word;'>E201, E221</td><td style='text-align: center; word-wrap: break-word;'>Exit temperature = 32 °C, pressure = -0.2 bar (pressure drop)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pump</td><td style='text-align: center; word-wrap: break-word;'>P201, P202, P205, P225</td><td style='text-align: center; word-wrap: break-word;'>Discharge pressure = 6 bar (P201); 3.5 bar (P202); 5.8 bar (P205); 3.3 bar (P225); pump efficiency = 0.6, driver efficiency = 0.9</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_623_777_848.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.46 Flash option input for recycle cooler E201 (and E221).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_935_713_1204.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.47 Setting the method for tear convergence to Broyden method.</div>


---

<!-- PDF page 262 -->

<div style="text-align: center;">Table 5.15 Simulation results from the closed-loop HDPE flowsheet of Figure 5.45.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream name</td><td style='text-align: center; word-wrap: break-word;'>Feed</td><td style='text-align: center; word-wrap: break-word;'>Feed2</td><td style='text-align: center; word-wrap: break-word;'>Slurry</td><td style='text-align: center; word-wrap: break-word;'>SL2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>5589.14</td><td style='text-align: center; word-wrap: break-word;'>5414.68</td><td style='text-align: center; word-wrap: break-word;'>8.442203</td><td style='text-align: center; word-wrap: break-word;'>66.0835</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C4H8</td><td style='text-align: center; word-wrap: break-word;'>4.53</td><td style='text-align: center; word-wrap: break-word;'>101.945</td><td style='text-align: center; word-wrap: break-word;'>4.53</td><td style='text-align: center; word-wrap: break-word;'>101.761</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HDPE</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5028.21</td><td style='text-align: center; word-wrap: break-word;'>10,178.8 $ ^{a)} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LP</td><td style='text-align: center; word-wrap: break-word;'>267.862</td><td style='text-align: center; word-wrap: break-word;'>444.752</td><td style='text-align: center; word-wrap: break-word;'>823.494</td><td style='text-align: center; word-wrap: break-word;'>1444.41</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>25,550</td><td style='text-align: center; word-wrap: break-word;'>51,106.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>214,919</td><td style='text-align: center; word-wrap: break-word;'>291,821</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>8.41171</td><td style='text-align: center; word-wrap: break-word;'>57.1002</td></tr></table>

a) Ethylene conversion to HDPE = 10 178.8/(5089.14 + 5414.68) = 92.5%.

The resulting ethylene conversion is slightly low. However, this workshop does not involve further validation with plant data to fine-tune the model parameters, such as kinetic parameters, to improve the simulation results.

#### 5.7 Workshop 5.2: Simulation of Stirred-Bed Gas-Phase PP Process

#### 5.7.1 Objective

The objective of this workshop is to demonstrate how to develop a simulation model for gas-phase polypropylene using stirred-bed reactors (SBRs). We model the process based on publicly available process patents [37–41] and research articles [5, 42–47]. Unlike slurry and solution processes, no liquid phase is present in the reactors, and only vapor and solids are present. There is also no solvent or liquid monomer to separate from the polymer, purify, and recycle. We show how to develop both open-loop and closed-loop processes.

#### 5.7.2 Process Description

Figure 5.48 shows a simplified diagram of a gas-phase PP process using a SBRs [44]. Polymerization takes place in a horizontal SBR that operates between 66 and 75°C and between 20 and 25 bar [44]. Reactor offgas is condensed, flashed, and returned to the reactor. The vapor recycle enters at various points along the bottom of the bed at a sufficiently low flow rate to avoid bed fluidization. The liquid recycle is sprayed at various locations along the top of the reactor. The vaporizing liquid absorbs most of the exothermic heat of polymerization, allowing for 10–15% conversion per pass to maintain a constant reactor temperature [44]. Fresh propylene enters the process at the overhead flash unit. Ethylene also enters here, for copolymerization processes. Fresh hydrogen, used for molecular weight control (chain-transfer agent), enters the

---

<!-- PDF page 263 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_778_541.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.48 A simplified diagram of a gas-phase PP process using a stirred-bed reactor for making a homopolymer. Source: Adapted from Caracotsios [44].</div>


vapor recycle stream. Catalyst deactivation agents may also enter the vapor recycle stream. A small portion of the vapor recycle stream is vented to remove propane and ethane that accumulate in the recycle loop.

The PP process uses a titanium-based catalyst and an aluminum-alkyl-based cocatalyst. Examples are titanium tetrachloride (TiCl4) and TEAL [Al-(C2H5)3], respectively [48]. Silane-based tacticity-control agents, such as diisobutyl-dimethoxysilane (DIBDMS) [41], fed with the catalyst, are commonly used to increase the isotactic content of the polypropylene.

The reactor is horizontal and cylindrical and contains several zones that are sometimes separated by weirs [44]. The polymer exists as a powder, given that the reactor temperature remains well below the polypropylene melting point of 157 °C [49]. Paddles connected to a rotating shaft mildly agitate the powder such that there is essentially no backmixing [44]. For the impact polymer process, two reactors are configured in series, and the second reactor incorporates the comonomer. Figure 5.49 shows a simplified diagram of a two-reactor system [5].

#### 5.7.3 Modeling the Stirred-Bed Reactor

During steady-state operation, the polymer level remains constant along the reactor length. The paddles along the reactor agitate the polymer only mildly, and the solids are not fluidized [44]. The polymer phase essentially experiences plug-flow conditions along the reactor length. We can simulate the plug-flow situation by using several CSTRs configured in series. Experimental studies on the RTD of polymers produced in horizontal stirred-bed reactors suggest that the polymer RTD is equivalent to that produced by three to five CSTRs [44]. Figure 5.50 compares the actual reactor to this modeling assumption. In our model, we use four CSTRs

---

<!-- PDF page 264 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_91_507_869_834.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">Figure 5.49 A simplified diagram of a gas-phase PP process using two stirred-bed reactors in series for making an impact polymer. Source: Adapted from Khare et al. [5].</div>


---

<!-- PDF page 265 -->

Actual reactor

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_172_618_770.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.50 Comparison of the actual reactor with the modeling assumption of four CSTRs in series. Source: Khare et al. [5]/American Chemical Society.</div>


to represent the stirred-bed reactor. Other modelers have used this approach as well [45]. Each CSTR receives liquid and vapor recycled from the overhead condenser, which includes fresh monomer and hydrogen. Only the first CSTR receives fresh catalyst and cocatalyst. The temperature and pressure are the same for all zones.

The concept of residence time is significantly different between this situation and that for multiple CSTRs in series. Furthermore, a residence-time calculation requires knowledge of the volumetric holdup in the reactor. We cannot measure the volume holdup very accurately because the paddles are always agitating the polymer and there is a void fraction associated with the solid phase. Therefore, we do not use residence time as a simulation target in the model and instead use reactor mass holdup. In the simulation, we constrain the CSTRs to the same polymer mass to maintain the same level along the bed length. This results in monotonically decreasing residence times for the four CSTRs corresponding to a given stirred-bed reactor, which conforms to reported experimental results [44].

---

<!-- PDF page 266 -->

The relationship between mass holdup and residence time is

 $$ \begin{aligned}Reactor mass holdup&=(Outlet mass flow rate of condensed phase)\\&\quad\times(Condensed-phase residence time)\end{aligned} $$ 

We apply this calculation to the final CSTR of each set of four CSTRs to determine the mass holdup for a given stirred-bed reactor.

#### 5.7.4 Process Flowsheet

Figures 5.51a and 5.51b show the first and second stirred-bed reactors of a two-reactor system for producing a gas-phase PP polymer. These two figures represent an expanded version of Figure 5.49. To close the recycle loops, streams 5 and 5A in Figure 5.51a together with streams 54 and 54A in Figure 5.51b would become a single stream, stream 5 and stream 54, respectively.

In the flowsheets, C1 and C2 are compressors; COND1 and COND2 are condensers; FL1 and FL2 are flash drums; MIC1 to MIX8 are mixers; P1 and P2 are pumps; RSPLT1, RSPLT1, and SPT1–SPT10 are flow splitters. We save the simulation file for Figures 5.51a and 5.51b as WS5.2 PP_Open-Loop.bkp and go through the current workshop with this file.

#### 5.7.5 Unit System, Components, and Characterization of Polymer and Site-Based Species

We use the METCBAR unit system for this workshop. Figures 5.52a and 5.52b show the components involved in the gas-phase PP process and the corresponding enterprise databases selected.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_811_808_1200.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.51a The front end of a two-reactor system for producing gas-phase PP polymer using stirred-bed reactors (open-loop).</div>


---

<!-- PDF page 267 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_164_780_502.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.51b The rear end of a two-reactor system for producing gas-phase PP polymer using stirred-bed reactors (open-loop).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_611_617_913.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 5.52a Component specifications.</div>


<div style="text-align: center;">Figure 5.52b Enterprises databases selected.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_491_1003_798_1240.jpg" alt="Image" width="31%" /></div>


---

<!-- PDF page 268 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_148_743_447.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 5.53 Defining the structure of DIBDMS (diisobutyldimethoxysilane).</div>


Propene (propylene) and ethylene are monomer and comonomer, respectively, with each having a repeated segment. TICl4 is catalyst, and TEAL is cocatalyst. Hydrogen is chain-transfer agent, and oxygen is a purge gas. Ethane and propane are impurities. DIBDMS is a tacticity-control agent [41]. A search on the Chemical Book website (www.chemicalbook.com) gives the molecular structure file, 17980-32-4.mol. We import the structure of DIBDMS into our simulation file by following the path: Properties→Components→Molecular Structure→DIBDMS→Structure and Functional Group→Structure→Draw/Import/Edit→Import→17980-32-4.mol. We also define the molecular by its connectivity according to Figure 5.53, which is needed for estimating unknown physical properties. We define the repeated segments of ethylene (R-C2H4) and propene (R-C3H6) following Figure 5.22 and characterize the attributes for ZN polymerization according to Figure 5.23.

To characterize our catalyst following Figure 5.24, we assume four active catalyst sites with a concentration of 0.0012 mol of sites per gram of catalyst [5] that are determined separately from our deconvolution of GPC data according to Section 5.5.2.3 and Supplement 5.2. We follow Section 5.5.2.2 to do deconvolution analysis and will show the deconvolution results in Section 5.7.8.

#### 5.7.6 Thermodynamic Model and Parameters

Following the LDPE example in Section 4.5.4, we choose POLYPCSF equation of state (Section 2.8) as our thermodynamic method. Based on the original references for POLYPCSF [22, 50–52], the Aspen Polymers Spheripol high impact PP copolymer example [35], our previous article [5], and a search of Aspen Polymers online help on “Parameters (POLYPCSF),” we input the pure-component parameters: Properties → Methods → Parameters → Pure Components → New → Scalar → Change name from Pure-1 to PCSAFT → Enter values as in Figure 5.54.

Specifically, PCSFTU is the segment energy parameter (K), PCSFTV is the segment diameter ( $ \mathring{A} $), PCSFTM is the segment number, and PCSFTR is a ratio parameter reserved for polymers that is equal to PCSFTM (m) divided by the

---

<!-- PDF page 269 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_776_313.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.54 POLYPCSF pure-component parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_386_777_580.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.55 User and estimated parameters of ideal-gas heat capacity.</div>


molecular weight of the monomer (M), or m/M. When these parameters are not readily available, Aspen Polymers online help recommends the following default values: (1) PCSFTU = 269.67 K, (2) PCSFTV = 4.072 Å, (3) PCSFTM = 0.02434, and (4) PCSFTR = 0.02434*M; M is the molecular weight.

Figure 5.55 shows the parameters for the ideal-gas heat capacity, CPIG-1. These parameter values came from Refs. [5, 35]. The parameter values for DIBDMS result from applying the estimation tool, based on the structure of Figure 5.53, by following the path:

Properties → Estimation → Input → Setup → Estimation option → Estimate all the missing parameters. After obtaining the estimated parameter values as shown by R-PCES for DIBDMS in Figure 5.55, we change the estimation option to “Do not estimate any parameters.”

Figures 5.56–5.58 show the estimated parameters for: (1) the liquid-phase heat capacity (CPLDIP-1) of PP based on the temperature-dependent correlation of the Design Institute for Physical Property Research (DIPPR); (2) Watson heat of vaporization (DHVLWT-1) of PP; and (3) Andrade liquid viscosity (MULAND-1) of PP. By clicking on the “Help” button, we can see the explicit temperature-dependent correlation for each parameter.

Figure 5.59 shows the estimated pure-component parameters for DIBDMS and PP.

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1139_776_1226.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.56 Estimated parameters of liquid-phase heat capacity of PP.</div>


---

<!-- PDF page 270 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_146_806_259.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.57 Estimated parameters of Watson heat of vaporization of PP.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_324_806_438.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.58 Estimated parameters of Andrade liquid viscosity of PP.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_508_648_773.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.59 Estimated pure-component parameters of DIBDMS and PP.</div>


Lastly, following Figure 5.32, we set the first parameter in the T-dependent liquid vapor pressure correlation PLXANT-1 for catalyst TiCl4, cocatalyst TEAL, and tacticity-control agent DIBDMS to a large negative number like -40. This ensures that these three components do not vaporize [36].

#### 5.7.7 Feed Streams

Table 5.16 specifies the feeds to the front end of a two-reactor flowsheet of Figure 5.51a. The last column in the table gives the total mass flows of monomers entering the process at the front end, excluding those through the tear stream 5A.

Table 5.17 specifies the feeds to the rear end of a two-reactor flowsheet of Figure 5.51b. The last column in the table gives the total mass flows of monomers entering the process at the front end, excluding those through the tear stream 54A.

We must also specify the site-based species attributes for CAT streams, following Figures 5.33 and 5.34. Figure 5.60 shows our specifications of the site-based attributes for catalyst CAT.

---

<!-- PDF page 271 -->

<div style="text-align: center;">Table 5.16 Feed streams entering the front end of the process shown in Figure 5.51a.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5A</td><td style='text-align: center; word-wrap: break-word;'>19</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>Total (excluding 5A)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T (°C)</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>32.22</td><td style='text-align: center; word-wrap: break-word;'>32.22</td><td style='text-align: center; word-wrap: break-word;'>66.001</td><td style='text-align: center; word-wrap: break-word;'>129.71</td><td style='text-align: center; word-wrap: break-word;'>32.22</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P (bar)</td><td style='text-align: center; word-wrap: break-word;'>26.2</td><td style='text-align: center; word-wrap: break-word;'>26.2</td><td style='text-align: center; word-wrap: break-word;'>30.3371</td><td style='text-align: center; word-wrap: break-word;'>26.545</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>24.4559</td><td style='text-align: center; word-wrap: break-word;'>30.3371</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>1341.9 (total)</td><td style='text-align: center; word-wrap: break-word;'>344.496</td><td style='text-align: center; word-wrap: break-word;'>17155.7</td><td style='text-align: center; word-wrap: break-word;'>0.34</td><td style='text-align: center; word-wrap: break-word;'>186,472</td><td style='text-align: center; word-wrap: break-word;'>7955.55</td><td style='text-align: center; word-wrap: break-word;'>359</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>1.7 kg/hr</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>41.6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.34</td><td style='text-align: center; word-wrap: break-word;'>0.34</td><td style='text-align: center; word-wrap: break-word;'>12.2083</td><td style='text-align: center; word-wrap: break-word;'>0.15</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propene</td><td style='text-align: center; word-wrap: break-word;'>1333.5</td><td style='text-align: center; word-wrap: break-word;'>338.5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>171,191</td><td style='text-align: center; word-wrap: break-word;'>7485.9</td><td style='text-align: center; word-wrap: break-word;'>371.119</td><td style='text-align: center; word-wrap: break-word;'>19,375.739</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propane</td><td style='text-align: center; word-wrap: break-word;'>6.7</td><td style='text-align: center; word-wrap: break-word;'>1.7</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>15,268.7</td><td style='text-align: center; word-wrap: break-word;'>469.5</td><td style='text-align: center; word-wrap: break-word;'>1.88054</td><td style='text-align: center; word-wrap: break-word;'>569.647</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DIBDMS</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.136</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Table 5.17 Feed streams entering the rear end of the process shown in Figure 5.51b.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>51</td><td style='text-align: center; word-wrap: break-word;'>53</td><td style='text-align: center; word-wrap: break-word;'>54a</td><td style='text-align: center; word-wrap: break-word;'>70</td><td style='text-align: center; word-wrap: break-word;'>71</td><td style='text-align: center; word-wrap: break-word;'>Total</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T (°C)</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>66.0009</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>78</td><td style='text-align: center; word-wrap: break-word;'>(excluding 54A)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P (bar)</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>26</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>6619</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(total)</td><td style='text-align: center; word-wrap: break-word;'>0.51</td><td style='text-align: center; word-wrap: break-word;'>116,819</td><td style='text-align: center; word-wrap: break-word;'>226</td><td style='text-align: center; word-wrap: break-word;'>4010</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.51 kg/hr</td><td style='text-align: center; word-wrap: break-word;'>6.68323</td><td style='text-align: center; word-wrap: break-word;'>0.34</td><td style='text-align: center; word-wrap: break-word;'>0.267647</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propene</td><td style='text-align: center; word-wrap: break-word;'>6584.33</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>102,144</td><td style='text-align: center; word-wrap: break-word;'>224.816</td><td style='text-align: center; word-wrap: break-word;'>3471.94</td><td style='text-align: center; word-wrap: break-word;'>10551.086</td></tr></table>

#### 5.7.8 Ziegler–Natta Kinetics Specifications

Following Figure 5.35, we create a ZN reaction set, named ZN-PP. Figure 5.61 shows the species specifications of the ZN reactions.

Based on deconvolution of GPC data for this process, we specified previously in Section 5.7.3 that the number of active catalysts is 4.  $ \underline{\text{Supplement 5.1c}} $ gives the details of these 72 reactions, together with the relevant kinetic parameters. These reactions include:

(1) Four spontaneous catalyst site-activation reactions (ACT-SPON), with one reaction per active catalyst site;

(2) Four catalyst-activation reactions (ACT-H2) by hydrogen [53], with one reaction per active catalyst site;

---

<!-- PDF page 272 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_808_474.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.60 Specification of site-based species attributes for CAT stream: Setting potential-site mole fraction (CPSFRAC) to one and the dead-site mole fraction (CDSFRAC) to zero. Set the mole fractions for the four inhibited sites (CISFRAC) (S_1 to S_4) to zero, and do the same for the four dead sites (CDSFRAC) (S_1 to S_4).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_614_743_866.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.61 Species specifications of ZN-PP reaction set.</div>


(3) Eight chain-initiation reactions by monomer C3H6 and by comonomer C2H4, with two reactions per active catalyst site;

(4) 16 chain-propagation reactions (PROP) of reacting polymer chain Pn[C3H6] with C3H6 and C2H4, and reacting polymer chain Pn[C2H4] with C3H6 and C2H4, totaling four reactions per active catalyst site;

(5) 16 reactions of chain transfer to monomer (CHAT-MON) by reacting polymer chain  $  \text{Pn}[\text{C}_3\text{H}_6]  $ with  $  \text{C}_3\text{H}_6  $ and  $  \text{C}_2\text{H}_4  $, and by reacting polymer chain  $  \text{Pn}[\text{C}_2\text{H}_4]  $ with  $  \text{C}_3\text{H}_6  $ and  $  \text{C}_2\text{H}_4  $, totaling four reactions per active catalyst site;

(6) Eight reactions of chain transfer to hydrogen (CHAT-H2) by reacting polymer chain Pn[C3H6] with H2 and by reacting polymer chain Pn[C2H4] with H2, with two reactions per active catalyst site;

(7) Four spontaneous catalyst deactivation reactions (DEACT-SPON), with one reaction per active catalyst-site type;

---

<!-- PDF page 273 -->

(8) Eight reactions of deactivation by tacticity-control agent DIBDMS by reacting an activated catalyst site  $ P_{0,i} $ with DIBDMS and by reacting a live polymer chain containing n segments attached to catalyst site i,  $ P_{n,i} $, with DIBDMS, with i = 1–4 for four active sites. (Because of the lack of deactivation reaction by agent [DEACT-AGENT] within Aspen Polymers, we use deactivation reaction by poison [DEACT-POISON] to represent these eight reactions); and

(9) Four reactions of atactic propagation (ATACT-PROP), with one reaction per active catalyst site.

To specify the reaction rate constants according to the Arrhenius form, Eq. (5.1), we follow the pre-exponential factors  $ k_{0} $ and the activation energy E for each reaction given in Supplement 5.1c.

#### 5.7.9 Specifications of Unit Operation and Chemical Reactor Blocks

###### 5.7.9.1 Mixers MIX1 to MIX8 (Figure 5.62)

<div style="text-align: center;">Figure 5.62 Specification of no pressure drop, maximum iterations, and error tolerance for MIX1 to MIX8.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_397_592_797_786.jpg" alt="Image" width="41%" /></div>


####### 5.7.9.2 Reactors R1 to R8 (Figures 5.63 and 5.64)

As illustrated in Figure 5.64, we further click on “Newton Parameters,” and specify “Line-Search” under Other (stabilization strategy), as recommended by Aspen Polymers online help for RCSTR convergence.

##### 5.7.9.3 Other Blocks

For flash units, FL1 and FL2, we specify the pressure at 2.04 MPa and the heat duty at 0 cal/sec (adiabatic). For pumps P1 and P2, we specify a discharge pressure of 2.8 MPa, a pump efficiency of 0.6, and a driver efficiency of 0.9. For compressors C1 and C2, we specify an isentropic operation with a discharge pressure of 2.68 MPa, an isentropic efficiency of 0.8, and a mechanical efficiency of 0.9. For condensers COND1 and COND2, we assume a zero pressure drop; for COND1, we assume an exit temperature of 51.6 °C, and for COND2, we specify an exit temperature of 43.5 °C. For flow splitters RSPLT1 and RSPT2, we specify the mass flow of stream 7C as 1031.9 kg/hr and of stream 56C as 984 kg/hr. Table 5.18 specifies the mole split fractions to various streams for flow splitters SPT0–SPT10.

---

<!-- PDF page 274 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_718_452.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 5.63 Specifications of reactors R1 to R8. For R5 to R8, change the condensed phase volume fraction to 0.408138.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_160_554_743_769.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 5.64 Specification of convergence parameters for reactors.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_854_646_1034.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.65 Selected convergence methods.</div>


##### 5.7.9.4 Convergence Blocks

Figure 5.65 specifies the convergence methods under: Convergence → Options → Default Methods.

We also fix the number of maximum flowsheet evaluations under:

 $$ \begin{aligned}&Convergence\rightarrow Options\rightarrow Methods\rightarrow Wegstein\rightarrow Maximum flowsheet\\&evaluations=800.\\ \end{aligned} $$ 

---

<!-- PDF page 275 -->

<div style="text-align: center;">Table 5.18 Flow splitter specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Flow splitter</td><td style='text-align: center; word-wrap: break-word;'>Mole split fraction</td><td style='text-align: center; word-wrap: break-word;'>Stream(s)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT1</td><td style='text-align: center; word-wrap: break-word;'>0.223807</td><td style='text-align: center; word-wrap: break-word;'>66</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT2</td><td style='text-align: center; word-wrap: break-word;'>0.367147, 0.204109, 0.201312</td><td style='text-align: center; word-wrap: break-word;'>LR1, LR2, LR3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT3</td><td style='text-align: center; word-wrap: break-word;'>0.9999</td><td style='text-align: center; word-wrap: break-word;'>13</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT4</td><td style='text-align: center; word-wrap: break-word;'>0.038</td><td style='text-align: center; word-wrap: break-word;'>68</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT5</td><td style='text-align: center; word-wrap: break-word;'>0.192527</td><td style='text-align: center; word-wrap: break-word;'>17</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT6</td><td style='text-align: center; word-wrap: break-word;'>0.359248, 0.204293, 0.02972</td><td style='text-align: center; word-wrap: break-word;'>VR1, VR2, VR3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT7</td><td style='text-align: center; word-wrap: break-word;'>0.03859</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT8</td><td style='text-align: center; word-wrap: break-word;'>0.462916, 0.168904, 0.232728</td><td style='text-align: center; word-wrap: break-word;'>LR5, LR6, LR7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT9</td><td style='text-align: center; word-wrap: break-word;'>0.9999</td><td style='text-align: center; word-wrap: break-word;'>62</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPT10</td><td style='text-align: center; word-wrap: break-word;'>0.204768, 0.232443, 0.230056</td><td style='text-align: center; word-wrap: break-word;'>VR5, VR6, VR7</td></tr></table>

#### 5.7.10 Open-Loop Simulation Results and Closing the Loop

We run the open-loop simulation, and the simulation converges. Table 5.19 shows the key results of the assumed tear streams 5A and 54A, computed tear streams 5 and 54, and PP product stream R8O in the open-loop flowsheet. We save the converged open-loop simulation file as WS5.2 PP_Open-Loop-Converged.bkp.

Based on the last columns of Tables 5.16 and 5.17, we see that the total amounts of propene and propane entering the process are 29,286.83 and 1108.625kg/hr, which sum together to give the total monomer mass flow of 30,395.455kg/hr. When

<div style="text-align: center;">Table 5.19 Comparison of assumed and computed tear streams, and result of PP product stream R80.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5A (assumed)</td><td style='text-align: center; word-wrap: break-word;'>5 (computed)</td><td style='text-align: center; word-wrap: break-word;'>54A (assumed)</td><td style='text-align: center; word-wrap: break-word;'>54 (computed)</td><td style='text-align: center; word-wrap: break-word;'>R8O</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>339.151</td><td style='text-align: center; word-wrap: break-word;'>343.15</td><td style='text-align: center; word-wrap: break-word;'>339.151</td><td style='text-align: center; word-wrap: break-word;'>343.15</td><td style='text-align: center; word-wrap: break-word;'>343.15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (MPa)</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td></tr><tr><td colspan="6">Mass flow (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propene</td><td style='text-align: center; word-wrap: break-word;'>171,191</td><td style='text-align: center; word-wrap: break-word;'>171,616</td><td style='text-align: center; word-wrap: break-word;'>102,144</td><td style='text-align: center; word-wrap: break-word;'>104,293</td><td style='text-align: center; word-wrap: break-word;'>5292.11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propane</td><td style='text-align: center; word-wrap: break-word;'>15,268.7</td><td style='text-align: center; word-wrap: break-word;'>15,464.7</td><td style='text-align: center; word-wrap: break-word;'>14,668</td><td style='text-align: center; word-wrap: break-word;'>14,827.8</td><td style='text-align: center; word-wrap: break-word;'>787.452</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ H_{2} $</td><td style='text-align: center; word-wrap: break-word;'>12.2083</td><td style='text-align: center; word-wrap: break-word;'>11.9805</td><td style='text-align: center; word-wrap: break-word;'>6.68323</td><td style='text-align: center; word-wrap: break-word;'>722,583</td><td style='text-align: center; word-wrap: break-word;'>0.0095</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>28,996.8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP, ATFRAC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.0384897</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>58,861.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>322,183</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.4736</td></tr></table>

---

<!-- PDF page 276 -->

compared to the PP production of 28,996.8 kg/hr for stream R8O in Table 5.19, this gives a monomer conversion of 95.398% for the open-loop simulation.

Referring to the open-loop flowsheets of Figures 5.51a and 5.51b, we close the loop by deleting the assumed tear stream 5A entering the flow splitter RSPLIT1 and replacing it with the computed tear stream 5 in Figure 5.51a. We also delete the assumed tear stream 54A entering the flow splitter RSPLIT2 and replace it with the computed tear stream 54 in Figure 5.51b. The resulting closed-loop flowsheets appear in Figures 5.66a and 5.66b.

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_388_810_724.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 5.66a The front end of a two-reactor system for producing gas-phase PP polymer using stirred-bed reactors (closed-loop).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_833_808_1201.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.66b The rear end of a two-reactor system for producing gas-phase PP polymer using stirred-bed reactors (closed-loop).</div>


---

<!-- PDF page 277 -->

<div style="text-align: center;">Table 5.20 A comparison of open-loop and closed-loop simulation results.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Total monomer feed (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>R80 (open-loop)</td><td style='text-align: center; word-wrap: break-word;'>R80 (closed-loop)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature ( $ ^\circ $C)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>343.15</td><td style='text-align: center; word-wrap: break-word;'>343.15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (MPa)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>21.7123</td><td style='text-align: center; word-wrap: break-word;'>21.7123</td></tr><tr><td colspan="4">Mass flow (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propene</td><td style='text-align: center; word-wrap: break-word;'>29,286.83</td><td style='text-align: center; word-wrap: break-word;'>5292.11</td><td style='text-align: center; word-wrap: break-word;'>5487.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Propane</td><td style='text-align: center; word-wrap: break-word;'>1108.625</td><td style='text-align: center; word-wrap: break-word;'>787.452</td><td style='text-align: center; word-wrap: break-word;'>573.331</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H $ _{2} $</td><td style='text-align: center; word-wrap: break-word;'>14.3259</td><td style='text-align: center; word-wrap: break-word;'>0.0095</td><td style='text-align: center; word-wrap: break-word;'>0.0171</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>28,996.8</td><td style='text-align: center; word-wrap: break-word;'>29,210.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PP, ATFRAC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.0384897</td><td style='text-align: center; word-wrap: break-word;'>0.1359211</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>58,861.4</td><td style='text-align: center; word-wrap: break-word;'>69,990.8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>322,183</td><td style='text-align: center; word-wrap: break-word;'>415,064</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.4736</td><td style='text-align: center; word-wrap: break-word;'>5.93</td></tr></table>

Without changing other inputs and convergence parameters, we run the closed-loop simulation, and it converges. Table 5.20 compares the results of both open-loop and closed-loop simulations for the PP product stream R8O. We save the converged closed-loop simulation file as WS5.2 PP_Closed-Loop-Converged.bkp.

#### 5.7.11 Model Applications

We re-save the simulation file, WS5.2 PP_Closed-Loop-Converged.bkp, as WS5.2a PP_Closed-Loop-PP Production vs TICL4 MASS FLOW.bkp, and use sensitivity analysis to quantify the effect of the mass flow rate of catalyst CAT (=TiCl4) on the PP production and the resulting MWN, MWW, and PDI. Figures 5.67a and 5.67b show the manipulated variable (“Vary”) and the dependent variables (“Define”) for the analysis.

Figures 5.68 and 5.69 illustrate the effects of the catalyst mass flow on the PP production (kg/hr) and on the resulting MWN and MWW.

#### 5.8 Workshop 5.3: Simulation of a Gas-Phase Fluid-Bed LLDPE Process with Condensed Mode Cooling

#### 5.8.1 Objective

The objective of this workshop is to present the details of a steady-state simulation model of a gas-phase fluidized-bed process for producing LLDPE with condensed mode cooling. Previously, we showed in Figure 5.8 a simplified flowsheet of the gas-phase fluidized-bed process for producing PP [16] and LLDPE [17, 18], and present in Supplement 5.1f the kinetic model for a LLDPE process. In this workshop, we demonstrate how to develop such a steady-state simulation model for

---

<!-- PDF page 278 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_147_638_461.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">Figure 5.67a Define the manipulated variable of the sensitivity analysis.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_534_636_855.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">Figure 5.67b Define the dependent variable of the sensitivity analysis.</div>


LLDPE based on the literature [54]. In Section 7.8, we will further demonstrate the dynamic and control aspects of this LLDPE process.

An objective of this workshop is to introduce the concept of condensed mode cooling [47–51, 53–56] to ethylene polymerization in fluidized-bed reactors. We use plant data from a UNIPOL fluidized-bed process for producing LLDPE in the Asia-Pacific and validate the model with plant data from two product grades.

#### 5.8.2 Condensed Mode Cooling in Ethylene Polymerization in a Fluidized-Bed Reactor

US patents 454399A and 4588790 [56, 57] present the concept of condensed mode cooling in ethylene polymerization in a fluidized-bed reactor (FBR). According to [56], condensed mode cooling in a FBR for an exothermic polymerization reaction cools the recycle stream to below its dew point and returns the resulting two-phase

---

<!-- PDF page 279 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>S-1 Results Summary</th><th style='text-align: center;'>Main Flowsheet</th><th style='text-align: center;'>Control Panel</th><th style='text-align: center;'>S-1</th><th style='text-align: center;'>S-1 Input</th><th style='text-align: center;'>Options</th><th style='text-align: center;'>Methods</th><th style='text-align: center;'>S-1 Results</th><th style='text-align: center;'>S-1 Results Summary</th><th style='text-align: center;'>Plot</th><th style='text-align: center;'>Scores</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td><td style='text-align: center;'>3300</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td><td style='text-align: center;'>4500</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td><td style='text-align: center;'>5000</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td><td style='text-align: center;'>5500</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td><td style='text-align: center;'>6000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.68 Effect of catalyst mass flow rate on the PP production.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>WAV '1.0'</th><th style='text-align: center;'>WAV '1.0'</th><th style='text-align: center;'></th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.69 Effect of catalyst mass flow rate on the MWN and MWW of PP.</div>


fluid stream to the reactor in order to maintain the fluidized bed at a desired temperature above the dew point of the recycle stream. This can increase the yield of polymer production, among other significant benefits. McKenna [58] presents a comprehensive review and detailed analysis of condensed model cooling in ethylene polymerization. He illustrates the concept of condensed mode cooling with a flowsheet shown in Figure 5.70. We summarize his basic analysis below.

First, we note that heat removal is the number one factor limiting the production rate of polyethylene on an industrial scale. For a fluidized-bed polymerization reactor system producing LLDPE and PP, such as the UNIPOL process of Figure 5.8 with modeling details in Supplement 5.1e, McKenna [58] notes that the melting point of a typical LLDPE is on the order of 110°C and a typical reactor-operating temperature is 85–95°C. Therefore, we have a very little margin for error in terms of heat removal. To understand the tools available for maximizing the heat removal, we

---

<!-- PDF page 280 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_148_634_552.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 5.70 An illustration of a fluidized-bed reactor (FBR) system for ethylene polymerization under condensing mode operation. Source: Adapted from McKenna [58]. In the figure, ICA represents an induced condensing agent.</div>


present a simple enthalpy balance around a gas-phase FBR by McKenna [58] below.

 $$ \begin{aligned}&F_{\mathrm{g,in}}C_{\mathrm{pg,in}}(T_{\mathrm{g,in}}-T_{\mathrm{ref}})-F_{\mathrm{g,out}}C_{\mathrm{pg,out}}(T_{\mathrm{g,out}}-T_{\mathrm{ref}})-F_{\mathrm{s,out}}C_{\mathrm{ps,out}}(T_{\mathrm{s,out}}-T_{\mathrm{ref}})\\ &\quad-UA(T_{\mathrm{R}}-T_{\mathrm{W}})-Q_{\mathrm{vap}}+R_{\mathrm{p}}V_{\mathrm{R}}(-\Delta H_{\mathrm{p}})=0\quad(5.1)\\ \end{aligned} $$ 

In the equation:

 $ F_{\mathrm{g,in}} $ and  $ F_{\mathrm{g,out}} $ = the inlet and outlet mass flow rates of process gas stream

 $ F_{s,out} = $ the outlet mass flow rate of the solid polymer stream

 $ C_{pg,in}, C_{pg,out}, $ and  $ C_{ps,out} = $ the heat capacities of the inlet and outlet process gas stream, and of the solid polymer stream

 $ T_{g,in}, T_{g,out}, T_{s,out} $, and  $ T_{ref} = $ the temperatures of the inlet and outlet process gas stream, of the outlet solid polymer stream, and the reference temperature for the calculation of the enthalpy

U = the overall heat-transfer coefficient

A = the surface area of contact between the reactor wall and the powder bed

and  $ T_{w}= $ the average temperatures of the reactor bed and the bed wall

 $ Q_{\text{vap}} = $ the total enthalpy of change due to evaporation of any liquid in the reactor

 $ R_{p} $ = the rate of reaction per unit volume of the reactor bed

 $ V_{R}= $ the volume of the reactive bed

 $ \Delta H_p = $ the overall enthalpy of polymerization

McKenna [58] further assumes that  $ T_{\text{ref}} = T_{\text{R}} = T_{\text{g,out}} $, together with the following simplifications:

(1) The solid leaves the reactor at the same temperature as the gas.

(2) The reactor is operating at a steady state with a uniform temperature  $ T_{R} $

---

<!-- PDF page 281 -->

(3) The enthalpy of the catalyst feed stream is negligible with respect to other streams.

(4) There are no significant heat losses.

With these assumptions and simplifications, we can rearrange Eq. (5.15) to give

 $$ R_{\mathrm{p}}V_{\mathrm{R}}=\frac{F_{\mathrm{g,in}}C_{\mathrm{pg,in}}(T_{\mathrm{R}}-T_{\mathrm{g,in}})+UA(T_{\mathrm{R}}-T_{\mathrm{W}})+Q_{\mathrm{vap}}}{-\Delta H_{\mathrm{p}}} $$ 

What can we learn from this defining relationship for maximizing our polymer production rate,  $ R_{p}V_{R} $?

(1) The reactor temperature  $ T_{\mathrm{R}} $ (85–95°C) has a very narrow operating range for producing LLDPE, as the melting temperature of LLDPE is about 110°C and higher bed temperature tends to promote softening and sticking of the polymer particles.

(2) It is difficult to increase the overall heat-transfer coefficient between the reactor wall and the powder bed. Increasing the gas velocity through the reactor may cause changes to the fluidizing medium.

(3) This basically leaves changes to the heat capacity  $ C_{pg,in} $ of the inlet process gas stream and to the total enthalpy due to evaporation of any liquid in the reactor  $ Q_{vap} $ as our manipulative variables for maximizing the polymer production.

The conclusion is that we can use the composition and phase conditions of the feed stream (only the inert components, obviously) to increase the amount of heat that can be removed, thus increasing the polymer production rate.

As illustrated in Figure 5.70, the feed to the bottom of the reactor below this distributor plate is composed of ethylene (monomer), nitrogen (inert), comonomer, hydrogen (chain-transfer agent), and at least one induced condensing agent (ICA) that is a partially liquefied, chemically inert species. An ICA is typically an alkane. Isomers of butane, pentane, and hexane appear to be most common, as referred to in the original patents [56, 57]. McKenna [58] presents the data in Table 5.21 to suggest a guideline for selecting an ICA.

<div style="text-align: center;">Table 5.21 Capacities of gaseous ICA components commonly used in the polymerization of ethylene.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>ICA component</td><td style='text-align: center; word-wrap: break-word;'>Nitrogen</td><td style='text-align: center; word-wrap: break-word;'>Propane</td><td style='text-align: center; word-wrap: break-word;'>n-Butane</td><td style='text-align: center; word-wrap: break-word;'>Iso-butane</td><td style='text-align: center; word-wrap: break-word;'>n-Pentane</td><td style='text-align: center; word-wrap: break-word;'>Iso-pentane</td><td style='text-align: center; word-wrap: break-word;'>n-Hexane</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Heat capacity $ ^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>7.0</td><td style='text-align: center; word-wrap: break-word;'>17.4</td><td style='text-align: center; word-wrap: break-word;'>23.3</td><td style='text-align: center; word-wrap: break-word;'>23.1</td><td style='text-align: center; word-wrap: break-word;'>28.6</td><td style='text-align: center; word-wrap: break-word;'>28.4</td><td style='text-align: center; word-wrap: break-word;'>34.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Heat of vaporization $ ^{b)} $</td><td style='text-align: center; word-wrap: break-word;'>4.8</td><td style='text-align: center; word-wrap: break-word;'>5.8</td><td style='text-align: center; word-wrap: break-word;'>5.1</td><td style='text-align: center; word-wrap: break-word;'>6.6</td><td style='text-align: center; word-wrap: break-word;'>6.5</td><td style='text-align: center; word-wrap: break-word;'>7.6</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ICA solubility in LLDPE $ ^{c)} $</td><td style='text-align: center; word-wrap: break-word;'>0.29</td><td style='text-align: center; word-wrap: break-word;'>0.94</td><td style='text-align: center; word-wrap: break-word;'>0.77</td><td style='text-align: center; word-wrap: break-word;'>1.83</td><td style='text-align: center; word-wrap: break-word;'>1.63</td><td style='text-align: center; word-wrap: break-word;'>2.85</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

a) At  $ 25^{\circ} $C, cal/K-mol.

b) At  $ 25^{\circ} $C, kcal/mol.

c) At 90 °C and 1.72 bar, g ICA per 100 g LLDPE (density = 0.918 g/cm³).

---

<!-- PDF page 282 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_147_809_341.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.71 A simulation flowsheet of a gas-phase fluidized-bed reactor system for a UNIPOL process for producing LLDPE with condensed model cooling.</div>


If we consider replacing nitrogen with an inert alkane, such as iso-pentane, the heat capacity of the gas phase will increase. In addition, as the solubility of a species in the amorphous polyethylene increases (longer, fewer branches), so does its heat of vaporization. Mckenna and his colleagues [59] present a detailed analysis of using n-hexane as an ICA in the production of LLDPE. In the commercial gas-phase fluidized-bed process for producing LLDPE that we simulate in this workshop, the ICA is iso-pentane.

#### 5.8.3 Process Flowsheet

Figure 5.71 shows a simulation flowsheet for the gas-phase fluidized-bed reactor system of a UNIPOL process for producing LLDPE. In Section 5.3.1, we discuss that the high recycle ratios of the recycle gas lead to uniform temperature and low concentration gradient in the FBR, making it reasonable to represent the FBR as a CSTR. We note that the flowsheet includes two essentially identical sections with the suffix letters for stream and block names being different. We use suffix letters A and B in the stream and block names to indicate product grades A and B. Including both sections in the same simulation flowsheet enables us to identify a single set of kinetic parameters to match the production targets for both product grades with different feed component mass flow rate and compositions. We save the simulation file as WS5.3 LLDPE.bkp.

#### 5.8.4 Unit System, Components, and Characterization of Oligomer, Polymer, and Site-Based Species

We use METCATM unit system for this workshop by starting with new unit set named METCATM based on the MET unit set and replacing the pressure unit from N/sqm to atm. Figure 5.72 shows the components involved.

Ethylene (E2) and 1-butene (C4) are monomer and comonomer, respectively, with each having a repeated segment. Catalyst CAT is TICl4, and cocatalyst COCAT is TEAL. IC5 (iso-pentane or 2-methyl butane) is an ICA. Hydrogen is a chain-transfer agent, and CO is a poison. N2 is an inert gas, and water is a cooling medium. Following the path,

Properties → Components → Polymers → Characterization → Oligomers, we define OLIGOMER according to Figure 5.73.

---

<!-- PDF page 283 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_151_619_422.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.72 Component specifications for the LLDPE process.</div>


<div style="text-align: center;">Figure 5.73 Specification of oligomer.</div>


<div style="text-align: center;">Figure 5.74 Specification of site-based species.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_432_489_798_823.jpg" alt="Image" width="37%" /></div>


We follow Figures 5.22 and 5.23 to specify the repeat segments, E-SEG and B-SEG, and choose the same built-in ZN attributes for LLDPE. Figure 5.74 specifies the site-based species.

#### 5.8.5 Deconvolution Analysis of GPC Data to Determine the Number of Active Catalyst Sites

In Section 5.5.2.3, we explained how to follow the detailed instructions in Supplement 5.2 to apply a deconvolution Excel spreadsheet, Excel for deconvolution.xls, to determine the number of active catalyst sites. Referring to the example file folders of this chapter, WS5.3, we see the GPC data for product grades A and B, Log(MW) versus d(wt)/d(log MW), where wt is the weight fraction of the slice and MW is molecular weight of the slice. Following the step-by-step instructions of Supplement 5.2, we do deconvolution analysis of the GPC data, assuming three and four active catalyst sites. See the resulting Excel files, WS5.3_Grade A_3 sites.xls, WS5.3_Grade A_4 sites, WS5.3_Grade B_3 sites.xls, WS5.3_Grade B_4 sites, in the example folder. Figures 5.75a and 5.75b compare the resulting plot

---

<!-- PDF page 284 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>(Weight Fraction) x 10^6</th><th style='text-align: center;'>Peak 1 - Cl</th><th style='text-align: center;'>Peak 2 - Cl</th><th style='text-align: center;'>Peak 3 - Cl</th><th style='text-align: center;'>Peak 4 - Cl</th><th style='text-align: center;'>Peak 5 - Cl</th><th style='text-align: center;'>Peak 6 - Cl</th><th style='text-align: center;'>Peak 7 - Cl</th><th style='text-align: center;'>Peak 8 - Cl</th><th style='text-align: center;'>Peak 9 - Cl</th><th style='text-align: center;'>Peak 10 - Cl</th><th style='text-align: center;'>Model - Cl</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.75a Weight fraction × 10⁶ versus log (molecular weight) resulting from GPC analysis of grade A data with three active catalyst sites.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>(Weight fraction) x 10^6</th><th style='text-align: center;'>Peak 1-Cl</th><th style='text-align: center;'>Peak 2-Cl</th><th style='text-align: center;'>Peak 3-Cl</th><th style='text-align: center;'>Peak 4-Cl</th><th style='text-align: center;'>Peak 5-Cl</th><th style='text-align: center;'>Peak 6-Cl</th><th style='text-align: center;'>Peak 7-Cl</th><th style='text-align: center;'>Peak 8-Cl</th><th style='text-align: center;'>Peak 9-Cl</th><th style='text-align: center;'>Peak 10-Cl</th><th style='text-align: center;'>Model -Cl</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.75b Weight fraction × 10⁶ versus log (molecular weight) resulting from GPC analysis of grade A data with four active catalyst sites.</div>


---

<!-- PDF page 285 -->

of MWD and MWDs of individual catalyst sites for grade A, assuming three and four catalyst sites, respectively. Note the negative fractional area between the MWD and the x-axis for four catalyst sites. Therefore, we choose three catalyst sites.

#### 5.8.6 Thermodynamic Model and Parameters

Following the LDPE example in Section 4.6.4 and the PP example in Section 5.7.6, we choose POLYPCSF theory equation of state (Section 2.8) as our thermodynamic method. Based on the original references for POLYPCSF [22, 50–52], the Aspen Polymers Spheripol high impact PP copolymer example [35], our previous article [5], and a search of Aspen Polymers online help on “Parameters (POLYPCSF),” we input the pure-component parameters:

Properties → Methods → Parameters → Pure Components → New → Scalar → Change name from Pure-1 to PCSAFT → Enter values as in Figure 5.76.

Following Section 4.4.5 and Figure 4.22, we use the PCES (Physical Constant Estimation System) to estimate all missing property parameters. The reader may refer to the simulation file, WS5.3 LLDPE.bkp, for the estimated property parameters. Following the path:

Properties → Methods → Parameters → Pure Components, we see parameter values from four sources: (1) Aspen enterprise databases – DB-PURE37 (i.e. APV110 PURE 37) and DB-POLYMER (i.e. APV110 Polymer); (2) Results of PCES – R-PCES; (3) User inputs. Figure 5.77 shows the user inputs for parameters of the temperature-dependent correlation ideal-gas heat capacity correlation CPG-1. This figure follows the component parameter values for H2, E2, and E-SEG and includes additional parameter values for 1-butene, B-SEG, and IC5 that we regressed from NIST property values (e.g. https://www.chemeo.com/cid/13-178-0/

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_833_778_955.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.76 POLYPCSF pure-component parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_1025_776_1222.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.77 Parameters for CPlG correlation.</div>


---

<!-- PDF page 286 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="6">Pure component scalar parameters</td></tr><tr><td colspan="2">Parameters</td><td style='text-align: center; word-wrap: break-word;'>Units</td><td style='text-align: center; word-wrap: break-word;'>Data set</td><td style='text-align: center; word-wrap: break-word;'>Component CAT</td><td style='text-align: center; word-wrap: break-word;'>Component CCAT</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TC</td><td style='text-align: center; word-wrap: break-word;'>K</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>600</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PC</td><td style='text-align: center; word-wrap: break-word;'>atm</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OMEGA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>VC</td><td style='text-align: center; word-wrap: break-word;'>cum/kmol</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr></table>

<div style="text-align: center;">Figure 5.78 Assumed property values for catalyst and cocatalyst.</div>


1-Butene). By clicking on the “help” button displayed in Figure 5.77, we can see the explicit temperature-dependent correlation for each parameter.

Figure 5.78 shows the assumed property values for catalyst CAT and cocatalyst CCAT under PURE-1. We create this folder by following the path: Properties → Methods → Parameters → Pure Components → New → Type: Scalar → Name: PURE-1 → Enter parameter name, unit, component name, and value according to Figure 5.78.

Figure 5.79 shows the parameter for the enthalpy of formation used by the van Krevelen method, DHFVK. We assume the same value for LLDPE as that reported for LPDE by Bokis et al. [60]. This parameter is important to the calculation of the heat of polymerization.

#### 5.8.7 Inlet Stream Specifications for Grades A and B

Table 5.22 specifies the inlet streams, and Table 5.23 gives the initial estimates of recycle streams. Referring to Figures 5.24 and 5.33, we specify the catalyst stream and its component attributes in Figure 5.80 for catalyst stream CAT-A. For component attributes displayed in the figure, we need to fill in the following: attribute ID – CPSFLOW, element CPSFLOW, value = 0; attribute ID – CPSFRAC, element CPSFRAC, value = 1; attribute ID – CDSFLOW, element CDSFLOW, value = 0; attribute ID – CDSFRAC, element CDSFRAC, value = 0; attribute ID – CVSFRAC, element S_1, value = 0; element S_2, value = 0; element S_3, value = 0. For catalyst stream CAT-B, we repeat the same specifications as for CAT-A in Figure 5.80, except to enter new catalyst mass flow rates of CAT = 0.165 kg/hr and CCAT = 5.06 kg/hr.

#### 5.8.8 Specifications of Unit Operation and Chemical Reactor Blocks

Table 5.24 specifies the unit operations and chemical reactors.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Parameters</td><td style='text-align: center; word-wrap: break-word;'>Units</td><td style='text-align: center; word-wrap: break-word;'>Data set</td><td style='text-align: center; word-wrap: break-word;'>Component</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DHFVK</td><td style='text-align: center; word-wrap: break-word;'>J/kmol</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-3.57e+07</td></tr></table>

<div style="text-align: center;">Figure 5.79 Assumed parameter for the enthalpy of formation for LLDPE.</div>


---

<!-- PDF page 287 -->

<div style="text-align: center;">Table 5.22 Specifications of inlet streams for grades A and B.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Streams</td><td style='text-align: center; word-wrap: break-word;'>Feed-A (Feed-B)</td><td style='text-align: center; word-wrap: break-word;'>C4-A (C4-B)</td><td style='text-align: center; word-wrap: break-word;'>C5-A (C5-B)</td><td style='text-align: center; word-wrap: break-word;'>CAT-A (CAT-B)</td><td style='text-align: center; word-wrap: break-word;'>Coldin-A (Coldin-B)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature ( $ ^\circ $C)</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>39</td><td style='text-align: center; word-wrap: break-word;'>45</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>26.59</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure, (atm [kPag])</td><td style='text-align: center; word-wrap: break-word;'>29,6077 (2898.67)</td><td style='text-align: center; word-wrap: break-word;'>31,5946 (3100)</td><td style='text-align: center; word-wrap: break-word;'>34,5554 (3400)</td><td style='text-align: center; word-wrap: break-word;'>28,5586 (2792.38)</td><td style='text-align: center; word-wrap: break-word;'>1 (0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>49,054 (45,900.5)</td><td style='text-align: center; word-wrap: break-word;'>5300 (3800)</td><td style='text-align: center; word-wrap: break-word;'>70 (70)</td><td style='text-align: center; word-wrap: break-word;'>6.1955 (5.225)</td><td style='text-align: center; word-wrap: break-word;'>1.86918E6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>49,000 (45825)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Butene</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5300 (3800)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>9 (30.5)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>N2</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CO</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.1955 (0.165)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CCAT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6 (5.06)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IC5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>70 (70)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2O</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.86918E6</td></tr></table>

---

<!-- PDF page 288 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_177_806_292.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.80 Specification of catalyst stream and component attributes.</div>


<div style="text-align: center;">Table 5.23 Recycle stream estimates for grades A and B.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Streams</td><td style='text-align: center; word-wrap: break-word;'>RECY1-A (RECY1-B)</td><td style='text-align: center; word-wrap: break-word;'>RECY-A (RECY-B)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature ( $ ^{\circ} $C)</td><td style='text-align: center; word-wrap: break-word;'>64</td><td style='text-align: center; word-wrap: break-word;'>51.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (atm)</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>22.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass flow (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>209,026</td><td style='text-align: center; word-wrap: break-word;'>918,570</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>41,480</td><td style='text-align: center; word-wrap: break-word;'>434,690</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Butene</td><td style='text-align: center; word-wrap: break-word;'>47,710</td><td style='text-align: center; word-wrap: break-word;'>124,140</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>656</td><td style='text-align: center; word-wrap: break-word;'>19,870</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>N2</td><td style='text-align: center; word-wrap: break-word;'>98,350</td><td style='text-align: center; word-wrap: break-word;'>253,910</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CO</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IC5</td><td style='text-align: center; word-wrap: break-word;'>20,830</td><td style='text-align: center; word-wrap: break-word;'>85,960</td></tr></table>

<div style="text-align: center;">Table 5.24 Block specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>React-A (React-B)</td><td style='text-align: center; word-wrap: break-word;'>86 °C, 23.2035 atm (2250 kPag); vapor-liquid; reactor volume and phase volume; Reactor volume = 150  $  \text{cum}  $; condensed phase, volume = 30  $  \text{cum}  $; streams Recy1-A (Recy1-B) = vapor, Powder-A (Powder-B) = liquid; kinetic R-1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Split1-A (Split1-B)</td><td style='text-align: center; word-wrap: break-word;'>Split fraction, Purge-A (Purge-B) = 0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Comp-A (Comp-B)</td><td style='text-align: center; word-wrap: break-word;'>Isentropic, discharge pressure = 23.149  $  \text{atm}  $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mix1-A (Mix1-B); Mix2-A (Mix2-B)</td><td style='text-align: center; word-wrap: break-word;'>Pressure = 0  $  \text{atm}  $ (no pressure drop)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cool-A (Cool-B)</td><td style='text-align: center; word-wrap: break-word;'>Design mode; hot stream outlet temperature = 49.7552 °C; minimum approach temperature = 10 °C; Pressure drop, hot side, outlet pressure = -0.68046  $  \text{atm}  $ (pressure drop);  $  U  $ methods, constant,  $  U = 0.85  $  $  \text{kW/sqm} \cdot \text{K}  $</td></tr></table>

---

<!-- PDF page 289 -->

<div style="text-align: center;">Figure 5.81 Species specifications for ZN reactions.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Species</td><td style='text-align: center; word-wrap: break-word;'>Reactions</td><td style='text-align: center; word-wrap: break-word;'>Rate Consta</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>LLDPE</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Monomers</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>BUTENE</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>goes to  $ \rightarrow $</td><td style='text-align: center; word-wrap: break-word;'>E-SEG</td><td style='text-align: center; word-wrap: break-word;'>B-SEG</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Precatalyst</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Catalysts</td><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cocatalysts</td><td style='text-align: center; word-wrap: break-word;'>CCAT</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Solvents</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transfer ag.</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hydrogens</td><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Poisons</td><td style='text-align: center; word-wrap: break-word;'>CO</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

#### 5.8.9 Ziegler–Natta Kinetics Specifications

Following Figure 5.35, we create a ZN reaction set, named R-1. Figure 5.81 shows the species specifications of the ZN reactions.

Based on deconvolution of GPC data for this process, we specified previously in Section 5.8.5 that the number of active catalysts is 3.  $ \underline{\text{Supplement 5.4}} $ gives the details of these 63 reactions, together with the relevant kinetic parameters. These reactions include:

(1) Three spontaneous catalyst site-activation reactions (ACT-SPON), with one reaction per active catalyst site;

(2) Three catalyst-activation reactions (ACT-COCAT) by cocatalyst, with one reaction per active catalyst site;

(3) Six catalyst-activation reactions (ACT-MON) by monomer C2H4 and comonomer C4H8, with two reactions per active catalyst site;

(4) Six chain-initiation reactions (CHAIN-INI) by monomer C2H4 and by comonomer C4H8, with two reactions per active catalyst site;

(5) 12 chain-propagation reactions (PROP) of reacting polymer chain Pn[C2H4] with C2H4 and C4H8, and reacting polymer chain Pn[C4H8] with C2H4 and C4H8, totaling four reactions per active catalyst site;

(6) 12 reactions of chain transfer to monomer (CHAT-MON) by reacting polymer chain Pn[C2H4] with C2H4 and C4H8, and by reacting polymer chain Pn[C4H8] with C2H4 and C4H8, totaling four reactions per active catalyst site;

(7) Six reactions of chain transfer to hydrogen (CHAT-H2) by reacting polymer chain Pn[C2H4] with H2 and by reacting polymer chain Pn[C4H8] with H2, with two reactions per active catalyst site;

(8) Six reactions of spontaneous chain transfer (CHAT-SPON) by reacting polymer chain  $  \text{Pn}[\text{C}_2\text{H}_4]  $, and by reacting polymer chain  $  \text{Pn}[\text{C}_4\text{H}_8]  $, with two reactions per active catalyst site;

(9) Three catalyst deactivation reactions by poison (DEACT-POISON), with one reaction per active catalyst-site type;

---

<!-- PDF page 290 -->

(10) Three spontaneous catalyst deactivation reactions (DEACT-SPON), with one reaction per active catalyst-site type;

(11) Three reactions of catalyst deactivation by hydrogen (DEACT-H2), with one reaction per active catalyst site.

To specify the reaction rate constants according to the Arrhenius form, Eq. (5.1), we follow the pre-exponential factors  $ k_{0} $ and the activation energy E for each reaction given in Supplement 5.4.

#### 5.8.10 Reactor and Flowsheet Simulation to Match Plant Production Targets

With inlet stream specifications in Table 5.22 and block specifications in Table 5.24, our modeling goal is to fine-tune the kinetic parameters to simulate the plant production targets for grades A and B. To speed up the simulation convergence of reactors REACT-A and REACT-B, we need to generate estimates of key-component mass flow rates in exiting streams from these reactors, as seen in the "Estimates" folder in Figure 5.43. These estimates include the mass flow rates of monomer ethylene (E2) and comonomer 1-butene (Butene) in vapor streams RECY1-A and RECY1-B, and of polymer LLDPE in liquid streams Powder-A and Powder-B. We generate these estimates in two steps. First, we run the simulation file, WS5.3 LLDPE.bkp, without these estimates and save the resulting "unconverged" simulation file as WS5.3 LLDPE no estimates.bkp. We obtain the simulated mass flow rates from this file and then make estimates of the key-component mass flow rates. Figure 5.82 illustrates the estimates for reactor REACT-A for producing grade A. Table 5.25 summarizes the estimates and simulation results. We save the converged simulation as WS5.3 LLDPE.bkp.

We follow Tables 5.4 and 5.9 to fine-tune the kinetic parameters to match the production targets.  $ \underline{\text{Supplement 5.4}} $ lists the values of the resulting kinetic parameters. Table 5.26 compares the simulation results with plant production targets.

#### 5.8.11 Model Applications

We want to demonstrate a sensitivity analysis of the effects of hydrogen mole flow on the LLDPE MI and density (DEN) [54, 61]. Following Section 2.10.2, Eqs. (2.31) and (2.32), we assume the following correlations for the LLDPE MI and DEN:

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_1013_649_1200.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 5.82 Estimates of key-component mass flow rates for reactor REACT-A.</div>


---

<!-- PDF page 291 -->

<div style="text-align: center;">Table 5.25 Estimates and simulation results of key-component mass flow rates.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Key component</td><td style='text-align: center; word-wrap: break-word;'>Ethylene (E2) in RECY1-A</td><td style='text-align: center; word-wrap: break-word;'>1-Butene (Butene) in RECY1-A</td><td style='text-align: center; word-wrap: break-word;'>LLPDE in POWDER-A</td><td style='text-align: center; word-wrap: break-word;'>Ethylene (E2) in RECY1-B</td><td style='text-align: center; word-wrap: break-word;'>1-Butene (Butene) in RECY1-B</td><td style='text-align: center; word-wrap: break-word;'>LLPDE in POWDER-B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Simulated mass flow (kg/hr); no estimates</td><td style='text-align: center; word-wrap: break-word;'>489,996</td><td style='text-align: center; word-wrap: break-word;'>52,999.7</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>458,250</td><td style='text-align: center; word-wrap: break-word;'>38,000</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Assumed mass flow estimate (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>480,000</td><td style='text-align: center; word-wrap: break-word;'>53,000</td><td style='text-align: center; word-wrap: break-word;'>10,000</td><td style='text-align: center; word-wrap: break-word;'>460,000</td><td style='text-align: center; word-wrap: break-word;'>38,000</td><td style='text-align: center; word-wrap: break-word;'>9000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Simulated mass flow (kg/hr) with estimates (converged)</td><td style='text-align: center; word-wrap: break-word;'>382,939</td><td style='text-align: center; word-wrap: break-word;'>49,169.2</td><td style='text-align: center; word-wrap: break-word;'>10,587.8 (product)</td><td style='text-align: center; word-wrap: break-word;'>361,288</td><td style='text-align: center; word-wrap: break-word;'>35,368</td><td style='text-align: center; word-wrap: break-word;'>9474.79 (product)</td></tr></table>

---

<!-- PDF page 292 -->

<div style="text-align: center;">Table 5.26 Comparison between production targets and model results.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td colspan="3">Grade A</td><td colspan="3">Grade B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polymer grade</td><td style='text-align: center; word-wrap: break-word;'>Production target</td><td style='text-align: center; word-wrap: break-word;'>Model result</td><td style='text-align: center; word-wrap: break-word;'>% Error</td><td style='text-align: center; word-wrap: break-word;'>Production target</td><td style='text-align: center; word-wrap: break-word;'>Model result</td><td style='text-align: center; word-wrap: break-word;'>% Error</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Production rate (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>10,500</td><td style='text-align: center; word-wrap: break-word;'>10,587.8</td><td style='text-align: center; word-wrap: break-word;'>0.84%</td><td style='text-align: center; word-wrap: break-word;'>9500</td><td style='text-align: center; word-wrap: break-word;'>9474.79</td><td style='text-align: center; word-wrap: break-word;'>0.27%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'>24,356</td><td style='text-align: center; word-wrap: break-word;'>25,131.1</td><td style='text-align: center; word-wrap: break-word;'>3.18%</td><td style='text-align: center; word-wrap: break-word;'>13,522</td><td style='text-align: center; word-wrap: break-word;'>13,797</td><td style='text-align: center; word-wrap: break-word;'>2.03%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'>105,496</td><td style='text-align: center; word-wrap: break-word;'>104,081</td><td style='text-align: center; word-wrap: break-word;'>1.34%</td><td style='text-align: center; word-wrap: break-word;'>55,265</td><td style='text-align: center; word-wrap: break-word;'>56,763</td><td style='text-align: center; word-wrap: break-word;'>2.71%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'>4.33</td><td style='text-align: center; word-wrap: break-word;'>4.15</td><td style='text-align: center; word-wrap: break-word;'>4.15%</td><td style='text-align: center; word-wrap: break-word;'>4.09</td><td style='text-align: center; word-wrap: break-word;'>4.11</td><td style='text-align: center; word-wrap: break-word;'>0.49%</td></tr></table>

 $$  DEN=0.936-0.02386^{*}(SFRAC^{*}100)^{0.514} $$ 

where SFRAC is the mole fraction of comonomer, 1-butene, in the LLDPE product. First, we define the MI and DEN correlations using a calculator block. Follow the path: Simulation → Flowsheeting options → Calculator → New → Name = C-1 → Input → (1) Define: See Figure 5.83 to define MWW, SFRAC, PROD, MI, and DEN (note that comonomer, 1-butene, mole fraction in the LLDPE polymer is element 2 within the SFRAC array; element 1 is the mole fraction of monomer, ethylene) → (2) Calculate: see Figure 5.84; and (3) Sequence: See Figure 5.85.

Next, we define the sensitivity analysis by following the path: Simulation → Model analysis tools → Sensitivity → New → Name = S-1 → Input: (1) Vary: see Figure 5.86; (2) Define: see Figure 5.87; and (3) Tabulate: see Figure 5.88. Figure 5.89 plots the resulting MI and DEN values as a function of hydrogen mole flow in stream FEED-A. We save the resulting simulation file as WS5.3 LLDPE_MI and DEN vs H2 Mole Flow.bkp.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_855_806_1219.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.83 Define the variables and parameters.</div>


---

<!-- PDF page 293 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_191_617_480.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 5.84 Specify Fortran equations for MI and DEN.</div>


<div style="text-align: center;">Figure 5.85 Define the calculation sequence.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_495_628_799_837.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Figure 5.86 Define the manipulated variable, "Vary."</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_412_947_798_1213.jpg" alt="Image" width="40%" /></div>


---

<!-- PDF page 294 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_174_552_464.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">Figure 5.87 Define the dependent variables and parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_528_409_822.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Figure 5.88 Specify the tabulated variables.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>S/F</th><th style='text-align: center;'>2020</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>20000000</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>18000000</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>15000000</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6</td><td style='text-align: center;'>12000000</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>8</td><td style='text-align: center;'>10000000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>8000000</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>12</td><td style='text-align: center;'>6000000</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>14</td><td style='text-align: center;'>4000000</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>16</td><td style='text-align: center;'>2500000</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>18</td><td style='text-align: center;'>1500000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>1000000</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>22</td><td style='text-align: center;'>700000</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>24</td><td style='text-align: center;'>500000</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>26</td><td style='text-align: center;'>300000</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>28</td><td style='text-align: center;'>200000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>100000</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>32</td><td style='text-align: center;'>50000</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>34</td><td style='text-align: center;'>20000</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>36</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>38</td><td style='text-align: center;'>5000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>42</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>44</td><td style='text-align: center;'>500</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.89 MI and DEN values as a function of hydrogen mole flow in stream FEED-A.</div>


---

<!-- PDF page 295 -->

#### 5.9 Workshop 5.4: Simulation of a Solution Polymerization Process for Producing Ethylene–Propylene Copolymer (EPM) or an Ethylene–Propylene–Diene Terpolymer (EPDM) with Metallocene Catalysts

#### 5.9.1 Objective

The general objective of this workshop is to introduce the methodology to simulate a polyolefin manufacturing process using a metallocene catalyst system. A specific objective is to demonstrate how to simulate the production of an EPM or an EPDM in a solution polymerization process. We explain the new features of the polymerization kinetics using a metallocene catalyst and their implementation within Aspen Polymers. As the literature contains only very limited information about the process details and operating conditions, we focus on the methodology for simulating the process under assumed operating conditions. If plant data are available, the reader may modify the workshop details easily to obtain more accurate simulations.

#### 5.9.2 Process Background

In a comprehensive review with over 500 literature references, Cesca [62] gives a detailed introduction to the chemistry of EPM and EPDM and presents the industrial solution and suspension polymerization process flowsheets. Van Duin et al. [63] present a historical and technical summary of Keltan developments defining EPDM for the past and the next 50 years. Figure 5.90 gives a process block diagram of a typical solution polymerization for producing EPDM [64].

Eisinger et al. [64] demonstrate how to adopt the UNIPOL gas-fluidized process to produce EPM or EPDM. This workshop focuses on the adaptation of

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_880_776_1199.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.90 A process block diagram for solution polymerization for producing EPDM. Source: Adapted from Eisinger et al. [64].</div>


---

<!-- PDF page 296 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_230_143_407_192.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 5.91 Molecular structures of the typical third monomer for EPDM terpolymer: (a) ENB (ethylidene norbornene; C9H12); and (b) DEPD (dicyclopentadiene; C10H12).</div>


the Ziegler–Natta polymerization kinetics model of Aspen Polymers to use a metallocene catalyst system.

For producing EPDM, the monomers include ethylene, propylene, and a diene. The typical diene monomer used includes: (1) ENB (ethylidene norbornene), CAS no. 16219-75-3, chemical formula C9H12, formula molecular weight 120.19, and molecular structure file 16129-75.3.mol (see Figure 5.91) (https://www.chemicalbook.com/ProductChemicalPropertiesCB1309456_EN.htm). While we can import the molecular structure file to represent ENB and estimate its properties, the Aspen Plus pure-component database unfortunately does not contain any repeated segment related to ENB. (2) DPCD (dicyclopentadiene), CAS no. 77-73-6, chemical formula C10H12, formula molecular weight 132.2. It is available within the Aspen Plus pure-component database, as is its repeat segment, dicyclopentadiene-R (C10H12-R). To import its molecular structure into Aspen Plus for property estimation, the structure file 77-73-6.mol is available (see Figure 5.91) (https://www.chemicalbook.com/Search_EN.aspx?keyword=dicyclopentadiene).

A typical ZN catalyst system used for producing EPM or EPDM is a vanadium catalyst–cocatalyst system,  $ VOCl_3-Al_2Et_3Cl_3 $. Cozewith and his colleagues [65, 66] were among the first to present the detailed ZN polymerization reactions and the associated experimental reaction rate constants for producing EPM or EPDM using vanadium-based catalysts in a continuous stirred-tank polymerization reactor and in a semi-batch or plug-flow polymerization reactor. Subsequently, a number of simulation and control studies based on the kinetic model of Cozewith have appeared [67–69]. Hagg et al. [70] later present an experimental and modeling study in a semi-batch bubble column reactor to produce EPM and EPDM using vanadium-based catalysts and compare the resulting ZN polymerization reaction rate constants with those from prior studies. Further modeling and experimental studies of EPM and EPDM using vanadium-based catalysts appear in [71–73].

Hamielec and Soares [74] present an excellent overview of the metallocene-catalyzed polymerization. They state that “metallocene catalysts are organometallic coordination compounds in which one or two cyclopentadienyl rings or substituted cyclopentadienyl rings are  $ \pi $-bonded to a transition metal atom (see Figure 5.92). The most remarkable feature of these catalysts is that their molecular strictures can be designed to create active center types to produce polymers with entirely novel properties.”

Continuing their previous study on the production of EPM copolymer and EPDM terpolymer using vanadium-based catalysts [70], Hagg et al. [75] present an experimental and modeling study using the same semi-batch bubble column reactor and a metallocene Et(Ind) $ _2 $ZrCl $ _2 $/MAO catalyst system. Here, “Et” stands for the ethyl group; and “Ind” represents zirconium. Et(Ind) $ _2 $ZrCl $ _2 $ is not available.

---

<!-- PDF page 297 -->

<div style="text-align: center;">Figure 5.92 Generic structure of a metallocene catalyst.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_554_147_799_491.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Figure 5.93 Molecular structure of MAO (C12H16OS2), a component of a metallocene catalyst system.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_589_521_707_610.jpg" alt="Image" width="12%" /></div>


within the Aspen Plus pure-component database. MAO represents C12H16OS₂, CAS no. 130184-19-9, and formula molecular weight 240.38. To import its structure file into Aspen Polymers for property estimation, the molecular structure file, 130184-19-9.mol, is available (see Figure 5.93) (https://www.chemicalbook.com/Search_EN.aspx?keyword=MAO).

Figure 5.94 compares the polymer yields for producing the EPDM terpolymer using both the vanadium-based ZN catalyst system, VOCl₃-Al₂Et₃Cl₃, and the metallocene catalyst system, Et(Ind)₂ZrCl₂/MAO [75]. The three monomers are ethylene, propylene, and ENB. The comparison shows the increased polymer yield when using a metallocene catalyst system.

#### 5.9.3 EPM Copolymerization Kinetics and EPDM Terpolymerization Using a Metallocene Catalyst System

Polymerization kinetics using a metallocene catalyst system include most of the reactions for ZN catalysts described in Section 5.2, except for two differences. First, a metallocene catalyst system mostly exhibits only a single active catalyst site and results in a narrow MWD with a PDI of approximately 2. Second, a metallocene catalyst system includes additional reactions involving terminal double bond (TDB) end groups that are absent in the traditional ZN polymerization kinetics. We follow [76] to explain how to include the relevant TDB reactions in Aspen Polymers.

Polymerization with a metallocene catalyst system typically leads to the formation of LCB, but the LCB frequency is usually small. The long-chain branches likely result from chain-propagation reactions involving a growing polymer chain and a

---

<!-- PDF page 298 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (minutes)</th><th style='text-align: center;'>VOC₁g/Al₂Et₃Cl₃ (sim.)</th><th style='text-align: center;'>VOC₁g/Al₂Et₃Cl₃ (exp.)</th><th style='text-align: center;'>Et(Ind)₂ZrCl₂/MAO (sim.)</th><th style='text-align: center;'>Et(Ind)₂ZrCl₂/MAO (exp.)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>12</td><td style='text-align: center;'>12</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>13</td><td style='text-align: center;'>13</td><td style='text-align: center;'>8</td><td style='text-align: center;'>6</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>25</td><td style='text-align: center;'>24</td><td style='text-align: center;'>12</td><td style='text-align: center;'>11</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>32</td><td style='text-align: center;'>30</td><td style='text-align: center;'>22</td><td style='text-align: center;'>22</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>36</td><td style='text-align: center;'>36</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>44</td><td style='text-align: center;'>44</td><td style='text-align: center;'>42</td><td style='text-align: center;'>24</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>56</td><td style='text-align: center;'>56</td><td style='text-align: center;'>54</td><td style='text-align: center;'>56</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td><td style='text-align: center;'>64</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td><td style='text-align: center;'>82</td><td style='text-align: center;'>90</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5.94 An illustration of increased EPDM terpolymer yields using a metallocene catalyst system when compared to a vanadium-based Ziegler–Natta catalyst system.</div>


TDB on a dead polymer chain. Polymer chains with TDBs are formed by some of the chain-transfer reactions. To form long-chain branches, the metal catalytic center must be open to provide a favorable reactivity ratio for the macromonomer.

Aspen Polymers tracks the concentration of TDB end groups on the dead polymer chains through a segment called TDB Segment, which typically has one less hydrogen atom than the related repeated segment. For example, we specify a C3H5-TDB end segment (C3H5-E) corresponding to a C3H6-SEG repeated segment (C3H6-R). TDB segments are generated through chain-transfer reactions and are consumed through the TDB polymerization reaction.

We summarize the ethylene–propylene copolymerization kinetics using a metallocene Et(Ind) $ _{2} $ZrCl $ _{2} $/MAO catalyst system in Table 5.27 [75]. We also convert the reported reaction rate constant  $ k $ (1/min) values in [75] to the corresponding pre-exponential factor  $ k_0 $ (1/sec) values used in Aspen Polymers according to the Arrhenius form, Eq. (5.1), assuming a reaction temperature  $ T $ of 85°C or 358 K in the equation. See Table 5.28. In the table, we follow [76] for the assumed values of the activation energies.

#### 5.9.4 Unit System, Components, and Characterization of Polymer

We choose to set up a unit system based on the MET unit set and replace the temperature from K to °C and the pressure from atm to psig. We make these changes, as we simulate the operating conditions of a UNIPOL gas-fluidized-bed process to produce EPM using a metallocene catalyst system in US patent No. 6,011,128 [64].

Figure 5.95 shows our component specifications. As METCAT1, catalyst Et(Ind) $ _{2} $ZrCl $ _{2} $, is not available within the Aspen Plus pure-component database,

---

<!-- PDF page 299 -->

<div style="text-align: center;">Table 5.27 Copolymerization kinetics for EPM (ethylene-propylene copolymer) using a metallocene Et(Ind)₂ZrCl₂/MAO catalyst system.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Representation</td><td style='text-align: center; word-wrap: break-word;'>Notes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Catalyst site activation by Cocatalyst (CAT-COCAT)</td><td style='text-align: center; word-wrap: break-word;'>$ CAT \rightarrow P_{0} $</td><td style='text-align: center; word-wrap: break-word;'>Assume a single active site.  $ P_{0} $ is a vacant site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Chain initiation by Monomer 1 (CHAIN-INI)</td><td style='text-align: center; word-wrap: break-word;'>$ P_{0} + M_{1}(C2H4) \rightarrow P_{1}[C2H4-R] $</td><td style='text-align: center; word-wrap: break-word;'>$ M_{1} $ is monomer 1,  $ C2H4 $.  $ P_{1} $ is a propagation site with an attached polymer chain containing one segment</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Chain initiation by monomer 2 (CHAIN-INI)</td><td style='text-align: center; word-wrap: break-word;'>$ P_{0} + M_{2}(C3H6) \rightarrow P_{1}[C3H6-R] $</td><td style='text-align: center; word-wrap: break-word;'>$ M_{2} $ is monomer 2,  $ C2H6 $</td></tr><tr><td rowspan="5">4. Chain propagation (PROPAGATION)</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer \rightarrow Propagating polymer chain</td><td rowspan="5">$ P_{0} $ and  $ P_{n+1} $ are polymer chains of length  $ n $ and  $ n+1 $ segments</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C2H4-R] + C2H4 \rightarrow P_{n+1}[C2H4] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C3H6-R] + C2H4 \rightarrow P_{n+1}[C2H4] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C2H4-R] + C3H6 \rightarrow P_{n+1}[C3H6-R] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C3H6-R] + C2H4 \rightarrow P_{n+1}[C3H6-R] $</td></tr><tr><td rowspan="3">5. Chain transfer to Monomer (CHAT-MON)</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer \rightarrow Dead chain + Growing monomer</td><td rowspan="3">$ D_{n} $ is a dead polymer chain of length  $ n $ segments.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C2H4] + C3H6 \rightarrow D_{n} + P_{1}[C3H6-R] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C3H6] + C3H6 \rightarrow D_{n} + P_{1}[C3H6-R] $</td></tr><tr><td rowspan="3">6. Chain transfer to agent (CHAT-AGENT OR CHAT-H2)</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Transfer agent \rightarrow Dead chain + Vacant site</td><td rowspan="3">$ P_{n}[C2H4] + H_{2} + P_{0} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C2H4] + Hydrogen \rightarrow D_{n} + P_{0} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C3H6] + Hydrogen \rightarrow D_{n} + P_{0} $</td></tr><tr><td rowspan="2">7. Spontaneous Catalyst Deactivation (DEACT-SPON)</td><td style='text-align: center; word-wrap: break-word;'>$ P_{0} \rightarrow DCAT $</td><td rowspan="2">DACT is a deactivated catalyst site</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n} \rightarrow D_{n} + DCAT $</td></tr><tr><td rowspan="2">8. TDB polymerization reaction (TDB-POLY)</td><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C2H4-R] + D_{n}[TDB-Seg] \rightarrow P_{n+m}[C2H4-R] $</td><td rowspan="2">TDB = terminal double bond</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{n}[C3H6-R] + D_{n}[TDB-Seg] \rightarrow P_{n+m}[C3H6-R] $</td></tr></table>

---

<!-- PDF page 300 -->

<div style="text-align: center;">Table 5.28 Conversion of the reported reaction rate constant  $ k $ (1/min) values in Ref. [75] to the corresponding pre-exponential factor  $ k_0 $ (1/sec) values used in Aspen Polymers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Comp 1</td><td style='text-align: center; word-wrap: break-word;'>Comp 2</td><td style='text-align: center; word-wrap: break-word;'>k (1/min) [75]</td><td style='text-align: center; word-wrap: break-word;'>K (1/sec)</td><td style='text-align: center; word-wrap: break-word;'>E_{a} (cal/mol)</td><td style='text-align: center; word-wrap: break-word;'>Exp[E_{a}/RT]</td><td style='text-align: center; word-wrap: break-word;'>K_{0} (1/sec)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT-COCAT</td><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>0.66667</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>51,005.47</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>5E4</td><td style='text-align: center; word-wrap: break-word;'>833.3333</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>15,633,755</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>5E3</td><td style='text-align: center; word-wrap: break-word;'>83.33333</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>1,563,375</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>1E6</td><td style='text-align: center; word-wrap: break-word;'>16,666.67</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>3.13E8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>6E5</td><td style='text-align: center; word-wrap: break-word;'>10,000</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>1.88E8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>2.1E6</td><td style='text-align: center; word-wrap: break-word;'>35,000</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>6.57E8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>5.3E5</td><td style='text-align: center; word-wrap: break-word;'>8833.333</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>5.33035E-5</td><td style='text-align: center; word-wrap: break-word;'>1.66E8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>7650.821</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>7650.821</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-H2</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>3457</td><td style='text-align: center; word-wrap: break-word;'>57.61667</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>4,408,148</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-H2</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>3457</td><td style='text-align: center; word-wrap: break-word;'>57.61667</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>4,408,148</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DEACT-SPON</td><td style='text-align: center; word-wrap: break-word;'>Active site P_{0}</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>80</td><td style='text-align: center; word-wrap: break-word;'>1.33333</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>102,010.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DEACT-SPON</td><td style='text-align: center; word-wrap: break-word;'>Polymer chain P_{n}</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>80</td><td style='text-align: center; word-wrap: break-word;'>1.33333</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.30705E-5</td><td style='text-align: center; word-wrap: break-word;'>102,010.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-POLY</td><td style='text-align: center; word-wrap: break-word;'>C2H4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2.1E6</td><td style='text-align: center; word-wrap: break-word;'>35,000</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.39131E-5</td><td style='text-align: center; word-wrap: break-word;'>2.68E9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-POLY</td><td style='text-align: center; word-wrap: break-word;'>C3H6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.3E5</td><td style='text-align: center; word-wrap: break-word;'>8333.333</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1.39131E-5</td><td style='text-align: center; word-wrap: break-word;'>6.76E8</td></tr></table>

Source: Adapted from Hagg et al. [75].

we use TICl4 to represent this component (but will enter the correct molecular weight of 420.81 later in Figure 5.99). We define the cocatalyst (COCAT) MAO of Figure 5.94 by importing its molecular structure file, 130184-19-9.mol (https://www.chemicalbook.com/Search_EN.aspx?keyword=MAO) (available in the workshop folder for this chapter). We follow the path: Properties → Components → Molecular structure → COCAT → Structure and functional group → Draw/import/edit: import 130184-19-9.mol → Calculate bonds → General → Atom number and atom type automatically defined by Aspen Plus. We save the simulation file as WS5.4 EPM_metallocene kinetics.bkp.

In Figure 5.95, ethylene and propylene are monomers, and their repeated segments are E-SEG and P-SEG. TDB-SEG is a terminal double-bound end segment, with one less hydrogen atom than the repeated segment P-SEG. EPM is the ethylene-propylene copolymer. It is not available within the Aspen Plus polymer component database, so we specify it as a generic polymer component. n-Hexane is a solvent, hydrogen is a chain-transfer agent, and nitrogen is an inert gas.

Next, we follow the path: Properties → Components → Polymer and specify the polymer segments according to Figure 5.96.

For the Polymers folder, we choose built-in attribute group, ZN selection for our polymer EPM. Figure 5.97 shows the specifications for the site-based species.

---

<!-- PDF page 301 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Component ID</td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Component name</td><td style='text-align: center; word-wrap: break-word;'>Alias</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>METCAT1</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>TITANIUM-TETRACHLORIDE</td><td style='text-align: center; word-wrap: break-word;'>TICL4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{3}H_{6}-2 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEXANE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>N-HEXANE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{6}H_{14}-1 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EPM</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>POLY(ETHYLENE-PROPYLENE)</td><td style='text-align: center; word-wrap: break-word;'>$ P(E\&amp;P) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4}-R $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{3}H_{6}-R $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>VINYL-E</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{3}-E $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NITROGEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>NITROGEN</td><td style='text-align: center; word-wrap: break-word;'>$ N_{2} $</td></tr></table>

<div style="text-align: center;">Figure 5.95 Component specifications.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_640_617_836.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 5.96 Segment definition for polymer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_916_762_1205.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 5.97 Specification of site-based species.</div>


---

<!-- PDF page 302 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="12">Pure component scalar parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Parameters</td><td style='text-align: center; word-wrap: break-word;'>Units</td><td style='text-align: center; word-wrap: break-word;'>Data set</td><td style='text-align: center; word-wrap: break-word;'>Component METCAT1</td><td style='text-align: center; word-wrap: break-word;'>Component COCAT</td><td style='text-align: center; word-wrap: break-word;'>Component ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>Component PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>Component HYDROGENE</td><td style='text-align: center; word-wrap: break-word;'>Component E-SEG</td><td style='text-align: center; word-wrap: break-word;'>Component P-SEG</td><td style='text-align: center; word-wrap: break-word;'>Component TDB-SEG</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCSFTM</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>1.55873</td><td style='text-align: center; word-wrap: break-word;'>1.9598</td><td style='text-align: center; word-wrap: break-word;'>0.828469</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCSFTU</td><td style='text-align: center; word-wrap: break-word;'>K</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>287.028</td><td style='text-align: center; word-wrap: break-word;'>287.028</td><td style='text-align: center; word-wrap: break-word;'>179.412</td><td style='text-align: center; word-wrap: break-word;'>207.19</td><td style='text-align: center; word-wrap: break-word;'>12.5276</td><td style='text-align: center; word-wrap: break-word;'>237.088</td><td style='text-align: center; word-wrap: break-word;'>267.732</td><td style='text-align: center; word-wrap: break-word;'>237.088</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCSFTV</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4.57764</td><td style='text-align: center; word-wrap: break-word;'>4.57764</td><td style='text-align: center; word-wrap: break-word;'>3.4305</td><td style='text-align: center; word-wrap: break-word;'>3.5356</td><td style='text-align: center; word-wrap: break-word;'>2.97294</td><td style='text-align: center; word-wrap: break-word;'>3.25929</td><td style='text-align: center; word-wrap: break-word;'>3.49356</td><td style='text-align: center; word-wrap: break-word;'>3.25929</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCSFTR</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.0481045</td><td style='text-align: center; word-wrap: break-word;'>0.0402106</td><td style='text-align: center; word-wrap: break-word;'>0.0481045</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 5.98 POLYPCSF pure-component parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_352_696_730.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 5.99 Assumed pure-component parameters for METCAT1 and COCAT.</div>


#### 5.9.5 Thermodynamic Method and Property Parameters for Components and Polymer

Our solution polymerization reactor for EPM operates at 300 psig [64], which is close to the operating pressure of our gas-phase stirred-tank reactor for PP in Section 5.7. Therefore, we choose POLYPCSF as our thermodynamic method. Following our examples for LDPE (Section 4.4.4), EVA (Section 4.6.4), and PP (Section 5.7.6), we enter the pure-component parameters for POLYPCSF by following the path: Properties → Methods → Parameters → Pure Components → New → Scalar → Change name from Pure-1 to PCSF → enter values as in Figure 5.98. We assume that TDB-SEG segment has the same parameter values as E-SEG.

We follow the same procedure in creating the pure-component parameter folder PCSF to generate a pure-component parameter folder named CAT and enter the values as in Figure 5.99. Note the molecular weight (MW) for our catalyst METCAT1, Et(Ind) $ _{2} $ZrCl $ _{2} $.

Figure 5.100 shows the parameters for the ideal-gas heat capacity, CPlG-1. These parameter values came from references [4, 5, 35]. We estimate the parameter values for COCAT by applying the estimation tool, based on the structure of Figure 5.93 and the molecular structure file, 130184-19-9.mol. Specifically, we follow the

---

<!-- PDF page 303 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_148_781_298.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.100 Parameters for ideal-gas heat capacity, CPlG-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_378_779_512.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 5.101 Parameter values for enthalpy of formation by the van Krevelen method, DHFVK.</div>


path: Properties → Estimation → Input → Setup → Estimation option → Estimate all missing parameters. After obtaining the estimated parameter values as shown by R-PCES for COCAT in Figure 5.100, we change the estimation option to “Do not estimate any parameters.”

Figure 5.101 displays the parameter values for enthalpy of formation by the van Krevelen method, DHFVK. These values came from WS4.3 of Section 4.6.

The reader may see other parameter values for DHVLWT-1 (heat of vaporization), KLDIP-1 (liquid thermal conductivity), MULAND-1 (liquid viscosity), PLXANT-1 (liquid vapor pressure), and SIGDIP (liquid surface tension) resulting from property estimation (R-PCES) from the simulation file WS5.4 EPM_metallocene_kinetics.bkp.

#### 5.9.6 Process Flowsheet and Inlet Stream and Block Specifications

Figure 5.102 depicts the fluidized-bed reactor system in our UNIPOL process for producing EPM copolymer.

Figure 5.103 shows the specification of CATFEED stream.

For component attributes displayed in Figure 5.103, we need to continue specifying the following attributes: CPSFLOW = CDSFLOW = CDSFRAC = CVSFLOW = CVSFRAC = 0.

For feed steam, FRESHFD, we specify 5 °C, 400 psig, and component mass flow rate (kg/hr): COCAT = 30, Ethylene = 25,000, Propylene = 5000, H2 = 5, and N2 = 20. Table 5.29 gives the block specifications. We note that the reactor-operating pressure of 300 psig (20.42 atm) follows the metallocene catalyst examples for polyolefins in [64, 76] and the PP and LLDPE examples in WS5.2 and WS5.3. The reader may change this pressure with available plant data.

---

<!-- PDF page 304 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_148_771_654.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 5.102 Fluidized-bed reactor system for producing EPM copolymer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_740_811_836.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5.103 Specifications of CATFEED stream.</div>


#### 5.9.7 Base-Case Simulation Results

In our base-case simulation, the actual reactions and their kinetic parameters are slightly different from those listed in Table 5.28 based on the literature to obtain reasonable monomer and copolymer yields, MWN, MWW, and PDI, as well as SFRACs (mole fractions of monomer and comonomer in the polymer product). See Tables 5.30 and 5.31 for the kinetic parameters and stream results for feed and polymer product.

We see a total monomer conversion of 10302.4/(25000 + 5000), or 34.34%. The mole fractions of ethylene, propylene, and TDB segment in the EPM copolymer are 0.807252, 0.192524, and 0.000224, respectively. The MWN is 134463 and MWW is 268975, giving a PDI of 1.99888. Should the reader have plant data for these results, it is not difficult to fine-tune the kinetic parameters to match the plant production

---

<!-- PDF page 305 -->

<div style="text-align: center;">Table 5.29 Block specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>T (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (psig)</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SOLREACT</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>300</td><td style='text-align: center; word-wrap: break-word;'>(1) Setup: Vapor-liquid phase; reactor volume and phase volume; reactor volume = 300 cum; condensed phase volume = 88 cum; streams: Vapor-vapor phase, POLY-liquid phase; kinetics: R-1. (2) Convergence (see Section 3.6): estimates - component mass flow, EPM = 10,000 kg/hr; flash options: maximum iterations = 200; convergence parameters: mass-balance convergence solver - Newton, maximum iterations - 100, and “initialize using integration”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPLIT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Split fraction: PURGE - 0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COMP</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Isentropic; discharge pressure = 325 psig</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COOLER</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>Pressure = -10 psia (pressure drop); flash options - maximum iteration = 200</td></tr></table>

targets by following examples in previous workshops of this chapter. We save the simulation file as WS 5.4 EPM_Metallocene_Kinetics.bkp.

#### 5.9.8 Extension to EPDM (Ethylene–Propylene–Diene Terpolymer)

As discussed in Section 5.9.2, Aspen Plus version 11 can represent the components involved in producing an EDPM terpolymer using DPCD as the diene monomer. In the simulation files for WS5.4, we have included a completed component and property file, WS 5.4 EPDM_metallocene_properties.bkp, for using DPCD as the diene monomer and a metallocene Et(Ind) $ _{2} $ZrCl $ _{2} $/MAO catalyst system [72]. Figure 5.104 shows the component specifications. Here, the details of the metallocene catalyst and cocatalyst are identical to those of the EPM copolymer example in WS5.4. The reader can refer to the simulation file to learn more about the components and properties involved.

Hagg et al. [75] have presented a generic reaction mechanism, reaction rate equations, and experimental reaction rate constants for an EPDM terpolymerization using a metallocene Et(Ind) $ _{2} $ZrCl $ _{2} $/MAO catalyst system. The third monomer, ENB, and its related repeat segment are not available within Aspen Plus pure-component and segment databases; we do not simulate the EPDM work of Hagg et al. [75]. However, when adequate polymerization kinetic data become available for DPCD as the diene monomer and ENB and its repeat segment become available in Aspen Plus databases, we can apply the same modeling methodology for the EPM (ethylene–propylene copolymer) to the ethylene–propylene–DPCD terpolymerization using a metallocene catalyst system.

---

<!-- PDF page 306 -->

<div style="text-align: center;">Table 5.30 Actual reactions and kinetic parameters for base-case simulation.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Site no.</td><td style='text-align: center; word-wrap: break-word;'>Comp 1</td><td style='text-align: center; word-wrap: break-word;'>Comp 2</td><td style='text-align: center; word-wrap: break-word;'>Pre-Exp (1/sec)</td><td style='text-align: center; word-wrap: break-word;'>Act-Energy (cal/mol)</td><td style='text-align: center; word-wrap: break-word;'>Order</td><td style='text-align: center; word-wrap: break-word;'>Tdp Frac</td><td style='text-align: center; word-wrap: break-word;'>References temperature ( $ ^\circ $C)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ACT-COCAT</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>METCAT1</td><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'>703,000</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.3675e+07</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>875,000</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>3.3675e+07</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>3.3675e+06</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>8.75e+06</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>8.75e+06</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>7200</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>7200</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>7200</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>7200</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-H2</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>3000</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-H2</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>3000</td><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DEACT-SPON</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.0006</td><td style='text-align: center; word-wrap: break-word;'>10,000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-POLY</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>TDB-SEG</td><td style='text-align: center; word-wrap: break-word;'>0.02</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1e+35</td></tr></table>

---

<!-- PDF page 307 -->

<div style="text-align: center;">Table 5.31 Stream results for feed and polymer.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>CATFEED</td><td style='text-align: center; word-wrap: break-word;'>FRESHFD</td><td style='text-align: center; word-wrap: break-word;'>POLY</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>85</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure (psig)</td><td style='text-align: center; word-wrap: break-word;'>420</td><td style='text-align: center; word-wrap: break-word;'>400</td><td style='text-align: center; word-wrap: break-word;'>300</td></tr><tr><td colspan="4">Mass flow (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>METCAT1</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>29.9641</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>25,000</td><td style='text-align: center; word-wrap: break-word;'>150.882</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5000</td><td style='text-align: center; word-wrap: break-word;'>54.692</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>0.0262353</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EPM</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10,302.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NITROGEN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0.0262353</td></tr><tr><td colspan="4">Polymer attributes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>134,463</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>268,975</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDI</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.99888</td></tr><tr><td colspan="4">SFRAC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.807252</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.192524</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-SEG</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.000224064</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Component ID</td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Component name</td><td style='text-align: center; word-wrap: break-word;'>Alias</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>METCAT1</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>TITANIUM-TETRACHLORIDE</td><td style='text-align: center; word-wrap: break-word;'>TICL4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COCAT</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPYLEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{3}H_{6}-2 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DPCD</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>DICYCLOPENTADIENE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{10}H_{12}-D_{0} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>ETHYLENE-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{4}-R $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>PROPYLENE-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{3}H_{6}-R $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DPCD-R</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>DICYCLOPENTADIENE-R</td><td style='text-align: center; word-wrap: break-word;'>$ C_{10}H_{12}-R $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDB-SEG</td><td style='text-align: center; word-wrap: break-word;'>Segment</td><td style='text-align: center; word-wrap: break-word;'>VINYL-E</td><td style='text-align: center; word-wrap: break-word;'>$ C_{2}H_{3}-E $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EPDM</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>GENERIC-POLYMER-COMPON...</td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEXANE</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>N-HEXANE</td><td style='text-align: center; word-wrap: break-word;'>$ C_{6}H_{14}-1 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>HYDROGEN</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NITROGEN</td><td style='text-align: center; word-wrap: break-word;'>Conventional</td><td style='text-align: center; word-wrap: break-word;'>NITROGEN</td><td style='text-align: center; word-wrap: break-word;'>$ N_{2} $</td></tr></table>

<div style="text-align: center;">Figure 5.104 Component specifications for simulating the manufacturing of an ethylene-propylene-DPCD terpolymer.</div>


---

<!-- PDF page 308 -->

### 5.10 Conclusions

In this chapter, we have demonstrated an effective methodology for estimating kinetic parameters for ZN polymerization for commercial processes producing polyolefins, such as HDPE, PP, LLDPE, and EPDM. We consider catalyst activation, initiation, propagation, chain transfer, deactivation, and other polymer-specific reactions. We have identified the reaction rate constants in ZN polymerization kinetics that have the most significant impacts on common production targets, which greatly simplifies the kinetic parameter estimation for simulation and optimization models for polyolefin processes using plant data.

Our methodology begins with a kinetic model considering a single active catalyst site, followed by converting the single-site model into a model assuming multiple active catalyst sites. We apply deconvolution analysis to characterize the GPC MWD data to determine the most probable CLD for each catalyst site, assuming a Flory distribution. The deconvolution analysis identifies the expected number of active catalyst sites together with the weight fraction and MWN for each active catalyst site.

We demonstrate an effective methodology in Figures 5.9a and 5.9b to use efficient software tools, such as data fit, sensitivity analysis, and design specification in Aspen Polymers, to simultaneously estimate multiple reaction rate constants for ZN kinetics to match several datasets of production targets, such as production rates, MWN, and SFRAC, in a computer-aided step-by-step procedure. This differentiates our study from most of the previous studies, which sequentially estimated these reaction rate constants. Our methodology in Figure 5.9a, b also greatly simplifies the kinetic parameter estimation for the multisite model, in that we only need to regress selected kinetic parameters for the multisite model to match the plant data for PDI and related production targets, such as the atactic fraction for PP production.

Our methodology in Figures 5.9a and 5.9b results in part from our insights and experiences from applying our methodology to several dozen commercial polyolefin processes at two of the world's largest petrochemical companies in the Asia-Pacific over the past two decades. Applying our methodology using efficient software tools results in validated simulation and optimization models that we can use to quantify changes in process operations, process capacity scale-up, polymer quality control, product grade change, etc.

Our detailed supplements with modeling examples and Excel modeling spreadsheet will be useful to practicing engineers interested in applying process modeling and optimization to commercial polyolefin production.

This chapter also presents four detailed hands-on workshops for simulating HDPE, PP, LLDPE, and EPM (ethylene-propylene copolymer) using ZN catalyst and metallocene catalysts–cocatalysts, and demonstrates how to apply efficient simulation software tools such as data fit, sensitivity analysis, and design specifications for kinetic parameter estimation, process improvement, and optimization.

---

<!-- PDF page 309 -->

## References

1 Soares, J.B.P. and McKenna, T.F.L. (2012). Polyolefin Reaction Engineering. Weinheim: Wiley-VCH.

2 Touloupidis, V. (2014). Catalytic olefin polymerization process modeling: multi-scale approach and modeling guidelines for micro-scale/kinetic modeling. Macromolecular Reaction Engineering 8: 508.

3 Zacca, J.J. and Ray, W.H. (1993). Modeling of liquid phase polymerization of olefins in loop reactors. Chemical Engineering Science 48: 3743.

4 Khare, N.P., Seavey, K.C., Liu, Y.A. et al. (2002). Steady-state and dynamic modeling of commercial slurry high-density polyethylene (HDPE) processes. Industrial and Engineering Chemistry Research 41: 5601.

5 Khare, N.P., Lucas, B., Seavey, K.C. et al. (2004). Steady-state and dynamic modeling of commercial gas-phase polypropylene processes using stirred-bed reactors. Industrial and Engineering Chemistry Research 43: 884.

6 Zhang, C., Shao, Z., Chen, X. et al. (2014). Kinetic parameter estimation of HDPE slurry process from molecular weight distribution: estimability analysis and multistep methodology. AIChE Journal 60: 3442.

7 Dotson, N.A., Galvan, R., Laurence, R.L., and Tirrell, M. (1996). Polymerization Process Modeling. New York: Wiley-VCH.

8 Meng, W., Li, J., Chen, B., and Li, H. (2013). Modeling and simulation of ethylene polymerization in industrial slurry reactor series. Chinese Journal of Chemical Engineering 21: 850.

9 Zhao, X., Guo, X., Chen, P. et al. (2012). Simulation and analysis of an ethylene slurry polymerization system using supercritical propane. Industrial and Engineering Chemistry Research 51: 682.

10 Zheng, Z.W., Shi, D.P., Su, P.L. et al. (2011). Steady-state and dynamic modeling of the basell multireactor olefin polymerization process. Industrial and Engineering Chemistry Research 50: 322.

11 Lu, C., Zhang, M., Jiang, S., and Song, D. (2006). Application of ASPEN PLUS in large-scale polypropylene plant. Qilu Petrochemical Technology 34: 404.

12 Touloupides, V., Kanellopoulos, V., Pladis, P. et al. (2010). Modeling and simulation of an industrial slurry-phase catalytic olefin polymerization reactor series. Chemical Engineering Science 65: 3208.

13 Chen, K., Tian, Z., Luo, N., and Liu, B. (2014). Modeling and simulation of Borstar bimodal polyethylene process based on a rigorous PC-SAFT equation of state model. Industrial and Engineering Chemistry Research 53: 19905.

14 Luo, Z.W., Zheng, Y., Cao, Z.K., and Wen, S.H. (2007). Mathematical modeling of the molecular weight distribution of polypropylene produced in a loop reactor. Polymer Engineering and Science 47: 1643.

15 Zheng, X.G. (2015). Operation optimization of dual-loop polypropylene process by polymers plus software. Petrochemical Technology 44: 612.

---

<!-- PDF page 310 -->

16 Shamiri, A., Hussain, M.A., Mjalli, F.S., and Mostoufi. (2010). Kinetic modeling of propylene homopolymerization in a gas-phase fluidized-bed reactor. Chemical Engineering Journal 161: 240.

17 Knuuttila, H., Lehtinen, A., and Nummila-Pakarinen, A. (2004). Advanced polyethylene technologies- controlled material properties. Advances in Polymer Science 169: 13.

18 Kashani, A.F., Abedini, H., and Kalace, M.R. (2011). Simulation of an industrial linear low density polyethylene plant. Chemical Product and Process Modeling 6 (Art. 34). https://www.degruyter.com/document/doi/10.2202/1934-2659.1611/htML.

19 You, C. and Li, S. (2007). Analysis and application of model building procedure in polypropylene plant. Petrochemical Industry Technology 14 (2): 56.

20 Luo, Z.H., Su, P.L., Shi, D.P., and Zheng, Z.W. (2009). Steady-state and dynamic modeling of commercial bulk polypropylene process of Hypol technology. Chemical Engineering Journal 149: 370.

21 Seavey, K.C., Khare, N.P., Liu, Y.A. et al. (2003). Quantifying relationships among the molecular weight distribution, non-Newtonian shear viscosity and melt index for linear polymers. Industrial and Engineering Chemistry Research 42: 5354.

22 Gross, J. and Sadowski, G. (2001). Perturbed-chain SAFT: an equation of state based on a perturbation theory for chain molecules. Industrial and Engineering Chemistry Research 40: 1244.

23 Sanchez, I.C. and Lacombe, R.H. (1976). An elementary molecular theory of classic fluids. Pure fluids. Journal of Physical Chemistry 80: 2352.

24 Lacombe, R.H. and Sanchez, I.C. (1976). Statistical thermodynamics of fluid mixtures. The Journal of Physical Chemistry 80: 2568.

25 Sanchez, I.C. and Lacombe, R.H. (1978). Statistical thermodynamics of polymer solutions. Macromolecules 11: 1145.

26 Tian, Z., Chen, K.R., Liu, B.P. et al. (2015). Short-chain branching distribution oriented model development for Borstar bimodal polyethylene process and its correlation with product performance of slow crack growth. Chemical Engineering Science 130: 41.

27 Tremblay, D. (2017). Modeling polymerization processes. Aspen Optimize Training, OPTIMIZE 2017, Houston, TX, April 2017.

28 Mattos Neto, A.G., Freitas, M.F., Nele, M., and Pinto, J.C. (2005). Modeling ethylene/1-butene copolymerizations in industrial slurry reactors. Industrial and Engineering Chemistry Research 44: 2697.

29 Sharma, N. and Liu, Y.A. (2019). 110th anniversary: an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient software tools. Industrial and Engineering Chemistry Research 58: 14209.

30 Kou, B., McAuley, K.B., Hsu, C.C. et al. Mathematical model and parameter estimation for gas-phase ethylene homopolymerization with supported metallocene catalyst. Industrial and Engineering Chemistry Research 44: 2428.

---

<!-- PDF page 311 -->

31 Kou, B., McAuley, K.B., Hsu, C.C., and Bacon, D.W. (2005). Mathematical model and parameter estimation for gas-phase ethylene-hexene copolymerization with metallocene catalyst. Macromolecular Materials and Engineering 290: 537.

32 Baughman, D.R. and Liu, Y.A. (1995). Neural Networks in Bioprocessing and Chemical Engineering. Atlanta, GA: Elsevier.

33 You, C. (2006). Modeling and analysis of polypropylene process in steady and dynamic states. MS thesis. College of Chemical Engineering, Tianjin University.

34 Soares, J.B.P. and Hamielec, A.E. (1995). Deconvolution of chain-length distribution of linear polymers made by multiple-site-type catalysts. Polymer 36: 2257.

35 Aspen Technology, Inc. (2021). Bessel Spheripol polypropylene process simulation example. https://esupport.aspentech.com/S_Article_id=000038267 (accessed 11 March 2021).

36 Bokis, C.P., Orbey, H., and Chen, C.C. (1999). Properly model polymer processes. Chemical Engineering Progress 95 (4): 39.

37 Shepard, J.W., Jezl, J.L., Peters, E.F., and Hall, R.D. (1976). Divided horizontal reactor for the vapor phase polymerization of monomers at different hydrogen levels. US Patent 3,957,488.

38 Jezl, J.L., Peters, E.F., Hall, R.D., and Shepard, J.W. (1976). Process for the vapor phase polymerization of monomers in a horizontal, quench-cooled, stirred-bed reactor using essentially total off-gas recycle and melt finishing. US Patent 3,965,083.

39 Peters, E.F., Spangler, M.J., Michaels, G.O., and Jezl, J.L. (1976). Vapor phase reactor off-gas recycle system for use in the vapor state polymerization of monomers. US Patent 3,971,768.

40 Jezl, J.L. and Peters, E.F. (1978). Horizontal reactor for the vapor phase polymerization of monomers. US Patent 4,129,701.

41 Buchelli, A. and Caracotsios, M. (1996). Polymerization of alpha-olefins. US Patent 5,504,166.

42 Choi, K.Y. and Ray, W.H. (1988). The dynamic behavior of continuous stirred-bed reactors for the solid catalyzed gas phase polymerization of propylene. Chemical Engineering Science 43: 2587.

43 Kissel, W.J., Han, J.H., and Meyer, J.A. (1999). Polypropylene: structure, properties, manufacturing processes, and applications. In: Handbook of Polypropylene and Polypropylene Composites (ed. H.G. Karian), 15. New York: Marcel Dekker.

44 Caracotsios, M. (1992). Theoretical modelling of Amoco's gas phase horizontal stirred bed reactor for the manufacturing of polypropylene resins. Chemical Engineering Science 47: 2591.

45 Zecca, J.J., Dehling, J.A., and Ray, W.H. (1996). Reactor residence time distribution effects on the multistage polymerization of olefins. I. Basic principles and illustrative examples. Polypropylene. Chemical Engineering Science 51: 4859.

46 Gorbach, A.B., Naik, S.D., and Ray, W.H. (2000). Dynamics and stability analysis of solid catalyzed gas-phase polymerization of olefins in continuous stirred bed reactors. Chemical Engineering Science 55: 4461.

47 Dittrich, C.J. and Mutsers, S.M.P. (2007). On the residence time distribution in reactors with non-uniform velocity profiles: the horizontal stirred bed reactor for polypropylene production. Chemical Engineering Science 62: 5777.

---

<!-- PDF page 312 -->

48 Moore, E.P. (1996). Polypropylene (commercial). In: Polymeric Materials Encyclopedia (ed. J.C. Salamone), 6578. Boca Raton, FL: CRC Press.

49 Balow, M.J. (1999). Growth of polypropylene usage as a cost-effective replacement of engineering polymers. In: Handbook of Polypropylene and Polypropylene Composites (ed. H.G. Karian), 1. New York: Marcel Dekker.

50 Gross, J. and Sadowski, G. (2004). Perturbed-Chain-SAFT: development of a new equation of state for simple, associating, multipolar and polymeric compounds. In: Supercritical Fluids as Solvents and Reaction Media (ed. G. Brunner), 295–322. Elsevier, B.V., Amsterdam.

51 Gross, J. and Sadowski, G. (2002). Application of perturbed-chain SAFT equation of state to associating systems. Industrial and Engineering Chemistry Research 41: 5510.

52 Gross, J. and Sadowski, G. (2002). Application of the perturbed-chain SAFT equation of state to associating systems. Industrial and Engineering Chemistry Research 41: 5510.

53 Kissin, Y.V. (2003). Multicenter nature of titanium-based Ziegler–Natta catalysts: comparison of ethylene and propylene polymerization reactions. Journal of Polymer Science Part A: Polymer Chemistry 41: 1745.

54 Wang, W.Q. (2008). Research on modeling and simulation for industrial polymerization process. MS thesis. Hangzhou, China: System Engineering, Zhejiang University.

55 Kouzai, I. and Fukuda, K. (2009). Modeling study on effects of liquid propylene in horizontally stirred gas-phase reactors for polypropylene. Macromolecular Symposia 285: 23.

56 Jenkins, J.M. III, Jones, R.L., and Jones, T.L. (1985). Fluidized bed reaction systems. US Patent 4588790.

57 Jenkins, J.M. III, Jones, R.L., Jones, T.L., and Beret, S. (1986). Method for fluidized bed polymerization. US Patent 4543399A.

58 McKenna, T.F.L. (2019). Condensed mode cooling of ethylene polymerization in fluidized bed reactors. Macromolecular Reaction Engineering 13: 1800026.

59 Rainho, P., Alizadeh, A., Ribeiro, M.R., and McKenna, T.L.F. (2014). Pseudo-homogeneous CSTR simulation of a fluidized-bed reactor operating in condensed-mode including Sanchez-Lacombe n-hexane co-solubility effect. Journal of Engineering for Rookies 1: 56. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1075.9872&rep=rep1&type=pdf.

60 Boks, C.P., Ramanathan, S., Franjone, J. et al. (2002). Physical properties, reactor modeling, and polymerization kinetics in the low-density polyethylene tubular reactor process. Industrial and Engineering Chemistry Research 41: 1017.

61 Gao, T. and Zhao, Y.I. (2008). Application of Aspen Plus process simulation software in LLDPE plant. Qilu Petrochemical Technology 36 (1): 35.

62 Cesca, S. (1975). The chemistry of unsaturated ethylene-propylene-based terpolymers. Journal of Polymer Science: Macromolecular Reviews 10: 1.

63 Van Duin, M., Van der Aar, I.N., and Van Dornemaele, G. (2017). Historical and technical summary of Keltan developments defining EPDM for the past and the

---

<!-- PDF page 313 -->

next 50 years. https://www.kgk-rubberpoint.de/en/21389/defining-epdm-for-the-past-and-the-next-50-years (accessed 29 June 2021).

64 Eisinger, R.F., Lee, K.H., Hussein, F.D., and Zilker, D.P. Jr., (2000). Process for conditioning a gas-phase reactor to produce an ethylene-propylene or ethylene-propylene-diane-rubber. US Patent No. 6,011,128.

65 Cozewith, C. (1988). Transient response of continuous-flow stirred-tank polymerization reactors. AIChE Journal 34: 272.

66 Ver Strate, G., Cozewith, C., and Ju, S. (1988). Near monodisperse ethylene-propylene copolymers by direct Ziegler-Natta polymerization. Preparation, characterization, properties. Macromolecules 21: 3360.

67 Ogunnaike, B.A. (1994). On-line modelling and predictive control of an industrial terpolymerization process. International Journal of Control 59: 711.

68 Meziou, A.M. (1993). Optimization and advanced control of an industrial polymerization process. H.D. dissertation. Louisville, KY: University of Louisville.

69 Meziou, A.M., Deshpande, P.B., Cozewith, C. et al. (1996). Dynamic matrix control of an ethylene-propylene-diane polymerization process. Industrial and Engineering Chemistry Research 35: 164.

70 Hagg, M.C., Henrique, J., Dantos, J.H.Z.D. et al. (1998). Dynamic simulation and experimental evaluation of EPDM terpolymerization with vanadium-based catalyst. Journal of Applied Polymer Science 70: 1173.

71 Pourhossaini, M.R., Vasheghani-Farahani, E., Gholamian, M., and Gholamian, M. (2006). Dynamic simulation and experimental evaluation of olefin copolymerization with vanadium-based catalysts. Journal of Applied Polymer Science 100: 3101.

72 Chen, H.J. (2016). Development of new product grades and industrial implementation of ethylene-propylene rubber (EPDM). MS thesis. Shanghai, China: College of Life and Environmental Sciences, Shanghai Normal University.

73 Xu, C.-Z., Wang, J.-J., Gu, X.-P., and Fang, L.-F. (2018). Modeling of molecular weight and copolymerization composition distributions for ethylene-propylene solution copolymerization. AIChE Journal 65: e1663.

74 Hamielec, A.E. and Soares, J.B.P. (1999). Metallocene catalyzed polymerization: industrial technology. In: Polypropylene. Polymer Science and Technology Series, vol. 2 (ed. J. Karger-Kocsis). Dordrecht: Springer. https://doi.org/10.1007/978-94-011-4421-6_62.

75 Hagg, M.C., Henrique, J., Dantos, J.H.Z.D. et al. (2000). Dynamic simulation and experimental evaluation of EPDM terpolymerization with Et(Ind) $ _{2} $ZrCl $ _{2} $/MAO catalyst system. Journal of Applied Polymer Science 76: 425.

76 Aspen Technology, Inc. (2020). How to model a terminal double bond polymerization in Aspen polymers? Knowledge Article No. 000086916. AspenTech Online Support. https://esupport.aspentech.com/S_Article?id=000086916 (accessed 3 July 2021).

---

<!-- PDF page 314 — MISSING, not yet parsed -->
