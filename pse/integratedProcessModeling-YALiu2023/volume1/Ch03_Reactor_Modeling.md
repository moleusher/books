# 3. Reactor Modeling, Convergence Tips, and Data-Fit Tool

<!-- PDF page 135 -->

## Reactor Modeling, Convergence Tips, and Data-Fit Tool

This chapter introduces the three types of kinetic or rate-based reactor models available within Aspen Plus/Polymers for polyolefin manufacturing, including continuous stirred-tank reactor (RCSTR), plug-flow reactor (RPLUG), and batch or semi-batch reactor (RBATCH). We focus on configurations and specifications of the three kinetic reactors in Sections 3.2–3.4, and on the representation of nonideal reactors in Section 3.5. We present practical tips to speed up the solution of mass, energy, and polymer-attribute conservation equations and phase-equilibrium calculations in Sections 3.6 and 3.7. Section 3.8 discusses the data-fit tool for regressing all types of simulation parameters, such as reaction kinetics, heat-transfer coefficients, and any accessible model input parameters (including property model parameters). Sections 3.9 and 3.10 cover hands-on workshops applying the data fit for kinetic parameter estimation using time-evolution concentration profile and polymer-attribute values (such as MWN and MWW). The chapter ends with a reference section.

### 3.1 Kinetic or Rate-Based Reactors

Given the reaction kinetics and operating conditions, kinetic reactor models do mass, energy, and polymer-attribute balance calculations. We note that while Aspen Plus also has a fluidized-bed reactor model, this model can only handle conventional reactions and not polymerization kinetics. In Section 3.5 and in Chapters 4–7, we show how to use the RCSTR model to represent fluidized-bed reactors in polyolefin manufacturing. We summarize in Table 3.1 the key assumptions of the kinetic or rate-based reactors available in Aspen Plus/Polymers.

### 3.2 Continuous Stirred-Tank Reactor Model (RCSTR)

#### 3.2.1 RCSTR Configurations

We use RCSTR in our slurry HDPE process in Chapter 5. A CSTR model can have a single or multiple feeds. Depending on the valid phases that we set, the model can

---

<!-- PDF page 136 -->

<div style="text-align: center;">Table 3.1 Assumptions of kinetic reactors in Aspen Plus/Polymers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reactor type</td><td style='text-align: center; word-wrap: break-word;'>Assumptions</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RCSTR</td><td style='text-align: center; word-wrap: break-word;'>Ideal mixing; homogeneous concentrations inside the reactor; constant temperature and pressure; phase equilibrium</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RPLUG</td><td style='text-align: center; word-wrap: break-word;'>Ideal plug flow of fluids without backmixing; homogeneous in the radial direction; phase equilibrium; allows co-current or countercurrent heating</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RBATCH</td><td style='text-align: center; word-wrap: break-word;'>Ideal mixing; homogeneous concentrations; constant temperature; constant pressure at each time step; phase equilibrium; permit a single charge or time-varying feeds; feed and product stream conditions are time-averaged</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FluidBed</td><td style='text-align: center; word-wrap: break-word;'>Ideal solid mixing; plug-flow vapor phase; homogeneous in the radial direction; continuous feeds of vapor and solids</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_522_815_771.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 3.1 RCSTR configurations.</div>


have a single liquid or vapor product (valid phases = liquid only or vapor only), a vapor product and a liquid product (valid phases = vapor–liquid), or a vapor product and two liquid products (valid phases = vapor–liquid–liquid). Figure 3.1 illustrates these configurations, in which we can replace the single feed with multiple feeds. Note for RCSTR3, we have added the optional input and output "heat" streams. Figure 3.2 shows where we set the valid phases and key components of the second liquid phase.

#### 3.2.2 RCSTR Specifications

Figure 3.3 illustrates the specifications of a CSTR D201 in Workshop 5.1 for a slurry HDPE process.

For operating pressure, we can specify an exit pressure (value positive) or a pressure drop (value zero or negative), and we can enter an exit temperature or a reactor heat duty. For phase, we can specify vapor phase or condensed phase. This chosen phase determines the specification type for the holdup input. Specifically, we may select one of seven types: (1) reactor volume, (2) residence time, (3) reactor volume

---

<!-- PDF page 137 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_146_714_474.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 3.2 Specification of valid phases and key components of second liquid phase.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_536_713_793.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 3.3 Specifications of a RCSTR.</div>


and phase volume, (4) reactor volume and phase volume fraction, (5) reactor volume and phase residence time, (6) residence time and phase volume fraction, and (7) phase residence time and volume fraction. We will demonstrate the specifications of kinetics and component attributes beginning in Chapter 4, and RCSTR convergence tips in Section 3.5.

### 3.3 Plug-Flow Reactor Model (RPLUG)

#### 3.3.1 RPLUG Configurations

We use RPLUG in our high-pressure low-density polyethylene (LDPE) process and ethylene-vinyl acetate (EVA) copolymer process in Chapter 4. Figure 3.4 illustrates a RPLUG configuration with valid phases of vapor-liquid-liquid. To specify the valid phases, follow the path: Simulation → Setup → Global settings → Valid phases → Vapor-liquid-liquid. We follow the same path when specifying the valid phases for RPLUG to be vapor only, liquid only, or vapor-liquid.

---

<!-- PDF page 138 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_144_813_386.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 3.4 RPLUG configuration with heat-transfer fluid (HTFL).</div>


A distinct feature of the RPLUG model is the ability to use a heat-transfer fluid (HTFL) or a thermal fluid. We see in Figure 3.4 the inlet and outlet HTFL streams, HTFLIN and HTFLOUT.

#### 3.3.2 RPLUG Specifications

Following the path: Simulation → Blocks → RPLUG → Setup → Reactor type→, we see the following options available to a thermal fluid in Figure 3.5:

For RPLUG with a thermal fluid, we see five possible options: (1) constant thermal fluid temperature; (2) co-current thermal fluid; (3) counter-current thermal fluid; (4) specified thermal fluid temperature along the reactor length; and (5) specified external heat flux profile. In the figure, we also see two common reactor types: (1) constant specified temperature and (2) adiabatic reactor. For a RPLUG with a co-current or counter-current thermal fluid, Figure 3.6 shows two additional specifications: (1) heat-transfer coefficient of the thermal fluid and (2) thermal fluid outlet temperature. In Chapter 4, we use the RPLUG model with a thermal fluid in the simulation of a high-pressure LDPE process with tabular reactors.

