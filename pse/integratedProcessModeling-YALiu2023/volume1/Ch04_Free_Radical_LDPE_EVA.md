# 4. Free Radical Polymerizations: LDPE and EVA

<!-- PDF page 163 -->

## Free Radical Polymerizations: LDPE and EVA

This chapter covers the modeling of manufacturing processes for high-pressure low-density polyethylene (LDPE) and poly(ethylene-vinyl acetate) (EVA) copolymers, using free radical polymerization with stirred autoclave and tubular reactors.

We cover conceptual development, modeling methodology, illustrative examples, and hands-on workshops. Section 4.1 introduces polymers through free radical polymerization. Section 4.2 covers the kinetics of free radical polymerization and copolymerization. Section 4.3 explains the selection of appropriate thermodynamic methods and estimation of essential property parameters for simulating polyolefin processes produced by free radical polymerization. Section 4.4 presents a hands-on workshop for simulating an autoclave high-pressure (HP) LDPE process. We present an effective methodology for estimating the kinetic parameters based on plant data in the development of simulation and optimization models for commercial polyolefin processes involving free radical polymerization. Section 4.5 is another hands-on workshop for simulating tubular reactors for a high-pressure LDPE process. Section 4.6 presents a hands-on workshop for simulating an autoclave EVA copolymerization process. A reference section is also included in the chapter.

### 4.1 Polymers by Free Radical Polymerization

Approximately 40% of commercial polymers are made by free radical polymerization with monomers generally in the liquid phase. Typical monomers are of the form XHC=CH₂ or XYC=CH₂. Table 4.1 gives some examples of the monomers, repeat units, and polymers formed by free radical polymerization.

### 4.2 Kinetics of Free Radical Polymerization

Figure 4.1 shows a schematic diagram of reactions in free radical polymerization. The key reactions include initiator decomposition, chain initiation, chain propagation, chain transfer, beta scission (spontaneous chain transfer), short-chain branching (intramolecular chain transfer or back backing), chain termination, and

---

<!-- PDF page 164 -->

<div style="text-align: center;">Table 4.1 Selected examples of free radical polymerization monomers, repeat units, and polymers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Monomer name</td><td style='text-align: center; word-wrap: break-word;'>Monomer formula</td><td style='text-align: center; word-wrap: break-word;'>Repeat unit</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ethylene</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2}C=CH_{2} $</td><td style='text-align: center; word-wrap: break-word;'>$ -\mathrm{CH}_{2}-\mathrm{CH}_{2}- $</td><td style='text-align: center; word-wrap: break-word;'>Polyethylene (PE)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Styrene</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{24}] $</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{3}] $</td><td style='text-align: center; word-wrap: break-word;'>Polystyrene (PS)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Vinyl acetate</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{4}] $</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{5}] $</td><td style='text-align: center; word-wrap: break-word;'>Polyvinyl acetate (PVAC)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ethylene-vinyl acetate (EVA)</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{25}] $</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{6}] $</td><td style='text-align: center; word-wrap: break-word;'>Poly(ethylene-vinyl acetate), or EVA copolymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Styrene and acrylonitrile</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{23}] $</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{7}] $</td><td style='text-align: center; word-wrap: break-word;'>Poly(styrene-co-acrylonitrile), or SAN Copolymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Methyl methacrylate</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{22}] $</td><td style='text-align: center; word-wrap: break-word;'>$ [F_{2}] $</td><td style='text-align: center; word-wrap: break-word;'>Poly(methyl methacrylate) (PMMA)</td></tr></table>

others, as explained in the textbook by Odian [2]. In Aspen Polymers [3], a search of “Reaction Kinetic Scheme (Free-Radical)” in the online help gives a complete listing and explanations of all reactions included in the free radical polymerization model.

#### 4.2.1 Initiator and Its Decomposition-Rate Parameters

Consider the initiator decomposition reaction:  $  \text{INIT} \rightarrow \text{e} \cdot \text{n} \cdot \text{R}^* + \text{aA} + \text{bB}  $, where  $  \text{INIT}  $ represents the initiator, such as  $  t  $-butyl peroxybenzoate (TBPB);  $  e  $ is the initiator efficiency;  $  n  $ is the number of free radicals generated;  $  R^*  $ denotes the free radical;  $  A  $ and  $  B  $ are byproducts, and  $  a  $ and  $  b  $ are the corresponding stoichiometric coefficients. We use TBPB as one of our initiators in Workshop 4.1 for a high-pressure LDPE process. By searching Aspen Polymers in the online help for the entry “initiator decomposition rate parameters,” we can access a large collection of kinetic parameters for commercial initiators in the database, API100.

---

<!-- PDF page 165 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_147_707_677.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 4.1 An illustration of reactions for free radical polymerization. Source: Adapted from Lingard [1].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_157_763_780_1000.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 4.2 Decomposition rate parameters for DTBP.</div>


INITIATO [4]. These initiators include azo-nitriles (both water-soluble and with solvent), diacyl peroxides, peroxycarbonates, alkyl peroxides, hydroperoxides, C–C initiators, and sulfanyl peroxides. For example, Figure 4.2 shows the decomposition rate parameters for DTBP (di-tert-butyl-peroxide), which is an alkyl peroxide.

Figure 4.3 shows a part of the initiator decomposition reaction in the kinetic model of free radical polymerization. Within the list of free radical reactions generated by the model, we highlight the first initiator decomposition reaction and click on “Edit Rate Constants” to access the details of the rate constants. We see the specific

---

<!-- PDF page 166 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_150_765_463.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 4.3 Accessing the database values of initiator decomposition rate parameters.</div>


form of the rate constant  $ k $ for the initiator decomposition reaction, in which  $ k_{\text{ref}} $ is the pre-exponential factor (1/sec or 1/hr),  $ E_a $ is the activation energy (cal/mol or kcal/mol),  $ \Delta V_P $ (cum/kmol or cc/mol) is the activation volume that is important in high-pressure reactions, and  $ T_{\text{ref}}(\degree C) $ is the reference temperature. By clicking on the button "Get Rate Constants," Aspen Polymers will fill in the relevant rate parameter values from the database API100 INITIATO. Note that the database assumes an initiator efficiency of 1, for which we should change to 0.8 or less in our workshop based on industrial experience. In Figure 4.3, we use an efficiency of 0.4.

#### 4.2.2 Chain Initiation Reactions

We consider three types of initiation reactions.

(1) Chain initiation (PI):

Monomer  $ M_j $ + Radical  $ R^* \rightarrow $ Growing monomer  $ P1_j $

 $$ j=1,2,\ldots,J(number of monomers) $$ 

We use brackets [] to present the species concentration, and write the reaction rate as:  $ R_{\mathrm{PL},j} = k_{\mathrm{PL},j}[M_{j}][R^*] $.

(2) Catalyzed initiation (CI):

 $$  Initiator INIT_{i}+Catalyst CAT_{k}\rightarrow e\cdot n\cdot R^{*}+CAT_{k}+aA+bB $$ 

where $i=1,2,\ldots,I$ (number of initiators); $k=1,2,\ldots,K$ (number of catalysts); A and B are products; and a and b are the corresponding stoichiometric coefficients.

The reaction rate of catalyzed initiation is  $ R_{\mathrm{Cl},k} = k_{\mathrm{Cl},k}[\mathrm{INIT}_{i}][\mathrm{CAT}_{k}] $.

(3) Special initiation (SI):

 $$ \mathrm{Monomer M_{j}+Coinitiator C_{i}\rightarrow\ Growing monomer P1_{j}+aA+bB} $$ 

---

<!-- PDF page 167 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_146_700_260.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 4.4 An illustration of chain propagation reaction.</div>


The reaction rate of special initiation is  $ R_{\mathrm{SL},j} = k_{\mathrm{SL},j} \left[ C_i \right]^{aj} \left[ M_j \right]^{bj} (h\nu)^{cj} $.

where  $ h $ is Planck's constant,  $ 6.626186 $ E-34 J s;  $ \nu $ is the electromagnetic frequency, number of cycles per second (hertz, Hz). Depending on the values of the three exponents, this rate expression represents three cases: (i) thermal initiation, aj = 0, cj = 0; see an example of thermal initiation in the bulk solution polymerization of styrene [5]; (ii) radiation initiation, aj = 0; (iii) coinitiator initiation, cj = 0.

#### 4.2.3 Chain Propagation Reactions

Growing polymer chain  $ \mathrm{Pn}(\mathrm{M}_{j}) + \mathrm{Monomer}\mathrm{M}_{j} $

→ Propagating polymer chain Pn + 1(Mj)

where  $ \mathrm{Pn}(M_j) $ is a growing polymer chain of length  $ n $ having an active monomer  $ M_j $ segment. The rate of propagation reaction is  $ \mathrm{RP}_j = \mathrm{kP}_j $  $ [M_j][\mathrm{Pn}] $. For polystyrene, we illustrate this reaction in Figure 4.4 [6]:

For copolymerization processes, such as the production of ethylene and vinyl acetate (EVA) copolymers, we need to consider the concept of monomer reactivity ratio. Let us consider the propagation reactions for monomers  $ M_1 $ and  $ M_2 $ [7]:

 $$ \mathbf{M}_{1}+\mathbf{M}_{1}\rightarrow\mathbf{M}_{1}\mathbf{M}_{1}\qquad\qquad reaction rate constant:k_{p11} $$ 

 $$ \mathbf{M}_{1}+\mathbf{M}_{2}\rightarrow\mathbf{M}_{1}\mathbf{M}_{2}\qquad\quad reaction rate constant:k_{p12} $$ 

 $$ \mathbf{M}_{2}+\mathbf{M}_{1}\rightarrow\mathbf{M}_{2}\mathbf{M}_{1}\qquad\qquad reaction rate constant:k_{p21} $$ 

 $$ \mathbf{M}_{2}+\mathbf{M}_{2}\rightarrow\mathbf{M}_{2}\mathbf{M}_{2}\qquad\qquad reaction rate constant:k_{p22} $$ 

where  $ M_{1} $ represents a radical of monomer  $ M_{1} $. We define the reactivity ratios as follows:

 $$ r_{1}=k_{p11}/k_{p12}\quad r_{2}=k_{p22}/k_{p21} $$ 

We write the rates of reaction of monomers and radicals as follows:

 $$ \begin{aligned}&-\mathbf{d}[\mathbf{M1}]/\mathbf{d}t=k_{p11}\left[\mathbf{M}_{1}\cdot\right]\left[\mathbf{M}_{1}\right]+k_{p21}\left[\mathbf{M}_{2}\cdot\right]\left[\mathbf{M}_{1}\right]\\&-\mathbf{d}[\mathbf{M2}]/\mathbf{d}t=k_{p22}\left[\mathbf{M}_{2}\cdot\right]\left[\mathbf{M}_{2}\right]+k_{p12}\left[\mathbf{M}_{1}\cdot\right]\left[\mathbf{M}_{2}\right]\\&\mathbf{d}[\mathbf{M1}\cdot]\mathbf{d}t=k_{p21}\left[\mathbf{M}_{2}\cdot\right]\left[\mathbf{M}_{1}\right]-k_{p12}\left[\mathbf{M}_{1}\cdot\right]\left[\mathbf{M}_{2}\right]\\&\mathbf{d}[\mathbf{M2}\cdot]\mathbf{d}t=k_{p12}\left[\mathbf{M}_{1}\cdot\right]\left[\mathbf{M}_{2}\right]-\mathbf{k}_{p21}\left[\mathbf{M}_{2}\cdot\right]\left[\mathbf{M}_{1}\right]\\ \end{aligned} $$ 

---

<!-- PDF page 168 -->

<div style="text-align: center;">Table 4.2 Reported reactivity ratios for EVA (ethylene-vinyl acetate) copolymerization at high pressures.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reactivity ratio  $ r_{1} = k_{p11}/k_{p12} $</td><td style='text-align: center; word-wrap: break-word;'>Reactivity ratio  $ r_{2} = k_{p22}/k_{p21} $</td><td style='text-align: center; word-wrap: break-word;'>Operating temperature (°C)</td><td colspan="2">Operating pressure (atm)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>1200</td><td style='text-align: center; word-wrap: break-word;'>1240</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>210</td><td style='text-align: center; word-wrap: break-word;'>1200</td><td style='text-align: center; word-wrap: break-word;'>1240</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>220-240</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>2066</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>220-240</td><td style='text-align: center; word-wrap: break-word;'>2400</td><td style='text-align: center; word-wrap: break-word;'>2480</td></tr></table>

