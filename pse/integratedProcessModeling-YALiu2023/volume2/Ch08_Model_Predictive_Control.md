# 8. Model-Predictive Control of Polyolefin Processes

<!-- PDF page 471 -->

## Model-Predictive Control of Polyolefin Processes

This chapter covers the fundamentals and practice of model-predictive control (MPC), or advanced process control (APC), of polyolefin processes. The motivation for this chapter appeared previously in Chapter 1, Section 1.4.2, discussing the industrial and potential applications of APC to optimizing polyolefin manufacturing.

We begin by introducing the basic concepts and tools of APC in Section 8.1. Specifically, Section 8.1.1 presents some basic definitions, including manipulated variable (MV), feedforward/disturbance variables (FF/DVs), controlled variable (CV), unit-step response curve, and integrating (ramp) variable. Section 8.1.2 explains the multivariable dynamic model and the key differences between conventional proportional-integral-derivative (PID) control and APC. This subsection describes where the benefits of APC come from, including model CV prediction and reconciliation to online measurements, steady-state economic optimization to identify MV and CV targets, and dynamic control execution to reach MV and CV targets. This subsection presents the Aspen DMCplus control structure, illustrating the three sources of benefits of APC, and the Aspen DMC3 (third-generation dynamic matrix control [DMC]) control structure. Section 8.1.3 introduces linear modeling of DMC, step-response model, and finite-impulse response (FIR) model. Section 8.1.4 covers model evaluation and useful tools, including the concepts of relative gain array (RGA), and ill-conditioned model matrices and collinear systems. Section 8.1.5 discusses open-loop predictions, prediction error filtering, and prediction update. Section 8.1.6 presents the important concepts and parameters in steady-state economic optimization and dynamic controller simulation. This is a key subsection that a beginner in APC should fully understand to develop and fine-tune advanced process controllers.

Section 8.2 presents a hands-on workshop for the step-by-step development of a dynamic matrix controller model for a copolymerization process using Aspen DMC3 Builder.

Section 8.3 introduces the MPC of nonlinear processes. Specifically, Section 8.3.1 discusses the challenges of developing nonlinear dynamic models for polymerization process control. Section 8.3.2 covers the state-space bounded derivative network (SS-BDN) for developing a nonlinear controller model of polyolefin processes.

---

<!-- PDF page 472 -->

Section 8.4 presents a hands-on workshop for the step-by-step development of a nonlinear model-predictive control (NMPC) of a polypropylene process. Section 8.5 discusses the new development of MPC with embedded AI, and this chapter ends with a reference section.

### 8.1 Introduction to Advanced Process Control (APC)

#### 8.1.1 Some Basic Definitions

##### 8.1.1.1 Independent and Dependent Variables

We begin by introducing the basic concepts of APC [1–4]. Figure 8.1 illustrates a simplified flowsheet of a solution copolymerization process. There are two monomers, methyl methacrylate (MMA) and vinyl acetate (VA), an initiator (INITIATO), and a chain-transfer agent (TRANSFER). The reactor has a cooling jacket with a cooling water (CW) stream as the cooling medium.

We define independent variables as those causal variables whose values are not affected by or are independent of any other variables in the process. We classify the independent variables into two categories:

(1) Manipulated variables (MVs): variables that the operator can change, particularly:

1. The setpoint to regulate a controller, labeled by *.SP, such as FMMA.SP, for the setpoint for the mass flow rate of monomer MMA, FMMA; and

2. The valve position (% open) to regulate a control valve, labeled by *.VP, such as FVA.VP for the valve position for the control valve for monomer mass flow rate, FVA.

(2) Feedforward/disturbance variables (FFs/DVs): variables that impact the process, but cannot be adjusted directly, such as:

1. The temperature of cooling water passing through the cooling jacket of the reactor, which depends on an upstream cooling tower system, and varies with seasonal weather.

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_943_809_1218.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.1 A simplified flowsheet of a solution copolymerization process.</div>


---

<!-- PDF page 473 -->

2. Unmeasured temperature of a feed stream, which acts as a disturbance variable.

We define dependent variables as those variables whose dynamic behavior could be fully described by changes in independent variables over time, particularly controlled variables (CVs), labeled by *.PV, such as polymer production rate, POLYMER.PV, that are typically maintained at a constant value or between high and low limits. We note that in a process, there are many dependent variables, but we only choose the important ones as CVs.

For the copolymerization example of Figure 8.1, we consider the following variables:

1. MVs: mass flow rates (kg/hr) of monomers MMA and VA, initiator and chain-transfer agent (represented by Flow_MMA.SP, Flow_VA.SP, Init.SP, and Transf.SP), and temperature of the cooling jacket, T_Jkt.SP.

2. CVs: polymer production rate (kg/hr), polymer molecular weight, reactor exit temperature (°C), and mole fraction of monomer MMA in the polymer product (represented by Polymer.PV, Mol_Wt.PV, T_Rx.PV, and Conc_MMA.PV).

3. There is no FF/DV in this example.

##### 8.1.1.2 Unit-Step Response Curve: Time to Steady State and Steady-State Gain

Figure 8.2 illustrates the step-response curve for a 2MV-1CV process, in which  $ CV_1 $ varies as a response to a step change of one unit of  $ MV_1 $. At time  $ t = 12\ \text{hr} $,  $ CV_1 $ no longer changes and reaches its steady-state value of 1.25 units. We call the time of 12 hr as the time to steady state ( $ T_{\text{ss}} $), and the ratio of the changes in values of CV1 to MV1 at steady state, that is,  $ \Delta CV_{1,\text{ss}} / \Delta MV_{1,\text{ss}} $ of 1.25/1.0, as the steady-state gain (SS gain).

##### 8.1.1.3 Integrating Variable (Ramp Variable)

Liquid level in a storage vessel with both steady inlet and exit flows is a typical ramp variable or integrating variable. Let us consider a cylindrical storage vessel

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>MV₁</th><th style='text-align: center;'>MV₂</th><th style='text-align: center;'>CV₁</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.3</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.6</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.7</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.2 A step response curve for  $ CV_1 $ in a 2MV-1CV process with a step change in  $ MV_1 $. Note the steady-state gain ( $ \Delta CV_{1,ss} / \Delta MV_{1,ss} $) and the time to steady state ( $ T_{ss} $).</div>


---

<!-- PDF page 474 -->

with inlet and exit liquid volumetric flow rates of  $ F_i $ and  $ F_0 $ m $ ^3 $/hr, respectively, a cross-sectional area of A m $ ^2 $, a liquid height of h m, and a liquid volume of V m $ ^3 $. See Figure 8.3.

A simple volume balance gives:

 $$ \mathrm{d}V/\mathrm{d}t=\mathrm{A}\mathrm{d}h/\mathrm{d}t=\mathrm{F}_{\mathrm{i}}-\mathrm{F}_{\mathrm{o}} $$ 

 $$ h=\left(\frac{1}{A}\right)\int_{0}^{t}[\mathrm{F_{i}}-\mathrm{F_{o}}]dt $$ 

Based on Eq. (8.2), we call the liquid level h an integrating variable or a ramp variable.

If the flow rate entering the vessel  $ F_{i} $ is increased and the exit flow rate  $ F_{o} $ is held fixed, the liquid level in the vessel increases. The flow exiting the vessel must be increased by the same amount to “balance the level.” Therefore, the level exhibits an integrating or a ramp response to changes to the inlet flow rate.

Figure 8.4 illustrates that for an integrating or ramp variable, the step response curve has a constant steady-state rate of change or slope of  $ \Delta(\mathrm{CV}_1)/\Delta(\mathrm{MV}_1) $, instead

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_580_773_810.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 8.3 Liquid level in a storage tank.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>MV₁</th><th style='text-align: center;'>MV₂</th><th style='text-align: center;'>CV₁</th><th style='text-align: center;'>CV₂</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.4 A step-response curve for CV1 in a 1MV-1CV integrating process with a step change in MV1.</div>


---

<!-- PDF page 475 -->

of a constant steady-state value as in Figure 8.2, and the “traditional” time to steady state  $ T_{ss} $ does not exist.

In addition to liquid level, we can cite examples for other pressure and temperature integrating variables. An example is the material imbalance ramp representing the pressure in a hydroprocessing reactor, for which the hydrogen pressure is a measure of the hydrogen consumption [5]. If the make-up hydrogen flow does not equal to the amount of hydrogen consumed in the reactor, then the pressure will either rise or fall. In this case, the pressure is a measure of the hydrogen material balance. Additionally, an example of an energy imbalance ramp is the dense-bed temperature in a fluid catalytic cracking (FCC) regenerator when the unit operates in a partial combustion mode [6]. This happens when the reactor temperature controller is operating in an automatic mode and continually changing the carbon balance on the catalyst. Breaking the reactor temperature controller will eliminate the ramp behavior in this case.

#### 8.1.2 Where Do the Benefits of APC Come from?

We describe three sources of the benefits of APC in this section.

##### 8.1.2.1 Online Reconciliation of Model-based Predictions to the Process Measurements to Provide Robustness to the Multivariable Dynamic Step-response Model

Multivariable Dynamic Model Extending the step-response model of Figure 8.2 to a system of multiple independent and dependent variables, we can develop a multi-variable step-response model to represent the time-dependent changes of controlled variables (CVs) to changes in MVs and FF/DVs. Workshop 8.1 in Section 8.2 gives the details of the development of a multivariable predictive controller model for our copolymerization process of Figure 8.1.

Figure 8.5 shows the resulting multivariable step-response model. In the plot, each column represents a dependent variable or a CV, and each row represents an independent variable, a MV, or a FF/DV. We typically arrange a FF/DV, if available, as a


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Orbital Input</td><td style='text-align: center; word-wrap: break-word;'>Typical Mode</td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>MOL_INT</td><td style='text-align: center; word-wrap: break-word;'>T_AIS</td><td style='text-align: center; word-wrap: break-word;'>OCRIC_JMA</td></tr><tr><td rowspan="2">PLDAL_JMA</td><td rowspan="2">1</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td rowspan="2">PLDAL_JX</td><td rowspan="2">1</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td rowspan="2">INT</td><td rowspan="2">1</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td rowspan="2">TRADSP</td><td rowspan="2">1</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td rowspan="2">T_JAT</td><td rowspan="2">1</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td><td style='text-align: center; word-wrap: break-word;'>0.001</td></tr></table>

<div style="text-align: center;">Figure 8.5 A multivariable step-response model for the copolymerization process.</div>


---

<!-- PDF page 476 -->

bottom row in the plot. For the copolymerization example, all 4 columns are CVs, all 5 rows are MVs, and there is no FF/DV. Note that in the plot, MV Flow_MMA has a negligible impact on CV T_RX, and the model does not show any step-response curve for the MV-CV pair, as the corresponding steady-state gains become negligible. The same is true for three other MV-CV pairs with no step-response curve.

In Figure 8.5, the number at the upper right corner of each step-response curve block represents the steady-state gain discussed in Figure 8.2. We can organize the displayed steady-state gains for all step-response curve blocks in a steady-state gain matrix, Eq. (8.3):


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>0.1715</td><td style='text-align: center; word-wrap: break-word;'>44.6648</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0661</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>0.3353</td><td style='text-align: center; word-wrap: break-word;'>21.1498</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>-0.3413</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>7.5180</td><td style='text-align: center; word-wrap: break-word;'>-424.1330</td><td style='text-align: center; word-wrap: break-word;'>-1.9756</td><td style='text-align: center; word-wrap: break-word;'>-1.4009</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>-67.7570</td><td style='text-align: center; word-wrap: break-word;'>-0.0964</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>1.6980</td><td style='text-align: center; word-wrap: break-word;'>21.0177</td><td style='text-align: center; word-wrap: break-word;'>1.2344</td><td style='text-align: center; word-wrap: break-word;'>0.0339</td></tr></table>

<div style="text-align: center;">This matrix represents the relationship in Eq. (8.4), which we will use below in introducing the steady-state optimization to obtain MV and CV targets to minimize the operating cost and maximize product profit:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_kJ}) $</td></tr></table>

Key Differences between Traditional PID Control and Advanced Process Control Figure 8.6 compares the traditional PID control and APC. A key difference between the two is that the traditional PID control aims at keeping a CV at its setpoint, while the APC maintains a CV between its specified lower and upper limits. Thus, an operator of an APC system is to specify the lower and upper limits of a CV, but not its setpoint.

From a control point of view, as long as MVs are within their lower and upper limits, and the predicted value of the CV from the dynamic process model is also within its lower and upper limits, then there is no need to vary the CV value and the corresponding values of MVs that affect this CV. This minimizes the frequency of adjusting the MVs that impact a chosen CV, thus greatly minimizing the fluctuations of CVs and enhancing the operational stability of the control system. Figure 8.7

---

<!-- PDF page 477 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_148_778_538.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.6 A comparison of traditional PID control (top) and advanced process control (bottom).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_631_778_870.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.7 Reduced variable fluctuations and increased profit by operating at economic optimum variable target.</div>


illustrates two facts: (1) APC could typically reduce the fluctuations of CVs by 30% or more; and (2) through a steady-state optimization step that we will discuss further below, APC typically operates at or near the lower or upper limits of CVs that minimize the steady-state operating cost and maximize the product profit, called the economic optimum variable target.

Continuing Reconciliation of Model-Based Predictions to the Process Measurements and Feedback Correction to Update the Model Predictions to the Future We illustrate a key aspect of predictive modeling of APC that makes it less sensitive to modeling errors and more accurate in predicting future CV responses [2]. Specifically, we consider a simple fire heater example in Figure 8.8, modified from Ref. [7].

Figure 8.9 shows the step response curve for the fired heater.

---

<!-- PDF page 478 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_146_406_260.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Figure 8.8 A simplified fire heater with two MVs (stream inlet temperature  $ T_{in} $ and input heat duty Q) and a CV (heating coil output temperature, COT).</div>


<div style="text-align: center;">Step-response curve for a fired heater</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>T_in</th><th style='text-align: center;'>COT (°C)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>650.5</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>651</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>651.5</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>652</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>652</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>652</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>652</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>652</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>652</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>ΔQ</th><th style='text-align: center;'>0°C</th><th style='text-align: center;'>1°C</th><th style='text-align: center;'>3°C</th><th style='text-align: center;'>4°C</th><th style='text-align: center;'>5°C</th><th style='text-align: center;'>5°C</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>3</td><td style='text-align: center;'>4</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>°C</th><th style='text-align: center;'>ΔCOT vs ΔT_in (=1)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.9 Step-response curve for a fired heater.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Feature</th><th style='text-align: center;'>Initial CV prediction</th><th style='text-align: center;'>Initial COT prediction</th><th style='text-align: center;'>Current time 12:01</th><th style='text-align: center;'>Current measured value</th><th style='text-align: center;'>ΔCOT due to ΔT_in</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Initial CV prediction</td><td style='text-align: center;'>710</td><td style='text-align: center;'>705</td><td style='text-align: center;'>695</td><td style='text-align: center;'>695</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>Initial COT prediction</td><td style='text-align: center;'>705</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>Online feedback correction of CV prediction based on measured value</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>695</td><td style='text-align: center;'>695</td><td style='text-align: center;'>700</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.10 Online feedback correction of CV prediction based on measured value from 12:00 to 12:01.</div>


Figures 8.10 and 8.11 demonstrate the continuing feedback corrections of the predicted CV responses based on measured CV values to minimize the prediction errors of CVs at the end of each sampling period of one minute.

In the middle plot of Figure 8.10, we see that the initial CV prediction (dark black curve) deviates from its measured value (dark square point) at 12:01. The online feedback correction shifts the CV prediction curve downward to match the measured CV value at 12:01 in the bottom plot. The black “real process” in the bottom plot also

---

<!-- PDF page 479 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Feature</th><th style='text-align: center;'>Current time</th><th style='text-align: center;'>Initial prediction</th><th style='text-align: center;'>ΔCOT due to ΔT_in</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:01</td><td style='text-align: center;'>12:01</td><td style='text-align: center;'>12:01</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:02</td><td style='text-align: center;'>12:02</td><td style='text-align: center;'>12:02</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:03</td><td style='text-align: center;'>12:03</td><td style='text-align: center;'>12:03</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:04</td><td style='text-align: center;'>12:04</td><td style='text-align: center;'>12:04</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:05</td><td style='text-align: center;'>12:05</td><td style='text-align: center;'>12:05</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:06</td><td style='text-align: center;'>12:06</td><td style='text-align: center;'>12:06</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:07</td><td style='text-align: center;'>12:07</td><td style='text-align: center;'>12:07</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:08</td><td style='text-align: center;'>12:08</td><td style='text-align: center;'>12:08</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:09</td><td style='text-align: center;'>12:09</td><td style='text-align: center;'>12:09</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:10</td><td style='text-align: center;'>12:10</td><td style='text-align: center;'>12:10</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:11</td><td style='text-align: center;'>12:11</td><td style='text-align: center;'>12:11</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:12</td><td style='text-align: center;'>12:12</td><td style='text-align: center;'>12:12</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:13</td><td style='text-align: center;'>12:13</td><td style='text-align: center;'>12:13</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:14</td><td style='text-align: center;'>12:14</td><td style='text-align: center;'>12:14</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:15</td><td style='text-align: center;'>12:15</td><td style='text-align: center;'>12:15</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:16</td><td style='text-align: center;'>12:16</td><td style='text-align: center;'>12:16</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:17</td><td style='text-align: center;'>12:17</td><td style='text-align: center;'>12:17</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:18</td><td style='text-align: center;'>12:18</td><td style='text-align: center;'>12:18</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:19</td><td style='text-align: center;'>12:19</td><td style='text-align: center;'>12:19</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:20</td><td style='text-align: center;'>12:20</td><td style='text-align: center;'>12:20</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:21</td><td style='text-align: center;'>12:21</td><td style='text-align: center;'>12:21</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:22</td><td style='text-align: center;'>12:22</td><td style='text-align: center;'>12:22</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:23</td><td style='text-align: center;'>12:23</td><td style='text-align: center;'>12:23</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:24</td><td style='text-align: center;'>12:24</td><td style='text-align: center;'>12:24</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:25</td><td style='text-align: center;'>12:25</td><td style='text-align: center;'>12:25</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:26</td><td style='text-align: center;'>12:26</td><td style='text-align: center;'>12:26</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:27</td><td style='text-align: center;'>12:27</td><td style='text-align: center;'>12:27</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:28</td><td style='text-align: center;'>12:28</td><td style='text-align: center;'>12:28</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:29</td><td style='text-align: center;'>12:29</td><td style='text-align: center;'>12:29</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:30</td><td style='text-align: center;'>12:30</td><td style='text-align: center;'>12:30</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:31</td><td style='text-align: center;'>12:31</td><td style='text-align: center;'>12:31</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:32</td><td style='text-align: center;'>12:32</td><td style='text-align: center;'>12:32</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:33</td><td style='text-align: center;'>12:33</td><td style='text-align: center;'>12:33</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:34</td><td style='text-align: center;'>12:34</td><td style='text-align: center;'>12:34</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:35</td><td style='text-align: center;'>12:35</td><td style='text-align: center;'>12:35</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:36</td><td style='text-align: center;'>12:36</td><td style='text-align: center;'>12:36</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:37</td><td style='text-align: center;'>12:37</td><td style='text-align: center;'>12:37</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:38</td><td style='text-align: center;'>12:38</td><td style='text-align: center;'>12:38</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:39</td><td style='text-align: center;'>12:39</td><td style='text-align: center;'>12:39</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:40</td><td style='text-align: center;'>12:40</td><td style='text-align: center;'>12:40</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:41</td><td style='text-align: center;'>12:41</td><td style='text-align: center;'>12:41</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:42</td><td style='text-align: center;'>12:42</td><td style='text-align: center;'>12:42</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:43</td><td style='text-align: center;'>12:43</td><td style='text-align: center;'>12:43</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:44</td><td style='text-align: center;'>12:44</td><td style='text-align: center;'>12:44</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:45</td><td style='text-align: center;'>12:45</td><td style='text-align: center;'>12:45</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:46</td><td style='text-align: center;'>12:46</td><td style='text-align: center;'>12:46</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:47</td><td style='text-align: center;'>12:47</td><td style='text-align: center;'>12:47</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:48</td><td style='text-align: center;'>12:48</td><td style='text-align: center;'>12:48</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:49</td><td style='text-align: center;'>12:49</td><td style='text-align: center;'>12:49</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:50</td><td style='text-align: center;'>12:50</td><td style='text-align: center;'>12:50</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:51</td><td style='text-align: center;'>12:51</td><td style='text-align: center;'>12:51</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:52</td><td style='text-align: center;'>12:52</td><td style='text-align: center;'>12:52</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:53</td><td style='text-align: center;'>12:53</td><td style='text-align: center;'>12:53</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:54</td><td style='text-align: center;'>12:54</td><td style='text-align: center;'>12:54</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:55</td><td style='text-align: center;'>12:55</td><td style='text-align: center;'>12:55</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:56</td><td style='text-align: center;'>12:56</td><td style='text-align: center;'>12:56</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:57</td><td style='text-align: center;'>12:57</td><td style='text-align: center;'>12:57</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:58</td><td style='text-align: center;'>12:58</td><td style='text-align: center;'>12:58</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:59</td><td style='text-align: center;'>12:59</td><td style='text-align: center;'>12:59</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:60</td><td style='text-align: center;'>12:60</td><td style='text-align: center;'>12:60</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:61</td><td style='text-align: center;'>12:61</td><td style='text-align: center;'>12:61</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:62</td><td style='text-align: center;'>12:62</td><td style='text-align: center;'>12:62</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:63</td><td style='text-align: center;'>12:63</td><td style='text-align: center;'>12:63</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:64</td><td style='text-align: center;'>12:64</td><td style='text-align: center;'>12:64</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:65</td><td style='text-align: center;'>12:65</td><td style='text-align: center;'>12:65</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:66</td><td style='text-align: center;'>12:66</td><td style='text-align: center;'>12:66</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:67</td><td style='text-align: center;'>12:67</td><td style='text-align: center;'>12:67</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:68</td><td style='text-align: center;'>12:68</td><td style='text-align: center;'>12:68</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:69</td><td style='text-align: center;'>12:69</td><td style='text-align: center;'>12:69</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:70</td><td style='text-align: center;'>12:70</td><td style='text-align: center;'>12:70</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:71</td><td style='text-align: center;'>12:71</td><td style='text-align: center;'>12:71</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:72</td><td style='text-align: center;'>12:72</td><td style='text-align: center;'>12:72</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:73</td><td style='text-align: center;'>12:73</td><td style='text-align: center;'>12:73</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:74</td><td style='text-align: center;'>12:74</td><td style='text-align: center;'>12:74</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:75</td><td style='text-align: center;'>12:75</td><td style='text-align: center;'>12:75</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:76</td><td style='text-align: center;'>12:76</td><td style='text-align: center;'>12:76</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:77</td><td style='text-align: center;'>12:77</td><td style='text-align: center;'>12:77</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:78</td><td style='text-align: center;'>12:78</td><td style='text-align: center;'>12:78</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:79</td><td style='text-align: center;'>12:79</td><td style='text-align: center;'>12:79</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:80</td><td style='text-align: center;'>12:80</td><td style='text-align: center;'>12:80</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:81</td><td style='text-align: center;'>12:81</td><td style='text-align: center;'>12:81</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:82</td><td style='text-align: center;'>12:82</td><td style='text-align: center;'>12:82</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:83</td><td style='text-align: center;'>12:83</td><td style='text-align: center;'>12:83</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:84</td><td style='text-align: center;'>12:84</td><td style='text-align: center;'>12:84</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:85</td><td style='text-align: center;'>12:85</td><td style='text-align: center;'>12:85</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:86</td><td style='text-align: center;'>12:86</td><td style='text-align: center;'>12:86</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:87</td><td style='text-align: center;'>12:87</td><td style='text-align: center;'>12:87</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:88</td><td style='text-align: center;'>12:88</td><td style='text-align: center;'>12:88</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:89</td><td style='text-align: center;'>12:89</td><td style='text-align: center;'>12:89</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:90</td><td style='text-align: center;'>12:90</td><td style='text-align: center;'>12:90</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:91</td><td style='text-align: center;'>12:91</td><td style='text-align: center;'>12:91</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:92</td><td style='text-align: center;'>12:92</td><td style='text-align: center;'>12:92</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:93</td><td style='text-align: center;'>12:93</td><td style='text-align: center;'>12:93</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:94</td><td style='text-align: center;'>12:94</td><td style='text-align: center;'>12:94</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:95</td><td style='text-align: center;'>12:95</td><td style='text-align: center;'>12:95</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:96</td><td style='text-align: center;'>12:96</td><td style='text-align: center;'>12:96</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:97</td><td style='text-align: center;'>12:97</td><td style='text-align: center;'>12:97</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:98</td><td style='text-align: center;'>12:98</td><td style='text-align: center;'>12:98</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>12:99</td><td style='text-align: center;'>12:99</td><td style='text-align: center;'>12:99</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:00</td><td style='text-align: center;'>13:00</td><td style='text-align: center;'>13:00</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:01</td><td style='text-align: center;'>13:01</td><td style='text-align: center;'>13:01</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:02</td><td style='text-align: center;'>13:02</td><td style='text-align: center;'>13:02</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:03</td><td style='text-align: center;'>13:03</td><td style='text-align: center;'>13:03</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:04</td><td style='text-align: center;'>13:04</td><td style='text-align: center;'>13:04</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:05</td><td style='text-align: center;'>13:05</td><td style='text-align: center;'>13:05</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:06</td><td style='text-align: center;'>13:06</td><td style='text-align: center;'>13:06</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:07</td><td style='text-align: center;'>13:07</td><td style='text-align: center;'>13:07</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:08</td><td style='text-align: center;'>13:08</td><td style='text-align: center;'>13:08</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:09</td><td style='text-align: center;'>13:09</td><td style='text-align: center;'>13:09</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:10</td><td style='text-align: center;'>13:10</td><td style='text-align: center;'>13:10</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:11</td><td style='text-align: center;'>13:11</td><td style='text-align: center;'>13:11</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:12</td><td style='text-align: center;'>13:12</td><td style='text-align: center;'>13:12</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:13</td><td style='text-align: center;'>13:13</td><td style='text-align: center;'>13:13</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:14</td><td style='text-align: center;'>13:14</td><td style='text-align: center;'>13:14</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:15</td><td style='text-align: center;'>13:15</td><td style='text-align: center;'>13:15</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:16</td><td style='text-align: center;'>13:16</td><td style='text-align: center;'>13:16</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:17</td><td style='text-align: center;'>13:17</td><td style='text-align: center;'>13:17</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:18</td><td style='text-align: center;'>13:18</td><td style='text-align: center;'>13:18</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:19</td><td style='text-align: center;'>13:19</td><td style='text-align: center;'>13:19</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:20</td><td style='text-align: center;'>13:20</td><td style='text-align: center;'>13:20</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:21</td><td style='text-align: center;'>13:21</td><td style='text-align: center;'>13:21</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:22</td><td style='text-align: center;'>13:22</td><td style='text-align: center;'>13:22</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:23</td><td style='text-align: center;'>13:23</td><td style='text-align: center;'>13:23</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:24</td><td style='text-align: center;'>13:24</td><td style='text-align: center;'>13:24</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:25</td><td style='text-align: center;'>13:25</td><td style='text-align: center;'>13:25</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:26</td><td style='text-align: center;'>13:26</td><td style='text-align: center;'>13:26</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13:27</td><td style='text-align: center;'>13:27</td><td style='text-align: center;'>13:27</td></tr>
    <tr><td style='text-align: center;'>Corrected prediction at 12:01</td><td style='text-align: center;'>13</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.11 Online feedback correction of CV prediction based on measured value from 12:01 to 12:02.</div>


shows that the deviation of the initial CV prediction only exists within a sampling period of one minute. At the end of a sampling period of one minute, that is, at 12:01, the online feedback correction based on the CV measured value completely eliminates the deviation.

Figure 8.11 repeats the same online feedback correction process, making the corrected CV prediction at 12:02 equal to the CV measured value.

Because the multivariable dynamic model based on step-response tests is data-driven and is not 100% accurate, APC strategy includes the online feedback corrections of initial CV predictions based on CV measured values to eliminate the CV prediction errors at the end of each sampling period. This approach reconciles the model-based predictions with the process measurements, and then feeds the information back to update the model predictions into the future [2]. This results in the robustness of the multivariable dynamic model in predicting accurately CV responses to changes in MVs, and this accurate model prediction capability represents the first source of benefits of APC.

##### 8.1.2.2 Steady-State Economic Optimization to Determine MV and CV Targets to Minimize Cost and Maximize Profit

The second source of benefits of APC results from the steady-state optimization to determine the MV and CV targets to minimize the cost and maximize the profit. Under the constraints of the lower and upper limits of all MVs and CVs, the DMC strategy typically minimizes a linear objective function of the form [7]:

 $$  Min\varphi=Cost_{1}\times\Delta MV_{1}+Cost_{2}\times\Delta MV_{2}+\ldots+Cost_{i}\times\Delta MV_{i} $$ 

where  $ Cost_{i} $ is essentially the steady-state gain:

 $$  Cost_{i}=\left(\frac{\Delta\phi}{\Delta MV_{i}}\right)_{\Delta MV_{j}}(j\neq i) $$ 

---

<!-- PDF page 480 -->

To minimize cost and maximize profit, we may write the objective function as

 $$ \begin{aligned}\varphi&=Cost-Profit\\&=(steady-state change in feed/utilities)*(cost of feed/utilities)\\&\quad-(steady-state change in production)*(value of products)\end{aligned} $$ 