Next, we see the configuration specifications in Figure 3.7.

The Streams folder specifies the products, with VAPOR being vapor phase, LIQ-UID1 being first liquid phase, and LIQUID2 being second liquid phase. We will give the details of Reaction specifications beginning in Chapter 4. The Pressure folder specifies the pressure at reactor inlet and the pressure drop. For the Holdup folder, we typically stay with the default condition, assuming no slip between phases.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1055_720_1222.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.5 Available reactor types for RPLUG.</div>


---

<!-- PDF page 139 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_689_309.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.6 Specifications of heat-transfer parameter and thermal fluid outlet temperature.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_389_689_642.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.7 Configuration specifications of the RPLUG.</div>


### 3.4 Batch Reactor Model (RBATCH)

#### 3.4.1 RBATCH Configuration

The RBATCH model can simulate a batch or a semi-batch operation. We use RBATCH in our SBS (styrene-butadiene-styrene rubber) process in Chapter 6. Figure 3.8 shows a RBATCH configuration. In the figure, BCHARGE represents a single batch charge stream (required). CFEEDs represents one or more continuous feed streams for semi-batch operation (optional). Product represents a single product stream (required). VENT represents a vent stream for semi-batch operation (optional). There is no inlet heat stream, and an optional outlet heat stream is allowed.

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_1051_642_1221.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">Figure 3.8 RBATCH configuration.</div>


---

<!-- PDF page 140 -->

RBATCH performs mass, energy, and polymer-attribute conservation calculations around an ideal batch reactor, assuming known reaction kinetics and the reactor contents to be well-mixed.

#### 3.4.2 RBATCH Specifications

Figure 3.9 illustrates the six options for reactor-operating specifications. Choosing each option will lead to additional required specifications: (1) constant temperature – operating temperature; (2) temperature profile – time versus operating temperature; (3) constant heat duty – heat duty; (4) heat duty profile – time versus heat duty; (5) constant thermal fluid temperature – thermal fluid temperature, overall heat-transfer coefficient, and heat-transfer area; and (6) heat-transfer user routine – see an example for specifying a heat-transfer user routine in Chapter 4 for our high-pressure LDPE reactor (which is a continuous reactor but with essentially similar user subroutine specifications).

In the figure, we see the pressure specification. Three options are available: (1) specify reactor pressure; (2) specify reactor profile (time versus operating pressure); and (3) calculate reactor pressure. Figure 3.10 illustrates the temperature profile, "calculate reactor pressure" specification, and valid phases. We need to provide the reactor volume to calculate the reactor pressure. When allowing a vent stream during a semi-batch operation, we specify a vent-opening pressure together with the reactor volume. In the figure, we also see the specification folders for "Stop Criteria,"

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_725_720_913.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.9 Six options for RBATCH-operating specifications.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_984_809_1198.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 3.10 Temperature profile, "Calculate reactor pressure" specification, and valid phases.</div>


---

<!-- PDF page 141 -->

“Operating Times,” and “Continuous Feeds,” which we will illustrate in detail in our SBS process in Chapter 6. See Table 6.13 and Figures 6.79a–6.79c.

Lastly, we see the specification folder of “Controllers” in Figure 3.10. RBATCH performs controller-calculations if temperature or temperature profile is specified and the reactor is semi-batch with continuous feeds, has vapor and liquid phases, and is venting with constant volume. A search of “RBATCH controllers” in the Aspen Plus online help gives details of the PID (proportional-integral-derivative) controllers for reactor temperature and pressure. We discuss controller specifications and tuning in detail in Chapter 7.

### 3.5 Representation of Nonideal Reactors

This section gives examples where we can use the RCSTR model to represent non-ideal reactors in the industrial manufacturing of polyolefins.

In Section 5.6.4, we discuss the role of solid polymer in phase-equilibrium calculations using a slurry HDPE process as an example. We assume that the polymer is dissolved in the liquid phase with the solvent, as would be the case in solution polymerization of ethylene, where the reactor temperature would be above the melting point of the polymer. Although this modeling simplification does not represent the physical picture of what is happening in the slurry polymerization of ethylene, the effect of it on thermodynamic modeling is relatively small. Figure 5.25 illustrates the difference between the actual conditions and the modeling assumption [1].

In Section 5.7.3, we discuss in detail the modeling of a horizontal stirred-bed reactor for a gas-phase PP process using a series of four RCSTRs [2]. See Figure 5.50. Experimental studies on the residence-time distribution (RTD) of polymers produced in horizontal stirred-bed reactors suggest that the polymer RTD is equivalent to that produced by three to five CSTRs [3].

Figure 5.8 shows a Univation UNIPOL LLDPE process using a fluidized-bed reactor. Current practice is to model UNIPOL and similar fluid-bed reactors as RCSTRs in Aspen Plus. The fluidizing solid polymer phase behaves like a fluid from a phase-equilibrium point of view. Referring to Figure 3.3, we need to specify the volume holdup of the condensed phase based on the known inventory of solids in the bed.

### 3.6 RCSTR Convergence

Figure 3.11 shows the RCSTR convergence scheme shown in the Aspen Plus online help. We follow this figure and discuss the details of each step below.

#### 3.6.1 Initialization

To initialize the mass, energy, and polymer-attribute conservation calculations, the default method used is called the solver method. Specifically, RCSTR sets

---

<!-- PDF page 142 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_145_806_391.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 3.11 Convergence scheme of RCSTR.</div>


outlet stream equal to inlet stream or uses specified estimates of temperature, component flow rates, and attribute values to initialize the RCSTR block, unless previously converged results are available. RCSTR then solves the mass, energy, and polymer-attribute conservation equations using a trial-and-error technique based on the initial guess.

An alternative initialization scheme is the integrator method, in which RCSTR numerically integrates the mass, energy, and polymer-attribute conservation equations from an initial condition to the steady-state condition. By default, the initial condition refers to setting the outlet stream equal to the inlet stream, temperature equal to the specified temperature, or heat duty equal to the specified heat duty. When using this method, we do not supply estimates of component flow rates and attribute values.

We follow the path: Simulation → Blocks → RCSTR Block → Convergence → Parameter → Initialization → Choose: (1) Do not use integration; (2) Always use integration; or (3) Initialize using integration. See Figure 3.12.