Taking the ratio of the first two equations gives

 $$ \begin{aligned}\mathrm{d}[\mathrm{M1}]/\mathrm{d}[\mathrm{M2}]=&([\mathrm{M1}]/[\mathrm{M2}])\left\{k_{p11}\left[\mathrm{M}_{1}\cdot\right]/\left[\mathrm{M}_{2}\cdot\right]+k_{p21}\right\}/\\&\left\{k_{p22}+k_{p12}\left[\mathrm{M}_{1}\cdot\right]/\left[\mathrm{M}_{2}\cdot\right]\right\}\end{aligned} $$ 

Assuming a pseudo steady-state for the radicals with d[M1·]/dt = d[M2·]/dt = 0 and introducing the reactivity ratios give

 $$ \mathrm{d}[\mathrm{M1}]/\mathrm{d}[\mathrm{M2}]=([\mathrm{M1}]/[\mathrm{M2}])\left\{r_{1}\left[\mathrm{M}_{1}\right]+\left[\mathrm{M}_{2}\right]\right\}/\left\{\left[\mathrm{M}_{1}\right]+r_{2}\left[\mathrm{M}_{2}\right]\right\} $$ 

We see from the right-hand side of the equation that the concentration ratio of the monomers in the feed,  $ [M1]/[M2] $, and the reactivity ratios  $ r_1 $ and  $ r_2 $, are affecting the rate of changes of monomers in the propagation reactions. As an example, Table 4.2 shows the experimental reactivity ratios of ethylene in the radically induced polymerization with vinyl acetate at high pressures reported by Ratzsch et al. [8].

We apply this experimental observation in our workshop WS4.3 for EVA copolymerization.

#### 4.2.4 Chain Transfer Reactions

We consider four types of chain transfer reactions, together with the spontaneous chain transfer reaction (beta scission) and intramolecular chain transfer (short-chain branching) reaction.

(1) Chain transfer to monomer:

 $$ \begin{aligned}Growing polymer chain\mathrm{Pn}\left(\mathrm{M}_{j}\right)&+Monomer\mathrm{M}_{j}\rightarrow Dead chain\mathrm{Dn}\left(\mathrm{M}_{j}\right)\\&+Growing monomer\mathrm{R}^{*}\end{aligned} $$ 

The reaction rate of chain transfer to monomer is  $ R_{\mathrm{trm},j} = k_{\mathrm{trm},j} \left[ \mathrm{Pn} \right] \left[ \mathrm{M}_{j} \right] $.

In this reaction, the live polymer chain (Pn) attracts a hydrogen from a monomer molecule, resulting in a dead polymer chain (Dn). The monomer, which loses a hydrogen, becomes a live polymer end group (i.e. a growing monomer) with an unreacted double bond (P1=) and a free radical attaching to it. For polystyrene that we cover in Chapter 6, we illustrate the chain transfer

---

<!-- PDF page 169 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_146_778_260.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.5 An illustration of chain transfer to monomer.</div>


to monomer below (the black dot represents a free radical attaching to the growing monomer) in Figure 4.5 [6]:

(2) Chain transfer to agent:

 $$ \begin{aligned}Growing polymer chain\mathrm{Pn}\left(\mathrm{M}_{j}\right)+Transfer agent\mathrm{A}_{k}&\rightarrow Dead chain\mathrm{Dn}\left(\mathrm{M}_{j}\right)\\&+Growing monomer\mathrm{R}^{*}\end{aligned} $$ 

The reaction rate of chain transfer to monomer is  $ R_{\text{tra},k} = k_{\text{tra},k} \left[ \text{Pn} \right] \left[ \text{A}_k \right] $. where  $ k = 1, 2, \ldots, K $ (number of chain transfer agents (CTAs)).

(3) Chain transfer to solvent:

Growing polymer chain  $ \mathrm{Pn}\left(\mathrm{M}_{j}\right) + \mathrm{Solvent}\mathrm{S}_{k} \rightarrow \mathrm{Dead}\mathrm{chain}\mathrm{Dn}\left(\mathrm{M}_{j}\right) + \mathrm{Growing}\mathrm{monomer}\mathrm{R}^{*} $

The reaction rate of chain transfer to solvent is  $ R_{\mathrm{trs},k} = k_{\mathrm{trs},k} \left[ \mathrm{Pn} \right] \left[ \mathrm{S}_{\mathrm{k}} \right] $.

where  $ k = 1, 2, \ldots, K $ (number of solvents).

(4) Chain transfer to polymer:

 $$ \mathrm{Growing~polymer~chain~Pn}\left(\mathrm{M}_{j}\right)+\mathrm{Dead~polymer~chain~Dm}\left(\mathrm{M}_{j}\right) $$ 

 $$ \rightarrow Dead polymer chain Dn\left(M_{j}\right)+Growing polymer chain Pm\left(M_{j}\right) $$ 

The reaction rate of chain transfer to polymer is  $ R_{\mathrm{trp},i} = k_{\mathrm{trp},i} \left[ \mathrm{Pn} \right] \left[ \mathrm{Dm} \right] $.

(5) Spontaneous chain transfer or beta-scission reaction:

Growing polymer chain  $ \mathrm{Pn}\left(\mathrm{M}_{j}\right)\rightarrow\mathrm{Dead}\ \mathrm{chain}\ \mathrm{Dn}\left(\mathrm{M}_{j}\right)+\mathrm{Growing}\ \mathrm{monomer}\ \mathrm{R}^{*} $

The reaction rate of beta scission is  $ R_{\mathrm{bsc},j} = k_{\mathrm{bsc},j}[\mathrm{Pn}] $.

(6) Intramolecular chain transfer, backbiting, or short-chain branching reaction

Growing polymer chain with free radical attached to segment j,  $ \mathrm{Pn}(\mathrm{M}_{j}) \rightarrow $

Growing polymer with free radical attached to segment i,  $ \mathrm{Pn}(\mathrm{M}_{i}) $. The reaction rate of short-chain branching is  $ R_{\mathrm{scb},j} = k_{\mathrm{scb},j} \left[ \mathrm{Pn}(\mathrm{M}_{j}) \right] $.

#### 4.2.5 Termination Reactions

(1) Termination by combination:

Growing polymer chain,  $ \mathrm{Pm}\left(\mathrm{M}_{j}\right) + \mathrm{Growing} $ polymer chain  $ \mathrm{Pn}\left(\mathrm{M}_{j}\right) $

→ Dead polymer chain D(m+n)

---

<!-- PDF page 170 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_147_807_294.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.6 An illustration of termination by combination.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_381_809_480.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.7 An illustration of termination by disproportionate.</div>


The reaction rate of termination by combination is  $ R_{tc,j} = k_{tc,j} $ [Pn][Pm]. For polystyrene, we illustrate this reaction in Figure 4.6 [6]:

(2) Termination by disproportionate:

 $$ \mathrm{Growing~polymer~chain,Pm\left(M_{j}\right)+Growing~polymer~chain~Pn\left(M_{j}\right)} $$ 

 $$ \rightarrow Dead polymer chain Dm+Dead polymer chain Dn $$ 

The reaction rate of termination by disproportionation is  $ R_{\mathrm{tp},j} = k_{\mathrm{tp},j} \left[ \mathrm{Pn} \right] \left[ \mathrm{Pm} \right] $. For polystyrene, we illustrate this reaction in Figure 4.7[6]:

#### 4.2.6 Autoacceleration, Trommsdorff Effect, or Gel Effect

At high polymer concentrations or high conversion, termination reactions between chain radicals become diffusion-controlled, resulting in an initial increase in the polymerization rate and molecular weight. This condition is known as autoacceleration, Trommsdorff effect, or gel effect [2]. At high polymer concentrations, the increased viscosity of the reaction medium imposes a diffusional limitation on the polymer chains, which leads to lower effective termination rates. Typically, the termination reaction constants are affected first by the gel effect because they involve diffusion of two bulky polymer radicals. Eventually, at sufficiently high conversions, even the propagation, initiation, and chain transfer reactions and the initiator efficiency are lowered by the gel effect. Hence, in general, it may be necessary to consider gel effect for all the polymerization reactions [3].

The diffusional limitation is usually modeled by an effective reaction rate constant,  $ k_{\text{eff}} $, obtained by multiplying the low-conversion reaction rate constant, k, by a correction factor for gel effect, GF, that decreases with increasing conversion. Hence, the effective reaction rate constant for a reaction is given by:  $ k_{\text{eff}} = k^* \text{GF} $.

---

<!-- PDF page 171 -->

The correction factor could be experimentally correlated with the monomer conversion [5]. We will demonstrate this correction in Workshop 6.1 for polystyrene.

#### 4.2.7 Other Free Radical Polymerization Reactions

The Aspen Polymers model includes several other reactions: (1) head-to-head propagation (cis- and trans-propagations); (2) inhibition; (3) terminal double-bond polymerization; (4) pendent double-bond polymerization; (5) bifunctional initiator decomposition and initiation; and (6) secondary initiator decomposition and initiation. A search of Aspen Polymers in the online help for the entry "Reaction Kinetic Scheme (Free-Radical)" gives the description of these reactions.

### 4.3 Thermodynamic Methods and Property Parameter Requirements

Table 4.3 summarizes several important commercial processes by free radical polymerization, the recommended thermodynamic methods for their process modeling and references for the method details, together with examples of process modeling applications.

<div style="text-align: center;">Table 4.3 Selected polymers, thermodynamic methods, method references, and simulation examples.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>Thermodynamic method</td><td style='text-align: center; word-wrap: break-word;'>Method references</td><td style='text-align: center; word-wrap: break-word;'>Simulation examples</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Low-density polyethylene (LDPE)</td><td style='text-align: center; word-wrap: break-word;'>POLYSL (polymer Sanchez-Lacombe) equation of state</td><td style='text-align: center; word-wrap: break-word;'>Section 2.6, [9-11]</td><td style='text-align: center; word-wrap: break-word;'>[12], Workshop 4.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LDPE</td><td style='text-align: center; word-wrap: break-word;'>POLYPCSF (polymer perturbed-chain statistical fluid theory) equation of state</td><td style='text-align: center; word-wrap: break-word;'>Section 2.8, [11, 13-16]</td><td style='text-align: center; word-wrap: break-word;'>[17-21], Workshop 4.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Poly(ethylene-vinyl acetate) (EVA copolymer)</td><td style='text-align: center; word-wrap: break-word;'>POLYPCSF</td><td style='text-align: center; word-wrap: break-word;'>Section 2.8, [11, 13-16, 22]</td><td style='text-align: center; word-wrap: break-word;'>[9, 23-30], Workshop 2.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polystyrene (PS)</td><td style='text-align: center; word-wrap: break-word;'>POLYNRTL (polymer nonrandom two-liquid) activity coefficient model</td><td style='text-align: center; word-wrap: break-word;'>Section 2.2, [10, 11]</td><td style='text-align: center; word-wrap: break-word;'>[31], Workshop 6.1</td></tr></table>

---

<!-- PDF page 172 -->

#### 4.4 Workshop 4.1: Simulation of an Autoclave High-pressure LDPE Process

#### 4.4.1 Objectives

We wish to develop a simulation model of a commercial autoclave high-pressure LDPE process and validate the model with plant data on production rate, MWN, and MWW. We then use the validated model to do sensitivity analysis to quantify the effects of key independent variables on the polymer production rate and quality targets.

#### 4.4.2 Process Flowsheet and Simulation Representation

Figure 4.8 shows a block flow diagram of a typical autoclave high-pressure LDPE process. The complete process consists of compression, polymerization, separation, pelleting, air conveying, mixing, processing, and packaging steps.

In Figure 4.8, the unreacted low-pressure recycle ethylene leaving the low-pressure separator D-10 enters compressor C-1, which consists of a low-pressure section (stages 1–3) and a high-pressure section (stages 4–6). The stream leaving the low-pressure section is combined with fresh ethylene from the ethylene process in vessel D-7, and the mixed feed is further compressed in the high-pressure section. The stream leaving compressor C-1 is combined with the unreacted high-pressure recycle ethylene from the high-pressure separator V-2 in mixer V-1, followed by compression train, C21 and C22. In the figure, we see a series of exchangers before each reactor and after the high-pressure and low-pressure separators. We draw the simulation flowsheet in three sections: (1) compression section; (2) reactor section; and (3) separation section.

Figures 4.9 shows the compression section.

For the reactor section, Figure 4.10 shows a schematic diagram of two autoclave reactors in series in the LDPE process, with ethylene monomer and initiator

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_899_808_1153.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.8 A block diagram of an autoclave high-pressure LDPE process with block numbers.</div>


---

<!-- PDF page 173 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_150_780_284.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.9 The compression section.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_346_747_568.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 4.10 A schematic diagram of two autoclave reactors in series.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_635_783_893.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.11 The reactor section.</div>


being fed at multiple locations throughout both reactors. Reference [19] shows a similar diagram.