For the copolymerization example, we write:

 $$ \begin{aligned}\varphi&=Cost-Profit\\&=\left\{\Delta Flow_{-}MMA\times(cost of Flow_{-}MMA)+\Delta Flow_{-}VA\times(cost of Flow_{-}VA)\right.\\&\quad+\Delta Flow_{-}INIT\times(cost of INIT)+\Delta Flow_{-}Transf\times(cost of Transf)\\&\quad+\Delta T_{jkt}\times(cost of T_{jkt})\}\\&\quad-\left\{\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}MMA)}\right)(\Delta Flow_{-}MMA)+\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}VA)}\right)(\Delta Flow_{-}VA)\right.\\&\quad+\left(\frac{\Delta(Polymer)}{\Delta(Init)}\right)(\Delta Flow_{-}INIT)+\left(\frac{\Delta(Polymer)}{\Delta(Transf)}\right)(\Delta Flow_{-}Transf)\\&\quad+\left(\frac{\Delta(Polymer)}{\Delta(T_{jkt})}\right)(\Delta T_{jkt})\right\}*\left(\\ value of polymer\right)\\&=\left\{\left(cost of Flow_{-}MMA\right)-\frac{\Delta(Polymer)}{\Delta(Flow_{-}MMA)}\right\}*\left(\\ value of polymer\right)\right\}*\Delta Flow_{-}MMA+\\&\quad\left\{(cost of Flow_{-}VA)-\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}VA)}\right)*\left(\\ value of polymer\right)\right\}*\Delta Flow_{-}VA+\\&\quad\left\{(cost of Flow_{-}INIT)-\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}INIT)}\right)*\left(\\ value of polymer\right)\right\}*\Delta Flow_{-}INIT+\\&\quad\left\{(cost of Flow_{-}Transf)-\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}Transf)}\right)*\left(\\ value of polymer\right)\right\}*\Delta Flow_{-}Transf+\\&\quad\left\{(cost of T_{jkt})-\left(\frac{\Delta(Polymer)}{\Delta(Flow_{-}VA)}\right)*\left(\\ value of polymer\right)\right\}*\Delta Flow_{-}VA\\&=\sum_{i=1}^{i=5}\quad\left[\left(cost of MV_{i,SS}-\frac{\Delta(Polymer)}{\Delta(MV_{i})}*(\value of polymer\right)\right]*(\Delta MV_{i,SS})\\&=\sum_{i=1}^{i=5}cost_{i}*\Delta MV_{i,SS}\end{aligned} $$ 

where the subscript SS represents steady state, and

 $$ \begin{aligned}Cost_{i}&=\left(\frac{\Delta\phi}{\Delta MV_{i}}\right)_{\Delta MV_{j}}(j\neq i)*(cost of MV_{i,SS})\\&\quad-\frac{\Delta(Polymer)}{\Delta(MV_{i})}*(Value of polymer)\end{aligned} $$ 

We call  $ Cost_i $ the steady-state LP cost that minimizes the objective function  $ \varphi $ (=cost - profit) by linear programming (LP). This minimization is constrained by the lower and upper limits of all MVs and CVs.

Figure 8.12 illustrates an Excel calculation of the steady-state LP costs (LP_Cost) based on the steady-state gains in Eq. (8.3), assuming the cost of  $ MV_{i,SS} $ (i = 1 to 5) to

---

<!-- PDF page 481 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>G</td><td style='text-align: center; word-wrap: break-word;'>H</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Economics</td><td style='text-align: center; word-wrap: break-word;'>CVj</td><td colspan="5">Copolymer LP Cost Calculation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>MVI</td><td style='text-align: center; word-wrap: break-word;'>Cost (+) or profit (-)</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>Mol_Wt</td><td style='text-align: center; word-wrap: break-word;'>T_Rx</td><td style='text-align: center; word-wrap: break-word;'>Conc_MMA</td><td style='text-align: center; word-wrap: break-word;'>LP_Cost</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Flow_MMA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$0.1715</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>-$0.1715</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>Flow_VA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$0.3363</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>-$0.3363</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>Init</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$7.9180</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>-$7.9180</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>Transf</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$67.7570</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$67.7570</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>T_jkt</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$1.6980</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>$0</td><td style='text-align: center; word-wrap: break-word;'>-$1.6980</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>SS Gains</td><td style='text-align: center; word-wrap: break-word;'>(ACV)/AMVjss</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>Flow_MMA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.1715</td><td style='text-align: center; word-wrap: break-word;'>44.6648</td><td style='text-align: center; word-wrap: break-word;'>0.0000</td><td style='text-align: center; word-wrap: break-word;'>0.0661</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>Flow_VA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.3353</td><td style='text-align: center; word-wrap: break-word;'>21.1498</td><td style='text-align: center; word-wrap: break-word;'>0.0000</td><td style='text-align: center; word-wrap: break-word;'>-0.3413</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>Init</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>7.8100</td><td style='text-align: center; word-wrap: break-word;'>-424.1330</td><td style='text-align: center; word-wrap: break-word;'>-1.9766</td><td style='text-align: center; word-wrap: break-word;'>-1.4009</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>Transf</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-$67.7570</td><td style='text-align: center; word-wrap: break-word;'>-0.0964</td><td style='text-align: center; word-wrap: break-word;'>0.0000</td><td style='text-align: center; word-wrap: break-word;'>0.0000</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>T_jkt</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1.6980</td><td style='text-align: center; word-wrap: break-word;'>21.0177</td><td style='text-align: center; word-wrap: break-word;'>1.2344</td><td style='text-align: center; word-wrap: break-word;'>-0.0339</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td colspan="7">Assume a value of 1 for the polymer flow</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">The resulting "relative" LP costs reduce to just the steady-state gains times minus one.</div>


<div style="text-align: center;">Figure 8.12 Excel calculation of steady-state LP costs.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>G</td><td style='text-align: center; word-wrap: break-word;'>H</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td rowspan="2">Economics</td><td rowspan="9">Cost (+) or profit (-)</td><td rowspan="9">CVj</td><td colspan="5">Copolymer LP Cost Calculation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Polymer</td><td style='text-align: center; word-wrap: break-word;'>Mol_Wt</td><td style='text-align: center; word-wrap: break-word;'>T_Rx</td><td style='text-align: center; word-wrap: break-word;'>Conc_MMA</td><td style='text-align: center; word-wrap: break-word;'>LP_Cost</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>MVI</td><td style='text-align: center; word-wrap: break-word;'>-1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Flow_MMA</td><td style='text-align: center; word-wrap: break-word;'>=D11*D33</td><td style='text-align: center; word-wrap: break-word;'>=E11*E33</td><td style='text-align: center; word-wrap: break-word;'>=F11*F33</td><td style='text-align: center; word-wrap: break-word;'>=G11*G33</td><td style='text-align: center; word-wrap: break-word;'>=SUM(C5:F5)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>Flow_VA</td><td style='text-align: center; word-wrap: break-word;'>=D12*D33</td><td style='text-align: center; word-wrap: break-word;'>=E12*E33</td><td style='text-align: center; word-wrap: break-word;'>=F12*F33</td><td style='text-align: center; word-wrap: break-word;'>=G12*G33</td><td style='text-align: center; word-wrap: break-word;'>=SUM(C6:F6)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>Init</td><td style='text-align: center; word-wrap: break-word;'>=D13*D33</td><td style='text-align: center; word-wrap: break-word;'>=E13*E33</td><td style='text-align: center; word-wrap: break-word;'>=F13*F33</td><td style='text-align: center; word-wrap: break-word;'>=G13*G33</td><td style='text-align: center; word-wrap: break-word;'>=SUM(C6:F6)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>Transf</td><td style='text-align: center; word-wrap: break-word;'>=D14*D33</td><td style='text-align: center; word-wrap: break-word;'>=E14*E33</td><td style='text-align: center; word-wrap: break-word;'>=F14*F33</td><td style='text-align: center; word-wrap: break-word;'>=G14*G33</td><td style='text-align: center; word-wrap: break-word;'>=SUM(C7:F7)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td rowspan="2">T_jkt</td><td rowspan="2">=D15*D33</td><td rowspan="2">=E15*E33</td><td rowspan="2">=F15*F33</td><td rowspan="2">=G15*G33</td><td rowspan="2">=SUM(C8:F8)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>SS Gains</td><td rowspan="7">(aCVj/aMVi)ss</td><td rowspan="7"></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>Flow_MMA</td><td style='text-align: center; word-wrap: break-word;'>0.171458</td><td style='text-align: center; word-wrap: break-word;'>44.6648</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.066125</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>Flow_VA</td><td style='text-align: center; word-wrap: break-word;'>0.33528</td><td style='text-align: center; word-wrap: break-word;'>21.14978</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>-0.34125</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>Init</td><td style='text-align: center; word-wrap: break-word;'>7.51802</td><td style='text-align: center; word-wrap: break-word;'>-424.133</td><td style='text-align: center; word-wrap: break-word;'>-1.97563</td><td style='text-align: center; word-wrap: break-word;'>-1.40089</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>Transf</td><td style='text-align: center; word-wrap: break-word;'>-67.757</td><td style='text-align: center; word-wrap: break-word;'>-0.0964</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td rowspan="2">T_jkt</td><td rowspan="2">1.69798</td><td rowspan="2">21.0177</td><td rowspan="2">1.23442</td><td rowspan="2">-0.0339115</td><td rowspan="2"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td></tr></table>

<div style="text-align: center;">Figure 8.13 Formulas for Excel calculation of steady-state LP costs.</div>


be insignificant when compared to the profit of polymer products (if this is not true, we can enter the cost of  $ MV_{i,SS} $, i = 1 to 5, into the spreadsheet). We also assume the profit for 1 kg/hr of polymer product to be US1. Figure 8.13 shows the calculation formulas for the LP_Cost.

We wish to minimize the objective function  $ \varphi\,(=\,cost\,-\,profit) $ following Eq. (8.8). Based on the calculated steady-state LP costs, Cost $ _{i} $, in Figure 8.12, should we move a specific MV $ _{i} $ toward its lower limit or upper limit? In other words, what is the MV $ _{i} $ target value based on steady-state optimization to minimize cost and maximize profit? The resulting MV $ _{i} $ target value appears in Table 8.1. We note that the CV $ _{j} $

<div style="text-align: center;">Table 8.1 Recommended MV $ _{i} $ target value based on steady-state optimization to minimize cost and maximize profit.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{i} $</td><td style='text-align: center; word-wrap: break-word;'>Cost $ _{i} $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta MV_{i,ss} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{1} $: Flow_MMA</td><td style='text-align: center; word-wrap: break-word;'>-0.1716</td><td style='text-align: center; word-wrap: break-word;'>Small positive increase toward upper limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{2} $: Flow_VA</td><td style='text-align: center; word-wrap: break-word;'>-0.3353</td><td style='text-align: center; word-wrap: break-word;'>Small positive increase toward upper limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{3} $: Flow_INIT</td><td style='text-align: center; word-wrap: break-word;'>-7.7518</td><td style='text-align: center; word-wrap: break-word;'>Large positive increase toward upper limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{4} $: Flow_Transf</td><td style='text-align: center; word-wrap: break-word;'>+67.760</td><td style='text-align: center; word-wrap: break-word;'>Large negative decrease toward lower limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ MV_{5} $:  $ T_{jkt} $</td><td style='text-align: center; word-wrap: break-word;'>-1.1980</td><td style='text-align: center; word-wrap: break-word;'>Medium positive increase toward upper limit</td></tr></table>

---

<!-- PDF page 482 -->

target value is to maximize the polymer production within the given lower and upper limits.

This example illustrates how DMC uses the steady-state optimization to identify the economic optimum steady-state MV and CV target values to minimize cost and maximize profit, which represents the second source of benefits of APC.

##### 8.1.2.3 Determination of Future MV Moves to Minimize the Least-Squares Errors Between Predicted and Desired Economic Optimum Target Values of CVs

Having identified the economic optimum steady-state MV and CV targets, the DMC strategy determines a set of future MV adjustments that will drive the CV to its desired economic optimum operating point without violating the lower and upper limits of MVs and CVs. Figure 8.14 shows the open-loop CV prediction reflecting the effects of past MV changes and the error between the predicted CV value and its set-point or the economic optimum target value [7]. The desired future response of each CV is to have it reach its setpoint or economic optimum, steady-state target value. Figure 8.15 illustrates the desired future CV response that is defined by the mirror image of the CV prediction about the setpoint or economic optimum steady-state target value [2]. Figure 8.16 displays the development of MV moves to minimize the least-squares errors between the predicted and desired values of CVs. We will

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>MV</th><th style='text-align: center;'>CV</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>100</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>100</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>100</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>100</td><td style='text-align: center;'>40</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>100</td><td style='text-align: center;'>30</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>100</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>100</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.14 The open-loop CV prediction reflecting the effects of past MV changes and the shaded area of errors between the CV prediction and its setpoint or economic optimum target value.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Event</th><th style='text-align: center;'>Time</th><th style='text-align: center;'>Setpoint: Economic Optimum CV Target</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Open-loop CV prediction</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>Open-loop CV prediction</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>Open-loop CV prediction</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Desired future CV response</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>Desired future CV response</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>Desired future CV response</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Desired future CV response</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.15 An illustration of the desired future CV response that best fits the mirror image of the CV prediction about the setpoint. The shaded area represents the CV errors.</div>


---

<!-- PDF page 483 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_766_426.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 8.16 An illustration of the development of MV moves to minimize the lease-squares errors between predicted and desired values of CVs.</div>


demonstrate this step quantitatively in Section 8.2.12 below. Depending on the time to steady state, sampling period, and controller execution interval, the DMC strategy calculates 8 to 14 future moves of each MV extending approximately one-half of the time to steady state into the future (see Section 8.2.7). This step of dynamic control execution to reach economic optimum steady-state MV and CV targets represents the third source of benefits of APC.

To summarize, in Sections 8.1.2.1–8.1.2.3, we have introduced three aspects of the DMC strategy that represent the sources of benefits of APC: (1) model CV prediction and reconciliation to online measurements: continuing reconciliation of model-based predictions to the process measurements and feedback correction to update the model predictions for the future; (2) steady-state economic optimization: steady-state economic optimization to determine MV and CV targets to minimize cost and maximize profit; and (3) dynamic control execution to reach MV and CV targets: determination of future MV moves to minimize the least-squares errors between predicted and desired economic optimum target values of CVs. In Figure 8.17, we

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_913_694_1225.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 8.17 The Aspen DMCplus control structure illustrates three sources of benefits of APC [7]. Used with permission from Aspen Technology, Inc.</div>


---

<!-- PDF page 484 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_143_807_327.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.18 The Aspen DMC3 control structure [7]. Used with permission from Aspen Technology, Inc.</div>


have modified a diagram in Ref. [7] to illustrate these three sources of benefits of APC in the context of the DMCplus control structure.

Figure 8.18 shows the Aspen DMC3 control structure taken from the DMC3 online help that extends the DMC control structure to provide more robust dynamic control. We note the five key blocks or controller applications in the figure. We follow the DMC3 online help to briefly describe these blocks or controller applications below.

(1) The “plant” (“process”) block or controller application: The “plant” stage of application development occurs in the controller deployment stage, where we specify input/output (or MV/CV) connection parameters to prepare the controller for online operation.

(2) The “model” block or controller application: It represents the “controller model” that we will discuss in detail beginning in Section 8.1.3.

(3) The “SS (steady-state) optimizer” block or controller application: It performs the “steady-state economic optimization” to find the MV and CV targets, as we illustrated in Section 8.1.2.2. In other words, the SS optimizer determines the best steady-state operating point for the plant, subject to the constraints for MVs and CVs.

(4) The “controller or path optimizer” block or controller application: It represents “the dynamic control execution” to reach MV and CV targets, or externally specified MV and CV targets that we will discuss more in Section 8.1.6.4 below. This application develops the move plan to take the plant from its current operating point to the economic optimum steady-state targets or externally specified targets with minimum least-squares errors, while respecting MV and CV constraints.

(5) The “filter” block or controller application: It compares the model predictions of CVs with the actual measured CV values at each execution. The filter application helps us understand the current prediction errors by estimating the size of unmeasured disturbances that enter the plant. This comparison tells us where the process is currently operating, and which direction the CVs will go if the MVs remain constant. Disturbance and dynamic state estimate from the filter are then passed to the optimizer.

---

<!-- PDF page 485 -->

#### 8.1.3 Linear Modeling for Dynamic Matrix Control (DMC)

##### 8.1.3.1 Step-Response Model

We use a simple step-response curve of Figure 8.19 to develop a linear matrix-based dynamic process model. In the figure, the MV has a unit step change at time zero, that is,  $ \Delta MV_0 = 1 $.

Based on Figure 8.19, we write the following relationships:

 $$ \begin{aligned}\Delta\mathrm{CV}_{1}&=\mathrm{CV}_{1}-\mathrm{CV}_{0}=1*\Delta\mathrm{MV}_{0}=a_{1}*\Delta\mathrm{MV}_{0}\\\Delta\mathrm{CV}_{2}&=\mathrm{CV}_{2}-\mathrm{CV}_{0}=3*\Delta\mathrm{MV}_{0}=a_{2}*\Delta\mathrm{MV}_{0}\\\Delta\mathrm{CV}_{3}&=\mathrm{CV}_{3}-\mathrm{CV}_{0}=4.3*\Delta\mathrm{MV}_{0}=a_{3}*\Delta\mathrm{MV}_{0}\\\Delta\mathrm{CV}_{4}&=\mathrm{CV}_{4}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}=a_{4}*\Delta\mathrm{MV}_{0}\\\Delta\mathrm{CV}_{5}&=\mathrm{CV}_{5}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}=a_{5}*\Delta\mathrm{MV}_{0}\end{aligned} $$ 

We illustrate two characteristics of the linearity of the process model in Figures 8.20 and 8.21.

The first characteristic is the preservation of scale, which suggests that if we increase the step change of MV at time zero by four times, that is,  $ \Delta MV_0 = 1 $ to

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time, minute</th><th style='text-align: center;'>CV</th><th style='text-align: center;'>CV₀</th><th style='text-align: center;'>CV₁</th><th style='text-align: center;'>CV₂</th><th style='text-align: center;'>CV₃</th><th style='text-align: center;'>CV₄</th><th style='text-align: center;'>CV₅</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>MV</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>+1</td><td style='text-align: center;'>+1</td></tr>
    <tr><td style='text-align: center;'>Step change</td><td style='text-align: center;'>ΔMV₀ = 1</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.19 Representation of a continuous step response curve by a series of discrete values  $ CV_0 $,  $ CV_1 $,  $ CV_2 $, ..., at time  $ t=1, 2, 3, \ldots $ minute for a unit step change of MV at time zero,  $ \Delta MV_0 = 1 $.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>CV</th><th style='text-align: center;'>CV₀</th><th style='text-align: center;'>CV₁</th><th style='text-align: center;'>CV₂</th><th style='text-align: center;'>CV₃</th><th style='text-align: center;'>CV₄</th><th style='text-align: center;'>CV₅</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.20 An illustration of the model linearity, i.e. preservation of scale, with reference to Figure 8.19.</div>


---

<!-- PDF page 486 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (min)</th><th style='text-align: center;'>CV response curve for ΔMV₀ = 1</th><th style='text-align: center;'>CV response curve for ΔMV₀ = 3</th><th style='text-align: center;'>CV response curve for ΔMV₀ = 2.3</th><th style='text-align: center;'>CV response curve for ΔMV₀ = -2</th><th style='text-align: center;'>CV response curve for both ΔMV₀ = 1 and ΔMV₂ = -2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>4.3</td><td style='text-align: center;'>-2</td><td style='text-align: center;'>-3.6</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>-6</td><td style='text-align: center;'>-8.6</td></tr>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>-8.6</td><td style='text-align: center;'>-10</td></tr>
    <tr><td style='text-align: center;'>-5</td><td style='text-align: center;'>-4.5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>-10</td><td style='text-align: center;'>-10</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.21 An illustration of the superposition principle of model linearity, adding the CV response curve for  $ \Delta MV_2 $ to the CV response curve for  $ \Delta MV_0 $.</div>


 $ \Delta MV_0 = 4 $,  $ \Delta CV_i $ ( $ i = 1 $ to 5, ...) will also increase four times, as seen in Figure 8.20. The second characteristic is the superposition principle; in Figure 8.21, we add the CV response curve for  $ \Delta MV_2 $ to the CV response curve for  $ \Delta MV_0 $. Extending Eq. (8.11), we write the following relationship for Figure 8.21:

 $$ \Delta CV_{1}=CV_{1}-CV_{0}=1^{*}\Delta MV_{0}=a_{1}^{*}\Delta MV_{0}=(1)^{*}(1)=1 $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{2}&=\mathrm{CV}_{2}-\mathrm{CV}_{0}=3^{*}\Delta\mathrm{MV}_{0}+1^{*}\Delta\mathrm{MV}_{1}=a_{2}^{*}\Delta\mathrm{MV}_{0}+a_{1}^{*}\Delta\mathrm{MV}_{1}\\&=3^{*}(1)+1^{*}(0)=3\end{aligned} $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{3}&=\mathrm{CV}_{3}-\mathrm{CV}_{0}=4.3*\Delta\mathrm{MV}_{0}+3*\Delta\mathrm{MV}_{1}+1*\Delta\mathrm{MV}_{2}\\&=a_{3}*\Delta\mathrm{MV}_{0}+a_{2}*\Delta\mathrm{MV}_{1}+a_{1}*\Delta\mathrm{MV}_{2}\\&=4.3*(1)+3*(0)+1*(-2)=2.3\end{aligned} $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{4}&=\mathrm{CV}_{4}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}+4.3*\Delta\mathrm{MV}_{1}+3*\Delta\mathrm{MV}_{2}\\&=a_{4}*\Delta\mathrm{MV}_{0}+a_{3}*\Delta\mathrm{MV}_{1}+a_{2}*\Delta\mathrm{MV}_{2}\\&=5*(1)+4.3*(0)+3*(-2)=-1\end{aligned} $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{5}&=\mathrm{CV}_{5}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}+5*\Delta\mathrm{MV}_{1}+4.3*\Delta\mathrm{MV}_{2}\\&=a_{5}*\Delta\mathrm{MV}_{0}+a_{4}*\Delta\mathrm{MV}_{1}+a_{3}*\Delta\mathrm{MV}_{2}\\&=5*(1)+5*(0)+4.3*(-2)=-3.6\end{aligned} $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{6}&=\mathrm{CV}_{6}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}+5*\Delta\mathrm{MV}_{1}+4.3*\Delta\mathrm{MV}_{2}\\&=a_{6}*\Delta\mathrm{MV}_{0}+a_{5}*\Delta\mathrm{MV}_{1}+a_{4}*\Delta\mathrm{MV}_{2}\\&=5*(1)+5*(0)+5*(-2)=-5\end{aligned} $$ 

 $$ \begin{aligned}\Delta\mathrm{CV}_{7}&=\mathrm{CV}_{7}-\mathrm{CV}_{0}=5*\Delta\mathrm{MV}_{0}+5*\Delta\mathrm{MV}_{1}+5*\Delta\mathrm{MV}_{2}\\&=a_{7}*\Delta\mathrm{MV}_{0}+a_{6}*\Delta\mathrm{MV}_{1}+a_{5}*\Delta\mathrm{MV}_{2}\\&=5*(1)+5*(0)+5*(-2)=-5\end{aligned} $$ 

---

<!-- PDF page 487 -->

We may re-write Eq. (8.11a–8.11g) in a matrix form:

 $$ \begin{aligned}\begin{bmatrix}{{{\Delta\mathrm{CV}_{1}}}} \\{{{\Delta\mathrm{CV}_{2}}}} \\{{{\Delta\mathrm{CV}_{3}}}} \\{{{\Delta\mathrm{CV}_{4}}}} \\{{{\Delta\mathrm{CV}_{5}}}} \\{{{\Delta\mathrm{CV}_{6}}}} \\{{{\Delta\mathrm{CV}_{7}}}}\end{bmatrix}&=\begin{bmatrix}{{{1}}}&{{{0}}}&{{{0}}} \\{{{3}}}&{{{1}}}&{{{0}}} \\{{{4.3}}}&{{{3}}}&{{{1}}} \\{{{5}}}&{{{4.3}}}&{{{3}}} \\{{{5}}}&{{{5}}}&{{{4.3}}} \\{{{5}}}&{{{5}}}&{{{5}}} \\{{{5}}}&{{{5}}}&{{{5}}}\end{bmatrix}\begin{bmatrix}{{{\Delta\mathrm{MV}_{1}}}} \\{{{\Delta\mathrm{MV}_{2}}}} \\{{{\Delta\mathrm{MV}_{3}}}}\end{bmatrix}=\begin{bmatrix}{{{a_{1}}}}&{{{0}}}&{{{0}}} \\{{{a_{2}}}}&{{{a_{1}}}}&{{{0}}} \\{{{a_{3}}}}&{{{a_{2}}}}&{{{a_{1}}}} \\{{{a_{4}}}}&{{{a_{3}}}}&{{{a_{2}}}} \\{{{a_{5}}}}&{{{a_{4}}}}&{{{a_{3}}}} \\{{{a_{6}}}}&{{{a_{5}}}}&{{{a_{4}}}} \\{{{a_{7}}}}&{{{a_{6}}}}&{{{a_{5}}}}\end{bmatrix}\begin{bmatrix}{{{\Delta\mathrm{MV}_{1}}}} \\{{{\Delta\mathrm{MV}_{2}}}} \\{{{\Delta\mathrm{MV}_{3}}}}\end{bmatrix}\end{aligned} $$ 

For this example,  $ a_4 = a_5 = a_6 = a_7 $, implying that the process reaches its steady state when time  $ t = 5 \text{ min} $. Additionally,  $ \Delta \text{MV}_4 = \Delta \text{MV}_5 = \Delta \text{MV}_6 = \Delta \text{MV}_7 = 0 $.

We write the time-dependent or dynamic linear matrix equation, Eq. (8.12), in a general matrix form that represents the step-response model:

 $$ \mathbf{\Delta C V}=\mathbf{A}^{*}\mathbf{\Delta M V} $$ 

Eq. (8.13) is the foundational model for DMC. It represents three classes of problems.

1. Prediction: Knowing the model matrix A and MV move vector  $ \Delta MV $, calculate the resulting CV change vector  $ \Delta CV $.

2. Control: Knowing the control change vector  $ \Delta CV $ and the model matrix A, find the required MV move vector  $ \Delta MV $.

3. Identification or modeling: Knowing the MV move vector and the resulting CV change vector, find the corresponding model matrix A.

##### 8.1.3.2 Finite-Impulse Response (FIR) Model

Figure 8.22 illustrates that in actual practice, there could be missing input data for MV for a certain time duration, and discontinuous CV response curve with CV instrument failure. The figure shows only three slices of valid MV-CV response curves. We call the process of identifying slices of good continuous MV-CV response curves without any instrument failure or missing data as “data slicing.” We show below how to modify our modeling equations, (8.11a) to (8.11g), to represent discontinuous MV-CV response curves.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Parameter</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Slice 1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Slice 2</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>Slice 3</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>Missing data</td><td style='text-align: center;'>4</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.22 An illustration of discontinuous MV–CV response curves with missing MV input data and CV instrument failure, resulting in three slices of valid MV–CV response curves.</div>


---

<!-- PDF page 488 -->

First, we write Eqs. (8.11b) and (8.11a) as follows:

 $$ \mathrm{CV}_{2}-\mathrm{CV}_{0}=a_{2}^{*}\Delta\mathrm{MV}_{0}+a_{1}^{*}\Delta\mathrm{MV}_{1} $$ 

 $$ \mathbf{C}\mathbf{V}_{1}-\mathbf{C}\mathbf{V}_{0}=a_{1}^{*}\Delta\mathbf{M}\mathbf{V}_{0} $$ 

Subtracting Eq. (8.11b) by Eq. (8.11a), to remove  $ CV_{0} $ and we get:

 $$ \mathbf{C}\mathbf{V}_{2}-\mathbf{C}\mathbf{V}_{1}=\mathbf{a}_{1}^{*}\Delta\mathbf{M}\mathbf{V}_{1}+(\mathbf{a}_{2}-\mathbf{a}_{1})*\Delta\mathbf{M}\mathbf{V}_{0} $$ 

Next, we write Eqs. (8.11c) and (8.11b) as follows:

 $$ \mathrm{CV}_{3}-\mathrm{CV}_{0}=a_{3}^{*}\Delta\mathrm{MV}_{0}+a_{2}^{*}\Delta\mathrm{MV}_{1}+a_{1}^{*}\Delta\mathrm{MV}_{2} $$ 

 $$  CV_{2}-CV_{0}=a_{2}^{*}\Delta MV_{0}+a_{1}^{*}\Delta MV_{1}\quad(8.11b) $$ 

Subtracting Eq. (8.11c) by Eq. (8.11b) gives

 $$ \mathbf{C}\mathbf{V}_{3}-\mathbf{C}\mathbf{V}_{2}=\mathbf{a}_{1}^{*}\Delta\mathbf{M}\mathbf{V}_{2}+(\mathbf{a}_{2}-\mathbf{a}_{1})^{*}\Delta\mathbf{M}\mathbf{V}_{1}+(\mathbf{a}_{3}-\mathbf{a}_{2})*\Delta\mathbf{M}\mathbf{V}_{0} $$ 

Following the same procedure, we can get:

 $$ \begin{aligned}\mathbf{C}\mathbf{V}_{4}-\mathbf{C}\mathbf{V}_{3}&=\mathbf{a}_{1}^{*}\Delta\mathbf{M}\mathbf{V}_{3}+(\mathbf{a}_{2}-\mathbf{a}_{1})*\Delta\mathbf{M}\mathbf{V}_{2}+(\mathbf{a}_{3}-\mathbf{a}_{2})*\Delta\mathbf{M}\mathbf{V}_{1}\\&+(\mathbf{a}_{4}-\mathbf{a}_{3})*\Delta\mathbf{M}\mathbf{V}_{0}\\\mathbf{C}\mathbf{V}_{5}-\mathbf{C}\mathbf{V}_{4}&=\mathbf{a}_{1}^{*}\Delta\mathbf{M}\mathbf{V}_{4}+(\mathbf{a}_{2}-\mathbf{a}_{1})*\Delta\mathbf{M}\mathbf{V}_{3}+(\mathbf{a}_{3}-\mathbf{a}_{2})*\Delta\mathbf{M}\mathbf{V}_{2}\\&+(\mathbf{a}_{4}-\mathbf{a}_{3})*\Delta\mathbf{M}\mathbf{V}_{1}+(\mathbf{a}_{5}-\mathbf{a}_{4})*\Delta\mathbf{M}\mathbf{V}_{0}\end{aligned} $$ 

For convenience, let us define a new set of model coefficients  $ b_{i} $ as follows:

 $$ b_{1}=a_{1}\quad b_{2}=a_{2}-a_{1}\quad b_{3}=a_{3}-a_{2}\quad b_{4}=a_{4}-a_{3}\quad b_{5}=a_{5}-a_{4} $$ 

We also write

 $$ \mathrm{a}CV_{i}=\mathrm{CV}_{i}-\mathrm{CV}_{i-1} $$ 

which applies to any slice of continuous CV response curve with two neighboring CV values,  $ CV_{i} $ and  $ CV_{i-1} $. Eq. (8.16) is different from Eq. (8.11),

 $$ \Delta C V_{i}=C V_{i}-C V_{0} $$ 

which assumes a continuous CV response curve from CV₀ to CV₁.

Applying Eqs. (8.15) and (8.16) to Eqs. (8.11a), (8.14a) to (8.14d) gives the following “impulse form” of our model equations:

 $$ \begin{aligned}&\partial\mathrm{CV}_{1}=b_{1}*\Delta\mathrm{MV}_{0}\\&\partial\mathrm{CV}_{2}=b_{1}*\Delta\mathrm{MV}_{1}+b_{2}*\Delta\mathrm{MV}_{0}\\&\partial\mathrm{CV}_{3}=b_{1}*\Delta\mathrm{MV}_{2}+b_{2}*\Delta\mathrm{MV}_{1}+b_{3}*\Delta\mathrm{MV}_{0}\\&\partial\mathrm{CV}_{4}=b_{1}*\Delta\mathrm{MV}_{3}+b_{2}*\Delta\mathrm{MV}_{2}+b_{3}*\Delta\mathrm{MV}_{1}+b_{4}*\Delta\mathrm{MV}_{0}\\&\partial\mathrm{CV}_{5}=b_{1}*\Delta\mathrm{MV}_{4}+b_{2}*\Delta\mathrm{MV}_{3}+b_{3}*\Delta\mathrm{MV}_{2}+b_{4}*\Delta\mathrm{MV}_{1}+b_{5}*\Delta\mathrm{MV}_{0}\end{aligned} $$ 

---

<!-- PDF page 489 -->

We write the resulting “impulse form” of our dynamic matrix model equation as follows:

 $$ \begin{bmatrix}{{{\partial\mathrm{CV}_{1}}}} \\{{{\partial\mathrm{CV}_{2}}}} \\{{{\partial\mathrm{CV}_{3}}}} \\{{{\partial\mathrm{CV}_{4}}}} \\{{{\partial\mathrm{CV}_{5}}}}\end{bmatrix}=\begin{bmatrix}{{{b_{1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{b_{2}}}}&{{{b_{1}}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{b_{3}}}}&{{{b_{2}}}}&{{{b_{1}}}}&{{{0}}}&{{{0}}} \\{{{b_{4}}}}&{{{b_{3}}}}&{{{b_{2}}}}&{{{b_{1}}}}&{{{0}}} \\{{{b_{5}}}}&{{{b_{4}}}}&{{{b_{3}}}}&{{{b_{2}}}}&{{{b_{1}}}}\end{bmatrix}\begin{bmatrix}{{{\Delta\mathrm{MV}_{0}}}} \\{{{\Delta\mathrm{MV}_{1}}}} \\{{{\Delta\mathrm{MV}_{2}}}} \\{{{\Delta\mathrm{MV}_{3}}}} \\{{{\Delta\mathrm{MV}_{4}}}}\end{bmatrix} $$ 

In a matrix form, Eq. (8.18) becomes

 $$ \mathbf{a}\mathbf{C}\mathbf{V}=\mathbf{B}^{*}\Delta\mathbf{M}\mathbf{V} $$ 

Eq. (8.19) represents the FIR form of the linear model equation for DMC. We can extend Eq. (8.19) to allow more than one MV to vary at the same time to give Eq. (8.20).

 $$ \begin{aligned}\begin{bmatrix}{{{\partial C V_{1}}}} \\{{{\partial C V_{2}}}} \\{{{\partial C V_{3}}}} \\{{{\partial C V_{4}}}} \\{{{\partial C V_{5}}}}\end{bmatrix}&=\begin{bmatrix}{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,4}}}}&{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}} \\{{{\Delta M V_{1,5}}}}&{{{\Delta M V_{1,4}}}}&{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{\Delta M V_{2,5}}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}\end{bmatrix}\begin{bmatrix}{{{b_{1,1}}}} \\{{{b_{1,2}}}} \\{{{b_{1,3}}}} \\{{{b_{1,4}}}} \\{{{b_{1,5}}}} \\{{{b_{2,1}}}} \\{{{b_{2,2}}}} \\{{{b_{2,3}}}} \\{{{b_{2,4}}}} \\{{{b_{2,5}}}}\end{bmatrix}\\ \end{aligned} $$ 

To identify the model coefficients  $ b_{i,j} $ or matrix B, we convert Eq.(8.20) to a residual form involving the error residual  $ r_{i,j} $:

 $$ \begin{bmatrix}{{{\partial C V_{1}}}} \\{{{\partial C V_{2}}}} \\{{{\partial C V_{3}}}} \\{{{\partial C V_{4}}}} \\{{{\partial C V_{5}}}}\end{bmatrix}=\begin{bmatrix}{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{0}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}}&{{{0}}} \\{{{\Delta M V_{1,4}}}}&{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{0}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{0}}} \\{{{\Delta M V_{1,5}}}}&{{{\Delta M V_{1,4}}}}&{{{\Delta M V_{1,3}}}}&{{{\Delta M V_{1,2}}}}&{{{\Delta M V_{1,1}}}}&{{{\Delta M V_{2,5}}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}} \\{{{\Delta M V_{2,5}}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,1}}}}&{{{\Delta M V_{2,4}}}}&{{{\Delta M V_{2,5}}}}&{{{\Delta M V_{2,3}}}}&{{{\Delta M V_{2,2}}}}&{{{\Delta M V_{2,1}}}}&{{{\Delta M V_{2,1}}}}\end{bmatrix}\begin{bmatrix}{{{b_{1,1}}}} \\{{{b_{1,2}}}} \\{{{b_{1,3}}}} \\{{{b_{1,4}}}} \\{{{b_{1,5}}}} \\{{{b_{2,1}}}} \\{{{b_{2,2}}}} \\{{{b_{2,3}}}} \\{{{b_{2,4}}}} \\{{{b_{2,5}}}}\end{bmatrix}=\begin{bmatrix}{{{r_{1,1}}}} \\{{{r_{1,2}}}} \\{{{r_{1,3}}}} \\{{{r_{1,4}}}} \\{{{r_{1,5}}}} \\{{{r_{2,1}}}} \\{{{r_{2,2}}}} \\{{{r_{2,3}}}} \\{{{r_{2,4}}}} \\{{{r_{2,5}}}}\end{bmatrix} $$ 

We typically find the values of the model coefficients  $ b_{i,j} $ or matrix B, by minimizing the sum of the squared residual error terms:

 $$ \mathrm{Min}\sum r_{i,j}^{2}=\mathrm{Min}\left(r_{1,1}^{2}+r_{1,2}^{2}+r_{1,3}^{2}+r_{1,4}^{2}+r_{1,5}^{2}+r_{2,1}^{2}+r_{2,2}^{2}+r_{2,3}^{2}+r_{2,4}^{2}+r_{2,5}^{2}\right) $$ 

To summarize, the FIR model identification procedure discussed so far has incorporated effective means to handle several practical issues for MPC in the

---

<!-- PDF page 490 -->

real world: (1) The data slicing permits the use of discontinuous MV–CV response curves with missing MV input data and CV instrument failure; (2) The procedure works with the incremental or “delta” world (∂CVᵢ or ΔCVᵢ), thus not requiring the process to be at a steady state; and (3) The approach allows for continuous updates of model coefficients when changing multiple MVs at the same time. These features represent significant advances of the FIR model over the step-response modeling approach.

#### 8.1.4 Model Evaluation and Useful Tools

In our hands-on workshop WS8.1, Section 8.2, we will go through the details of applying several tools to evaluate how accurate our model prediction is and how robust our model response is to disturbances. Section 8.2.9 demonstrates uncertainty and correlation analysis of the model, and Section 8.2.11 illustrates a five-step procedure for collinearity analysis of the model. In this section, we introduce some basic concepts and tools relating to collinearity analysis.

##### 8.1.4.1 Relative Gain Array (RGA)

We introduce the concept of RGA [8–10] by considering the liquid level in a tank shown in Figure 8.23.

Here, we control the tank temperature  $ T $ and total tank liquid flow  $ m_t $ (GPM) by manipulating the inlet flow rates of cold water  $ m_c $ (GPM) and hot water  $ m_h $ (GPM). We assume that the liquid level setpoint corresponds to 50% tank-full level with  $ m_t = 11.6 $ GPM, and the temperature setpoint is  $ T = 24.4^\circ\text{C} $. The steady-state flow rates are  $ m_c = 9.61 $ GPM, and  $ m_h = 1.99 $ GPM.

We wish to find a proper pairing of two control variables  $ (T $ and  $ m_{t}) $ with two MVs  $ (m_{c} $ and  $ m_{h}) $. In other words, we are interested in the proper pairing of a simple process with two control variables  $ (T $ and  $ m_{t}) $ and two MVs  $ (m_{c} $ and  $ m_{h}) $. See Figure 8.24 for a simple representation of the current example.

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_920_797_1218.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 8.23 Mixing of a hot water stream with a cold water stream in a tank.</div>


---

<!-- PDF page 491 -->

<div style="text-align: center;">Figure 8.24 A simplified diagram of a  $ 2 \times 2 $ water-mixing process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_435_144_800_283.jpg" alt="Image" width="37%" /></div>


The corresponding balance equations are:

 $$ T=f_{1}(m_{\mathrm{c}},m_{\mathrm{h}})=\frac{m_{\mathrm{c}}T_{\mathrm{c}}+m_{\mathrm{h}}T_{\mathrm{h}}}{m_{\mathrm{c}}+m_{\mathrm{h}}} $$ 

 $$ m_{\mathrm{t}}=f_{2}(m_{\mathrm{c}},m_{\mathrm{h}})=m_{\mathrm{c}}+m_{\mathrm{h}} $$ 

Around steady state, we write ∆T and ∆m, in terms of open-loop gains Kij:

 $$ \Delta T=\left(\frac{\partial\mathrm{T}}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}\Delta m_{\mathrm{c}}+\left(\frac{\partial\mathrm{T}}{\partial m_{\mathrm{h}}}\right)_{m_{\mathrm{c}}}\Delta m_{\mathrm{h}}=K_{11}\Delta m_{\mathrm{c}}+K_{12}\Delta m_{\mathrm{h}} $$ 

 $$ \Delta m_{\mathrm{t}}=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}\Delta m_{\mathrm{c}}+=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{h}}}\right)_{m_{\mathrm{c}}}\Delta m_{\mathrm{h}}=K_{21}\Delta m_{\mathrm{c}}+K_{22}\Delta m_{\mathrm{h}} $$ 

By substituting Eqs. (8.23) and (8.24) into Eqs. (8.25) and (8.26), we find:

 $$ K_{11}=[m_{\mathrm{h}}(T_{\mathrm{c}}-T_{\mathrm{h}})]/m_{\mathrm{t}}^{2}\quad K_{12}==[m_{\mathrm{c}}(T_{\mathrm{h}}-T_{\mathrm{c}})]/m_{\mathrm{t}}^{2}\quad K_{21}=K_{22}=1 $$ 