Aspen Plus online help suggests that “numerical integration is more reliable than trial-and-error solvers.” Therefore, when troubleshooting mass balance convergence problems, consider deleting initial estimates and initializing using integration.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_991_790_1221.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 3.12 An illustration of initialization options.</div>


---

<!-- PDF page 143 -->

#### 3.6.2 Scaling Factors

Scaling factors have a strong influence on the RCSTR convergence behavior. Basically, Aspen Plus uses numerical solvers to solve the mass, energy, and polymer-attribute conservation equations and to converge on recycle loop calculations in the kinetic reactors, including RCSTR. The solver algorithms use scaled variables. Ideally, the scale factors for each type of variable should be on the same order of magnitude as the variable itself (e.g. mass fraction from 0 to 1; polymer-attribute MWN from 5000 to 60,000). In other words, the solvers work best when the scaled variables are close to unity. We note that if the scaling factors are large and the variables are small, then the model will be loosely converged; if the scaling factors are small and the variables are large, then the convergence criteria would be unacceptably tight, leading to model convergence failure.

Clicking on “Advanced Parameters” button displayed in Figure 3.13 leads us to two scaling parameter options: component-based and substream-based. Interested readers may search in Aspen Plus online help for “Component Attributes Scale Factors” for additional details. For substream-based scaling, search for “Substream Mixed and Stream Class CONVEN” to understand how Aspen Plus arranges component mole flows, total mole flow rate, temperature, pressure, mass enthalpy, ... component attributes for polymer (e.g. SFRAC, MWN, MWW, and PDI), into a substream vector MIXED for conventional components.

Table 3.2 lists the guidelines for how Aspen Plus determines the scaling factors by the RCSTR component-based and substream-based methods. Note the trace scaling factor displayed in Figure 3.12. When this factor equals 1, both component-based and substream-based scaling methods are identical.

#### 3.6.3 Residence Time Loop

In Figure 3.3, we have provided the reactor volume and phase volume. If we choose to specify the residence time instead of volume, RCSTR adjusts the volume

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_892_688_1220.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.13 Scaling parameter options: component-based and substream-based.</div>


---

<!-- PDF page 144 -->

<div style="text-align: center;">Table 3.2 Guidelines for RCSTR component-based and substream-based scaling factors.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Variable type</td><td style='text-align: center; word-wrap: break-word;'>Component-based scaling</td><td style='text-align: center; word-wrap: break-word;'>Substream-based scaling</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Enthalpy</td><td style='text-align: center; word-wrap: break-word;'>Estimated outlet stream enthalpy</td><td style='text-align: center; word-wrap: break-word;'>10E5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Component mole flows</td><td style='text-align: center; word-wrap: break-word;'>The larger of: (1) Estimated mole flow in the outlet stream; (2) (Trace scaling factor between 0 and 1)*(Total estimated flow rate of the outlet stream)</td><td style='text-align: center; word-wrap: break-word;'>Total estimated mole flow rate of the outlet stream</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Conserved polymer attributes</td><td style='text-align: center; word-wrap: break-word;'>The larger of: (1) Estimates value in the outlet stream; (2) (Default attribute scaling factor)*(Estimated component mole flow); and (3) (Trace scaling factor)*(total estimated mole flow)*(default attribute scaling factor)</td><td style='text-align: center; word-wrap: break-word;'>Default attribute scaling factors</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_530_809_764.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 3.14 Reducing the maximum volume step parameter to speed up residence to loop convergence.</div>


to satisfy the residence time specification. We can alleviate the convergence problem in the residence time loop by providing initial volume estimates. We follow the path: RCSTR → Convergence → Estimates → Volume: fill in estimates of reactor volume. If convergence problems persist, we change the maximum volume step by following the path: RCSTR → Convergence → Parameters → Volume Convergence → Maximum Volume Step → Reduce from 1 to a smaller value. See Figure 3.14.

When troubleshooting convergence problems, Aspen Online Help recommends that we simplify the problem by specifying temperature and volume, instead of heat duty and residence time.

#### 3.6.4 Energy Balance Loop

In the energy balance loop, RCSTR adjusts the reactor temperature to match the specified reactor heat duty. If we specify the reactor temperature instead of the reactor heat duty, RCSTR will bypass this loop, and move on to the mass balance loop, thus greatly simplifying the mass and energy balance calculations. This also suggests that when it is feasible, simply perform the RCSTR (and RPLUG and

---

<!-- PDF page 145 -->

RBATCH) calculations by specifying the reactor temperature, instead of heat duty or heat-transfer parameters (thermal fluid temperature, overall heat-transfer coefficient, or thermal fluid stream).

We note that the reaction rates are sensitive to temperature, and any large changes in the reactor temperature may cause the energy balance loop to diverge.

If we follow the path to specify both pressure and heat duty as the reactor-operating conditions: Simulation → Blocks → RCSTR → Setup → Operating conditions → specify pressure and heat duty, we may avoid reactor convergence problem by providing a good temperature estimate. We do this by following the path: Simulation → Blocks → RCSTR → Convergence → Estimates → Temperature: fill in the estimate. If the convergence problem persists, we could reduce the maximum temperature step size from the default of 50°C to a smaller value. See Figure 3.15.

#### 3.6.5 Mass Balance Loop

RCSTR has two solvers to converge the mass, energy, and polymer-attribute conservation equations for component mole flow and conserved component attributes (e.g. SFRAC, MWN, and MWW): (1) the Broyden algorithm tends to be relatively fast but may be unstable if the number of components and attributes is large and the reaction rates are high; and (2) the Newton algorithm tends to be slower but more stable for many classes of problems.

Before we talk about the number of mass balance iterations to achieve convergence for each algorithm, let us see Figure 3.16 and understand the concept of damping [4]. Process simulation software tools typically include provisions to apply a damping factor to reduce the ratio of the root-mean-squared (RMS) error of process variables to the error tolerance to less than 1 within a finite number of iterations and thus achieve convergence. This figure illustrates how this ratio reduces to less than 1 (i.e.  $ 10^{0} $) within a finite number of iterations in a well-damped system after applying a damping factor, and how this ratio grows in an under-damped system.

