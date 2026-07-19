# 2. Selection of Property Methods and Estimation of Physical Properties

<!-- PDF page 89 -->

## Selection of Property Methods and Estimation of Physical Properties for Polymer Process Modeling

This chapter covers the property methods to characterize phase equilibrium and to estimate physical properties in polyolefin manufacturing. We discuss the polymer nonrandom two-liquid (POLYNRTL) activity coefficient model (ACM), and the polymer Sanchez-Lacombe (POLYSL) and polymer perturbed-chain statistical fluid theory (POLYPCSF) equations of state (EOS). We present specific guidelines for the selection of an appropriate polymer ACM or EOS for modeling a specific polyolefin process [1, 2].

This chapter begins by discussing the property methods and parameter requirements in simulating a polymer process (Section 2.1). We then present the polymer ACM, particularly the POLYNRTL ACM, in Section 2.2 and cover a workshop for estimating POLYNRTL binary interaction parameters using UNIFAC in Section 2.3. We discuss the prediction of polymer physical properties using the Van Krevelen group contribution method in Section 2.4 and follow by a workshop to estimate the physical properties of a copolymer in Section 2.5. In Section 2.6, we introduce the POLYSL EOS. Section 2.7 presents a workshop to estimate the property parameters using data regression tool. Section 2.8 introduces the POLYPCSF EOS, and Section 2.9 presents a workshop for regression of property parameters for POLYPCSF EOS. In Section 2.10, we conclude this chapter by discussing the correlation of polyolefin product quality indices, such as melt flow rate or melt index and polymer density. This chapter ends with a reference section.

### 2.1 Property Methods and Thermophysical Parameter Requirements for Process Simulation

Aspen Plus refers to a property method as a collection of models and methods for calculating phase equilibria and various physical properties, such as density, enthalpy, viscosity, and thermal conductivity. We discuss two major categories of property methods, namely the ACMs and EOS, in Sections 2.2–2.9, and provide guidelines on how to choose an appropriate property method for a specific polyolefin process.

Table 2.1 summarizes the key process modeling tasks and the essential thermophysical properties required for completing the tasks. The reader may search the

---

<!-- PDF page 90 -->

<div style="text-align: center;">Table 2.1 Process modeling tasks and essential thermophysical property requirements.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process modeling task</td><td style='text-align: center; word-wrap: break-word;'>Essential thermophysical property requirements</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mass balance</td><td style='text-align: center; word-wrap: break-word;'>Density or standard liquid volume, phase equilibrium</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Energy balance</td><td style='text-align: center; word-wrap: break-word;'>Heat capacity, heat of formation, heat of reaction, heat of vaporization, liquid vapor pressure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Heat transfer</td><td style='text-align: center; word-wrap: break-word;'>Density, heat capacity, thermal conductivity, viscosity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure drop</td><td style='text-align: center; word-wrap: break-word;'>Density, viscosity</td></tr></table>

information within Aspen Plus: Help → Property requirements → Property requirements for mass and energy balance simulations.

We discuss below the two key types of property methods for characterizing the phase equilibrium and estimating the physical properties in polyolefin processes: ACM and EOS.

### 2.2 Polymer Activity Coefficient Models (ACM): Polymer Nonrandom Two-liquid (POLYNRTL) Model

In Chapter 6, we present the modeling of manufacturing processes for polystyrene (PS) using free radical polymerization and poly(styrene-butadiene-styrene) rubber or SBS rubber using ionic polymerization. For both processes, we must account for vapor-liquid equilibrium with a high degree of nonideality in the presence of polar components (such as water) at low to medium pressure (<10 bar), that is away from the critical region [1, 2]. In the discussion below, we follow the explanation in [3–5].

#### 2.2.1 Vapor–Liquid Equilibrium for an Ideal Vapor Phase and a Nonideal Liquid Phase

Figure 2.1 shows a vapor–liquid mixture. We assume that the vapor phase is ideal. The partial pressure of component i in the vapor phase,  $ P_{i} $, is equal to

 $$ P_{i}=x_{i}\gamma_{i}(x_{i},T)P_{i}^{sat}(T)=y_{i}P $$ 

In the equation,  $ x_i $ is the liquid mole fraction of component  $ i $,  $ \gamma_i(x_i, T) $ is the activity coefficient of component  $ i $ as a function of liquid composition  $ x_i $ and temperature  $ T $,  $ P_{sat}(T) $ is the vapor pressure of pure component  $ i $,  $ y_i $ is the vapor mole fraction of component  $ i $, and  $ P $ is the pressure.

For ideal solutions, the partial pressure  $ P_i $ is equal to  $ x_i P_i^{\text{sat}}(T) $ according to Raoult's law [1]. For nonideal solutions, we correct this term by multiplying it with an activity coefficient,  $ \gamma_i(x_i, T) $. For an ideal vapor phase, the partial pressure  $ P_i $ is equal to  $ y_i P $ according to Dalton's law [1].

---

<!-- PDF page 91 -->

<div style="text-align: center;">Figure 2.1 A vapor-liquid mixture.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_578_147_785_361.jpg" alt="Image" width="21%" /></div>


#### 2.2.2 General Vapor–Liquid Equilibrium Relationships Based on Fugacity Coefficient and Liquid-phase Activity Coefficient

Based on Walas [1], we generalize Eq. (2.1) to define the vapor–liquid equilibrium using a gas-phase fugacity coefficient and a liquid-phase activity coefficient:

 $$ x_{i}\Upsilon_{i}f_{i}^{\mathrm{oL}}=y_{i}\varphi_{i}^{V}P=P_{i} $$ 

In the equation,  $ f_i^{OL} $ is the liquid-phase reference fugacity, defined as the fugacity of a pure liquid at the temperature  $ T $ and pressure  $ P $ of the mixture, and  $ \varphi_i^{V} $ is the partial gas-phase fugacity coefficient of component  $ i $ computed from an EOS.

#### 2.2.3 Segment-based Mole Fraction Versus Species-based Mole Fraction

This section follows the discussion in [3]. There are two types of molecular accounting systems that we use to model physical properties and phase equilibrium in polymer-containing systems. Species-based calculations consider polymer chains as single molecules, while segment-based accounting considers every polymer repeat unit (“segment”) as an individual molecule. The segment-based approach can characterize polymer molecules by the chemical properties of segments or monomer units that comprise the polymers. This makes it easier to evaluate the effect of polymer composition on thermodynamic properties. The segment-based approach can also consider the chain length, which is important in the modeling of phase equilibrium and physical properties.

Figure 2.2 illustrates a segment-based representation of polymer chains in a mixture, which permits the consideration of the interaction between each segment type and solvent molecules.

We note that the mole fraction of polymer chains is often of little physical significance. Let us consider a mixture of 1 g high-density polyethylene (HDPE) of a molecular weight 50,000, dissolved in 10 g of n-hexane of molecular weight 86.18. We find the mole fraction of polymer as

 $$ \begin{aligned}x_{polymer}&=(moles polymer)/(moles solvent+moles polymer)\\&=(1/50,000)/[1/86.18+1/50,000]=1.72E-4\\ \end{aligned} $$ 

---

<!-- PDF page 92 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_660_533.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 2.2 A segment-based representation of polymer chains in a mixture.</div>