Based on Figures 4.8 and 4.10, we develop a simulation flowsheet for the reactor section. See Figure 4.11, in which continuous stirred tank reactors R3A1 to R3A3 simulate the three sections of the actual reactor R-3A, while R3B1 to R3B2 simulate the two sections of the actual reactor R-3B.

After drawing both sections 1 and 2, we save the simulation as WS 4.1 LDPE BaseCase_Secs 1-2.bkp. Figure 4.12 shows the separation section. We save the simulation file with all three sections as WS 4.1 LDPE BaseCase_Secs 1-2-3.bkp. See Figure 4.12.

---

<!-- PDF page 174 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_148_810_378.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.12 The separation section.</div>


#### 4.4.3 Unit System, Components, and Characterization of Polymer

We define a unit system, METCKGCM, by copying most units from MET system, except to replace temperature unit by °C and pressure unit by kg/sqcm. See Figure 4.13.

Figure 4.14 shows the enterprise databases used in the simulation of free radical polymerization processes, and Figure 4.15 specifies the components for the LDPE process.

C2H4 and C2H4-R are ethylene monomer and ethylene segment (repeat type). LDPE is the polymer product. Figure 4.16 shows the definition of ethylene segment, E2-SEG or C2H4-R, and Figure 4.17 displays polymer attributes in the free radical polymerization and the attribute selection.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_774_810_922.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.13 Defining a unit system METKGCM by copying most units from MET system.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1001_559_1222.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Figure 4.14 Selection of enterprise databases.</div>


---

<!-- PDF page 175 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_148_779_348.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.15 Component specifications.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_413_521_647.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">Figure 4.16 Definition of C2H4-R segment.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_712_780_927.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.17 Free radical polymer-attribute selection.</div>


INIT1 is our first initiator, t-butyl peroxybenzoate, called TBPB within Aspen Polymers initiator databank, APV100 INITIATO (Figure 4.14), with a molecular weight of 194.23 g/mol. INIT2 is 3,5,5-trimethylhexanoyl peroxide with a chemical formula of C18H34O4, a molecular weight of 314.466 g/mol, and a CAS number of 3851-87-4. It is not available within the Aspen Polymers initiator databank. To define INIT2, we search for the component on the website of Chemical Book (www.chemicalbook.com). We can Google for the entry "Chemical Book, 3,5,5-trimethylhexanoyl peroxide," and see the structure in the first entry, as shown in Figure 4.18. We can download and save the molecular structure file, 3851-87-4.mol, and import it into Aspen Polymers by following the path: Properties → Components → Molecular Structure → INIT2 → Structure

---

<!-- PDF page 176 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_135_818_455.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Figure 4.18 Search for the structure of 3,5,5-trimethylhexanoyl peroxide within Chemical Book.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_551_809_758.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.19a Molecular structure of INIT2 obtained by importing its MOL file from the Internet.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_860_744_1030.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 4.19b The INIT2 molecular structure and the "Calculate Bonds" button.</div>


(Graphical Structure)→Draw/Import/Edit→Molecule Editor→Import Mol File→3851-87-4.mol→Structure shown in Figure 4.19a.

Next, we see the “Calculate Bonds” button, as displayed in Figure 4.19b.

After clicking on the “Calculate Bonds” button, Aspen Polymers automatically completes the “General” structure folder. Figure 4.19c shows the general structure, which we will use below in the estimation of property parameters.

---

<!-- PDF page 177 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_691_415.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 4.19c The molecular structure automatically defined by Aspen Polymers based on the chemical structure of Figure 9.19b.</div>


#### 4.4.4 Thermodynamic Methods and Property Parameters for Components, Segment, and Polymer

We choose the polymer Sanchez-Lacombe (POLYSL) equation of state (see Section 2.6) for the LDPE process simulation, following an online LDPE simulation example available within Aspen Polymers [12], which also provides some essential property parameter values. We note that several references (i.e. [14–16]) demonstrate the use of the perturbed-chain statistical association fluid theory (PC-SAFT) equation of state (see Section 2.8) for the LDPE process simulation, which we will illustrate in the next workshop.

Based on Ref. [12] and a search of Aspen Polymers help on “Sanchez-Lacombe unary parameters,” we input the pure-component and segment parameters: Properties → Methods → Parameters → Pure Components → New → Scalar → Change name from Pure-1 to POLYSL → Enter values as in Figure 4.20.

We enter the ideal-gas heat capacity parameters for ethylene and ethylene segments in Figure 4.21 based on Ref. [15] by following the path: Properties →

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_901_779_1063.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.20 POLYSL pure-component and segment parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_1124_779_1228.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.21 Ideal-gas heat capacity parameters.</div>


---

<!-- PDF page 178 -->

Methods → Parameters → Pure Components → New → T-dependent correlation → Ideal-gas heat capacity → CPlG-1.

#### 4.4.5 PCES (Physical Constant Estimation System) for Estimating Missing-Property Parameters

We estimate all the missing-property parameters based on molecular structures. See Figure 4.22.

We then run property estimation and save the estimated parameter values before moving on to the simulation step. Figure 4.23 illustrates the estimated property values.

#### 4.4.6 Defining Free Radical Polymerization Reactions for LDPE

References  $ [15, 18] $ have described in detail the relevant free radical polymerization reactions for the high-pressure LDPE process. Table 4.4 summarizes the free radical polymerization reactions for the current workshop.

To generate these reactions within Aspen Polymers, follow the path: Reactions → New: R-1 FREE-RAD type → OK. See Figures 4.24a and 4.24b. Based on the species defined in Figure 4.24a, we click on the “generate reactions” button displayed in Figure 4.24b. Aspen Polymers automatically generates the 11 reactions in Figure 4.24b. For the reaction rate constants in Figure 4.24c, we use the

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_707_809_862.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.22 Estimation of all missing-property parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_926_809_1222.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.23 An illustration of estimated property values.</div>


---

<!-- PDF page 179 -->

<div style="text-align: center;">Table 4.4 Free radical polymerizations for high-pressure LDPE process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Representation</td><td style='text-align: center; word-wrap: break-word;'>Notes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Initiator 1 decomposition</td><td style='text-align: center; word-wrap: break-word;'>Initiator 1 → RadicalsINIT1 → ∈ n R* + aA + bB(no byproducts A and B for this initiator)</td><td style='text-align: center; word-wrap: break-word;'>E is the decomposition efficiency, typically assumed to be 0.8. Our INIT1 or TBDP (t-Butyl peroxybenzoate) generates two radicals (n = 2).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Initiator 2 decomposition</td><td style='text-align: center; word-wrap: break-word;'>Initiator 2 → RadicalsINIT2 → ∈ n R* + aA + bB(no byproducts A and B for this initiator)</td><td style='text-align: center; word-wrap: break-word;'>Our INIT2 or 3,5,5-trimethylhexanoyl peroxide generates two radicals (n = 2).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Chain initiation</td><td style='text-align: center; word-wrap: break-word;'>Monomer + Radical → Growing monomer E2 + R* → P1[E2]</td><td style='text-align: center; word-wrap: break-word;'>E2 = C2H4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. Chain propagation</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer → Propagating polymer chainPn[E2] + E2 → Pn + 1[E2]</td><td style='text-align: center; word-wrap: break-word;'>Pn[E2] is a growing polymer chain of length n having an active C2H4-R or E2-R segment.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. Chain transfer to monomer</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Monomer → Dead chain + Growing monomerPn[E2] + E2 → Dn + R *</td><td style='text-align: center; word-wrap: break-word;'>Dn is a dead polymer chain of n segments that does not have an attached radical.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6. Chain transfer to agent</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Transfer agent → Dead chain + Growing polymerPn[E2] + A → Dn + R*</td><td style='text-align: center; word-wrap: break-word;'>A represents the chain transfer agent.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7. Chain transfer to polymer</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain + Dead chain → Dead chain + Growing polymer chain Pn[E2] + Dm → Dn + Pm + 1[E2]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8. Beta scission (spontaneous chain transfer)</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain → Dead chain + Growing monomerPn[E2] → Dn + R*</td><td style='text-align: center; word-wrap: break-word;'>A growing polymer chain Pn[E2] breaks into a dead chain Dn and a primary radical R*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9. Short-chain branching (back biting or intramolecular chain transfer)</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer with free radical attached to segment I → Growing polymer with free radical attached to segment jPn[E2] → Pm[E2]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10. Chain termination by combination</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain Pm + Growing polymer chain Pn → Dead polymer chain Dm + nPn[E2] + Pm[E2] → Dm + n</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11. Termination by disproportionate</td><td style='text-align: center; word-wrap: break-word;'>Growing polymer chain Pm + Growing polymer chain Pn → Dead polymer chainDn + Dead polymer chain DmPm[E2] + Pn[E2] → Dn + Dm</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<!-- PDF page 180 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_148_810_494.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.24a Create the free radical polymerization reaction set for LDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_561_809_820.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.24b Eleven free radical reactions for LDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_885_809_1053.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.24c Initial values of kinetic parameters for LDPE process</div>


pre-exponential factor and activation energy for the reaction rate constant from Ref. [12] as our initial values.

We pause to explain how to obtain the decomposition reaction rate parameters for initiators INIT1 and INIT2 from the Aspen Polymers initiator database [4], as this will be useful to the reader when using different initiators. Specifically, we follow the path: Reactions → Highlight reaction 1) Init-Dec, Initi → Edit Rate Constants → Rate

---

<!-- PDF page 181 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_146_714_404.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 4.25a Assessing the “rate constant parameters” screen.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_481_736_683.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 4.25b Retrieved initiator decomposition reaction rate parameters.</div>


Constant Parameters (see Figure 4.25a); change the units for pre-exponential factor  $ k_{ref} $, activation energy  $ E_{a} $, and activation volume  $ \Delta VP $ to 1/sec, J/kmol, and cum/kmol, respectively  $ \rightarrow $ Click on “Get Rate Constants”  $ \rightarrow $ See the retrieved constants in Figure 4.25b. Be sure to change the efficiency from a perfect value of 1 to a practical value of 0.8 or less. We use a value of 0.4 in this workshop based on industrial experience. Repeat these steps for initiator INIT2.

#### 4.4.7 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks

Tables 4.5 and 4.6 specify the compression and reactor sections.

We proceed to simulate the compression and reactor sections and fine-tune the reaction kinetic parameters to match the plant data before simulating the separation section.

#### 4.4.8 Methodology for Improving Simulation Convergence and for Kinetic Parameter Estimation

Based on Refs. [15, 18] and our industrial project experience, we propose the methodology for kinetic parameter estimation illustrated in Figure 4.26, which is

---

<!-- PDF page 182 -->