Figure 3.17 shows that the default number of iterations for the mass balance convergence solver, the Broyden algorithm, is 50. This default is sufficient for the Newton algorithm but is usually too small for the Broyden algorithm. This is illustrated in Figure 3.17, where Aspen Plus online help recommends increasing the number of iterations for the Broyden algorithm for polymer process simulation to at least 500 and applying a small damping factor between 0.1 and 0.001 (accessed by clicking on the "Advanced Parameters" button displayed in the figure).

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1087_737_1246.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3.15 Energy-balance convergence: reducing the maximum temperature step size.</div>


---

<!-- PDF page 146 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Iterations</th><th style='text-align: center;'>Under-damped system</th><th style='text-align: center;'>Well-damped system</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3.16 An illustration of the concept of damping.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_367_562_758.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">Figure 3.17 Setting the maximum number of iterations for the Broyden algorithm to 500 and adding a small damping factor on mass balance variables between 0.1 and 0.001.</div>


When using the Newton algorithm for mass balance iterations, apply a stabilization strategy to specify the method used to stabilize the Newton algorithm. There are two options: (1) dogleg strategy (default) that uses Powell's dogleg strategy in optimization theory to combine Newton and steepest descent directions; and (2) line search strategy that uses one-dimensional search along Newton direction. Line search is recommended for polymerization kinetics and systems where reaction rates are sensitive to the concentrations of trace species, which are also reacting (such as reacting catalysts or inhibitors). Changing the stabilization strategy within "Newton Parameters" from "dogleg" to "line search" could improve the convergence behavior, especially for ionic and Ziegler–Natta polymerization kinetics. See Figure 3.18.

#### 3.6.6 Flash Loop

As illustrated in Figure 3.11, we see from the bottom up that the flash loop is the innermost loop, while the energy balance loop and the residence time loop represent the outer loops. The flash loop does the phase-equilibrium calculations. It is

---

<!-- PDF page 147 -->

<div style="text-align: center;">Figure 3.18 Changing the stabilization strategy to “line search” to improve mass balance convergence.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_400_149_796_476.jpg" alt="Image" width="41%" /></div>


essential to have accurate physical properties over the entire range of temperatures and pressures found in the process. When we see the message of “initial flash failure” in the control panel, this is likely the result of a physical property problem. Check the heat of formation (DHFORM) and the ideal gas heat capacity (CPIG) of the polymer and oligomer components. If these property values are missing, apply the property estimation methods of Chapter 2 (see Section 2.7). If a supercritical component (light gases and low-molecular-weight hydrocarbons) is present, consider treating them as Henry components when using the POLYNRTL property method (see Section 2.2.5). When flash failures appear during the mass balance loop, change the parameters of flash options by following the path:

Simulation → Blocks → RCSTR → Convergence → Flash options → Increase “maximum iterations” to 200 and decrease flash tolerance to less than 0.0001.

#### 3.6.7 Recommendation for RCSTR Mass Balance Algorithm for Polyolefin Process Simulation

Table 3.3 summarizes the recommended RCSTR mass balance convergence algorithms for polyolefin process simulation.

<div style="text-align: center;">Table 3.3 Recommendations for RCSTR mass balance convergence algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Polyolefin Polymerization Kinetics</td><td style='text-align: center; word-wrap: break-word;'>RCSTR Mass-balance Convergence Algorithm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Free-radical polymerization (Chapter 4: LDPE, EVA; Chapter 7, PS)</td><td style='text-align: center; word-wrap: break-word;'>Use Broyden for homopolymerization, assuming pseudo steady-state approximation (PSSA); otherwise, use Newton</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Ziegler-Natta polymerization (Chapter 5: HDPE, PP, LLDPE); and ionic polymerization (Chapter 7: SBS)</td><td style='text-align: center; word-wrap: break-word;'>Use Newton with estimates. If this fails, initialize with integration. Reduce the default trace scaling factor of 0.0001 (see Figure 3.12) by a factor of 10 if trouble persists. Change the stabilization strategy from “dogleg” to “line search”</td></tr></table>

---

<!-- PDF page 148 -->

### 3.7 RPLUG/RBATCH Model Convergence

The convergence calculations of both RPLUG and RBATCH are essentially similar. They use a variable-step Gear integration scheme [5] to solve the mass, energy, and polymer-attribute conservation equations. For RPLUG, we integrate along the reactor length, and for RBATCH, we integrate along the time axis. Figure 3.19 shows the identical “flash options” for both RPLUG and RBATCH.

Figure 3.20 illustrates the “integration loop” of RPLUG.

For both RPLUG and RBATCH, the solver algorithm for mass, energy, and polymer-attribute conservation calculations is called the corrector. Two corrector methods are available to RPLUG and RBATCH: (1) Direct – direct substitution method and (2) Newton method. In general, the Newton method has the best performance with polymerization kinetics, but for problems with a large number of variables, the direct method is faster. Aspen Plus online help suggests trying both methods to see which is faster for a specific problem.

In Figure 3.20, we see an “initial step size of integration variables” of 0.01. If the solver cannot converge the equations with this step size, it will cut the step size by a factor of 10. This process will repeat up to six times. If the solver still cannot converge, the reactor calculation fails with an error message “solver cannot converge with

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_654_720_840.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 3.19 Flash options for both RPLUG and RBATCH.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_909_766_1219.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3.20 Integration loop of RPLUG.</div>


---

<!-- PDF page 149 -->

minimum step size." When this occurs, we recommend reducing the initial step size to as low as 1E-4.

Figure 3.20 also shows a “maximum number of integration steps” for a default value of 1000. For kinetics with fast reactions involving trace components, especially when the corrector uses the direct substitution method, Aspen Plus online help recommends increasing the maximum number of integration steps from 1000 to 5000. If more than 5000 steps are required for convergence, try replacing the corrector method to Newton.

We see in Figure 3.20 that for RPLUG, there is a default “error tolerance ratio” of 0.1. This means that the corrector tolerance is 1E-5, that is, 0.1 times the integration convergence tolerance (set at 0.0001). For some problems, especially those involving RPLUG with heat-transfer calculations, the error tolerance ratio may be higher than 0.1, but it should always be less than 1. For RBATCH, we do not see the entry of error tolerance ratio within the integration loop, but it has a hidden default value of 0.1.