Now, let us consider the ethylene segment  $ (-C_2H_4- $ $ of a molecular weight of 28.05. An HDPE polymer of a molecular weight of 50,000 corresponds to a degree of polymerization of 50,000/28.05 or 1534.9 segments. We treat each solvent molecule as a single segment. The segment-based mole fraction of polymer is then

 $$ \begin{aligned}X_{polymer}&=(moles polymer segments)/(moles solvent+moles polymer segments)\\&=[(1/50,000)\times1534.9]/[10/28.05+(1/50,000)\times1534.9]\\&=7.93E-2\\ \end{aligned} $$ 

This segment-based mole fraction is more representative of the amount of polymer in the mixture than the species-based mole fraction of the polymer.

In general, we can convert the species-based mole fraction x to a segment-based mole fraction X according to the relationship [5]:

 $$ X_{I}=\frac{x_{i}r_{i,I}}{\sum_{i}\sum_{I}x_{i}r_{i,I}} $$ 

where subscript I refers to polymer segments, subscript i refers to a polymer molecule, and  $ r_{i,I} $ is the number of segment type I in polymer molecule i.

#### 2.2.4 POLYNRTL: Polymer Nonrandom Two-liquid Activity Coefficient Model

In the POLYNRTL model of Chen [4], the Gibbs free energy of mixing of a polymer solution is the sum of (1) the enthalpy of mixing, based on the nonrandom two-liquid (NRTL) theory [5], and (2) the entropy of mixing, based on the Flory–Huggins (F-H) theory [6–8]. The model calculates the activity coefficient as a sum of two

---

<!-- PDF page 93 -->

contributions:

 $$ \ln\gamma_{i}=\ln\gamma_{i}^{\mathrm{NRTL}}+\ln\gamma_{i}^{\mathrm{F-H}} $$ 

where  $ \gamma_{i} $ is the activity coefficient of species i, and superscripts NRTL and F-H represent the NRTL and Flory-Huggins contributions, respectively.

We note that POLYNRTL and many other ACMs ignore a third term in Eq. (2.3), representing the free-volume (FV) or compressibility contribution. Oishi and Prausnitz [9] proposed a UNIFAC-FV model to include the FV contribution. Interested readers may search “UNIFAC free volume model” in Aspen Plus online help to learn more detail about the model, but we do not use the model in this text.

The NRTL activity coefficient contribution is different for polymers (subscript i = p) and solvents (subscript i = s). The relevant expressions are as follows:

 $$ \ln\gamma_{i-P}^{\mathrm{NRTL}}=\sum_{J}r_{P,J}\left[\frac{\sum_{K}X_{K}G_{KJ}\tau_{KJ}}{\sum_{K}X_{K}G_{KJ}}+\sum_{K}\frac{X_{K}G_{JK}}{\sum_{L}X_{L}G_{LK}}\left(\tau_{JK}-\frac{\sum_{L}X_{L}G_{LK}\tau_{LK}}{\sum_{L}X_{L}G_{LK}}\right)\right] $$ 

 $$ \ln\gamma_{i=s}^{\mathrm{NRTL}}=\frac{\sum_{K}X_{K}G_{Ks}\tau_{Ks}}{\sum_{K}X_{K}G_{Ks}}+\sum_{L}\frac{X_{L}G_{sL}}{\sum_{K}X_{K}G_{KL}}\left(\tau_{sL}-\frac{\sum_{K}X_{K}G_{KL}\tau_{KL}}{\sum_{K}X_{K}G_{KL}}\right) $$ 

In the equations,  $ X_K $ is the segment-based mole fraction defined by Eq. (2.3). The parameter  $ G_{IJ} $ relates the overall segment-based mole fractions to the local segment-based mole fractions. It is related to the binary interaction parameter  $ \tau_{ij} $ and the nonrandomness factor  $ \alpha_{ij} $ through the following relationship:

 $$ G_{ij}=\exp(-\alpha_{ij}\tau_{ij}) $$ 

 $ \alpha_{ij} $ has a value between 0.2 and 0.3, and its value has no significant impact on the behavior of the model [5]. The binary interaction parameter  $ \tau_{ij} $ is related to the energy of interaction between species i and j,  $ g_{ij} $, and the energy of interaction between a pair of j species,  $ g_{jj} $, according to

 $$ \tau_{ij}=(g_{ij}-g_{jj})/RT $$ 

This definition suggests that  $ \tau_{ii} $ is zero.

Aspen Plus databanks provide temperature-dependent relationships for both the binary interaction parameters  $ \tau_{ij} $ and the nonrandomness factor  $ \alpha_{ij} $:

 $$ \tau_{ij}=a_{ij}+b_{ij}/T+e_{ij}\ln T+f_{ij}T $$ 

 $$ \alpha_{ij}=c_{ij}+d_{ij}\ (T-273.15) $$ 

The Flory-Huggins contribution in Eq. (2.4) is as follows:

 $$ \ln\gamma_{I}^{\mathrm{FH}}=\ln\left(\frac{\varphi_{I}}{X_{I}}\right)+1-m_{I}\sum_{J}\left(\frac{\varphi_{J}}{m_{J}}\right) $$ 

For a solvent,  $ \varphi_i = X_i $, which is the segment-based mole fraction of the solvent; for a polymer,  $ \varphi_i = X_i $, summed over all the segments.

---

<!-- PDF page 94 -->

<div style="text-align: center;">Table 2.2 POLYNRTL model parameters.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Parameter name/element</td><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Default</td><td style='text-align: center; word-wrap: break-word;'>Unit keyword</td><td style='text-align: center; word-wrap: break-word;'>Comments</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/1</td><td style='text-align: center; word-wrap: break-word;'>$ a_{ij} $ and  $ a_{ji} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Binary, Asymmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/2</td><td style='text-align: center; word-wrap: break-word;'>$ b_{ij} $ and  $ b_{ji} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td><td style='text-align: center; word-wrap: break-word;'>Binary, Asymmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/3</td><td style='text-align: center; word-wrap: break-word;'>$ c_{ij} $</td><td style='text-align: center; word-wrap: break-word;'>0.3</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Binary, Symmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/4</td><td style='text-align: center; word-wrap: break-word;'>$ d_{ij} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/TEMP</td><td style='text-align: center; word-wrap: break-word;'>Binary, Symmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/5</td><td style='text-align: center; word-wrap: break-word;'>$ e_{ij} $ and  $ e_{ji} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Binary, Asymmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/6</td><td style='text-align: center; word-wrap: break-word;'>$ f_{ij} $ and  $ f_{ji} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/TEMP</td><td style='text-align: center; word-wrap: break-word;'>Binary, Asymmetric</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/7</td><td style='text-align: center; word-wrap: break-word;'>$ T_{\text{min}} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td><td style='text-align: center; word-wrap: break-word;'>Unary</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NRTL/8</td><td style='text-align: center; word-wrap: break-word;'>$ T_{\text{max}} $</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td><td style='text-align: center; word-wrap: break-word;'>Unary</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FHSIZE/1</td><td style='text-align: center; word-wrap: break-word;'>$ s_{i} $</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Unary</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FHSIZE/2</td><td style='text-align: center; word-wrap: break-word;'>$ \varepsilon_{i} $</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Unary</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLDP</td><td style='text-align: center; word-wrap: break-word;'>$ P_{i} $</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>—</td><td style='text-align: center; word-wrap: break-word;'>Unary</td></tr></table>

 $ m_{i} $ is the characteristic size of species i. It is related to the degree of polymerization by

 $$ m_{i}=s_{i}\times P_{i}^{\varepsilon i} $$ 

where  $ s_{i} $ and  $ \varepsilon_{i} $ are empirical parameters with default values for both being 1.0 for small molecules.  $ P_{i} $ is the degree of polymerization of species i.

Table 2.2 summarizes the POLYNRTL model parameters. In using the POLYN-RTL model within Aspen Plus, we only need to enter parameters NRTL/1-NRTL/8; Aspen Polymers sets the remaining model parameters to their default values.

#### 2.2.5 Concept of Henry Components for Vapor–Liquid Equilibrium for a Vapor Phase and a Nonideal Liquid Phase Involving Supercritical Components

A serious weakness of ACMs is that they are not accurate in predicting the solubilities of supercritical components in the liquid phase. Those components refer to light gases and low-molecular-weight hydrocarbons, such as  $ H_2 $,  $ O_2 $,  $ N_2 $, CO,  $ CO_2 $,  $ H_2S $,  $ NO_2 $,  $ SO_2 $,  $ CH_4 $,  $ C_2H_4 $,  $ C_2H_6 $,  $ C_3H_6 $, and  $ C_3H_8 $. Refer to Eq. (2.1) for the vapor–liquid equilibrium relationship between an ideal vapor phase and a nonideal liquid phase:

 $$ P_{i}=x_{i}\gamma_{i}(x_{i},T)P_{i}^{sat}(T)=y_{i}P $$ 

For a vapor phase and a nonideal liquid phase involving supercritical components, we modify Eq. (2.1) as

 $$ x_{i}\gamma_{i}^{*}H_{i}=\phi_{i}^{\nu}y_{i}P=P_{i} $$ 

In the equation,  $ \gamma_i^* = \gamma_i / \gamma_\infty $, and  $ \gamma_\infty $ is the infinite-dilution activity coefficient.  $ H_i $ is the Henry's law constant, and  $ \phi_i^\nu $ is the vapor-phase fugacity coefficient.

---

<!-- PDF page 95 -->

calculated by an EOS. For an ideal vapor phase, we choose the ideal gas law as the EOS; for a nonideal gas (such as a gas phase up to medium pressures), we use the Redlich–Kwong–Soave (RKS) EOS, which is a cubic EOS where the product of the pressure p and the third power (cubic) of the volume of the mixture,  $ V_m^3 $, is related to the ideal gas law constant R multiplied by the temperature T of the mixture. Interested reader may search “Redlich–Kwong–Soave” on Aspen Plus online help for details of the RKS EOS.

The Henry’s law constant  $ H_{i} $ is typically correlated as a function of temperature. For a supercritical component i and a solvent A, Aspen Plus uses the following correlation:

 $$ \ln(H_{i,A})=a_{i,A}+b_{i,A}/T+c_{i,A}\ln T+d_{i,A}T+e_{i,A}/T^{2}\qquad T_{L}<T<T_{H} $$ 

Table 2.3 summarizes the Henry's law parameters.

We demonstrate below how to implement the concept of Henry components and compare the resulting concentrations of light gases in the solvent with and without applying Henry's law. Consider a simple two-phase flash problem shown in Figure 2.3 and defined in Table 2.4. We save the simulation file as Example 2.1 NRTL Flash with Henry Component.bkp.

Figure 2.4 illustrates how to specify Henry components: Properties → Components → Henry comps → New: HC-1 → Move H2 and N2 from “Available Components” to “Selected Component.”

<div style="text-align: center;">Table 2.3 Henry's law parameters.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Parameter name/element</td><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Default</td><td style='text-align: center; word-wrap: break-word;'>Unit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/1</td><td style='text-align: center; word-wrap: break-word;'>$ a_{LA} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>—</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/2</td><td style='text-align: center; word-wrap: break-word;'>$ b_{LA} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/3</td><td style='text-align: center; word-wrap: break-word;'>$ c_{LA} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/4</td><td style='text-align: center; word-wrap: break-word;'>$ d_{LA} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/5</td><td style='text-align: center; word-wrap: break-word;'>$ T_{L} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/6</td><td style='text-align: center; word-wrap: break-word;'>$ T_{H} $</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry/7</td><td style='text-align: center; word-wrap: break-word;'>$ e_{LA} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TEMP</td></tr></table>

<div style="text-align: center;">Figure 2.3 A simple flash unit for Example 2.1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_361_1023_798_1260.jpg" alt="Image" width="45%" /></div>


---

<!-- PDF page 96 -->

<div style="text-align: center;">Table 2.4 Specifications of Example 2.1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Components</td><td style='text-align: center; word-wrap: break-word;'>Water,  $ H_{2} $,  $ N_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Property method</td><td style='text-align: center; word-wrap: break-word;'>NRTL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Henry&#x27;s components</td><td style='text-align: center; word-wrap: break-word;'>$ H_{2} $,  $ N_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Feed</td><td style='text-align: center; word-wrap: break-word;'>70 °C, 1 bar, Water (1000 kg/hr),  $ H_{2} $(50 kg/hr),  $ N_{2} $ (50 kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flash drum</td><td style='text-align: center; word-wrap: break-word;'>70 °C, 1 bar</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_384_670_628.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 2.4 Specification of Henry's components, HC-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_697_809_826.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.5 Henry's law parameter values for H2–N2–water mixture.</div>


After defining the Henry components, we can see Henry’s law parameters for both H2 and N2 by following the path: Properties → Methods → Parameters → Binary Interaction → HENRY-1 (see Figure 2.5). Refer to Eq. (2.13) and Table 2.3 for Henry parameters.

Next, we enter the feed stream and flash conditions in Table 2.4. Subsequently, an inexperienced Aspen Plus user may follow the habit of clicking on the “Next” button and seeing a message of “required input complete” and proceed to run the simulation (see Figure 2.6).

This results in the mass fractions of  $ H_{2} $ and  $ N_{2} $ in the LIQUID product being 4.98053E-6 and 5.25986E-5, or 4.98 and 52.5 ppm, respectively (see Figure 2.7). As we show shortly, despite having defined  $ H_{2} $ and  $ N_{2} $ as Henry components, these mass fractions actually result from the NRTL property method without incorporating the Henry's law.

To incorporate Henry’s law into the calculation of the NRTL property method, we must tell Aspen Plus to do so following the path: Property→Methods→

---

<!-- PDF page 97 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_147_699_492.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 2.6 Clicking on the "Next" button, seeing the required input complete and clicking "OK" to run the simulation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_584_757_874.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 2.7 Computed mass fractions of H2 and N2 in the LIQUID product without incorporating Henry's law into the NRTL property method.</div>


Specification → Henry components → HC-1 defined in Figure 2.3. We illustrate this step in Figure 2.8.

Running the simulation again, we see in Figure 2.9 the resulting mass fractions of H2 and N2 in the LIQUID product being 9.47979E-7 and 6.16813E-7 or 0.948 and 0.617 ppm, respectively (compared to the incorrect values of 4.98 and 52.5 ppm in Figure 2.7). The significant difference demonstrates the importance of correctly including Henry components into the NRTL property method. This observation applies to the POLYNRTL property method as well.

To summarize, the POLYNRTL method is applicable to polyolefin processes involving a highly nonideal liquid phase (with polar and hydrogen-bonding species) up to medium pressures of approximately 10 bar. It must be used with Henry's law when the mixture contains light gases and low-molecular-weight hydrocarbons.

---

<!-- PDF page 98 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_599_287.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 2.8 Including Henry components HC-1 into the NRTL property method.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_356_806_677.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.9 Computed mass fractions of H2 and N2 in the LIQUID product after incorporating Henry's law into the NRTL property method.</div>


Two typical processes are polystyrene (PS) using free radical polymerization and poly(styrene-butadiene-styrene) rubber or SBS rubber using ionic polymerization discussed in Chapter 6. For nonpolyolefin systems, we apply the POLYNRTL method to Nylon, PET (polyethylene terephthalate), PLA (polylactic acid), etc. for step-growth polymerization processes [3].

##### 2.3 Workshop 2.1. Estimating POLYNRTL Binary Parameters Using UNIFAC

#### 2.3.1 Objective

The UNIFAC (UNIQUAC Functional-group Activity Coefficients) method [10, 11] is a semiempirical system for the prediction of nonelectrolyte activity in nonideal mixtures. Over the years, there have been numerous articles and books extending the method to more complex vapor–liquid mixtures. The UNIFAC method attempts to break down the problem of predicting interactions between molecules by describing molecular interactions based on functional groups, such as functional groups 1005 (>CH-), 1100 (>CH2), 1015 (-CH3), and 2400 (CH2SH), attached to the molecule. A search of Aspen Plus online help for “UNIFAC Functional Groups”

---

<!-- PDF page 99 -->

will give Tables 3.12–3.21 of the functional groups available within Aspen Plus. This workshop demonstrates how to use UNIFAC to estimate POLYNTRL binary parameters.

#### 2.3.2 Estimating POLYNRTL Binary Parameters Using UNIFAC for Polystyrene Manufacturing

Figure 2.10 shows some of the components involved in polystyrene manufacturing, where Sty and STY-SEG are styrene (monomer) and styrene segment (repeat unit), and EB (ethyl benzene) and DDM (n-dodecyl mercaptan) are chain-transfer agents. We save the simulation file as WS2.1 Estimating POLYNRTL Binary Parameters Using UNIFAC.bkp.

If a component is present in the Aspen Enterprise Database for pure components and segments, we will see its structure being displayed within the “Molecular Structure” folder, as illustrated in Figure 2.11 for DDM (C12H26S). Additionally, Aspen Plus will automatically complete a representation of the displayed structure as a combination of UNIFAC functional groups, that is C12H26S = H3C-(CH2)10-CH2SH = 1*(Group 1015, H3C) +10*(Group 1100, CH2) +1*(Group 2400, CH2SH). In fact, Aspen Plus will do this for all specified components that are present in the Aspen Enterprise Database, which will enable the use of UNIFAC group-contribution method to estimate the binary parameters.

We see a “Draw/Import/Edit” button in Figure 2.11. In Section 4.4.3, we show how to import a molecular structure file, *.mol, from the Internet (such as Chemical Book, www.chemicalbook.com) for a component not available within Aspen

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_769_662_941.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 2.10 Component specifications for WS 2.1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1007_662_1202.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 2.11 A graphical structure of DDM (n-dodecyl mercaptan) available in the Aspen Enterprise Database.</div>


---

<!-- PDF page 100 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_692_391.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 2.12 Specification to estimate binary interaction parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_460_804_594.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.13 Specification of binary interaction parameters to be estimated.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_657_788_852.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 2.14 Estimated binary interaction parameters.</div>


Enterprise Database. In Section 6.1.4, we also demonstrate how to use the drawing tools within Aspen Plus to draw a molecular structure.

Next, we follow the path: Properties → Estimation → Input → (1) Estimation Option → Estimate only the selected parameters; (2) Parameter type → Binary interaction parameters (see Figure 2.12).

In Figure 2.13, we click on the “New” button and then choose the parameter “NRTL” and method “UNIFAC.” We can specify component i (STYRENE) and component j (STY-SEG) and other i-j component combination one by one. However, this is not necessary; by choosing “ALL” for both components i and j, Aspen Plus will estimate the interaction parameters for all binary component combinations for us.

We then run the property estimation. Figure 2.14 shows the estimated binary interaction parameters, according to Eqs. (2.9) and (2.10) and Table 2.2. We save the simulation file as WS 2.1 Estimating Binary Parameters Using UNIFAC.bkp.

---

<!-- PDF page 101 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_771_317.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.15 Entering the estimated binary interaction parameters to the “parameters” form.</div>


Additionally, by following the path Properties → Methods → Parameters → Binary Interaction → NRTL-1, we also see the estimated parameters being entered as the result (R) of the Physical Constant Estimation System (PCES), that is R-PCES (see Figure 2.15).

### 2.4 Prediction of Polymer Physical Properties by Van Krevelen Functional Group Method

As we discussed vapor–liquid equilibrium according to Eq. (2.12), the POLYNRTL property method uses the POLYNRTL ACM for the liquid phase and applies the RKS (Redlich–Kwong–Soave) [12] cubic EOS for the vapor phase. For property calculations, the POLYNRTL property method uses Van Krevelen functional group method to predict the physical properties of polymers.

The Van Krevelen method is based on the chemical structure of the polymers [13]. Table 2.5 summarizes the key concepts of applying the Van Krevelen method.

<div style="text-align: center;">Table 2.5 Applying the Van Krevelen method to estimate properties of a system containing polymers by going from functional groups to segments and then to polymer mixture.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">-CH2-</td><td rowspan="2">Functional group (Van Krevelen; VK)</td><td style='text-align: center; word-wrap: break-word;'>Estimate segment properties using properties of the functional groups making up the segment(s), e.g. heat capacity  $ C_{p} $,  $ C_{p} = \sum_{k} n_{k} C_{p,k} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k refers to the  $ k $th functional group;  $ n_{k} $ is the number of the  $ k $th functional group. When retrieving the segments from the SEGMENT databank, there is no need to supply functional groups. Otherwise, define the segments based on the VK functional groups.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-CH2-CH2-</td><td style='text-align: center; word-wrap: break-word;'>Segment (ethylene)</td><td style='text-align: center; word-wrap: break-word;'>Calculate polymer properties from segment properties, number-average degree of polymerization, and segment composition.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-CH2-CH2-CH2-CH2-</td><td style='text-align: center; word-wrap: break-word;'>Polymer (polyethylene)</td><td style='text-align: center; word-wrap: break-word;'>Find the mixture properties of the whole component system (polymer, monomer, solvents, etc.).</td></tr></table>

---

<!-- PDF page 102 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Temperature</th><th style='text-align: center;'>Liquid V_i</th><th style='text-align: center;'>Amorphous V_c</th><th style='text-align: center;'>Glassy V_g</th><th style='text-align: center;'>Semi-Crystalline V_c</th><th style='text-align: center;'>Crystalline V_c</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T_g</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T_m</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.16 Molar volume versus temperature for different physical states of a polymer.</div>


A search of the online help of Aspen Plus for “Thermophysical Properties of Polymers” will show the large number of polymer properties that we can estimate by the Van Krevelen method.

Let us illustrate the concept of the Van Krevelen method by considering the molar volume of a polymeric component, which depends on the temperature and the physical state of the polymer. Figure 2.16 shows a plot of the molar volume versus temperature of a polymer at different physical states. In Figure 2.16,  $ V_1 $ refers to the molar volume of a polymer liquid,  $ V_c $ indicates the molar volume of a crystalline polymer, and  $ V_g $ represents the molar volume of an amorphous glassy polymer.  $ X_c $ represents the mass fraction of a crystalline polymer.  $ T_g $ and  $ T_m $ are, respectively, the glass transition temperature and the melting transition temperature. These volume and temperature concepts are well explained in most introductory polymer textbooks [14].

The basic idea of a group contribution method for estimating the physical properties of polymers is to calculate the sum of contributions of the constituents (the structural and functional groups) as an approximation. Consider, for example, finding the molar density of a propylene repeat segment illustrated in Figure 2.17.



<div style="text-align: center;"><img src="imgs/img_in_image_box_724_815_829_863.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;">Figure 2.17 A propylene repeat segment C3H6-R.</div>


The molecular weight of this structural unit is 42.08 g/mol. From Table 4.5 in Van Krevelen and te Nijenhuis [13], we know that the Van der Waals volume ( $ V_w $) contribution of Van Krevelen functional group 100,  $ -CH_2- $, at 25°C is 16.1 cm $ ^3 $/mol, and that of group 101,  $ -CH(CH_3)_2 $, is 33.2 cm $ ^3 $/mol. The additive sum of both volume contributions is 49.3 cm $ ^3 $/mol. Therefore, the molar density of a propylene repeat segment at 25°C is [42.08 g/mol]/[49.3 cm $ ^3 $/mol] or 0.85 g/cm $ ^3 $. This value is in perfect agreement with the experimental value [13]. We note, however, that not every property prediction by the Van Krevelen method matches perfectly with the experimental data.

When we cannot neglect the interactions between functional and structural groups, the Van Krevelen method includes correction terms for the interactions. The resulting models are called group interaction models [13]. Interested

---

<!-- PDF page 103 -->

readers can find additional details about the Van Krevelen method for estimating physical properties by searching Aspen Plus online help for “Van Krevelen group contribution methods.”

##### 2.5 Workshop 2.2. Estimating the Physical Properties of a Copolymer Using the Van Krevelen Group Contribution Method

#### 2.5.1 Objective

This workshop demonstrates the procedure of applying the Van Krevelen group contribution method to estimate the physical properties of a copolymer. These properties include CP (heat capacity), K (thermal conductivity), MU (viscosity), RHO (density), TG (glass transition temperature), and TM (melting transition temperature). We use styrene-butadiene rubber (SBR) that we will discuss in more detail in Chapter 6 as our copolymer and assume the copolymer with a number-average degree of polymerization (DPN) of 2000. We study the flash operation of an SB copolymer consisting of 50% by mole styrene and 50% by mole butadiene at 250° and 1.01325 bar. We assume that the mass flow rates of the styrene, butadiene, and SB copolymer are identical, each at 10 kg/hr.

We show how to apply the Van Krevelen method according to the following steps: (1) draw the process flowsheet; (2) specify the unit set and global options; (3) define components, segments, and polymer and characterize their structures; (4) choose property method and enter or estimate the property parameters; (5) define streams and blocks; (6) create property sets; (7) define property analysis runs to create property tables; and (8) run the simulation, examining the results, and make property plots.

#### 2.5.2 Draw the Process Flowsheet and Specify the Unit Set and Global Options

Our simple flash unit is the same as in Figure 2.3. We choose the unit set METCBAR in Setup in both Properties and Simulation, as demonstrated previously in Figure 1.7. For global options, we follow the path: Simulation → Setup → Global settings → Flow basis: choose “Mass” (see Figure 1.6).

#### 2.5.3 Define Components, Segments, and Polymer and Characterize Their Structures

Figure 2.18 shows our component specifications. We note two points: (1) We purposely do not specify the component name and alias (chemical formula) of the styrene segment, STY-SEG, as we want to demonstrate how to use Van Krevelen functional groups to specify this segment; (2) We specify the styrene-butadiene copolymer with a number-average degree of polymerization, DPN, defined in Eqs. (1.5) and (1.11), of 2000, as a “generic polymer component” with an alias “polymer.”

---

<!-- PDF page 104 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_644_359.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 2.18 Component specifications.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_422_764_604.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 2.19 Choosing the built-in “Properties selection” attribute group.</div>


To characterize the polymer component, we follow the path:

Properties → Components → Polymer → Segments → Segment definition: Choose "Repeat" unit for both STY-SEG and BUT-SEG. Figure 2.19 shows our selection of the built-in polymer attributes for "Properties Selection" for our SB copolymer. See Figure 1.19. We have previously explained all the selected attributes in Sections 1.3.2 and 1.3.3.

Next, we check the path: Properties → Components → Molecular structure → Structural and functional groups and note that segment BUT-SEG and pure components BUTADIEN and STYRENE are available within Aspen Plus segment and component databanks, and we see their structures being displayed. We do not need the structure of the generic polymer component, SB copolymer, but we need to specify the structure of the segment STY-SEG, as shown in Figure 2.20.



<div style="text-align: center;"><img src="imgs/img_in_image_box_727_818_829_906.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;">Figure 2.20 Structure of STY-SEGA.</div>


A search of Aspen Plus online help on “Van Krevelen Functional Group Parameters” shows that we can represent STY-SEG as a sum of three Van Krevelen (VK) functional groups: (1) VK group 100,  $ -CH_{2}- $; (2) VK group 131,  $ >CH- $; and (3) VK group 146, benzyl group. We specify these groups according to Figure 2.21.

#### 2.5.4 Choosing Property Method and Entering or Estimating Property Parameters

We choose the POLYNRTL property method for the current problem, as in our detailed styrene-butadiene rubber (SBR) workshop in Chapter 6. Following exactly Workshop 2.1, Section 2.6, we estimate all missing binary interaction parameters. Figure 2.22 shows the estimated binary parameters.

---

<!-- PDF page 105 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_778_462.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.21 Specifications of Van Krevelen functional groups for STY-SEG.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_561_779_761.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.22 Estimated binary interaction parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_858_779_1075.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.23 Specification of feed stream with component attributes SFRAC, SFLOW, and DPN for the generic polymer component, SB copolymer.</div>


#### 2.5.5 Specifications of Feed Stream and Flash Block

Figure 2.23 shows the specification of feed stream. Under component attributes, we need to specify the SFRAC, SFLOW, and DPN for SB copolymer.

For the flash unit, we enter a temperature of  $ 250^{\circ} $C and a pressure of 1.01325 bar.

---

<!-- PDF page 106 -->

#### 2.5.6 Creating Property Sets

A property set is a collection of thermodynamic, transport, and other properties that we can use in stream reports, physical property tables and analysis, heating and cooling curves of unit operation models (e.g. exchanger, condenser, and reboiler), distillation column stage property reports, reactor temperature profiles, etc.

We create a property set to display the property values that we find from a physical property analysis. We define a property set in either the Properties or Simulation environment, and the resulting property set will appear in both environments. We follow the path: Properties → Property sets → New; name- PS-1 → Properties and Qualifiers (see Figures 2.24 and 2.25). Note the pull-down menu of the physical properties and the corresponding units for the user to choose. We include CP (heat capacity), K (thermal conductivity), MU (viscosity), RHO (density), TG (glass transition temperature), and TM (melting transition temperature) in the property set.

To ensure that the stream report from our flash unit includes values of the specified properties in the property set PS-1, we follow the path: Simulation → Setup → Report Options → Streams → Click on “Property Sets” button → Property Sets: Move PS-1 from Available property sets to Selected property sets → Close (see Figure 2.26).

#### 2.5.7 Defining Property Analysis Run to Create Property Tables

We can use property analysis tool to generate tables and plots of physical properties of pure components and mixtures as a function of temperature, pressure, and

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_731_644_951.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 2.24 Including physical properties in the property set PS-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1014_645_1224.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 2.25 Qualifiers for selected properties in the property set.</div>


---

<!-- PDF page 107 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_148_779_447.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.26 Including specified property set PS-1 in the stream report.</div>


composition. We should emphasize that both property analysis and regression tools in Aspen Plus do not support polymer attributes. Therefore, for property analysis and regression runs, we should define a polymer as an oligomer. By doing so, we eliminate the need to enter any attribute information. We should specify its number of repeat units or segments, segment composition (following the path:

Components → Polymers → Characterization → Oligomers → Oligomer Structure → Fill in the number of repeat units), and degree of polymerization. Alternatively, as in the current example, we specify the SB copolymer as a generic polymer component with an alias “polymer” and specify its attributes, particularly segment composition by SFRAC and its degree of polymerization (see Figures 2.18 and 2.23).

We create an analysis of stream properties by following the path: Process flowsheet → Right-click the name of FEED stream Choose "Analysis" on the pull-down menu → Choose analysis type, "Stream Properties." See Figures 2.27 and 2.28. We then click on the "Run Analysis" button in Figure 2.28 to do stream property analysis. When the analysis is completed, we click on the "Results" button displayed in Figure 2.28 and follow the same approach as in Figures 1.22 and 1.23 to make a "custom" plot of properties (CP, K, MU, and RHO) versus temperature. Figures 2.29 and 2.30 illustrate the resulting plots of thermal conductivity and

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1026_737_1222.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 2.27 Initiating an analysis of stream properties for FEED stream.</div>


---

<!-- PDF page 108 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_161_809_525.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.28 Specification of stream property analysis (SPROP-1).</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>SNP</th><th style='text-align: center;'>100</th><th style='text-align: center;'>200</th><th style='text-align: center;'>300</th><th style='text-align: center;'>400</th><th style='text-align: center;'>500</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.29 Thermal conductivity (K) of styrene, butadiene, and SB copolymer versus temperature.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>C</th><th style='text-align: center;'>SPRO-1 (MOST) Results</th><th style='text-align: center;'>SPRO-1 (DREAM) Results</th><th style='text-align: center;'>SPRO-1 (DREAM) Results</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>940</td><td style='text-align: center;'>940</td><td style='text-align: center;'>940</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>930</td><td style='text-align: center;'>930</td><td style='text-align: center;'>930</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>920</td><td style='text-align: center;'>920</td><td style='text-align: center;'>920</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>910</td><td style='text-align: center;'>910</td><td style='text-align: center;'>910</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>890</td><td style='text-align: center;'>890</td><td style='text-align: center;'>890</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>880</td><td style='text-align: center;'>880</td><td style='text-align: center;'>880</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>870</td><td style='text-align: center;'>870</td><td style='text-align: center;'>870</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>860</td><td style='text-align: center;'>860</td><td style='text-align: center;'>860</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>840</td><td style='text-align: center;'>840</td><td style='text-align: center;'>840</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>830</td><td style='text-align: center;'>830</td><td style='text-align: center;'>830</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>820</td><td style='text-align: center;'>820</td><td style='text-align: center;'>820</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>810</td><td style='text-align: center;'>810</td><td style='text-align: center;'>810</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>790</td><td style='text-align: center;'>790</td><td style='text-align: center;'>790</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>780</td><td style='text-align: center;'>780</td><td style='text-align: center;'>780</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>770</td><td style='text-align: center;'>770</td><td style='text-align: center;'>770</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>760</td><td style='text-align: center;'>760</td><td style='text-align: center;'>760</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>740</td><td style='text-align: center;'>740</td><td style='text-align: center;'>740</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>730</td><td style='text-align: center;'>730</td><td style='text-align: center;'>730</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>720</td><td style='text-align: center;'>720</td><td style='text-align: center;'>720</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>710</td><td style='text-align: center;'>710</td><td style='text-align: center;'>710</td></tr>
    <tr><td style='text-align: center;'>185</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>690</td><td style='text-align: center;'>690</td><td style='text-align: center;'>690</td></tr>
    <tr><td style='text-align: center;'>195</td><td style='text-align: center;'>680</td><td style='text-align: center;'>680</td><td style='text-align: center;'>680</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>670</td><td style='text-align: center;'>670</td><td style='text-align: center;'>670</td></tr>
    <tr><td style='text-align: center;'>205</td><td style='text-align: center;'>660</td><td style='text-align: center;'>660</td><td style='text-align: center;'>660</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>215</td><td style='text-align: center;'>640</td><td style='text-align: center;'>640</td><td style='text-align: center;'>640</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>630</td><td style='text-align: center;'>630</td><td style='text-align: center;'>630</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>620</td><td style='text-align: center;'>620</td><td style='text-align: center;'>620</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>610</td><td style='text-align: center;'>610</td><td style='text-align: center;'>610</td></tr>
    <tr><td style='text-align: center;'>235</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>590</td><td style='text-align: center;'>590</td><td style='text-align: center;'>590</td></tr>
    <tr><td style='text-align: center;'>245</td><td style='text-align: center;'>580</td><td style='text-align: center;'>580</td><td style='text-align: center;'>580</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>570</td><td style='text-align: center;'>570</td><td style='text-align: center;'>570</td></tr>
    <tr><td style='text-align: center;'>255</td><td style='text-align: center;'>560</td><td style='text-align: center;'>560</td><td style='text-align: center;'>560</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td></tr>
    <tr><td style='text-align: center;'>265</td><td style='text-align: center;'>540</td><td style='text-align: center;'>540</td><td style='text-align: center;'>540</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>530</td><td style='text-align: center;'>530</td><td style='text-align: center;'>530</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>520</td><td style='text-align: center;'>520</td><td style='text-align: center;'>520</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>510</td><td style='text-align: center;'>510</td><td style='text-align: center;'>510</td></tr>
    <tr><td style='text-align: center;'>285</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>490</td><td style='text-align: center;'>490</td><td style='text-align: center;'>490</td></tr>
    <tr><td style='text-align: center;'>295</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>470</td><td style='text-align: center;'>470</td><td style='text-align: center;'>470</td></tr>
    <tr><td style='text-align: center;'>305</td><td style='text-align: center;'>460</td><td style='text-align: center;'>460</td><td style='text-align: center;'>460</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td></tr>
    <tr><td style='text-align: center;'>315</td><td style='text-align: center;'>440</td><td style='text-align: center;'>440</td><td style='text-align: center;'>440</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>430</td><td style='text-align: center;'>430</td><td style='text-align: center;'>430</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>420</td><td style='text-align: center;'>420</td><td style='text-align: center;'>420</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>410</td><td style='text-align: center;'>410</td><td style='text-align: center;'>410</td></tr>
    <tr><td style='text-align: center;'>335</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>390</td><td style='text-align: center;'>390</td><td style='text-align: center;'>390</td></tr>
    <tr><td style='text-align: center;'>345</td><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>370</td><td style='text-align: center;'>370</td><td style='text-align: center;'>370</td></tr>
    <tr><td style='text-align: center;'>355</td><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td></tr>
    <tr><td style='text-align: center;'>365</td><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>330</td><td style='text-align: center;'>330</td><td style='text-align: center;'>330</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>310</td><td style='text-align: center;'>310</td><td style='text-align: center;'>310</td></tr>
    <tr><td style='text-align: center;'>385</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>290</td><td style='text-align: center;'>290</td><td style='text-align: center;'>290</td></tr>
    <tr><td style='text-align: center;'>395</td><td style='text-align: center;'>280</td><td style='text-align: center;'>280</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>270</td><td style='text-align: center;'>270</td><td style='text-align: center;'>270</td></tr>
    <tr><td style='text-align: center;'>405</td><td style='text-align: center;'>260</td><td style='text-align: center;'>260</td><td style='text-align: center;'>260</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>415</td><td style='text-align: center;'>240</td><td style='text-align: center;'>240</td><td style='text-align: center;'>240</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>230</td><td style='text-align: center;'>230</td><td style='text-align: center;'>230</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>210</td><td style='text-align: center;'>210</td><td style='text-align: center;'>210</td></tr>
    <tr><td style='text-align: center;'>435</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td></tr>
    <tr><td style='text-align: center;'>445</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td></tr>
    <tr><td style='text-align: center;'>455</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>465</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td></tr>
    <tr><td style='text-align: center;'>485</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>495</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>505</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>515</td><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>535</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.30 Mass density (RHO) of styrene, butadiene, and SB copolymer versus temperature.</div>


---

<!-- PDF page 109 -->

mass density versus temperature. The tabulated analysis results also show that the glass transition temperature and the melt transition temperature of the SB copolymer are 45.3472 and 225.23°C, respectively. This concludes the current workshop. We save the simulation file as WS 2.2 Estimating Physical Properties of a Copolymer Using VK Group Contribution Method. bkp.

### 2.6 Polymer Sanchez–Lacombe Equation of State (POLYSL)

To simulate the polyolefin processes at high pressures, ACMs, such as POLYNRTL, suffer from some weaknesses, as most of them are applicable only to incompressible liquid solutions. Additionally, ACMs fail to predict correctly the phase behavior of polymer solutions at the lower critical solution temperature (LCST) below which the components of a mixture are miscible for all compositions. ACMs also fail to predict an upper bound to a temperature interval of partial miscibility called the upper critical solution temperature (UCST). By contrast, an EOS can accurately represent the relationship among temperature, pressure, volume (or density), and composition of a vapor-liquid or vapor-liquid-liquid mixture over the entire fluid region. EOS models can evaluate the physical properties of any fluid phase, liquid and/or vapor at medium to high pressures, as long as the fluid mixture does not contain any polar components. References  $ [15, 16] $ reviewed the development of EOSs for mixtures involving pure components, oligomers, and polymers.

Two of the most useful EOSs for modeling polyolefin processes are (1) POLYSL EOS [17–20] and (2) POLYPCSF EOS [21–23], an extension of the statistical fluid theory (SAFT) EOS [24–26]. We discuss the POLYSL EOS below.

The Sanchez-Lacombe EOS is known as a lattice-gas model since the P-V-T properties of a pure component are calculated assuming that the component is broken into parts or “mers” that are placed into a lattice and are allowed to interact with a mean-field-type intermolecular potential [20]. The Sanchez-Lacombe EOS for pure fluids is

 $$ \tilde{\rho}^{2}+\tilde{P}+\tilde{T}\left[\ln(1-\tilde{\rho})+\left(1-\frac{1}{m}\right)\tilde{\rho}\right]=0 $$ 

where

 $$ \tilde{T}=\frac{T}{T^{*}}\tilde{P}=\frac{P}{P^{*}}\tilde{\rho}=\frac{\rho}{\rho^{*}} $$ 

with

 $$ T^{*}=\frac{\varepsilon^{*}}{k}\ P^{*}=\frac{\varepsilon^{*}}{\nu^{*}}\ \rho^{*}=\frac{M}{mv^{*}} $$ 

In these equations, $T$ is the absolute temperature (K), $P$ is pressure (bar), $\rho$ is density (kg/m$^3$), $\tilde{T}$, $\tilde{P}$, and $\tilde{\rho}$ are the reduced temperature, pressure, and density, respectively, $T^*(\mathrm{K})$, $P^*(\mathrm{bar})$, and $\rho^*(\mathrm{kg/m^3})$ are the scale factors that are independent of the molecular size of the polymer, $\varepsilon^*$ is a characteristic interaction energy per segment, $k$ is the Boltzmann constant, which is a proportionality constant

---

<!-- PDF page 110 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_809_265.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.31 Entering unary or pure component parameters of the POLYSL EOS for simulating an HDPE process.</div>


between the quantities temperature (with unit kelvin) and energy (with unit joule), with a value of 1.380649E-23 J/K,  $ v^{*} $ is the closed-packed volume of a segment, M is the molecular weight, and m is the number of segments per chain.

We typically determine the scale factors,  $ T^*(\text{K}) $,  $ P^*(\text{bar}) $, and  $ \rho^*(\text{kg}/\text{m}^3) $, from regressing experimental data, such as vapor-pressure data for conventional components and liquid-volume data for polymer species. We demonstrate how to do this in Workshop 2.3, Section 2.3. A search of “Sanchez-Lacombe unary parameters” in Aspen Plus online help gives the values of these unary parameters for many polymers, solvents, and monomers, and several published articles also give the regressed unary parameters for selected segments in simulating HDPE, LDPE, and LLDPE processes [27–30]. Figure 2.31 gives examples of POLYSL unary (or pure component) parameters for simulating a slurry HDPE copolymerization process [27]. In Figure 2.31, TICL4 and TEAL (triethyl aluminum) are catalyst and cocatalyst; CH4, C2H6, and N2 are impurities; C2H4 and C4H8 are monomer and comonomer; R-C2H4 and R-C4H8 are ethylene and 1-butene segments; and H2 is the chain-transfer agent. To enter these parameter values, we follow the path: Properties → Methods → Parameters → Pure Components → New: name = PURE-1 → Parameters: SLTSTR, SLPSTR, and SLRSTR and enter the values. For those species with missing unary parameters, Aspen Plus online help suggests using the values: SLTSTR = 415 K, SLPSTR = 3000 bar, and SLRSTR = 736 kmol/cum (which must be converted to a mass-based unit with the molecular weight of the component).

To apply the POLYSL EOS to mixtures, the model parameters become composition dependent through the following mixing rules. The mixing rule for the characteristic closed-packed molar volume of “mers” (that is, the broken parts of a component within a lattice [20]) of the mixture,  $ v_{mix}^{*} $, is

 $$ v^{*}_{\mathrm{mix}}=\sum_{i}\sum_{j}\varphi_{i}\varphi_{j}v^{*}_{ij} $$ 

with

 $$ \nu_{ij}^{*}=\frac{1}{2}\left[\nu_{ii}^{*}+\nu_{jj}^{*}\right](1-\eta_{ij}) $$ 

where the binary interaction parameter  $ \eta_{ij} $ (called parameter SLETIJ-1 within Aspen Plus) corrects for deviations from arithmetic mean and subscripts i and j are the components in the solution mixture. The segment fraction of component i,  $ \varphi_i $, is defined as

---

<!-- PDF page 111 -->

 $$ \varphi_{i}=\frac{\frac{w_{i}}{\rho_{i}^{*}v_{i}^{*}}}{\sum_{j}\left(\frac{w_{j}}{\rho_{j}^{*}v_{j}^{*}}\right)} $$ 

where  $ w_i $ is the mass fraction of component  $ i $ in the mixture, and  $ \rho_j $ and  $ v_j $ are the characteristic mass density and closed-packed molar volume of component  $ j $, respectively. The mixing rule for the characteristic interaction energy for the mixture,  $ \varepsilon_{\text{mix}}^{*} $, is

 $$ \varepsilon_{\mathrm{mix}}^{*}=\frac{1}{\nu_{\mathrm{mix}}^{*}}\sum_{i}\sum_{j}\varphi_{i}\varphi_{j}\varepsilon_{ij}^{*}\nu_{ij}^{*} $$ 

with

 $$ \varepsilon_{ij}^{*}=\sqrt{\varepsilon_{ii}^{*}\varepsilon_{jj}^{*}}(1-k_{ij}) $$ 

where  $ \varepsilon_{ii}^{*} $ and  $ \varepsilon_{jj}^{*} $ are the characteristic interaction energies between different broken parts of a component within a lattice (called mer–mer interaction in [20]) for components i and j. The binary interaction parameter  $ k_{ij} $ (called parameter SLKIJ-1 within Aspen Plus) accounts for specific binary interactions between components i and j. Lastly, the mixing rule for the number of sites occupied by a molecule of the mixture,  $ r_{mix} $, is given by

 $$ \frac{1}{r_{mix}}=\sum_{j}\frac{\varphi_{j}}{r_{j}} $$ 

where  $ r_{j} $ is the number of site molecule j occupies in the lattice, and  $ \varphi_{j} $ is the segment fraction of component j, defined previously in Eq. (2.20).

Binary interaction parameters  $ k_{ij} $ and  $ \eta_{ij} $ are typically correlated as a function of reduced temperature,  $ T_r = T/T_{ref} $ where  $ T_{ref} = 298.15 \, K $:

 $$ k_{ij}=a_{ij}+\mathrm{^{b}_{i j}/}_{T_{r}}+c_{ij}\ln T_{r}+d_{ij}T_{r}+e_{ij}T_{r}^{2} $$ 

 $$ \eta_{ij}=a^{\prime}_{ij}+b^{\prime}_{ij}/_{T_{r}}+c^{\prime}_{ij}\ln T_{r}+d^{\prime}_{ij}T_{r}+e^{\prime}_{ij}T^{2}_{r} $$ 

Figures 2.32 and 2.33 show the values of binary interaction parameters  $ k_{ij} $ and  $ \eta_{ij} $ for simulating an HDPE process [27]. To enter these values within Aspen Plus, follow the path:

<div style="text-align: center;">Figure 2.32 Binary interaction on parameters  $ k_{ij} $ for simulating an HDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_366_1028_796_1264.jpg" alt="Image" width="44%" /></div>


---

<!-- PDF page 112 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_148_594_382.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">Figure 2.33 Binary interaction on parameters  $ \eta_{ij} $ for simulating an HDPE process.</div>


<div style="text-align: center;">Properties → Methods → Parameters → Binary Interaction → New → Name: SLKIJ-1 → Enter the values (do the same for SLITIJ-1).</div>


##### 2.7 Workshop 2.3. Estimating Property Parameters Using Data Regression Tool

#### 2.7.1 Objective

This workshop demonstrates how to use the data regression (DRS) tool to identify the pure component parameters and binary interaction parameters of an EOS model based on component liquid density data and binary vapor–liquid equilibrium (VLE) data (two of the most commonly used property data for property parameter regression). We use the example of a slurry HDPE process [27].

We show how to apply the DRS tool according to the following steps: (1) define a DRS run; (2) specify the unit set and global options; (3) define components, segments, oligomers, and polymer, making sure to define a polymer as an oligomer; (4) choose property method and enter known property parameters from Aspen enterprise databanks; (5) enter experimental data; (6) specify a regression run and physical property parameters to be regressed (7) running the simulation, examining the results and compare the model predictions with experimental data.

#### 2.7.2 Defining a DRS Run

We begin by creating a data regression run and save the simulation file as WS2.3. Estimating Property Parameters Using Data Regression Tool.bkp. We choose a data regression in the run mode section from the toolbar at the top of the screen, as highlighted in Figure 2.34.

#### 2.7.3 Specifying a Unit Set and Global Options

We define a unit set named DRS by copying most units from the unit set, SI, but change the pressure unit to Bar. Following Figure 1.6, we specify a global option of using a mass-based flow rate according to the path: Simulation→Setup→Specifications→Global→Global settings→Flow basis: mass.

---

<!-- PDF page 113 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_734_399.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 2.34 Creating a data regression run.</div>


#### 2.7.4 Defining Components, Segments, Oligomers, and Polymer

Figure 2.35 shows the same component specifications for a commercial slurry HDPE process that we will simulate in detail in Chapter 5 [27]. We repeat the important information presented previously in Section 1.3 and emphasize that both property analysis and regression tools in Aspen Plus do not support polymer attributes. Therefore, for property analysis and regression runs, we should define a polymer as an oligomer. By doing so, we eliminate the need to enter any attribute information.

In Figure 2.35, LP refers to an oligomer product; R-C2H4 and R-C3H6 are ethylene and propylene segments; C2H4 and C3H6 are monomer and comonomer; hexane (HX) is a solvent; H2 is the chain-transfer agent; CH4, C2H6, C4H10, and C3H8 are impurities; and N2 is an inert gas.

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_828_777_1220.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.35 Component specifications for data regression of an HDPE process.</div>


---

<!-- PDF page 114 -->

We note that except for HDPE and LP, Aspen Plus automatically fills in the molecular structures for other components that appear in the enterprise databases for pure components and segments. See Properties→Components→Molecular Structure→Choose component name→Structural and functional group→Graphical structure.

We quantify both HDPE and LP by following the path:

Properties → Components → Polymers → Segments: Set both segments R-C2H4 and R-C3H6 as repeat unit; Oligomers: Assume HDPE and LP to have 1500 and 16 repeat segments. Note that the exact number of repeated segments for HDPE does not affect the regression results.

#### 2.7.5 Choose Property Method and Enter Known Property Parameters from Aspen Enterprise Databanks

Clicking on the “Review” button at the bottom of Figure 2.35 will ask Aspen Plus to call up all the relevant pure component parameters from the enterprise databanks for pure components, segments, and polymers. For example, Figure 2.36 shows the resulting listing of pure component parameters (both scalar and temperature dependent) provided by the databanks. Figure 2.36 displays the parameters for the ideal gas heat capacity from the segment databank, DB-SEGMET. To see the specific form of any temperature-dependent parameter correlation, such as CPG, click the “Help” button in Figure 2.36 to access the Aspen Plus online help. We see the following correlation for CPG in Figure 2.37.

Additionally, we can see the scalar pure-component parameter values by following the path: Properties → Methods → Parameters → Pure components → REVIEW-1 (see Figure 2.38). To understand the meaning of each listed parameter, click on the name to expand the pull-down menus, you will see a description.

For HDPE, Aspen Plus assumes the molecular weight for HDPE to be that of the C2H4 segment, that is, 28.0538. To enter the correct molecular weight of our HDPE “oligomer” with 1500 repeated segments, we follow the path: Properties → Methods → Parameters → Pure Components → New → Name: MWHDPE → Input: Component = HDPE, Parameter: MW = 42080.7 (= 28.0538 × 1500). We note that the exact value of this MW does not affect the regression results.

This list of pure component parameters displayed by Aspen Plus in Figure 2.38 does not include the values of  $ T^{*} $,  $ P^{*} $, and  $ \rho^{*} $ defined by Eq. (2.17) and illustrated

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1028_808_1221.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.36 Calling up databank values of pure component parameters.</div>


---

<!-- PDF page 115 -->

## Aspen Ideal Gas Heat Capacity Polynomial

 $$ \begin{aligned}&C_{p}^{*,ig}=C_{1i}+C_{2i}T+C_{3i}T^{2}+C_{4i}T^{3}+C_{5i}T^{4}+C_{6i}T^{5}\ for C_{7i}\leq T\leq C_{8i}\\&C_{p}^{*,ig}=C_{9i}+C_{10i}T^{C_{10i}} for T<C_{7i}\\ \end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_155_735_461.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 2.37 Access Aspen Plus online help for CPlG parameter correlation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_529_781_721.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 2.38 Values of scalar pure component parameters called up from the databanks and displayed in REVIEW-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_804_778_936.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.39 Pure component parameters for POLYSL EOS for an HDPE process.</div>


in Figure 2.31. We follow the path: Properties → Methods → Parameters → Pure Components → New: name = SLTPR → Parameters: SLTSTR, SLPSTR, and SLRSTR and enter the values according to Khare et al. [27] (see Figure 2.39). These values are essential when running regression of vapor–liquid equilibrium data for missing binary interaction parameters.

#### 2.7.6 Enter Experimental Data for Data Regression, Run the Regression, and Examine the Results

We first demonstrate how to regress the pure component parameters for POLYSL,  $ T^{*} $,  $ P^{*} $, and  $ \rho^{*} $, defined by Eq. (2.17) for C2H4, and compare the resulting values

---

<!-- PDF page 116 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_147_673_443.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 2.40 Liquid density data for C2H4 for regression of pure component parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_520_744_992.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 2.41 TPXY data for regression of binary interaction parameters.</div>


with those listed in Figure 2.39. We enter the liquid density data of C2H4 [31] by following the path: Properties → Data → New → Enter ID: C2RHOL, select type: PURE-COMP → Setup: Category = Thermodynamic, Property = RHOL, Component = C2H4; Data - enter C2RHOL data according to Figure 2.40. To enter the TPXY data of Figure 2.41, we follow the path: Properties → Data → New → Enter ID: PEXY1, select type: MIXTURE → Setup: Category → Phase Equilibrium, Data type → TPXY, Components in mixture: C2H4, HDPE, Composition basis: Mass fraction, Data → enter the data displayed in Figure 2.41.

---

<!-- PDF page 117 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_779_340.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.42 Input for regressing pure component parameters using liquid density data C2RHOL.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_426_666_747.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 2.43 Specification of POLYSL pure component parameters to be regressed.</div>


#### 2.7.7 Specifying a Regression Run and the Parameters to be Regressed

To regress the pure component parameters for POLYSL, we follow the path: Properties → Regression → New: Enter ID = C2 → Input: see Figure 2.42.

Next, we specify the pure component parameters to be regressed (see Figure 2.43).

#### 2.7.8 Running the Regression Case and Examining the Results

When running the regression, the control panel first shows which regression case to run. We choose case C2 and click OK to run (see Figure 2.44).

We follow Figure 2.45 to keep the regressed pure component parameter values in the result folder of regression run C2 and not replace the previously entered values (see Figure 2.46). The regressed parameters SLTSTR = 334.509 K, SLPSTR = 2.39886E8 kPa = 2398.86 bar, and SLRSTR = 631.704 kg/cum, which compare favorably with the values of 333, 2400, and 631 entered for C2H4 in Figure 2.39 [27]. Looking at “Profiles” folder of results, we see a table of comparison of experimental and estimated values of temperature, pressure, and liquid density of C2H4 (see Figure 2.47). We plot the results by following the path: Plot (upper

---

<!-- PDF page 118 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_155_507_395.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">Figure 2.44 Selecting the regression case C2 to run.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_463_761_613.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 2.45 Clicking No three times for not placing the parameter values of SLTSTR, STPSTR, and SLRSTR previously entered in Figure 2.39.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_694_744_891.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 2.46 Regressed values of POLYSL pure component parameters for C2H4.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_956_810_1193.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.47 Comparison of experimental and estimated temperature, pressure, and liquid density of C2H4.</div>


---

<!-- PDF page 119 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Plot</th><th style='text-align: center;'>Data</th><th style='text-align: center;'>X-Axis</th><th style='text-align: center;'>Y-Axis</th><th style='text-align: center;'>Data Type</th><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>Y-Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>M1</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>M2</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>M3</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>C17</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>C27</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>C30</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S10</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S20</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S30</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S40</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S50</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S60</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S70</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S80</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S90</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S100</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S110</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S120</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S130</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S140</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S150</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S160</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S170</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S180</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S190</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S200</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S210</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S220</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S230</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S240</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S250</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S260</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S270</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S280</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S290</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S300</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S310</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S320</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S330</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S340</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S350</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S360</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S370</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S380</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S390</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S400</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S410</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S420</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S430</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S440</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S450</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S460</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S470</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S480</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S490</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S500</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S510</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S520</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S530</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S540</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S550</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S560</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S570</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S580</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S590</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S600</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S610</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S620</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S630</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S640</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S650</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S660</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S670</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S680</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S690</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S700</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S710</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S720</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S730</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S740</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S750</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S760</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S770</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S780</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S790</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S800</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S810</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S820</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S830</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S840</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S850</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S860</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S870</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S880</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S890</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S900</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S910</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S920</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S930</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S940</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S950</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S960</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S970</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S980</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>S990</td><td style='text-align: center;'>F-Value</td><td style='text-align: center;'>C-1000s</td><td style='text-align: center;'>200</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.48 The initial plot of estimated liquid density of C2H4 value versus measured value. Note the Format options of Squared plot and Diagonal line at the top.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Exp Val RHO LiQUID C2H4 kg/cum</th><th style='text-align: center;'>Mass Density kg/cum</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>390</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>410</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>420</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>430</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>440</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>460</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>470</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>490</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>510</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>520</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>530</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>540</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>560</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.49 Improved plot of estimated versus measured liquid density of C2H4.</div>


right corner of the computer screen) → Custom → X-axis: Exp Val RHO LQUID C2H4, kg/cum; Y-axis: Est Val RHO LQUID C2H4, kg/cum. See the initial plot in Figure 2.48 → Plot: Format. Choose Squared plot and Diagonal line → see the improved plot in Figure 2.49.

We can use the same approach to regress the pure component parameters for the ethylene segment and other components using the liquid density data. Experimental data for liquid density and heat capacity for most components in the PE, HDPE, LDPE, and LLDPE processes are available in [31–36].

Next, we demonstrate how to regress binary interaction parameters SLETIJ ( $ \eta_{ij} $) and SLKIJ ( $ k_{ij} $) based on Eqs. (2.24) and (2.25) using the liquid density data of C2H4.

---

<!-- PDF page 120 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_150_505_468.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">Figure 2.50 Specification of binary interaction parameters to be regressed.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_539_742_628.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 2.51 Regressed binary interaction parameters between C2H4 and HDPE.</div>


C2RHOL, of Figure 2.40 and the vapor-liquid equilibrium data for polyethylene and ethylene, PEXY1, of Figure 2.41.

We create a new regression run by following the path: Properties → Regression → New → Enter ID: C2TPXY → OK → Setup: enter datasets PEXY1 and C2RHOL (following Figure 2.42) → Parameters → See Figure 2.50 for specifying the binary interaction parameters to be regressed.

Following Figures 2.44–2.46, we run the regression case C2TPXY, and the resulting binary interaction parameters appear in Figure 2.51. The accuracy of these parameters depends on the accuracy of the experimental data.

### 2.8 Polymer Perturbed-chain Statistical Fluid Theory (POLYPCSF) Equation of State

Gross and Sadowski [21–23] developed the PC–SAFT EOS, which is an extension of the well-known SAFT EOS [24–26]. A key difference between the two models is that PC-SAFT model replaces the expression of the dispersion (attractive) interactions between isolated (or disconnected) polymer segments with that between connected polymer segments. See an illustration in Figure 2.52 in which each circle dot represents a segment.

The PC-SAFT model is applicable to fluid systems of both small and large molecules over a wide range of temperature and pressure conditions, and it represents polymer systems very well.

---

<!-- PDF page 121 -->

Statistical thermodynamics typically uses the Helmholtz free energy A to represent the attractive (or perturbation) interactions between molecules, as most properties of interest, such as pressure, can be obtained by proper differentiation of A. In the SAFT model, this attractive or perturbation term is a series expansion in terms of the reciprocal temperature, and each coefficient of the expansion depends on the density and composition. By contrast, the PC-SAFT model represents the molar residual Helmholtz free energy  $ A^{res} $ as a sum of two contributions

 $$ A^{\mathrm{res}}=A^{\mathrm{ref}}+A^{\mathrm{pert}} $$ 

where  $ A^{res} $ and  $ A^{pert} $ are the reference and perturbation (attractive) contributions, respectively. The reference term considers a fluid consisting of hard-sphere chains as a reference for the perturbation theory, and the perturbation term incorporates the attractive forces between the chains.

The primary difference between the PC-SAFT and SAFT models is in the perturbation term. The SAFT model uses hard spheres, not hard-sphere chains, as a reference fluid for the perturbation contribution. The use of hard-sphere chains allows the PC-SAFT EOS to account for the connectivity of segments that comprise the chains when considering the attractions between species, resulting in a more realistic description of the thermodynamic behavior of mixtures of chainlike molecules. Gross and Sadowski [21–23] and others [28–30] demonstrate that the PC-SAFT predictions for vapor–liquid and vapor–liquid–liquid equilibria are superior to the SAFT model.

The resulting PC-SAFT EOS expresses the compressibility as a sum of the ideal (with a value of unity), reference, and perturbation contributions:

 $$ \frac{\mathrm{PC}}{RT}=z=z^{\mathrm{id}}+z^{\mathrm{ref}}+z^{\mathrm{pert}}=1+z^{\mathrm{ref}}+z^{\mathrm{pert}} $$ 

Interested readers may refer to the original references for the analytical expressions of the PC-SAFT model [21–23] for the details of this contributions. A recent article by Kang et al. [37] gives a fairly complete analysis of the PC-SAFT model equations and their iterative solution procedures.

The application of the PC-SAFT model requires the use of three pure-component parameters for each species involved: (1) segment number, m, which is a characteristic length and is directly proportional to the size (molecular weight) of the species; (2) segment diameter,  $ \sigma $ Å; and (3) segment energy,  $ \varepsilon $ Joule, typically expressed as a ratio  $ \varepsilon/k_B $ in K, where  $ k_B $ is the Boltzmann's constant, 1.38 E-23 J/K. For polymers,

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1094_594_1220.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 2.52 An illustration of the disconnected segments in SAFT versus the connected segments in PC-SAFT.</div>


---

<!-- PDF page 122 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_808_289.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.53 Pure component parameters for POLYPCSF model for simulating a PP process.</div>


we typically replace the segment number m by a ratio r defined as m divided by the number-average molecular weight, MWN:

 $$ r=m/M W N $$ 

Using this ratio is more convenient because the polymer molecular weight is often unknown until the polymer is produced. For segments, we often use the ratio r as well. These parameters are obtained by fitting experimental vapor pressure and liquid molar volume data for pure components.

Figure 2.53 illustrates the values of these pure component parameters in the simulation of a gas-phase PP process [38]. To enter these parameters in Aspen Plus, follow the path:

Properties → Methods → Parameters → Pure Components → New: name = PCSAFT → Enter parameter name, component, and value. In Figure 2.53, (1) parameter PCSFTM is the segment number m; (2) parameter PCSFTU represents the ratio of the segment energy to the Boltzmann's constant  $ \varepsilon/k $ in K; (3) parameter PCSFTV is the segment diameter,  $ \sigma $ Å; and (4) parameter PCSFTR represents the ratio  $ r $ in mol/g defined by Eq. (2.27). For those species with missing pure component parameters, a search “missing parameters (POLYPCSF)” of Aspen Plus online help suggests using the values: PCSFTM = 0.02434* (component molecular weight); PCSFTU = 267.67 K; PCSFTV = 4.072 Å; and PCSFTR = 0.02434 mol/g for polymer species and segments.

The POLYPCSF model also requires binary interaction parameters that are correlated by Eq. (2.24) as a function of  $ T_r = T/T_{ref} $, where  $ T_{ref} = 298.15 \, K $:

 $$ k_{ij}=a_{ij}+\mathrm{^{b}_{i j}/}_{T_{r}}+c_{ij}\ln T_{r}+d_{ij}T_{r}+e_{ij}T_{r}^{2} $$ 

These parameters may be obtained by regressing phase-equilibrium data. When these parameter values are not supplied, they default to zero.

##### 2.9 Workshop 2.4. Regression of Property Parameters for POLYPCSF EOS

#### 2.9.1 Objective and Data Sources

The objective of this workshop is to demonstrate that the step-by-step procedure of Workshop 2.3 for regression of property parameters for POLYSL EOS is directly applicable to the POLYPCSF EOS.

---

<!-- PDF page 123 -->

For polymer components, we may find relevant thermophysical property and phase equilibrium data: (1) for ethylene and propylene in [34–36]; (2) for polymer solutions and components in [31, 32, 39–42]; (3) for solvent vapor and liquid phase data in [33]; and (4) for pure component parameters for POLYPCSF for PP process in [38].

#### 2.9.2 Regression of Pure Component Parameters for POLYPCSF EOS

Following Figure 2.34, we begin by creating a data regression run and choosing the MET unit set and save the simulation file as WS2.4 Regressing Property Parameters for POLYPCSF.bkp.

Figure 2.54 shows the component specification. As discussed in Sections 2.7.4, both property analysis and regression tools in Aspen Plus do not support polymer attributes. Therefore, for property analysis and regression runs, we define PE as an oligomer.

We follow the path: Properties → Components → Polymers → Characterization: (1) Segments – Define C2H4SEG as repeat segment; (2) Oligomers: Specify PE to include 1250 C2H4SEG. Next, we click on “Review” button illustrated in Figure 2.54 to call up pure component parameters from Aspen Plus databanks for pure components, segments, and polymers. Following the path:

Properties → Parameters → Pure Components → REVIEW-1 → we see in Figure 2.55 the molecular weight (MW) for PE being 28.0538, which is the molecular weight of the monomer C2H4, not that of the oligomer with 1250 C2H4SEG repeated segments. To specify the correct molecular weight of PE, we follow the path: Properties → Parameters → Pure Components → New → Choose type = scalar and specify name = MWPE → OK → Input: enter component PE, parameter MW = 35067.25 (28.0538 × 1250).

We follow the procedure in Figure 2.40 to enter the liquid density dataset PERHOL for PE (see Figure 2.56) and the vapor–liquid equilibrium dataset PETPXY1 for C2H4-PE of Figure 2.41 (with component name PE replacing HDPE).

Following Figure 2.42, we set up a regression run C2H4SEG to estimate the POLYPCSF pure component parameters PCSFTU (the ratio of the segment energy to the Boltzmann's constant  $ \varepsilon/k $ in K), PCSFTV (the segment diameter,  $ \sigma \mathring{A} $), and PCSFTR (the ratio  $ r $ in mol/g defined by Eq. (2.27)) for C2SEG (see Figure 2.57).

Executing a regression run based on the liquid density dataset C2RHOL gives the resulting pure component parameters of Figure 2.58.

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_1052_617_1234.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 2.54 Component specifications.</div>


---

<!-- PDF page 124 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_151_743_455.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 2.55 Pure component parameters from Aspen databanks.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_511_551_828.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">Figure 2.56 Liquid density dataset PERHOL of PE.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_885_726_1221.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 2.57 Setting up a regression run for POLYPCSF pure component parameters of C2SEG.</div>


---

<!-- PDF page 125 -->

Data - PERHOL (PURE-COMP)  $ \times $ Control Panel  $ \times $ C2SEG - Results  $ \times $
Parameters Consistency Tests Residual Profiles Correlation Sum of Squares Evaluation Extra Property St
Regressed parameters
Parameter Component i Component j Value (SI units) Standard deviation
PCSTFU/I C2H4SEG 254.45 1.95559
PCSTFV/I C2H4SEG 1.94588 0.0778691
PCSFTR/I C2H4SEG 0.232374 0.0278565

<div style="text-align: center;">Figure 2.58 Regressed POLYPCSF pure component parameters for C2H4 segment.</div>


Data - PERHOL (PURE-COMP)  $ \times $ Control Panel  $ \times $ C2SEG - Results +
Parameters Consistency Tests Residual Profiles Correlation Sum of Squares Evaluation Extra Property
Data set PERHOL
Summary of regression results
Exp Val TEMP Est Val TEMP Exp Val PRES Est Val PRES Exp Val RHO Est Val RHO LIQUID PE LIQUID PE
K K atm atm kg/cum kg/cum
408.25 408.25 1 787.9 787.733
415.85 415.85 1 783.58 783.457
422.65 422.65 1 779.61 779.658
433.65 433.65 1 773.4 773.56
445.15 445.15 1 767.05 767.238
457.95 457.95 1 760.05 760.248
471.15 471.15 1 753.38 753.08

<div style="text-align: center;">Figure 2.59 A comparison of estimated and experimental data of liquid density data of PE.</div>


The last two columns in Figure 2.59 show that the estimated liquid density data of PE match the experimental data well.

Following Figure 2.50, we create a regression run BINARY to estimate the binary interaction parameter PCSKIJ between components C2H4 and C2H4SEG using the vapor–liquid equilibrium dataset PETPXY1 for C2H4-PE of Figure 2.41 (with component name PE replacing HDPE, see Figure 2.60).

Figure 2.61 shows the resulting binary interaction parameter. This concludes the current workshop. We save the simulation file as WS 2.4 Regressing Property Parameters for POLYPCSF.bkp.

This workshop concludes our sections of selection of thermodynamic methods and estimation of physical properties. We summarize our discussion of the differences between an EOS and an activity coefficient (gamma) model for polymer applications in Table 2.6.

### 2.10 Correlation of Polymer Product Quality Indices and Structure-Property Correlations

#### 2.10.1 Polyolefin Product Quality Indices

Fundamentally speaking, polymer products are characterized by their molecular structures. The key quality measures include molecular weight averages (MWN

---

<!-- PDF page 126 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_163_565_507.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Figure 2.60 Input to regress binary interaction parameter PCSKIJ.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_592_648_720.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 2.61 Regressed POLYPCSF binary interaction parameter.</div>


<div style="text-align: center;">Table 2.6 Comparison of an equation of state and an activity coefficient model for polymer applications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>EOS Models</td><td style='text-align: center; word-wrap: break-word;'>Gamma or Activity Coefficient Models</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Limited in ability to represent nonideal liquid</td><td style='text-align: center; word-wrap: break-word;'>Can represent highly nonlinear liquids with polar and hydrogen-bonding species</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Fewer binary interaction parameters required</td><td style='text-align: center; word-wrap: break-word;'>Many binary interaction parameters required; Section 2.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Parameters extrapolate reasonably with temperature</td><td style='text-align: center; word-wrap: break-word;'>Binary interaction parameters are highly temperature dependent</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Can represent both vapor and liquid</td><td style='text-align: center; word-wrap: break-word;'>Can only represent the liquid phase</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Consistent in critical region for light gases and low-molecular-weight components</td><td style='text-align: center; word-wrap: break-word;'>Inconsistent in critical region, resulting in incorrect concentrations of light gases and low-molecular-weight components in liquid phase, Section 2.2.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Common EOS Models</td><td style='text-align: center; word-wrap: break-word;'>Common Gamma Models</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLYSL, Polymer Sanchez-Lacombe EOS, Sections 2.6 and 2.7; POLYPCSF, Polymer Perturbed-Chain Statistical Fluid Theory EOS, Sections 2.8 and 2.9</td><td style='text-align: center; word-wrap: break-word;'>POLYNRTL, Polymer Non-Random Two-Liquid Activity Coefficient Model, Sections 2.2.4 and 2.3</td></tr></table>

---

<!-- PDF page 127 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_147_750_389.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 2.62 Melt-flow plastometer for Ml determination.</div>


and MWW), polydispersity index, copolymer composition, type and frequency of branching, and tacticity. Aspen Polymers can predict these quality indices from the moment equations as a part of the simulation model.

In practice, industrial polymer producers focus more on empirical product quality indices. Two most important quality measures are melt index (MI) or melt flow rate (MFR) and polymer density. MI or MFR is defined as the mass of polymer, in grams, flowing in 10 minutes (gm/10 min) through a capillary of a specific diameter and length by a pressure applied via prescribed alternative gravimetric weights for alternative prescribed temperatures. The standard testing methods are ASTM D1238 for flow rates of thermoplastics by extrusion plastometer and ISO 1133 for determination of MFR of thermoplastics. For density, the standard testing methods are ASTM D1505 for density of plastics, ASTM D792-00 for density and specific gravity of plastics, and ISO 1183 for density of plastics.

Figure 2.62 illustrates a melt-flow plastometer for MI determination. The polymer melt flows through the barrel, entrance region (or contraction), and capillary. The blow-up depicts the entrance region, where funneling flow takes place. The size of the capillary is standardized at 0.083" diameter and 0.250" length. For polyethylenes, the most common conditions are 190°C and 2.16 kg force. For polypropylene, the temperature is 230°C. For some polyethylene, the load is increased to 21.6 kg, which is called the High Load Melt Index (HLMI) [43]. MI gives a relative indication of the molecular weight and viscosity of the polymer. The lower the MI, the higher the molecular weight and viscosity.

The tacticity is an important quality measure of polypropylene. In Figure 2.63, we see that in an isotactic PP, (all the repeating methyl CH3) groups, represented by the dark downward arrow, are arranged along the same side of the polymer chain. In the syndiotactic (syntactic) PP, the repeating methyl groups are arranged on an alternating side of the polymer chain, while in the atactic PP, the repeating methyl groups are on either side of the polymer chain. In Chapter 5, we show that Aspen Polymers simulation quantifies the tacticity of PP by an atactic fraction (ATFRAC), which is defined as the ratio of atactic propagation reaction rate to the total propagation reaction rate.

---

<!-- PDF page 128 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_142_454_421.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">Figure 2.63 Three stereochemical configurations of PP.</div>


#### 2.10.2 Empirical Correlations of Polymer Product Quality Targets

We first note that the estimated molecular weight distribution can vary by catalyst, process, plant operation, and testing method. Therefore, empirical correlations of polymer product quality targets have a limited range of applicability. Correlations from a particular catalyst, a particular comonomer, a single reactor, or from multi-reactor operations could be different.

In an early publication in 1953, Sperati et al. [44] presented a fairly complete study of 11 property correlations of LDPE. Two of the reported correlations include:

 $$ \mathrm{Log}\left(\mathrm{MI}\right)=5.09-1.53\times10^{-4}\left(\mathrm{MWN}\right) $$ 

 $$ Density=2.0\times10^{-3}(crystallinity)+0.03 $$ 

A popular correlation for HDPE or LLDPE copolymer density is of the form

 $$ \mathrm{Density}=A-B^{*}(\mathrm{SFRAC}^{*}100)^{\mathrm{C}} $$ 

where A, B, and C are constants, and SFRAC is the mole fraction of the comonomer in the polymer product (e.g. comonomer 1-butene with monomer ethylene).

In the literature, most empirical correlations for MI for polyolefins with broad MWD or large PDI are based on the weight-average molecular weight (MWW). For example, a general MI correlation with MWW [45–47] is in the form of

 $$ \mathbf{M}\mathbf{I}=a(\mathbf{M}\mathbf{W}\mathbf{W})^{-b} $$ 

where a and b are the correlating parameters. For PP, the MI may depend on the MWW as well as the atactic fraction (ATFRAC), calculated by the atactic chain propagation reaction (ATACT-PROP) in Aspen Polymers [38].

The polymer density is usually measured for the pellets and correlated as a function of the MWW. For copolymerization, we often correlate the polymer density as a function of mole fraction of the comonomer and the MWW [47, 48]. In Ref. [48], the HDPE density obtained from ethylene copolymerization with comonomer 1-butene follows the following correlation:

 $$ \left(1-0.0081x_{B}^{0.148895}\right)\times\left[1.137247-0.014314\ln(MWW)\right] $$ 

---

<!-- PDF page 129 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_149_779_437.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 2.64 Using Excel to develop a correlation for melt index.</div>


where  $ x_{B} $ is the mole fraction of 1-butene.

We demonstrate below how to develop simple linear and nonlinear correlations of melt index based on the measured data from a PP process using Excel. We save the Excel file as Example 2.2 Correlation of Melt Index.xlsx.

Referring to Figure 2.64, we see the measured data for MI, MWN, and MWW, and PDI (= MWW/MWN) for polymer grade 1 in cells B10–B13, C10–C13, E10–E13, and D10–D13, and for polymer grade 2 in cells B17–B20, C17–C20, E17–E20, and D17–D20. Based on the assumed values of parameters a and b, we find the sum of squared errors (SOE) between the estimated values and experimental data and then use Goal Seek solver in Excel to find the fitted values of parameters a and b that minimize the SOE. To access the Goal Seek solver, follow the path: Data → What-If Analysis → Goal Seek. We note that because of the significant difference in the values of MI for grades 1 and 2, it may be best to develop two separate correlations for the measured data.

#### 2.10.3 Estimation of Apparent Newtonian Viscosity from MI-MWW Measurement

We begin with some background about Newtonian and non-Newtonian fluids. Newtonian fluids satisfy Newton's law of viscosity, where the proportionality constant  $ \eta $ is the viscosity of the fluid.

 $$ \tau\left(shear stress,Pa\right)=\eta\left(viscosity,Pa-s\right)\times\dot{\gamma}\left(shear rate,1/s\right) $$ 

In reality, most fluids are non-Newtonian, which means that their viscosity depends on shear rate (shear thinning or thickening) or the deformation history. Non-Newtonian fluids display a nonlinear relation between viscosity and shear rate (see Figure 2.65). A fluid is shear thickening if the viscosity of the fluid increases as the shear rate increases. A common example of shear thickening fluids is a mixture of corn starch and water. Fluids are shear thinning if the viscosity decreases as the shear rate increases. Common examples include ketchup, paints, and blood.

---

<!-- PDF page 130 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_147_438_421.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">Figure 2.65 An illustration of shear thickening, shear thinning, and Newtonian fluid.</div>


Seavey et al. [46] review the relationships among the molecular weight distribution, non-Newtonian shear viscosity, and melt index. Both simple and more complex semiempirical methods exist to relate these variables. For example, Bremner et al. [49] present experimental data and study the relationship between different molecular weight averages and melt index for several commercial thermoplastics, including PS, PP, LPDE, and HDPE.

Rohlfing and Janzen [50] take a different approach using a model for the flow within the melt indexer itself to predict the melt index. Referring to Figure 2.62, they consider the pressure drop in the melt indexer as a sum of the pressure drops in the barrel, entrance region, and the capillary. They develop a set of integral-algebraic equations relating the shear rates at the barrel wall, at the capillary wall, and in the capillary, the barrel pressure drop, the capillary pressure drop, the entrance pressure drop, and the volumetric flow rate.

For a Newtonian fluid with viscosity  $ \mu $ (in Pascal-second, or Pa-s) and based on the melt indexer of Figure 2.62 with standard dimensions specified in Section 2.10.1, analytical solution of the Rohlfing and Janzen model equations is possible, and it results in a simple equation:

 $$ \mathrm{MI}=7280/\mu $$ 

The details appear in [46].

Working backward from the melt index to predict the non-Newtonian shear viscosity (or “flow curve”) is difficult because of the integral-algebraic equations involved. In cases where the integral covers part of the shear-thinning region of the flow curve, solutions to the flow model are not unique. For example, a polymer with a high Newtonian viscosity but with a rapid onset of shear thinning may have the same melt index as a polymer with a lower Newtonian viscosity with less shear-thinning behavior.

Therefore, in our example below, we limit ourselves to the characterization of the apparent Newtonian viscosity of a polymer sample which can be estimated using the analytical correlation, Eq. (2.34). Once the apparent Newtonian viscosities are estimated from the MI data, we can use a power-law expression to correlate MWW with the viscosity.

---

<!-- PDF page 131 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>E</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Step 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>Data (Bremner, Budin, and Cook, 1990)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Calculate apparent Newtonian Viscosity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>MWW (g/mol)</td><td style='text-align: center; word-wrap: break-word;'>Mt (g/10min)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Viscosity in. Pa s)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>167000</td><td style='text-align: center; word-wrap: break-word;'>0.3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>24267</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>103000</td><td style='text-align: center; word-wrap: break-word;'>0.6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>12133</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>145000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>7280</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>131000</td><td style='text-align: center; word-wrap: break-word;'>0.8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>9100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>68000</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6067</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>79000</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1820</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>102000</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3640</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>54000</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>364</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>48000</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>146</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>38000</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>73</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 2.66 MI vs MWW for LDPE samples. Source: Adapted from Aspen Technology, Inc. [51].</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Step 2</td></tr><tr><td colspan="2">Plot  $ \ln(\text{Visc}) $ vs.  $ \ln(\text{MWW}) $ and  $ \text{Fit} $ a Line</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \ln(\text{MWW}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \ln(\mu) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12.02574909</td><td style='text-align: center; word-wrap: break-word;'>10.09685895</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.54248427</td><td style='text-align: center; word-wrap: break-word;'>9.403711765</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.88448902</td><td style='text-align: center; word-wrap: break-word;'>8.892886141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.7829526</td><td style='text-align: center; word-wrap: break-word;'>9.116029693</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.12726298</td><td style='text-align: center; word-wrap: break-word;'>8.710564584</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.27720313</td><td style='text-align: center; word-wrap: break-word;'>7.50659178</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11.53272809</td><td style='text-align: center; word-wrap: break-word;'>8.199738961</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10.89673933</td><td style='text-align: center; word-wrap: break-word;'>5.897153868</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10.77895629</td><td style='text-align: center; word-wrap: break-word;'>4.980863136</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10.54534144</td><td style='text-align: center; word-wrap: break-word;'>4.287715955</td></tr></table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>ln(MWW)</th><th style='text-align: center;'>ln(√(z))</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>10.7</td><td style='text-align: center;'>5.2</td></tr>
    <tr><td style='text-align: center;'>10.9</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>11.1</td><td style='text-align: center;'>8.8</td></tr>
    <tr><td style='text-align: center;'>11.2</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>11.4</td><td style='text-align: center;'>9.2</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>8.2</td></tr>
    <tr><td style='text-align: center;'>11.6</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>11.7</td><td style='text-align: center;'>9.2</td></tr>
    <tr><td style='text-align: center;'>11.8</td><td style='text-align: center;'>8.8</td></tr>
    <tr><td style='text-align: center;'>11.9</td><td style='text-align: center;'>9.5</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>10.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2.67 Developing a correlation between apparent Newtonian viscosity  $ \mu $ and MWW.</div>


Let us open the Excel spreadsheet Example 2.2 Correlation of Melt Index.xlsx. Columns B and C show the data of MI vs. MWW for LLDPE samples from Table 1 of [51] (see Figure 2.66). Based on Eq. (2.35), we can find Column E from Column C, that is  $ \mu = 7280/MI $.

We then use Excel to develop a correlation between  $ \mu $ and MWW (see Figure 2.67). We note that this approach will work well for low MI materials where the flow through the melt indexer is primarily Newtonian.

Finally, we note that we demonstrate how to implement the correlations for MI and polymer density, Eqs. (2.31) and (2.32), in steady-state polymer process simulation in Section 5.8.11 using FORTRAN in Aspen Polymers and in dynamic polymer-grade changes using “Tasks” in Aspen Plus Dynamics in Section 7.6.3.

## References

1 Walas, S.M. (1985). Phase Equilibria in Chemical Engineering. Stoneham, MA: Butterworth.

2 Bokis, C.P., Orbey, H., and Chen, C.C. (1999). Properly model polymer processes. Chemical Engineering Progress 95 (4): 39.

---

<!-- PDF page 132 -->

3 Seavey, K.C. and Liu, Y.A. (2008). Step-Growth Polymerization Process Modeling and Product Design, 87–92. New York: Wiley.

4 Chen, C.C. (1993). A segment-based local composition model for Gibbs energy of polymer solutions. Fluid Phase Equilibria 83: 135.

5 Renon, H. and Prausnitz, J.M. (1968). Local compositions in thermodynamic excess functions for liquid mixtures. AIChE Journal 14: 135.

6 Flory, P.J. (1942). Thermodynamics of high polymer solutions. Journal of Chemical Physics 10: 51.

7 Flory, P.J. (1953). Principles of Polymer Chemistry. New York: Cornell University Press.

8 Huggins, M.L. (1942). Some properties of solutions of long-chain compounds. Journal of Physical Chemistry 46: 151.

9 Oishi, T. and Prausnitz, J.M. (1978). Estimation of solvent activity in polymer solutions using a group contribution method. Industrial and Engineering Chemistry Process Design and Development 17: 333.

10 Fredenslund, A., Jones, R.L., and Prausnitz, J.M. (1975). Group contribution estimation of activity coefficients in nonideal liquid mixtures. AIChE Journal 21: 1086.

11 Fredenslund, A. (1977). Vapor-Liquid Equilibria Using UNIFAC: A Group-Contribution Method. New York: Elsevier.

12 Redlich, O. and Kwong, J.N.S. (1949). On the thermodynamics of solutions. V. An equation of state. Fugacities of gaseous solutions. Chemical Reviews 44: 233.

13 Van Krevelen, D.W. and te Nijenhuis, K. (2009). Properties of Polymers - Their Correlation with Chemical Structure; Their Numerical Estimation and Prediction from Additive Group Contributions, 4e. Amsterdam: Elsevier.

14 Painter, P.C. and Coleman, M.M. (1977). Fundamentals of Polymer Science: An Introductory Text, 2e. Lancaster, PA: Technonomic Publishing Company, Inc.

15 Lambert, S.M., Song, Y., and Prausnitz, J.M. (2000). Equations of state for polymer systems. In: Equations of State for Fluids and Fluid Mixtures (ed. J.V. Sengers, R.F. Kayer, C.J. Peters, and H.J. White), 523–588. New York: Elsevier.

16 Wei, Y.S. and Sadus, R.J. (2000). Equations of state for calculation of fluid-phase equilibria. AIChE Journal 46: 169.

17 Sanchez, I.C. and Lacombe, R.H. (1976). An elementary molecular theory of classical fluids. Pure fluids. Journal of Physical Chemistry 80: 2352.

18 Lacombe, R.H. and Sanchez, I.C. (1976). Statistical thermodynamics of fluid mixtures. Journal of Physical Chemistry 80: 2568.

19 Sanchez, I.C. and Lacombe, R.H. (1978). Statistical thermodynamics of polymer solutions. Macromolecules 11: 1145.

20 McHugh, M.A. and Krukonis, V.J. (1994). Supercritical Fluid Extraction: Principles and Practice, 2e, 99–134. Elsevier.

21 Gross, J. and Sadowski, G. (2001). Perturbed-chain SAFT: an equation of state based on a perturbation theory for chain molecules. Industrial and Engineering Chemistry Research 40: 1244.

22 Gross, J. and Sadowski, G. (2002). Modeling polymer systems using of perturbed-chain SAFT equation of state. Industrial and Engineering Chemistry Research 41: 1084.

---

<!-- PDF page 133 -->

23 Gross, J. and Sadowski, G. (2002). Application of perturbed-chain SAFT equation of state to associating systems. Industrial and Engineering Chemistry Research 41: 5510.

24 Chapman, W.G., Gubbins, K.E., Jackson, G., and Radosz, M. (1990). New reference equation of state for associating liquids. Industrial and Engineering Chemistry Research 29: 1709.

25 Huang, S.H. and Radosz, M. (1990). Equation of state for small, large, polydisperse, and associating molecules. Industrial and Engineering Chemistry Research 29: 2284.

26 Huang, S.H. and Radosz, M. (1991). Equation of state for small, large, polydisperse, and associating molecules: extension to fluid mixtures. Industrial and Engineering Chemistry Research 30: 1994.

27 Khare, N.P., Seavey, K.C., Liu, Y.A. et al. (2002). Steady-state and dynamic modeling of commercial slurry high-density polyethylene (HDPE) processes. Industrial and Engineering Chemistry Research 41: 5601.

28 Orbey, H., Bokis, C.P., and Chen, C.C. (1998). Equation of state modeling of phase equilibrium in the low-density polyethylene process: the Sanchez-Lacombe, statistical associating fluid theory, and polymer-Soave-Redlich-Kwong equations of state. Industrial and Engineering Chemistry 37: 4481.

29 Bokis, C.P., Ramanathan, S., Franjione, J. et al. (2002). Physical properties, reactor modeling, and polymerization kinetics in the low-density polyethylene tubular reactor process. Industrial and Engineering Chemistry Research 41: 1017.

30 Krallis, A. and Kanellopoulos, V. (2013). Application of Sanchez–Lacombe and perturbed-chain statistical fluid theory equation of state models in catalytic olefins (co)polymerization industrial applications. Industrial and Engineering Chemistry Research 52: 9060.

31 Hao, W., Elbro, H.S., and Alessi, P. (1992). Polymer Solution Data Collection, Chemistry Data Series, Part 1, vol. XIV. Frankfurt: DECHEMA.

32 Danner, R.P. and Hugh, M.S. (1993). Handbook of Polymer Solution Thermodynamics. New York: Design Institute for Physical property Research, American Institute of Chemical Engineers.

33 NIST (National Institute of Science and Technology) (2023). NIST Chemistry Webbook, SRD69, Thermophysical Properties of Fluid Systems. https://webbook.nist.gov/chemistry/fluid/ (accessed 30 March 2023).

34 William, R.B. and Katz, D.L. (1954). Vapor-liquid equilibria in binary systems. Hydrogen with ethylene, ethane, propylene, and propane. Industrial and Engineering Chemistry 46: 2512.

35 Beaton, C.F. and Hewitt, G.F. (1989). Physical Property Data for the Design Engineer. New York: Hemisphere Publishing Corp.

36 Sychev, V.V., Vasserman, A.A., Golovsky, E.A. et al. (1987). Thermodynamic Properties of Ethylene. New York: Hemisphere Publishing Corp.

37 Kang, J., Zhu, L., Xu, S. et al. (2018). Equation-oriented approach for handling the perturbed-chain SAFT equation of state in simulation and optimization of polymerization process. Industrial and Engineering Chemistry Research 57: 4697.

---

<!-- PDF page 134 -->

38 Khare, N.P., Lucas, B., Seavey, K.C. et al. (2004). Steady-state and dynamic modeling of gas-phase polypropylene processes using stirred-bed reactors. Industrial and Engineering Chemistry Research 43: 884.

39 Olabisi, O. and Simha, R. (1975). Pressure-volume-temperature studies of amorphous and crystalline polymers. I. Experimental. Macromolecules 8: 206.

40 Gaur, U. and Wunderlich, B. (1981). Heat capacity and other thermodynamic properties of linear macromolecules. II. Polyethylene. Journal of Physical and Chemical Reference Data 10: 119.

41 Knapp, H., Doring, R., Oellrich, L. et al. (1982). Vapor-Liquid Equilibria for Mixtures of Low Boiling Substances, Chemistry Data Series, Part 1, vol. VI. Frankfurt: DECHEMA.

42 Brandrup, J., Immergut, E.H., and Grulke, E.A. (1999). Polymer Handbook, 4e. New York: Wiley.

43 Griff, A.L. (2003). Melt Index Mysteries Unmasked. https://griffex.com/wp-content/uploads/2020/09/Griff-meltindex.pdf (accessed 16 May 2021).

44 Sperati, C.A., Franta, W.A., and Starkweather, H.W. (1953). The molecular structure of polyethylene V. The effect of chain branching and molecular weight on physical properties. Journal of the American Chemical Society 75: 6127.

45 Sinclair, K.B. (1983). Characteristics of Linear LDPE and Description of the UCC Has Phase Process. Process Economics Report. Menlo Park, CA: SRI International.

46 Seavey, K.C., Khare, N.P., Liu, Y.A. et al. (2003). Quantifying relationships among the molecular weight distribution, non-newtonian shear viscosity and melt index for linear polymers. Industrial and Engineering Chemistry Research 42: 5354.

47 Mattos Neto, A.G., Freitas, M.F., Nele, M., and Pinto, J.C. (2005). Modeling ethylene/1-butene copolymerization in industrial slurry reactors. Industrial and Engineering Chemistry Research 44: 2697.

48 Meng, W., Li, J., Chen, B., and Li, H. (2013). Modeling and simulation of ethylene polymerization in industrial slurry reactor series. Chinese Journal of Chemical Engineering 21: 850.

49 Bremner, T., Rudin, A., and Cook, D.G. (1990). Melt flow index values and molecular weight distributions of commercial thermoplastics. Journal of Applied Polymer Science 41: 1617.

50 Rohlfing, D.C. and Janzen, J. (1997). What is happening in the melt-flow plastometer: the role of elongational viscosity. Technical Papers of the Annual Technical Conference-Society of Plastics Engineers Incorporated, Society of Plastics Engineers Inc., 1010–1014.

51 Aspen Technology, Inc. (2020). Top Questions about Aspen Polymer Process Modeling in Aspen Plus. AspenTech FAQ. https://www.aspentech.com/en/resources/faq-documents/top-questions-about-polymer-process-modeling-in-aspen-plus (accessed 4 June 2021).