In addition to open-loop gains, we introduce closed-loop gains  $ K_{ii}' $ defined as:

 $$ \begin{aligned}&K_{11}^{\prime}=\left(\frac{\partial\mathrm{T}}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}\quad&K_{12}^{\prime}=\left(\frac{\partial\mathrm{T}}{\partial m_{\mathrm{h}}}\right)_{m_{\mathrm{c}}}\\&K_{21}^{\prime}=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}\quad&K_{22}^{\prime}=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{h}}}\right)_{m_{\mathrm{c}}}\\ \end{aligned} $$ 

Basically,  $ K'_{11} $ represents a measure of how MV  $ m_c $ affects CV T if CV  $ m_t $ is held constant ( $ \Delta m_t = 0 $) and under closed-loop control. Specifically, when  $ \Delta m_t = 0 $, Eq. (8.26) gives

 $$ 0=K_{21}m_{\mathrm{c}}+K_{22}m_{\mathrm{h}}\rightarrow\Delta m_{\mathrm{h}}=-\frac{K_{21}}{K_{22}}\Delta m_{\mathrm{c}} $$ 

Substituting Eq. (8.29) into Eq. (8.25) gives

 $$ \Delta T=\left(K_{11}-\frac{K_{11}K_{22}-K_{12}K_{21}}{K_{22}}\right)\Delta m_{c} $$ 

When control variable  $ m_t $ is held constant ( $ \Delta m_t = 0 $), Eq. (8.30) gives the relationship for the closed-loop gain  $ K'_{11} $:

 $$ K_{11}^{\prime}=\left(\frac{\partial T}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}=K_{11}-\frac{K_{11}K_{22}-K_{12}K_{21}}{K_{22}} $$ 

---

<!-- PDF page 492 -->

Likewise, we can develop the following expressions ([10], pp. 554–556):

 $$ K_{12}^{\prime}=\left(\frac{\partial T}{\partial m_{\mathrm{h}}}\right)_{m_{*}}=\frac{K_{12}K_{21}-K_{11}K_{22}}{K_{21}} $$ 

 $$ K_{21}^{\prime}=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{c}}}\right)_{m_{\mathrm{h}}}=\frac{K_{12}K_{21}-K_{11}K_{22}}{K_{12}} $$ 

 $$ K_{22}^{\prime}=\left(\frac{\partial m_{\mathrm{t}}}{\partial m_{\mathrm{h}}}\right)_{m_{\mathrm{c}}}=\frac{K_{11}K_{22}-K_{12}K_{21}}{K_{12}} $$ 

The ratio of  $ K_{ij} $ to  $ K'_{ij} $ is called a relative gain, denoted by  $ \lambda_{ij} $:

 $$ \lambda_{ij}=\frac{K_{ij}}{K^{\prime}_{ij}} $$ 

Based on Eqs. (8.27), and the defining relationships for Eqs. (8.27) and (8.31) to (8.34), we can write a RGA as follows (with  $ m_{\mathrm{h}}=1.99 $ GPM,  $ m_{\mathrm{c}}=9.61 $ GPM, and  $ m_{\mathrm{t}}=11.6 $ GPM):

 $$ \lambda=\begin{bmatrix}\lambda_{11}&\lambda_{12}\\ \lambda_{21}&\lambda_{22}\end{bmatrix}=\begin{bmatrix}m_{\mathrm{h}}/m_{\mathrm{t}}&m_{\mathrm{c}}/m_{\mathrm{t}}\\ m_{\mathrm{c}}/m_{\mathrm{t}}&m_{\mathrm{h}}/m_{\mathrm{t}}\end{bmatrix}=\begin{bmatrix}m_{\mathrm{c}}&m_{\mathrm{h}}\\ T&0.172\\ m_{\mathrm{t}}&0.828\end{bmatrix} $$ 

RGA has several useful properties [8–10] that help in choosing a specific MV that has the most impact on a given CV.

1. Property 1: The rows and columns of the RGA sum to 1.0.

2. Property 2: Always pair the MV and CV on positive RGA elements that are closest to 1.0.

3. Property 3: Pairing on negative RGA elements results in either an unstable system or in an inverse responding system (a system that initially responds in the opposite direction to its final steady-state response when its input is changed).

In Eq. (8.36), the relative gain element pairing  $ T $ and  $ m_h $, and pairing  $ m_t $ and  $ m_c $, 0.828, is close to 1.0. Property 2 suggests that  $ T $ (tank liquid temperature) should be controlled by manipulating  $ m_h $ (hot water flow rate), and  $ m_t $ (total tank liquid flow rate, initially at 11.6 GPM, and hence the liquid tank level) should be controlled by manipulating  $ m_c $ (cold water flow rate, 9.61 GPM). This pairing is consistent with physical intuitions, as a higher temperature difference of the hot water means that hot water flow can change the tank liquid temperature faster than cold water flow, and the larger cold water flow can change the tank liquid level quicker than the smaller hot water flow.

Next, we wish to extend the concept of RGA for application to the steady-state gain matrix, such as Eqs. (8.3) and (8.4). In practice, the steady-state gain matrix is typically not a square matrix with an equal number of independent (manipulated and feedforward/disturbance) variables and dependent (controlled) variables. To handle this situation, DMC3 calculates the RGAs for all  $ 2 \times 2 $ submatrices in the model and highlights any issues.

Bristol [8], McAvoy ([9], pp. 31–33), and Smith and Corripio ([10], pp. 561–562) explain how to develop the RGA from an  $ n \times n $ steady-state gain matrix, denoted

---

<!-- PDF page 493 -->

by K, based on matrix operations. Specifically, we find the RGA by obtaining the transpose of the inverse of the steady-state gain matrix [that is,  $ (\mathbf{K}^{-1})^{T} $], and multiplying each term of the resulting matrix by the corresponding term in the original matrix, K. The terms thus obtained are the relative gains. Let us illustrate this calculation procedure with an example from McAvoy ([9], pp. 31–33). We consider the following steady-state gain matrix relationship:

 $$ \mathbf{C}\mathbf{V}=\mathbf{K}^{*}\mathbf{M}\mathbf{V} $$ 

 $$ \begin{bmatrix}\mathrm{CV}_{1}\\ \mathrm{CV}_{2}\\ \mathrm{CV}_{3}\end{bmatrix}=\begin{bmatrix}2.662&8.351&8.351\\ 0.3816&-0.5586&-0.5586\\ 0&11.896&-0.3511\end{bmatrix}*\begin{bmatrix}\mathrm{MV}_{1}\\ \mathrm{MV}_{2}\\ \mathrm{MV}_{3}\end{bmatrix} $$ 