Like RCSTR, RPLUG and RBATCH solve the mass, energy, and polymer-attribute conservation equations using scale factors discussed in Section 3.6.2. In Figure 3.20, we see the entry of error-scaling method. Both RPLUG and RBATCH have two options: (1) Static scaling factors based on the feed stream conditions, which are held constant throughout the integration process; and (2) Dynamic scaling factors, which are updated at each integration step based on previous variable values. In Figure 3.20, we see in the integration loop of RPLUG an entry for “minimum scale factor” with a default value of 1E-10. When running RPLUG simulation, we may encounter the error message “integration error: maximum number of integration steps is reached.” This may happen with dynamic scaling when a variable value becomes so small that a small absolute error becomes a large scaled error. The solution is to increase the minimum scale factor from the default value of 1E-10 to 1E-5.

This concludes our general discussion of guidelines for reactor convergence tips. In Chapters 4–7, we illustrate the applications of these guidelines to specific industrial polymerization reactors with different polymerization kinetics and discuss the practical guidelines for flowsheet convergence involving reactors, separators, and other units.

### 3.8 Data Fit (Simulation Data Regression)

In Section 2.7, we discussed the data regression (DRS) tool to estimate thermophysical properties and pure-component and binary interaction parameters for property methods. Aspen Plus has another useful tool for simulation data regression called data fit. We can use it to: (1) estimate unknown model parameters (e.g. reaction kinetic parameters, heat-transfer coefficients, and separation efficiencies); (2) reconcile measured data; and (3) estimate unknown model parameters and reconcile measured data simultaneously.

Data fit is an efficient nonlinear regression tool that allows the user to determine statistically acceptable model parameters from constant, time-varying, or

---

<!-- PDF page 150 -->

temperature-dependent laboratory measurements or from matching the process simulation to plant targets. We can use either point data or time-profile data for regression. We need to define the data with reconciled input variables and a standard deviation. We estimate the model parameters using the data within the specified range [6].

The least-square regression objective function that the data fit minimizes is as follows:

 $$ f=\min_{X_{\mathrm{p}},X_{\mathrm{ri}}}\frac{1}{2}\sum_{i=1}^{N_{\mathrm{set}}}\left(W_{i}\times\left(\sum_{j=1}^{N_{\mathrm{expi}}}\left(\sum_{i=1}^{N_{\mathrm{ri}}}\left(\frac{X_{\mathrm{mri}}-X_{\mathrm{ri}}}{\sigma_{X_{\mathrm{mri}}}}\right)^{2}+\sum_{m=1}^{N_{\mathrm{rr}}}\left(\frac{X_{\mathrm{mrr}}-X_{\mathrm{rr}}}{\sigma_{X_{\mathrm{mr}}}}\right)^{2}\right)\right)\right) $$ 

subject to

 $$ X_{\mathrm{p l b}}\leq X_{\mathrm{p}}\leq X_{\mathrm{p u b}},\quad X_{\mathrm{r i l b}}\leq X_{\mathrm{r i}}\leq X_{\mathrm{r i u b}} $$ 

where:

 $ N_{set} = \text{number of datasets specified for regression} $
 $ N_{expi} = \text{number of experiments in dataset } i $
 $ N_{ri} = \text{number of reconciled input variables} $
 $ N_{rr} = \text{number of measure output variables} $
 $ W_{i} = \text{weight for each dataset } i \text{ for regression} $
 $ X_{p} = \text{vector of varied parameters} $
 $ X_{mri} = \text{measured values of the reconciled input variables} $
 $ X_{ri} = \text{calculated values of the reconciled input variables} $
 $ X_{mrt} = \text{measured values of the output variables} $
 $ X_{rr} = \text{calculated values of the output variables} $
 $ \sigma = \text{standard deviation specified for the measured variables} $

Since the model parameter estimation is a complex regression problem, we can vary some numerical parameters within the data fit to speed up the convergence calculations. We vary the maximum algorithm iterations and the maximum number of passes through the process flowsheet, which are required to compute the residuals. We specify a bound factor, which gives the upper and lower bounds for variables by multiplying by the standard deviation. We also specify the absolute sum of squares objective function tolerance so that the problem converges whenever the objective function value is less than the tolerance value.

The tool performs least-square regression using a trust region algorithm for parameter estimation. Specifically, the algorithm maintains an estimate of the diameter of a region, called the trust region, based on the current estimate of the vector of varied values in which it can predict the behavior of the least-squares objective function. If an adequate model is found within the trust region, the region is expanded; if the model is a poor approximation, then the trust region is contracted. The tool also provides certain handles to implement the regression with the trust region optimization algorithm.

---

<!-- PDF page 151 -->

#### 3.9 Workshop 3.1: Data Fit of Kinetic Parameters for Styrene Polymerization Using Concentration Profile Data

#### 3.9.1 Objective

The objective of this workshop is to demonstrate the steps involved in applying data-fit tool to regress kinetic parameters for simplified styrene bulk polymerization by thermal initiation [7, 8]. This is an example of free radical polymerization, which we discuss in detail in Chapter 4 for LDPE and EVA copolymer, and in Chapter 6 for polystyrene (PS). For this workshop, we begin with a simplified simulation model for PS, explain the completed steps, and then demonstrate the step-by-step application of the data-fit tool in order to regress the kinetic parameters of the polymerization reactions based on time-dependent evolution of PS concentration in a batch reactor. Our starting simulation file for the workshop is WS 3.1 Data Fit_Profile Data_PS.bkp.

#### 3.9.2 A Simplified Kinetic Model for Styrene Polymerization

We open the starting simulation file and go to the Properties environment. The Setup folder shows that this example uses a unit set METCBAR built from a MET unit set by changing the temperature unit from K to °C and the pressure unit from atm to bar, as demonstrated previously in Figure 1.7a.

Next, we go to the Components folder displaying the components in Figure 3.21.

Here, STY and STE-SEG are styrene monomer and styrene segment (repeat type). PS is the polystyrene product. INIT is the chain initiator, di-t-butyl-peroxide (DTBP), which is available within the Aspen Polymers initiator databank. CINI is a co-initiator, which is a hypothetical component required to activate the thermal initiator reaction in the free radical polymerization kinetic model of Aspen Polymers. EB (ethylbenzene) is a chain-transfer agent to control the molecular weight. INHIBIT is an inhibitor, which is represented by STY.

We click on the “Enterprise Database” button shown in Figure 3.21 to ensure that we have included databanks for pure components, segments, polymers, and initiators for this example. See Figure 3.22.

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1021_617_1222.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 3.21 Component specifications.</div>


---