<div style="text-align: center;">Table 4.5 Specifications of the compression section.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>Ethylene flow rate (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>CTA (ethane) flow rate (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D8OUT</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>1.433</td><td style='text-align: center; word-wrap: break-word;'>2,550</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CTA</td><td style='text-align: center; word-wrap: break-word;'>Vapor fraction = 1</td><td style='text-align: center; word-wrap: break-word;'>4.433</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>40</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2-</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>34.033</td><td style='text-align: center; word-wrap: break-word;'>9,220</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RCYC2</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>251.033</td><td style='text-align: center; word-wrap: break-word;'>25,750</td><td style='text-align: center; word-wrap: break-word;'>540</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BLOCK</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>Others</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C11</td><td style='text-align: center; word-wrap: break-word;'>40 (cooler outlet)</td><td style='text-align: center; word-wrap: break-word;'>34.033</td><td style='text-align: center; word-wrap: break-word;'>3 stages, isentropic compression</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C1MIX</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>O (no pressure drop)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C12</td><td style='text-align: center; word-wrap: break-word;'>40 (cooler outlet)</td><td style='text-align: center; word-wrap: break-word;'>O</td><td style='text-align: center; word-wrap: break-word;'>3 stages, isentropic compression</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>V1</td><td style='text-align: center; word-wrap: break-word;'>40 (cooler outlet)</td><td style='text-align: center; word-wrap: break-word;'>O</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C21</td><td style='text-align: center; word-wrap: break-word;'>90 (cooler outlet)</td><td style='text-align: center; word-wrap: break-word;'>1,101.033</td><td style='text-align: center; word-wrap: break-word;'>1 stage, isentropic compression</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C22</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,701.033</td><td style='text-align: center; word-wrap: break-word;'>Isentropic compression</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SEP</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CeH4 in LEAKGAS = 500 kg/hr</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Table 4.6 Specifications of the reactor section.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>INIT1 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>INIT2 (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIR3A1</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1701.033</td><td style='text-align: center; word-wrap: break-word;'>4.018</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIR3A2</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1601.033</td><td style='text-align: center; word-wrap: break-word;'>2.009</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIR3A3</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1601.033</td><td style='text-align: center; word-wrap: break-word;'>4.018</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIR3B1</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1301.033</td><td style='text-align: center; word-wrap: break-word;'>4.571</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIR3B2</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1301.033</td><td style='text-align: center; word-wrap: break-word;'>1.959</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Unit</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>Volume (L)</td><td style='text-align: center; word-wrap: break-word;'>Reaction set</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E13-14A</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>$ -100 $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E13-14B</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>$ -400 $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E13-14C</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>$ -100 $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E13-14D</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>$ -100 $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E13-14E</td><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>$ -100 $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3A1</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1601.033</td><td style='text-align: center; word-wrap: break-word;'>216.67</td><td style='text-align: center; word-wrap: break-word;'>R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3A2</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1601.033</td><td style='text-align: center; word-wrap: break-word;'>216.67</td><td style='text-align: center; word-wrap: break-word;'>R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3A3</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>1601.033</td><td style='text-align: center; word-wrap: break-word;'>216.67</td><td style='text-align: center; word-wrap: break-word;'>R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3AV</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1301.033</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E15A</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>0 (no pressure drop)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3B1</td><td style='text-align: center; word-wrap: break-word;'>240</td><td style='text-align: center; word-wrap: break-word;'>1301.033</td><td style='text-align: center; word-wrap: break-word;'>325</td><td style='text-align: center; word-wrap: break-word;'>R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3B2</td><td style='text-align: center; word-wrap: break-word;'>260</td><td style='text-align: center; word-wrap: break-word;'>1301.033</td><td style='text-align: center; word-wrap: break-word;'>325</td><td style='text-align: center; word-wrap: break-word;'>R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R3BV</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>251.033</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E15B</td><td style='text-align: center; word-wrap: break-word;'>240</td><td style='text-align: center; word-wrap: break-word;'>0 (no pressure drop)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<!-- PDF page 183 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_150_704_663.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 4.26 Methodology for Kinetic Parameter Estimation for LDPE Process.</div>


particularly effective in matching polymer production targets. For polyolefin reactors operating in a small temperature range, we only estimate the pre-exponential factor  $ k_{0} $ and keep the activation energy E constant with values from the literature.

In adjusting the pre-exponential factors, we note the following kinetic relationship for degree of polymerization (DPN) for free radical polymerization [2]:

 $$ 1/MWN\propto1/DPN=k_{tr,m}/k_{p}+\left(k_{tr,A}^{*}CA\right)/\left(k_{p}^{*}Cm\right) $$ 

where the subscripts p, tr,m, and tr,A represent propagation, chain transfer to monomer, and chain transfer to CTA, respectively; CA and Cm represent the concentrations of CTA and monomer, respectively. Eq. (4.1) suggests that: (1) as the pre-exponential factors for chain initiation and chain propagation increase, the production rate or monomer conversion increases; (2) as the pre-exponential factors for chain transfer to monomer, to CTA, or to solvent, and for beta-scission reaction increase, MWN decreases; and (3) as the pre-exponential factor for chain transfer to polymer increases, MWW (or PDI) increases. As we increase or decrease a specific pre-exponential factor, it is important that we do this gradually with a small increment for the change in the pre-exponential factor to correctly approach the simulation targets.

Our goal for simulating the base case is to quantify the kinetic parameters to match the following production targets: (1) LPDE production rate = 8500 kg/hr; (2) MWN = 10,500; and (3) MWW = 191,800.

In simulating both the compression and reactor sections, we may encounter convergence issues for a recycle or tear steam, LEAKGAS in Figure 4.9, and for the

---

<!-- PDF page 184 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_791_318.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.27 Parameter values to improve tear stream convergence.</div>


five reactors in Figure 4.11. To improve the tear stream convergence, a search of “tear stream convergence” in the Aspen Polymers online help gives the following recommendations on convergence parameters: (1) for the Wegstein convergence scheme, increase the maximum number of flowsheet evaluations to 3000, increase the value of “Wait” to 4, increase the consecutive acceleration steps to 20, and increase the upper bound of acceleration parameter to 0.5; or (2) for the Broyden convergence scheme, increase the maximum number of flowsheet evaluations to 3000 and increase the value of “Wait” to 4 (see Figure 4.27).

For mass balance failure in reactor simulation, a search of “RCSTR mass balance convergence failure” on Aspen Polymers in the online help gives the following recommendations (see also Section 3.6.5): (1) use the Broyden convergence scheme, increase the number of iterations to 1000, and decrease the damping factor (0.5, 0.3, 0.1, ..., 0.0001) until the problem converges; or (2) use the Newton convergence scheme with 1000 iterations and “initialize using integration,” and change the stabilization strategy from “Dogleg” to “Line search” (see Figures 4.28a and 4.28b).

#### 4.4.9 Base-Case Simulation Results

Following the methodology of Figure 4.26, we fine-tune the pre-exponential factors of Figure 4.24c. Figure 4.29 shows the resulting kinetic parameters, and Figures 4.30a and 4.30b display that the simulation matches the LDPE production rate and the corresponding MWN and MWW targets. We compare both simulation results and targets in Table 4.7. We save the resulting simulation file as WS4.1_LDPE_BaseCase_GoodProduction_MWN+MWW.bkp.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1004_809_1202.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.28a Parameter values to improve RCSTR mass balance convergence using Broyden scheme.</div>


---

<!-- PDF page 185 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_777_316.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.28b Parameter values to improve RCSTR mass balance convergence using Newton scheme.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_385_778_557.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.29 Estimated kinetic parameters for the base case.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_615_779_881.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.30a Simulated LDPE production rate of 8495.53 kg/hr.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_936_737_1219.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 4.30b Simulated LDPE MWN of 10,864.6 and MWW of 191,899.</div>


---

<!-- PDF page 186 -->

<div style="text-align: center;">Table 4.7 Comparison of simulation results with production targets.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Target</td><td style='text-align: center; word-wrap: break-word;'>Simulation</td><td style='text-align: center; word-wrap: break-word;'>Error (%)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LDPE (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>8,500</td><td style='text-align: center; word-wrap: break-word;'>8,495.63</td><td style='text-align: center; word-wrap: break-word;'>0.05</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'>10,500</td><td style='text-align: center; word-wrap: break-word;'>10,846.6</td><td style='text-align: center; word-wrap: break-word;'>3.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'>191,800</td><td style='text-align: center; word-wrap: break-word;'>191,899</td><td style='text-align: center; word-wrap: break-word;'>0.05</td></tr></table>

#### 4.4.10 Model Applications

We can use the validated base-case model to do sensitivity analyses and design specification studies to identify the operating conditions needed to improve the current process performance. For example, while keeping the same polymer quality targets, MWN and MWW, could we increase the LDPE production rate? After conducting sensitivity analyses for varying different independent variables, we find that varying the temperatures of reactors R3B1 and R3B2 could achieve our goal.

Specifically, R3B1 temperature varies from 240 to 260°C, while R3B2 temperature is 20°C above the R3B1 temperature. We first define a FORTRAN (“Calculator”) block to quantify the relationship between R3B1 and R3B2 temperatures (see Figures 4.31a–4.31c).

By raising the temperature of reactor R3B1 from 240 to 260°C and applying the calculator to set the temperature of reactor R3B2, simulation with the validated kinetic parameters of Figure 4.29 gives the following result: (1) LPDE production rate = 9494.43 kg/hr; (2) MWN = 10,137; and (3) MWW = 198,912. We compare these with the base-case simulation targets: (1) LPDE production rate = 8500 kg/hr; (2) MWN = 10,500; and (3) MWW = 191,800. This comparison suggests that we can increase the LPDE production rate by 1000 kg/hr.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_860_792_984.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.31a Create a FORTRAN ("Calculator") block.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1051_809_1226.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.31b Define the variables for the FORTRAN expression.</div>


---

<!-- PDF page 187 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_148_714_404.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 4.31c FORTRAN equation and calculation sequence.</div>


and obtain an MWN that is close to the target value but with an MWW that is 7112 above the target value. Following our methodology in Figure 4.26, we fine-tune the kinetic parameter for the pre-exponential factor for the chain transfer to polymer from 34,280 to 34,065 and run the simulation again, resulting in no change to the MWN and an exact match of the MWW of 191,800. We save the resulting simulation file as WS4.1_LDPE_BaseCase_Sec 2_R3B up by 20 C.bkp.

#### 4.4.11 Separation Section

We now add the separation section of Figure 4.12 into our simulation flowsheet (see Figure 4.32).

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_773_780_1218.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.32 A complete flowsheet of the compression, reaction, and separation sections.</div>


---

<!-- PDF page 188 -->

<div style="text-align: center;">Table 4.8 Specifications of the separation section.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>C2H4 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>CTA (C2H6) (kg/hr)</td></tr><tr><td colspan="5">SEC3FEED</td></tr><tr><td colspan="3">BYPASS</td><td style='text-align: center; word-wrap: break-word;'>0.0001</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="3">D8MAKEUP</td><td style='text-align: center; word-wrap: break-word;'>0.0001</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BLOCK</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (kg/sqcm)</td><td style='text-align: center; word-wrap: break-word;'>Others</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>V2</td><td colspan="2">251.033</td><td style='text-align: center; word-wrap: break-word;'>Vapor fraction = 0.74</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E16</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>0(no pressure drop)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="3">RECSPLIT</td><td style='text-align: center; word-wrap: break-word;'>SPLITOUT = 500 kg/hr; LEAKOUT = 260 kg/hr</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E8</td><td style='text-align: center; word-wrap: break-word;'>120</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="3">MAKEUPMX</td><td style='text-align: center; word-wrap: break-word;'>C2H4 in HPMAKEUP = 0.0001 kg/hr</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D10</td><td style='text-align: center; word-wrap: break-word;'>150</td><td style='text-align: center; word-wrap: break-word;'>1.433</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_617_810_909.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.33 LDPE product stream going to the extruder, TOEXTRUD.</div>


Table 4.8 shows the specifications of the separation section.

Figure 4.33 shows the simulated result for our LDPE polymer product stream going to the extruder, TOEXTRUD.

We save the resulting simulation file with all three sections as WS4.1_LDPE_BaseCase_Sec 1-2-3.bkp.

#### 4.5 Workshop 4.2: Simulation of Tubular Reactors for HP LDPE Process

#### 4.5.1 Objectives

In addition to the stirred autoclave reactors studied in Workshop 4.1, we wish to simulate tubular reactors for making high-pressure LDPE in the current

---

<!-- PDF page 189 -->

workshop. Both stirred autoclave and tubular reactors are extensively used in LDPE processes [12, 32, 33]. Aspen Polymers has an example of LDPE process with tubular reactors, which uses the POLYSL equation of state (Section 2.6) for thermodynamic method, as in our last workshop. There are several articles [11, 13–16] demonstrating that the POLYPCSF equation of state (Section 2.8) gives more accurate predictions for thermodynamic phase equilibrium and physical properties than the POLYSF method. In this workshop, we use the POLYPCSF thermodynamic method for our simulation. An objective of this workshop is to show how to access and estimate the required property parameters for the POLYPCSF equation of state for the simulation. Additionally, the Aspen Polymers example for the LDPE process does not deal with kinetic parameter estimation to match the simulation targets, and we wish to apply our methodology from Figure 4.26 to the current workshop. Finally, we want to show how to use an external FORTRAN subroutine for heat transfer calculations within Aspen Polymers.

#### 4.5.2 Process Flowsheet and Simulation Representation

Figure 4.34 shows a schematic diagram of a typical high-pressure LDPE process using tubular reactors [34].

Following the Aspen Polymers example [12], we draw our flowsheet in Figure 4.35 to simulate most components of the process in Figure 4.34.

We save the simulation file as WS4.2_LDPE BaseCase.bkp.

#### 4.5.3 Unit System, Components, and Characterization of Polymer

We use METCBAR as our unit system. Figure 4.36 shows the component specifications.

We follow the procedure demonstrated previously in Figure 4.19a–4.19c to characterize the structures of initiators INIT1 and INIT2 for use in estimating the initiator property parameters.

Following Figures 4.16 and 4.17, we define E2-SEG as a repeat segment and choose free radical attributes for polymer LDPE.

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_1034_766_1235.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.34 A schematic diagram of a high-pressure LDPE process using tubular reactors [34].</div>


---

<!-- PDF page 190 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_145_812_445.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.35 Simulation flowsheet of a tubular reactor system for high-pressure LDPE with jacketed cooling, two split feeds, four reaction zones, two initiator injection inlets modeled by four plug-flow reactors in series, and high-pressure and low-pressure separators.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_554_809_722.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.36 Component specifications.</div>


#### 4.5.4 Thermodynamic Method and Property Parameters for Components

We choose polymer perturbed-chain statistical fluid theory (POLYPCSF) equation of state (Section 2.8) as our thermodynamic method. Based on the original references for POLYPCSF [13, 14], the Aspen Polymers LDPE example [12], and a search of Aspen Polymers online help on “Parameters (POLYPCSF),” we input the pure-component parameters by following the path:

Properties → Methods → Parameters → Pure Components → New → Scalar → Change name from Pure-1 to POLYPCSF → Enter values as in Figure 4.37.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1048_695_1222.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 4.37 POLYPCSF pure-component parameters.</div>


---

<!-- PDF page 191 -->

In Figure 4.37, the first three parameters are for pure components or segments. Specifically, PCSFTU is the segment energy parameter (K), PCSFTV is the segment diameter ( $ \mathring{A} $), and PCSFTM is the segment number. The last parameter, PCSFTR, is a ratio parameter that is equal to PCSFTM (m) divided by the molecular weight of the monomer (M) or m/M. This parameter is reserved for polymer. When these parameters are not readily available, Aspen Polymers online help recommends the following default values: (1) PCSFTU = 269.67 K, (2) PCSFTV = 4.072  $ \mathring{A} $, (3) PCSFTM = 0.02434, and (4) PCSFTR = 0.02434*M; M is the molecular weight.

Following the Aspen Polymers LDPE example [12], we enter: (1) the temperature-dependent parameters for the ideal-gas heat capacity (CPIG-1) for E2 and E2-SEG; (2) the scalar van Krevelen glass transition temperature (TGVK) and melt temperature (TGVM), and polymer critical molecular weight (CRITMW) for LDPE; and (3) the scalar standard liquid molar volume (VLSTD) for E2-SEG. See Figure 4.38.

We also enter the temperature-dependent parameters for liquid vapor pressure for initiators to ensure that they do not vaporize and stay in the liquid phase by following the path: Properties → Methods → Parameters → New → T-dependent correlation → Liquid vapor pressure → PLXANT-1 → Enter values as in Figure 4.39. This correlation makes ln(liquid vapor pressure of initiator) = -40 and makes the vapor pressure of the initiators extremely small (4.24 E-23 bar) [35].

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_674_760_975.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 4.38 Pure-component parameters for monomer, segment, and LDPE.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_1047_762_1182.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.39 Setting the first parameter of the T-dependent liquid vapor pressure correlation PLXANT-1 to a large negative number of -40 to ensure that the initiators remain in the liquid phase.</div>


---

<!-- PDF page 192 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_790_273.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 4.40 The binary interaction parameter PCSKIJ between LDPE and ethylene.</div>


We enter the binary interaction parameter PCSKIJ between LDPE and ethylene based on Ref. [14]. See Figure 4.40.

#### 4.5.5 PCES (Physical Constant Estimation System) for Estimating Missing-Property Parameters

Following Figure 4.22, we estimate all missing-property parameters based on molecular structures. Figure 4.41 illustrates some of the estimated property parameters.

#### 4.5.6 Free Radical Polymerization Reactions for LDPE

We refer the reader to the identical kinetics in Table 4.4 and Figures 4.24a–4.24c in the previous workshop. We use essentially the same initial kinetic parameters as in the previous LDPE workshop. See Figure 4.42.

#### 4.5.7 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks

Table 4.9 gives the stream and block specifications.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_807_647_1008.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 4.41 An illustration of estimated property parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1068_808_1253.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.42 Initial kinetic parameter values for LDPE process.</div>


---

<!-- PDF page 193 -->

<div style="text-align: center;">Table 4.9 Stream and block specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (bar)</td><td style='text-align: center; word-wrap: break-word;'>E2 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>INIT1 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>INIT2 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Water (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2H4FEED</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>2020</td><td style='text-align: center; word-wrap: break-word;'>100,000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INITR1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>2020</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>9.2</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INITR2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>2020</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>4.6</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CW1,CW2</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>160,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CW3,CW4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (bar)</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEATER1</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEATER2</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MIX1, MIX2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2000(MIX1)</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1900(MIX2)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG1</td><td colspan="6">Reactor with countercurrent thermal fluid @170°; length = 250 M (RPLUG1 and RPLUG3); 200 m (RPLUG2 and RPUG4); diameter = 0.059 m; pressure drop = 100 bar (process stream); 4 bar (thermal fluid); reaction set = R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HPS,LPS</td><td style='text-align: center; word-wrap: break-word;'>250 bar (HPS); 1 bar (LPS)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="2">Adiabatic, Q = 0 Kcal/hr; vapor And liquid phases</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_788_714_1013.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 4.43 Specification of STEAM-TA property method for coolant stream.</div>


For each RPLUG reactor with external thermal fluid (cooling water), we specify in its block option the use of steam table, STEAM-TA, as the property method for the coolant stream. See Figure 4.43. We do this step for all four reactors.

#### 4.5.8 User FORTRAN Subroutine for Heat Transfer Calculations for the LDPE Reactor

The Aspen Polymers example for the LDPE tubular reactor uses a FORTRAN user subroutine, named usrfpe.f, to do heat transfer calculations. The reader can see

---

<!-- PDF page 194 -->

the details of this FORTRAN subroutine by opening the file with a NOTEPAD and finding that the subroutine is based on heat transfer correlations reported in Refs. [17, 33]. The subroutine includes a correlation for estimating the fouling resistance, named FR, across the reactor wall, which has a unit of  $ cm^{2} $-K-sec/cal:

 $$  FR=A+B^{*}W_{}\mathrm{POL}=REALQ(1)+REALQ(2)^{*}W_{}\mathrm{POL} $$ 

where A and B are empirical correlation parameters, corresponding to the FOR-TRAN code parameters, REALQ(1) and REALQ(2), with a unit of  $ cm^{2} $-K-sec/cal; and W_Pol is the weight fraction of polymer, dimensionless.

To use the subroutine, we must put the simulation file, WS4.2_LDPE BaseCase.bkp., in the same working folder as the FORTRAN subroutine, usrfpe.f. See Figure 4.44, in which we see the values of the two parameters of the fouling correlation, REALQ(1) and REALQ(2), being set to 40 and 100 cm²-K-sec/cal, respectively.

We need to repeat the parameter specification of Figure 4.44 for all four reactors, RPLUG1 to RPLUG4.

As many readers do not have the required version of FORTRAN compiler to run the subroutine, it is helpful to convert the FORTRAN file to the corresponding dll (dynamic link library) file and dlopt (dynamic link options) file. Fortunately, the required userfort.dll and userfort.dlopt files for heat transfer calculations are already present in the same working folder as the Aspen Polymers online LDPE example for our use without the need to compile the FORTRAN subroutine again.

The reader can check if you have the appropriate FORTRAN compiler for Aspen Polymers by checking the path: Start → Aspen Plus → Set Compiler V10 (or a higher version). If a compiler is present, you can follow the instructions on “How to compile and run an external user subroutine in an Aspen Plus simulation” (article ID 000094619, dated April 27, 2020) that are available through a search on the AspenTech support website.

To use the userfort.dll and userfort.dlopt files, we follow the path: Customize → Options → Run Settings → Engine Files → Linker Options → “userfort.dlopt” (see Figure 4.45). We must give a word of caution to the reader: if you click on the dotted

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_946_743_1201.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 4.44 Two real parameters for the fouling correlation, REALQ(1) and REALQ(2), equal to 40 and 100 cm²-K-sec/cal.</div>


---

<!-- PDF page 195 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_779_366.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.45 Specifying the linker options for user FORTRAN subroutine, telling the linker to use the dll file specified in the file userfort.dlopt.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_447_666_664.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 4.46 A warning: Do not link the *dlopt file with the detailed location on your computer drive. The simulation would not work.</div>


box to the right of the “Linker Options” to search for the *.dlopt file and find the file location as shown in Figure 4.46, the simulation will not work.

#### 4.5.9 Base-Case Simulation Targets and Kinetic Parameter Estimation

We use the same initial kinetic parameters for our LDPE process with tubular reactors as those with stirred autoclaves. See Figure 4.24c.

Our goal in simulating the base case is to identify the kinetic parameters to match the following production targets: (1) LPDE production rate = 18,500 kg/hr; (2) MWN = 65,000; and (3) MWW = 289,000.

Following the step-by-step procedure described in Section 4.4.8 and depicted in Figure 4.26, we fine-tune the kinetic parameters. First, by increasing the pre-exponential factors for both the chain initiation and chain propagation reactions from 2.5E8 to 6.075E8 1/sec, we are able to achieve an LDPE production rate of 18,499.1 kg/hr with an MWN of 61,245.5 and an MWW of 344,295.

Next, we decrease the pre-exponential factors for both chain transfer to monomer from 1.25E6 to 1.075E6 1/sec and for beta scission from 6.07E7 to 5.8E7 1/sec, resulting in an LDPE production of 18,498.7 kg/hr, an MWN of 64,192.3, and an MWW of 380,373.

To decrease MWW to 289,000, we decrease the pre-exponential factor for chain transfer to polymer from 1.24E6 to 0.918E6, leading to an LDPE production of

---

<!-- PDF page 196 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Type</td><td rowspan="2">Comp 1</td><td rowspan="2">Comp 2</td><td rowspan="2">Pre-Exp. //sec.</td><td rowspan="2">Act-Energy //kmol.</td><td rowspan="2">Act-Volume - cum/kmol.</td><td rowspan="2">Ref. Temp. C</td><td rowspan="2">No. Rads</td><td rowspan="2">[n]</td><td rowspan="2">TDB fraction [I]</td><td rowspan="2">Gel Effect</td><td rowspan="2">Efficiency [e]</td><td rowspan="2">Efficiency Gel Effect</td></tr><tr></tr><tr><td style='text-align: center; word-wrap: break-word;'>INF-DEC</td><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.8807e-06</td><td style='text-align: center; word-wrap: break-word;'>1.2721e+08</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INF-DEC</td><td style='text-align: center; word-wrap: break-word;'>INF2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.7907e-09</td><td style='text-align: center; word-wrap: break-word;'>1.5346e+08</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-IN</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.075e+08</td><td style='text-align: center; word-wrap: break-word;'>3.53e+07</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROHAGATION</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>6.075e+08</td><td style='text-align: center; word-wrap: break-word;'>3.53e+07</td><td style='text-align: center; word-wrap: break-word;'>-0.0213</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>1.075e+06</td><td style='text-align: center; word-wrap: break-word;'>4.54e+07</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-POL</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>918000</td><td style='text-align: center; word-wrap: break-word;'>3.04e+07</td><td style='text-align: center; word-wrap: break-word;'>0.0016</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \beta $-SCISSION</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.8e+07</td><td style='text-align: center; word-wrap: break-word;'>4.53e+07</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TERM-DIS</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>2.5e+09</td><td style='text-align: center; word-wrap: break-word;'>4.19e+06</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TERM-COMB</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>2.5e+09</td><td style='text-align: center; word-wrap: break-word;'>4.19e+06</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SC-BRANCH</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>1.3e+09</td><td style='text-align: center; word-wrap: break-word;'>4.16e+07</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 4.47 Kinetic parameter values to reach an LDPE production of 18,487 kg/hr, an MWN of 64,202 and an MWW of 288,860.</div>


18,487 kg/hr, an MWN of 64,202, and an MWW of 288,860, which are very close to production targets. Figure 4.47 shows the resulting values of kinetic parameters. We save the validated simulation file as WS4.2_LDPE BaseCase.bkp.

We illustrate further results from this workshop. Figures 4.48a–4.48c show the “Profiles” results and how to plot the temperature profile along the length of reactor RPLUG1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_644_810_917.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.48a "Profiles" results from reactor RPLUG1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_170_998_503_1243.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">Figure 4.48b Setting up the temperature-profile plot.</div>


---

<!-- PDF page 197 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Length in m</th><th style='text-align: center;'>Mass Flowsheet</th><th style='text-align: center;'>RPLUG1 (RPLug) - Profile</th><th style='text-align: center;'>Control Root</th><th style='text-align: center;'>(PROTM MATRIAL - Results (Default) - Temperature - Pmt)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>2450</td><td style='text-align: center;'>2450</td><td style='text-align: center;'>2450</td><td style='text-align: center;'>2450</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>2400</td><td style='text-align: center;'>2400</td><td style='text-align: center;'>2400</td><td style='text-align: center;'>2400</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>2350</td><td style='text-align: center;'>2350</td><td style='text-align: center;'>2350</td><td style='text-align: center;'>2350</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td><td style='text-align: center;'>2300</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>2250</td><td style='text-align: center;'>2250</td><td style='text-align: center;'>2250</td><td style='text-align: center;'>2250</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td><td style='text-align: center;'>2200</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>2150</td><td style='text-align: center;'>2150</td><td style='text-align: center;'>2150</td><td style='text-align: center;'>2150</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>2100</td><td style='text-align: center;'>2100</td><td style='text-align: center;'>2100</td><td style='text-align: center;'>2100</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>2050</td><td style='text-align: center;'>2050</td><td style='text-align: center;'>2050</td><td style='text-align: center;'>2050</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>1950</td><td style='text-align: center;'>1950</td><td style='text-align: center;'>1950</td><td style='text-align: center;'>1950</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>1900</td><td style='text-align: center;'>1900</td><td style='text-align: center;'>1900</td><td style='text-align: center;'>1900</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>1850</td><td style='text-align: center;'>1850</td><td style='text-align: center;'>1850</td><td style='text-align: center;'>1850</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>1750</td><td style='text-align: center;'>1750</td><td style='text-align: center;'>1750</td><td style='text-align: center;'>1750</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>1700</td><td style='text-align: center;'>1700</td><td style='text-align: center;'>1700</td><td style='text-align: center;'>1700</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>1650</td><td style='text-align: center;'>1650</td><td style='text-align: center;'>1650</td><td style='text-align: center;'>1650</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>1600</td><td style='text-align: center;'>1600</td><td style='text-align: center;'>1600</td><td style='text-align: center;'>1600</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>1550</td><td style='text-align: center;'>1550</td><td style='text-align: center;'>1550</td><td style='text-align: center;'>1550</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>1450</td><td style='text-align: center;'>1450</td><td style='text-align: center;'>1450</td><td style='text-align: center;'>1450</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>1400</td><td style='text-align: center;'>1400</td><td style='text-align: center;'>1400</td><td style='text-align: center;'>1400</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>1350</td><td style='text-align: center;'>1350</td><td style='text-align: center;'>1350</td><td style='text-align: center;'>1350</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>1300</td><td style='text-align: center;'>1300</td><td style='text-align: center;'>1300</td><td style='text-align: center;'>1300</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>1250</td><td style='text-align: center;'>1250</td><td style='text-align: center;'>1250</td><td style='text-align: center;'>1250</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1200</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>1150</td><td style='text-align: center;'>1150</td><td style='text-align: center;'>1150</td><td style='text-align: center;'>1150</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>1100</td><td style='text-align: center;'>1100</td><td style='text-align: center;'>1100</td><td style='text-align: center;'>1100</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>1050</td><td style='text-align: center;'>1050</td><td style='text-align: center;'>1050</td><td style='text-align: center;'>1050</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td></tr>
    <tr><td style='text-align: center;'>185</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>195</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>205</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>215</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td></tr>
    <tr><td style='text-align: center;'>235</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>245</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>255</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 4.48c Temperature profile along the length of reactor RPLUG1.</div>


#### 4.5.10 Model Applications

In the current flowsheet of Figure 4.35, 60% of the feed mass flow goes to the lower reactor train through the split feed, C2H4FD21. We want to investigate how the feed split fraction affects the resulting LDPE production and the polymer MW and MWW. Figures 4.49a–4.49c show the inputs and tabulated results of our sensitivity analysis, and Figures 4.50a and 4.50b illustrate the results graphically.

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_700_761_929.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.49a Defining the feed split fraction as the independent variable, "Vary".</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_994_761_1229.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.49b Defining the LDPR production rate, MWN, and MWW as the dependent variables.</div>


---

<!-- PDF page 198 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">Main Flowsheet  $ \times $ S-1 - In</td><td style='text-align: center; word-wrap: break-word;'>VARY 1 FEEDSPLI C2H4FD21 FRAC</td><td rowspan="2">LPDEPROD</td><td rowspan="2">LPDEMWN</td><td rowspan="2">LPDEMWW</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Vary</td><td style='text-align: center; word-wrap: break-word;'>Define</td><td style='text-align: center; word-wrap: break-word;'>Row/Case</td><td rowspan="2">Status</td></tr><tr><td colspan="3">Sampled variables (dra</td><td colspan="3">KG/HR</td></tr><tr><td colspan="2">Variable</td><td style='text-align: center; word-wrap: break-word;'>1 OK</td><td style='text-align: center; word-wrap: break-word;'>0.3</td><td style='text-align: center; word-wrap: break-word;'>18590.9</td><td style='text-align: center; word-wrap: break-word;'>61910.1</td><td style='text-align: center; word-wrap: break-word;'>264335</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2 OK</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>18839.1</td><td style='text-align: center; word-wrap: break-word;'>63200.6</td><td style='text-align: center; word-wrap: break-word;'>271968</td></tr><tr><td colspan="2">LPDEPROD</td><td style='text-align: center; word-wrap: break-word;'>3 OK</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>18901.5</td><td style='text-align: center; word-wrap: break-word;'>64271.4</td><td style='text-align: center; word-wrap: break-word;'>283277</td></tr><tr><td colspan="2">LPDEMWN</td><td style='text-align: center; word-wrap: break-word;'>4 OK</td><td style='text-align: center; word-wrap: break-word;'>0.6</td><td style='text-align: center; word-wrap: break-word;'>18487</td><td style='text-align: center; word-wrap: break-word;'>64202</td><td style='text-align: center; word-wrap: break-word;'>288860</td></tr><tr><td colspan="2">LPDEMWW</td><td style='text-align: center; word-wrap: break-word;'>5 OK</td><td style='text-align: center; word-wrap: break-word;'>0.7</td><td style='text-align: center; word-wrap: break-word;'>17514</td><td style='text-align: center; word-wrap: break-word;'>62571.4</td><td style='text-align: center; word-wrap: break-word;'>277107</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6 OK</td><td style='text-align: center; word-wrap: break-word;'>0.8</td><td style='text-align: center; word-wrap: break-word;'>16296.9</td><td style='text-align: center; word-wrap: break-word;'>60374</td><td style='text-align: center; word-wrap: break-word;'>257562</td></tr><tr><td colspan="2">$ \times $</td><td style='text-align: center; word-wrap: break-word;'>7 OK</td><td style='text-align: center; word-wrap: break-word;'>0.9</td><td style='text-align: center; word-wrap: break-word;'>14994</td><td style='text-align: center; word-wrap: break-word;'>58074</td><td style='text-align: center; word-wrap: break-word;'>245041</td></tr></table>

<div style="text-align: center;">Figure 4.49c Tabulating the sensitivity analysis results.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-axis</th><th style='text-align: center;'>S1- Results Summary</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.00</td><td style='text-align: center;'>4000</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>4100</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>4150</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>4180</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>4200</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>4220</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>4240</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>4260</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>4280</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>4300</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>4320</td></tr>
    <tr><td style='text-align: center;'>0.44</td><td style='text-align: center;'>4340</td></tr>
    <tr><td style='text-align: center;'>0.48</td><td style='text-align: center;'>4360</td></tr>
    <tr><td style='text-align: center;'>0.52</td><td style='text-align: center;'>4380</td></tr>
    <tr><td style='text-align: center;'>0.56</td><td style='text-align: center;'>4400</td></tr>
    <tr><td style='text-align: center;'>0.60</td><td style='text-align: center;'>4420</td></tr>
    <tr><td style='text-align: center;'>0.64</td><td style='text-align: center;'>4440</td></tr>
    <tr><td style='text-align: center;'>0.68</td><td style='text-align: center;'>4460</td></tr>
    <tr><td style='text-align: center;'>0.72</td><td style='text-align: center;'>4480</td></tr>
    <tr><td style='text-align: center;'>0.76</td><td style='text-align: center;'>4500</td></tr>
    <tr><td style='text-align: center;'>0.80</td><td style='text-align: center;'>4520</td></tr>
    <tr><td style='text-align: center;'>0.84</td><td style='text-align: center;'>4540</td></tr>
    <tr><td style='text-align: center;'>0.88</td><td style='text-align: center;'>4560</td></tr>
    <tr><td style='text-align: center;'>0.92</td><td style='text-align: center;'>4580</td></tr>
    <tr><td style='text-align: center;'>0.96</td><td style='text-align: center;'>4600</td></tr>
    <tr><td style='text-align: center;'>0.98</td><td style='text-align: center;'>4620</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 4.50a The LPDE production rate reaching a maximum at a feed split ratio of 0.5.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>LECs/min</th><th style='text-align: center;'>LECs/min</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.35</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.45</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.55</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.60</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.65</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.70</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.75</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.80</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.85</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.90</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>0.95</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
    <tr><td style='text-align: center;'>1.00</td><td style='text-align: center;'>10000</td><td style='text-align: center;'>10000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 4.50b Effect of feed split ration on the polymer product MWN and MWW.</div>


---

<!-- PDF page 199 -->

This concludes the current workshop. We save the simulation file as WS4.2 LPDE Applications.bkp.

#### 4.6 Workshop 4.3: Simulation of Tubular Reactors for Ethylene–Vinyl Acetate (EVA) Copolymerization Process

#### 4.6.1 Objective

The objective of this workshop is to demonstrate that the methodology for simulating high-pressure LPDE processes using stirred autoclave reactors or tubular reactors presented in Workshops 4.1 and 4.2 is readily applicable to simulating the EVA copolymerization process using similar reactors. While there are a number of student theses and published reports on simulating the EVA copolymerization processes [7, 22–30, 36], we can only find partial process information (such as temperature, pressure, mass flow rate of feed and product streams, chemical names of initiators, solvents, and modifiers or CTAs used, operating conditions of unit operation and reactor blocks, and copolymer production targets) that is reported in separate references. As a result, we can only make educated guesses about appropriate process conditions based on published information. Additionally, these reports lack specific details in their selection of appropriate thermodynamic methods, estimation of essential property parameters, and free radical polymerization reactions. In this workshop, we focus on how to select the appropriate thermodynamic methods, property parameters, and polymerization kinetics. We show that applying our simulation methodology gives reasonable simulated results when compared to published information. We encourage those readers who have specific design and production data for an EVA copolymerization process to make appropriate changes to the current workshop and practice the application of the simulation methodology to industrial process data.

#### 4.6.2 Process Background

Table 4.10 compares the general features of EVA copolymer production by stirred autoclave and tubular reactors [37].

Figures 4.51a and 4.51b show two published process flowsheets for high-pressure LDPE and for EVA copolymerization using stirred autoclave reactors [30, 38].

The autoclave reactor in Figure 4.51a has seven reaction zones, with reaction feeds entering zones 1–5 and the initiator feeds entering zones 1, 2, and 4. We could modify our previous stirred autoclave reactor system for LDPE production in Figures 4.10 and 4.11 to develop a simulation flowsheet for the EVA copolymerization reactor section. For example, Figure 4.52 shows the autoclave reactor section of our flowsheet.

In this workshop, we focus on simulating the tubular reactor system for producing EVA copolymer. We modify our previous tubular reactor system for LDPE production in Figures 4.34 and 4.35 to develop a simulation flowsheet for the EVA

---

<!-- PDF page 200 -->

<div style="text-align: center;">Table 4.10 A general comparison of tubular and stirred autoclave reactors for EVA copolymer production.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process</td><td style='text-align: center; word-wrap: break-word;'>Tubular reactors</td><td style='text-align: center; word-wrap: break-word;'>Stirred autoclaves</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Typical mass production rate per reactor train, ton/yr</td><td style='text-align: center; word-wrap: break-word;'>400,000 ton/yr (50 ton/hr @8000 hr/yr)</td><td style='text-align: center; word-wrap: break-word;'>150,000 ton/yr (18.75 ton/hr @8000 hr/yr)</td></tr><tr><td colspan="3">Reactors</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>L/D ratio</td><td style='text-align: center; word-wrap: break-word;'>1000-40,000 : 1</td><td style='text-align: center; word-wrap: break-word;'>10-40 : 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Monomer conversion%</td><td style='text-align: center; word-wrap: break-word;'>25-35</td><td style='text-align: center; word-wrap: break-word;'>10-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Heat removal</td><td style='text-align: center; word-wrap: break-word;'>Water-cooling jacket</td><td style='text-align: center; word-wrap: break-word;'>Cold feed, hot product</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Scaling</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure, MPa</td><td style='text-align: center; word-wrap: break-word;'>240-300</td><td style='text-align: center; word-wrap: break-word;'>130-220</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature, °C</td><td style='text-align: center; word-wrap: break-word;'>250-340</td><td style='text-align: center; word-wrap: break-word;'>150-300</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Initiators</td><td style='text-align: center; word-wrap: break-word;'>Air,  $ O_{2} $, organic peroxides</td><td style='text-align: center; word-wrap: break-word;'>Organic peroxides</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chain transfer agents</td><td style='text-align: center; word-wrap: break-word;'>Propylene, propane, propionaldehyde</td><td style='text-align: center; word-wrap: break-word;'>Isobutene, n-butane</td></tr><tr><td colspan="3">Reactor conditions</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Feed gas</td><td style='text-align: center; word-wrap: break-word;'>Preheating</td><td style='text-align: center; word-wrap: break-word;'>Cooling</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature range</td><td style='text-align: center; word-wrap: break-word;'>Narrow</td><td style='text-align: center; word-wrap: break-word;'>Broad</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure change, MPa</td><td style='text-align: center; word-wrap: break-word;'>30-40</td><td style='text-align: center; word-wrap: break-word;'>&lt;5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>High-pressure relief valve, impulse change</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Start-up</td><td style='text-align: center; word-wrap: break-word;'>Fixed pressure, gradually raise temperature</td><td style='text-align: center; word-wrap: break-word;'>Gradually raise both pressure and temperature</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_873_811_1197.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.51a Flowsheet of the EVA copolymerization using a stirred autoclave reactor. Source: Chien et al. [30]/with permission of Elsevier.</div>


---

<!-- PDF page 201 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_767_440.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.51b Flowsheet of the ICI high-pressure autoclave reactor technology for LDPE production and for EVA copolymerization with minor modification. Source: Adapted from López-Carpy et al. [38].</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_544_764_994.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 4.52 Simulation flowsheet of the stirred autoclave reactor for EVA copolymerization.</div>


copolymerization reactor section. For convenience, we modify the simulation file, WS4.2_LDPE BaseCase.bkp from Workshop 4.2. Figure 4.53 shows the reactor section of our flowsheet. We save the simulation file as WS4.3.bkp.

#### 4.6.3 Unit System, Components, and Characterization of Polymer

We choose METCBAR as our unit system. Figure 4.54 shows our component specifications for the EVA copolymerization process. Following Ref. [23], we

---

<!-- PDF page 202 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_146_812_442.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.53 Simulation flowsheet of a tubular reactor system for high-pressure EVA copolymerization with jacketed cooling, two split feeds, four reaction zones, two initiator injection inlets modeled by four plug-flow reactors in series, plus high-pressure and low-pressure separators.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_593_768_798.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 4.54 Component specifications.</div>


choose TBPEH (tert-butylperoxy-2-ethylhexanoate; CAD number 3006-82-4) as our initiator. Other potential initiators are TBPND (tert-butyl peroxyneodecanoate; CAS number 26748-41-4), TBPB (CAS number 614-45-9); and TBPPI (t-butyl peroxypivalate; CAS number 927-07-1). All four are available within the Aspen Polymers initiator database. For modifiers or CTAs, the literature suggests propylene [23, 37] or propane [37] for tubular reactors, isobutylene and n-butane [37] for stirred autoclave reactors, and n-hexane [36] as our solvent. Additionally, we follow Figures 4.16 and 4.17 to define our repeat segments, E2-R and VA-R, and our polymer POLYEVA, together with the selection of attributes for free radical polymerization.

We also follow Figures 4.18, 4.19a–4.19c to obtain the chemical structures of initiators TBPEH and TBPND and characterize their general structures according to bond types. See the example file folder for Chapter 4 for TBPEH.mol and TBPND.mol. Figure 4.55 illustrates the chemical structure of TBPEH obtained from the initiator database of Aspen Polymers, API100 INITIATO.

---

<!-- PDF page 203 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_150_665_489.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 4.55 Chemical structure of initiator TBPEH.</div>


#### 4.6.4 Thermodynamic Method and Property Parameters for Components and Polymer

We follow Figure 4.37 in the previous workshop for high-pressure LDPE, choose POLYPCSF as our thermodynamic method, and enter the required pure-component parameters in Figure 4.56.

In the figure, PCSFTU is the segment energy parameter (K), PCSFTV is the segment diameter ( $ \mathring{A} $), and PCSFTM is the segment number. The last parameter, PCSFTR, is a ratio parameter that is equal to PCSFTM (m) divided by the molecular weight of the monomer (M) or m/M. This parameter is reserved for polymer. We find the parameter values for E2, VA, propylene (a CTA), n-butane (another CTA), solvent (hexane), and water from [13, 14, 23], and for E2-R and VA-R from [22]. We assume the values for initiator TBPEH following [12]. For propylene, we follow the values given in Figure 2.53.

Following Figure 4.22, we estimate all missing parameters using molecular structure-based estimates. As an example, Figure 4.57 shows the resulting parameters for the temperature-dependent ideal-gas heat capacity correlation, CPlG-1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_1056_779_1220.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 4.56 Pure-component and segment parameters.</div>


---

<!-- PDF page 204 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_808_275.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.57 Parameter values for temperature-dependent, ideal-gas heat capacity correlation, CPlG-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_358_808_551.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 4.58 Parameter values for temperature-dependent, Antoine vapor pressure correlation, PLXANT.</div>


Following Figure 4.39, we enter a parameter value of -40 for liquid vapor pressure, PLXANT, for initiator TBPEH, to ensure that it stays in the liquid phase and does not vaporize. See Figure 4.58.

#### 4.6.5 Free Radical Polymerization Kinetics for EVA Copolymerization

We expand the reaction set for free radical polymerization for high-pressure LDPE in Table 4.4 to include the addition of a comonomer, VA, and the corresponding changes to the chain initiation, chain propagation, chain transfer, chain termination reactions, and the beta-scission and short-chain branching reactions involving both the monomer E2 and comonomer VA. This results in Table 4.11, in which we have also added the initial kinetic parameter values based on the literature.

We follow the procedure in the previous workshops to generate a reaction set R-1 based on the free radical polymerization model within Aspen Polymers for EVA copolymerization. Figures 4.59 and 4.60 illustrate the specification of species and the resulting reactions for EVA copolymerization. Refer to Table 4.11 for the values of initial kinetic parameters.

#### 4.6.6 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks

Table 4.12 gives the stream and block specifications.

Following Figure 4.43, we specify in the block option of each RPLUG reactor with external thermal fluid (cooling water) the use of steam table, STEAM-A, as the property method for the coolant stream. We also follow Figures 4.44–4.46 in Section 4.5.7.

---

<!-- PDF page 205 -->

<div style="text-align: center;">Table 4.11 Initial parameters for free radical polymerization kinetics for EVA copolymerization.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reaction</td><td style='text-align: center; word-wrap: break-word;'>Comp 1</td><td style='text-align: center; word-wrap: break-word;'>Comp 2</td><td style='text-align: center; word-wrap: break-word;'>Pre-exponential factor (1/sec)</td><td style='text-align: center; word-wrap: break-word;'>Activation energy (cal/mol)</td><td style='text-align: center; word-wrap: break-word;'>Activation volume (Cum/kmol)</td><td style='text-align: center; word-wrap: break-word;'>References</td><td style='text-align: center; word-wrap: break-word;'>Notes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Initiator decomposition</td><td rowspan="2">E2</td><td rowspan="2">E2(1)</td><td rowspan="2">1.1742E-4</td><td rowspan="2">25759.5</td><td rowspan="2">0</td><td rowspan="2">[4, 25]</td><td rowspan="2">Initiator efficiency = 0.4; number of radicals = 2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TBPND</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Initiator decomposition</td><td rowspan="3">E2</td><td rowspan="3">E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.25E8</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td><td style='text-align: center; word-wrap: break-word;'>-0.02</td><td style='text-align: center; word-wrap: break-word;'>[13, 25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TDPHE</td><td style='text-align: center; word-wrap: break-word;'>1.47E7</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td><td style='text-align: center; word-wrap: break-word;'>-0.0107</td><td style='text-align: center; word-wrap: break-word;'>[13, 25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chain initiation $ ^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>1.25E8</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td><td style='text-align: center; word-wrap: break-word;'>-0.02</td><td style='text-align: center; word-wrap: break-word;'>[8, 25, 39]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">Chain propagation</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.148E8</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td><td style='text-align: center; word-wrap: break-word;'>-0.02</td><td style='text-align: center; word-wrap: break-word;'>[8, 25, 39]</td><td style='text-align: center; word-wrap: break-word;'>$ K_{p,11} = 1.09 \times k_{p,12} $ [8]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>1.47E7</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td><td style='text-align: center; word-wrap: break-word;'>-0.0107</td><td style='text-align: center; word-wrap: break-word;'>[8, 25, 39]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.387E7</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td><td style='text-align: center; word-wrap: break-word;'>-0.0107</td><td style='text-align: center; word-wrap: break-word;'>[8, 25, 39]</td><td style='text-align: center; word-wrap: break-word;'>$ K_{p,22} = 1.06 \times k_{p,21} $ [8]</td></tr><tr><td rowspan="4">Chain transfer to monomer</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>8.7E5</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td><td style='text-align: center; word-wrap: break-word;'>-0.02</td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>8.7E5</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>7.616E3</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>7.616E3</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td rowspan="2">Chain transfer to agent</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>8.7E5</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td><td style='text-align: center; word-wrap: break-word;'>-0.02</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>7.616E3</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td rowspan="4">Chain transfer to polymer</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>4.78E8</td><td style='text-align: center; word-wrap: break-word;'>13120.1</td><td style='text-align: center; word-wrap: break-word;'>0.0044</td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>4.78E8</td><td style='text-align: center; word-wrap: break-word;'>13210.1</td><td style='text-align: center; word-wrap: break-word;'>0.0044</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.088E4</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.088E4</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Termination by</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.25E9</td><td style='text-align: center; word-wrap: break-word;'>649.4</td><td style='text-align: center; word-wrap: break-word;'>0.013</td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">(1) combination and (2) disproportionate</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.25E9</td><td style='text-align: center; word-wrap: break-word;'>649.4</td><td style='text-align: center; word-wrap: break-word;'>0.013</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>3.7E9</td><td style='text-align: center; word-wrap: break-word;'>3199.1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>3.7E9</td><td style='text-align: center; word-wrap: break-word;'>3199.1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td rowspan="2">Beta scission</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.292E7</td><td style='text-align: center; word-wrap: break-word;'>11268.3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>1.292E7</td><td style='text-align: center; word-wrap: break-word;'>11268.3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr><tr><td rowspan="2">Short-chain branching</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>1.6E8</td><td style='text-align: center; word-wrap: break-word;'>10942.4</td><td style='text-align: center; word-wrap: break-word;'>0.0229</td><td style='text-align: center; word-wrap: break-word;'>[25]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E2(1)</td><td style='text-align: center; word-wrap: break-word;'>E2(2)</td><td style='text-align: center; word-wrap: break-word;'>1.6E8</td><td style='text-align: center; word-wrap: break-word;'>10942.4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Assumed</td></tr></table>

a) Set chain initiation rate constant equal to or larger than chain propagation rate constant [39]; assume the same termination rate constants by combination and by disproportionation.

---

<!-- PDF page 206 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_145_648_387.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 4.59 Specification of species for EVA copolymerization.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_452_766_1002.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 4.60 Free radical polymerization reactions to produce EVA copolymer.</div>


to specify the use of the same user subroutine for heat transfer calculations. We save the simulation file with the initial kinetic parameters as WS4.3BaseCase.bkp.

#### 4.6.7 Base-Case Simulation Targets and Kinetic Parameter Estimation

Running the base-case simulation file gives an EVA copolymer production rate of 70,112 kg/hr (which represents a monomer conversion of 70.1%), an MWN of 2385, and an MWW of 980,352.

---

<!-- PDF page 207 -->

<div style="text-align: center;">Table 4.12 Stream and block specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (bar)</td><td style='text-align: center; word-wrap: break-word;'>E2 (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>VA (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>TBPEH (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>CTA (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Solvent (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Water (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2VAFEEED</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>2020</td><td style='text-align: center; word-wrap: break-word;'>70,000</td><td style='text-align: center; word-wrap: break-word;'>30,000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INITR1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>2010</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INITR2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>2010</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CW1, CW2</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>160,000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CW3, CW4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Temperature (°C)</td><td style='text-align: center; word-wrap: break-word;'>Pressure (bar)</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEATER1</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HEATER2</td><td style='text-align: center; word-wrap: break-word;'>250</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MIX1,MIX2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2000(MIX1)</td><td style='text-align: center; word-wrap: break-word;'>Liquid-only</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1900(MIX2)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG1</td><td colspan="8">Reactor with countercurrent thermal fluid @ 170°; length = 250 m (RPLUG1 and RPLUG3); 220 m (RPLUG2 and RPUG4); diameter = 0.059 m; pressure drop = 100 bar (process stream); 4 bar (thermal fluid); reaction set = R1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HPS,LPS</td><td style='text-align: center; word-wrap: break-word;'>250 bar (HPS); 1 bar (LPS)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="3">Adiabatic, Q = 0 kcal/hr; vapor and liquid phases</td></tr></table>

We apply the methodology for kinetic parameter estimation for LDPE process in Figure 4.26 to EVA copolymerization. According to Table 4.10, the monomer conversion for EVA copolymerization is about 25% to 35%, but it could go up to nearly 40%. We wish to fine-tune our kinetic parameters to produce an EVA copolymer with a monomer conversion of 39%, an MWN of 49,500, and an MWW of 420,000.

In particular, we note three important guidelines from Section 4.4.8: (1) as the pre-exponential factors for chain initiation and chain propagation increase, the production rate or monomer conversion increases; (2) as the pre-exponential factors for chain transfer to monomer, to CTA, or to solvent, and for beta-scission reaction increase, MWN decreases; and (3) as the pre-exponential factor for chain transfer to polymer decreases, MWW (or PDI) decreases.

Following guideline (1), we adjust the pre-exponential factors for chain initiation and propagation, as shown in Figure 4.61, keeping in mind that the propagation pre-exponential factor,  $ k_{o,E2,E2} = 1.09 \times k_{o,E2,VA} $ (that is,  $ 1.635 \times 10^{-7} = 1.09 \times 1.5 \times 10^{-7} $ in Figure 4.61), and  $ k_{o,VA,VA} = 1.06 \times k_{o,VA,E2} $ (that is,  $ 1.59 \times 10^{-7} = 1.5 \times 10^{-7} $ in Figure 4.61), according to Ref. [8] noted in Table 4.10. We set the pre-exponential factors for chain transfer reactions to 12,000. We do not change the pre-exponential factors for other reactions not shown in Figure 4.61. We save the simulation file as WS4.3-1.bkp.

Running the simulation file WS4.3-1.bkp gives an EVA copolymer production rate of 39141 kg/hr (representing a monomer conversion of 39.1%), an MWN of 1585, and an MWW of 650,753. The resulting conversion is within the target value between 38% and 40%.

---

<!-- PDF page 208 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Comp 1</td><td style='text-align: center; word-wrap: break-word;'>Comp 2</td><td style='text-align: center; word-wrap: break-word;'>Pre-Exp 1/we</td><td style='text-align: center; word-wrap: break-word;'>Act-Energy cal/mol</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT-DEC</td><td style='text-align: center; word-wrap: break-word;'>TBPEH</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.00011742</td><td style='text-align: center; word-wrap: break-word;'>27579.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.5e+07</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAIN-INI</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.5e+07</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>1.635e+07</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>1.5e+07</td><td style='text-align: center; word-wrap: break-word;'>7550.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>1.5e+07</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPAGATION</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>1.75e+07</td><td style='text-align: center; word-wrap: break-word;'>4947.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>6298.8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-MON</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>6298.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-AGENT</td><td style='text-align: center; word-wrap: break-word;'>E2</td><td style='text-align: center; word-wrap: break-word;'>CTA</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>9998.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAT-AGENT</td><td style='text-align: center; word-wrap: break-word;'>VA</td><td style='text-align: center; word-wrap: break-word;'>CTA</td><td style='text-align: center; word-wrap: break-word;'>12000</td><td style='text-align: center; word-wrap: break-word;'>6298.6</td></tr></table>

<div style="text-align: center;">Figure 4.61 Modified kinetic parameters to achieve a monomer conversion between 38% and 40%.</div>


<div style="text-align: center;">Table 4.13 Comparison of simulation results with production targets.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Target</td><td style='text-align: center; word-wrap: break-word;'>Simulation</td><td style='text-align: center; word-wrap: break-word;'>Error (%)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EVA copolymer (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>39,000</td><td style='text-align: center; word-wrap: break-word;'>38,949</td><td style='text-align: center; word-wrap: break-word;'>0.131</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWN</td><td style='text-align: center; word-wrap: break-word;'>49,500</td><td style='text-align: center; word-wrap: break-word;'>49,606.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'>420,000</td><td style='text-align: center; word-wrap: break-word;'>420,357</td><td style='text-align: center; word-wrap: break-word;'>0.0085</td></tr></table>

Following guidelines (2) and (3) for kinetic parameter tuning, we increase the pre-exponential factor for chain transfer to monomer and to agent from 12,000 to 16,400, change the pre-exponential factor for beta scission to also 16,400, and decrease the pre-exponential factor for chain transfer to polymer to 2.44E5. Table 4.13 shows the resulting comparison of simulation results with target values. We save the simulation file as WS4.3-2.bkp.

## References

1 Lingard, S. (2002). Styrenics Modeling Seminar. Aspen Technology, Inc., Houston, TX.

2 Odian, G. (1991). Principles of Polymerization, 3e. New York: Wiley.

3 Aspen Technology, Inc. (2017). Free Radical Bulk Polymerization Models. Aspen Polymers V8.5 Unit Operation and Reactor Models, pp. 163–198.

4 Aspen Technology, Inc. (2017). Initiator Decomposition Rate Parameters. Aspen Polymers V8.5 Unit Operation and Reactor Models, pp. 431–444.

5 Hui, A.W. and Hamielec, A.E. (1972). Thermal polymerization of styrene at high conversions and temperatures: an experimental study. Journal of Applied Polymer Science 16: 749.

6 Chapter 1: Free radical polymerization. https://ethz.ch/content/dam/ethz/special-interest/chab/icb/morbidelli-dam/documents/Education/PRCE/DOC_2016/Chapter1.pdf (accessed June 8, 2020).

7 Kan, T.W. (2003). Modeling of High-Pressure Ethylene-Vinyl Acetate Copolymer in Autoclave Reactor. M.S. thesis, Department of Chemical Engineering, National Taiwan University of Science and Technology, Taipei.

---

<!-- PDF page 209 -->

8 Ratzsch, M., Schneider, W., and Musche, D. (1971). Reactivity of ethylene in the radically initiated copolymerization of ethylene with vinyl acetate. Journal of Polymer Science Part A-1 9: 785.

9 Aspen Technology, Inc. (2019). Aspen Physical Property System: Physical Property Models, V.11.

10 Sanchez, I.C. and Lacombe, R.H. (1978). Statistical thermodynamics of polymer solutions. Macromolecules 11: 1145.

11 Orbey, H., Bokis, C.P., and Chen, C.C. (1998). Equation of state modeling of phase equilibrium in the low-density polyethylene process: the Sanchez–Lacombe, statistical associating fluid theory, and polymer-Soave–Redlich–Kwong equations of state. Industrial and Engineering Chemistry 37: 4481.

12 Aspen Technology, Inc. (2017). Application B8 - low-density high-pressure process. Aspen Polymers V8.4: Examples and Applications, pp. 187-204.

13 Gross, J. and Sadowski, G. (2001). Perturbed-chain SAFT: an equation of state based on a perturbation theory for chain molecules. Industrial and Engineering Chemistry Research 40: 1244.

14 Gross, J. and Sadowski, G. (2002). Application of perturbed-chain SAFT equation of state to associating systems. Industrial and Engineering Chemistry Research 41: 5510.

15 Boks, C.P., Ramanathan, S., Franjione, J. et al. (2002). Physical properties, reactor modeling, and polymerization kinetics in the low-density polyethylene tubular reactor process. Industrial and Engineering Chemistry Research 41: 1017.

16 Cheluget, E.L., Bokis, C.P., Wardhagh, L. et al. (2002). Modeling polyethylene fractionation using the perturbed-chain statistical associating fluid theory equation of state. Industrial and Engineering Chemistry Research 41: 968.

17 Chen, C.H., Vermeuchuk, J.G., Howell, J.A., and Ehrlich, P. (1976). Computer model for tubular high-pressure polyethylene reactor. AICHE Journal 22: 463.

18 Hendrickson, G. (1997). Simulation of a LDPE Autoclave Reactor with POLYMERS PLUS. Presented at Aspen World, Boston, MA, October, 1997. https://docplayer.net/27596341-Simulation-of-a-ldpe-autoclave-reactor-with-polymers-plus-greg-hendrickson-senior-process-engineer-chevron-chemical-company-kingwood-texas.html (accessed 20 May 2020).

19 Caliani, E., Cavalcanti, M., Lona, L.M., and Fernandez, F. (2008). Modeling and simulation of high-pressure industrial high-pressure polyethylene reactor. Express Polymer Letters 2: 57.

20 Azmi, A. and Aziz, N. (2016). Low density polyethylene tubular reactor modeling: overview of the model developments and future directions. Journal of Applied Engineering Research 11: 9906.

21 Zhmad, Z. and Azix, N. (2018). Modeling and nonlinearity of low-density polyethylene (LDPE) tubular reactor. Materials Today: Proceedings 5: 21612.

22 Camacho, J., Diez, E., Diaz, I., and Ovejero, G. (2017). PC-SAFT thermodynamics of EVA copolymer-solvent systems. Fluid Phase Equilibria 449: 10.

23 Lee, Y., Jeon, K., Cho, J. et al. (2019). Multicomponent model of ethylene-vinyl acetate autoclave reactor: a combined computational fluid dynamics and polymerization kinetics model. Industrial and Engineering Chemistry Research 58: 16459.

---

<!-- PDF page 210 -->

24 Samaroria, C. and Brandolin, A. (2000). Modeling of molecular weights in industrial autoclave reactors for high pressure polymerization of ethylene and ethylene-vinyl acetate. Polymer Engineering and Science 40: 1480.

25 Ghiass, M. and Hutchinson, R.A. (2003). Simulation of free radical high pressure copolymerization in a multizone autoclave: model development and application. Polymer Reaction Engineering 11: 989.

26 Chien, I.L., Kan, T.W., and Cheb, B.S. (2007). Dynamic simulation and operation of a high pressure ethylene-vinyl acetate autoclave reactor. Computers and Chemical Engineering 31: 233.

27 Chen, B. S. (2004). Modeling and Control of High-Pressure Ethylene-Vinyl Acetate Copolymerization Process. M.S. thesis, Department of Chemical Engineering, National Taiwan University of Science and Technology, Taipei.

28 Lee, H.Y., Yang, T.H., Chien, I.L., and Huang, H.P. (2009). Grade transition using dynamic neural networks for an industrial high-pressure ethylene-vinyl acetate (EVA) copolymerization process. Computers and Chemical Engineering 33: 1371.

29 Sharmin, R., Sundararaj, U., Shah, S. et al. (2006). Inferential sensors for estimation of polymer quality parameters: industrial application of PLS-based soft sensor for a LDPE plant. Chemical Engineering Science 61: 6372.

30 Chien, I.L., Kan, T.W. and Chen, B.S. (2005). Rigorous modeling of a high-pressure ethylene-vinyl acetate (EVA) copolymerization autoclave reactor. IFAC Proceedings. https://folk.ntnu.no/skoge/prost/proceedings/ifac2005/Fullpapers/02171.pdf (accessed 10 June 2020).

31 Aspen Technology, Inc. (2017). Application B1 - Polystyrene Bulk Polymerization by Thermal Initiation. Aspen Polymers V8.4: Examples and Applications, pp. 97-108.

32 Yan, R. Study of Operating Mode and Process Simulation of LDPE Plant at BYPC(2000). China Synthetic Resin and Plastics 17 (2): 36.

33 Kiparissides, C., Veros, G., and MacGregor, J.F. (1993). Mathematical modeling, optimization, and quality control of high-pressure ethylene polymerization reactor. Reviews in Macromolecular Chemistry & Physics C33: 437.

34 Pladis, P. and Kiparissides, C. (2014). Polymerization reactors. https://doi.org/10.1016/B978-0-12-409547-2.10908-4 (accessed 1 June 2020).

35 Boks, C.P., Orbey, H., and Chen, C.C. (1999). Properly model polymer processes. Chemical Engineering Progress 95 (4): 39.

36 Kawahara, T. and Hikasa, T. (2005). Method for producing ethylene-vinyl acetate copolymer and saponified product thereof., U. S. Patent 6,838,517 B2.

37 Liu, Y.L., Su, G.R., and Cheng, M.H. (2019). The comparison and prospect of EVA plant with tubular reactor and autoclave reactor. Zhejiang Chemical Industry 50 (7): 29.

38 López-Carpy, B., Saldivar-Guerra, E., Zapata-González, I., and García-Franco, C. (2018). Mathematical modeling of the molecular weight distribution in low density polyethylene. I. Steady-state operation of multizone autoclave reactors. Macromolecular Reaction Engineering 12: 1800013.

39 Aspen Technology, Inc. (2017). Application B4 – styrene ethyl acrylate free radical copolymerization process. Aspen Polymers V8.4: Examples and Applications, pp. 133–146.