There are many online matrix calculators (e.g. https://matrixcalc.org/en/) to calculate the inverse and transpose. We find:

 $$ \begin{aligned}&\mathbf{K}^{-1}=\begin{bmatrix}{{{0.1195}}}&{{{1.787}}}&{{{0}}} \\{{{2.341\times10^{-3}}}}&{{{-0.01633}}}&{{{0.08165}}} \\{{{0.07931}}}&{{{-0.5532}}}&{{{-0.08165}}}\end{bmatrix}\\ \end{aligned} $$ 

 $$ \left(\mathbf{K}^{-1}\right)^{T}=\begin{bmatrix}0.1195&2.341\times10^{-3}&0.07931\\ 1.787&-0.01633&-0.5532\\ 0&0.08165&-0.08165\end{bmatrix} $$ 

Multiplying each term of the resulting matrix  $ (K^{-1})^{T} $, Eq. (8.40), by the corresponding term in the original matrix, K, Eq. (8.38), is a matrix operation called Hadamard product, for which online calculators are available (e.g. https://keisan.casio.com/exec/system/15157205321124). We find the resulting RGA as:

 $$ \boldsymbol{\lambda}=[(\mathbf{K}^{-1})^{T}*\mathbf{K}]_{Hadamard}=\begin{bmatrix}0.318&0.0195&0.663\\ 0.682&0.00913&0.309\\ 0&0.971&0.0287\end{bmatrix} $$ 

We note that the Hadamard product matrix elements result from multiplying each term of Eq. (8.40) by the corresponding term in the original K matrix in Eq. (8.38); for example,

 $$ \lambda_{11}=2.662\times0.1195=0.318\quad\lambda_{12}=8.351\times2.341\times10^{-3}=0.0195 $$ 

##### 8.1.4.2 Ill-Conditioned Model Matrices and Collinear System

As a part of model evaluation, DMC3 applies a collinearity analysis tool to identify and repair ill-conditioned model matrices  $ [11] $. This section introduces the concepts of conditioned number and collinear system and relates them to the RGA.

For an  $ n \times n $ steady-state gain matrix K, we may decompose it into a product of three matrices:

 $$ \mathbf{K}=\mathbf{U}*\mathbf{\lambda}*\mathbf{V}^{\mathrm{T}} $$ 

where  $ \mathbf{U} $ is  $ n \times k $,  $ \lambda $ is  $ k \times k $, and  $ \mathbf{V} $ is  $ n \times k $. Matrix  $ \lambda $ is diagonal, with elements  $ \lambda_1 $,  $ \lambda_1 $, ...,  $ \lambda_k $ being the positive square roots of  $ \lambda_1^2 $,  $ \lambda_2^2 $,  $ \lambda_3^2 $ ..., which are nonzero eigenvalues of  $ \mathbf{K}^\mathrm{T} \times \mathbf{K} $ or of  $ \mathbf{K} \times \mathbf{K}^\mathrm{T} $. The values  $ \lambda_1 $,  $ \lambda_1 $, ...,  $ \lambda_k $ are called the singular values of

---

<!-- PDF page 494 -->

matrix K. This matrix decomposition process is called singular value decomposition (SVD). Section A.2.5.3 of Appendix A, “Matrix Algebra in Multivariate Data Analytics and Model-Predictive Control,” gives the details of SVD, including the meaning of matrices U and V.

Let us use the SVD of three simple matrices to illustrate the concept of condition number and an ill-conditioned system. We use an online SVD calculator to obtain the numerical results (e.g. https://keisan.casio.com/exec/system/15076953160460).

 $$ \begin{aligned}(1)\mathbf{K}&=\begin{bmatrix}{{{1}}}&{{{0}}} \\{{{0}}}&{{{1}}}\end{bmatrix}=\mathbf{U}*\lambda*\mathbf{V}^{T}&=\begin{bmatrix}{{{-1}}}&{{{0}}} \\{{{0}}}&{{{-1}}}\end{bmatrix}*\begin{bmatrix}{{{1}}}&{{{0}}} \\{{{0}}}&{{{1}}}\end{bmatrix}*\begin{bmatrix}{{{-1}}}&{{{0}}} \\{{{0}}}&{{{-1}}}\end{bmatrix}\end{aligned} $$ 

The  $ \lambda $ matrix is diagonal, and its diagonal elements  $ (\lambda_1, \lambda_2, ..., \lambda_k) $ are singular numbers. The condition number is the ratio of the largest diagonal element to the smallest diagonal element. For case (1), the condition number is  $ (1/1) $ or 1.0.

 $$ \begin{aligned}\text{Ⅲ }\mathbf{K}&=\begin{bmatrix}{{{1}}}&{{{0.96}}} \\{{{0.96}}}&{{{1}}}\end{bmatrix}=\mathbf{U}*\lambda*\mathbf{V}^{T}\\&=\begin{bmatrix}{{{-0.7071}}}&{{{-0.7071}}} \\{{{0.7071}}}&{{{-0.7071}}}\end{bmatrix}*\begin{bmatrix}{{{0.041}}}&{{{0}}} \\{{{0}}}&{{{1.96}}}\end{bmatrix}*\begin{bmatrix}{{{-0.7071}}}&{{{0.7071}}} \\{{{-0.7071}}}&{{{-0.7071}}}\end{bmatrix}\end{aligned} $$ 

For case (2), the condition number is  $ (1.96/0.04) $ or 49.

 $$ \begin{aligned}\text{Ⅲ }\mathbf{K}&=\begin{bmatrix}{{{1}}}&{{{0.96}}} \\{{{0.96}}}&{{{1}}}\end{bmatrix}=\mathbf{U}*\lambda*\mathbf{V}^{T}\\&=\begin{bmatrix}{{{0.7071}}}&{{{-0.7071}}} \\{{{-0.7071}}}&{{{-0.7071}}}\end{bmatrix}*\begin{bmatrix}{{{0}}}&{{{0}}} \\{{{0}}}&{{{2}}}\end{bmatrix}*\begin{bmatrix}{{{0.7071}}}&{{{-0.7071}}} \\{{{-0.7071}}}&{{{-0.7071}}}\end{bmatrix}\end{aligned} $$ 

For case (3), the condition number is  $ (2/0) $ or  $ \infty $.

McAvoy ([9], p. 181) suggests that a gain matrix with a condition number close to, greater than, or equal to 50 indicates the system to be nearly singular or ill-conditioned. This includes cases (2) and (3) above.

In a patent assigned to AspenTech, Zhang et al. [11] define a process model with an  $ n \times m $ steady-state gain matrix to be collinear by looking at the maximum and minimum singular values resulting from SVD of the gain matrix. In particular, we consider a square  $ (n = m) $ submatrix of the gain matrix and define two terms: (1) Not collinear: If the submatrix has a rank of m (see Section A.2.1, Appendix A for rank), then the given system has a full rank and the gain matrix is “not collinear”; (2) Collinear or perfectly collinear: If the submatrix has a rank smaller than m and the singular value  $ \lambda_m = 0 $, then the system is “collinear or perfectly collinear.”

The collinearity analysis tool within DMC3 identifies and repairs ill-conditioned model matrices [11]. When dealing with collinearity, we can focus on square sub-matrices because, if an  $ n \times m $ matrix is collinear (when  $ n > m $), then all its  $ m \times m $ submatrices must be collinear [11]. In particular, the tool calculates the RGA for all  $ 2 \times 2 $ submatrices in the model and highlights possible issues.

DMC3 suggests the following RGA thresholds for each MV-CV pair:

1. RGA = 1: Ideal performance; complete correlation

2. RGA <5: Good correlation between the MV-CV pair

3. RGA <8: Reasonable and acceptable correlation between the MV-CV pair

---

<!-- PDF page 495 -->

4. RGA >8: Possible inconsistent gain; collinearity issue

5. RGA >20: Nearly collinear system; review and repair

Section 8.2.11 gives a hands-on workshop for the model evaluation by collinearity analysis.

#### 8.1.5 Open-Loop Prediction, Prediction Error Filtering, and Prediction Update for Steady-State Variables

In Section 8.1.2.1, we presented an example of the open-loop prediction for a fired heater model and introduced the concept of continuing reconciliation of model-based predictions to the process measurements and feedback correction to update the model predictions to the future that is one of the three sources of benefits of APC. In Section 8.2.12, we demonstrate this open-loop prediction in our hands-on workshop. Here, we look at three types of prediction errors that are calculated on each DMC3 controller execution, which we have applied in real industrial projects.

##### 8.1.5.1 Prediction Error (PREDER)

The prediction error, also called model bias, is the difference between the model prediction and the actual measured CV value at each controller execution:

 $$  Prediction error(Model bias)=CV_{pred}-CV_{actual} $$ 

We use the value of this error to shift the future CV prediction vector up or down to match the current CV value, as illustrated previously in Figures 8.10 and 8.11 for the online feedback correction of CV prediction based on measured value.

##### 8.1.5.2 Accumulated Prediction Error (ACPRER)

Referring to Figure 8.25, we define the accumulated prediction error as the integral of the time-dependent error  $ E(t) $ from the last prediction initialization to the current time:

 $$  Accumulated prediction error=\int_{0}^{t}E(t)\mathrm{d}t $$ 

This integrated prediction error represents the ultimate bias that must be added to the model-predicted value of a dependent variable to match its process response. In general, we prefer to monitor the accumulated prediction error, instead of the prediction error, to get a better idea of time-correlated errors.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_1085_689_1223.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 8.25 An illustration of accumulated prediction error.</div>


---

<!-- PDF page 496 -->

##### 8.1.5.3 Average Prediction Error (AVPRER) and Prediction Error Filtering

The concept of average prediction error is related to the noise or model-plant mismatch that affects the controller negatively. Values of average prediction error on the same order of magnitude as the noise band of the CV measurement suggest that prediction errors are caused primarily by measurement noise, which could lead to excessive MV movement and possibly valve wear. Values of average prediction error outside the noise band indicate a potential model-plant mismatch, and significant model-plant mismatch could cause cycling or instability in CV response. Additionally, unmeasured disturbances could lead to unexpected MV moves. To mitigate these effects, we typically apply filtering or smoothing to the prediction error.

The average prediction error is a “filtered” value of the absolute value of the prediction error or model bias. The typical filter used is a first-order exponential filter with a filter factor equal to 0.8–0.99 (DMC3 uses a filter factor of 0.965), which is set to 0.0 upon filter initialization. The reader may refer to [12] for an introduction to exponential filter. We note that an exponential filter is also called an “exponentially weighted moving average (EWMA) filter,” or just “exponential moving average (EMA) filter.”

Nonlinear controllers in DMC3 use an extended Kalman filter algorithm [13] for prediction error or model bias filtering.

##### 8.1.5.4 Prediction Update for Control Variable Values

In Section 8.1.2.1, Figures 8.9–8.11, we illustrated the “preceding” process for prediction update to control variable values: (1) update the CV predictions from the previous controller execution cycle based on the changes in MVs; (2) compute the prediction errors for CVs; (3) shift the CV predictions by prediction errors to make the current CV predictions match the current CV measurements; and (4) do this online correction for each CV at the beginning of each controller execution cycle.

#### 8.1.6 Concepts and Parameters in Steady-State Economic Optimization and Dynamic Controller Simulation

In Section 8.1.2.2, we illustrated the steady-state (SS) economic optimization to determine the MV and CV targets to minimize cost and optimize profit for the copolymerization problem. In this section, we introduce additional concepts and parameters that are relevant to SS optimization and the subsequent dynamic controller simulation steps. These concepts and parameters are key to developing and fine-tuning both linear and nonlinear multivariable model-predictive controllers using Aspen DMCplus and Aspen DMC3. The same concepts and parameters are equally important to Aspen nonlinear controller for polyolefin applications.

##### 8.1.6.1 Variable Limits and Feasible Solution

Figure 8.26 illustrates the concept of variable limits. Take MV as an example. The upper and lower operating limits, or simply the upper and lower limits, define the

---

<!-- PDF page 497 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_150_709_312.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 8.26 An illustration of variable limits [7]. Used with permission from Aspen Technology, Inc.</div>


control range over which the MV may be moved by the controller. The upper and lower validity limits specify the prediction range over which the MV may be used for prediction. If the operating limits are set outside the validity limits, the MV is downgraded to FF status.

The upper and lower engineering limits define the commissioned range and are used to clamp the operating limits if the operating limits are set outside the engineering limits but within the validity limits. Engineering limits outside the validity limits are clamped at the validity limits without downgrading the MV to FF status.

The SS (steady state) optimizer performs a validity check using the current measurement, limits, and tuning parameters, and provides economic optimum MV and CV targets to the path optimizer for dynamic controller simulation. A feasible solution is defined as a solution where all CV steady-state targets are at or within their operating limits. We note that MV steady-state targets are always maintained within their operating limits.

How does the SS optimizer know which CV operating limits are the least important and which could be changed slightly, if necessary, to find a feasible solution? The SS optimizer uses two sets of parameters to allow the control engineer to specify the relative importance of CV operating limits: (1) CV limit ranking, and (2) steady-state equal concern error (SS ECE), which are discussed below.

##### 8.1.6.2 CV Limit Ranking Method to Handle Steady-State Feasibility

Aspen DMC3 Builder assigns a relative ranking to each CV operating limit to characterize the order of priority of that limit, and the steady-state economic optimization satisfies CV limits in a ranked order. The software checks for the limit for feasibility in order of increasing rank. Specifically, a CV limit with a smaller numerical ranking is more important than another CV limit with a larger numerical ranking, e.g. a CV limit with rank 1 is more important than another CV limit with rank 999; and the former CV limit must not be violated, while the latter CV limit could be relaxed if appropriate.

DMC3 Builder recognizes the following possible ranks: (1) rank 0: All CV's have the same rank, rank 0, and we consider trade-off with MV constraints (not recommended in practice); (2) rank 1–999 (see more below): all CV limits go through a standard feasibility check; (3) rank 1000: a special “soft target” constraint, which is solved in the economic optimization only (not in the feasibility calculation); and (4) rank 9999: the CV limit is not used in steady-state economic optimization.

---

<!-- PDF page 498 -->

The CV limit ranking results from consulting with experienced plant operators and engineers, who typically know the relative importance of each CV limit. When it is not possible to clearly define the relative ranking of a CV limit, we could consider assigning the CV limit to the following suggested rank between 1 and 999 [7]: (1) safety and environmental limits (e.g. stack  $ NO_{x} $ emissions; safety valve controller output; heater tube skin temperature, etc.): rank 1–99; (2) integrating or ramp variable (Section 8.1.1.3): rank 100–199; (3) model validity requirements (e.g. control valve outputs; column flooding limit, etc.): rank 200–299; (4) product quality specifications (fractionator boiling points; product impurity specifications, etc.): rank 300–399; and (5) economic optimization soft targets that cannot be uniquely defined: rank 1000.

Figure 8.27 illustrates the CV ranking method to handle steady-state feasibility for CV limits of different ranks. We satisfy the more important constraints (lower numerical ranks) first, while relaxing the less important constraints (larger numerical ranks) to find a feasible solution. In the figure, line B (CV2U, representing  $ CV_2 $ upper operating limit (UPL), of rank 100) and line C (CV1L, representing  $ CV_1 $ lower operating limit (LPL), of rank 200) are both satisfied and intersect at point F. We could find a feasible solution if we could relax the constraint of line A (CV3U, representing  $ CV_3 $ UPL, of rank 300) by moving line A to line A', which satisfies the feasible solution at point F. The distance between lines A and A' represents the relaxed amount required to make a constraint feasible, which we call a constraint give-up ( $ \varepsilon $).

Figure 8.28 shows another example about constraint give-up when the CV limit ranks are equal. In the figure, line B (CV2U, representing CV2 UPL) and line C (CV3U, representing CV3 UPL) are both satisfied and intersect at point F. We move the constraint of line A (CV1L, representing CV1 LPL) to line A', which satisfies the feasible solution at point F. The distance between lines A and A' represents the relaxed amount required to make the constraint CV1L feasible. This is the constraint give-up ( $ \varepsilon $) for CV1L.

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_923_654_1156.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 8.27 Achieving steady-state feasibility for CV limits of different ranks by satisfying constraints CV2U (CV₂, upper operating limit of rank 100; line B) and CV1L (CV₁ lower operating limit of rank 200, line C), while relaxing the constraint of CV3U (shifting CV₃ upper operating limit of rank 300 from line A to line A').</div>


---

<!-- PDF page 499 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_146_615_344.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 8.28 Achieving steady-state feasibility for CV limits of the same rank by satisfying constraints CV2U and CV3U, while relaxing the constraint CV1L (shifting CV1 lower operating limit from line A to line A').</div>


##### 8.1.6.3 Steady-State Equal Concern Error (SS ECE) to Handle Steady-State Feasibility

For the copolymerization problem, assuming the CV limits to be of an equal rank, what magnitude of error in each of the CVs should get an equal level of attention or concern from the control engineer? Let us consider Table 8.2, in which we quantify the CV error that is 10% of the difference between the upper and lower operating limits.

In terms of engineering units, we see that for each CV, an error above the UPL or below the LPL with a magnitude larger than the value displayed in the last column of Table 8.2 should require the control engineer an equal level of attention or concern to take appropriate corrective action.

DMC3 Builder includes a steady-state parameter, called SS ECE, to handle the infeasibility of potential violations of multiple CV limits of an equal rank. The SS ECE factors allow the control engineer to specify the “standard” or “reference” amount of error for a given CV. These are then used to balance movement (error) in one CV against movement (error) in another CV. A small SS ECE for a CV means that this CV has a smaller tolerance threshold to any deviation from its upper or lower operating limit, and the control engineer must give sufficient attention or concern to the resulting potential infeasibility. For example, if the SS ECE for CV1 is less than the SS ECE for CV2, and both have the same engineering unit, then

<div style="text-align: center;">Table 8.2 Magnitude of error in each of the CVs.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>CV</td><td style='text-align: center; word-wrap: break-word;'>Measurement (current value)</td><td style='text-align: center; word-wrap: break-word;'>Lower operating limit (LPL)</td><td style='text-align: center; word-wrap: break-word;'>Upper operating limit (UPL)</td><td style='text-align: center; word-wrap: break-word;'>(UPL-LPL) $ \times $10% deviation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polymer, kg/hr</td><td style='text-align: center; word-wrap: break-word;'>23.3</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>3 kg/hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mol_Wt.</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>34500</td><td style='text-align: center; word-wrap: break-word;'>35500</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_Rx,  $ {}^{\circ} $C</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>70</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>3.0  $ {}^{\circ} $C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Conc_MMA, mole fraction</td><td style='text-align: center; word-wrap: break-word;'>0.56</td><td style='text-align: center; word-wrap: break-word;'>0.55</td><td style='text-align: center; word-wrap: break-word;'>0.60</td><td style='text-align: center; word-wrap: break-word;'>0.005 mole fraction</td></tr></table>

---

<!-- PDF page 500 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_146_651_503.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 8.29 Achieving steady-state feasibility for CV limits of the same rank by satisfying constraints CV1L with a smaller SS ECE of 0.01, while relaxing the constraint CV2U of a larger SS ECE of 1 and shifting CV2 upper operating limit from line B to line B'.</div>


satisfying the CV1 limit constraint is more important than satisfying the CV2 limit constraint.

Figure 8.29 gives an example of using SS ECE to resolve a set of infeasible CV limits. In the figure, line A (CV2L, representing CV1 LPL) has a smaller steady-state ECE of SS Low Concern of 0.01 and must be satisfied. Line B (CV2U, representing CV2 upper operating limit) has a larger steady-state ECE of SS High Concern of 1, and could be relaxed. We move the less important constraint of line B to line B', which satisfies the feasible solution at point F. The distance between lines B and B' represents the relaxed amount required to make the constraint CV2U feasible. This is the constraint give-up ( $ \varepsilon $) for CV2L.

To resolve a set of infeasible CV limits of an equal rank, DMC3 Builder provides two algorithms: (1) LP (linear programming) solution; and (2) QP (quadratic programming) solution. We consider only the LP solution here. Specifically, assume that  $ \varepsilon_{1}, \varepsilon_{2}, \varepsilon_{3}, \ldots $ are the amounts of constraint give-up, illustrated in Figures 8.27 and 8.28, to make a CV limit feasible. We restrict the give-ups,  $ \varepsilon_{i} $, to be positive or zero (zero means that a feasible solution exists). For each constraint give-up, we assign a weight or weighting factor  $ W_{i} $, indicating the relative importance of satisfying i-th CV limit. The LP solution includes the following linear minimization objective function plus the linear CV limit constraint:

 $$ \operatorname{Min}\varphi=\varepsilon_{1}*W_{1}+\varepsilon_{2}*W_{2}+\ldots\ldots\ldots $$ 

subject to the following CV limit constraints in a vector form

 $$ \mathbf{C}\mathbf{V}\leq\mathbf{C}\mathbf{V}_{\max}+\varepsilon_{1} $$ 

 $$ \mathbf{C}\mathbf{V}\geq\mathbf{C}\mathbf{V}_{\min}-\varepsilon_{2} $$ 

---

<!-- PDF page 501 -->

The weight or weighting factor,  $ W_i $, is a positive number, typically from 1 to  $ 10^6 $; the higher its value, the more important it is to satisfy the upper or lower limit constraint for  $ CV_i $.

In applying the LP algorithm to resolve the infeasible CV limits, DMC3 Builder specifically relates the weighting factor  $ W_i $ (varying from 1 to  $ 10^6 $) to the corresponding SS ECE $ _i $ (varying from 1 to  $ 10^{-6} $) by the relationship:

 $$  SS ECE_{i}=1/W_{i} $$ 

Suppose that it is very important to satisfy the  $ i $-th CV limit by setting the weighting factor  $ W_i $ to  $ 10^6 $, Eq. (8.47) suggests that the corresponding SS ECE for the  $ i $-th CV limit, SS ECE $ _i $, is  $ 10^{-6} $. We note that in doing a SS Optimizer calculation (simulation), we need only the relative values of ECEs (low concern and high concern) for all CVs, not their specific numerical values in engineering units. As such, we could specify the ECEs for CV limits as 1, 0.1, 0.01, 0.001, ..., with smaller ECE values (higher weighting factors) indicating that it is more important to satisfy the corresponding upper or lower CV limit.

For steady-state economic optimization (SS Optimizer), we need to specify both the limit ranks and the ECEs. These include: (1) the SS Low Concern, SS Low Rank, SS High Concern, and SS High Rank for each CV; and (2) Validity, Engineering, and Operator Limits (Low and High) for each MV and each CV.

##### 8.1.6.4 Dynamic Equal Concern Errors for CV Limits in Dynamic Controller Simulation

Having completed the steady-state economic optimization via the SS Optimizer and identified the economic optimum MV and CV targets, DMC3 Builder continues with dynamic controller simulation to determine a series of MV moves to drive the MV and CV to their target values through the Path Optimizer. In this step, a key tuning parameter in dynamic controller simulation is the dynamic equal concern error or dynamic ECE. Basically, dynamic ECEs indicate the level of concern by the control engineer for dynamic deviations from the steady-state CV targets. As with steady-state ECEs, it is the relative values of the dynamic ECEs that determine how tightly a CV is controlled to its steady-state target and not the value of the dynamic ECE itself. We can minimize the deviation of a CV from its steady-state target by reducing the dynamic ECE. This is done at the expense of more errors on the other CVs and more movements for the MVs.

Figure 8.30 illustrates the concept of dynamic ECEs in three different regions: below the LPL, above the UPL, and between the LPL and UPL.

First, DMC3 Builder specifies a dynamic ECE called “Dynamic low concern” for CV values below the “Operator low limit,” and a dynamic ECE called “Dynamic high concern” for CV values above the “Operator high limit.” Next, we see in the figure, a narrow transition zone to the right of Operator low limit, called lower transition zone or “Dynamic low zone,” in which the weight (dashed line) drops and the Dynamic low concern (solid line) increases; we also see a narrow transition zone to the left of the Operator high limit, called upper transition zone or “Dynamic high zone,” in which the weight (dashed line) increases and the Dynamic high concern (solid line)

---

<!-- PDF page 502 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Category</th><th style='text-align: center;'>Item</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Operator</td><td style='text-align: center;'>low limit</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>1</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>2</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>4</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>5</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>6</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>7</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>8</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>9</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic low concern</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>1</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>2</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>4</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>5</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>6</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>7</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>8</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>9</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high concern</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>1</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>2</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>3</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>4</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>5</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>6</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>7</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>8</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>9</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>10</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>11</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>12</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>13</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>14</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>15</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>16</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>17</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>18</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>19</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>20</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>21</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>22</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>23</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>24</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>25</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>26</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>27</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>28</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>29</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>30</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>31</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>32</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>33</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>34</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>35</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>36</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>37</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>38</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>39</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>40</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>41</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>42</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>43</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>44</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>45</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>46</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>47</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>48</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>49</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>50</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>51</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>52</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>53</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>54</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>55</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>56</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>57</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>58</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>59</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>60</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>61</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>62</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>63</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>64</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>65</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>66</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>67</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>68</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>69</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>70</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>71</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>72</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>73</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>74</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>75</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>76</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>77</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>78</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>79</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>80</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>81</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>82</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>83</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>84</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>85</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>86</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>87</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>88</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>89</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>90</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>91</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>92</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>93</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>94</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>95</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>96</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>97</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>98</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>99</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>101</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>102</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>103</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>104</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>105</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>106</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>107</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>108</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>109</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>110</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>111</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>112</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>113</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>114</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>115</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>116</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>117</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>118</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>119</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>120</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>121</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>122</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>123</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>124</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>125</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>126</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>127</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>128</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>129</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>130</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>131</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>132</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>133</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>134</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>135</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>136</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>137</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>138</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>139</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>140</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>141</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>142</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>143</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>144</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>145</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>146</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>147</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>148</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>149</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>150</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>151</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>152</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>153</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>154</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>155</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>156</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>157</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>158</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>159</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>160</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>161</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>162</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>163</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>164</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>165</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>166</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>167</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>168</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>169</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>170</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>171</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>172</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>173</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>174</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>175</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>176</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>177</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>178</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>179</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>180</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>181</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>182</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>183</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>184</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>185</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>186</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>187</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>188</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>189</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>190</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>191</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>192</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>193</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>194</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>195</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>196</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>197</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>198</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>199</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>201</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>202</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>203</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>204</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>205</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>206</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>207</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>208</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>209</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>210</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>211</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>212</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>213</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>214</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>215</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>216</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>217</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>218</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>219</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>220</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>221</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>222</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>223</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>224</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>225</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>226</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>227</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>228</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>229</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>230</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>231</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>232</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>233</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>234</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>235</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>236</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>237</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>238</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>239</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>240</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>241</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>242</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>243</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>244</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>245</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>246</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>247</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>248</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>249</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>250</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>251</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>252</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>253</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>254</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>255</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>256</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>257</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>258</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>259</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>260</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>261</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>262</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>263</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>264</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>265</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>266</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>267</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>268</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>269</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>270</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>271</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>272</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>273</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>274</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>275</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>276</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>277</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>278</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>279</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>280</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>281</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic high limit</td><td style='text-align: center;'>282</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Dynamic</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.30 Dynamic equal concern errors for CV limits [7]. Used with permission from Aspen Technology, Inc.</div>


drops. The transition zones help to avoid “chatter” when ECEs are different in the three different regions noted above and displayed in the figure. Thirdly, we see in the figure a middle region between the right boundary line of the lower transition zone or “Dynamic low zone,” and the left boundary line of the upper transition zone or “Dynamic high zone.” While we see a label “Dynamic middle concern” in this middle region, this ECE has no real significance and is being ignored in the DMC3 dynamic controller simulation. This follows because, within this middle region, the CV value is always between its LPL and UPL, and the control engineer sees no chance for the CV to deviate from its limits.

In the DMC3 control structure of Figure 8.18, we see that the path optimizer may determine a series of CV moves to drive the MVs and CVs to their economic optimum, steady-state targets obtained by the SS optimizer. Additionally, the figure shows that the path optimizer may also determine a series of MV moves to drive a specific CV to an external target value specified by the control engineer (instead of the target value determined by the SS optimizer, that is, the economic optimum, steady-state target). DMC3 treats an external target for a CV the same as a CV constraint and includes it in the feasibility checks by the SS optimizer. Additionally, when doing a dynamic controller simulation through the path optimizer, DMC3 Builder includes a dynamic ECE for the external target, called Dynamic Target Concern. This is the concern associated with the dynamic move plan target for a CV. It defines how far the output can drift dynamically from its steady-state target before you get concerned. An increase in this value will allow the output more freedom to deviate dynamically from the steady-state target. A decrease will drive the output closer to the steady-state target dynamically.

To summarize, for dynamic controller simulation, we need to specify both the limit ranks and the ECEs. These include: (1) SS Low Concern, Dynamic Low Concern, SS High Concern, Dynamic High Concern, and SS Low Rank, SS High Rank, Dynamic

---

<!-- PDF page 503 -->

Low Zone, and Dynamic High Zone for each CV; (2) Validity, Engineering, and Operator Limits (Low and High) for each MV and each CV; and (3) Dynamic Target Concern, if there is an external target for a specific CV.

##### 8.1.6.5 Move Suppression for MV

A key parameter for dynamic controller simulation via path optimizer is the move suppression for MVs. Move suppression parameter affects how aggressively the controller will move the MVs to achieve control objectives. A larger value means more suppression, i.e. less MV movement.

Figure 8.31 illustrates the trade-off between: (1) minimizing CV error from its steady-state economic optimum target by an aggressive MV movement by specifying a small move suppression; and (2) minimizing MV move size by specifying a large move suppression, resulting in increasing CV error from its SS optimization target. Figure 8.32 compares the impacts of small and large move suppression parameters on the MV move size in response to CV setpoint change from 310 to 350°C.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Sum of absolute CV move sizes</th><th style='text-align: center;'>Sum of absolute CV errors</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>25</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.31 The trade-off between minimizing CV error from its steady-state economic optimum target by an aggressive MV movement by specifying a small move suppression, and minimizing MV move size by specifying a large move suppression.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Move suppression limit</th><th style='text-align: center;'>CV: T-RX (°C)</th><th style='text-align: center;'>MV: Init (°C)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>310</td><td style='text-align: center;'>15</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.32 Comparing the impacts of small and large move suppression parameters on the MV move size in response to CV setpoint change from 310 to 350°C.</div>


---

<!-- PDF page 504 -->

There are several sources of qualitative information that can help a control engineer determine the appropriate value of move suppression to use in a dynamic controller simulation: (1) experience during step testing to develop the controller model; (2) comfort level of the control engineer for how fast an MV can be moved; (3) the capability of the exiting PID loop to track CV setpoint changes; (4) the type of disturbances for which the MV must compensate; and (5) settings for similar controllers, which have demonstrated success.

Additionally, we may apply a multi-level strategy to initialize the move suppression parameters. We start by applying a move suppression value of  $ x $ (say, 0.1) for a flow setpoint MV. We then specify a move suppression value of  $ 2x $ (say, 0.2) for a temperature setpoint MV, and of  $ 4x $ (say, 0.4) for a pressure setpoint MV and a feed rate setpoint MV. The larger values of move suppression for the pressure setpoint MV and feed rate setpoint MV imply that we do not want both the pressure and feed rate setpoints to move quickly.

Finally, we note that move suppression is the most straightforward way to handle on dynamic controller performance. ECE tuning has a relatively narrow range where it affects dynamic controller performance, and it sometimes could give unpredictable results for disturbances affecting more than one CV at a time.

In the next section, we present a hands-on workshop to illustrate all the concepts and parameters introduced so far. We also use the workshop to demonstrate the practical tips for applying DMC3 Builder to the MPC of a copolymerization process.

#### 8.2 Workshop 8.1: Development and Application of a Predictive Controller Model for a Copolymerization Process

#### 8.2.1 Objective

The objective of this workshop is to teach the reader how to use the DMC3 Builder for a multivariable DMC project, specifically the development and applications of a predictive controller model for a solution copolymerization reactor based on data from plant step tests. We focus on the identification of a dynamic process model using the modeling tools within DMC3 Builder and the use of the resulting predictive controller model to optimize the polymer production rate.

#### 8.2.2 A Copolymerization Reactor

Figure 8.33 shows a simplified flowsheet of a solution copolymerization reactor system.

There are two monomers, MMA and VA, an initiator (INITIATO), and a chain-transfer agent (TRANSF). Figure 8.33 shows five manipulated (independent) variables and four controlled (dependent) variables.

---

<!-- PDF page 505 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_148_775_394.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.33 A simplified flowsheet of a solution copolymerization reactor system.</div>


#### 8.2.3 Starting the DMC3 Builder Program: Creating a New Project

Start Aspen DMC3 Builder and choose “New.” Figure 8.34 illustrates the resulting screen to choose one of the two project types: (1) DMC project, which includes DMC3 controller, Aspen Watch for controller performance monitoring, and a complete set of adaptive control tools; and (2) APC project, which includes DMCplus controller and nonlinear controller, Aspen Watch, and some adaptive control tools if licensed.

For controlling the production rate, product concentration, and qualities (such as polymer density and melt index) of polyolefins, we recommend choosing APC project and using the nonlinear controller, as both polymer density and melt index have nonlinear dependencies on key MVs.

For controlling the polymer production rate, molecular weight, and concentration of monomer in the polymer, we can use a linear multivariable MPC, such as DMCplus controller under APC project or its newer version, DMC3 controller under DMC3 project. For now, we choose DMC3 Project and complete the project name

<div style="text-align: center;"><img src="imgs/img_in_image_box_129_872_779_1219.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.34 Selection of project type and related software tools.</div>


---

<!-- PDF page 506 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_147_575_263.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">Figure 8.35 Specifying project name and working folder location.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_302_811_617.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.36 DMC3 interface layout: tool ribbons (top), navigation workflow buttons (bottom left) - datasets, controllers, composite and online; navigation tree area (left "white" column), and workspace (middle).</div>


and the working folder location, as in Figure 8.35. After clicking OK, we see the interface layout of Figure 8.36.

#### 8.2.4 DMC3 Builder Task One: Data Processing for Developing a Master Model – Import Process Data, Merge the Datasets, and Mark and Delete Bad Data Slices

DMC3 Builder can perform six key tasks: (1) Master Model: data processing and model identification (ID); (2) Configuration: configuring the steady-state optimizer and dynamic controller; (3) Optimization: performing the steady-state optimization; (4) Simulation: including five types of simulation, namely, controller, optimizer, filter, model, and preview dynamics; (5) Calculations: performing online calculations and transformations; and (6) Deployment: performing controller deployment. We begin with task one, data processing to develop the master model, below.

From the “Import” tool ribbon on the top left, we choose “Dataset.” We then select the collect file WS8.1-1.clc within our working folder and click on the Open button. See Figures 8.37 and 8.38.

We see in Figure 8.38 that the first collect file has 9 tags, a sample period of 60 sec, an interpolation span of 5 min, and a total of 2640 samples collected from 10/1/1996 07:14:00 to 10/3/1996 03:13:00. We click "Import" to upload the data into the project. In general, an interpolation span of 5–10 min would be sufficient for most problems.

---

<!-- PDF page 507 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_148_780_334.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.37 Important dataset, collect file WS8.1-1.clc.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_405_779_799.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.38 Contents of the first collect file.</div>


Before the software imports the data into the project, an “Interpolate Dataset” window shows up. We click on “Start” button to interpolate any bad and missing data slices longer than 5 min in duration. We then click on “Close” button to conclude the interpolation analysis. The analysis results in the message “0 of 9 vectors (variables) have been interpolated.” We do not show the screen images of this straightforward step.

Figure 8.39 displays the first dataset in the Datasets view and trend plots. The software will automatically show the first three in the view (which happen to be all MVs, Flow_MMA, Flow_VA, and Init), but we choose to add the remaining two MVs (Transf and T_JKT) to display. Of particular significance in the displayed plot are the stepwise changes in all five MVs within the total duration of step tests.

We repeat the same process to import the second collect file, WS8.1-2.clc. Figure 8.40 illustrates the key features of the second collect file. Its list of vectors to import is identical to that in Figure 8.38. A display of the five MVs is similar to Figure 8.39. Figure 8.41 displays the continuous changes in all four controlled (dependent) variables within the duration of step tests.

---

<!-- PDF page 508 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Ligand</th><th style='text-align: center;'></th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.39 A display of the first dataset for stepwise changes in five manipulated variables during step tests.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_682_808_863.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.40 Contents of second collect file.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Date</th><th style='text-align: center;'>Pdfom (High)</th><th style='text-align: center;'>Pdfom (Low)</th><th style='text-align: center;'>Pdfom (High)</th><th style='text-align: center;'>Pdfom (Low)</th><th style='text-align: center;'>Pdfom (High)</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.41 A display of the second dataset for continuous changes in four controlled variables during step tests.</div>


---

<!-- PDF page 509 -->

<div style="text-align: center;">Figure 8.42 Merge two datasets into a new dataset, WS8_1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_364_147_797_294.jpg" alt="Image" width="44%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'></th><th style='text-align: center;'>10/2/1996</th><th style='text-align: center;'>10/4/1996</th><th style='text-align: center;'>10/6/1996</th><th style='text-align: center;'>10/8/1996</th><th style='text-align: center;'>10/10/1996</th><th style='text-align: center;'>10/12/1996</th><th style='text-align: center;'>10/14/1996</th><th style='text-align: center;'>10/16/1996</th><th style='text-align: center;'>10/18/1996</th><th style='text-align: center;'>10/20/1996</th><th style='text-align: center;'>10/22/1996</th><th style='text-align: center;'>10/24/1996</th><th style='text-align: center;'>10/26/1996</th><th style='text-align: center;'>10/28/1996</th><th style='text-align: center;'>10/30/1996</th><th style='text-align: center;'>10/32/1996</th><th style='text-align: center;'>10/34/1996</th><th style='text-align: center;'>10/36/1996</th><th style='text-align: center;'>10/38/1996</th><th style='text-align: center;'>10/40/1996</th><th style='text-align: center;'>10/42/1996</th><th style='text-align: center;'>10/44/1996</th><th style='text-align: center;'>10/46/1996</th><th style='text-align: center;'>10/48/1996</th><th style='text-align: center;'>10/50/1996</th><th style='text-align: center;'>10/52/1996</th><th style='text-align: center;'>10/54/1996</th><th style='text-align: center;'>10/56/1996</th><th style='text-align: center;'>10/58/1996</th><th style='text-align: center;'>10/60/1996</th><th style='text-align: center;'>10/62/1996</th><th style='text-align: center;'>10/64/1996</th><th style='text-align: center;'>10/66/1996</th><th style='text-align: center;'>10/68/1996</th><th style='text-align: center;'>10/70/1996</th><th style='text-align: center;'>10/72/1996</th><th style='text-align: center;'>10/74/1996</th><th style='text-align: center;'>10/76/1996</th><th style='text-align: center;'>10/78/1996</th><th style='text-align: center;'>10/80/1996</th><th style='text-align: center;'>10/82/1996</th><th style='text-align: center;'>10/84/1996</th><th style='text-align: center;'>10/86/1996</th><th style='text-align: center;'>10/88/1996</th><th style='text-align: center;'>10/90/1996</th><th style='text-align: center;'>10/92/1996</th><th style='text-align: center;'>10/94/1996</th><th style='text-align: center;'>10/96/1996</th><th style='text-align: center;'>10/98/1996</th><th style='text-align: center;'>10/100/1996</th><th style='text-align: center;'>10/102/1996</th><th style='text-align: center;'>10/104/1996</th><th style='text-align: center;'>10/106/1996</th><th style='text-align: center;'>10/108/1996</th><th style='text-align: center;'>10/110/1996</th><th style='text-align: center;'>10/112/1996</th><th style='text-align: center;'>10/114/1996</th><th style='text-align: center;'>10/116/1996</th><th style='text-align: center;'>10/118/1996</th><th style='text-align: center;'>10/120/1996</th><th style='text-align: center;'>10/122/1996</th><th style='text-align: center;'>10/124/1996</th><th style='text-align: center;'>10/126/1996</th><th style='text-align: center;'>10/128/1996</th><th style='text-align: center;'>10/130/1996</th><th style='text-align: center;'>10/132/1996</th><th style='text-align: center;'>10/134/1996</th><th style='text-align: center;'>10/136/1996</th><th style='text-align: center;'>10/138/1996</th><th style='text-align: center;'>10/140/1996</th><th style='text-align: center;'>10/142/1996</th><th style='text-align: center;'>10/144/1996</th><th style='text-align: center;'>10/146/1996</th><th style='text-align: center;'>10/148/1996</th><th style='text-align: center;'>10/150/1996</th><th style='text-align: center;'>10/152/1996</th><th style='text-align: center;'>10/154/1996</th><th style='text-align: center;'>10/156/1996</th><th style='text-align: center;'>10/158/1996</th><th style='text-align: center;'>10/160/1996</th><th style='text-align: center;'>10/162/1996</th><th style='text-align: center;'>10/164/1996</th><th style='text-align: center;'>10/166/1996</th><th style='text-align: center;'>10/168/1996</th><th style='text-align: center;'>10/170/1996</th><th style='text-align: center;'>10/172/1996</th><th style='text-align: center;'>10/174/1996</th><th style='text-align: center;'>10/176/1996</th><th style='text-align: center;'>10/178/1996</th><th style='text-align: center;'>10/180/1996</th><th style='text-align: center;'>10/182/1996</th><th style='text-align: center;'>10/184/1996</th><th style='text-align: center;'>10/186/1996</th><th style='text-align: center;'>10/188/1996</th><th style='text-align: center;'>10/190/1996</th><th style='text-align: center;'>10/192/1996</th><th style='text-align: center;'>10/194/1996</th><th style='text-align: center;'>10/196/1996</th><th style='text-align: center;'>10/198/1996</th><th style='text-align: center;'>10/200/1996</th><th style='text-align: center;'>10/202/1996</th><th style='text-align: center;'>10/204/1996</th><th style='text-align: center;'>10/206/1996</th><th style='text-align: center;'>10/208/1996</th><th style='text-align: center;'>10/210/1996</th><th style='text-align: center;'>10/212/1996</th><th style='text-align: center;'>10/214/1996</th><th style='text-align: center;'>10/216/1996</th><th style='text-align: center;'>10/218/1996</th><th style='text-align: center;'>10/220/1996</th><th style='text-align: center;'>10/222/1996</th><th style='text-align: center;'>10/224/1996</th><th style='text-align: center;'>10/226/1996</th><th style='text-align: center;'>10/228/1996</th><th style='text-align: center;'>10/230/1996</th><th style='text-align: center;'>10/232/1996</th><th style='text-align: center;'>10/234/1996</th><th style='text-align: center;'>10/236/1996</th><th style='text-align: center;'>10/238/1996</th><th style='text-align: center;'>10/240/1996</th><th style='text-align: center;'>10/242/1996</th><th style='text-align: center;'>10/244/1996</th><th style='text-align: center;'>10/246/1996</th><th style='text-align: center;'>10/248/1996</th><th style='text-align: center;'>10/250/1996</th><th style='text-align: center;'>10/252/1996</th><th style='text-align: center;'>10/254/1996</th><th style='text-align: center;'>10/256/1996</th><th style='text-align: center;'>10/258/1996</th><th style='text-align: center;'>10/260/1996</th><th style='text-align: center;'>10/262/1996</th><th style='text-align: center;'>10/264/1996</th><th style='text-align: center;'>10/266/1996</th><th style='text-align: center;'>10/268/1996</th><th style='text-align: center;'>10/270/1996</th><th style='text-align: center;'>10/272/1996</th><th style='text-align: center;'>10/274/1996</th><th style='text-align: center;'>10/276/1996</th><th style='text-align: center;'>10/278/1996</th><th style='text-align: center;'>10/280/1996</th><th style='text-align: center;'>10/282/1996</th><th style='text-align: center;'>10/284/1996</th><th style='text-align: center;'>10/286/1996</th><th style='text-align: center;'>10/288/1996</th><th style='text-align: center;'>10/290/1996</th><th style='text-align: center;'>10/292/1996</th><th style='text-align: center;'>10/294/1996</th><th style='text-align: center;'>10/296/1996</th><th style='text-align: center;'>10/298/1996</th><th style='text-align: center;'>10/300/1996</th><th style='text-align: center;'>10/302/1996</th><th style='text-align: center;'>10/304/1996</th><th style='text-align: center;'>10/306/1996</th><th style='text-align: center;'>10/308/1996</th><th style='text-align: center;'>10/310/1996</th><th style='text-align: center;'>10/312/1996</th><th style='text-align: center;'>10/314/1996</th><th style='text-align: center;'>10/316/1996</th><th style='text-align: center;'>10/318/1996</th><th style='text-align: center;'>10/320/1996</th><th style='text-align: center;'>10/322/1996</th><th style='text-align: center;'>10/324/1996</th><th style='text-align: center;'>10/326/1996</th><th style='text-align: center;'>10/328/1996</th><th style='text-align: center;'>10/330/1996</th><th style='text-align: center;'>10/332/1996</th><th style='text-align: center;'>10/334/1996</th><th style='text-align: center;'>10/336/1996</th><th style='text-align: center;'>10/338/1996</th><th style='text-align: center;'>10/340/1996</th><th style='text-align: center;'>10/342/1996</th><th style='text-align: center;'>10/344/1996</th><th style='text-align: center;'>10/346/1996</th><th style='text-align: center;'>10/348/1996</th><th style='text-align: center;'>10/350/1996</th><th style='text-align: center;'>10/352/1996</th><th style='text-align: center;'>10/354/1996</th><th style='text-align: center;'>10/356/1996</th><th style='text-align: center;'>10/358/1996</th><th style='text-align: center;'>10/360/1996</th><th style='text-align: center;'>10/362/1996</th><th style='text-align: center;'>10/364/1996</th><th style='text-align: center;'>10/366/1996</th><th style='text-align: center;'>10/368/1996</th><th style='text-align: center;'>10/370/1996</th><th style='text-align: center;'>10/372/1996</th><th style='text-align: center;'>10/374/1996</th><th style='text-align: center;'>10/376/1996</th><th style='text-align: center;'>10/378/1996</th><th style='text-align: center;'>10/380/1996</th><th style='text-align: center;'>10/382/1996</th><th style='text-align: center;'>10/384/1996</th><th style='text-align: center;'>10/386/1996</th><th style='text-align: center;'>10/388/1996</th><th style='text-align: center;'>10/390/1996</th><th style='text-align: center;'>10/392/1996</th><th style='text-align: center;'>10/394/1996</th><th style='text-align: center;'>10/396/1996</th><th style='text-align: center;'>10/398/1996</th><th style='text-align: center;'>10/400/1996</th><th style='text-align: center;'>10/402/1996</th><th style='text-align: center;'>10/404/1996</th><th style='text-align: center;'>10/406/1996</th><th style='text-align: center;'>10/408/1996</th><th style='text-align: center;'>10/410/1996</th><th style='text-align: center;'>10/412/1996</th><th style='text-align: center;'>10/414/1996</th><th style='text-align: center;'>10/416/1996</th><th style='text-align: center;'>10/418/1996</th><th style='text-align: center;'>10/420/1996</th><th style='text-align: center;'>10/422/1996</th><th style='text-align: center;'>10/424/1996</th><th style='text-align: center;'>10/426/1996</th><th style='text-align: center;'>10/428/1996</th><th style='text-align: center;'>10/430/1996</th><th style='text-align: center;'>10/432/1996</th><th style='text-align: center;'>10/434/1996</th><th style='text-align: center;'>10/436/1996</th><th style='text-align: center;'>10/438/1996</th><th style='text-align: center;'>10/440/1996</th><th style='text-align: center;'>10/442/1996</th><th style='text-align: center;'>10/444/1996</th><th style='text-align: center;'>10/446/1996</th><th style='text-align: center;'>10/448/1996</th><th style='text-align: center;'>10/450/1996</th><th style='text-align: center;'>10/452/1996</th><th style='text-align: center;'>10/454/1996</th><th style='text-align: center;'>10/456/1996</th><th style='text-align: center;'>10/458/1996</th><th style='text-align: center;'>10/460/1996</th><th style='text-align: center;'>10/462/1996</th><th style='text-align: center;'>10/464/1996</th><th style='text-align: center;'>10/466/1996</th><th style='text-align: center;'>10/468/1996</th><th style='text-align: center;'>10/470/1996</th><th style='text-align: center;'>10/472/1996</th><th style='text-align: center;'>10/474/1996</th><th style='text-align: center;'>10/476/1996</th><th style='text-align: center;'>10/478/1996</th><th style='text-align: center;'>10/480/1996</th><th style='text-align: center;'>10/482/1996</th><th style='text-align: center;'>10/484/1996</th><th style='text-align: center;'>10/486/1996</th><th style='text-align: center;'>10/488/1996</th><th style='text-align: center;'>10/490/1996</th><th style='text-align: center;'>10/492/1996</th><th style='text-align: center;'>10/494/1996</th><th style='text-align: center;'>10/496/1996</th><th style='text-align: center;'>10/498/1996</th><th style='text-align: center;'>10/500/1996</th><th style='text-align: center;'>10/502/1996</th><th style='text-align: center;'>10/504/1996</th><th style='text-align: center;'>10/506/1996</th><th style='text-align: center;'>10/508/1996</th><th style='text-align: center;'>10/510/1996</th><th style='text-align: center;'>10/512/1996</th><th style='text-align: center;'>10/514/1996</th><th style='text-align: center;'>10/516/1996</th><th style='text-align: center;'>10/518/1996</th><th style='text-align: center;'>10/520/1996</th><th style='text-align: center;'>10/522/1996</th><th style='text-align: center;'>10/524/1996</th><th style='text-align: center;'>10/526/1996</th><th style='text-align: center;'>10/528/1996</th><th style='text-align: center;'>10/530/1996</th><th style='text-align: center;'>10/532/1996</th><th style='text-align: center;'>10/534/1996</th><th style='text-align: center;'>10/536/1996</th><th style='text-align: center;'>10/538/1996</th><th style='text-align: center;'>10/540/1996</th><th style='text-align: center;'>10/542/1996</th><th style='text-align: center;'>10/544/1996</th><th style='text-align: center;'>10/546/1996</th><th style='text-align: center;'>10/548/1996</th><th style='text-align: center;'>10/550/1996</th><th style='text-align: center;'>10/552/1996</th><th style='text-align: center;'>10/554/1996</th><th style='text-align: center;'>10/556/1996</th><th style='text-align: center;'>10/558/1996</th><th style='text-align: center;'>10/560/1996</th><th style='text-align: center;'>10/562/1996</th><th style='text-align: center;'>10/564/1996</th><th style='text-align: center;'>10/566/1996</th><th style='text-align: center;'>10/568/1996</th><th style='text-align: center;'>10/570/1996</th><th style='text-align: center;'>10/572/1996</th><th style='text-align: center;'>10/574/1996</th><th style='text-align: center;'>10/576/1996</th><th style='text-align: center;'>10/578/1996</th><th style='text-align: center;'>10/580/1996</th><th style='text-align: center;'>10/582/1996</th><th style='text-align: center;'>10/584/1996</th><th style='text-align: center;'>10/586/1996</th><th style='text-align: center;'>10/588/1996</th><th style='text-align: center;'>10/590/1996</th><th style='text-align: center;'>10/592/1996</th><th style='text-align: center;'>10/594/1996</th><th style='text-align: center;'>10/596/1996</th><th style='text-align: center;'>10/598/1996</th><th style='text-align: center;'>10/600/1996</th><th style='text-align: center;'>10/602/1996</th><th style='text-align: center;'>10/604/1996</th><th style='text-align: center;'>10/606/1996</th><th style='text-align: center;'>10/608/1996</th><th style='text-align: center;'>10/610/1996</th><th style='text-align: center;'>10/612/1996</th><th style='text-align: center;'>10/614/1996</th><th style='text-align: center;'>10/616/1996</th><th style='text-align: center;'>10/618/1996</th><th style='text-align: center;'>10/620/1996</th><th style='text-align: center;'>10/622/1996</th><th style='text-align: center;'>10/624/1996</th><th style='text-align: center;'>10/626/1996</th><th style='text-align: center;'>10/628/1996</th><th style='text-align: center;'>10/630/1996</th><th style='text-align: center;'>10/632/1996</th><th style='text-align: center;'>10/634/1996</th><th style='text-align: center;'>10/636/1996</th><th style='text-align: center;'>10/638/1996</th><th style='text-align: center;'></th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.43 Merged dataset WS8_1.</div>


Next, we follow the path: tool ribbons → dataset actions → merge → create new dataset: name – WS8_1 → OK. See Figure 8.42.

Figure 8.43 illustrates the merged datasets. We note that the software has automatically highlighted in gray the section of date and time within the duration of the dataset that contains bad/missing values. When we choose to use our mouse to highlight the gray section, it will become green and activate the data slicing tools on the top ribbon buttons. See Figure 8.44.

We then click on the “Mark Bad” ribbon button and see the input window of Figure 8.45, in which we apply global slicing tool to remove bad dataset section of all vectors (variables) with missing data and click the OK button.

#### 8.2.5 Create Manipulated Variable (MV) and Controlled Variable (CV) Lists

On the top tool ribbon, we choose Manage Lists to build: (1) MV (manipulated variable) list – Flow_MMA, Flow_VA, Init, Transf, and T_Jkt; and (2) CV (controlled variable) list – Polymer, Mol_Wt, T_Rx, and Conc_MMA. Use the Add (+) and Delete (−) buttons to create a new list or delete an existing list, respectively. After creating a list, choose the desired variable (vector) from the right-top list and use the arrow

---

<!-- PDF page 510 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_146_808_451.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.44 Using a mouse to highlight the bad/missing data section to activate the data slicing tools in the ribbon buttons.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_550_678_924.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">Figure 8.45 Global slicing of bad dataset section of all vectors (variables) with missing data.</div>


key to move it to the list on the right-button section. See Figures 8.46 and 8.47 for the MV and CV lists.

We pause to present an important note. Our MVs are independent variables that the operator can change. A control problem may include additional independent variables, called feedforward variables (FF), that impact the process, but the operator cannot change them directly. If our dataset from plant step tests includes the time-dependent change profile of FF vectors (variables), we should include those FF vectors to the end of the independent variable list. For our current problem, we would

---

<!-- PDF page 511 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_148_781_389.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.46 Manipulated variable list, MV.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_458_779_700.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.47 Controlled variable list, CV.</div>


include any FF variables to the end of the MV list in Figure 8.46 and place those FF variables after the reactor cooling jacket temperature variable, T_Jkt.

#### 8.2.6 DMC3 Builder Task One: Model Identification (ID) for Developing Master Model – Setting up the Model ID

We click on Create Model button located at the far right of the tool ribbons to start building the dynamic controller model using the dataset, WS8.1_1. In the Identify Model-Specify Structure input form, we enter model name, copolymerization, specify a time to steady state of 90 min, and choose the five MVs as input variables, and the four CVs as output variables. See Figure 8.48. Click OK to see the Case Editor Screen of Figure 8.49.

On the left column of the navigation tree for copolymerization controller, we click on All Variables within Master Model to see a listing of dataset and input and output variables, as illustrated in Figure 8.50.

Next, we click on parameter trials of the case views on the tool ribbons (see Figure 8.50) to start specifying the trial cases, focusing on FIR trials (simulation runs) with the parameters listed in Table 8.3.

---

<!-- PDF page 512 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_149_811_402.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.48 Controller model specification.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_478_811_762.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.49 Case editor screen.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_838_810_1124.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.50 Dataset and input and output variables.</div>


---

<!-- PDF page 513 -->

<div style="text-align: center;">Table 8.3 Parameters for FIR trial cases, WS8.1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Time to steady state (min)</td><td style='text-align: center; word-wrap: break-word;'>Number of coefficients</td><td style='text-align: center; word-wrap: break-word;'>Smoothing factor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>120</td><td style='text-align: center; word-wrap: break-word;'>120</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_412_780_688.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.51 List of trial cases.</div>


When we click on Parameter Trials, the software automatically creates the cases with “Time to Steady State  $ (T_{ss}) $” equal to 30, 60, and 90 min. Make sure to check the boxes for Master, Prediction, Uncertainty, and Time Uncertainty for the 90-min case. We also need to click on the “+” button next to FIR trials to add the new case with a  $ T_{ss} $ of 120 min. See Figure 8.51.

As our sampling period (data collection interval) is 1 min (Figure 8.48), the software assumes a controller execution interval of 1 min and gives the Number of Model Coefficients equal to the  $ T_{SS} $ according to Eq. (8.48):

 $$ \begin{bmatrix}Controller\\ Execution\\ Interval,min\end{bmatrix}=\frac{Time to Steady State,\ min}{Number of Moel Coefficients}\times\begin{bmatrix}Sampling\\ Period,min\end{bmatrix} $$ 

Model coefficients are required to model faster responses. For example, if the controller execution interval is 0.5 min, with the  $ T_{ss} (=90\text{ min}) $ and sampling period (=1 min) remain the same, Eq. (8.48) means the number of model coefficients is 180. The number of model coefficients also determines the number of future control moves being calculated by DMC3 Builder. See Table 8.4. We note that the larger the number of model coefficients, the smaller the controller execution interval, and the larger the number of control moves calculated. Understanding this relationship is

---

<!-- PDF page 514 -->

<div style="text-align: center;">Table 8.4 Relationship between the number of model coefficients and the number of control moves calculated.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Number of model coefficients</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>45</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>105</td><td style='text-align: center; word-wrap: break-word;'>120</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Number of control moves calculated</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>14</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_338_808_530.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.52 Window display of the progress of the FIR model identification.</div>


key to applying control to respond to fast-changing independent disturbances in the system.

The third parameter, Smoothing Factor, is used to smooth the data and apply the penalty for change between successive FIR model coefficients. The default value of 5 is acceptable in most cases.

We now move to Case Actions within the tool buttons and click on the Identify button to run the model identification (ID). Figure 8.52 shows the window display of the progress of the FIR model identification. We click “Close” when see the message “Solution Complete.” Figure 8.53 shows the identified smoothed and unsmoothed model curves for each  $ T_{SS} $.

#### 8.2.7 Guidelines for Selecting Model Parameters

In Section 8.2.6, we have previously discussed the number of model coefficients in relation to Eq. (8.48), the sampling period, and the controller execution interval. We indicate that the use of a smoothing factor of 5 is always a good practice. How do we then choose the third parameter, the  $ T_{SS} $?

We choose the  $ T_{ss} $ based on the slowest responses in the model, and all model responses should reach steady state at the selected  $ T_{ss} $. We extend faster response curves to match the selected  $ T_{ss} $.

Figures 8.54a–d compare the FIR curves at  $ T_{ss} = 30 $, 60, 90, and 120 min and with a smoothing factor of 5. The comparison confirms our selection of master model with a  $ T_{ss} $ of 90 min for all control variables (Polymer, Mol_Wt, T_Rx, and Conc_MA) to reach their steady-state values. In general, a control variable will continue to change past a chosen  $ T_{ss} $ value that is too short; and a large  $ T_{ss} $ will cause the

---

<!-- PDF page 515 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Output Real</td><td style='text-align: center; word-wrap: break-word;'>Typical Move</td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>MOL, SIT</td><td style='text-align: center; word-wrap: break-word;'>T, RSI</td><td style='text-align: center; word-wrap: break-word;'>CONC, MBA</td></tr><tr><td rowspan="3">FLOP, MBA</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-6, 27</td><td style='text-align: center; word-wrap: break-word;'>-18, 33</td><td style='text-align: center; word-wrap: break-word;'>-4, 293</td><td style='text-align: center; word-wrap: break-word;'>-6, 264</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-405</td><td style='text-align: center; word-wrap: break-word;'>-11, 15</td><td style='text-align: center; word-wrap: break-word;'>-5, 275</td><td style='text-align: center; word-wrap: break-word;'>-2, 237</td></tr><tr><td rowspan="3">FLOP, VA</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-7, 18</td><td style='text-align: center; word-wrap: break-word;'>-424</td><td style='text-align: center; word-wrap: break-word;'>-1, 375</td><td style='text-align: center; word-wrap: break-word;'>-1, 491</td></tr><tr><td rowspan="3">NET</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-40</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-7, 18</td><td style='text-align: center; word-wrap: break-word;'>-424</td><td style='text-align: center; word-wrap: break-word;'>-1, 375</td><td style='text-align: center; word-wrap: break-word;'>-1, 491</td></tr><tr><td rowspan="3">TRHGF</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-7, 18</td><td style='text-align: center; word-wrap: break-word;'>-424</td><td style='text-align: center; word-wrap: break-word;'>-1, 375</td><td style='text-align: center; word-wrap: break-word;'>-1, 491</td></tr><tr><td rowspan="3">T, KT</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-25</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td><td style='text-align: center; word-wrap: break-word;'>-20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-7, 18</td><td style='text-align: center; word-wrap: break-word;'>-424</td><td style='text-align: center; word-wrap: break-word;'>-1, 375</td><td style='text-align: center; word-wrap: break-word;'>-1, 491</td></tr></table>

<div style="text-align: center;">Figure 8.53 Identified smoothed and unsmoothed model response curves: "fir S5, U90" means finite-impulse response; smoothing factor = 5;  $ T_{SS} = 90 $ min.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Output Input</td><td style='text-align: center; word-wrap: break-word;'>Typical Move</td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>HOL VIT</td><td style='text-align: center; word-wrap: break-word;'>T,RX</td><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td></tr><tr><td rowspan="4">FLORI_MMA</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4.2</td><td style='text-align: center; word-wrap: break-word;'>10.5</td><td style='text-align: center; word-wrap: break-word;'>4.05</td><td style='text-align: center; word-wrap: break-word;'>4.45</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4.0</td><td style='text-align: center; word-wrap: break-word;'>10.5</td><td style='text-align: center; word-wrap: break-word;'>4.05</td><td style='text-align: center; word-wrap: break-word;'>4.45</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>40</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr></table>

<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_150_692_727_801.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_143_820_727_920.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_148_939_734_1034.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">Figure 8.54 (a)–(d) Evaluation of the selection of time to steady state ( $ T_{ss} $). (a) first S5 U30: finite-impulse response → S5 = smoothing factor of 5, U30 =  $ T_{ss} $ of 30 min. MOL_WT and CONC_MMA (y-axis) continue to increase past  $ T_{ss} $ of 30 min (x-axis). T_RX continues to drop past  $ T_{ss} $ of 30 min. Pay attention to the red curve that ends at 30 min. (b) first S5 U60:  $ T_{ss} $ of 60 min. MOL_WT and CONC_MMA continue to increase past  $ T_{ss} $ of 60 min. T_RX continues to drop past  $ T_{ss} $ of 60 min. (c) first S5 U90:  $ T_{ss} $ of 90 min. POLYMER, MOL_WT, T_RX, and CONC_MMA appear to reach their steady-state values and do not change much past  $ T_{ss} $ of 90 min. (d) first S5 U120:  $ T_{ss} $ of 120 min appears to be too long as all dependent variables have already reached their steady-state values around  $ T_{ss} $ of 90 min.</div>


---

<!-- PDF page 516 -->

smoothed and unsmoothed response curves of a control variable to drift apart at the end.

#### 8.2.8 Uncertainty and Correlation Plots of the Master Model

We display the master model with a  $ T_{ss} $ of 90 min by following the path on the navigation tree: Copolymerization Model → Master Model → Cases Folder → All Variables and click on the “Frequency Uncertainty” button on the tool ribbons. Figure 8.55 shows the resulting frequency-domain uncertainty plot. In each response plot, the shaded area above and below the dark average response curve indicates a two-sigma confidence region that includes 95.4% of all data points. The narrower the shaded area, the more accurate the average response curve is. For example, the model response plots of Mol_Wt and Conc_MMA to changes in Flow_MMA contain very narrow two-sigma confidence region and the quality of these model response plots is graded “excellent” or “A.” By contrast, the wide shaded two-sigma region for the model response plot of T_Rx to changes in Flow_MMA and in Transf indicates a plot of poor quality with a grade of “C.” We see plots of very poor quality with large shaded two-sigma region for the model response plot of Polymer to changes in Transf with a grade of D.

Likewise, Figure 8.56 shows the time-domain uncertainty plot. For each input/output variable pair, we see the shaded two-sigma confidence region, and the corresponding model grade from A to D. Both frequency-domain and time-domain uncertainty plots result in essentially identical model grades.

The correlation plot of Figure 8.57 shows how much an input variable or MV correlates with another input variable. The correlation coefficient is a statistical measure of the strength of the relationship between the relative movements of two variables. The values range between -1.0 and 1.0. … A correlation of -1.0 shows a perfect negative correlation, while a correlation of 1.0 shows a perfect positive correlation.

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_896_809_1219.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.55 Frequency domain uncertainty plot for the master model at a  $ T_{ss} $ of 90 min.</div>


---

<!-- PDF page 517 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_779_427.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.56 Time domain uncertainty plot for the master model with a  $ T_{ss} $ of 90 min.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_499_778_820.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.57 Correlation plot for the master model at a  $ T_{ss} $ of 90 min.</div>


In Figure 8.57, both x-axis and y-axis represent input variables or MVs. We see the value of the correlation coefficient between two input variables on the upper right corner of each plot, with values between 0 and 0.28, indicating a relatively minor positive correlation.

#### 8.2.9 DMC3 Builder Task One: Building the Controller Model for Developing the Master Model

Before creating the final controller model, we need to check the steady-state gain of each input-output pair and investigate which changes in an input variable have a notable impact on a specific output variable. Specifically, we copy the steady-state gain values of all input-output pairs by following the path: Controllers→Copolymerization→Master Model→Case Folder→All Variables→Right-click within the workspace of model response curves→Copy gains. See Figures 8.58 and 8.59.

---

<!-- PDF page 518 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_149_808_366.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.58 Copying steady-state gains of model response curves.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>0.17934</td><td style='text-align: center; word-wrap: break-word;'>45.14481</td><td style='text-align: center; word-wrap: break-word;'>-0.03789</td><td style='text-align: center; word-wrap: break-word;'>0.06183</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>0.30703</td><td style='text-align: center; word-wrap: break-word;'>20.66526</td><td style='text-align: center; word-wrap: break-word;'>0.02761</td><td style='text-align: center; word-wrap: break-word;'>-0.03299</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>6.48822</td><td style='text-align: center; word-wrap: break-word;'>-449.30365</td><td style='text-align: center; word-wrap: break-word;'>-1.79204</td><td style='text-align: center; word-wrap: break-word;'>-1.48661</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>0.057621</td><td style='text-align: center; word-wrap: break-word;'>-69.59745</td><td style='text-align: center; word-wrap: break-word;'>-0.08827</td><td style='text-align: center; word-wrap: break-word;'>-0.001382</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>1.68508</td><td style='text-align: center; word-wrap: break-word;'>19.29814</td><td style='text-align: center; word-wrap: break-word;'>1.14019</td><td style='text-align: center; word-wrap: break-word;'>-0.03625</td></tr></table>

<div style="text-align: center;">Figure 8.59 Steady-state gains of model response curves with a  $ T_{ss} $ of 90 min.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_Wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_Wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Flow\_VA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_Wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Init}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_Wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Transf}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Polymer}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Mol\_Wt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Rx}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{Conc\_MMA}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_Jkt}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta(\text{T\_kJt}) $</td></tr></table>