<!-- PDF page 152 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_149_646_310.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 3.22 Specified enterprise databases.</div>


Next, we follow the path: Properties → Components → Polymers → (1) Segments: segment ID = STY-SEG, type = Repeat; and (2) Polymers: Polymer ID: Choose “PS”; Built-in attribute group: Choose “Free radical selection.”

This workshop uses the POLYNRTL property method discussed in Section 2.2.4. Follow the path: Properties → Methods → Specifications → Global → Method name: Choose POLYNRTL.

Next, we click on the “Review” button displayed at the bottom of Figure 3.21 to call up the pure-component parameters. We see the resulting pure-component parameters by following the path: Properties → Methods → Parameters → Pure Components.

To ensure that PS has an extremely small liquid vapor pressure and does not vaporize, we enter the first temperature-dependent parameter for the extended Antoine correlation for liquid vapor pressure (PLXANT-1) for PS as -40. See Figure 3.23. To see the specific equation for the PLXANT correlation, click on the "Help" button displayed in Figure 3.23 to see the extended Antoine correlation.

Following Section 2.3, Workshop 2.1, we estimate all the missing binary interaction parameters for the POLYNRTL model using the UNIFAC group-contribution method. We follow the path to see the estimated parameters: Properties → Methods → Parameter → Binary Interactions → NRTL-1 (see Figure 3.24). After this estimation, we follow the path to discontinue this estimation step in the next simulation: Properties → Estimation → Input → Setup → Estimation options: choose "Do not estimate any parameters."

Next, we go to the simulation environment and see the flowsheet of the RBATCH reactor in Figure 3.25.

The FEED stream is at 100°C and 4.5 bar, and the component mass flow rates (kg/hr) are: STY = 1000; INIT = CINIT = 1; EB = 5; and INHIBIT = 0.5.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_1047_791_1222.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 3.23 Specification of user parameter for liquid vapor pressure correlation for PS.</div>


---

<!-- PDF page 153 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_147_778_389.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 3.24 Estimated POLYNRTL binary interaction parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_131_457_660_703.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 3.25 RBATCH reactor for WS 3.1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_774_618_996.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 3.26 Reaction species specifications.</div>


We discuss in more detail in Chapter 4 about the kinetics of free radical polymerization. To create our reaction set, we follow the path: Simulation → Reactions → New → Create New ID → Enter ID = R-1; Select Type: Free-Rad → OK → Species specification →. See Figure 3.26.

For this workshop, we generate the reactions by following the path: Simulation → Reactions → Reaction R-1a → Species specification (Figure 3.2) → Reactions → Click on “Generate Reactions” button → Nine reactions listed in Figure 3.27, which include: (1) initiator decomposition (Init-Dec); (2) special thermal initiation

---

<!-- PDF page 154 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_147_808_333.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 3.27 The generated reaction set for styrene polymerization by thermal initiation.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_418_809_619.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 3.28 Initial rate constants for WS 3.1.</div>


(Init-Sp); (3) chain initiation (Chain-Ini); (4) chain propagation (Propagation); (5) chain transfer to monomer (Chat-Mon); (6) chain transfer to chain-transfer agent (Chain-Agent); (7) termination by disproportionation (Term-Dis); (8) chain termination by combination (Term-Comb); and (9) inhibition by inhibition agent (Inhibition).

In Section 4.2, we will give detailed explanations of each type of free radical reaction. For the current workshop, we focus only on a simplified reaction set by deleting reactions 1 and 7 and entering the initial set of rate constants as the initial values for kinetic parameter regression by the data-fit tool. Figure 3.28 shows the initial rate constants for the remaining seven reactions.

We note that the reaction rate constants listed in Figure 3.28 have the following standard Arrhenius form:

 $$ k=k_{0}*\mathrm{e}^{-\frac{E}{R}\left(\frac{1}{T}-\frac{1}{T_{\mathrm{r}}}\right)} $$ 

where  $ k_{0} $ is the pre-exponential factor, E is the activation energy, R is the ideal gas constant, T is the temperature of the reaction system, and  $ T_{r} $ is the reference temperature.

#### 3.9.3 Datasets

Our isothermal experimental data from RBATCH include the time evolution of the liquid-phase mass fraction of PS (PSFRAC). See Table 3.4.

---

<!-- PDF page 155 -->

<div style="text-align: center;">Table 3.4 Time evolution of liquid-phase mass fraction of PS.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Data Set</td><td style='text-align: center; word-wrap: break-word;'>PS1</td><td style='text-align: center; word-wrap: break-word;'>PS2</td><td style='text-align: center; word-wrap: break-word;'>PS3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Time (hr)</td><td style='text-align: center; word-wrap: break-word;'>PSFRAC</td><td style='text-align: center; word-wrap: break-word;'>PSFRAC</td><td style='text-align: center; word-wrap: break-word;'>PSFRAC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.00799</td><td style='text-align: center; word-wrap: break-word;'>0.000366</td><td style='text-align: center; word-wrap: break-word;'>0.00041</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.015</td><td style='text-align: center; word-wrap: break-word;'>0.000806</td><td style='text-align: center; word-wrap: break-word;'>0.000861</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>0.0227</td><td style='text-align: center; word-wrap: break-word;'>0.00123</td><td style='text-align: center; word-wrap: break-word;'>0.00127</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0.0316</td><td style='text-align: center; word-wrap: break-word;'>0.00163</td><td style='text-align: center; word-wrap: break-word;'>0.00178</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.5</td><td style='text-align: center; word-wrap: break-word;'>0.038</td><td style='text-align: center; word-wrap: break-word;'>0.00211</td><td style='text-align: center; word-wrap: break-word;'>0.00205</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0.0466</td><td style='text-align: center; word-wrap: break-word;'>0.00249</td><td style='text-align: center; word-wrap: break-word;'>0.00265</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.5</td><td style='text-align: center; word-wrap: break-word;'>0.0506</td><td style='text-align: center; word-wrap: break-word;'>0.00294</td><td style='text-align: center; word-wrap: break-word;'>0.00304</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0.061</td><td style='text-align: center; word-wrap: break-word;'>0.0033</td><td style='text-align: center; word-wrap: break-word;'>0.00358</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4.5</td><td style='text-align: center; word-wrap: break-word;'>0.064</td><td style='text-align: center; word-wrap: break-word;'>0.00388</td><td style='text-align: center; word-wrap: break-word;'>0.00389</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>0.0759</td><td style='text-align: center; word-wrap: break-word;'>0.0043</td><td style='text-align: center; word-wrap: break-word;'>0.0046</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_632_635_804.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 3.29 Defining the time evolution of the liquid-phase mass fraction of PS as dataset PS1.</div>


We create the datasets by following the path: Simulation → Model Analysis Tools → Data Fit → Dataset → New → Enter ID = PS1; Select type = Profile-data → OK → (1) Define: See Figure 3.29; (2) Data: See Figure 3.30 for dataset PS1 in Table 3.4. Repeat this path to enter datasets PS2 and PS3.

#### 3.9.4 Simulation Data Regression (Data Fit)

To define a simulation-regression run, we follow the path: Simulation → Model Analysis Tools → Data Fit → Regression → New → Enter ID: R-1 → OK → Specifications: (1) Active: yes; (2) Select datasets to be regressed: PS1, PS2, and PS3; (2) Vary: New → See Figure 3.31. Variable 1 (ISPRE-EXP, pre-exponential factor for special initiation reaction); Variable 2 (ISACT-Energy, activation energy of special initiation reaction); Variable 3 (INPRE-EXP, pre-exponential factor of inhibition reaction). Define Variable 2 and Variable 3 in the same way as Variable 1.

---

<!-- PDF page 156 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_600_412.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 3.30 Dataset PS1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_483_766_777.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3.31 Manipulated variables ("Vary") of simulation data regression R-1.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_849_766_1084.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3.32 Default convergence parameters for data fit.</div>


<div style="text-align: center;">Figure 3.32 shows the default convergence parameters for data fit:</div>


(1) Maximum algorithm iterations: Controls the number of regression iterations. Fifty runs are more than enough (the current run converges in five iterations).

---

<!-- PDF page 157 -->

(2) Maximum passes through the flowsheet: For problems with many variables and experiments, increase the number of passes.

(3) Absolute (objective) function tolerance: Usually the default value of 0.01 is too low.

(4) Relative function tolerance: Stop iterating when the predicted relative change in the objective function falls below the specified value; the default of 0.002 is very tight. Typically, a value of 0.01 (or 1%) is sufficient.

(5) X convergence tolerance: Stop iterating when the predicted maximum relative change in any variable is below the specified value; the default value of 0.002 is very tight.

(6) Minimum step tolerance: Controls “solution may be suboptimal message.” The default value is very conservative.

We follow the path: Simulation → Model analysis tools → Data fit → Regression → Results → Summary. See Figure 3.33. Here, we look for reasonable improvement from the initial value (14970.5) to the final value (122.333) of the objective function. Theoretically speaking, the statistical value of Chi-square should be less than the 95% confidence critical value; however, this rarely happens in real regressions.

Next, we check the resulting manipulated variables shown in Figure 3.34. Here, we look for tighter bounds between the lower and upper limits of the 95% confidence interval. Wide bounds indicate loose fits. Also, make sure that the estimated value is reasonably larger than the standard deviation.

A review of the iteration history will also give useful insights. Figure 3.35 shows good progress between iterations in terms of the “objective function” value, and of the actual relative difference between the previous and current values of the objective function (called the “delta function”). Interested readers may search Aspen Plus

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_803_735_1050.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3.33 Summary of simulation-regression results.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_1117_657_1221.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 3.34 Estimated manipulated variable values and standard deviations.</div>


---

<!-- PDF page 158 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_686_332.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 3.35 Iteration history of data-fit run.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>61</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>63</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>67</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>69</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>71</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>73</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>77</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>79</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>81</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>83</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>87</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>89</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>91</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>93</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>97</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>99</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>101</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>102</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>103</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>104</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>106</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>107</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>108</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>109</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>111</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>112</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>113</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>114</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>116</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>117</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>118</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>119</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>121</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>122</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>123</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>124</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>126</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>127</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>128</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>129</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>131</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>132</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>133</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>134</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>136</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>137</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>138</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>139</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>141</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>142</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>143</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>144</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>146</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>147</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>148</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>149</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>151</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>152</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>153</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>154</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>156</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>157</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>158</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>159</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>161</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>162</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>163</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>164</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>166</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>167</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>168</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>169</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>171</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>172</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>173</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>174</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>176</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>177</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>178</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>179</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>181</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>182</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>183</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>184</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>185</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>186</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>187</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>188</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>189</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>191</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>192</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>193</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>194</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>195</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>196</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>197</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>198</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>199</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>201</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>202</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>203</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>204</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>205</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>206</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>207</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>208</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>209</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>211</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>212</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>213</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>214</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>215</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>216</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>217</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>218</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>219</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>221</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>222</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>223</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>224</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>226</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>227</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>228</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>229</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>231</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>232</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>233</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>234</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>235</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>236</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>237</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>238</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>239</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>241</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>242</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>243</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>244</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>245</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>246</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>247</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>248</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>249</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>251</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>252</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>253</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>254</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>255</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>256</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>257</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>258</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>259</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>261</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>262</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>263</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>264</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>265</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>266</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>267</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>268</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>269</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>271</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>272</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>273</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>274</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>276</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>277</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>278</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>279</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>281</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>282</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>283</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>284</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>285</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>286</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>287</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>288</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>289</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>291</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>292</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>293</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>294</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>295</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>296</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>297</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>298</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>299</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>301</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>302</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>303</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>304</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>305</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>306</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>307</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>308</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>309</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>311</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>312</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>313</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>314</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>315</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>316</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>317</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>318</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>319</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>321</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>322</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>323</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>324</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>326</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>327</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>328</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>329</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>331</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>332</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>333</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>334</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>335</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>336</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>337</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>338</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>339</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>341</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>342</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>343</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>344</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>345</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>346</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>347</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>348</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>349</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.0000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3.36 The initial plot of estimated value versus measured value. Note the Format options of Squared plot and Diagonal line at the top.</div>


online help for “Data fit regression results iteration history sheet” for explanations of other tabulated results in the figure.