<div style="text-align: center;">Figure 8.60 Explicit ratio elements of the steady-state gain matrix.</div>


Figure 8.60 gives the explicit ratio elements of the steady-state gain matrix of Figure 8.23.

Comparing the magnitudes of the steady-state gain values in each CV column, we conclude that all input variables or MV rows have a notable influence on the “polymer molecular weight” column. Additionally, we note the following:

1. The mass flow rate of the chain-transfer agent, Transf, has the least influence on the polymer mass flow rate, Polymer, with a gain of 0.057621.

2. Both mass flow rates of MMA and VA, that is, Flow_MMA and Flow_VA, have the smallest influences on the reactor exit temperature, T_Rx with gains of -0.03789 and 0.02761.

---

<!-- PDF page 519 -->

3. The mass flow rate of the chain-transfer agent, Transf, has the least influence on the concentration or mole fraction of monomer MMA in the polymer product, Conc_MMA with a gain of -0.001382.

We eliminate those MVs that have the least influence on a specific CV with the smallest steady-state gain values and click on “Mask Selection” to disable copying those response curves over to the final master model. For example, we mask the mass flow rate of transfer agent, Transf, as a MV for controlling the mole fraction of MMA in the polymer product, Conc_MMA, by highlighting the corresponding response curve, right-clicking to show the selection menu, and then choosing “Mask Selection.” See Figures 8.61 and 8.62.

#### 8.2.10 DMC3 Builder Task One: Creating a Controller Model

The first step to creating a controller model is to define the various trial runs as the Master trial. We confirm our previous selection, illustrated in Figure 8.53. We

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_562_778_882.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.61 Eliminating the model response curve of a selected input-output pair from the final master model by Mark Selection.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_974_778_1205.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.62 A display of four highlighted response curves that are eliminated in the final maser model after Mask Selection.</div>


---

<!-- PDF page 520 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_810_427.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.63 Master Model view waiting for Update Curves to copy the Master Case response curves with a  $ T_{ss} $ of 90 min to the empty model panel.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_518_809_727.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.64 Model update report after clicking on Update Curve.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_799_809_1058.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.65 Updated final master model with a  $ T_{ss} $ of 90 min.</div>


click on Master Model in the navigation tree and see the Model views in the tool ribbons. Click on Update Curve within Model Operations in the tool ribbons. See Figure 8.63. After clicking on Update Curves, we see a model update report. Be sure to choose “Allow overwrite of all null models in the master,” and “Overwrite all curve operations” (see Figure 8.64). Clicking OK will generate the Master Model response curves of Figure 8.65.

---

<!-- PDF page 521 -->

#### 8.2.11 Identification of Dead Time in Model Response Curves

We enlarge the model response curve between Flow_VA and Mol_Wt by double-clicking on the curve. The enlarged curve appears to show a dead time of about 9 min before Mol_Wt begins to change after Flow_VA changes. We identify the dead time by following the path: Highlight the model curve → Right-click to open the menu for curve operations → Click on Curve Operations (see Figure 8.66) → Shift the curve by −9 min and update chart (see Figure 8.67) → Then shift the curve by +9 min and update chart (see Figure 8.68) → Update curve.

Figure 8.69 shows the model response curves resulting from this curve operation to identify the dead time between output variable Mol_Wt and input variable Flow_VA. Note the dark blue triangle on the lower right corner of the response curve plot between these variables.

Following the same procedure, we identify the dead times of other input-output pairs. Figure 8.70 shows the resulting model response curves.

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_569_779_864.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.66 Access the menu for curve operations.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_958_779_1219.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.67 Shifting the model curve by -9 min and updating chart.</div>


---

<!-- PDF page 522 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_167_156_809_405.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.68 Shifting the model curve by 9 min and updating chart.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_476_809_786.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.69 Model response plot with a blue triangular on the lower right corner of a plot indicating having completed a curve operation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_872_809_1179.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.70 Model response curves after curve operations for dead times.</div>


---

<!-- PDF page 523 -->

#### 8.2.12 Collinearity Analysis

Always perform collinearity analysis (discussed in Sections 8.1.4.1 and 8.1.4.2) on the master model before its deployment. The collinearity analysis identifies and repairs ill-conditioned model matrices. It can identify sub-models from a model matrix that are nearly collinear or highly nonlinear. A collinearity analysis includes the following four steps:

Step 1. Select variables and specify options – We choose MVs and CVs to be analyzed and specify the gain analysis options, such as RGA (relative gain analysis) threshold, singular value analysis, and allowable gain changes.

Step 2. Analyze and determine relationships – We analyze the model and determine which CV-MV pairs have collinearity trouble and specify confidence limits for the gains on individual model response curves.

Step 3. Create groups – We create groups using MV–CV curves that do not have square relationships  $ (2\times2, 3\times3, \text{etc.}) $.

Step 4. Repair groups and update model – We repair gains for the square and non-square groups by either collinearizing or un-collinearizing the groups.

We explain and demonstrate the details of each step below.

### Step 1. Select Variables and Specify Options

We begin by going to the Controller navigation tree and choosing Copoly-merization → Master Model. On the top tool buttons, we click on “Collinearity” within “Model Operations.” See Figure 8.71. We immediately see a dialog: “Do you want to use collinearity repair wizard?” We choose “No” in order to use the collinearity repair dialog. See Figure 8.72.

We then see “Select Variables–Copolymerization” and select all MVs and CVs for analysis. Click OK to proceed to the Collinearity Analysis window. See Figure 8.73. We note that if our list of MVs includes FF variables, we do not choose them in the collinearity analysis.

Next, we see the “Collinearity Analysis–Copolymerization” window, displaying the top toolbar for collinearity analysis buttons. We click on “Options” and see the window of “Collinearity Options,” as shown in Figure 8.74. We note that the default settings specify the use of RGA with a relative gain threshold of 10, a large threshold of 50, and a small threshold

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1025_778_1221.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.71 Activate the collinearity analysis within model operations.</div>


---

<!-- PDF page 524 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_152_808_362.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.72 Choose the collinearity repair dialog by clicking on "No."</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_431_809_545.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.73 Select variables for collinearity analysis.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_613_811_956.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.74 Collinearity analysis options with default settings: relative gain array (RGA) or singular value analysis (SVA).</div>


of 1. These default settings will suffice for our model. We click OK on the “Collinearity Options” window to accept these settings, and then see the display of the results of the collinearity analysis of Figure 8.75. In the figure, we see that the total number of submatrices as 1. This follows because we have 5 MVs and 4 CVs, and a 5×4 gain matrix; and RGA applies only to a single 4×4 square submatrix of the 5×4 gain matrix.

### Step 2. Analyze and Determine Relationships

Figure 8.75 shows that there are two collinear systems, as indicated by the shaded MV–CV pairs: (Flow_VA)-(MOL-WT) with a gain of 21.15 and

---

<!-- PDF page 525 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Options</td><td style='text-align: center; word-wrap: break-word;'>Analyze</td><td style='text-align: center; word-wrap: break-word;'>Create Group</td><td style='text-align: center; word-wrap: break-word;'>Repair Groups</td><td style='text-align: center; word-wrap: break-word;'>Repair Square</td><td style='text-align: center; word-wrap: break-word;'>Highlight</td><td style='text-align: center; word-wrap: break-word;'>Lock</td><td style='text-align: center; word-wrap: break-word;'>Unlock</td><td style='text-align: center; word-wrap: break-word;'>Help</td><td colspan="2">Use closed loop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Relative Gain</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Relative Gain</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Total Submatrices</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Large Threshold:</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Maximum: 2.204</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Perfectly Collinear: 1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Closed Loop: Handles</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Small Threshold:</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Minimum: 0.037</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Nearly Collinear: 0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mode:</td><td style='text-align: center; word-wrap: break-word;'>Uncertainty</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output Input</td><td style='text-align: center; word-wrap: break-word;'>Typical Move</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>T_JX</td><td style='text-align: center; word-wrap: break-word;'>COKIC_MMA</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 8.75 Screen display of the results of collinearity analysis.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分 Options</td><td style='text-align: center; word-wrap: break-word;'>值 Analysis</td><td style='text-align: center; word-wrap: break-word;'>配 Create Group</td><td style='text-align: center; word-wrap: break-word;'>配 Repair Groups</td><td style='text-align: center; word-wrap: break-word;'>配 Repair Squares</td><td style='text-align: center; word-wrap: break-word;'>日 Highlight</td><td style='text-align: center; word-wrap: break-word;'>日 Lock</td><td style='text-align: center; word-wrap: break-word;'>日 Lock</td><td style='text-align: center; word-wrap: break-word;'>Help</td><td style='text-align: center; word-wrap: break-word;'>日</td><td style='text-align: center; word-wrap: break-word;'>&lt;nl&gt;</td></tr></table>

<div style="text-align: center;">Figure 8.76 Choosing the MV and CV to form parallel groups and the resulting red triangles on the top right corners of the variable names.</div>


(T_JKT)-(MOL_WT) with a gain of 21.03; and (FLOW_VA)-(CONC_MMA) with a gain of -0.03412, and (T_JKT)-(CONC_MMA) with a gain of -0.03391.

### Step 3. Create Groups

Next, we click on CV names, MOL_WT and CONC_MMA, and on MV names, FLOW_VA and T_JKT to select these variables to form “Parallel Groups.” This results in a red triangle on the top right corner of the selected variable name. See Figure 8.76.

We then click on the “Create Group” button to the top tool bar for collinearity analysis and see the display of “Edit Parallel Groups” screen of Figure 8.77. Clicking on the “Edit” button displayed in Figure 8.77 will show the screen of Figure 8.78.

---

<!-- PDF page 526 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_148_811_485.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.77 Display of the “Edit Parallel Groups” screen.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_567_809_918.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.78 Creating parallel groups, choosing the default, FLOW_VA, as the pivot, and clicking on "Recalculate" to determine the required gain changes to collinearize the MVs.</div>


### Step 4. Repair Groups and Update Model

We click “OK” in the “Create Parallel Group” folder in Figure 8.78, followed by clicking on “Repair Square” in the top tool bar for collinearity analysis to fix the gain matrix for both remaining square submatrix groups, and the parallel group defined in the previous task. This leads to Figures 8.79 and 8.80, which show the relative gains and the (model) gains, respectively.

We then click on “Repair” followed by “Start.” Figure 8.81 shows the Start and Finish of RGA (relative gain array) repair.

---

<!-- PDF page 527 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_148_779_454.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.79 Display of relative gains after clicking on “Repair Square.”</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_137_513_779_858.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.80 Display of (model) gains after clicking on "Repair Square."</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_920_779_1241.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.81 Run RGA square repair.</div>


---

<!-- PDF page 528 -->

### Step 5. Review and Save Gains to the Master Model

Figure 8.82 asks us to apply the recommended changes. Click OK. This leads to Figure 8.83. We place the mouse inside the figure, right-click to open the options, and choose "Copy Gains."

The final model gains are as follows:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>0.171458</td><td style='text-align: center; word-wrap: break-word;'>44.6648</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.066125</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>0.335285</td><td style='text-align: center; word-wrap: break-word;'>21.14978</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>-0.034125</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>7.51802</td><td style='text-align: center; word-wrap: break-word;'>-424.133</td><td style='text-align: center; word-wrap: break-word;'>-1.97563</td><td style='text-align: center; word-wrap: break-word;'>-1.40089</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>-67.757</td><td style='text-align: center; word-wrap: break-word;'>0.096417</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>1.69798</td><td style='text-align: center; word-wrap: break-word;'>21.0177</td><td style='text-align: center; word-wrap: break-word;'>1.23442</td><td style='text-align: center; word-wrap: break-word;'>-0.033912</td></tr></table>

Before we continue further, we export the current controller application and save it according to the following path: Controller→Copolymerization→Right-click: Export→Save as WS8.1a.dmc3application (see Figure 8.84).

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_540_809_879.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.82 Display of “Apply Collinearity” and apply gain changes directly.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_944_808_1216.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.83 "Copy Gains" of the model after collinearity analysis.</div>


---

<!-- PDF page 529 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_777_353.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.84 Export and save the controller model as WS8.1a.dmc3application.</div>


#### 8.2.13 Open-Loop Prediction and Prediction Error (Model Bias)

We first identify the units and ranges of MVs and CVs in our dataset before continuing with open-loop prediction. Following the path: Controllers → Copolymerization → Master Model → Cases Folder → All variables, we see the units and ranges of MVs and CVs displayed in Figure 8.85.

To proceed with predictions, we follow the path: Controller → Copolymerization → Master Model → Top ribbons: Master Model Actions → Compare → Compare predictions → See Figure 8.86 → Generate predictions → Close → Top ribbons: Zoom-In → Figure 8.87. We note from Figure 8.85 from the dataset, the polymer production rate, POLYMER, varies from 12.297 to 31.843 kg/hr. This is the range of POLYMER in Figure 8.87. To understand Figure 8.87, we note the difference between the prediction (blue) and measurement (red) gives the prediction error (pink). In the figure, we should read the positive and negative values for the prediction error beginning from the baseline of zero prediction error at 20 kg/hr. Figure 8.88 shows the prediction plot for all four CVs.

A significant result from the prediction analysis is the scatter plot. Predictions should be unbiased over the entire dataset range. It is important to review the scatter plot. Figure 8.89 illustrates that the scatter plots for all four CVs in our copolymerization controller appear to be acceptable.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_997_778_1221.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.85 Units and ranges of MVs and CVs in copolymerization controller model.</div>


---

<!-- PDF page 530 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_150_676_532.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">Figure 8.86 Setup for prediction run.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>10/2/1996</th><th style='text-align: center;'>0.0</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.87 Comparison of CV prediction with measurement and illustration of prediction error.</div>


#### 8.2.14 DMC3 Builder Task 2: Configuration – Model Configuration

The model configuration task involves the specifications of: (1) feedback filters for prediction errors (discussed previously in Section 8.1.5 for prediction error filtering); (2) subcontrollers; (3) test groups; and (4) composite participation. See Figure 8.90.

Aspen DMC3 allows a controller to be subdivided into multiple units of MVs and CVs for operational convenience in turning multiple variables ON or OFF at the same time. These units of MVs and CVs are known as subcontrollers. For example, we may classify a large DMC3 controller for an ethylene production train to have the following subcontrollers: (1) ethylene cracked gas compressor and quench;

---

<!-- PDF page 531 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Polymer Flow (kg/hr)</th><th style='text-align: center;'>28</th><th style='text-align: center;'>28</th><th style='text-align: center;'>28</th><th style='text-align: center;'>28</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.88 Prediction plots for all four CVs</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Plot</th><th style='text-align: center;'>X-Axis</th><th style='text-align: center;'>Y-Axis</th><th style='text-align: center;'>Data Type</th><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>Y-Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34000</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34250</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34500</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34750</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>35000</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Left</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>35250</td><td style='text-align: center;'>34477</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34000</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34250</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34500</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>34750</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>35000</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Top-Right</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>POLYMER_Measurement</td><td style='text-align: center;'>NOL_WT</td><td style='text-align: center;'>35250</td><td style='text-align: center;'>34472</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>75.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>78.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>80.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>82.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>84.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>86.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>88.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>90.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>92.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>94.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>96.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>98.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>102.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>104.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>106.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>108.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>110.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>112.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>114.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>116.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>118.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>120.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>122.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>124.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>126.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>128.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>130.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>132.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>134.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>136.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>138.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>140.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>142.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>144.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>146.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>148.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>150.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>152.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>154.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>156.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>158.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>160.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>162.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>164.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>166.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>168.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>170.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>172.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>174.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>176.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>178.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>180.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>182.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>184.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>186.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>188.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>190.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>192.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>194.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>196.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>198.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>200.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>202.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>204.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>206.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>208.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>210.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>212.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>214.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>216.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>218.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>220.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>222.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>224.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>226.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>228.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>230.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>232.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>234.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>236.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>238.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>240.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>242.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>244.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>246.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>248.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>250.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>252.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>254.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>256.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>258.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>260.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>262.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>264.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_MMA_Prediction</td><td style='text-align: center;'>266.0</td><td style='text-align: center;'>76.1</td></tr>
    <tr><td style='text-align: center;'>Bottom-Left</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>T-EK_Measurement</td><td style='text-align: center;'>COMC_</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.89 Scatter plots for all four CVs.</div>


(2) cold-box and demethanizer, refrigeration compressors; and (3) de-ethanizer and C2 splitter. If subcontrollers are used, every MV in the controller must be a member of one and only one subcontroller. Every CV in the controller must be a member of at least one subcontroller, although a CV may belong to more than one subcontroller. FFs do not belong to subcontrollers. Our current workshop deals with a small controller and does not have subcontrollers.

Aspen DMC3 SmartStep application uses primitive process models to predict the behavior of the tested process. When the tester application automatically steps an independent variable, it also keeps dependent variables within their prescribed limits. The result is a constrained step test where all constraints are honored.

---

<!-- PDF page 532 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_647_434.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 8.90 Model configuration task in DMC3.</div>


A SmartStep application uses the concept of test groups to help maximize testing efficiency. A test group consists of MVs and CVs for which step tests are performed. The current workshop does not involve a SmartStep application with test groups.

The last DMC3 model configuration application involves composite controllers. An Aspen DMC3 composite application facilitates the coordinated action of multiple DMC3 controller applications. It works by providing consistently calculated steady-state MV and CV targets to participating controllers. A composite application is typically used in the following scenarios: (1) a large part of the unit is under the control of several controller applications; and (2) controllers on separate processes, with significantly different times to steady-state, are linked by common constraints. A DMC3 composite application utilizes the same steady-state optimization technology that is embedded in FIR controller applications. The composite suite variable set is a superset of all MVs, FFs, and CVs in all participating controllers. The steady-state solution obtained from the DMC3 composite application, therefore, honors the constraints and utilizes the MVs of all the participating controllers. Our current workshop does not include composite applications.

Figure 8.91 illustrates that we specify the default option of “full feedback” of prediction error (model bias), in which we calculate the difference between the current

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_989_810_1200.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.91 Specification of "full feedback" option for prediction error feedback in model configuration.</div>


---

<!-- PDF page 533 -->

measurement and the current prediction to calculate a bias that is applied to each element of the prediction error. This is exactly what we previously demonstrated in Figures 8.9–8.11, Section 8.1.2.1. Figure 8.91 also shows the options of “First order” and “Moving average” filters, which were previously explained in Section 8.1.5 for prediction error filtering. Lastly, the checkboxes in the option of “Intermittent” in Figure 8.91 refer to those CVs for which a new measurement is not available in each controller execution cycle. This is typically the case of a discretely sampled variable, such as composition from a stream analyzer.

#### 8.2.15 DMC3 Builder Task 2: Configuration – Configuring the Steady-State Optimization

We follow Sections 8.1.6.1 and 8.1.6.2 to configure the steady-state optimizer. Figure 8.92 illustrates the interface to configure the SS optimizer. Figures 8.93a and 8.93b show the input entries for MVs and CVs for the steady-state simulator, respectively.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_567_779_714.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.92 Configuration of the steady-state optimizer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_778_779_989.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.93a Input entries for MVs for steady-state simulator.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_1057_779_1222.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.93b Input entries for CVs for steady-state simulator.</div>


---

<!-- PDF page 534 -->

#### 8.2.16 DMC3 Builder Task 3: Optimization – Performing the Steady-State Optimization

We initialize the SS optimizer tuning by clicking on “Initialize Tuning” button. We choose the dataset WS8_1, uncheck “initialize dynamic tuning,” and click “OK,” followed by clicking on “Calculate” button (see Figure 8.94). The results of CV targets from the SS optimization appear in Figures 8.95 and 8.96.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_356_502_617.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">Figure 8.94 Initialize optimizer tuning and calculate.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>Combined Status</td><td style='text-align: center; word-wrap: break-word;'>Service Request</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Ideal Steady State</td><td style='text-align: center; word-wrap: break-word;'>Ideal Constraint</td><td style='text-align: center; word-wrap: break-word;'>SS Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \bullet $ PLOW_SMAA</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \triangle $</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>-0.1715</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>84</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>91</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>-0.3353</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INT</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0.16</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.13</td><td style='text-align: center; word-wrap: break-word;'>0.33</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \triangle $</td><td style='text-align: center; word-wrap: break-word;'>0.33</td><td style='text-align: center; word-wrap: break-word;'>0.36</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>-0.7318</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>2.7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.8</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>5.8</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \triangle $</td><td style='text-align: center; word-wrap: break-word;'>3.1</td><td style='text-align: center; word-wrap: break-word;'>6.3</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>-1.698</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>Low Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>61</td><td style='text-align: center; word-wrap: break-word;'>62</td><td style='text-align: center; word-wrap: break-word;'>62</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \blacktriangledown $</td><td style='text-align: center; word-wrap: break-word;'>66</td><td style='text-align: center; word-wrap: break-word;'>67</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>67.76</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Critical</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Anti Windup Status</td><td style='text-align: center; word-wrap: break-word;'>Reverse Acting</td><td style='text-align: center; word-wrap: break-word;'>Engineer Request</td><td style='text-align: center; word-wrap: break-word;'>SS Move Limit</td><td style='text-align: center; word-wrap: break-word;'>Cost Rank</td><td style='text-align: center; word-wrap: break-word;'>MinMove Criterion</td><td style='text-align: center; word-wrap: break-word;'>Shadow Price</td><td style='text-align: center; word-wrap: break-word;'>Active Constraint Indicator</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.1715</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.3353</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.7518</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>3.5</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1.698</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>67.76</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr></table>

<div style="text-align: center;">Figure 8.95 MV results of steady-state optimization using the current configuration and tuning.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Ideal Steady State</td><td style='text-align: center; word-wrap: break-word;'>Ideal Constraint</td><td style='text-align: center; word-wrap: break-word;'>SS Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>SS Low Concern</td><td style='text-align: center; word-wrap: break-word;'>SS Low Rank</td><td style='text-align: center; word-wrap: break-word;'>SS High Concern</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $</td><td style='text-align: center; word-wrap: break-word;'>0.4374</td><td style='text-align: center; word-wrap: break-word;'>27</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOL WT</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>34000</td><td style='text-align: center; word-wrap: break-word;'>34000</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \nabla $</td><td style='text-align: center; word-wrap: break-word;'>-79.84</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>50000</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>79</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>73</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>79</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \nabla $</td><td style='text-align: center; word-wrap: break-word;'>-1.869</td><td style='text-align: center; word-wrap: break-word;'>87</td><td style='text-align: center; word-wrap: break-word;'>89</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.17</td><td style='text-align: center; word-wrap: break-word;'>0.25</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $</td><td style='text-align: center; word-wrap: break-word;'>0.1264</td><td style='text-align: center; word-wrap: break-word;'>0.76</td><td style='text-align: center; word-wrap: break-word;'>0.84</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0051</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>SS High Rank</td><td style='text-align: center; word-wrap: break-word;'>Critical</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Active Constraint Indicator</td><td style='text-align: center; word-wrap: break-word;'>Engineer Request</td><td style='text-align: center; word-wrap: break-word;'>Shadow Price</td><td style='text-align: center; word-wrap: break-word;'>ECEs Using Eng/Units</td><td style='text-align: center; word-wrap: break-word;'>Cost Rank</td><td style='text-align: center; word-wrap: break-word;'>Max Steady-State Step</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>10000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>

<div style="text-align: center;">Figure 8.96 CV results of steady-state optimization using the current configuration and tuning.</div>


---

<!-- PDF page 535 -->

#### 8.2.17 DMC3 Builder Task 4: Simulation – Configuring and Simulating the Dynamic Controller

We follow Section 8.1.6.1–8.1.6.5 to configure the dynamic controller. Figures 8.97a–8.97d show how to initialize the controller simulation. Figures 8.98a and 8.98b show the input entries for MVs and CVs, including operating values and tuning values. After completing the entries displayed in Figures 8.97a–8.97d, we save the simulation file as WS8.1_BaseCase.dmc3application.

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_363_617_608.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 8.97a Initialize the controller simulation.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>Combined Status</td><td style='text-align: center; word-wrap: break-word;'>Service Request</td><td style='text-align: center; word-wrap: break-word;'>Service Status</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_YA</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>84</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'>91</td><td style='text-align: center; word-wrap: break-word;'>200</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0.16</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.13</td><td style='text-align: center; word-wrap: break-word;'>0.16</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.33</td><td style='text-align: center; word-wrap: break-word;'>0.36</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>2.7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.8</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>2.7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5.8</td><td style='text-align: center; word-wrap: break-word;'>6.3</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>Low Limit</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>65</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>65</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>Combined Status</td><td style='text-align: center; word-wrap: break-word;'>Service Request</td><td style='text-align: center; word-wrap: break-word;'>Service Status</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>Prediction</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLVMER</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>27</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>34500</td><td style='text-align: center; word-wrap: break-word;'>34500</td><td style='text-align: center; word-wrap: break-word;'>35000</td><td style='text-align: center; word-wrap: break-word;'>35500</td><td style='text-align: center; word-wrap: break-word;'>35500</td><td style='text-align: center; word-wrap: break-word;'>50000</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>73</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>79</td><td style='text-align: center; word-wrap: break-word;'>95</td><td style='text-align: center; word-wrap: break-word;'>95</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P_CONC_MMA</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.17</td><td style='text-align: center; word-wrap: break-word;'>0.25</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.76</td><td style='text-align: center; word-wrap: break-word;'>0.84</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">Figure 8.97b Input entries for controller simulation – part 1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>Critical</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Setpoint</td><td style='text-align: center; word-wrap: break-word;'>Loop Status</td><td style='text-align: center; word-wrap: break-word;'>Anti Windup Status</td><td style='text-align: center; word-wrap: break-word;'>Reverse Acting</td><td style='text-align: center; word-wrap: break-word;'>Plot Low</td><td style='text-align: center; word-wrap: break-word;'>Plot High</td><td style='text-align: center; word-wrap: break-word;'>Shed Option</td><td style='text-align: center; word-wrap: break-word;'>Limit Check Tool</td><td style='text-align: center; word-wrap: break-word;'>Plot Auto Scale</td><td style='text-align: center; word-wrap: break-word;'>Calculate Step Size</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>-0.1715</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>16.4</td><td style='text-align: center; word-wrap: break-word;'>23.6</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>-0.3353</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.5</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>-0.7518</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.11</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>-1.698</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1.95</td><td style='text-align: center; word-wrap: break-word;'>6.15</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>67.76</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>61.6</td><td style='text-align: center; word-wrap: break-word;'>66.4</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>SS Low Concern</td><td style='text-align: center; word-wrap: break-word;'>SS Low Rank</td><td style='text-align: center; word-wrap: break-word;'>SS High Concern</td><td style='text-align: center; word-wrap: break-word;'>SS High Rank</td><td style='text-align: center; word-wrap: break-word;'>Control Weight</td><td style='text-align: center; word-wrap: break-word;'>Dynamic Low Concern</td><td style='text-align: center; word-wrap: break-word;'>Dynamic High Concern</td><td style='text-align: center; word-wrap: break-word;'>Dynamic Target Concern</td><td style='text-align: center; word-wrap: break-word;'>Critical</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Plot Low</td><td style='text-align: center; word-wrap: break-word;'>Plot High</td><td style='text-align: center; word-wrap: break-word;'>Plot Auto Scale</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>13.8</td><td style='text-align: center; word-wrap: break-word;'>28.2</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>33900</td><td style='text-align: center; word-wrap: break-word;'>35100</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>73.8</td><td style='text-align: center; word-wrap: break-word;'>88.2</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0051</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0.0051</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0051</td><td style='text-align: center; word-wrap: break-word;'>0.0051</td><td style='text-align: center; word-wrap: break-word;'>0.051</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.199</td><td style='text-align: center; word-wrap: break-word;'>0.811</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr></table>

<div style="text-align: center;">Figure 8.97c Input entries for controller simulation – part 2.</div>


---

<!-- PDF page 536 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>Engineer Request</td><td style='text-align: center; word-wrap: break-word;'>SS Move Limit</td><td style='text-align: center; word-wrap: break-word;'>Cast Rank</td><td style='text-align: center; word-wrap: break-word;'>MinMove Criterion</td><td style='text-align: center; word-wrap: break-word;'>Shadow Price</td><td style='text-align: center; word-wrap: break-word;'>Active Constraint Indicator</td><td style='text-align: center; word-wrap: break-word;'>Error Status</td><td style='text-align: center; word-wrap: break-word;'>Move Accumulation</td><td style='text-align: center; word-wrap: break-word;'>Move Suppression</td><td style='text-align: center; word-wrap: break-word;'>Move Suppression Increase</td><td style='text-align: center; word-wrap: break-word;'>Move Resolution</td><td style='text-align: center; word-wrap: break-word;'>Maximum Move</td><td style='text-align: center; word-wrap: break-word;'>Tram Targ</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.1715</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.6</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.3353</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.7518</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.02</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1.698</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>9999</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>67.76</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>Initialize Predictions</td><td style='text-align: center; word-wrap: break-word;'>Pred Error Filter Type</td><td style='text-align: center; word-wrap: break-word;'>Is Intermittent Signal</td><td style='text-align: center; word-wrap: break-word;'>Acc Pred Error</td><td style='text-align: center; word-wrap: break-word;'>Average Prediction Error</td><td style='text-align: center; word-wrap: break-word;'>Active Constraint Indicator</td><td style='text-align: center; word-wrap: break-word;'>Engineer Request</td><td style='text-align: center; word-wrap: break-word;'>Shadow Price</td><td style='text-align: center; word-wrap: break-word;'>ECEs Using Englints</td><td style='text-align: center; word-wrap: break-word;'>Cost Rank</td><td style='text-align: center; word-wrap: break-word;'>Max SteadyState Step</td><td style='text-align: center; word-wrap: break-word;'>SS Constraint Violation</td><td style='text-align: center; word-wrap: break-word;'>Error Status</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>POLYMER</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Full Bias</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOL_WT</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Full Bias</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>10000</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_RX</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Full Bias</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CONC_MMA</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Full Bias</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">Figure 8.97d Input entries for controller simulation – part 3.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>Service Request</td><td style='text-align: center; word-wrap: break-word;'>Service Status</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>41.76</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>41.76</td><td style='text-align: center; word-wrap: break-word;'>2.00E-06</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>86.24</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>84</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>86.24</td><td style='text-align: center; word-wrap: break-word;'>4.167E-06</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>200</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.13</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>2.151E-08</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.8</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>-5.604E-08</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>68.6</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>68.6</td><td style='text-align: center; word-wrap: break-word;'>-3.903E-06</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr></table>

<div style="text-align: center;">Figure 8.98a Input entries for controller simulation increasing polymer production to 40 kg/hr – part 1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>Critical</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Setpoint</td><td style='text-align: center; word-wrap: break-word;'>Loop Status</td><td style='text-align: center; word-wrap: break-word;'>Anti Windup Status</td><td style='text-align: center; word-wrap: break-word;'>Reverse Acting</td><td style='text-align: center; word-wrap: break-word;'>Plot Low</td><td style='text-align: center; word-wrap: break-word;'>Plot High</td><td style='text-align: center; word-wrap: break-word;'>Shed Option</td><td style='text-align: center; word-wrap: break-word;'>Limit Check Tel</td><td style='text-align: center; word-wrap: break-word;'>Plot Auto Scale</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_MMA</td><td style='text-align: center; word-wrap: break-word;'>-0.1715</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>41.76</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>16.4</td><td style='text-align: center; word-wrap: break-word;'>23.6</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FLOW_VA</td><td style='text-align: center; word-wrap: break-word;'>-0.3353</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>88.24</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.5</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INIT</td><td style='text-align: center; word-wrap: break-word;'>-0.7518</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0.11</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TRANSF</td><td style='text-align: center; word-wrap: break-word;'>-1.698</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>1.95</td><td style='text-align: center; word-wrap: break-word;'>6.15</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_JKT</td><td style='text-align: center; word-wrap: break-word;'>67.76</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>68.6</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>61.6</td><td style='text-align: center; word-wrap: break-word;'>66.4</td><td style='text-align: center; word-wrap: break-word;'>Shed Controller</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr></table>

<div style="text-align: center;">Figure 8.98b Input entries for controller simulation increasing polymer production to 40 kg/hr – part 2.</div>


Before we make the controller simulation, we save this simulation file as WS8.1_BaseCase.dmc3application. Saving the input entries for the base case is essential, as it allows us to return to these initial specifications later if necessary. We note that when running the controller simulation forward in time, DMC Builder has no provision to let the controller rewind in time to its initial specifications.

---

<!-- PDF page 537 -->

With this controller model, we can proceed to fine-tune the controller to optimize the polymer production, improve product quality, compensate for disturbances and setpoint changes, etc.

#### 8.2.18 DMC3 Builder Task 4: Simulation–Dynamic Controller Applications to Polymer Production and Setpoint Changes

To increase the polymer production, we save the base case as a new file, WS8.1-1.dmc3application. There are many ways to increase the polymer production from its current value. We illustrate an approach in Figures 8.98a and 8.98b, which show the controller input entries to raise the polymer production to 40kg/hr, while satisfying all the constraints. This involves setting the higher engineering and validity limits of initiator mass flow INIT to 1.5kg/hr, the higher engineering and validity limits of chain transfer agent mass flow TRANSF to 6kg/hr, and the lower engineering and validity limits of polymer mass flow POLYMER to 40kg/hr.

We save the converged simulation file as WS8.1-2.dmc3application.

Next, we wish to raise the polymer molecular weight to 36,000, while keeping the polymer production to 40 kg/hr, and controlling the concentration of MMA in the polymer product to 0.2. We can achieve this setpoint change by referring to the input entries of Figure 8.98a, and raising the operator and validity high limits of polymer molecular weight MOL_WT to 36,000, while keeping other input entries unchanged. Running the simulation quickly reaches the new polymer molecular weight target value of 36,000. See Figure 8.99. We save the resulting simulation file as WS8.1-3.dmc3application.