Lastly, we may compare the estimated and measured values by following the path: Regression R-1 → Results → Fitted Data → Plot: Choose Custom. X Axis – estimated values; Y Axis – measured value → OK. See the initial plot in Figure 3.36 → Plot: Format. Choose Squared plot and Diagonal line → see the improved plot in Figure 3.37.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Estimated value</th><th style='text-align: center;'>Measured value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.010</td><td style='text-align: center;'>0.008</td></tr>
    <tr><td style='text-align: center;'>0.020</td><td style='text-align: center;'>0.015</td></tr>
    <tr><td style='text-align: center;'>0.030</td><td style='text-align: center;'>0.029</td></tr>
    <tr><td style='text-align: center;'>0.040</td><td style='text-align: center;'>0.038</td></tr>
    <tr><td style='text-align: center;'>0.050</td><td style='text-align: center;'>0.047</td></tr>
    <tr><td style='text-align: center;'>0.060</td><td style='text-align: center;'>0.060</td></tr>
    <tr><td style='text-align: center;'>0.065</td><td style='text-align: center;'>0.063</td></tr>
    <tr><td style='text-align: center;'>0.070</td><td style='text-align: center;'>0.075</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3.37 Estimated versus measured data.</div>


---

<!-- PDF page 159 -->

This concludes the current workshop. We save the simulation file as WS 3.1 Data Fit_Profile Data_PS.bkp.

#### 3.10 Workshop 3.2: Data Fit of Kinetic Parameters for Styrene Polymerization Using Point Data

#### 3.10.1 Objective

The objective of the current workshop is to continue our previous PS workshop and demonstrate how to apply data-fit tool to regress kinetic parameters for the product stream from the RBATCH reactor to meet the required MWN and MWW values at the end of batch polymerization. The dataset for data-fit run includes only single values of MWN and MWW, which are called point dataset.

We use the same simulation file as WS 3.1 and re-save it as WS 3.2 Data Fit_Point Data_PS.bkp. We follow the path: Simulation → Streams → Product → Result → Component Attributes → MWN = 2792.19, and MWW = 5483.05 (see Figure 3.38). Our task is to find the appropriate pre-exponential factors for rate constants for chain-propagation reaction and chain-transfer-to-monomer reaction to produce a PS product with MWN = 2800 and MWW = 5500.

#### 3.10.2 Dataset

We create the dataset by following the path: Simulation → Model Analysis Tools → Data Fit → Dataset → New → Enter ID = PS4; Select type = Point-data → OK → (1) Define: Variable PSMWN. See Figure 3.39 for MWN of PS product stream; repeat the same step to define variable PSMWW for MWW of PS product stream; (2) Data: See Figure 3.40 for dataset PS4.

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_888_750_1269.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3.38 Product polymer attributes: MWN and MWW values.</div>


---

<!-- PDF page 160 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_743_425.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 3.39 Defining point-data variables PSMWN and PSMWW.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_501_599_643.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 3.40 Specification of point dataset PS4.</div>


#### 3.10.3 Simulation Data Regression (Data Fit)

To define a simulation-regression run, we follow the path: Simulation → Model Analysis Tools → Data Fit → Regression → New → Enter ID: R-2 → OK → Specifications: (1) Active: yes; (2) Select datasets to be regressed: PS4; (2) Vary: New → See Figure 3.41. Variable 1 (PRPRE-EXP, pre-exponential factor for chain propagation); Variable 2 (CMPRE-EXP, pre-exponential factor of chain transfer to monomer). Define Variable 2 in the same way as Variable 1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_947_790_1220.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3.41 Manipulated variables for simulation data regression R-2.</div>


---

<!-- PDF page 161 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_149_711_369.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 3.42 Summary of simulation-regression results.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_431_726_557.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3.43 Estimated manipulated variables and standard deviations.</div>


Before we run regression R-2, we need to deactivate the previous regression run R-1 by following the path: Simulation → Model Analysis Tools → Data Fit → Regression → R-1 → Specifications: Cancel the “Active” entry. We then run regression R-2 through the control panel. Figure 3.42 shows that the regression objective function drops from 355881.6 to 1.09908 within two iterations.

Figure 3.43 illustrates that the standard deviation for the estimated kinetic parameters is large. We note that this is due to the regression of two variables using two datapoints. From a technical standpoint, the regression should be able to perfectly fit the data, and a standard deviation should not exist, but one does exist due to variable 2 being at its lower bound. This workshop is simply a demonstration of how to use the data-fit tool. Real data-fit problems should rely on more datapoints for fitting. For “n” variables, a minimum of “n” datapoints are required, and “n + 1” datapoints are required for a standard deviation to exist. Results that are statistically significant require a number of datapoints that is at least an order of magnitude greater than the number of regressed variables. Figures 3.44 and 3.45 show where you can compare fitted data to regression-estimated data and objective function iteration results.

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1048_727_1218.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3.44 Comparison of measured value and estimated value.</div>


---

<!-- PDF page 162 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_754_316.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3.45 The objective function drops significantly within two iterations.</div>


We conclude the current workshop and save the simulation file as: WS 3.2 Data Fit_Point Data_PS.bkp.

## References

1 Khare, N.P., Seavey, K.C., Liu, Y.A. et al. (2002). Steady-state and dynamic modeling of commercial slurry high-density polyethylene (HDPE) processes. Industrial and Engineering Chemistry Research 41: 5601.

2 Khare, N.P., Lucas, B., Seavey, K.C. et al. (2004). Steady-state and dynamic modeling of gas-phase polypropylene processes using stirred-bed reactors. Industrial and Engineering Chemistry Research 43: 884.

3 Caracotsios, M. (1992). Theoretical modelling of Amoco's gas phase horizontal stirred bed reactor for the manufacturing of polypropylene resins. Chemical Engineering Science 47: 2591.

4 Liu, Y.A., Chang, A.F., and Pashikanti, K. (2018). Petroleum Refinery Process Modeling: Integrated Optimization Tools and Applications, 71. Weinheim: Wiley-VCH.

5 Gear, C.W. (1971). Numerical Initial Value Problems in Ordinary Differential Equations. Englewood Cliffs, NJ: Prentice-Hall.

6 Sharma, N. and Liu, Y.A. (2019). An effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient simulation software tools. Industrial and Engineering Chemistry Research 58: 14209.

7 Aspen Technology, Inc. (2017). Application B1 – Polystyrene Bulk Polymerization by Thermal Initiation. Aspen Polymers V8.4: Examples and Applications, pp. 97–108.

8 Aspen Technology, Inc. (2017). Initiator Decomposition Rate Parameters. Aspen Polymers V8.5 Unit Operation and Reactor Models, pp. 431–444.