This concludes the current “long” workshop of introducing DMC3 for a copolymerization problem. We covered the DMC3 tasks of (1) master model, (2) configuration, (3) optimization, and (4) simulation. Interested readers may refer to training courses offered by Aspen Technology, Inc. for an introduction to the additional tasks of (5) calculations (performing online calculations and variable transformations), and (6) deployment (performing controller deployment).

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_948_780_1180.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.99 Input entries for controller simulation increasing the polymer molecular weight MOL_WT to 36,000 while keeping the concentration of MMA in the product CONC_MMA at 0.2.</div>


---

<!-- PDF page 538 -->

### 8.3 Model-Predictive Control of Nonlinear Polyolefin Processes

#### 8.3.1 Challenges of Developing Nonlinear Predictive Modeling for Polyolefin Process Control

In Section 1.4.2, we review the observations by Turner and his colleagues [14, 15] of the significant deficiencies in applying the conventional neural networks to MPC of polymer processes, particularly with grade changes. Specifically, we mention that: (1) Conventional neural network architectures intrinsically contain regions where the partial derivative of a dependent variable (a process variable, PV) with respect to an independent variable (a manipulative variable, MV) becomes zero, and the resulting zero model gain would lead to an infinite controller gain; and (2) conventional neural network models cannot cope with the extrapolative demands of predictive control during polymer grade transitions. These two deficiencies are only two of the ten reasons that Turner and his colleagues [14, 15] speak against applying conventional neural network models to MPC of polymer processes. In a 2020 article, Bindlish [16] has demonstrated a controller output variable that has a steady-state gain inversion (changing signs from positive to negative, or from negative to positive) in a nonlinear MPC of a DOW chemical process.

In analyzing what must be done for model-based control of polymer processes, Bausa [17] describes that the nonlinearities in a polymer process occur mainly during the grade change. A model that was identified for a special grade often does not predict the steady-state gains correctly when considering other polymer qualities such as melt index, which typically varies nonlinearly with process independent variables.

Bausa [17] says that it is a logical step to extend the linear MPC algorithms gradually with nonlinear model characteristics. Figure 8.100 illustrates two approaches to do this. The Wiener approach multiplies the linear dynamic model output with a nonlinear steady-state function or mapping to yield the output prediction; the Hammerstein approach connects the output from a nonlinear steady-state function or mapping with a linear dynamic model to produce the output prediction. Jeong et al. [18] have demonstrated a nonlinear model-predictive controller using a Wiener model for an experimental continuous MMA polymerization reactor. We note that

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1006_717_1221.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 8.100 (a) The Wiener model; (b) The Hammerstein model.</div>


---

<!-- PDF page 539 -->

in applying a Wiener model, the linear dynamic model is typically a multi-input and multi-output (MIMO) model, while the nonlinear steady-state function or mapping is typically a multi-input single-output (MISO) model. For example, the single output could be the melt index of a polyolefin product, while the multiple inputs could be the hydrogen mass flow rate, flow rate ratios of ethylene to hydrogen, and butane to hydrogen, etc.

#### 8.3.2 Nonlinear Steady-State Mapping by State-Space Bounded Derivative Network (SS-BDN)

##### 8.3.2.1 Possible Gain Inversion and Non-Monotonic Behavior of Conventional Neural Networks

We refer the reader to reference [19] and many online tutorials about conventional neural networks, and will not repeat those readily available, basic materials in this text. We briefly review the relevant features of a conventional neural network that is essential to demonstrating its deficiencies for polymer process control applications.

Figure 8.101 illustrates the foundation of a neural network, the neuron, or node (sometimes called a processing element). We represent the inputs to the j-th node as an input vector, a, with components  $ a_i $ ( $ i=1 $ to  $ n $). The node manipulates these inputs, or activities, to give the output,  $ b_j $, which can then form a part of the input to other nodes. In the figure, we see that the j-th node transfers the i-th input  $ a_i $ to the j-th output  $ b_j $ through a weight factor  $ w_{ij} $ and a transfer function  $ f(x_j) $.  $ T_j $ is the internal threshold for node j.

In polymer process control using neural network models, input components  $ a_i $ could represent the independent variables such as hydrogen mass flow rate, flow rate ratios of ethylene to hydrogen, and of butane to hydrogen, etc.; while the output  $ b_j $ could be a dependent variable, such as the polymer melt index. Depending on the type of transfer function  $ f(x_j) $ being used, we may find that the partial derivative of an output or a dependent variable  $ b_j $ with respect to an input component or an independent variable  $ a_i $ may change sign from positive to negative, or from negative to positive. According to Eqs. (8.3) and (8.4), these partial derivatives represent elements of the steady-state gain matrix. We call this sign change as a steady-state gain inversion.

Consider, for example, a popular transfer function,  $ f(x_j) = \tanh(x_j) $, the hyperbolic tangent function. We review some basic calculus for the hyperbolic tangent function here.

Figure 8.101 The processing element (neuron or node) of a neural network.



<div style="text-align: center;"><img src="imgs/img_in_image_box_469_1053_802_1264.jpg" alt="Image" width="34%" /></div>


 $$ x_{j}=\sum_{i}w_{ij}a_{i}-T_{j}\quad 鳥 \quad f(x_{j})=\begin{cases}sigmoid\\ sine\\ tanh\end{cases} $$ 

---

<!-- PDF page 540 -->

Define:

 $$ \cosh x=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}\quad\sinh x=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2} $$ 

 $$ \tanh x=\frac{\sinh x}{\cosh x}=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{\mathrm{e}^{x}+\mathrm{e}^{-x}}\quad\quad\quad\quad\mathrm{sech}x=\frac{1}{\cosh x}=\frac{2}{\mathrm{e}^{x}+\mathrm{e}^{-x}} $$ 

 $$ \operatorname{csch} x=\frac{1}{\sinh x}=\frac{2}{\mathrm{e}^{x}-\mathrm{e}^{-x}} $$ 

Let  $ u = f(x) $, we write the derivatives as follows:

 $$ \frac{\mathrm{d}}{\mathrm{d}x}(\sinh u)=\cosh u\frac{\mathrm{d}u}{\mathrm{d}x}\quad\frac{\mathrm{d}}{\mathrm{d}x}(\cosh u)=\sinh u\frac{\mathrm{d}u}{\mathrm{d}x}\quad\frac{\mathrm{d}}{\mathrm{d}x}(\tanh u)=(\operatorname{sech} u)^{2}\frac{\mathrm{d}u}{\mathrm{d}x} $$ 

Figure 8.102 illustrates the hyperbolic tangent function and its derivative. While the hyperbolic tangent function monotonically increases with increasing  $ x_j $, its derivative value changes from monotonically positive when  $ x_j $ is negative to monotonically negative when  $ x_j $ is positive. Therefore, using the hyperbolic tangent transfer function could lead to a change in the sign of the partial derivative of dependent variable  $ b_j $ with respect to independent variable  $ x_j $, resulting in a gain inversion.

What type of transfer function do we need to avoid possible gain inversion? We want to choose a transfer function whose derivative varies monotonically. Consider, for example, the analytical integral of a standard hyperbolic tangent transfer function as our new transfer function [14, 15]:

 $$ \int\tanh(ax)\mathrm{d}x=\frac{1}{a}\ln[\cosh(ax)]+c\Longrightarrow\begin{array}{c}(Nonlinear transfer function)\\ \ln(\cosh u)\end{array} $$ 

 $$ \frac{\mathrm{d}}{\mathrm{d}x}[\ln(\cosh u)]=\frac{1}{\cosh u}\sinh u\frac{\mathrm{d}u}{\mathrm{d}x}=\tanh u\frac{\mathrm{d}u}{\mathrm{d}x} $$ 

Figure 8.103 illustrates the transfer function  $ \log(\cosh u) $, Eq. (8.50) and its derivative, Eq. (8.51). While the function itself is always positive in value, its derivative

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-0.99</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>-0.95</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>-0.85</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>-0.75</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.55</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-0.25</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 8.102 (a) The hyperbolic tangent transfer function and (b) its derivative.</div>


---

<!-- PDF page 541 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>2.3</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>1.4</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>2.3</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-0.99</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>-0.95</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>-0.85</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>-0.75</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.55</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-0.25</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 8.103 The transfer function  $ \log(\cosh u) $ and it's derivative.</div>


monotonically increases with increasing independent variable  $ x_{j} $. Therefore, there is no concern for possible gain inversion.

##### 8.3.2.2 State-Space Bounded Derivative Network (SS-BDN)

As discussed in [15, 20], the SS-BDN is essentially the analytical integral of a neural network. Based on Eqs. (8.50)–(8.51), we illustrate the general model architecture of a SS-BDN based on the analytical integral of a neural network based on a hyperbolic tangent transfer function. Figure 8.104 shows the model architecture.

We wish to use this architecture to demonstrate that the partial derivative of the dependent variable y with respect to independent variables  $ x_{k} $ is always bounded (hence the name of bounded derivative network). Based on Figure 8.104, we write:

 $$ \begin{aligned}y&=w_{11}^{(6,1)}+\sum_{i}w_{i1}^{(6,2)}.w_{ii}^{(2,0)}.x_{i}\\&\quad\left(1\rightarrow6\right)\\&\quad+\sum_{j}w_{j1}^{(6,5)}\left\{w_{jj}^{(5,4)}\left[\log\left(\cosh\left(w_{j1}^{(3,1)}\right.\right.\right.\left.\left.\left.\left.\left.\left.\sum_{i}w_{ji}^{(3,2)}\left(w_{ii}^{(2,0)}x_{i}\right)\right)\right)\right]\right\}\\&\quad\left.\left.\left.\left.\sum_{j}w_{j1}^{(6,5)}\left\{w_{jj}^{(5,3)}\left[w_{j1}^{(3,1)}\right.\right.\right.\left.\left.\left.\left.\sum_{i}w_{ji}^{(3,2)}\left(w_{ii}^{(2,0)}x_{i}\right)\right)\right]\right.\right.\right.\right.\\&\quad\left.\left.\left.\left.\left.\left.\sum_{j}\left(5\rightarrow6\right)\left(3\rightarrow5\right)\left(1\rightarrow3\right)\right.\left.\left.\left.\sum_{i}w_{ji}^{(3,2)}\left(w_{ii}^{(2,0)}x_{i}\right)\right)\right.\right.\right.\right.\right.\end{aligned} $$ 

---

<!-- PDF page 542 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_147_804_662.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.104 Architecture of the state-space bounded derivative network.</div>


Applying  $ \frac{\mathrm{d}}{\mathrm{d}x}\ln[\cosh(ax)] = a\tanh(ax) $ and setting  $ i = k $, we can write:

 $$ \begin{aligned}\frac{\partial y}{\partial x_{k}}&=w_{k1}^{(6,2)}\cdot w_{kk}^{(2,0)}\\&\quad+w_{kk}^{(2,0)}\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,4)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\underbrace{\tanh\left(\boldsymbol{w}_{j1}^{(3,1)}+\sum_{i}\boldsymbol{w}_{ji}^{(3,1)}\boldsymbol{w}_{ii}^{(2,0)}\boldsymbol{x}_{i}\right)}_{(1\rightarrow3)}\\&\quad+\boldsymbol{w}_{kk}^{(2,0)}\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,4)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\\&\quad\frac{\partial y}{\partial x_{k}}&=\boldsymbol{w}_{kk}^{(2,0)}\left[\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,3)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\right.\\&\quad\left.+\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,4)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\cdot\tanh\left(\boldsymbol{w}_{ji}^{(3,1)}+\sum_{i}\boldsymbol{w}_{ji}^{(3,2)}\boldsymbol{w}_{ii}^{(2,0)}\boldsymbol{x}_{i}\right)+\boldsymbol{w}_{k1}^{(6,2)}\right]\\&=\begin{cases}\boldsymbol{w}_{kk}^{(2,0)}\left[\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,3)}\cdot\boldsymbol{w}_{jk}^{(3,2)}-\sum_{j}\left|\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,4)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\right|+\boldsymbol{w}_{k1}^{(6,2)}\right]\begin{pmatrix}(lower\ bound\\when\ tanh\ u=-1)\end{pmatrix}\ $ 8.51)\\\boldsymbol{w}_{kk}^{(2,0)}\left[\sum_{j}\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,3)}\cdot\boldsymbol{w}_{jk}^{(3,2)}+\sum_{j}\left|\boldsymbol{w}_{j1}^{(6,5)}\cdot\boldsymbol{w}_{jj}^{(5,4)}\cdot\boldsymbol{w}_{jk}^{(3,2)}\right|+\boldsymbol{w}_{k1}^{(6,2)}\right]\begin{pmatrix}\text{uppetbound}\\when\ tanh\ u=1\end{pmatrix}\ $ 8.52)\end{cases}\end{aligned} $$ 

---

<!-- PDF page 543 -->

Eqs. (8.51) and (8.52) show the key features of the SS-BDN for nonlinear steady-state mapping that ensure the partial derivative of the dependent variable with respect to independent variables remains bounded. Additionally, as demonstrated in Figure 8.103, the choice of the transfer function within the network makes the values of the partial derivative monotonically increase with increasing values of the independent variable. Both features are essential to the success of applying the Wiener model, Figure 8.100a, to polymer process control [15, 20].

#### 8.4 Workshop 8.2: Development of a Nonlinear Predictive Controller Model for a Polypropylene Process

#### 8.4.1 Objective

The objective of this workshop is to demonstrate how to use the DMC3 Builder to develop a nonlinear model-predictive controller for a polypropylene process based on the Wiener model of Figure 8.100a. This model consists of a linear state-space dynamic model for the process dynamics integrated with a nonlinear SS-BDN for polymer quality control. The goal of the controller is to control the polymer melt index and density. We also simulate the controller performing a transition from a melt index of 1 to a melt index of 10 at a constant density of 920 kg/m³.

#### 8.4.2 Starting an APC Project and Choosing Nonlinear Controllers, and Data Preprocessing

Figure 8.105 shows the selection of APC project and DMCplus, state-space and non-linear controllers. We save the project as “PP Quality Control.” From the “Import” tool ribbon on the top left, we choose “Dataset,” and select the text file, WS8.2.txt, within our working folder. We then click on the Open button. See Figures 8.106 and 8.107.

In Figure 8.107, we see the following variables: (1) CVs – MI_Lab, MI_Inst, Density_Lab, and Density_Inst; (2) MVs – H2_C2 and C4_C2; and (3) DVs: Temp and

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_947_779_1207.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.105 Selection of APC Project and DMCplus, State-Space and Nonlinear Controllers.</div>


---

<!-- PDF page 544 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_149_809_327.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.106 Import dataset, WS8.2.txt</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_392_722_738.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 8.107 Contents of imported dataset.</div>


C2_Partial_Pressure. We click on Import displayed in Figure 8.107, and see an “Interpolate Dataset” window. We click on “Start” button to interpolate any bad and missing data slices longer than 5 min in duration. We then click the “Close” button to complete the interpolation analysis. We see the message that “0 of 8 vectors (variables) have been interpolated.” We do not show the screen images of these simple steps.

Following the interpolation step, we see the vector (variable) summary and the corresponding trend plot. The software automatically shows the first three CVs (MI_Lab, MI_Int, and Density_Lab), and we choose the fourth CV (Density_Inst). See Figure 8.108. We also display the MVs (H2_C2 and C4_C2) and DVs (Temp and C2_Partial_Pressure). See Figure 8.109.

Reviewing the trend plots of Figures 8.108 and 8.109, we see no need to do data slicing, as there is no bad data slice.

Next, we click on “Manage Lists” button on the top tool ribbon and follow Figures 8.46 and 8.47 to create the MV and CV lists. See Figures 8.110 and 8.111.

---

<!-- PDF page 545 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Sample</th><th style='text-align: center;'>Peak 1 (ppm)</th><th style='text-align: center;'>Peak 2 (ppm)</th><th style='text-align: center;'>Peak 3 (ppm)</th><th style='text-align: center;'>Peak 4 (ppm)</th><th style='text-align: center;'>Peak 5 (ppm)</th><th style='text-align: center;'>Peak 6 (ppm)</th><th style='text-align: center;'>Peak 7 (ppm)</th><th style='text-align: center;'>Peak 8 (ppm)</th><th style='text-align: center;'>Peak 9 (ppm)</th><th style='text-align: center;'>Peak 10 (ppm)</th><th style='text-align: center;'>Peak 11 (ppm)</th><th style='text-align: center;'>Peak 12 (ppm)</th><th style='text-align: center;'>Peak 13 (ppm)</th><th style='text-align: center;'>Peak 14 (ppm)</th><th style='text-align: center;'>Peak 15 (ppm)</th><th style='text-align: center;'>Peak 16 (ppm)</th><th style='text-align: center;'>Peak 17 (ppm)</th><th style='text-align: center;'>Peak 18 (ppm)</th><th style='text-align: center;'>Peak 19 (ppm)</th><th style='text-align: center;'>Peak 20 (ppm)</th><th style='text-align: center;'>Peak 21 (ppm)</th><th style='text-align: center;'>Peak 22 (ppm)</th><th style='text-align: center;'>Peak 23 (ppm)</th><th style='text-align: center;'>Peak 24 (ppm)</th><th style='text-align: center;'>Peak 25 (ppm)</th><th style='text-align: center;'>Peak 26 (ppm)</th><th style='text-align: center;'>Peak 27 (ppm)</th><th style='text-align: center;'>Peak 28 (ppm)</th><th style='text-align: center;'>Peak 29 (ppm)</th><th style='text-align: center;'>Peak 30 (ppm)</th><th style='text-align: center;'>Peak 31 (ppm)</th><th style='text-align: center;'>Peak 32 (ppm)</th><th style='text-align: center;'>Peak 33 (ppm)</th><th style='text-align: center;'>Peak 34 (ppm)</th><th style='text-align: center;'>Peak 35 (ppm)</th><th style='text-align: center;'>Peak 36 (ppm)</th><th style='text-align: center;'>Peak 37 (ppm)</th><th style='text-align: center;'>Peak 38 (ppm)</th><th style='text-align: center;'>Peak 39 (ppm)</th><th style='text-align: center;'>Peak 40 (ppm)</th><th style='text-align: center;'>Peak 41 (ppm)</th><th style='text-align: center;'>Peak 42 (ppm)</th><th style='text-align: center;'>Peak 43 (ppm)</th><th style='text-align: center;'>Peak 44 (ppm)</th><th style='text-align: center;'>Peak 45 (ppm)</th><th style='text-align: center;'>Peak 46 (ppm)</th><th style='text-align: center;'>Peak 47 (ppm)</th><th style='text-align: center;'>Peak 48 (ppm)</th><th style='text-align: center;'>Peak 49 (ppm)</th><th style='text-align: center;'>Peak 50 (ppm)</th><th style='text-align: center;'>Peak 51 (ppm)</th><th style='text-align: center;'>Peak 52 (ppm)</th><th style='text-align: center;'>Peak 53 (ppm)</th><th style='text-align: center;'>Peak 54 (ppm)</th><th style='text-align: center;'>Peak 55 (ppm)</th><th style='text-align: center;'>Peak 56 (ppm)</th><th style='text-align: center;'>Peak 57 (ppm)</th><th style='text-align: center;'>Peak 58 (ppm)</th><th style='text-align: center;'>Peak 59 (ppm)</th><th style='text-align: center;'>Peak 60 (ppm)</th><th style='text-align: center;'>Peak 61 (ppm)</th><th style='text-align: center;'>Peak 62 (ppm)</th><th style='text-align: center;'>Peak 63 (ppm)</th><th style='text-align: center;'>Peak 64 (ppm)</th><th style='text-align: center;'>Peak 65 (ppm)</th><th style='text-align: center;'>Peak 66 (ppm)</th><th style='text-align: center;'>Peak 67 (ppm)</th><th style='text-align: center;'>Peak 68 (ppm)</th><th style='text-align: center;'>Peak 69 (ppm)</th><th style='text-align: center;'>Peak 70 (ppm)</th><th style='text-align: center;'>Peak 71 (ppm)</th><th style='text-align: center;'>Peak 72 (ppm)</th><th style='text-align: center;'>Peak 73 (ppm)</th><th style='text-align: center;'>Peak 74 (ppm)</th><th style='text-align: center;'>Peak 75 (ppm)</th><th style='text-align: center;'>Peak 76 (ppm)</th><th style='text-align: center;'>Peak 77 (ppm)</th><th style='text-align: center;'>Peak 78 (ppm)</th><th style='text-align: center;'>Peak 79 (ppm)</th><th style='text-align: center;'>Peak 80 (ppm)</th><th style='text-align: center;'>Peak 81 (ppm)</th><th style='text-align: center;'>Peak 82 (ppm)</th><th style='text-align: center;'>Peak 83 (ppm)</th><th style='text-align: center;'>Peak 84 (ppm)</th><th style='text-align: center;'>Peak 85 (ppm)</th><th style='text-align: center;'>Peak 86 (ppm)</th><th style='text-align: center;'>Peak 87 (ppm)</th><th style='text-align: center;'>Peak 88 (ppm)</th><th style='text-align: center;'>Peak 89 (ppm)</th><th style='text-align: center;'>Peak 90 (ppm)</th><th style='text-align: center;'>Peak 91 (ppm)</th><th style='text-align: center;'>Peak 92 (ppm)</th><th style='text-align: center;'>Peak 93 (ppm)</th><th style='text-align: center;'>Peak 94 (ppm)</th><th style='text-align: center;'>Peak 95 (ppm)</th><th style='text-align: center;'>Peak 96 (ppm)</th><th style='text-align: center;'>Peak 97 (ppm)</th><th style='text-align: center;'>Peak 98 (ppm)</th><th style='text-align: center;'>Peak 99 (ppm)</th><th style='text-align: center;'>Peak 100 (ppm)</th><th style='text-align: center;'>Peak 101 (ppm)</th><th style='text-align: center;'>Peak 102 (ppm)</th><th style='text-align: center;'>Peak 103 (ppm)</th><th style='text-align: center;'>Peak 104 (ppm)</th><th style='text-align: center;'>Peak 105 (ppm)</th><th style='text-align: center;'>Peak 106 (ppm)</th><th style='text-align: center;'>Peak 107 (ppm)</th><th style='text-align: center;'>Peak 108 (ppm)</th><th style='text-align: center;'>Peak 109 (ppm)</th><th style='text-align: center;'>Peak 110 (ppm)</th><th style='text-align: center;'>Peak 111 (ppm)</th><th style='text-align: center;'>Peak 112 (ppm)</th><th style='text-align: center;'>Peak 113 (ppm)</th><th style='text-align: center;'>Peak 114 (ppm)</th><th style='text-align: center;'>Peak 115 (ppm)</th><th style='text-align: center;'>Peak 116 (ppm)</th><th style='text-align: center;'>Peak 117 (ppm)</th><th style='text-align: center;'>Peak 118 (ppm)</th><th style='text-align: center;'>Peak 119 (ppm)</th><th style='text-align: center;'>Peak 120 (ppm)</th><th style='text-align: center;'>Peak 121 (ppm)</th><th style='text-align: center;'>Peak 122 (ppm)</th><th style='text-align: center;'>Peak 123 (ppm)</th><th style='text-align: center;'>Peak 124 (ppm)</th><th style='text-align: center;'>Peak 125 (ppm)</th><th style='text-align: center;'>Peak 126 (ppm)</th><th style='text-align: center;'>Peak 127 (ppm)</th><th style='text-align: center;'>Peak 128 (ppm)</th><th style='text-align: center;'>Peak 129 (ppm)</th><th style='text-align: center;'>Peak 130 (ppm)</th><th style='text-align: center;'>Peak 131 (ppm)</th><th style='text-align: center;'>Peak 132 (ppm)</th><th style='text-align: center;'>Peak 133 (ppm)</th><th style='text-align: center;'>Peak 134 (ppm)</th><th style='text-align: center;'>Peak 135 (ppm)</th><th style='text-align: center;'>Peak 136 (ppm)</th><th style='text-align: center;'>Peak 137 (ppm)</th><th style='text-align: center;'>Peak 138 (ppm)</th><th style='text-align: center;'>Peak 139 (ppm)</th><th style='text-align: center;'>Peak 140 (ppm)</th><th style='text-align: center;'>Peak 141 (ppm)</th><th style='text-align: center;'>Peak 142 (ppm)</th><th style='text-align: center;'>Peak 143 (ppm)</th><th style='text-align: center;'>Peak 144 (ppm)</th><th style='text-align: center;'>Peak 145 (ppm)</th><th style='text-align: center;'>Peak 146 (ppm)</th><th style='text-align: center;'>Peak 147 (ppm)</th><th style='text-align: center;'>Peak 148 (ppm)</th><th style='text-align: center;'>Peak 149 (ppm)</th><th style='text-align: center;'>Peak 150 (ppm)</th><th style='text-align: center;'>Peak 151 (ppm)</th><th style='text-align: center;'>Peak 152 (ppm)</th><th style='text-align: center;'>Peak 153 (ppm)</th><th style='text-align: center;'>Peak 154 (ppm)</th><th style='text-align: center;'>Peak 155 (ppm)</th><th style='text-align: center;'>Peak 156 (ppm)</th><th style='text-align: center;'>Peak 157 (ppm)</th><th style='text-align: center;'>Peak 158 (ppm)</th><th style='text-align: center;'>Peak 159 (ppm)</th><th style='text-align: center;'>Peak 160 (ppm)</th><th style='text-align: center;'>Peak 161 (ppm)</th><th style='text-align: center;'>Peak 162 (ppm)</th><th style='text-align: center;'>Peak 163 (ppm)</th><th style='text-align: center;'>Peak 164 (ppm)</th><th style='text-align: center;'>Peak 165 (ppm)</th><th style='text-align: center;'>Peak 166 (ppm)</th><th style='text-align: center;'>Peak 167 (ppm)</th><th style='text-align: center;'>Peak 168 (ppm)</th><th style='text-align: center;'>Peak 169 (ppm)</th><th style='text-align: center;'>Peak 170 (ppm)</th><th style='text-align: center;'>Peak 171 (ppm)</th><th style='text-align: center;'>Peak 172 (ppm)</th><th style='text-align: center;'>Peak 173 (ppm)</th><th style='text-align: center;'>Peak 174 (ppm)</th><th style='text-align: center;'>Peak 175 (ppm)</th><th style='text-align: center;'>Peak 176 (ppm)</th><th style='text-align: center;'>Peak 177 (ppm)</th><th style='text-align: center;'>Peak 178 (ppm)</th><th style='text-align: center;'>Peak 179 (ppm)</th><th style='text-align: center;'>Peak 180 (ppm)</th><th style='text-align: center;'>Peak 181 (ppm)</th><th style='text-align: center;'>Peak 182 (ppm)</th><th style='text-align: center;'>Peak 183 (ppm)</th><th style='text-align: center;'>Peak 184 (ppm)</th><th style='text-align: center;'>Peak 185 (ppm)</th><th style='text-align: center;'>Peak 186 (ppm)</th><th style='text-align: center;'>Peak 187 (ppm)</th><th style='text-align: center;'>Peak 188 (ppm)</th><th style='text-align: center;'>Peak 189 (ppm)</th><th style='text-align: center;'>Peak 190 (ppm)</th><th style='text-align: center;'>Peak 191 (ppm)</th><th style='text-align: center;'>Peak 192 (ppm)</th><th style='text-align: center;'>Peak 193 (ppm)</th><th style='text-align: center;'>Peak 194 (ppm)</th><th style='text-align: center;'>Peak 195 (ppm)</th><th style='text-align: center;'>Peak 196 (ppm)</th><th style='text-align: center;'>Peak 197 (ppm)</th><th style='text-align: center;'>Peak 198 (ppm)</th><th style='text-align: center;'>Peak 199 (ppm)</th><th style='text-align: center;'>Peak 200 (ppm)</th><th style='text-align: center;'>Peak 201 (ppm)</th><th style='text-align: center;'>Peak 202 (ppm)</th><th style='text-align: center;'>Peak 203 (ppm)</th><th style='text-align: center;'>Peak 204 (ppm)</th><th style='text-align: center;'>Peak 205 (ppm)</th><th style='text-align: center;'>Peak 206 (ppm)</th><th style='text-align: center;'>Peak 207 (ppm)</th><th style='text-align: center;'>Peak 208 (ppm)</th><th style='text-align: center;'>Peak 209 (ppm)</th><th style='text-align: center;'>Peak 210 (ppm)</th><th style='text-align: center;'>Peak 211 (ppm)</th><th style='text-align: center;'>Peak 212 (ppm)</th><th style='text-align: center;'>Peak 213 (ppm)</th><th style='text-align: center;'>Peak 214 (ppm)</th><th style='text-align: center;'>Peak 215 (ppm)</th><th style='text-align: center;'>Peak 216 (ppm)</th><th style='text-align: center;'>Peak 217 (ppm)</th><th style='text-align: center;'>Peak 218 (ppm)</th><th style='text-align: center;'>Peak 219 (ppm)</th><th style='text-align: center;'>Peak 220 (ppm)</th><th style='text-align: center;'>Peak 221 (ppm)</th><th style='text-align: center;'>Peak 222 (ppm)</th><th style='text-align: center;'>Peak 223 (ppm)</th><th style='text-align: center;'>Peak 224 (ppm)</th><th style='text-align: center;'>Peak 225 (ppm)</th><th style='text-align: center;'>Peak 226 (ppm)</th><th style='text-align: center;'>Peak 227 (ppm)</th><th style='text-align: center;'>Peak 228 (ppm)</th><th style='text-align: center;'>Peak 229 (ppm)</th><th style='text-align: center;'>Peak 230 (ppm)</th><th style='text-align: center;'>Peak 231 (ppm)</th><th style='text-align: center;'>Peak 232 (ppm)</th><th style='text-align: center;'>Peak 233 (ppm)</th><th style='text-align: center;'>Peak 234 (ppm)</th><th style='text-align: center;'>Peak 235 (ppm)</th><th style='text-align: center;'>Peak 236 (ppm)</th><th style='text-align: center;'>Peak 237 (ppm)</th><th style='text-align: center;'>Peak 238 (ppm)</th><th style='text-align: center;'>Peak 239 (ppm)</th><th style='text-align: center;'>Peak 240 (ppm)</th><th style='text-align: center;'>Peak 241 (ppm)</th><th style='text-align: center;'>Peak 242 (ppm)</th><th style='text-align: center;'>Peak 243 (ppm)</th><th style='text-align: center;'>Peak 244 (ppm)</th><th style='text-align: center;'>Peak 245 (ppm)</th><th style='text-align: center;'>Peak 246 (ppm)</th><th style='text-align: center;'>Peak 247 (ppm)</th><th style='text-align: center;'>Peak 248 (ppm)</th><th style='text-align: center;'>Peak 249 (ppm)</th><th style='text-align: center;'>Peak 250 (ppm)</th><th style='text-align: center;'>Peak 251 (ppm)</th><th style='text-align: center;'>Peak 252 (ppm)</th><th style='text-align: center;'>Peak 253 (ppm)</th><th style='text-align: center;'>Peak 254 (ppm)</th><th style='text-align: center;'>Peak 255 (ppm)</th><th style='text-align: center;'>Peak 256 (ppm)</th><th style='text-align: center;'>Peak 257 (ppm)</th><th style='text-align: center;'>Peak 258 (ppm)</th><th style='text-align: center;'>Peak 259 (ppm)</th><th style='text-align: center;'>Peak 260 (ppm)</th><th style='text-align: center;'>Peak 261 (ppm)</th><th style='text-align: center;'>Peak 262 (ppm)</th><th style='text-align: center;'>Peak 263 (ppm)</th><th style='text-align: center;'>Peak 264 (ppm)</th><th style='text-align: center;'>Peak 265 (ppm)</th><th style='text-align: center;'>Peak 266 (ppm)</th><th style='text-align: center;'>Peak 267 (ppm)</th><th style='text-align: center;'>Peak 268 (ppm)</th><th style='text-align: center;'>Peak 269 (ppm)</th><th style='text-align: center;'>Peak 270 (ppm)</th><th style='text-align: center;'>Peak 271 (ppm)</th><th style='text-align: center;'>Peak 272 (ppm)</th><th style='text-align: center;'>Peak 273 (ppm)</th><th style='text-align: center;'>Peak 274 (ppm)</th><th style='text-align: center;'>Peak 275 (ppm)</th><th style='text-align: center;'>Peak 276 (ppm)</th><th style='text-align: center;'>Peak 277 (ppm)</th><th style='text-align: center;'>Peak 278 (ppm)</th><th style='text-align: center;'>Peak 279 (ppm)</th><th style='text-align: center;'>Peak 280 (ppm)</th><th style='text-align: center;'>Peak 281 (ppm)</th><th style='text-align: center;'>Peak 282 (ppm)</th><th style='text-align: center;'>Peak 283 (ppm)</th><th style='text-align: center;'>Peak 284 (ppm)</th><th style='text-align: center;'>Peak 285 (ppm)</th><th style='text-align: center;'>Peak 286 (ppm)</th><th style='text-align: center;'>Peak 287 (ppm)</th><th style='text-align: center;'>Peak 288 (ppm)</th><th style='text-align: center;'>Peak 289 (ppm)</th><th style='text-align: center;'>Peak 290 (ppm)</th><th style='text-align: center;'>Peak 291 (ppm)</th><th style='text-align: center;'>Peak 292 (ppm)</th><th style='text-align: center;'>Peak 293 (ppm)</th><th style='text-align: center;'>Peak 294 (ppm)</th><th style='text-align: center;'>Peak 295 (ppm)</th><th style='text-align: center;'>Peak 296 (ppm)</th><th style='text-align: center;'>Peak 297 (ppm)</th><th style='text-align: center;'>Peak 298 (ppm)</th><th style='text-align: center;'>Peak 299 (ppm)</th><th style='text-align: center;'>Peak 300 (ppm)</th><th style='text-align: center;'>Peak 301 (ppm)</th><th style='text-align: center;'>Peak 302 (ppm)</th><th style='text-align: center;'>Peak 303 (ppm)</th><th style='text-align: center;'>Peak 304 (ppm)</th><th style='text-align: center;'>Peak 305 (ppm)</th><th style='text-align: center;'>Peak 306 (ppm)</th><th style='text-align: center;'>Peak 307 (ppm)</th><th style='text-align: center;'>Peak 308 (ppm)</th><th style='text-align: center;'>Peak 309 (ppm)</th><th style='text-align: center;'>Peak 310 (ppm)</th><th style='text-align: center;'>Peak 311 (ppm)</th><th style='text-align: center;'>Peak 312 (ppm)</th><th style='text-align: center;'>Peak 313 (ppm)</th><th style='text-align: center;'>Peak 314 (ppm)</th><th style='text-align: center;'>Peak 315 (ppm)</th><th style='text-align: center;'>Peak 316 (ppm)</th><th style='text-align: center;'>Peak 317 (ppm)</th><th style='text-align: center;'>Peak 318 (ppm)</th><th style='text-align: center;'>Peak 319 (ppm)</th><th style='text-align: center;'>Peak 320 (ppm)</th><th style='text-align: center;'>Peak 321 (ppm)</th><th style='text-align: center;'>Peak 322 (ppm)</th><th style='text-align: center;'>Peak 323 (ppm)</th><th style='text-align: center;'>Peak 324 (ppm)</th><th style='text-align: center;'>Peak 325 (ppm)</th><th style='text-align: center;'>Peak 326 (ppm)</th><th style='text-align: center;'>Peak 327 (ppm)</th><th style='text-align: center;'>Peak 328 (ppm)</th><th style='text-align: center;'>Peak 329 (ppm)</th><th style='text-align: center;'>Peak 330 (ppm)</th><th style='text-align: center;'>Peak 331 (ppm)</th><th style='text-align: center;'>Peak 332 (ppm)</th><th style='text-align: center;'>Peak 333 (ppm)</th><th style='text-align: center;'>Peak 334 (ppm)</th><th style='text-align: center;'>Peak 335 (ppm)</th><th style='text-align: center;'>Peak 336 (ppm)</th><th style='text-align: center;'>Peak 337 (ppm)</th><th style='text-align: center;'>Peak 338 (ppm)</th><th style='text-align: center;'>Peak 339 (ppm)</th><th style='text-align: center;'>Peak 340 (ppm)</th><th style='text-align: center;'>Peak 341 (ppm)</th><th style='text-align: center;'>Peak 342 (ppm)</th><th style='text-align: center;'>Peak 343 (ppm)</th><th style='text-align: center;'>Peak 344 (ppm)</th><th style='text-align: center;'>Peak 345 (ppm)</th><th style='text-align: center;'>Peak 346 (ppm)</th><th style='text-align: center;'>Peak 347 (ppm)</th><th style='text-align: center;'>Peak 348 (ppm)</th><th style='text-align: center;'>Peak 349 (ppm)</th><th style='text-align: center;'>Peak 350 (ppm)</th><th style='text-align: center;'>Peak 351 (ppm)</th><th style='text-align: center;'>Peak 352 (ppm)</th><th style='text-align: center;'>Peak 353 (ppm)</th><th style='text-align: center;'>Peak 354 (ppm)</th><th style='text-align: center;'>Peak 355 (ppm)</th><th style='text-align: center;'>Peak 356 (ppm)</th><th style='text-align: center;'>Peak 357 (ppm)</th><th style='text-align: center;'>Peak 358 (ppm)</th><th style='text-align: center;'>Peak 359 (ppm)</th><th style='text-align: center;'>Peak 360 (ppm)</th><th style='text-align: center;'>Peak 361 (ppm)</th><th style='text-align: center;'>Peak 362 (ppm)</th><th style='text-align: center;'>Peak 363 (ppm)</th><th style='text-align: center;'>Peak 364 (ppm)</th><th style='text-align: center;'>Peak 365 (ppm)</th><th style='text-align: center;'>Peak 366 (ppm)</th><th style='text-align: center;'>Peak 367 (ppm)</th><th style='text-align: center;'>Peak 368 (ppm)</th><th style='text-align: center;'>Peak 369 (ppm)</th><th style='text-align: center;'>Peak 370 (ppm)</th><th style='text-align: center;'>Peak 371 (ppm)</th><th style='text-align: center;'>Peak 372 (ppm)</th><th style='text-align: center;'>Peak 373 (ppm)</th><th style='text-align: center;'>Peak 374 (ppm)</th><th style='text-align: center;'>Peak 375 (ppm)</th><th style='text-align: center;'>Peak 376 (ppm)</th><th style='text-align: center;'>Peak 377 (ppm)</th><th style='text-align: center;'>Peak 378 (ppm)</th><th style='text-align: center;'>Peak 379 (ppm)</th><th style='text-align: center;'>Peak 380 (ppm)</th><th style='text-align: center;'>Peak 381 (ppm)</th><th style='text-align: center;'>Peak 382 (ppm)</th><th style='text-align: center;'>Peak 383 (ppm)</th><th style='text-align: center;'>Peak 384 (ppm)</th><th style='text-align: center;'>Peak 385 (ppm)</th><th style='text-align: center;'>Peak 386 (ppm)</th><th style='text-align: center;'>Peak 387 (ppm)</th><th style='text-align: center;'>Peak 388 (ppm)</th><th style='text-align: center;'>Peak 389 (ppm)</th><th style='text-align: center;'>Peak 390 (ppm)</th><th style='text-align: center;'>Peak 391 (ppm)</th><th style='text-align: center;'>Peak 392 (ppm)</th><th style='text-align: center;'>Peak 393 (ppm)</th><th style='text-align: center;'>Peak 394 (ppm)</th><th style='text-align: center;'>Peak 395 (ppm)</th><th style='text-align: center;'>Peak 396 (ppm)</th><th style='text-align: center;'>Peak 397 (ppm)</th><th style='text-align: center;'>Peak 398 (ppm)</th><th style='text-align: center;'>Peak 399 (ppm)</th><th style='text-align: center;'>Peak 400 (ppm)</th><th style='text-align: center;'>Peak 401 (ppm)</th><th style='text-align: center;'>Peak 402 (ppm)</th><th style='text-align: center;'>Peak 403 (ppm)</th><th style='text-align: center;'>Peak 404 (ppm)</th><th style='text-align: center;'>Peak 405 (ppm)</th><th style='text-align: center;'>Peak 406 (ppm)</th><th style='text-align: center;'>Peak 407 (ppm)</th><th style='text-align: center;'>Peak 408 (ppm)</th><th style='text-align: center;'>Peak 409 (ppm)</th><th style='text-align: center;'>Peak 410 (ppm)</th><th style='text-align: center;'>Peak 411 (ppm)</th><th style='text-align: center;'>Peak 412 (ppm)</th><th style='text-align: center;'>Peak 413 (ppm)</th><th style='text-align: center;'>Peak 414 (ppm)</th><th style='text-align: center;'>Peak 415 (ppm)</th><th style='text-align: center;'>Peak 416 (ppm)</th><th style='text-align: center;'>Peak 417 (ppm)</th><th style='text-align: center;'>Peak 418 (ppm)</th><th style='text-align: center;'>Peak 419 (ppm)</th><th style='text-align: center;'>Peak 420 (ppm)</th><th style='text-align: center;'>Peak 421 (ppm)</th><th style='text-align: center;'>Peak 422 (ppm)</th><th style='text-align: center;'>Peak 423 (ppm)</th><th style='text-align: center;'>Peak 424 (ppm)</th><th style='text-align: center;'>Peak 425 (ppm)</th><th style='text-align: center;'>Peak 426 (ppm)</th><th style='text-align: center;'>Peak 427 (ppm)</th><th style='text-align: center;'>Peak 428 (ppm)</th><th style='text-align: center;'>Peak 429 (ppm)</th><th style='text-align: center;'>Peak 430 (ppm)</th><th style='text-align: center;'>Peak 431 (ppm)</th><th style='text-align: center;'>Peak 432 (ppm)</th><th style='text-align: center;'>Peak 433 (ppm)</th><th style='text-align: center;'>Peak 434 (ppm)</th><th style='text-align: center;'>Peak 435 (ppm)</th><th style='text-align: center;'>Peak 436 (ppm)</th><th style='text-align: center;'>Peak 437 (ppm)</th><th style='text-align: center;'>Peak 438 (ppm)</th><th style='text-align: center;'>Peak 439 (ppm)</th><th style='text-align: center;'>Peak 440 (ppm)</th><th style='text-align: center;'>Peak 441 (ppm)</th><th style='text-align: center;'>Peak 442 (ppm)</th><th style='text-align: center;'>Peak 443 (ppm)</th><th style='text-align: center;'>Peak 444 (ppm)</th><th style='text-align: center;'>Peak 445 (ppm)</th><th style='text-align: center;'>Peak 446 (ppm)</th><th style='text-align: center;'>Peak 447 (ppm)</th><th style='text-align: center;'>Peak 448 (ppm)</th><th style='text-align: center;'>Peak 449 (ppm)</th><th style='text-align: center;'>Peak 450 (ppm)</th><th style='text-align: center;'>Peak 451 (ppm)</th><th style='text-align: center;'>Peak 452 (ppm)</th><th style='text-align: center;'>Peak 453 (ppm)</th><th style='text-align: center;'>Peak 454 (ppm)</th><th style='text-align: center;'>Peak 455 (ppm)</th><th style='text-align: center;'>Peak 456 (ppm)</th><th style='text-align: center;'>Peak 457 (ppm)</th><th style='text-align: center;'>Peak 458 (ppm)</th><th style='text-align: center;'>Peak 459 (ppm)</th><th style='text-align: center;'>Peak 460 (ppm)</th><th style='text-align: center;'>Peak 461 (ppm)</th><th style='text-align: center;'>Peak 462 (ppm)</th><th style='text-align: center;'>Peak 463 (ppm)</th><th style='text-align: center;'>Peak 464 (ppm)</th><th style='text-align: center;'>Peak 465 (ppm)</th><th style='text-align: center;'>Peak 466 (ppm)</th><th style='text-align: center;'>Peak 467 (ppm)</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.108 A display of the CVs.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>All Workers</th><th style='text-align: center;'>Q_1</th><th style='text-align: center;'>Q_2</th><th style='text-align: center;'>Q_3</th><th style='text-align: center;'>Q_4</th><th style='text-align: center;'>Q_5</th><th style='text-align: center;'>Q_6</th><th style='text-align: center;'>Q_7</th><th style='text-align: center;'>Q_8</th><th style='text-align: center;'>Q_9</th><th style='text-align: center;'>Q_10</th><th style='text-align: center;'>Q_11</th><th style='text-align: center;'>Q_12</th><th style='text-align: center;'>Q_13</th><th style='text-align: center;'>Q_14</th><th style='text-align: center;'>Q_15</th><th style='text-align: center;'>Q_16</th><th style='text-align: center;'>Q_17</th><th style='text-align: center;'>Q_18</th><th style='text-align: center;'>Q_19</th><th style='text-align: center;'>Q_20</th><th style='text-align: center;'>Q_21</th><th style='text-align: center;'>Q_22</th><th style='text-align: center;'>Q_23</th><th style='text-align: center;'>Q_24</th><th style='text-align: center;'>Q_25</th><th style='text-align: center;'>Q_26</th><th style='text-align: center;'>Q_27</th><th style='text-align: center;'>Q_28</th><th style='text-align: center;'>Q_29</th><th style='text-align: center;'>Q_30</th><th style='text-align: center;'>Q_31</th><th style='text-align: center;'>Q_32</th><th style='text-align: center;'>Q_33</th><th style='text-align: center;'>Q_34</th><th style='text-align: center;'>Q_35</th><th style='text-align: center;'>Q_36</th><th style='text-align: center;'>Q_37</th><th style='text-align: center;'>Q_38</th><th style='text-align: center;'>Q_39</th><th style='text-align: center;'>Q_40</th><th style='text-align: center;'>Q_41</th><th style='text-align: center;'>Q_42</th><th style='text-align: center;'>Q_43</th><th style='text-align: center;'>Q_44</th><th style='text-align: center;'>Q_45</th><th style='text-align: center;'>Q_46</th><th style='text-align: center;'>Q_47</th><th style='text-align: center;'>Q_48</th><th style='text-align: center;'>Q_49</th><th style='text-align: center;'>Q_50</th><th style='text-align: center;'>Q_51</th><th style='text-align: center;'>Q_52</th><th style='text-align: center;'>Q_53</th><th style='text-align: center;'>Q_54</th><th style='text-align: center;'>Q_55</th><th style='text-align: center;'>Q_56</th><th style='text-align: center;'>Q_57</th><th style='text-align: center;'>Q_58</th><th style='text-align: center;'>Q_59</th><th style='text-align: center;'>Q_60</th><th style='text-align: center;'>Q_61</th><th style='text-align: center;'>Q_62</th><th style='text-align: center;'>Q_63</th><th style='text-align: center;'>Q_64</th><th style='text-align: center;'>Q_65</th><th style='text-align: center;'>Q_66</th><th style='text-align: center;'>Q_67</th><th style='text-align: center;'>Q_68</th><th style='text-align: center;'>Q_69</th><th style='text-align: center;'>Q_70</th><th style='text-align: center;'>Q_71</th><th style='text-align: center;'>Q_72</th><th style='text-align: center;'>Q_73</th><th style='text-align: center;'>Q_74</th><th style='text-align: center;'>Q_75</th><th style='text-align: center;'>Q_76</th><th style='text-align: center;'>Q_77</th><th style='text-align: center;'>Q_78</th><th style='text-align: center;'>Q_79</th><th style='text-align: center;'>Q_80</th><th style='text-align: center;'>Q_81</th><th style='text-align: center;'>Q_82</th><th style='text-align: center;'>Q_83</th><th style='text-align: center;'>Q_84</th><th style='text-align: center;'>Q_85</th><th style='text-align: center;'>Q_86</th><th style='text-align: center;'>Q_87</th><th style='text-align: center;'>Q_88</th><th style='text-align: center;'>Q_89</th><th style='text-align: center;'>Q_90</th><th style='text-align: center;'>Q_91</th><th style='text-align: center;'>Q_92</th><th style='text-align: center;'>Q_93</th><th style='text-align: center;'>Q_94</th><th style='text-align: center;'>Q_95</th><th style='text-align: center;'>Q_96</th><th style='text-align: center;'>Q_97</th><th style='text-align: center;'>Q_98</th><th style='text-align: center;'>Q_99</th><th style='text-align: center;'>Q_100</th><th style='text-align: center;'>Q_101</th><th style='text-align: center;'>Q_102</th><th style='text-align: center;'>Q_103</th><th style='text-align: center;'>Q_104</th><th style='text-align: center;'>Q_105</th><th style='text-align: center;'>Q_106</th><th style='text-align: center;'>Q_107</th><th style='text-align: center;'>Q_108</th><th style='text-align: center;'>Q_109</th><th style='text-align: center;'>Q_110</th><th style='text-align: center;'>Q_111</th><th style='text-align: center;'>Q_112</th><th style='text-align: center;'>Q_113</th><th style='text-align: center;'>Q_114</th><th style='text-align: center;'>Q_115</th><th style='text-align: center;'>Q_116</th><th style='text-align: center;'>Q_117</th><th style='text-align: center;'>Q_118</th><th style='text-align: center;'>Q_119</th><th style='text-align: center;'>Q_120</th><th style='text-align: center;'>Q_121</th><th style='text-align: center;'>Q_122</th><th style='text-align: center;'>Q_123</th><th style='text-align: center;'>Q_124</th><th style='text-align: center;'>Q_125</th><th style='text-align: center;'>Q_126</th><th style='text-align: center;'>Q_127</th><th style='text-align: center;'>Q_128</th><th style='text-align: center;'>Q_129</th><th style='text-align: center;'>Q_130</th><th style='text-align: center;'>Q_131</th><th style='text-align: center;'>Q_132</th><th style='text-align: center;'>Q_133</th><th style='text-align: center;'>Q_134</th><th style='text-align: center;'>Q_135</th><th style='text-align: center;'>Q_136</th><th style='text-align: center;'>Q_137</th><th style='text-align: center;'>Q_138</th><th style='text-align: center;'>Q_139</th><th style='text-align: center;'>Q_140</th><th style='text-align: center;'>Q_141</th><th style='text-align: center;'>Q_142</th><th style='text-align: center;'>Q_143</th><th style='text-align: center;'>Q_144</th><th style='text-align: center;'>Q_145</th><th style='text-align: center;'>Q_146</th><th style='text-align: center;'>Q_147</th><th style='text-align: center;'>Q_148</th><th style='text-align: center;'>Q_149</th><th style='text-align: center;'>Q_150</th><th style='text-align: center;'>Q_151</th><th style='text-align: center;'>Q_152</th><th style='text-align: center;'>Q_153</th><th style='text-align: center;'>Q_154</th><th style='text-align: center;'>Q_155</th><th style='text-align: center;'>Q_156</th><th style='text-align: center;'>Q_157</th><th style='text-align: center;'>Q_158</th><th style='text-align: center;'>Q_159</th><th style='text-align: center;'>Q_160</th><th style='text-align: center;'>Q_161</th><th style='text-align: center;'>Q_162</th><th style='text-align: center;'>Q_163</th><th style='text-align: center;'>Q_164</th><th style='text-align: center;'>Q_165</th><th style='text-align: center;'>Q_166</th><th style='text-align: center;'>Q_167</th><th style='text-align: center;'>Q_168</th><th style='text-align: center;'>Q_169</th><th style='text-align: center;'>Q_170</th><th style='text-align: center;'>Q_171</th><th style='text-align: center;'>Q_172</th><th style='text-align: center;'>Q_173</th><th style='text-align: center;'>Q_174</th><th style='text-align: center;'>Q_175</th><th style='text-align: center;'>Q_176</th><th style='text-align: center;'>Q_177</th><th style='text-align: center;'>Q_178</th><th style='text-align: center;'>Q_179</th><th style='text-align: center;'>Q_180</th><th style='text-align: center;'>Q_181</th><th style='text-align: center;'>Q_182</th><th style='text-align: center;'>Q_183</th><th style='text-align: center;'>Q_184</th><th style='text-align: center;'>Q_185</th><th style='text-align: center;'>Q_186</th><th style='text-align: center;'>Q_187</th><th style='text-align: center;'>Q_188</th><th style='text-align: center;'>Q_189</th><th style='text-align: center;'>Q_190</th><th style='text-align: center;'>Q_191</th><th style='text-align: center;'>Q_192</th><th style='text-align: center;'>Q_193</th><th style='text-align: center;'>Q_194</th><th style='text-align: center;'>Q_195</th><th style='text-align: center;'>Q_196</th><th style='text-align: center;'>Q_197</th><th style='text-align: center;'>Q_198</th><th style='text-align: center;'>Q_199</th><th style='text-align: center;'>Q_200</th><th style='text-align: center;'>Q_201</th><th style='text-align: center;'>Q_202</th><th style='text-align: center;'>Q_203</th><th style='text-align: center;'>Q_204</th><th style='text-align: center;'>Q_205</th><th style='text-align: center;'>Q_206</th><th style='text-align: center;'>Q_207</th><th style='text-align: center;'>Q_208</th><th style='text-align: center;'>Q_209</th><th style='text-align: center;'>Q_210</th><th style='text-align: center;'>Q_211</th><th style='text-align: center;'>Q_212</th><th style='text-align: center;'>Q_213</th><th style='text-align: center;'>Q_214</th><th style='text-align: center;'>Q_215</th><th style='text-align: center;'>Q_216</th><th style='text-align: center;'>Q_217</th><th style='text-align: center;'>Q_218</th><th style='text-align: center;'>Q_219</th><th style='text-align: center;'>Q_220</th><th style='text-align: center;'>Q_221</th><th style='text-align: center;'>Q_222</th><th style='text-align: center;'>Q_223</th><th style='text-align: center;'>Q_224</th><th style='text-align: center;'>Q_225</th><th style='text-align: center;'>Q_226</th><th style='text-align: center;'>Q_227</th><th style='text-align: center;'>Q_228</th><th style='text-align: center;'>Q_229</th><th style='text-align: center;'>Q_230</th><th style='text-align: center;'>Q_231</th><th style='text-align: center;'>Q_232</th><th style='text-align: center;'>Q_233</th><th style='text-align: center;'>Q_234</th><th style='text-align: center;'>Q_235</th><th style='text-align: center;'>Q_236</th><th style='text-align: center;'>Q_237</th><th style='text-align: center;'>Q_238</th><th style='text-align: center;'>Q_239</th><th style='text-align: center;'>Q_240</th><th style='text-align: center;'>Q_241</th><th style='text-align: center;'>Q_242</th><th style='text-align: center;'>Q_243</th><th style='text-align: center;'>Q_244</th><th style='text-align: center;'>Q_245</th><th style='text-align: center;'>Q_246</th><th style='text-align: center;'>Q_247</th><th style='text-align: center;'>Q_248</th><th style='text-align: center;'>Q_249</th><th style='text-align: center;'>Q_250</th><th style='text-align: center;'>Q_251</th><th style='text-align: center;'>Q_252</th><th style='text-align: center;'>Q_253</th><th style='text-align: center;'>Q_254</th><th style='text-align: center;'>Q_255</th><th style='text-align: center;'>Q_256</th><th style='text-align: center;'>Q_257</th><th style='text-align: center;'>Q_258</th><th style='text-align: center;'>Q_259</th><th style='text-align: center;'>Q_260</th><th style='text-align: center;'>Q_261</th><th style='text-align: center;'>Q_262</th><th style='text-align: center;'>Q_263</th><th style='text-align: center;'>Q_264</th><th style='text-align: center;'>Q_265</th><th style='text-align: center;'>Q_266</th><th style='text-align: center;'>Q_267</th><th style='text-align: center;'>Q_268</th><th style='text-align: center;'>Q_269</th><th style='text-align: center;'>Q_270</th><th style='text-align: center;'>Q_271</th><th style='text-align: center;'>Q_272</th><th style='text-align: center;'>Q_273</th><th style='text-align: center;'>Q_274</th><th style='text-align: center;'>Q_275</th><th style='text-align: center;'>Q_276</th><th style='text-align: center;'>Q_277</th><th style='text-align: center;'>Q_278</th><th style='text-align: center;'>Q_279</th><th style='text-align: center;'>Q_280</th><th style='text-align: center;'>Q_281</th><th style='text-align: center;'>Q_282</th><th style='text-align: center;'>Q_283</th><th style='text-align: center;'>Q_284</th><th style='text-align: center;'>Q_285</th><th style='text-align: center;'>Q_286</th><th style='text-align: center;'>Q_287</th><th style='text-align: center;'>Q_288</th><th style='text-align: center;'>Q_289</th><th style='text-align: center;'>Q_290</th><th style='text-align: center;'>Q_291</th><th style='text-align: center;'>Q_292</th><th style='text-align: center;'>Q_293</th><th style='text-align: center;'>Q_294</th><th style='text-align: center;'>Q_295</th><th style='text-align: center;'>Q_296</th><th style='text-align: center;'>Q_297</th><th style='text-align: center;'>Q_298</th><th style='text-align: center;'>Q_299</th><th style='text-align: center;'>Q_300</th><th style='text-align: center;'>Q_301</th><th style='text-align: center;'>Q_302</th><th style='text-align: center;'>Q_303</th><th style='text-align: center;'>Q_304</th><th style='text-align: center;'>Q_305</th><th style='text-align: center;'>Q_306</th><th style='text-align: center;'>Q_307</th><th style='text-align: center;'>Q_308</th><th style='text-align: center;'>Q_309</th><th style='text-align: center;'>Q_310</th><th style='text-align: center;'>Q_311</th><th style='text-align: center;'>Q_312</th><th style='text-align: center;'>Q_313</th><th style='text-align: center;'>Q_314</th><th style='text-align: center;'>Q_315</th><th style='text-align: center;'>Q_316</th><th style='text-align: center;'>Q_317</th><th style='text-align: center;'>Q_318</th><th style='text-align: center;'>Q_319</th><th style='text-align: center;'>Q_320</th><th style='text-align: center;'>Q_321</th><th style='text-align: center;'>Q_322</th><th style='text-align: center;'>Q_323</th><th style='text-align: center;'>Q_324</th><th style='text-align: center;'>Q_325</th><th style='text-align: center;'>Q_326</th><th style='text-align: center;'>Q_327</th><th style='text-align: center;'>Q_328</th><th style='text-align: center;'>Q_329</th><th style='text-align: center;'>Q_330</th><th style='text-align: center;'>Q_331</th><th style='text-align: center;'>Q_332</th><th style='text-align: center;'>Q_333</th><th style='text-align: center;'>Q_334</th><th style='text-align: center;'>Q_335</th><th style='text-align: center;'>Q_336</th><th style='text-align: center;'>Q_337</th><th style='text-align: center;'>Q_338</th><th style='text-align: center;'>Q_339</th><th style='text-align: center;'>Q_340</th><th style='text-align: center;'>Q_341</th><th style='text-align: center;'>Q_342</th><th style='text-align: center;'>Q_343</th><th style='text-align: center;'>Q_344</th><th style='text-align: center;'>Q_345</th><th style='text-align: center;'>Q_346</th><th style='text-align: center;'>Q_347</th><th style='text-align: center;'>Q_348</th><th style='text-align: center;'>Q_349</th><th style='text-align: center;'>Q_350</th><th style='text-align: center;'>Q_351</th><th style='text-align: center;'>Q_352</th><th style='text-align: center;'>Q_353</th><th style='text-align: center;'>Q_354</th><th style='text-align: center;'>Q_355</th><th style='text-align: center;'>Q_356</th><th style='text-align: center;'>Q_357</th><th style='text-align: center;'>Q_358</th><th style='text-align: center;'>Q_359</th><th style='text-align: center;'>Q_360</th><th style='text-align: center;'>Q_361</th><th style='text-align: center;'>Q_362</th><th style='text-align: center;'>Q_363</th><th style='text-align: center;'>Q_364</th><th style='text-align: center;'>Q_365</th><th style='text-align: center;'>Q_366</th><th style='text-align: center;'>Q_367</th><th style='text-align: center;'>Q_368</th><th style='text-align: center;'>Q_369</th><th style='text-align: center;'>Q_370</th><th style='text-align: center;'>Q_371</th><th style='text-align: center;'>Q_372</th><th style='text-align: center;'>Q_373</th><th style='text-align: center;'>Q_374</th><th style='text-align: center;'>Q_375</th><th style='text-align: center;'>Q_376</th><th style='text-align: center;'>Q_377</th><th style='text-align: center;'>Q_378</th><th style='text-align: center;'>Q_379</th><th style='text-align: center;'>Q_380</th><th style='text-align: center;'>Q_381</th><th style='text-align: center;'>Q_382</th><th style='text-align: center;'>Q_383</th><th style='text-align: center;'>Q_384</th><th style='text-align: center;'>Q_385</th><th style='text-align: center;'>Q_386</th><th style='text-align: center;'>Q_387</th><th style='text-align: center;'>Q_388</th><th style='text-align: center;'>Q_389</th><th style='text-align: center;'>Q_390</th><th style='text-align: center;'>Q_391</th><th style='text-align: center;'>Q_392</th><th style='text-align: center;'>Q_393</th><th style='text-align: center;'>Q_394</th><th style='text-align: center;'>Q_395</th><th style='text-align: center;'>Q_396</th><th style='text-align: center;'>Q_397</th><th style='text-align: center;'>Q_398</th><th style='text-align: center;'>Q_399</th><th style='text-align: center;'>Q_400</th><th style='text-align: center;'>Q_401</th><th style='text-align: center;'>Q_402</th><th style='text-align: center;'>Q_403</th><th style='text-align: center;'>Q_404</th><th style='text-align: center;'>Q_405</th><th style='text-align: center;'>Q_406</th><th style='text-align: center;'>Q_407</th><th style='text-align: center;'>Q_408</th><th style='text-align: center;'>Q_409</th><th style='text-align: center;'>Q_410</th><th style='text-align: center;'>Q_411</th><th style='text-align: center;'>Q_412</th><th style='text-align: center;'>Q_413</th><th style='text-align: center;'>Q_414</th><th style='text-align: center;'>Q_415</th><th style='text-align: center;'>Q_416</th><th style='text-align: center;'>Q_417</th><th style='text-align: center;'>Q_418</th><th style='text-align: center;'>Q_419</th><th style='text-align: center;'>Q_420</th><th style='text-align: center;'>Q_421</th><th style='text-align: center;'>Q_422</th><th style='text-align: center;'>Q_423</th><th style='text-align: center;'>Q_424</th><th style='text-align: center;'>Q_425</th><th style='text-align: center;'>Q_426</th><th style='text-align: center;'>Q_427</th><th style='text-align: center;'>Q_428</th><th style='text-align: center;'>Q_429</th><th style='text-align: center;'>Q_430</th><th style='text-align: center;'>Q_431</th><th style='text-align: center;'>Q_432</th><th style='text-align: center;'>Q_433</th><th style='text-align: center;'>Q_434</th><th style='text-align: center;'>Q_435</th><th style='text-align: center;'>Q_436</th><th style='text-align: center;'>Q_437</th><th style='text-align: center;'>Q_438</th><th style='text-align: center;'>Q_439</th><th style='text-align: center;'>Q_440</th><th style='text-align: center;'>Q_441</th><th style='text-align: center;'>Q_442</th><th style='text-align: center;'>Q_443</th><th style='text-align: center;'>Q_444</th><th style='text-align: center;'>Q_445</th><th style='text-align: center;'>Q_446</th><th style='text-align: center;'>Q_447</th><th style='text-align: center;'>Q_448</th><th style='text-align: center;'>Q_449</th><th style='text-align: center;'>Q_450</th><th style='text-align: center;'>Q_451</th><th style='text-align: center;'>Q_452</th><th style='text-align: center;'>Q_453</th><th style='text-align: center;'>Q_454</th><th style='text-align: center;'>Q_455</th><th style='text-align: center;'>Q_456</th><th style='text-align: center;'>Q_457</th><th style='text-align: center;'>Q_458</th><th style='text-align: center;'>Q_459</th><th style='text-align: center;'>Q_460</th><th style='text-align: center;'>Q_461</th><th style='text-align: center;'>Q_462</th><th style='text-align: center;'>Q_463</th><th style='text-align: center;'>Q_464</th><th style='text-align: center;'>Q_465</th><th style='text-align: center;'>Q_466</th><th style='text-align: center;'>Q_467</th><th style='text-align: center;'>Q_468</th><th style='text-align: center;'>Q_469</th><th style='text-align: center;'>Q_470</th><th style='text-align: center;'>Q_471</th><th style='text-align: center;'>Q_472</th><th style='text-align: center;'>Q_473</th><th style='text-align: center;'>Q_474</th><th style='text-align: center;'>Q_475</th><th style='text-align: center;'>Q_476</th><th style='text-align: center;'>Q_477</th><th style='text-align: center;'>Q_478</th><th style='text-align: center;'>Q_479</th><th style='text-align: center;'>Q_480</th><th style='text-align: center;'>Q_481</th><th style='text-align: center;'>Q_482</th><th style='text-align: center;'>Q_483</th><th style='text-align: center;'>Q_484</th><th style='text-align: center;'>Q_485</th><th style='text-align: center;'>Q_486</th><th style='text-align: center;'>Q_487</th><th style='text-align: center;'>Q_488</th><th style='text-align: center;'>Q_489</th><th style='text-align: center;'>Q_490</th><th style='text-align: center;'>Q_491</th><th style='text-align: center;'>Q_492</th><th style='text-align: center;'>Q_493</th><th style='text-align: center;'>Q_494</th><th style='text-align: center;'>Q_495</th><th style='text-align: center;'>Q_496</th><th style='text-align: center;'>Q_497</th><th style='text-align: center;'>Q_498</th><th style='text-align: center;'>Q_499</th><th style='text-align: center;'>Q_500</th><th style='text-align: center;'>Q_501</th><th style='text-align: center;'>Q_502</th><th style='text-align: center;'>Q_503</th><th style='text-align: center;'>Q_504</th><th style='text-align: center;'>Q_505</th><th style='text-align: center;'>Q_506</th><th style='text-align: center;'>Q_507</th><th style='text-align: center;'>Q_508</th><th style='text-align: center;'>Q_509</th><th style='text-align: center;'>Q_510</th><th style='text-align: center;'>Q_511</th><th style='text-align: center;'>Q_512</th><th style='text-align: center;'>Q_513</th><th style='text-align: center;'>Q_514</th><th style='text-align: center;'>Q_515</th><th style='text-align: center;'>Q_516</th><th style='text-align: center;'>Q_517</th><th style='text-align: center;'>Q_518</th><th style='text-align: center;'>Q_519</th><th style='text-align: center;'>Q_520</th><th style='text-align: center;'>Q_521</th><th style='text-align: center;'>Q_522</th><th style='text-align: center;'>Q_523</th><th style='text-align: center;'>Q_524</th><th style='text-align: center;'>Q_525</th><th style='text-align: center;'>Q_526</th><th style='text-align: center;'>Q_527</th><th style='text-align: center;'>Q_528</th><th style='text-align: center;'>Q_529</th><th style='text-align: center;'>Q_530</th><th style='text-align: center;'>Q_531</th><th style='text-align: center;'>Q_532</th><th style='text-align: center;'>Q_533</th><th style='text-align: center;'>Q_534</th><th style='text-align: center;'>Q_535</th><th style='text-align: center;'>Q_536</th><th style='text-align: center;'>Q_537</th><th style='text-align: center;'>Q_538</th><th style='text-align: center;'>Q_539</th><th style='text-align: center;'>Q_540</th><th style='text-align: center;'>Q_541</th><th style='text-align: center;'>Q_542</th><th style='text-align: center;'>Q_543</th><th style='text-align: center;'>Q_544</th><th style='text-align: center;'>Q_545</th><th style='text-align: center;'>Q_546</th><th style='text-align: center;'>Q_547</th><th style='text-align: center;'>Q_548</th><th style='text-align: center;'>Q_549</th><th style='text-align: center;'>Q_550</th><th style='text-align: center;'>Q_551</th><th style='text-align: center;'>Q_552</th><th style='text-align: center;'>Q_553</th><th style='text-align: center;'>Q_554</th><th style='text-align: center;'>Q_555</th><th style='text-align: center;'>Q_556</th><th style='text-align: center;'>Q_557</th><th style='text-align: center;'>Q_558</th><th style='text-align: center;'>Q_559</th><th style='text-align: center;'>Q_560</th><th style='text-align: center;'>Q_561</th><th style='text-align: center;'>Q_562</th><th style='text-align: center;'>Q_563</th><th style='text-align: center;'>Q_564</th><th style='text-align: center;'>Q_565</th><th style='text-align: center;'>Q_566</th><th style='text-align: center;'>Q_567</th><th style='text-align: center;'>Q_568</th><th style='text-align: center;'>Q_569</th><th style='text-align: center;'>Q_570</th><th style='text-align: center;'>Q_571</th><th style='text-align: center;'>Q_572</th><th style='text-align: center;'>Q_573</th><th style='text-align: center;'>Q_574</th><th style='text-align: center;'>Q_575</th><th style='text-align: center;'>Q_576</th><th style='text-align: center;'>Q_577</th><th style='text-align: center;'>Q_578</th><th style='text-align: center;'>Q_579</th><th style='text-align: center;'>Q_580</th><th style='text-align: center;'>Q_581</th><th style='text-align: center;'>Q_582</th><th style='text-align: center;'>Q_583</th><th style='text-align: center;'>Q_584</th><th style='text-align: center;'>Q_585</th><th style='text-align: center;'>Q_586</th><th style='text-align: center;'>Q_587</th><th style='text-align: center;'>Q_588</th><th style='text-align: center;'>Q_589</th><th style='text-align: center;'>Q_590</th><th style='text-align: center;'>Q_591</th><th style='text-align: center;'>Q_592</th><th style='text-align: center;'>Q_593</th><th style='text-align: center;'>Q_594</th><th style='text-align: center;'>Q_595</th><th style='text-align: center;'>Q_596</th><th style='text-align: center;'>Q_597</th><th style='text-align: center;'>Q_598</th><th style='text-align: center;'>Q_599</th><th style='text-align: center;'>Q_600</th><th style='text-align: center;'>Q_601</th><th style='text-align: center;'>Q_602</th><th style='text-align: center;'>Q_603</th><th style='text-align: center;'>Q_604</th><th style='text-align: center;'>Q_605</th><th style='text-align: center;'>Q_606</th><th style='text-align: center;'>Q_607</th><th style='text-align: center;'>Q_608</th><th style='text-align: center;'>Q_609</th><th style='text-align: center;'>Q_610</th><th style='text-align: center;'>Q_611</th><th style='text-align: center;'>Q_612</th><th style='text-align: center;'>Q_613</th><th style='text-align: center;'>Q_614</th><th style='text-align: center;'>Q_615</th><th style='text-align: center;'>Q_616</th><th style='text-align: center;'>Q_617</th><th style='text-align: center;'>Q_618</th><th style='text-align: center;'>Q_619</th><th style='text-align: center;'>Q_620</th><th style='text-align: center;'>Q_621</th><th style='text-align: center;'>Q_622</th><th style='text-align: center;'>Q_623</th><th style='text-align: center;'>Q_624</th><th style='text-align: center;'>Q_625</th><th style='text-align: center;'>Q_626</th><th style='text-align: center;'>Q_627</th><th style='text-align: center;'>Q_628</th><th style='text-align: center;'>Q_629</th><th style='text-align: center;'>Q_630</th><th style='text-align: center;'>Q_631</th><th style='text-align: center;'>Q_632</th><th style='text-align: center;'>Q_633</th><th style='text-align: center;'>Q_634</th><th style='text-align: center;'>Q_635</th><th style='text-align: center;'>Q_636</th><th style='text-align: center;'>Q_637</th><th style='text-align: center;'>Q_638</th><th style='text-align: center;'>Q_639</th><th style='text-align: center;'>Q_640</th><th style='text-align: center;'>Q_641</th><th style='text-align: center;'>Q_642</th><th style='text-align: center;'>Q_643</th><th style='text-align: center;'>Q_644</th><th style='text-align: center;'>Q_645</th><th style='text-align: center;'>Q_646</th><th style='text-align: center;'>Q_647</th><th style='text-align: center;'>Q_648</th><th style='text-align: center;'>Q_649</th><th style='text-align: center;'>Q_650</th><th style='text-align: center;'>Q_651</th><th style='text-align: center;'>Q_652</th><th style='text-align: center;'>Q_653</th><th style='text-align: center;'>Q_654</th><th style='text-align: center;'>Q_655</th><th style='text-align: center;'>Q_656</th><th style='text-align: center;'>Q_657</th><th style='text-align: center;'>Q_658</th><th style='text-align: center;'>Q_659</th><th style='text-align: center;'>Q_660</th><th style='text-align: center;'>Q_661</th><th style='text-align: center;'>Q_662</th><th style='text-align: center;'>Q_663</th><th style='text-align: center;'>Q_664</th><th style='text-align: center;'>Q_665</th><th style='text-align: center;'>Q_666</th><th style='text-align: center;'>Q_667</th><th style='text-align: center;'>Q_668</th><th style='text-align: center;'>Q_669</th><th style='text-align: center;'>Q_670</th><th style='text-align: center;'>Q_671</th><th style='text-align: center;'>Q_672</th><th style='text-align: center;'>Q_673</th><th style='text-align: center;'>Q_674</th><th style='text-align: center;'>Q_675</th><th style='text-align: center;'>Q_676</th><th style='text-align: center;'>Q_677</th><th style='text-align: center;'>Q_678</th><th style='text-align: center;'>Q_679</th><th style='text-align: center;'>Q_680</th><th style='text-align: center;'>Q_681</th><th style='text-align: center;'>Q_682</th><th style='text-align: center;'>Q_683</th><th style='text-align: center;'>Q_684</th><th style='text-align: center;'>Q_685</th><th style='text-align: center;'>Q_686</th><th style='text-align: center;'>Q_687</th><th style='text-align: center;'>Q_688</th><th style='text-align: center;'>Q_689</th><th style='text-align: center;'>Q_690</th><th style='text-align: center;'>Q_691</th><th style='text-align: center;'>Q_692</th><th style='text-align: center;'>Q_693</th><th style='text-align: center;'>Q_694</th><th style='text-align: center;'>Q_695</th><th style='text-align: center;'>Q_696</th><th style='text-align: center;'>Q_697</th><th style='text-align: center;'>Q_698</th><th style='text-align: center;'>Q_699</th><th style='text-align: center;'>Q_700</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.109 A display of the MVs and DVs.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_895_779_1115.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.110 Manipulated variables, MVs.</div>


---

<!-- PDF page 546 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_810_342.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.111 Controlled variables, CVs.</div>


#### 8.4.3 Aspen Nonlinear Controller: Task 1 – Model Identification

##### 8.4.3.1 Step-Response Plot

At the far right of the tool ribbons, we click on “Create Model” button. In “Model Type Selection,” we choose “Nonlinear.” See Figure 8.112. Clicking on OK gives the “Identify Model” inputs. See Figure 8.113.

Clicking on “Options” displayed in Figure 8.113 gives the default specifications of Figure 8.114. We accept these specifications and click on “OK.” We then click on “Identify” shown in Figure 8.113. This results in the step-response plot of

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_639_811_810.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.112 Selection of model type.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_876_648_1217.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 8.113 "identify Model" inputs.</div>


---

<!-- PDF page 547 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_147_580_471.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">Figure 8.114 Model identification options.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_540_777_845.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.115 Step response curves of a nonlinear polypropylene process.</div>


Figure 8.115, which represents the first type of plot under “model views” button on the top tool ribbon.

The step-response curve of a nonlinear polymer process is quite different from that of a linear process (e.g. Figure 8.53). For example, when H2_C2, a MV, increases, the affected MI_Lab, a CV, also increases, but it displays three response curves of increasing values from colors in red to blue and then to green. By contrast, when MV C4_C2 increases, the affected CVs, Density_Lab and Density_Inst, show three response curves of decreasing values from colors in red to blue and then to green. These responses depend on the operating point or values of the MVs, the direction of the change, and the step size of the change in MV. In particular, the three response curves in the figure represent the time-dependent change of a chosen CV to a change of a chosen MV with its magnitude equal to the default step size of 1 (red curve), two times the step size (blue curve) and three times the step size (green curve). Additionally, putting the mouse inside the response curve box for a selected CV-MV pair,

---

<!-- PDF page 548 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_147_809_327.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.116 Showing the details of the MI_Lab-H2_C2 step response curve.</div>


right-clicking to open the menu, and selecting “details,” we see a detailed plot of the MI_Lab-H2_C2 response curve in Figure 8.116.

##### 8.4.3.2 I/O Response Plot

Next, we click on the I/O button on the top tool ribbon to generate an I/O plot, which represents the response of each output as each input is moved from its lower limit to its upper limit. See Figure 8.117 for the resulting I/O plot and Figure 8.118 for a detailed MI_Lab-H2_C2 I/O plot. In the I/O plot, the limits are either the validity limits or the minimum and maximum values for that input from the current dataset. We see in Figure 8.117 that as MV C4_C2 increases,

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_685_809_929.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.117 The I/O response curve of a nonlinear polypropylene process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_1010_808_1222.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.118 Showing the details of the MI_Lab-H2_C2 I/O response curve.</div>


---

<!-- PDF page 549 -->

both Density_Lab and Density_Inst decrease. Table 8.5 summarizes the positive or negative sign of  $ \Delta CV/\Delta MV $ or  $ \Delta CV/\Delta DV $ for CVs (MI_Lab, MI_Inst, Density_Lab, and Density_Inst) and MVs (H2_C2, C4_C2) or DVs (Temp, C2_Partial_Pressure).

##### 8.4.3.3 Gain Plot

Finally, we click on the “Gain” button on the top tool ribbon to generate a gain plot of Figure 8.119, which represents the amount of gain for each input/output pair as each input increases from its lower limit to its upper limit. Figure 8.120 presents a detailed MI_Lab-H2_C2 I/O plot.

<div style="text-align: center;">Table 8.5 Positive or negative sign of  $ \Delta CV/\Delta MV $ or  $ \Delta CV/\Delta DV $.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>MV or DV</td><td style='text-align: center; word-wrap: break-word;'>CV-1. MI</td><td style='text-align: center; word-wrap: break-word;'>CV-2. Density</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.  $ H_{2} $_C2</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $MV&gt;0</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $MV&gt;0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.  $ H_{2} $_C4</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $MV&gt;0</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $MV&lt;0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Temp</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $DV&gt;0</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $DV&gt;0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4.  $ H_{2} $_partial_pressure</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $DV&gt;0</td><td style='text-align: center; word-wrap: break-word;'>$ \Delta $CV/ $ \Delta $DV&gt;0</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Model Name</td><td colspan="5">3D Device</td></tr></table>

<div style="text-align: center;">Figure 8.119 The gain plot of a nonlinear polypropylene plot.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1085_777_1223.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.120 Showing the details of the MI_Lab-H2_C2 gain curve.</div>


---

<!-- PDF page 550 -->

#### 8.4.4 Aspen Nonlinear Controller: Task 1 – Model Identification; Building the Nonlinear State-Space Bounded Derivative Network (SS-BDN)

##### 8.4.4.1 Configure Dynamics and Output States

On the top tool ribbon, we click on “Build Models” button. We see an “Edit MISO Models” window and hit the “Configuration” button. This results in Figure 8.121, displaying the default model type, “Model Identified.” We replace each model type of our output variable (CV) with BDN through the drop-down menu. This leads to Figure 8.122. We see the “Inputs” button in Figure 8.122. Clicking on the “Inputs” and specifying the inputs affecting each output, we see Figure 8.123. Next, we hit the “Deadtimes” and specify the initial Deadtimes in number of sample periods. These dead times are used to model nonlinearity in the initial process response during changes. See Figure 8.124. We click on each output variable, followed by hitting the “Identify Deadtimes” button and keeping the default parameters and then click on “Identify” to identify Deadtimes. See Figure 8.125. Repeat this step for all four output variables (MI_Lab, MI_Inst, Density_Lab, and Density_Inst).

Having identified the Deadtimes, we click on “Configure” button displayed in Figures 8.121–8.125. This leads to Figure 8.126, in which we configure within the “Dynamics” tab, the filter time constants for input variables (He_C2, C4_C2, Temp, and C2_Partial_Pressure) for output variable MI_Lab. We repeat this step for output variables MI-Inst, Density_Lab, and Density_Inst. Next, we switch to the “Output States” tab within “Configure” step, and configure one output state, one for each

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_750_809_976.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.121 Displaying available model types.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_1060_810_1220.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.122 Choosing the model type, bounded derivative network (BDN).</div>


---

<!-- PDF page 551 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_159_779_328.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.123 Specifying the input variables affecting each output.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_404_779_581.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.124 Specifying the dead times: “2” refers to the number of sample periods (called index value).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_677_779_905.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.125 Identify for Deadtimes for MI_Lab. Repeat this step for all four output variables.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_997_779_1190.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.126 Configure the filter time constants for input variables (He_C2, C4_C2, Temp, C2_Partial_Pressure) for output variable M1_Lab.</div>


---

<!-- PDF page 552 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_146_811_349.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.127 Configure the output states for each filter for input variables (He_C2, C4_C2, Temp, C2_Partial_Pressure) for output variable MI_Lab.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_437_810_695.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.128 Specify the steady-state gain constraints for MI-Lab following Table 8.5.</div>


filter, as illustrated in Figure 8.127. We repeat this step for output variables MI-Inst, Density_Lab, and Density_Inst.

##### 8.4.4.2 Build Model with Gain Constraints

This step features a significant ability of the BDN to build a model based on specified gain constraints to avoid incorrect gain inversion discussed in Section 8.3.2.1. Based on Figure 8.117 and Table 8.5 in Section 8.4.3.2, we can specify the corresponding gain constraints.

We specify the steady-state gain constraints by continuing the “Configure” step and clicking on “Steady State” tab displayed in Figure 8.127, corresponding to output or CV, MI_Lab. This gives Figure 8.128, in which we specify a Min Gain of 0 and a Max Gain of 10,000 for a positive gain; and a Min Gain of -10,000 and a Max Gain of 0 for a negative gain following Table 8.5. We then select “Identify” to build the BDN model for the MI-Lab. Figure 8.129 shows the resulting comparison between the nonlinear BDN model prediction and plant data for MI-Lab. For an average MI_Lab value of 4, the root-mean-squared error (RMSE) between the model prediction and plant data is only 0.0221, or approximately 0.55%.

Figure 8.130 shows the specification of steady-state gain constraints for Density_Lab, following Table 8.5, and Figure 8.131 compares the predicted Density_Lab values from the nonlinear BDN model with plant data. For an average value of

---

<!-- PDF page 553 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_148_780_490.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.129 Comparison between nonlinear BDN model prediction with plant data for MI_Lab with a "Max Gain" of 10000.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_567_778_850.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.130 Specify the steady-state gain constraints for Density-Lab following Table 8.5.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Iteration</th><th style='text-align: center;'>Calibration Data</th><th style='text-align: center;'>Model Time</th><th style='text-align: center;'>Model Scores</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>10000000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>100000000000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000000000000000000000</td><td style='text-align: center;'>100</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>Random Scores</td></tr>
    <tr><td style='text-align: center;'>1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.131 Comparison between nonlinear BDN model prediction with plant data for Density_Lab with a “Min Gain” for C4_C2 of -10000, and a “Max Gain” for the remaining inputs of +10000.</div>


---

<!-- PDF page 554 -->

Density_Lab of 918, the RMSE between the model prediction and plant data is only 0.007485, or approximately 0.008154%.

Following the steady-state gain constraints of Table 8.5 and repeating the same procedure to identify the models for MI_Inst and Density_Inst, we get essentially identical comparison curves as in Figures 8.129 for MI and 8.131 for Density.

##### 8.4.4.3 Fine-Tune Steady-State BDN Gains

Referring to Figure 8.128, we narrow the range of the steady-state BDN gain by lowering the “Max Gain” for all four inputs from 10,000 to 100 and run the BDN regression again. This results in Figure 8.132, in which the error between the model prediction and plant data of MI_Lab drops from 0.022068413 to 0.010037448. Likewise, referring to Figure 8.130 for Density_Lab, we change the “Min Gain” for C4_C2 to -100, and the “Max Gain” for the remaining three inputs to 100, and run the BDN regression. We find that the resulting error between the model prediction and plant data of Density_Lab shows no improvement.

After configuring and identifying the SS-BDN model, we see the “OK” status of the model identification, as seen in Figure 8.133. We also see the resulting steady-state gain plot of Figure 8.134.

Table 8.6 shows the resulting steady-state gain for the SS-BDN model. In practice, we only pay attention to the columns of MI_Lab and Density_Lab. We do not need to develop the model for MI_Inst and Density_Inst.

##### 8.4.4.4 Generate Model Predictions

Next, we apply the SS-BDN model to predict the MI_Lab and Density_Lab, and compare the predictions with plant data. We click on “Generate Predictions” on the top

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_811_809_1032.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.132 Comparison between nonlinear BDN model prediction with plant data for MI_Lab with a "Max Gain" of 100.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1120_808_1222.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.133 Status "OK" indicating completion of the SS-BDN model identification.</div>


---

<!-- PDF page 555 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_148_778_343.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.134 Steady-state gain plot of the SS-BDN model.</div>


<div style="text-align: center;">Table 8.6 Steady-state gains of the SS-BDN model.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>MV/DV↓</td><td style='text-align: center; word-wrap: break-word;'>CV→</td><td style='text-align: center; word-wrap: break-word;'>MI_Lab</td><td style='text-align: center; word-wrap: break-word;'>MI_Inst</td><td style='text-align: center; word-wrap: break-word;'>Density_Lab</td><td style='text-align: center; word-wrap: break-word;'>Density_Inst</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2_C2</td><td style='text-align: center; word-wrap: break-word;'>29.1</td><td style='text-align: center; word-wrap: break-word;'>29.1</td><td style='text-align: center; word-wrap: break-word;'>14.4</td><td style='text-align: center; word-wrap: break-word;'>14.4</td><td style='text-align: center; word-wrap: break-word;'>14.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C4_C2</td><td style='text-align: center; word-wrap: break-word;'>2.42</td><td style='text-align: center; word-wrap: break-word;'>2.42</td><td style='text-align: center; word-wrap: break-word;'>$ -23.7 $</td><td style='text-align: center; word-wrap: break-word;'>$ -23.7 $</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temp</td><td style='text-align: center; word-wrap: break-word;'>0.088</td><td style='text-align: center; word-wrap: break-word;'>0.088</td><td style='text-align: center; word-wrap: break-word;'>0.44</td><td style='text-align: center; word-wrap: break-word;'>0.44</td><td style='text-align: center; word-wrap: break-word;'>0.44</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2_Partial_Pressure</td><td style='text-align: center; word-wrap: break-word;'>0.59</td><td style='text-align: center; word-wrap: break-word;'>0.59</td><td style='text-align: center; word-wrap: break-word;'>0.18</td><td style='text-align: center; word-wrap: break-word;'>0.18</td><td style='text-align: center; word-wrap: break-word;'>0.18</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_719_616_867.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 8.135 Select dataset to compare with model predictions.</div>


tool ribbons and choose dataset WS8.2. See Figure 8.135. The resulting comparison appears in Figure 8.136.

#### 8.4.5 Aspen Nonlinear Controller: Task 2 – Configuration – Model Configuration

As discussed in Section 8.2.14, the model configuration task involves the specifications of feedback filters for prediction errors, based on prediction error filtering covered in Section 8.1.5. We click on the “Feedback Filter” button within the top tool ribbons, followed by “Fine Tune” button to fine-tune the feedback filter. See Figures 8.137 and 8.138.

---

<!-- PDF page 556 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_807_426.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.136 Generated model predictions of MI_Lab and Density_Lab.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_492_809_612.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.137 Choosing the default feedback filter.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_678_808_939.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.138 Fine-tune the feedback filter.</div>


#### 8.4.6 Aspen Nonlinear Controller: Task 2 – Configuring and Running the Steady-State Optimization

We follow Figure 8.92 to configure the steady-state optimizer. Figure 8.139 specifies the inputs and outputs to configure the optimizer. Figures 8.140a and 8.140b show the input entries for MVs and CVs for the steady-state simulator, respectively. In Figure 8.140a, we set the initial LP costs for MVs based on the negative values of the steady-state gains reported in Table 8.6. We do this by following the example illustrated in Figure 8.12 and Table 8.1. We note that in Table 8.6, in the MI_Lab column, all gains are positive; in the Density_Lab column, the gain  $ \Delta(\text{Density\_Lab})/\Delta(\text{C}_4\text{C}_2) $ is negative. In the following, we choose the negative

---

<!-- PDF page 557 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_150_778_260.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.139 Inputs and outputs for steady-state optimization.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_329_776_561.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.140a Specifications of MVs for steady-state simulator.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_634_775_799.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.140b Specifications of CVs for steady-state simulator.</div>


values of the steady-state gains in the Density_Lab column of Table 8.6 as our initial LP costs, except that we change the gain value for  $ \Delta(\text{Density\_Lab})/\Delta(\text{C}_4\text{C}_2) $ from -23.7 to -5 (hence, the LP cost becomes +5 for MV or input C4_C2 in Figure 8.140a). As discussed in Section 8.1.2.2 and Table 8.1, an input or a MV with a positive LP cost means that to minimize cost and maximize profit, we tend to move the MV toward its lower operating limit. By contrast, we tend to move a MV with a negative LP cost toward its upper operating limit. We will explore the impact of having different initial LP costs on the resulting steady-state targets of MVs and CVs.

Next, we click on the “Constraints” button and see the display of Figure 8.141. We are to calculate the steady-state targets of CVs and MVs.

We initialize the steady-state optimizer calculation by specifying the dataset WS8.2 and canceling the initialization of the dynamic tuning. See Figure 8.142.

We now explore the impact of using the negative values of the steady-state gains in the MI_Lab column of Table 8.6 as our initial LP costs. Figures 8.146a,b show the specifications MVs for steady-state simulator. The specifications for the CV are

---

<!-- PDF page 558 -->

identical to those displayed in Figure 8.140b. Following the same procedure as in Figures 8.141 and 8.144, we find the results of steady-state values obtained by the steady-state optimizer in Figure 8.147, which are different from those displayed in Figure 8.143. This comparison demonstrates that the initial LP cost specifications affect the resulting steady-state targets for both MVs and CVs.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_301_809_458.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.141 Current constraints of MVs and CVs for steady-state optimization.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_533_655_694.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 8.142 Initialize steady-state optimizer by specifying the dataset.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_768_810_990.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.143 Steady-state values obtained by the steady-state optimizer.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1068_810_1222.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.144 Specifications of MVs for steady-state simulator.</div>


---

<!-- PDF page 559 -->

In Table 8.6, between the negative values of  $ Density\_Lab $ column and of  $ MI\_Lab $ column, which set of values should we use as initial LP costs displayed in Figures 8.145 and 8.147? We suggest choosing the set of initial LP costs that gives us the steady-state target values of CV that are close to our intended controller operation.

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_302_780_474.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.145 Steady-state values obtained by the steady-state optimizer.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Inputs</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td></tr><tr><td colspan="2">H2_C2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-29.1</td></tr><tr><td colspan="2">C4_C2</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-2.42</td></tr><tr><td colspan="2">Temp</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>-0.008</td></tr><tr><td colspan="2">C2_Partial_Pressure</td><td style='text-align: center; word-wrap: break-word;'>6.52</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6.52</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>-0.38</td></tr><tr><td colspan="2">OutOfService Value</td><td style='text-align: center; word-wrap: break-word;'>Move Down Limit</td><td style='text-align: center; word-wrap: break-word;'>Move Up</td><td style='text-align: center; word-wrap: break-word;'>Use Limit Tracking</td><td style='text-align: center; word-wrap: break-word;'>Validated Measurement</td><td style='text-align: center; word-wrap: break-word;'>Setpoint</td><td style='text-align: center; word-wrap: break-word;'>Loop Status</td><td style='text-align: center; word-wrap: break-word;'>Reverse Acting</td><td style='text-align: center; word-wrap: break-word;'>Plot Low</td><td style='text-align: center; word-wrap: break-word;'>Plot High</td><td style='text-align: center; word-wrap: break-word;'>High Limit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>72.5</td><td style='text-align: center; word-wrap: break-word;'>102.5</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>4.6</td><td style='text-align: center; word-wrap: break-word;'>9.4</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>On</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.09</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 8.146 (a) Initial MV specifications of controller simulation. (b) Initial CV specifications of controller simulation.</div>


---

<!-- PDF page 560 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>Move Suppression</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2-C2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-29.1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C4-C2</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.35</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-10</td><td style='text-align: center; word-wrap: break-word;'>0.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temp</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>85</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>-0.088</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2 Partial Pressure</td><td style='text-align: center; word-wrap: break-word;'>6.52</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6.52</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>-0.58</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>Prediction</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td><td style='text-align: center; word-wrap: break-word;'>SS Low Concern</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI_Lab</td><td style='text-align: center; word-wrap: break-word;'>2.701</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI_Inst</td><td style='text-align: center; word-wrap: break-word;'>2.687</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density_Lab</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>938</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density_Inst</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>938</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>40</td></tr></table>

<div style="text-align: center;">Figure 8.147 Changes to selected MV and CV tuning parameters for MI and Density transition control.</div>


#### 8.4.7 Aspen Nonlinear Controller: Task 3 – Configuring and Simulating the Dynamic Controller with Setpoint Changes

We follow Figure 8.97a to initialize the controller simulation. Figure 8.146a,b show the inputs for MVs and CVs, including the operating values and tuning values. We save the resulting simulation file as WS8.2_BaseCase_BDN.dmc3application.

We wish to simulate the transition control of CV values of MI_Lab and MI_Inst from 2.7 to 1.5 while keeping both Density_Lab and Density_Inst between a lower operating limit of 938 kg/m³ and an UPL of 940 kg/m³. Based on Figure 8.134 and Table 8.6, we expect the following changes to the MVs: C2_H2 and C4_C2 values to increase toward their UPL, and temp and C2_Partial_Pressure values remain essentially unchanged.

We lower the initial move suppression of both MVs, C2_H2, and C4_C2, from 1 to 0.2, to speed up the increase of both MVs. We also increase the initial move suppression of MV, Temp, from 1 to 5, to slow down the change in Temp.

Figure 8.147 shows the changes of our MV and CV specifications.

Figure 8.148 shows the results after CV steady-state values reach their operating limits, that is, at a MI-Lab value of 1.5, and a Density-Lab value of 925 kg/m³. We note that during the simulation, the controller runs in a true closed-loop fashion, with measurement data received as follows: (1) For MVs, the setpoint calculated by the


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Inputs</td><td style='text-align: center; word-wrap: break-word;'>easurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Current Move</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ H_{2}, C_{2} $</td><td style='text-align: center; word-wrap: break-word;'>0.2164</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1627</td><td style='text-align: center; word-wrap: break-word;'>-0.0189</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-29.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ C_{4}, C_{2} $</td><td style='text-align: center; word-wrap: break-word;'>0.3554</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>-0.1247</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>-10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temp</td><td style='text-align: center; word-wrap: break-word;'>84.15</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>85.15</td><td style='text-align: center; word-wrap: break-word;'>0.6518</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>-0.088</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ C_{2}, Partial\_Pressure $</td><td style='text-align: center; word-wrap: break-word;'>6.344</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>7.344</td><td style='text-align: center; word-wrap: break-word;'>-0.1064</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>-0.58</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Outputs</td><td style='text-align: center; word-wrap: break-word;'>Measurement</td><td style='text-align: center; word-wrap: break-word;'>Validity Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Operator Low Limit</td><td style='text-align: center; word-wrap: break-word;'>Steady State Value</td><td style='text-align: center; word-wrap: break-word;'>Operator High Limit</td><td style='text-align: center; word-wrap: break-word;'>Engineering High Limit</td><td style='text-align: center; word-wrap: break-word;'>Validity High Limit</td><td style='text-align: center; word-wrap: break-word;'>Prediction</td><td style='text-align: center; word-wrap: break-word;'>LP Cost</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI_Lab</td><td style='text-align: center; word-wrap: break-word;'>2.95</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>2.949</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI_Inst</td><td style='text-align: center; word-wrap: break-word;'>2.95</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>2.949</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density_Lab</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>925</td><td style='text-align: center; word-wrap: break-word;'>925</td><td style='text-align: center; word-wrap: break-word;'>930</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density_Inst</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>840</td><td style='text-align: center; word-wrap: break-word;'>925</td><td style='text-align: center; word-wrap: break-word;'>925</td><td style='text-align: center; word-wrap: break-word;'>930</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>940</td><td style='text-align: center; word-wrap: break-word;'>919</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">Figure 8.148 Results after CV steady-state values reach their operating limits.</div>


---

<!-- PDF page 561 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Measurement</th><th style='text-align: center;'>Prediction</th><th style='text-align: center;'>Calculated Steady State Target</th><th style='text-align: center;'>Open Loop Prediction</th><th style='text-align: center;'>Closed Loop Prediction</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>12:42:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>12:48:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>12:54:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:00:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:06:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:12:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:18:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:24:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:30:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:36:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:42:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>13:48:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:04:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:10:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:16:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:22:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:28:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:34:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:40:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>14:46:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:00:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:06:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:12:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:18:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:24:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:30:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:36:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:42:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>15:48:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:04:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:10:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:16:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:22:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:28:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:34:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:40:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:46:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>16:52:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:00:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:06:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:12:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:18:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:24:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:30:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:36:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:42:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>17:48:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:04:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:10:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:16:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:22:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:28:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:34:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:40:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:46:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>18:52:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:00:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:06:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:12:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:18:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:24:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:30:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:36:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:42:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>19:48:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:04:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:10:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:16:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:22:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:28:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:34:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:40:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:46:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>20:52:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>21:00:00</td><td style='text-align: center;'>2.90</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.45</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.149 Controller simulation plot showing the closed-loop predictions (in red) approach the calculated steady-state targets (in greed) of CVs.</div>


move plan is transferred to the measurement value; and (2) For CVs, the prediction for the next cycle is transferred to the measurement value. Therefore, the measurements of all variables do not become stale.

The top plot in Figure 8.149 shows that the closed-loop MI_Lab prediction (in red) continues to decrease downward and approach the calculated steady-state target (the UPL) of 1.5 (in green); the bottom plot in Figure 8.149 shows that the closed-loop Density_Lab prediction (in red) continues to increase upward and approach the calculated steady-state target (the lower operating limit) of 925 kg/m³. We will not show the remaining simulation cycle in which the closed-loop prediction values match the calculated steady-state targets.

This concludes the current workshop. We save the project as PP Density and MI Control_Final.

### 8.5 Aspen Maestro for Automating the Model-Building Workflow

Aspen DMC3 V12 has added a powerful tool to automate the model-building process for MPC. We recommend the reader to take time to view the on-demand webinar by Kalafatis [21] to see how embedding AI into DMC3 can greatly speed up the model-building process and improve the model-prediction accuracy. However, we emphasize that to truly understand the concepts and know-how behind each step of this automated model-building process, the reader should first become familiar with the fundamentals and practice we cover in Sections 8.1 and 8.2.

Figures 8.150a–8.150d [22] show the screen image of the four steps of the automated model-building process using Aspen Maestro, which is an integrated part of DMC3 V12 and later versions. Note that we have purposely removed a part of the step-response curves on the right side of the figure to clearly show the Aspen Maestro workflow steps.

---

<!-- PDF page 562 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_809_517.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.150a Step 1 of Aspen Maestro model workflow for DMC3 – Select variables.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_590_809_920.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.150b Step 2 of Aspen Maestro model workflow for DMC3 – Data mining.</div>


Step 1. Select variables: Figure 8.150a; follow Sections 8.2.2–8.2.4. Note the new “Maestro Model” button next to the “Select Variables” button in DMC3 V12 on the left of top tool buttons.

Step 2. Data mining: Figure 8.150b; automate Section 8.2.5, data slicing – this step explores data slices used to create the model. Select one of the four available options in the sensitivity scale (PID, low, medium, and high) and view the data slicing results. A high sensitivity scale tends to include the best independent moves available to each input or MV. Note the new “Data Mining” button in DMC3 V12 on the left of top tool buttons.

Step 3a. Data analysis – Correlation detection Figure 8.150c – input correlation detection. This step quantifies how much an input variable or a MV correlates with

---

<!-- PDF page 563 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_780_509.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 8.150c Step 3a of Aspen Maestro model workflow for DMC3 – Input correlation detection.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_600_781_942.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.150d Step 3b of Aspen Maestro model workflow for DMC3 – Transform detection.</div>


another input variable. Clusters of input variables inside a circle represent highly correlated variables with correlation coefficients close to -1.0 to 1.0. A correlation of -1.0 shows a perfect negative correlation, while a correlation of 1.0 shows a perfect positive correlation. See Section 8.2.8 and Figure 8.57. The plot also identifies input variables with no or minimum correlation.

Step 3b. Transform detection. Figure 8.150d. This figure shows an example of transforming dependent variable measurements into a piecewise linear representation, that is, correlating the measurement data into connected multiple straight-line segments with different slopes. Aspen Maestro automates the development of transforms in DMC3 to deal with nonlinear dependent variable measurements.

---

<!-- PDF page 564 -->

and configures transforms to re-scale the data. For example, Aspen Maestro includes the well-known linear valve output transform and parabolic valve output transform introduced in Perry's Chemical Engineers' Handbook, 5th edition, that relates the fraction of maximum flow rate, Q, to fraction of valve stem travel, L, with a valve transform parameter  $ \alpha $ ( $ 0 < \alpha \leq 1 $) according to Eqs. (8.53) and (8.54):

 $$ Q=\frac{L}{\sqrt{\alpha+(1-\alpha)L^{2}}}\left(linear\right) $$ 

 $$ Q=\frac{L^{2}}{\sqrt{\alpha+(1-\alpha)L^{4}}}\ (parabolic) $$ 

Figure 8.151 shows a plot of valve output transforms, displaying both linear and parabolic valves, Eqs. (8.53) and (8.54).

Step 4. Create Model. Figure 8.152 shows the model results based on previous selections of data mining (data slicing) and data analysis. Aspen Maestro automatically selects the best model curves to generate the final model, and we can transfer the resulting model to the controller view.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Fractional valve stem position, L</th><th style='text-align: center;'>α = 0.05</th><th style='text-align: center;'>α = 0.2</th><th style='text-align: center;'>α = 0.20</th><th style='text-align: center;'>α = 0.25</th><th style='text-align: center;'>α = 0.5</th><th style='text-align: center;'>α = 0.75</th><th style='text-align: center;'>α = 1.0</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.01</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.02</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>0.82</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.03</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.04</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.84</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.06</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0.99</td><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.83</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8.151 An illustration of linear and parabolic valve output transformations included in Aspen Maestro. Used with permission from Aspen Technology. Inc.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_950_810_1220.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 8.152 Step 4 of Aspen Maestro model workflow for DMC3 – create model.</div>


---

<!-- PDF page 565 -->

This concludes our illustration of Aspen Maestro for automating the model-building process. In Chapter 10, we will further illustrate embedding AI into DMC3 by using deep learning neural networks (such as LSTM [long short-term memory]) recurrent networks (see Section 10.4.2.2), and GRU (gated recurrent networks) (see Section 10.4.2.3) to develop soft sensors or IQ inferential for process and product quality variables that are not measured frequently.

## References

1 Camacho, E.F. and Bordons, C. (2007). Model-predictive Control, 2e. London, United Kingdom: Springer-Verlag.

2 Lahiri, S.K. (2017). Multivariable Predictive Control: Applications in Industry. New York: Wiley.

3 Stephanopoulos, G. (1983). Chemical Process Control: An Introduction to Theory and Practice. Englewood Cliffs, New Jersey: Prentice-Hall.

4 Cutler, C. R. and Ramaker, B. L. (1979). Dynamic Matrix Control – A Computer Control Algorithm. AIChE National Meeting, Houston, Texas.

5 Liu, Y.A., Chang, A.F., and Pashikanti, K. (2018). Petroleum Refinery Process Modeling: Integrated Optimization Tools and Applications. Weinheim, Germany: Wiley-VCH.

6 Sadeghbeigi, R. (2000). Fluid Catalytic Cracking Handbook: Design, Operation and Troubleshooting of FCC Facilities, 2e. Houston, TX: Gulf Publishing Company.

7 Aspen Technology, Inc. (2016), Training course APC125, “Introduction to Aspen DMC3 Builder: Modeling and Building Controllers for Industrial Processes”.

8 Bristol, E. (1966). On a measure of interaction for multivariable process control. IEEE Transactions on Automatic Control AC-11: 133.

9 McAvoy, T.J. (1983). Interaction Analysis. Research Triangle Park, NC: Instrument Society of America.

10 Smith, C.A. and Corripio, A.B. (1997). Principles and Practice of Automatic Process Control, 2e. New York, NY: Wiley.

11 Zhang, Q., Harmse, M. J., Rasmussen, K., and McIntyre, B. (2007). Methods and Articles for Detecting, Verifying, and Repairing Collinearity in a Model or Subsets of a Model. U.S. patent no. 7,231,264 B2, assigned to Aspen Technology, Cambridge, MA.

12 Stanley, G. (2020) Exponential Filter. Greg Stanley and Associates. https://gregstanleyandassociates.com/whitepapers/FaultDiagnosis/Filtering/ExponentialFilter/exponential-filter.htm (accessed 16 December 2021).

13 Becker, A. (2023) Kalman Filter Tutorial. https://www.kalmanfilter.net/default.aspx (accessed 25 March 2023).

14 Turner, P., Guiver, J., and Lines, B. (2003). Introducing the bounded derivative network for commercial transition control. Proceedings of American Control Conference, Denver, Colorado, June 4-6, p. 5400.

---

<!-- PDF page 566 -->

15 Turner, P. and Guiver, J. (2005). Introducing the bounded derivative network – superceding the application of neural networks in control. International Journal of Control 15: 407.

16 Bindlish, R. (2020). Nonlinear Model-predictive control of an Industrial Process with Steady-State Gain Inversion. Computers & Chemical Engineering 135: 106739.

17 Bausa, J. (2007). Model-based operation of polymer processes – what has to be done? Macromolecular Symposia 259: 42.

18 Jeong, B.-G., Yoo, Y.-K., and Rhee, H.-K. (2001). Nonlinear model-predictive control using a wiener model for a continuous methyl methacrylate polymerization reactor. Industrial & Engineering Chemistry Research 40: 5968.

19 Baughman, D.R. and Liu, Y.A. (1995). Chapter 5 – Forecasting, modeling and control. In: Neural Networks in Bioprocessing and Chemical Engineering. San Diego, CA: Academic Press, Inc.

20 Donat, J.S., Bhat, N., and McAvoy (1991). Neural-net based model-predictive control. International Journal of Control 54: 1453.

21 Kalafatis, A. (2021). Embedding AI in APC – Current Capabilities, Direction and Roadmap. AspenTech Optimize Conference 21 (Virtual) – The Future Starts with Industrial AI. May 21.

22 Kalafatis, A. and Reis, L. (2020). Revolutionize APC Model Building and Make More Accurate Predictions with Embedded AI. AspenTech on-Demand Webinar, December 10. https://www.aspentech.com/en/resources/on-demand-webinars/revolutionize-apc-model-building-and-make-more-accurate-predictions-with-embedded-ai (accessed 22 May 2022).