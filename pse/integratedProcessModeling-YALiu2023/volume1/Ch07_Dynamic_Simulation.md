# 7. Improved Polymer Process Operability and Control

<!-- PDF page 369 -->

# Improved Polymer Process Operability and Control Through Steady-State and Dynamic Simulation Models

This chapter covers dynamic polymer process modeling using Aspen Plus and Aspen Plus Dynamics. Starting with a steady-state (time-independent) simulation model for a polymer process developed in Aspen Plus, we can convert a steady-state model to a dynamic (time-dependent) simulation model using Aspen Plus Dynamics. This enables the users to create powerful dynamic polymer process simulations for better analysis of process operability and control.

Section 7.1 demonstrates a four-step workflow for dynamic process modeling using Aspen Plus and Aspen Plus Dynamics. For convenience, we use the term Aspen Dynamics, or abbreviation AD, for Aspen Plus Dynamics throughout this chapter. Section 7.2 introduces how to run dynamic simulation in AD. We cover types of dynamic simulations (flow-driven and pressure-driven), graphical interface of AD, simulation run modes and run control, viewing simulation results using predefined tables and plots, specification status and analysis, creating new tables and plots, and variable finding in AD. Section 7.3 discusses process control in AD, including adding and configuring a PID controller. Section 7.4 explains snapshot management and taking a snapshot of simulation inputs and results. Section 7.5 introduces tasks for defining a sequence of discrete events, which are useful for simulating grade changes in polyolefin production. Section 7.6 presents a workshop, dynamic simulation and grade change of a slurry high-density polyethylene (HDPE) process and demonstrates the use of tasks in simulating grade changes. Section 7.7 presents another workshop to demonstrate how to implement various control schemes in a commercial slurry HDPE process. Section 7.8 demonstrates the controller design for a gas-phase fluidized-bed LLDPE process under a condensed mode operation previously presented in Section 5.8 and introduces the concept of a split-range (SR) controller. Section 7.9 presents the inferential controller of a slurry HDPE process. This chapter ends with a reference section.

There are several published studies of dynamic simulation and control of polyolefin processes using Aspen Plus and Aspen Plus Dynamics [1–5]. However, none of the published studies has presented sufficient details to enable the readers to apply software tools for this application. An objective of this chapter is to present the workflow and details of dynamic polymer process simulation with illustrative workshops to help our readers.

---

<!-- PDF page 370 -->

#### 7.1 Workshop 7.1: Workflow for Dynamic Process Modeling Using Aspen Plus and Aspen Plus Dynamics

We begin with an illustrative example to demonstrate the following steps in our workflow:

1. Create a steady-state simulation flowsheet in Aspen Plus (which includes Aspen Polymers), resulting in a steady-state simulation file, *.bkp);

2. Enter the data required to calculate the dynamics of the process, particularly the vessel type and geometry required for vessel volume; vessel initial fill percentage required for starting vessel holdup; process heat-transfer option, equipment heat-transfer option, and environmental heat-transfer method for heat-transfer calculations. Run the steady-state simulation and save the results.

3. Export the simulation to Aspen Plus Dynamics, resulting in a dynamic simulation file, *.dynf, and an Aspen property data file, *.appdf.

4. Open the dynamic simulation file in AD; apply process disturbances; change the default level, pressure, and temperature controllers; add new controllers; and add tables or figures for displaying simulation results before running the dynamic simulation.

For step 1, we open a steady-state simulation file, WS7.1.bkp. Figure 7.1 shows the flowsheet, and Table 7.1 specifies the inputs.

For step 2, we click the Dynamics tab on the ribbon and click on the Dynamic Mode button to activate the dynamic input form. See Figure 7.2 for inputs for the heater, which include a dynamic heater type instead of an instantaneous type and heater volume specifications.

For heat-transfer option, we choose the default, constant duty. Other options include: (1) constant medium temperature with heat duty depending on the temperature difference between process fluid and the heating/cooling medium; and

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_873_809_1219.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.1 Flowsheet for WS7.1.</div>


---

<!-- PDF page 371 -->

<div style="text-align: center;">Table 7.1 Specifications of the steady-state simulation, WS7.1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Components</td><td style='text-align: center; word-wrap: break-word;'>N2, NC6 (n-hexane), and water</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Property method</td><td style='text-align: center; word-wrap: break-word;'>NRTL thermodynamic method with Henry component, N2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Feed: 20 °C, 1.1 bar, mole flow (kmol/hr): N2 - 2, NC6 - 20, and water - 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Blocks</td><td style='text-align: center; word-wrap: break-word;'>Heater: 0 bar (no pressure drop), output vapor fraction = 0.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Flash: 1 bar, 0 MMkcal/hr (adiabatic)</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_401_777_1004.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.2 Dynamic data inputs for the heater.</div>


(2) LMTD (log-mean temperature difference) between the process fluid and the heating/cooling medium.

We do not consider equipment heat transfer in this example. When there are large changes in the equipment temperature (including startup, shutdown, or pressure relief), equipment heat transfer becomes important, and we need to enter the mass and heat capacity of the equipment, the overall heat-transfer coefficient, and the ambient temperature in order to model equipment heat capacity and heat transfer with the environment.

---

<!-- PDF page 372 -->

The flash unit is a vertical vessel with an elliptical head, a length of 4.5 m, and a diameter of 1.5 m. We assume a constant duty option for heat transfer and specify a liquid volume fraction of 0.3 for the initial conditions. We do not consider equipment heat transfer and vessel wall heat transfer. A search of the AD online help, “Vessel Geometry,” gives pictures of different vessel orientations and head types and shows how volume and height are calculated and how liquid level is determined.

In converting a steady-state simulation model to a dynamic simulation model, AD automatically adds default controllers according to the following rules: (1) If there is a liquid in the vessel, add a level controller (LC); (2) If there is a vapor in the vessel, add a pressure controller (PC); and (3) If the vessel is a reactor that uses kinetics, add a temperature controller (TC). Following rules (1) and (2), we add default controllers for level and pressure. We then run the steady-state simulation and save the resulting file as WS7.1.bkp within our AD working folder.

For Step 3, we click the Dynamic tab on the ribbon and click the Flow Driven button to export the simulation from Aspen Plus to AD, and save the dynamic simulation in the AD working folder as WS7.1.dynf. This will automatically open the simulation flowsheet in AD with the default level and pressure controllers on top of the Aspen Plus simulation window. See Figure 7.3.

When we check the AD working folder, we see three simulation files for our example: (1) steady-state simulation, Aspen Plus backup file, WS7.1.bkp; (2) dynamic simulation, Aspen Dynamics language file, WS7.1.dynf; and (3) Aspen Plus property data, or problem definition file, WS7.1dyn.appdf. To run the dynamic simulation file property, we must place the dynamic simulation and property data files within the same working folder.

For Step 4, we open the dynamic simulation, WS7.1.dynf, within AD. We introduce the operation of AD to run a simulation in the next section.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_839_814_1199.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.3 Clicking on the Flow Driven button within the Dynamic Tab within Aspen Plus to export the flowsheet to display within Aspen Plus Dynamics.</div>


---

<!-- PDF page 373 -->

### 7.2 Running Simulation in Aspen Plus Dynamics

#### 7.2.1 Types of Dynamic Simulations: Flow-Driven and Pressure-Driven

In Figure 7.3, we choose flow-driven simulation type instead of pressure-driven. Table 7.2 compares the two types of dynamic simulations. For most liquid-phase polymer processes, we choose flow-driven simulations.

#### 7.2.2 Graphical Interface of Aspen Plus Dynamics

Figure 7.4 illustrates the graphical interface of AD. The interface displays several areas: (a) a large flowsheet window, in which we see the flowsheet; (b) simulation explorer, including areas labeled by (2), (3), (4), and (6); (c) model libraries for adding streams and blocks to the flowsheet, area labeled by (5); and (d) message window, area labeled by (7).

To display the message window, we click on “View” on the top left row, followed by “Messages.” To display the simulation explorer, we click on the graphical button labeled by (8), which is one of the buttons on the top horizontal tool bar, labeled by (1); we may also click on “Tools” on the top left row, followed by “Explorer.” We then see the area labeled by (2), or “Exploring – Simulation.” Within the simulation explorer, we see the “Flowsheet” folder, labeled by (3), which includes “Blocks” (FLASH, FLASH_LC, FLASH_PC, and HEATER) and “Streams” (FEED, FEED1, ISO, IS1, IS2, IS3, LIQ, and VAP).

<div style="text-align: center;">Table 7.2 A comparison of flow-driven and pressure-driven dynamic simulations.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Item</td><td style='text-align: center; word-wrap: break-word;'>Flow-driven simulation</td><td style='text-align: center; word-wrap: break-word;'>Pressure-driven simulation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.</td><td style='text-align: center; word-wrap: break-word;'>Specified</td><td style='text-align: center; word-wrap: break-word;'>Feed flow rate and pressure specified</td><td style='text-align: center; word-wrap: break-word;'>All feed and product pressures specified; feed flow rate not specified</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.</td><td style='text-align: center; word-wrap: break-word;'>Stream flow rate and pressure difference</td><td style='text-align: center; word-wrap: break-word;'>Flow rate is not controlled by pressure difference</td><td style='text-align: center; word-wrap: break-word;'>Flow rate results from pressure difference</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.</td><td style='text-align: center; word-wrap: break-word;'>Outlet flow rate from a block</td><td style='text-align: center; word-wrap: break-word;'>Specified or determined from mass balance, and not affected by downstream pressure</td><td style='text-align: center; word-wrap: break-word;'>Determined by pressure and by pressure/flow relationship between upstream and downstream pressures</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4.</td><td style='text-align: center; word-wrap: break-word;'>Flow and pressure control</td><td style='text-align: center; word-wrap: break-word;'>Perfect control assumed for liquid processes, as the pressure/flow dynamics for liquids are very fast</td><td style='text-align: center; word-wrap: break-word;'>Proper control required</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5.</td><td style='text-align: center; word-wrap: break-word;'>Simplicity or complexity of application</td><td style='text-align: center; word-wrap: break-word;'>Easy to set up; useful for an initial approach to studying the dynamics of liquid processes</td><td style='text-align: center; word-wrap: break-word;'>More rigorous, and complex to set up (need to balance the pressures within Aspen Plus with valves, pumps, etc.)</td></tr></table>

---

<!-- PDF page 374 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_161_809_525.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.4 An illustration of the graphical interface of Aspen Plus Dynamics.</div>


We note that IS represents a control signal, labeled by (6), as one of the six types of streams within the model libraries, labeled by (5). Within the flowsheet window, we see the dashed control signal lines for the level controller (LC) and pressure controller (PC).

Figure 7.5 shows the contents of the simulation folder within the simulation explorer.

The simulation folder displayed in Figure 7.5 includes the following: (1) component list – components and physical properties; (2) globals – details of variables global to the simulation, such as ambient temperature, ideal gas law constant R and numerical constant Pi ( $ \pi = 3.1416 $) (more later); (3) flowsheet – streams and blocks in the flowsheet; (4) local library – customized models; (5) libraries – library of models; and (6) diagnostics – information on simulation resolution.

#### 7.2.3 Simulation Run Modes and Run Control

AD includes the initialization and dynamic run modes. To do a simulation, we begin with an initialization run, which solves the equations representing the process at time zero to find the values of the free or unspecified variables. To do a dynamic run, we first make an initialization run at time zero and then integrate the system of equations representing the process step-by-step. AD reports the simulation results at each specified communication interval.

Before we make a dynamic simulation, we  $ \underline{\text{must}} $ save our original AD dynamic simulation file for a given problem, such as  $ \underline{\text{WS7.1.dynf}} $, under a new name, such as  $ \underline{\text{WS7.1-1.dynf}} $. We then proceed to use the newly saved file for our dynamic simulation. This step is important, as a time-dependent, dynamic simulation in AD does not automatically save the specifications of the starting file for us, and we must save the original starting file for future use.

---

<!-- PDF page 375 -->

<div style="text-align: center;">Figure 7.5 Contents of simulation folder and flowsheet folder.</div>


<div style="text-align: center;">WS7.1.dynf - Aspen Plus Dynamics V11</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_499_188_798_797.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Table 7.3 Types of variable specifications in Aspen Plus Dynamics (AD).</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Specification type</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.</td><td style='text-align: center; word-wrap: break-word;'>Fixed</td><td style='text-align: center; word-wrap: break-word;'>Variable value specified by the user, and not solved in the simulation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.</td><td style='text-align: center; word-wrap: break-word;'>Free</td><td style='text-align: center; word-wrap: break-word;'>Variable value solved by the simulation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.</td><td style='text-align: center; word-wrap: break-word;'>Initial</td><td style='text-align: center; word-wrap: break-word;'>Variable value known at time zero for an initialization or a dynamic run</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4.</td><td style='text-align: center; word-wrap: break-word;'>RateInitial</td><td style='text-align: center; word-wrap: break-word;'>Variable whose time derivative is known at time zero for an initialization or a dynamic run</td></tr></table>

To verify that the dynamic simulation file exported from Aspen Plus has correctly specified the required inputs and is ready for simulation runs, we see a “Ready” word together with a green status indicator in the lower right corner of Figure 7.6. Table 7.3 lists the types of variable specifications, and Table 7.4 summarizes the types of run modes in AD.

---

<!-- PDF page 376 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_151_805_485.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.6 An illustration of the initialization run mode, the run button, and the green ready status indicator of specifications complete.</div>


<div style="text-align: center;">Table 7.4 Run modes in Aspen Plus Dynamics (AD).</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Run type</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.</td><td style='text-align: center; word-wrap: break-word;'>Initialization run</td><td style='text-align: center; word-wrap: break-word;'>Specifying the initial conditions for a subsequent dynamic run. May initialize process variables, their time derivatives, or a combination of both.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.</td><td style='text-align: center; word-wrap: break-word;'>Steady-state run</td><td style='text-align: center; word-wrap: break-word;'>Running a simulation where the time derivatives of a dynamic simulation are equal to zero</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.</td><td style='text-align: center; word-wrap: break-word;'>Dynamic run</td><td style='text-align: center; word-wrap: break-word;'>Running a simulation where the variables change over time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4.</td><td style='text-align: center; word-wrap: break-word;'>Estimation run</td><td style='text-align: center; word-wrap: break-word;'>Fitting model parameters to experimental or process data (parameter estimation) or comparing the steady-state process performance with that predicted by a model (data reconciliation)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5.</td><td style='text-align: center; word-wrap: break-word;'>Optimization run</td><td style='text-align: center; word-wrap: break-word;'>Optimizing steady-state or dynamic solutions using an objective function and supplied constraints</td></tr></table>

#### 7.2.4 Viewing Simulation Results Using Predefined Tables and Plots

We first run an initialization. Next, we set up some predefined tables and plots for our dynamic run. Specifically, we right-click the Feed name to open Forms, followed by setting up the predefined Manipulate table and the TPF (temperature–pressure–molar flowrate) plot. See Figure 7.7.

In the same way, we set up the predefined TPF plots for Feed1 stream from the Heater and both VAP and LIQ streams from the Flash unit. We arrange the resulting table and plots properly within the flowsheet window, as illustrated in Figure 7.8. We note that in the Feed.Manipulate Table, both temperature and pressure are fixed, but the total molar flow is free.

Next, we change the run type from Initialization to Dynamic, and select Run Options from the Run menu. We enter the required inputs according to Figure 7.9. Note that we pause the dynamic simulation at 1 hr.

---

<!-- PDF page 377 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_151_437_467.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Figure 7.7 Right-click on Feed name to open up Forms, followed by setting up the predefined Manipulate table and TPF (temperature-pressure-molar flow rate) plot.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_573_630_894.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 7.8 Setting up the predefined tables and plots.</div>


We run the dynamic simulation until it pauses at 1 hr. At that time, we change the Feed mole flow (FR) in the Feed. Manipulate Table from 92 to 115 kmol/hr, and change its variable type from Free to Fixed. We then see the Specification Status button (previously illustrated in Figure 7.6) changes from green to red, indicating that the system is overspecified. See Figure 7.10.

#### 7.2.5 Specification Status and Analysis

Table 7.5 summarizes the several types of specification status that we frequently encounter while running AD. Basically, to solve a simulation, the number of equations must equal the number of variables to be calculated (or unknowns). In other words, the total number of degrees of freedom must be satisfied. If necessary, we can adjust the specification by unfixing and then fixing an equal number of

---

<!-- PDF page 378 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_147_476_658.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Figure 7.9 Run options showing a pause at 1 hr, with other inputs at default values.</div>


variables. For more complex specification status not listed in the table, we recommend the reader to search for “overview of specification status” with AD online help.

According to Table 7.5 and Figure 7.11, our simulation example is overspecified when changing Feed stream from 92 to 115 kmol/hr and from a free variable to a fixed variable. To know more details about this overspecification, we double-click the red status button to open the Specification Analysis tool of AD. We then click the Analyze button to show the “Recommended changes to specifications,” that is, to change the mole flow of nitrogen in the Feed from a fixed variable to a free variable. See Figure 7.11. In other words, after changing Feed stream from 92 to 115 kmol/hr, we let the simulation calculate the new mole flow of nitrogen in the Feed (the nitrogen mole flow in the Feed changes from 2 kmol/hr specified in Table 7.1 to 25 kmol/hr).

We should always think over the recommendation changes made by the Specification Analysis to see if they are reasonable and not blindly accept all the recommended changes. In the current example, we choose to accept the recommended change and click on the Accept button. We see the status button change from red to green again.

We then run the dynamic simulation from 1 to 5 hr by following Figure 7.9, and ask AD to pause the simulation at 5 hr. We illustrate the results in Figure 7.12. In displaying the graphical results, we need to double-click the x-axis of each figure (“Time Hours”) to open up the “Plot Axis Scale Setting” and change its “Axis Range” from 0 to 5 hr. We see that mole flows, temperature, and pressure in VAP and LIQ approach new steady-state values at 5 hr.

---

<!-- PDF page 379 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_149_778_671.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.10 Changing Feed stream from 92 to 115 kmol/hr and from a free variable to a fixed variable at 1 hr leads to a change of specification status button from green (complete) to red (overspecified).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_812_712_1154.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 7.11 Using the Specification Analysis tool with AD to identify recommended changes to make variable specifications complete.</div>


---

<!-- PDF page 380 -->

<div style="text-align: center;">Table 7.5 Specification status buttons within AD.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Specification status button</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td><td style='text-align: center; word-wrap: break-word;'>Explanation</td><td style='text-align: center; word-wrap: break-word;'>Suggested solution</td></tr><tr><td style='text-align: center; word-wrap: break-word;'><img src="imgs/img_in_image_box_109_255_161_288.jpg" alt="Image"" /></td><td style='text-align: center; word-wrap: break-word;'>Underspecified</td><td style='text-align: center; word-wrap: break-word;'>The number of equations is less than the number of variables to be calculated</td><td style='text-align: center; word-wrap: break-word;'>Fix more variables or add more equations</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>▲</td><td style='text-align: center; word-wrap: break-word;'>Overspecified</td><td style='text-align: center; word-wrap: break-word;'>The number of equations is greater than the number of variables to be calculated</td><td style='text-align: center; word-wrap: break-word;'>Fix less variables or remove redundant equations</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>□</td><td style='text-align: center; word-wrap: break-word;'>Complete</td><td style='text-align: center; word-wrap: break-word;'>The number of equations equals the number of variables to be calculated</td><td style='text-align: center; word-wrap: break-word;'>Ready to run simulation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'><img src="imgs/img_in_image_box_109_483_165_513.jpg" alt="Image"" /></td><td style='text-align: center; word-wrap: break-word;'>Undetermined</td><td style='text-align: center; word-wrap: break-word;'>Cannot determine the status of the flowsheet</td><td style='text-align: center; word-wrap: break-word;'>Check the simulation message for possible causes. Could be an empty simulation or inconsistency in the types used or in the flowsheet connectivity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>▼</td><td style='text-align: center; word-wrap: break-word;'>Underspecified of initial variable</td><td style='text-align: center; word-wrap: break-word;'>The number of initial variables is less than the number of process variables</td><td style='text-align: center; word-wrap: break-word;'>Initialize more process variables or initialize more time-differential variables</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>▲</td><td style='text-align: center; word-wrap: break-word;'>Overspecified of initial variables</td><td style='text-align: center; word-wrap: break-word;'>The number of initial variables is greater than the number of process variables</td><td style='text-align: center; word-wrap: break-word;'>Un-initialize some process variables, or un-initialize some time-differential variables</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_326_158_354.jpg" alt="Image" width="5%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_413_159_443.jpg" alt="Image" width="5%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_592_160_621.jpg" alt="Image" width="5%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_679_160_706.jpg" alt="Image" width="5%" /></div>


#### 7.2.6 Creating New Tables and Plots

Instead of using predefined tables and plots (Figure 7.7), we demonstrate how to create our own tables and plots in AD. First, we open our original simulation file, WS7.1.dynf, and save it as WS7.1-2.dynf. Following the run options in Figure 7.9, we run dynamic simulation for 1 hr and pause. We then follow Figure 7.10 to change Feed stream from 92 to 138 kmol/hr and from a free variable to a fixed variable at 1 hr. We also change the mole flow of nitrogen in the Feed from a fixed variable to a free variable according to Figure 7.11. We then run the dynamic simulation to pause at 10 hr.

To create a plot or a table, we click the New Form button in the top horizontal tool bar that is circled in red in Figure 7.13 to open a New Flowsheet Form. For a plot, we select the type, Plot, and enter name, Flash, and click OK to generate an initially empty “Flash Plot.” For a table, we select the type, Table, and enter name, FlashResult, and click OK to generate an initially empty “FlashResult Table.”

Refer to Figure 7.14. We double-click the Flash block to open the large FLASH.Results Table. We select the variable T (temperature) and drag and drop it to the small new table, FlashResult Table. Specifically, we click the selected variable

---

<!-- PDF page 381 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_150_775_550.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.12 Simulation results from 1 hr to 5 hr after increasing Feed mole flow from 92 to 115 kmol/hr at 1 hr.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_646_643_966.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 7.13 Creating a plot or a table through the New Form button circled in red.</div>


once, click and hold until a circle-with-slash icon appears, and then drag and drop. Repeat the same operation for variables  $ P $ (pressure) and level (liquid level). This results in a FlashResult Table with  $ T $ at 109.411 °C,  $ P $ at 16.3486 bar, and level at 1.625 m at 10 hr. Next, to show the time-dependent change of these three variables from 0 to 10 hr in the Flash Plot, we drag and drop the same three variables from the FLASH.Results Table to the Flash Plot.

We note that the names of the created plot, Flash, and the created table, FlashResult, appear in the Contents of Flowsheet, as illustrated previously in area labeled (4) in Figure 7.4.

---

<!-- PDF page 382 -->

#### 7.2.7 Variable Finding in Aspen Plus Dynamics (AD)

We can use Variable Find to create a list of variables that we have specified. From this list, we can create a table or a plot or change the properties of a variable. To use “Variable Find,” we click on “Tools” on the top left row, followed by “Variable Find.” Alternatively, we click the “Variable Find” button in the top horizontal tool bar that is circled in red in Figure 7.14 to open a Variable Find Form.

As in Section 7.2.6, we first open our original simulation file, WS7.1.dynf, and save it as WS7.1-3.dynf. Following the run options in Figure 7.9, we run dynamic simulation for 1 hr and pause. We then follow Figure 7.10 to change Feed stream from 92 to 138 kmol/hr and from a free variable to a fixed variable at 1 hr. We also change the mole flow of nitrogen in the Feed from a fixed variable to a free variable according to Figure 7.11. Before we run the dynamic simulation to pause at 10 hr, we demonstrate how to use Variable Find to set up a plot of the free nitrogen mole flow in the Feed stream. We complete this by following the steps illustrated in Figures 7.15 and 7.16.

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_559_816_877.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.14 Dragging and dropping selected variables from FLASH.Results Table to the created FlashResult Table and Flash Plot.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_969_810_1187.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.15 Clicking on Variable Find button (circled in red) to open the Variable Find Form; choosing free, algebraic and state variables; and clicking on Browse to find free variables in the FLASH block.</div>


---

<!-- PDF page 383 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_150_780_541.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.16 Clicking on “Find” button in the Variable Find to identify free variables in the FLASH block; setting up a plot named VapLiq_MoleFlow following Figure 7.14; dragging the free FLASH Vap and Liq mole flow variables and dropping them to the plot.</div>


We then choose Run Options from the Run menu and ask the dynamic simulation to pause at 10 hr. Figure 7.16 displays the resulting Vap and Liq mole flows from the FLASH block.

### 7.3 Process Control in Aspen Plus Dynamics

##### 7.3.1 Workshop 7.2: Adding a PID Controller

We begin by opening the Aspen Plus simulation file, WS7.2.bkp. We click the Dynamics tab on the ribbon and click the Dynamic Mode button to activate the dynamic input form. We complete the relevant dynamic data according to Table 7.6. After running the steady-state simulation, we export the simulation from Aspen Plus to AD, and save the resulting dynamic simulation file, WS7.2.dynf, and the Aspen Property problem definition file, WS7.2.appdf. Figure 7.17 shows the resulting flowsheet with the added level and pressure controllers.

After opening the exported dynamic simulation in AD, we make an Initialization run first and then change the run mode to Dynamic. In the following, we demonstrate how to add a proportional-integral-derivative (PID) temperature controller to stream FEED1 (feed to the FLASH block) and manipulate the heater heat duty from the HEATER block.

Step 1: See Figure 7.18. Go to the View menu to display the Model Library. Click the PID Incr icon (circled in red in the figure) on the Model Library. Click on the flowsheet to place the new controller B1. Right-click the controller block to see "rename block." Change controller name from B1 to TC.

---

<!-- PDF page 384 -->

<div style="text-align: center;">Table 7.6 Specifications of the steady-state simulation, WS7.2.bkp.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Components</td><td style='text-align: center; word-wrap: break-word;'>N2, NC6 (n-hexane), and water</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Property</td><td style='text-align: center; word-wrap: break-word;'>NRTL thermodynamic method with Henry component,  $ N_{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Method</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Feed: 20°C, 1.1 bar, mole flow (kmol/hr):  $ N_{2}-2 $,  $ NC_{6}-20 $, and water - 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Heater block</td><td style='text-align: center; word-wrap: break-word;'>0 bar (no pressure drop), output vapor fraction = 0.4; dynamic heater, inlet volume = 1 cum, outlet volume = 1 cum; medium flow direction - countercurrent; medium temperature = 60°C; temperature approach = 10°C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flash block</td><td style='text-align: center; word-wrap: break-word;'>75°C, 1 bar; vertical vessel; elliptical type; length = 4.5 m; diameter = 1.5 m; initial condition - liquid volume fraction = 0.4; default controllers - pressure and level</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_506_668_762.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 7.17 The starting dynamic simulation flowsheet for WS7.2.dynf.</div>


Step 2. (1) See Figure 7.19a. Click the Control Signal stream type in the Model Library. On the TC controller block, we see an input signal arrow (for process variable or controlled variable, FEED 1 temperature) on the left and an output signal arrow (for manipulated variable or controller output, HEATER heat duty) on the right.

Step 2. (2) See Figure 7.19b. Connect the left control signal to the output signal arrow of FEED1, and choose FEED1 temperature as the process variable or controlled variable.

Figure 7.19c shows the resulting left controller input signal connection to the process variable or controlled variable, FEED 1 temperature.

Step 3. (1) See Figure 7.19d. Click the Control Signal stream type in the Model Library. On the TC controller block, we see an output signal arrow (for manipulated variable or controller output, HEATER heat duty) on the right.

Step 3. (2) See Figure 7.19e. Connect the right control signal of TC to the input signal arrow of HEATER, and choose heat duty as the manipulated variable or controller output.

Figure 7.19f shows the resulting right controller output signal connection to the manipulated variable or controller output, HEATER heat duty.

---

<!-- PDF page 385 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_144_776_614.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.18 Adding a PID temperature controller to the flowsheet.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_674_780_1049.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.19a Choosing the TC process variable or controlled variable to connect to the left input signal of TC.</div>


#### 7.3.2 Configuring a PID Controller

After we have added the controller, we save the current dynamic simulation file under a new name, WS7.2-1.dynf, and proceed with the first case study of the controller. We save the current dynamic simulation file, WS7.2.dynf, as a backup starting file for additional case studies.

---

<!-- PDF page 386 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_150_811_529.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.19b Choosing FEED1 temperature as TC process variable or controlled variable to connect the right output signal of TC.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_614_727_913.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 7.19c Connection between the left controller input signal to the process variable or controlled variable, FEED1 temperature.</div>


We double-click the controller TC to display the controller faceplate. See Figure 7.20.

On the faceplate, the first three buttons from left to right at the top level enable us to switch among auto, manual, and cascade modes, respectively. The fourth button (%) allows us to switch between viewing values in process units or percentages of range. To see the process units, we can hold the mouse over the label SP (setpoint), PV (process variable), or OP (controller output). The fifth to seventh buttons are Configure form, Plot form, and Tuning form, respectively, which we demonstrate further below.

First, we click the Configure form button, and then the Initialize Values button. This configures the controller with default values: (1) SP is the current controlled

---

<!-- PDF page 387 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_163_767_493.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.19d Choosing the TC-manipulated variable or controller output to connect to the right output signal of TC.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_594_781_939.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.19e Choosing HEATER heat duty as TC-manipulated variable or controller output to connect the right output signal of TC.</div>


variable (FEED1 stream temperature at 78.3214°C); (2) OP is set to the current controller output or manipulated variable (HEATER heat duty at 0.259759 MMkcal/hr). The ranges of PV and OP are specified to 0 and twice the current variable value, respectively.

Clicking the “Other” tab within the Configure form of Figure 7.21 shows the types of PID controller algorithms available with AD.

Table 7.7 describes the ideal, series, and parallel algorithms. See AD online help with vendor algorithms.

We choose the Ideal algorithm for the current example.

---

<!-- PDF page 388 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_153_784_477.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 7.19f Connection between the right controller output signal to the manipulated variable or controller output, HEATER heat duty.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_168_578_773_938.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 7.20 Controller faceplate and configure form.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_1024_477_1168.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">Figure 7.21 PID controller algorithms available displayed within the Other folder in Configure form.</div>


---

<!-- PDF page 389 -->

<div style="text-align: center;">Table 7.7 Typical PID controller algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>PID algorithm</td><td style='text-align: center; word-wrap: break-word;'>Model equation</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.</td><td style='text-align: center; word-wrap: break-word;'>Ideal</td><td style='text-align: center; word-wrap: break-word;'>OP = Bias +  $ K_{\mathrm{c}} \times \{E_{\mathrm{p}} + (1/T_{1})\int E_{1} \mathrm{~d}t + T_{\mathrm{D}} \mathrm{~d}E_{\mathrm{D}} / \mathrm{d}t\} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.</td><td style='text-align: center; word-wrap: break-word;'>Series (interacting form)</td><td style='text-align: center; word-wrap: break-word;'>OP = Bias +  $ K_{\mathrm{c}} \times \{E_{\mathrm{p}} + (1/T_{1})\int E_{1} \mathrm{~d}t\} \times \{1 + T_{\mathrm{D}} \mathrm{~d}E_{\mathrm{D}} / \mathrm{d}t\} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.</td><td style='text-align: center; word-wrap: break-word;'>Parallel (standard, ISA, or noninteracting form)</td><td style='text-align: center; word-wrap: break-word;'>OP = Bias +  $ K_{\mathrm{c}} \times E_{\mathrm{p}} + (1/T_{1})\int E_{1} \mathrm{~d}t + T_{\mathrm{D}} \mathrm{~d}E_{\mathrm{D}} / \mathrm{d}t $</td></tr></table>

OP = controller output; Bias = the value of the manipulated variable when the process is at steady state; Gain = proportional gain  $ K_c $;  $ E = \text{error} = \text{setpoint} - \text{process variable} $;  $ E_p = \text{proportional mode error} $;  $ E_1 = \text{integral mode error} $;  $ E_D = \text{Derivative mode error} $;  $ T_1 = \text{integral time} $;  $ T_D = \text{derivative error} $.

We give some observations on the PID controller-tuning parameters below [6, 7]:

(1) The proportional gain,  $ K_{c} $, is typically expressed as 100/(proportional band, PB). The PB is the error (expressed as the percentage of the range of the measured variable) required to move the control valve (the final control element) from fully closed to fully open. Typically, PB has a value between 30 and 300.

(2) The larger the proportional gain,  $ K_{c} $, the smaller the difference between the set-point value and the process variable value at steady state (called steady-state error or offset). P (proportional) control corrects the present error between the setpoint and the process variable.

(3) The integral time, or reset time,  $ T_{1} $, is the time it takes the controller to give an output that is twice the output from a proportional controller, following a step change in error. In other words, the integral time is the time it takes for the controller to “repeat” the proportional controller action.

(4) The integral controller acts to eliminate the steady-state error (offset) that is present in applying the proportional controller action alone. A large integral or reset time essentially minimizes the integral controller action. PI (proportional-integral) control corrects the past and present errors between the setpoint and process variable.

(5) The derivative action increases the stability of the controlled system and permits either a higher controller gain,  $ K_{c} $, or a lower integral or reset time,  $ T_{1} $, to be used. The latter speeds up the dynamic response of the controlled system. If the derivative time  $ T_{D} $ is large enough, the controlled system would be theoretically stable for all the controller gains. PID control corrects the past, present, and future errors between setpoint and process variable, considering the positive or negative rate of change of the error in the output variable in affecting the future error.

Table 7.8 gives the heuristic PID controller-tuning parameters for different types of controllers [1, 2].

We follow these initial values for our temperature controller, as illustrated in Figure 7.20. We also choose Reverse controller action for this temperature controller because we need to decrease the HEATER heat duty when the

---

<!-- PDF page 390 -->

<div style="text-align: center;">Table 7.8 Initial PID controller-tuning parameters.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Controller type</td><td style='text-align: center; word-wrap: break-word;'>Proportional gain ( $ K_{c} $)</td><td style='text-align: center; word-wrap: break-word;'>Integral time  $ T_{1} $ (min)</td><td style='text-align: center; word-wrap: break-word;'>Derivative time  $ T_{D} $ (min)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flow</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Level</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Composition</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">Table 7.9 PID controller actions.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>When the action is</td><td style='text-align: center; word-wrap: break-word;'>And the measured variable (controlled variable or process variable)</td><td style='text-align: center; word-wrap: break-word;'>Then the manipulated variable</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Direct</td><td style='text-align: center; word-wrap: break-word;'>Increases</td><td style='text-align: center; word-wrap: break-word;'>Increases</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Direct</td><td style='text-align: center; word-wrap: break-word;'>Decreases</td><td style='text-align: center; word-wrap: break-word;'>Decreases</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reverse</td><td style='text-align: center; word-wrap: break-word;'>Increases</td><td style='text-align: center; word-wrap: break-word;'>Decreases</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reverse</td><td style='text-align: center; word-wrap: break-word;'>Decreases</td><td style='text-align: center; word-wrap: break-word;'>Increases</td></tr></table>

<div style="text-align: center;">Table 7.10 Guidelines for AD default controllers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Controller added</td><td style='text-align: center; word-wrap: break-word;'>When</td><td style='text-align: center; word-wrap: break-word;'>Measured variable (controlled variable or process variable)</td><td style='text-align: center; word-wrap: break-word;'>Manipulated variable</td><td style='text-align: center; word-wrap: break-word;'>PID tuning parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pressure</td><td style='text-align: center; word-wrap: break-word;'>Vapor holdup is modeled</td><td style='text-align: center; word-wrap: break-word;'>Pressure in vessel</td><td style='text-align: center; word-wrap: break-word;'>Vapor outlet flow rate</td><td style='text-align: center; word-wrap: break-word;'>$ K_{c}=0.2 $,  $ T_{1}=12 \text{ min} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Level</td><td style='text-align: center; word-wrap: break-word;'>Liquid holdup is modeled</td><td style='text-align: center; word-wrap: break-word;'>Liquid level</td><td style='text-align: center; word-wrap: break-word;'>Liquid outlet flow rate</td><td style='text-align: center; word-wrap: break-word;'>$ K_{c}=0.2 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Temperature</td><td style='text-align: center; word-wrap: break-word;'>Stirred reactor block</td><td style='text-align: center; word-wrap: break-word;'>Vessel temperature</td><td style='text-align: center; word-wrap: break-word;'>Heat duty</td><td style='text-align: center; word-wrap: break-word;'>$ K_{c}=0.2 $,  $ T_{1}=12 \text{ min} $</td></tr></table>

temperature increases. Table 7.9 summarizes the other options for controller action.

Lastly, we mention that AD automatically generates the default pressure, level, and temperature controllers according to the guidelines of Table 7.10.

We now select Run Options from the Run menu, accept the default parameters, and ask the simulation to pause at 5 hr. On the Controller faceplate, we click the Plot form to display both the controlled variable or process variable (FEED1 temperature) and the controller output or manipulated variable (HEATER heat duty). See Figure 7.22. We then run the simulation until it pauses at 5 hr. Next, we follow Figure 7.12 to change Feed stream from 92 to 138 kmol/hr and from a free variable to a fixed variable at 1 hr. We also change the mole flow of nitrogen in the Feed from a fixed variable to a free variable according to Figure 7.12. We then

---

<!-- PDF page 391 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_150_779_408.jpg" alt="Image" width="67%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>Process Variable C</th><th style='text-align: center;'>Control Output MMkcal/hr</th><th style='text-align: center;'>Set Point C</th><th style='text-align: center;'>Control Output MMkcal/hr</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.35</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.22 Controller response after increasing the FEED mole flow from 92 to 138 kmol/hr: FEED1 temperature (PV) changes from 78.3215 to 76.4821°C, while HEATER duty increases from 0.2598 to 0.5195 MMkcal/hr.</div>


run the dynamic simulation to pause at 15 hr. We see the controller response in Figure 7.22.

We show in Table 7.11 the available control-related models within AD. The reader may refer to AD online help for description and example of using a specific model. In Section 7.7, we illustrate the use of the split-range controller in a HDPE workshop.

<div style="text-align: center;">Table 7.11 Control-related models available within AD.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Model</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Comparator</td><td style='text-align: center; word-wrap: break-word;'>Calculates the difference between two input signals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Dead_time</td><td style='text-align: center; word-wrap: break-word;'>Delays a signal by a specified time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DMCplus</td><td style='text-align: center; word-wrap: break-word;'>Interface to DMCplus online control</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Discretize</td><td style='text-align: center; word-wrap: break-word;'>Discretizes a signal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HiLoSelect</td><td style='text-align: center; word-wrap: break-word;'>Selects the higher or lower of two input signals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IAE</td><td style='text-align: center; word-wrap: break-word;'>Calculates the integral of the absolute value</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ISE</td><td style='text-align: center; word-wrap: break-word;'>Calculates the integral of the squared error</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lag_1</td><td style='text-align: center; word-wrap: break-word;'>Models a first-order lag between the input and output</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lead_lag</td><td style='text-align: center; word-wrap: break-word;'>Models a lead-lag element</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Multiply</td><td style='text-align: center; word-wrap: break-word;'>Calculates the product of two input signals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PIDlncr</td><td style='text-align: center; word-wrap: break-word;'>A three-mode Proportional-integral-derivative controller</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PRBS</td><td style='text-align: center; word-wrap: break-word;'>Generates a pseudo-random binary signal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ratio</td><td style='text-align: center; word-wrap: break-word;'>Calculates the ratio of two input signals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Scale</td><td style='text-align: center; word-wrap: break-word;'>Scales an input signal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SplitRange</td><td style='text-align: center; word-wrap: break-word;'>Models a split-range controller</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sum</td><td style='text-align: center; word-wrap: break-word;'>Calculates the sum of two input signals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transform</td><td style='text-align: center; word-wrap: break-word;'>Performs a loge, square, square root, or power transform</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Valve_dyn</td><td style='text-align: center; word-wrap: break-word;'>Models the dynamics of a valve actuator</td></tr></table>

---

<!-- PDF page 392 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_152_743_559.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 7.23 Snapshot Management and Take a Snapshot buttons, and choosing when to take an automatic snapshot under Create within Snapshot Management.</div>


### 7.4 Snapshots

A snapshot is a saved set of values and specifications for all variables in a simulation. It is useful for moving back to a point when simulation was converged. The snapshot is created automatically after every run type except for dynamic. We can also take manual snapshots at desired times.

Refer to Figure 7.23. We see the Snapshot Management and Take a Snapshot buttons in the top horizontal toolbar. Click Snapshot Management and select the Create tab. We see that we can request AD to take snapshots automatically under the specified conditions.

Next, refer to Figure 7.24. We can also ask AD to take a snapshot at a desired simulation time. We click the Take a Snapshot button, enter the description "End_of_5_hr_run" and click OK. We then see a snapshot under this name as a new listing under the General folder of Snapshot Management.

We can copy values from any snapshot or result to the current simulation. This copies values when the name of the variable in the snapshot or result matches the name of a variable in the current simulation.

We can rewind the simulation to a previous time point if snapshots are available. If there are no snapshots, rewinding will take the simulation back to time zero.

#### 7.5 Workshop 7.3: Tasks for Implementing Discrete Events

A task is a set of instructions, which defines a sequence of discrete actions, such as disturbances in feed condition, or changes to controller set points. Tasks can trigger

---

<!-- PDF page 393 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_158_711_526.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 7.24 Taking a Snapshot and Listing Under Snapshot Management.</div>


an event or action when a predefined condition becomes true. An example is to close or open a valve when the fluid level falls/rises above/below a value. All task statements are executed in sequence.

There are two types of tasks within AD: (1) Event-driven tasks – it requires a conditional expression to determine when the task begins. These events can be explicit or events, which always happen and are usually time-specific, or implicit or events may or may not happen depending on other events or conditions. (2) Callable tasks – they are called by other tasks instead of being triggered by an event. You can optionally define callable tasks with parameter call lists, with the calling task passing the parameter values. You can make calls to tasks within models, to tasks in a tasks folder, or to other tasks in your flowsheet.

Figure 7.25 shows the structure of a task manager. An event-driven task must be activated to be considered by the task manager during the dynamic simulation.

We illustrate the task by opening a steady-state simulation file, WS7.3.bkp. Figure 7.26 shows the flowsheet, and Table 7.12 specifies the input.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_1000_768_1239.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.25 The structure of a task manager.</div>


---

<!-- PDF page 394 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_171_753_429.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 7.26 Flowsheet for WS7.3.</div>


<div style="text-align: center;">Table 7.12 Specifications of the steady-state simulation, WS7.3.bkp.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Components</td><td style='text-align: center; word-wrap: break-word;'>Acetic acid (HOAc), ethanol (EtOH), ethyl acetate (EtOAc), water</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Thermodynamic Method</td><td style='text-align: center; word-wrap: break-word;'>NRTL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stream</td><td style='text-align: center; word-wrap: break-word;'>Feed: 70°C, 1 atm, Mass flow (kg/hr) - 2300 (HOAc), 1600 (EtOH), 100 (water)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Reactor: 1 atm, 70°C, liquid-only, reactor volume = 2.5 cum; Dynamic data: vertical vessel, elliptical, length = 2 m, heat-transfer option-constant temperature, medium temperature = 20°C, initial condition - liquid volume fraction = 0.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reactions</td><td style='text-align: center; word-wrap: break-word;'>HOAc + EtOH → EtOAc + H2O;  $ k = 1.9 \times 10^{8} $,  $ E = 5.95 \text{J/kmol} $</td></tr></table>

Running the steady-state simulation and then exporting the simulation to AD gives a dynamic simulation file, WS7.3.dynf, and an Aspen property data file, WS7.3dyn.appdf. On the dynamic simulation flowsheet of Figure 7.27, we delete the automatically generated LC and associated control signal connections. We change the run mode to Initialization and perform an initialization run.

In Figure 7.27, we also show the “Add task” button within the Flowsheet folder. We demonstrate below the following tasks:

Task A: Start the sequence at time 0.01 hr.

Task B: Shut off the feed.

Task C: Drain the vessel by emptying the product at a rate of 60 kg/hr until the reactor liquid level falls below 0.1 m.

Task D: Shut off the ethyl acetate product liquor.

Task E: Charge the reactor with feed at a mass flow rate of 4000 kg/hr for a period of 0.7 hr. Start by ramping the feed flow to 4000 kg/hr over a period of 0.1 hr.

Task F: Shut off the feed.

Task G: Wait for the concentration of ethyl acetate in the reactor to become greater than 7 kmol/m³.

---

<!-- PDF page 395 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_139_157_775_444.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.27 The exported dynamic simulation flowsheet with an automatically generated level controller and the "Add task" button within Flowsheet folder.</div>


Task H: Set up a task to call all the preceding subtasks.

(1) Task A: Run the dynamic simulation and ask the AD to pause at 0.01 hr.

(2) Task B: Following Figure 7.27, click "Add Task" button within Contents of Flowsheet to create the task "ShutoffFeed" from Flowsheet window. As we see in Figure 7.28b, we have AD print to the message window that the task has started; set feed molar flow rate (FmR), that is (STREAMS("FEED").FmR), to zero; and print out to message that the task has ended. At the end of defining the task "ShutoffFeed" or any task within AD, we compile the task script to detect any errors. Referring to Figure 7.28b, we do this by right-clicking the mouse inside the task window to bring up the "compile" tab. Clicking on the tab to compile the task script. Note in Figure 7.28b, line 1 gives the task name, and lines 2–9 give the standard instructions for tasks within AD. To save figure space, we will not display lines 1–9 in Figures 7.29–7.33 defining tasks C–H.

(3) Task C: Create the task “DrainVessel” from Flowsheet window; print out to messages when the task starts; set the Acetate mass flow rate (FR), that is (Streams("Acetate").FR), to 60kg/hr; wait for reactor level (Blocks("Reactor").Level) to reach less than or equal to 0.1 m; and print out to messages when the task ends. See Figure 7.29.

(4) Task D: Create the task “ShutOffProduct” from the Flowsheet window; print out to messages when the task starts; RAMP changes Acetate mass FR, that is (Streams("Acetate").FR) to 0 linearly over a period of 0.1 time units; Print out “End of Task ShutOffProduct” when the task ends. See Figure 7.30.

RAMP is a simple, linear ramp function. Its function syntax, RAMP (Variable, Target, Period, and Ramp type), says the following:

- Variable: The name of the variable whose value is to be ramped. The variable must have the variable's value is to be changed.

• Period: The period over which the ramp takes place.

---

<!-- PDF page 396 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_153_806_809.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.28 (a) Click "Add Task" button within Contents of Flowsheet to create the task "ShutOffFeed." (b) Content of task ShutOffFeed.</div>


Print "";

---

<!-- PDF page 397 -->

<div style="text-align: center;">Figure 7.31 Content of tasks "ChargeReactor" and "Shut off Feed."</div>


10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
Print "Begin Task ChargeReactor";
Print "";
Time_next as RealParameter;
Time_next: TIME + 0.7;
SRAMP(Streams("Feed").FmR, 4000, 0.1);
Wait for Time >= Time_next;
Streams("Feed").FmR: 0.0;
Print "";
Print "End of ChargeReactor";
Print "";
End

• Ramp type: Can be either DISCRETE or CONTINUOUS. CONTINUOUS ramps are recalculated whenever the integrator moves its time. DISCRETE ramps are recalculated at communication points only. The ramp type may be omitted, in which case the default ramp type of CONTINUOUS is used.

(5) Tasks E and F: Create the task “Charge Reactor” from the Flowsheet window; print out to messages when the task starts; define “Time_next” as a real parameter (Time_next as RealParameter); set Time_next to TIME+0.7 (Time_next: TIME+0.7); SRAMP changes feed stream mass flow rate (Streams(“Feed”).FmR) with the shape of a sinusoidal curve to 4000 kg/hr over an interval of 0.1 time units; wait for Time to become greater than or equal to Time_next; “Shut off the Feed Stream Flow” (task F); and print out to messages when the task ends. See Figure 7.31.

SRAMP is a sinusoidal ramp, which gives a smoother S-shaped curve for the ramped variable. With SRAMP, if the ramp is decreasing the value of a variable, then the ramp follows the shape of a sinusoidal curve between 0 and  $ \pi $ (=3.1416). If the target is an increase, then the curve follows the shape of a sinusoidal curve between  $ \pi $ and  $ 2\pi $. SRAMP's function syntax follows that of RAMP, as described above.

(6) Task G: Create the task “AgeReactor” in the Flowsheet window; print out to messages when the task starts; wait for the reactor molar concentration of acetate, Blocks(“Reactor”). conc_mol(“acetate”), to reach 7.0 kmol/hr; print out to messages when the task ends. See Figure 7.32.

(7) Task H: Create the task “BatchSequenceRuns” in the Flowsheet window in order to call the subtasks that we have just created. See Figure 7.33.

Next, we create three plots to observe: (1) reactor liquid volume, liquid level, and temperature; (2) reactants and products concentrations in the reactor – use one axis for the concentrations; and (3) feed and product stream mass flows – use one axis for both variables.

Open AllVariables table for Acetate stream. Change mole flow rate FR to fixed and mass flow rate FmR to free. Run initialization, Steady-state, and then dynamic simulations to pause at 10 hr. Before running the dynamic simulation, we must activate the task, "BatchSequenceRuns," which controls all the defined sequencing tasks, by right-clicking on the task name within Contents of Flowsheet. Figures 7.34 illustrates the results. Note that to see the distinct drop-in level from the drain step and then the rise in level from the charge step, we must re-scale the x-coordinate to show in smaller time steps.

---

<!-- PDF page 398 -->

10
11 Print）；
12 Print "Begin Task AgeReactor";
13 Print）；
14
15 Wait For Blocks("Reactor").cone_mol("ETOAc") >= 7.0;
16
17 Print）；
18 Print "End of Task AgeReactor";
19 Print）；
20 End
21

<div style="text-align: center;">Figure 7.33 Content of task "BatchSequenceRuns."</div>


Run At 0.01;
Call ShutOffFeed;
Call DrainVessel;
Call ShutOffProduct;
Call ChargeReactor;
Call ShutOffFeed;
Call AgeReactor;
END

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (Hours)</th><th style='text-align: center;'>FeedProductMassFlows (kPa)</th><th style='text-align: center;'>ReactorPlots (kPa)</th><th style='text-align: center;'>ReactorConc Rot (kPa)</th><th style='text-align: center;'>ReactorConc</th><th style='text-align: center;'>ReactorConc</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>100.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.34 An illustration of results from task workshop, WS7.3.</div>


#### 7.6 Workshop 7.4: Dynamic Simulation and Grade Change of a Slurry HPDE Process

#### 7.6.1 Objectives

We wish to demonstrate how to convert a steady-state simulation model to a dynamic simulation model, illustrate the initial adjustments of the dynamic model and the tests of the validity of the default control schemes. We then show how to use a task procedure to implement grade-change operations applied to HDPE productions.

#### 7.6.2 Stepwise Procedure to Develop Aspen Plus Dynamics (AD) Simulation Model

We begin with a steady-state simulation model of a commercial slurry HDPE process developed by Aspen Plus (which includes Aspen Polymers) in Chapter 5 and present a step-by-step dynamic simulation of adding various controllers and making grade changes in Aspen Plus Dynamic (AD). Reference [2] includes some brief details of this application.

---

<!-- PDF page 399 -->

### Step 1. Making the steady-state simulation model ready for conversion to a dynamic simulation model

We open a steady-state simulation model, WS7.4.bkp, representing the reactors and separators in a serial-flow slurry HDPE process using multi-site Ziegler–Natta kinetics [3]. Figure 7.35 shows a steady-state simulation flowsheet in which M1 and M2 are mixers, R1 and R2 are reactors, F1 and F2 are flash units, C1 and C2 are compressors, E1 and E2 are exchangers, and S1 and S2 are splitters. The reader may see the inputs for steady-state simulation in the Aspen Plus simulation file.

For the continuous stirred tank reactors R1 and R2, we can use the RCSTR model with one vapor product stream and one liquid product stream (as in RCSTR2 in Figure 3.1). For readers with process simulation models developed with early versions of Aspen Plus, the RCSTR model could have only one exiting product stream. In that situation, we can use an alternative representation of our vapor and liquid product streams from the reactor. Specifically, we use flash units F1 and F2 following reactors R1 and R2 to generate the vapor products (V1 and V2) and liquid products (MXD and PROD), with both the CSTR and flash units being specified at the same temperature and pressure. Figure 7.35 illustrates this representation.

In this text, the reader will see again this alternative representation of a RCSTR model with both vapor product and liquid product streams by a combination of a RCSTR model with a single product stream followed by a two-phase flash model.

Our first task in preparing an Aspen Plus model for conversion into a dynamic model is to minimize the number of unnecessary computations. Unnecessary computations appear in three places: (1) unnecessary components; (2) extraneous phase calculations; and (3) extraneous unit-operation models [1].

Unnecessary components are those that appear in trace quantities and do not affect the major results of the simulation. When AD perturbs these variables, small amounts of the components with zero flow rate enter the

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_950_780_1221.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.35 A steady-state simulation flowsheet for WS7.4.</div>


---

<!-- PDF page 400 -->

system. If the system is sensitive to their presence, this can cause problems. By checking the component mass flow and mass fraction in the stream summary of the steady-state simulation results, we do not find such components in the steady-state model.

We examine the resulting vapor fraction (VFRAC) for each feed stream in the steady-state model. If a feed stream has a single phase only, we specify that stream as single phase in the flash options. This avoids singularities that result from flashing single-phase streams. We also check the outlet streams for each unit operation. If a stream is single-phase, we alter the flash options for the block so that there is no vapor–liquid check.

Extraneous unit-operation models are those that we can easily combine into other unit operations. In the current steady-state simulation, we do not have such models.

Our next task is to complete the dynamic simulation specifications for the reactors and other unit-operation blocks. We enter the data in Table 7.13.

### Step 2. Converting to a dynamic model

We click the Dynamic tab on the ribbon, click the Flow Driven button to export the simulation from Aspen Plus to AD, and save the dynamic simulation as WS7.4.dynf and the corresponding property file as WS7.4dyn.appdf in our AD working folder. Figure 7.36 shows the resulting dynamic simulation flowsheet in AD.

<div style="text-align: center;">Table 7.13 Dynamic specifications for WS7.4.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>F1 and F2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous flash with no dynamic effects</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C1 and C2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous compression</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R1 and R2</td><td style='text-align: center; word-wrap: break-word;'>Vertical vessel, elliptical, length = 6.678 m, heat-transfer option - constant duty, initial condition - liquid volume fraction = 0.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E1 and E2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous heat transfer, heat-transfer option - constant duty</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M1 and M2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous mixing</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_945_818_1255.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Figure 7.36 The dynamic simulation flowsheet of WS7.4.</div>


---

<!-- PDF page 401 -->

<div style="text-align: center;">Figure 7.37 Specifying global property mode and flash basis.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_425_148_800_362.jpg" alt="Image" width="38%" /></div>


### Step 3. Initial adjustments to the AD model

Our next step is to make initial adjustments to the AD model, focusing on: (1) rigorous property option; (2) polymer attributes for streams and blocks; (3) heat duties and temperatures; (4) calculation of derived polymer attributes; and (5) revising the control scheme setup.

(1) Rigorous property option: Using rigorous properties is generally slower but much more robust than local properties, especially when working with polymer systems. Follow the following path to change the property option: Explorer → Global → Dynamic Options → (1) Global Property Mode: Rigorous; and (2) Global Flash Basis: Equation. See Figure 7.37.

(2) Polymer attributes for streams and blocks: If there are trace amounts of catalyst or polymer in the overhead streams, AD will make the stream a polymer stream. This means that the equations involving component attributes are included for the stream. This is a problem when a stream contains a trace amount of polymer or catalyst, which is a numerical artifact. Figure 7.38 shows how we can change the stream type to eliminate this problem (Flash unit F1→overhead stream V1→Right-click Forms→PolymerInputs table→Change the Value of Catalyst_in_Stream from Yes to No.). We note that compressor C1, into which the overhead vapor V1 enters, does not support polymers. During converting from a steady-state to dynamic simulation file, AD automatically dropped catalyst attributes. We repeat the same step with overhead stream V2, leaving flash unit F2.

Once we make these adjustments to all the streams not containing catalyst or polymer, the model should be “square,” meaning that the number of fixed and free variables corresponds appropriately to the number of equations in the model. We run in Initialization mode and then run in Steady State mode. We save each one as a snapshot for future use.

<div style="text-align: center;">Figure 7.38 Changing the Value of Catalyst_in_Stream in stream V1 from Yes to No.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_499_1156_798_1285.jpg" alt="Image" width="31%" /></div>


---

<!-- PDF page 402 -->

<div style="text-align: center;">Table 7.14 Initial Specifications of Default Controllers for WS7.4.dynf.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Controller</td><td style='text-align: center; word-wrap: break-word;'>Measured variable (process variable PV or controlled variable)</td><td style='text-align: center; word-wrap: break-word;'>Manipulated variable (controller output OP)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R1_PC and R2_PC</td><td style='text-align: center; word-wrap: break-word;'>Reactor pressure: R1 at 7.55 bar; R2 at 3.5 bar</td><td style='text-align: center; word-wrap: break-word;'>Specified vapor flow rate: R1 at 19.1579 kmol/hr (same flow rate as V1 in Figure 7.37); R2 at 628.3473 kmol/hr (as flow rate as V2)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R1_TC and R2_TC</td><td style='text-align: center; word-wrap: break-word;'>Reactor temperature: R1 at 85°C; R2 at 80°C</td><td style='text-align: center; word-wrap: break-word;'>Specified heat duty: R1 at  $ -19.8786 $ GJ/hr; R2 at  $ -16.8558 $ GJ/hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R1_LC and R2_LC</td><td style='text-align: center; word-wrap: break-word;'>Reactor liquid level: R1 at 4.8287 m; R2 at 4.8287 m</td><td style='text-align: center; word-wrap: break-word;'>Specified liquid mass flow rate: R1 at 20914.4 kg/hr (same flow rate as MXD in Figure 7.37); R2 at 26222.7 kg/hr (same flow rate as PROD)</td></tr></table>

It is important to make steady-state runs and save snapshots after making each change to the dynamic model. If we make many changes at once, the system may not converge.

(3) Heat duties and temperatures: We must review each unit operation to see if AD has fixed the heat duty (Qr) and make adjustments if necessary. We should not fix the heat duties for heat exchangers because we do not know what they are. Instead, we should fix the temperatures and leave heat duty as a fee variable.

(4) Calculation of derived polymer attributes: For the polymer product stream exiting reactor R2, we must ask AD to calculate the relevant polymer attributes, such as weight-average molecular weight (MWW) and PDI. To do this, right-click the stream name, R2OUT, choose Forms, and then PolymerResults. Change “Calculate derived polymer attributes” from No to Yes.

(5) Revising control scheme setup: We save the current dynamic simulation file as WS7.4Original.dynf as a backup before we continue and modify the control schemes in the simulation file WS7.4.dynf. This flowsheet includes three default controllers for pressure, level, and temperature, as specified previously in Table 7.9. These default controllers are not necessarily valid. We must add and/or delete controllers to match the control scheme in the actual process. Table 7.14 gives the initial specifications of the default controllers.

These tabulated values match the values in the initial controller faceplates in Figure 7.39.

The default pressure controllers on the reactors R1 and R2 are not valid. Each controller maintains the reactor pressure by increasing the vapor flow rate out of the reactor (that is, vapor flow rate of streams V1 and V2 in Figure 7.36). This only increases the flow rate of material recycled into the reactor, resulting in an increase in reactor pressure. In addition, the actual reactor in the plant does not contain a

---

<!-- PDF page 403 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_149_772_380.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 7.39 Initial controller faceplates.</div>


pressure controller. Therefore, we delete both pressure controllers and their control signals.

We follow Figure 7.21 to initialize values of the controllers and revise the proportional gain and integral time for the temperature and LCs according to Table 7.8. We save the resulting flowsheet with controllers as WS7.4a.dynf.

Next, we wish to test the resulting temperature and LC in response to an increase in ethylene mass flow rate. Specifically, we re-save WS7.4a.dynf as WS7.4b.dynf and use the latter file for our controller testing. We make initialization, steady-state and dynamic runs of WS7.4b.dynf to pause at 10 hr and then increase the ethylene mass flow to both reactors R1 and R2: Stream C21 → Right-click Forms → Manipulate → Change FmR (specified total mass flow) from 5700 to 7000 kg/hr; do the same for Stream C22 and change the mass flow from 5400 to 7000 kg/hr. Run the dynamic simulation again until 30 hr. Follow Figure 7.21 to display the resulting plots for the temperature and LC.

Figure 7.40 shows that after increasing the ethylene feed mass flow for both reactors at 10 hr, the temperature and LCs for both reactors respond quickly to return to the setpoints.

We can fine-tune the controller parameters by following the following heuristics:

(1) When we make a small step change in the setpoint for process variable for a particular controller, if a dynamic run approaches the setpoint but does not flatten out at the setpoint value, we increase the integral time for the controller.

(2) If the dynamic run meets the setpoint but takes too long to do so, we increase the proportional gain for the controller. If the controller displays unstable behavior (not settling to a steady state), we decrease the gain.

(3) Iterate between these two adjustments until sufficiently tight control of the process variable occurs.

(4) Note that poor performance by one controller can affect the performance of other controllers. We should simultaneously monitor the control plots for all controllers when adjusting parameters for each one individually.

#### 7.6.3 Simulation of Grade-Change Operations

Table 7.15 summarizes the key process and quality variables for WS7.4.

---

<!-- PDF page 404 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>Process Variable C</th><th style='text-align: center;'>-D- Controller Output G/hr</th><th style='text-align: center;'>-Set Point C</th><th style='text-align: center;'>-23.5</th><th style='text-align: center;'>-21.0</th><th style='text-align: center;'>-18.5</th><th style='text-align: center;'>-16.0</th><th style='text-align: center;'>-10.0</th><th style='text-align: center;'>-5.0</th><th style='text-align: center;'>0.0</th><th style='text-align: center;'>5.0</th><th style='text-align: center;'>10.0</th><th style='text-align: center;'>15.0</th><th style='text-align: center;'>20.0</th><th style='text-align: center;'>25.0</th><th style='text-align: center;'>30.0</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>95.0</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>10.0</th><th style='text-align: center;'>70.0</th><th style='text-align: center;'>70.0</th><th style='text-align: center;'>70.0</th><th style='text-align: center;'>70.0</th></tr></thead>
  <tbody>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>Process Variable m</th><th style='text-align: center;'>Set Point m</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>21000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>21000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>22000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>23000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>24000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>25000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>26000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>27000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>28000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>29000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>30000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>31000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>32000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>33000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>34000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>35000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>36000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>37000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>38000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>39000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>40000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>41000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>42000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>43000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>44000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>45000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>46000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>47000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>48000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>49000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>50000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>51000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>52000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>53000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>54000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>55000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>56000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>57000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>58000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>59000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>60000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>61000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>62000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>63000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>64000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>65000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>66000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>67000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>68000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>69000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>70000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>71000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>72000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>73000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>74000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>75000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>76000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>77000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>78000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>79000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>80000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>81000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>82000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>83000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>84000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>85000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>86000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>87000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>88000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>89000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>90000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>91000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>92000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>93000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>94000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>95000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>96000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>97000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>98000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>99000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>100000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>101000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>102000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>103000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>104000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>105000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>106000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>107000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>108000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>109000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>110000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>111000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>112000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>113000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>114000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>115000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>116000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>117000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>118000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>119000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>120000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>121000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>122000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>123000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>124000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>125000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>126000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>127000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>128000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>129000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>130000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>131000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>132000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>133000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>134000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>135000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>136000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>137000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>138000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>139000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>140000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>141000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>142000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>143000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>144000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>145000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>146000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>147000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>148000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>149000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>150000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>151000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>152000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>153000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>154000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>155000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>156000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>157000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>158000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>159000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>160000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>161000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>162000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>163000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>164000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>165000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>166000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>167000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>168000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>169000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>170000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>171000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>172000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>173000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>174000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>175000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>176000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>177000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>178000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>179000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>180000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>181000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>182000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>183000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>184000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>185000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>186000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>187000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>188000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>189000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>190000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>191000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>192000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>193000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>194000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>195000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>196000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>197000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>198000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>199000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>200000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>201000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>202000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>203000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>204000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>205000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>206000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>207000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>208000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>209000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>210000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>211000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>212000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>213000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>214000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>215000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>216000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>217000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>218000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>219000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>220000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>221000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>222000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>223000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>224000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>225000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>226000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>227000.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>Process Variable m</th><th style='text-align: center;'>Set Point m</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>10.2</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>20.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>21.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>21.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>22.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>22.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>23.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>23.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>24.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>24.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>25.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>26.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>26.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>27.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>27.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>28.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>28.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>29.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>29.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.40 Temperature and level controllers for both reactors R1 and R2 respond quickly to return to the setpoints after an increase in ethylene mass flow at 10 hr.</div>


Table 7.16 summarizes the operational details of four HDPE grades that we wish to produce.

For the purpose of demonstrating grade change in this case, we only vary the Hydrogen flow (H21, H22) and the Comonomer flow (C42) here, keeping the rest of the variables the same. Following the illustration of Figure 7.27 to Figure 7.34, we define tasks G1 to G4 under Flowsheet → Contents of Flowsheet → Add Task. Figure 7.41 shows the details of task G1. Here, we use the SRAMP function explained previously in Figure 7.31. Basically, SRAMP(Streams("H21"). FmR,4,4) changes the mass flow rate of stream H21 according to the shape of a sinusoidal curve to 4 kg/hr over an interval of 4 time units.

Following Figure 7.41 and Table 7.16, we complete the specifications of tasks G2–G4 in the same way.

We compiled all four tasks and find no errors.

We create the plots for calculated process quality variables, such as melt index (MI) and copolymer density, based on empirical correlations suggested by Sinclair [8] that we used in Eq. (5.16) and (5.17). Specifically, we correlate plant data for MI as a function of the MWW of the HDPE product according to the equation:

 $$ \mathrm{MI}=\mathrm{A\_MI}\Big(\frac{\mathrm{MWW}}{\mathrm{C\_MI}}\Big)^{\mathrm{B\_MI}} $$ 

For illustrative purposes, we assume A_MI = 901, B_MI = -5, and C_MI = 1e5. When plant data for MI are available, the reader can regress new values of A_MI and

---

<!-- PDF page 405 -->

<div style="text-align: center;">Table 7.15 Process and quality variables for WS7.4.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process variable</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C21</td><td style='text-align: center; word-wrap: break-word;'>Ethylene monomer flow in the feed to the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H21</td><td style='text-align: center; word-wrap: break-word;'>Hydrogen flow in the feed to the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>Catalyst flow to the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX1</td><td style='text-align: center; word-wrap: break-word;'>Solvent (n-hexane) flow to the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C42</td><td style='text-align: center; word-wrap: break-word;'>1-Butene co-monomer flow to the second reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C22</td><td style='text-align: center; word-wrap: break-word;'>Ethylene monomer flow to the second reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H22</td><td style='text-align: center; word-wrap: break-word;'>Hydrogen flow to the second reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX2</td><td style='text-align: center; word-wrap: break-word;'>Solvent (n-hexane) flow to the second reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Quality variable</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MWW</td><td style='text-align: center; word-wrap: break-word;'>Weight-average molecular weight of polymer in outlet stream</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SFRAC</td><td style='text-align: center; word-wrap: break-word;'>Co-monomer fraction in outlet polymer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Rate_pol</td><td style='text-align: center; word-wrap: break-word;'>Polymer flow rate in outlet stream</td></tr></table>

<div style="text-align: center;">Table 7.16 Values of process variables for grades 1 to 4.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Current</td><td style='text-align: center; word-wrap: break-word;'>Grade 1</td><td style='text-align: center; word-wrap: break-word;'>Grade 2</td><td style='text-align: center; word-wrap: break-word;'>Grade 3</td><td style='text-align: center; word-wrap: break-word;'>Grade 4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tasks G1 to G4 run at</td><td style='text-align: center; word-wrap: break-word;'>@0 hr</td><td style='text-align: center; word-wrap: break-word;'>G1 @5 hr</td><td style='text-align: center; word-wrap: break-word;'>G2 @40 hr</td><td style='text-align: center; word-wrap: break-word;'>G3 @80 hr</td><td style='text-align: center; word-wrap: break-word;'>G4 @120 hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H21, kg/hr</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H22, kg/hr</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.75</td><td style='text-align: center; word-wrap: break-word;'>0.75</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C42, kg/hr</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>750</td><td style='text-align: center; word-wrap: break-word;'>750</td><td style='text-align: center; word-wrap: break-word;'>900</td></tr></table>

B_MI. Additionally, we correlate the copolymer density (DENSITY) in kg/m³ by the equation:

 $$ \mathrm{DENSITY}/1000=0.996-\mathrm{A.DN(SFRAC_{-}Comonomer)}^{\mathrm{B.DN}} $$ 

where SFRAC_Comonomer is the mole fraction of segments of the comonomer, butene ( $ C_4H_8 $), and the assumed correlation parameters A_DN = 0.02386 and B_DN = 0.514.

To implement these correlations in the simulation, we right-click Flowsheet within Contents of Flowsheet and choose Edit to open the Constraints-Flowsheet window, and enter the correlations following Figure 7.42. Be sure to compile the equations entered following the example of Figure 7.28b to ensure that there is no coding error.

After compiling the flowsheet constraint equations, we right-click Local Variables within Contents of Flowsheet to see the initially calculated values of Density and Melt_Index in the LocalVariables Table. We follow the example of Figure 7.14 to set up a plot named MI_Density. See Figure 7.43.

---

<!-- PDF page 406 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_807_485.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.41 Specification of task G1 to run at 24 hr.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_562_807_875.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.42 Specification of the flowsheet constraints, Ml, and copolymer density correlations.</div>


Next, we create three plots to display: (1) R1_Feeds: mass flow rates (FmR), kg/hr, of H21 feed to reactor R1; (2) R2_Feeds: mass flow rates (FmR), kg/hr, of C42 and H22 feeds to reactor R2; and (3) Polymer: polymer production rate (Rate_pol), kg/hr; MWW, kg/kmol; and to display each y-axis variable on its own y-axis scale, we put the mouse in the middle of the plot, right-click to show “properties,” and choose AxisMap, followed by “One for Each,” indicating one y-axis scale for each variable. See Figure 7.44.

We make initialization and steady-state runs, and then make a dynamic simulation to pause at 150 hr. Figure 7.44 shows the resulting plots of R1_Feeds, R2_Feeds, and Polymer. Before running the dynamic simulation, it is important to activate all tasks G1 to G4 by right-clicking on the task name within Contents of Flowsheet. At the end of 150 hr, if you do not see the result plot spanned over the time range of 0 to 150 hr, then right-click on the plot name (e.g. R1_Feeds) within Contents of

---

<!-- PDF page 407 -->


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Add Form</td><td style='text-align: center; word-wrap: break-word;'>LocalVariables Table</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>☒</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Add Script</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Value</td><td style='text-align: center; word-wrap: break-word;'>Units</td><td style='text-align: center; word-wrap: break-word;'>Spec</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Add Ta...</td><td style='text-align: center; word-wrap: break-word;'>A DN</td><td style='text-align: center; word-wrap: break-word;'>0.02306</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flowsheet</td><td style='text-align: center; word-wrap: break-word;'>A MI</td><td style='text-align: center; word-wrap: break-word;'>490847.</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Blocks</td><td style='text-align: center; word-wrap: break-word;'>B DN</td><td style='text-align: center; word-wrap: break-word;'>0.514</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Streams</td><td style='text-align: center; word-wrap: break-word;'>B MI</td><td style='text-align: center; word-wrap: break-word;'>4.32416</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R1\_Feeds</td><td style='text-align: center; word-wrap: break-word;'>ComponentList</td><td style='text-align: center; word-wrap: break-word;'>Type1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R2\_Feeds</td><td style='text-align: center; word-wrap: break-word;'>Density</td><td style='text-align: center; word-wrap: break-word;'>950.272</td><td style='text-align: center; word-wrap: break-word;'>kg/m3</td><td style='text-align: center; word-wrap: break-word;'>Free</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Polym...</td><td style='text-align: center; word-wrap: break-word;'>Melt Index</td><td style='text-align: center; word-wrap: break-word;'>0 19051</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Free</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML\_Density</td><td style='text-align: center; word-wrap: break-word;'>UserNotes</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reactions</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chemistry</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Structures</td><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LocalVariab...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>MI_Density (kg/m3)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.19</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>100.0</td><td style='text-align: center;'>0.17</td></tr>
    <tr><td style='text-align: center;'>150.0</td><td style='text-align: center;'>0.16</td></tr>
    <tr><td style='text-align: center;'>200.0</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>250.0</td><td style='text-align: center;'>0.14</td></tr>
    <tr><td style='text-align: center;'>300.0</td><td style='text-align: center;'>0.13</td></tr>
    <tr><td style='text-align: center;'>350.0</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>400.0</td><td style='text-align: center;'>0.11</td></tr>
    <tr><td style='text-align: center;'>450.0</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>500.0</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>550.0</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>600.0</td><td style='text-align: center;'>0.07</td></tr>
    <tr><td style='text-align: center;'>650.0</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>700.0</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>750.0</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>800.0</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>850.0</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>900.0</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>6950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>7950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>8950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>9950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>11950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>12950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>13950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14350.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14400.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14450.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14500.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14550.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14600.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14650.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14700.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14750.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14800.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14850.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14900.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>14950.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15000.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15050.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15100.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15150.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15200.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15250.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15300.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>15350.0</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.43 Setting up a figure of calculated melt index and copolymer density.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (Hr)</th><th style='text-align: center;'>STREADLY-HQ7 FMR Y/H%</th><th style='text-align: center;'>STREADLY-HQ7 FMR Y/H%</th><th style='text-align: center;'>0.025</th><th style='text-align: center;'>0.05</th><th style='text-align: center;'>0.075</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.44 Evolution of feed mass flow rates for producing grades G1–G4.</div>


Flowsheet and choose “Show as Plot.” You will then see the complete results as plotted in Figure 7.44. You can also see the evolution of the computed MI and copolymer density in Figure 7.45.

#### 7.7 Workshop 7.5: Dynamic Simulation and Control of a Commercial Slurry HDPE Process

#### 7.7.1 Objectives

We wish to demonstrate how to implement various control schemes in a commercial slurry HDPE process. We introduce the use of flowsheet variables and constraints, and ratio block in implementing the actual controller configuration in a commercial process.

#### 7.7.2 Converting a Steady-State Simulation Model to a Dynamic Simulation Model

We open a steady-state simulation model, WS7.5.bkp, representing a set of reactors and separators in a parallel-flow slurry HDPE process. For simplicity, we use

---

<!-- PDF page 408 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (h)</th><th style='text-align: center;'>Mell_Index</th><th style='text-align: center;'>Density kg/m3</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>8.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>9.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>0.944</td><td style='text-align: center;'>0.9425</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.45 Evolution of the computed melt index and copolymer density.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_579_812_881.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.46 A steady-state simulation flowsheet for WS7.5.</div>


single-site kinetics in developing the steady-state simulation file in this example. This assumption does not affect our procedure for dynamic simulation and control. Figure 7.46 shows a steady-state simulation flowsheet, in which M1 is a mixer, D201 is a reactor, 201F and D205 are flash units, C201 is a compressor, E201 is an exchanger, P202 is a pump, and S1 and S2 are flow splitters. The reader may see the inputs for steady-state simulation in the Aspen Plus simulation file.

Table 7.17 shows the dynamic data for WS7.5.

We complete the dynamic data according to Table 7.17. After running the steady-state simulation, we export the simulation from Aspen Plus to AD and save the resulting dynamic simulation file, WS7.5.dynf, and the Aspen Property problem definition file, WS7.5dyn.appdf. Figure 7.47 shows the resulting flowsheet with the added default controllers.

---

<!-- PDF page 409 -->

<div style="text-align: center;">Table 7.17 Dynamic specifications for WS7.5.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>201F</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous flash with no dynamic effects</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D205</td><td style='text-align: center; word-wrap: break-word;'>Vertical vessel, elliptical, length = 4.85 m, diameter = 2.5 m, heat-transfer option - constant duty, initial condition - liquid volume fraction = 0.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C201</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous compression</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D201</td><td style='text-align: center; word-wrap: break-word;'>Vertical vessel, elliptical, length = 6.678 m, heat-transfer option - constant duty, initial condition - liquid volume fraction = 0.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E201 and E2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous heat transfer, heat-transfer option - constant duty</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M1</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous mixing</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_494_780_840.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.47 The starting dynamic simulation flowsheet for WS7.5.dynf.</div>


#### 7.7.3 Initial Adjustments of the AD Model

##### 7.7.3.1 Polymer Attributes for Streams and Blocks

We follow the path: Flash unit 201F→Overhead stream RG→Right-click Forms→We do not see “PolymerInputs Table,” indicating that stream RG does not contain polymer components.

##### 7.7.3.2 Implementation of Reactor Level Control Using Mechanical Weir

The reactor D201 has no LC, but it has a weir. We delete the default controller D201_LC and two associated control signals. We enter the equations for weir in the flowsheet form (Exploring-Simulation→Flowsheet→Contents of Flowsheet→Flowsheet→Right-click Edit→Constraints→Flowsheet variables and equations), as illustrated in Figure 7.48:

We note that the weir constant, K_weir, results from: (1) the current slurry mass flow rate, STREAMS("SLURRY").FmR of 18254.9 kg/hr; (2) D201 liquid level,

---

<!-- PDF page 410 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_148_808_291.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.48 Using flowsheet constraints to define the weir variables and equations.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_357_767_513.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 7.49 Access to Local Variables Table for values of weir constants in flowsheet constraint variables and equations.</div>


BLOCKS(“D201”).level of 4.82869 m; and (3) weir height, h_weir of 4.8 m; and K_weir = 18254.9 kg/hr/(4.82869 - 4.8) m = 636,238 kg/hr-m.

We will explain the pressure/flow equation with a valve flow constant,  $ C_{v\_E201} $, in Figure 7.48 shortly below.

When we compile the flowsheet form after adding the weir equations, we find that the model is overspecified by one variable. We free the weir constant (K_weir) and run the simulation. The computed value for K_weir appears in the Local Variables table within the Contents of Flowsheet. See Figure 7.49.

##### 7.7.3.3 Improvement of the Reactor Temperature Controller

The reactor has a temperature controller that adjusts the amount of overhead gas exiting the compressor, stream C201OUT, that recycles to the reactor inlet, stream RE-G. The remainder of this stream, stream RE-E201, enters cooler E201 with the vapor outlet of the reactor, stream RG. We reconnect the temperature controller D201_TC to stream splitter S1 and choose the fraction leaving in stream RE-G as the manipulated variable. We double-click the temperature controller, click the Configure button, and enter the temperature controller parameters according to Table 7.8. We make the controller Direct because an increase in reactor temperature should result in an increase in the amount of vapor sent back to the reactor via stream RE-G. We initialize the controller, run it in steady state, and save the snapshot.

The temperature controller does not operate correctly until we add a Flowsheet Constraint to Figure 7.48 to compute the pressure at the outlet of heat exchanger E201. The equation computes the pressure drop across the heat exchanger using the following relation:

 $$  Flow_{E201OUT}=C_{v}\sqrt{\Delta P} $$ 

where  $ C_{v} $ is a valve flow constant and  $ \Delta P $ is the pressure drop across the heat exchanger. See Figure 7.50. When we compile the flowsheet form, the model is

---

<!-- PDF page 411 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_147_780_328.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.50 Adding the flowsheet constraint to compute pressure drop across exchanger E201.</div>


overspecified by one variable. We free the valve constant and make a steady-state run. This computes the valve constant. We then fix the valve constant and free the mass flow in stream RG. We save a snapshot of the steady-state run.

##### 7.7.3.4 Deletion of Pressure Controllers

We delete the pressure controllers, D201_PC and D205_PC and the associated control signals, as the actual plant does not have these controllers.

##### 7.7.3.5 Adding a Hydrogen–Ethylene Ratio Controller to the Recycle Gas

There is a controller that manipulates the feed rate of hydrogen and the purge rate from vessel D205 to maintain the hydrogen–ethylene ratio in the recycle gas. The process variable for this controller is the hydrogen–ethylene ratio in the recycle-gas stream. We must introduce three blocks to the dynamic model when implementing this controller. See Figure 7.51.

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_770_780_1238.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.51 Adding a hydrogen–ethylene ratio controller to the recycle gas.</div>


---

<!-- PDF page 412 -->

The first block is a Ratio block, which computes the ratio of the mole flow of hydrogen, STREAMS("205V").  $ F_{cn}(“H2”) $ as input 1 to that of ethylene, STREAMS("205V").  $ F_{cn}(“C2H4”) $ as input 2 in the recycle gas, stream 205V. The controller output is the computed mole ratio of hydrogen to ethylene.

The second block is a PID controller that accepts the hydrogen–ethylene ratio from the ratio block. We name the controller as H2C2 and specify its controller action as reverse. We set the proportional gain and integral time according to those for composition controllers in Table 7.8. The PID output signal specifies the mass split fraction of the purge stream exiting the flow splitter S2, BLOCKS(“S2”).sf(“PURGE”).

We open the faceplates and plots for controllers H2C2, D205_LC, and D201_TC, make initialization and steady-state runs, and then make a dynamic run to pause at 10 hr. Figure 7.52 shows that the current controller appears to work properly.

At 10 hr, we increase: (1) the specified ethylene mass flow rate from 5950 to 7500 kg/hr (STREAM C2 → Right-click Forms → AllVariables → FmR, specified total mass flow), We then run dynamic simulation to pause at 20 hr. Figure 7.53 shows the performance plots of the three controllers, indicating an acceptable performance.

Now we specifically test the critical PID H2/C2 controller against a change in input ethylene flow rate (STREAMS("C2").FmR. We increase: (1) the flow rate of ethylene from 7500 to 9000 kg/hr; (2) the specified catalyst total mass flow rate from 49.206 to 60 kg/hr (STREAM CAT → Right-click Forms → AllVariables → FmR,

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_708_809_922.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.52 Performance of the current ratio, level, and temperature controllers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_993_809_1251.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.53 Performance of controllers after increasing ethylene mass flow rate to 7500 kg/hr.</div>


---

<!-- PDF page 413 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_150_779_356.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.54 Performance of controllers after increasing ethylene mass flow rate to 9000 kg/hr, catalyst mass flow rate to 60 kg/hr, and C3 mass flow rate to 100 kg/hr.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_439_667_771.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 7.55 Gain and integral time for the H2C2 controller.</div>


specified total mass flow), and (3) the specified propylene total mass flow rate from 85 to 100 kg/hr (STREAM C3 → Right-click Forms → AllVariables → FmR, specified total mass flow). We run the controllers to pause at 40 hr. Figure 7.54 shows the performance plots. The process output curve matches the set point closely.

For the H2C2 controller, we find the current tuning parameters are: Gain = 35.1131%/% and integral time = 77.76604 min (see Figure 7.55). In the following, we want to learn how to use the tuning tool within the PID controller and check if these tuning parameters are optimal. We first save the simulation file as WS7.5-Final-2.dynf.

Next, we follow the heuristic gain and integral time for a composition controller given in Table 7.8 and change the gain displayed in Figure 7.55 to 0.1 and the integral time to 0.2 min, and initialize values. We then follow the following procedure to tune the controller parameters.

1) Run the simulation in Dynamic run mode for a few steps.

2) Pause the simulation.

3) Open the controller Faceplate.

4) Display the result plot.

5) Click the tune button. See the resulting Figure 7.56.

6) Click the <Start Test> button, as seen in Figure 7.56.

---

<!-- PDF page 414 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_147_626_439.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 7.56 Controller “Tune” interface.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_165_508_626_717.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 7.57 Choosing tuning rule.</div>


7) Run the simulation, and you should observe that the OP of the controller is stepped up, and the ratio on the stage PV increases. Pause the simulation when it reaches steady state. Click Finish Test on the controller-tuning sheet.

8) Click the Tuning parameters tab.

9) Select the tuning method (PI controller and Cohen-Coon tuning rule). Click the <Calculate> button. See Figure 7.57. The reader may search Aspen Dynamics online help for “Cohen-Coon” about explanations of different tuning rules.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_982_626_1219.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 7.58 Updated tuning parameters.</div>


---

<!-- PDF page 415 -->

<div style="text-align: center;">Figure 7.59 Continually decaying response resulting from the updated tuning parameters.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_377_144_798_544.jpg" alt="Image" width="43%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time Hours</th><th style='text-align: center;'>Process Variable</th><th style='text-align: center;'>Set Point</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>22.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>27.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>32.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>37.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>42.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>45.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>47.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>52.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>55.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>57.5</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>60.0</td><td style='text-align: center;'>0.0000</td><td style='text-align: center;'>0.0000</td></tr>
  </tbody>
</table>

10) You click <Update Controller> the new settings are applied. Restart the simulation. Click the Update controller button. We see the updated tuning parameters in Figure 7.58, and the continually decaying controller response in Figure 7.59. This concludes the current workshop. We save the simulation file as WS5.3-Final-3.dynf.

#### 7.8 Workshop 7.6: Dynamic Simulation and Control of a Gas-Phase Fluidized-Bed Process for Producing LLDPE in Condensed Mode Operation

#### 7.8.1 Objectives

We want to show how to implement various control schemes in a gas-phase fluidized-bed process for producing LLDPE in a condensed mode operation that we covered in Section 5.8. We demonstrate reactor pressure control using a split-range controller.

#### 7.8.2 Converting a Steady-State Simulation Model to a Dynamic Simulation Model

Referring to Figure 5.71, we open the simulation file WS7.6_LLDPE.bkp. Figure 7.60 shows the resulting flowsheet.

Table 7.18 gives the dynamic specifications for the current workshop.

We complete the dynamic data according to Table 7.18. After running the steady-state simulation, we export the simulation from Aspen Plus to AD and save the resulting dynamic simulation file, WS7.6.dynf, and the Aspen Property problem definition file, WS7.6dyn.appdf. Figure 7.61 shows the resulting flowsheet with the added default controllers.

---

<!-- PDF page 416 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_150_741_356.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 7.60 Process flowsheet for LLDPE for WS7.6.</div>


<div style="text-align: center;">Table 7.18 Dynamic specifications for WS7.6.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Block</td><td style='text-align: center; word-wrap: break-word;'>Specifications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COMP</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous compression</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REACT</td><td style='text-align: center; word-wrap: break-word;'>Vertical vessel, elliptical head, length = 3.5 m, heat-transfer option - constant duty</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COOL</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous heat transfer, heat-transfer option - constant duty</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MIX1, MIX2</td><td style='text-align: center; word-wrap: break-word;'>Instantaneous mixing</td></tr></table>

<div style="text-align: center;">Table 7.19 Default controller specifications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Controller</td><td style='text-align: center; word-wrap: break-word;'>Manipulated variable</td><td style='text-align: center; word-wrap: break-word;'>Controlled variable</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REACT_LC</td><td style='text-align: center; word-wrap: break-word;'>POWDER liquid mass flow rate</td><td style='text-align: center; word-wrap: break-word;'>REACT liquid level</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REACT_TC</td><td style='text-align: center; word-wrap: break-word;'>REACT heat duty</td><td style='text-align: center; word-wrap: break-word;'>REACT temperature</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REACT_PC</td><td style='text-align: center; word-wrap: break-word;'>RECY1 vapor molar flow rate</td><td style='text-align: center; word-wrap: break-word;'>REACT pressure</td></tr></table>

As the RECY1 vapor recycle molar flow rate tends to increase, leading to an increase in the reactor pressure, we need a better control scheme for the reactor pressure. We want to introduce a SR (split-range) controller for our reactor pressure control. Referring to Figure 7.62, we see that valve A opens when the controller output goes from 0% to 50% and valve B opens when the controller output goes from 51% to 100%.

Figure 7.63 shows a modified flowsheet where we have added a SR controller and the PC controller output, BLOCKS("REACT_PC"), becomes the input to the SR controller. When this PC controller output is between 0 and 50%, the manipulated variable for the PC controller is the mass flow rate of N2 in the FEED stream, STREAMS("FEED"). FmcR("N2"), whose value is bounded between 0 and 100 kg/hr. When this PC controller output is between 51% and 100%, the manipulated variable for the PC controller is the split fraction for the PURGE stream, BLOCKS("SPLIT").sf("PURGE"), whose value is bound between 1E-6 and

---

<!-- PDF page 417 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_150_781_532.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.61 Dynamic simulation flowsheet with default controllers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_618_580_851.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">Figure 7.62 An illustration of a split-range (SR) controller.</div>


0.1. We follow the path: Controller SplitRange → Right-click “Forms” → Configure: See Figure 7.64.

We run the dynamic simulation to pause at 5 hr. We find that the controllers perform correctly. We save the converged simulation file as WS7.6-1_LLDPE.dynf for possible future use. We then re-save the simulation file as WS7.6-2_LLDPE.dynf before we change the FEED pressure from 30 to 25 bar. We then run the dynamic simulation to pause at 15 hr. Figure 7.65 displays that in response to the FEED pressure decrease from 30 to 25 bar, the pressure controller performs correctly. As the controller output is at 12.75%, the SR controller activates an increase in the N2 mass flow rate from 25 to 46.4267 kg/hr while keeping the PURGE split fraction unchanged and the reactor pressure at the set point of 21.6975 bar.

This concludes the current workshop. We save the simulation file as WS7.6-2_LLDPE.dynf.

---

<!-- PDF page 418 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_811_472.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.63 A modified dynamic process simulation flowsheet with a split-range controller.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">SplitRange.Configure Table</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Value</td><td style='text-align: center; word-wrap: break-word;'>Units</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output1Action</td><td style='text-align: center; word-wrap: break-word;'>Action for Output 1</td><td style='text-align: center; word-wrap: break-word;'>Reverse</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output1Min</td><td style='text-align: center; word-wrap: break-word;'>Minimum value of Output 1</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output1Max</td><td style='text-align: center; word-wrap: break-word;'>Maximum value of Output 1</td><td style='text-align: center; word-wrap: break-word;'>100.0</td><td style='text-align: center; word-wrap: break-word;'>kg/hr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output1Min</td><td style='text-align: center; word-wrap: break-word;'>Value of input above which Output 1 starts to change</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output1MinMax</td><td style='text-align: center; word-wrap: break-word;'>Value of input above which Output 1 stops changing</td><td style='text-align: center; word-wrap: break-word;'>50.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output2Action</td><td style='text-align: center; word-wrap: break-word;'>Action for Output 2</td><td style='text-align: center; word-wrap: break-word;'>Direct</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output2Min</td><td style='text-align: center; word-wrap: break-word;'>Minimum value of Output 2</td><td style='text-align: center; word-wrap: break-word;'>1.e-006</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output2Max</td><td style='text-align: center; word-wrap: break-word;'>Maximum value of Output 2</td><td style='text-align: center; word-wrap: break-word;'>0.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output2InMin</td><td style='text-align: center; word-wrap: break-word;'>Value of input above which Output 2 starts to change</td><td style='text-align: center; word-wrap: break-word;'>50.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Output2InMax</td><td style='text-align: center; word-wrap: break-word;'>Value of input above which Output 2 stops changing</td><td style='text-align: center; word-wrap: break-word;'>100.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 7.64 The configuration specifications of the split-range controller.</div>


#### 7.9 Workshop 7.7: Dynamic Simulation and Control of a Slurry HDPE Process Using an Inferential Controller

#### 7.9.1 Objective

The objective of this workshop is to develop an inferential control for MI measurement in a HDPE production process. The controller controls the MI to target and minimize the difference between the target and measured MI values during grade transitions. We perform grade transition of the polymer for different MI values using the inferential controller, and we also try to improve the controller to minimize the off-spec product.

#### 7.9.2 Inferential Control Theory and Recent Applications

In many industrial processes, it is difficult to measure certain product quality targets. In such cases, we measure some secondary process outputs to correlate the product

---

<!-- PDF page 419 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_148_778_454.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.65 Keeping the reactor pressure at 21.6975 bar by increasing the mass flow rate of N2 from 25 to 46.4267 kg/hr as determined through a split-range controller.</div>


quality with primary outputs for quality control. The additional measurement of the secondary output gives an inference on the key unmeasured variables, which is often called inferential control [9–12].

Inferential controllers use simple models to predict the controlled variables using plant measurements such as raw material feed rates and reactor temperature. Once a measurement is available for the controlled variable, we compare the measurement with the model prediction to adjust the model. The model can then recommend a new control action.

In one of the first applications of inferential controllers, Joseph and Brosilow [13] apply the inferential control to adjust the column temperature in a petroleum process. They build steady-state and dynamic inferential control systems [14]. Parrish and Brosilow [15] showcase how an inferential controller performs better than a cascade PID controller when applied to heat exchanger and industrial reactor control.

In a recent application, Wang et al. [16] use the inferential control for temperature and simultaneous composition control of a divided wall column. Behrooz [17] uses inferential control for controlling the product quality of crude oil distillation using stochastic optimization. Choi et al. [18] apply inferential control for controlling the grade transition in pulping process. Durr et al. [19] use the inferential control for controlling the quality of produced granules in a fluidized-bed process. Pachauri et al. [20] apply the inferential control to control a fermentation process by maintaining product ethanol concentrations.

In polymer processes, the product quality measurements, such as MI, are sparse and not very accurate. Therefore, control becomes important for reaching the quality target. MI is dependent on the hydrogen flow rate, which becomes an important manipulated variable. However, using a traditional feedback controller is inefficient, because the plant will only measure the MI of the product once every six hours, and there is a long-time delay between where the hydrogen is fed to where the MI is measured. That is why we need an inferential controller for MI. Ogawa et al. [9] use inferential control for quality control of a HDPE process in one of the earliest

---

<!-- PDF page 420 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_148_810_326.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 7.66 A simplified steady-state flowsheet for a slurry HDPE process.</div>


applications to polymer processes. Oshima and Tanigaki [12] apply the inferential control for optimizing grade change.

#### 7.9.3 HDPE Process Description and Steady-State Model Empirical Correlation

We consider a single CSTR for modeling the HDPE process. With a HDPE production rate of 5 metric tons (MT) per hour and product grades with MI values of 1–20, we wish to optimize the grade transition while minimizing the amount of off-spec product. The HDPE process also consists of a centrifuge and extruder, which we do not model. This follows because we can approximate the MI of product in the downstream process by the MI value at the reactor outlet by considering the time lag.

We first make a steady-state HDPE model with a single CSTR. Figure 7.66 shows a simplified HDPE process flowsheet with a single reactor and a flash drum. We save the simulation file as WS7.7.bkp. MI is dependent on the hydrogen feed flow, which represents an inferential variable. We use the model to determine an empirical correlation of MI with hydrogen feed flow rate by simulating data with different hydrogen flow rates, keeping other variables constant, and calculating the product MI value.

We approximate the steady-state MI data given in WS7.7.xlsx by the following empirical equation applicable to the current problem:

 $$ \ln(\mathrm{MI_{i}})=3.266\ln(\mathrm{H_{2}})-3.215 $$ 

We refer to this steady-state  $ MI_{i} $ as the instantaneous MI, which is a function of the hydrogen feed flow rate ( $ H_{2} $). Based on the steady-state model, we can calculate the hydrogen feed flow value for a particular MI grade.

We convert the steady-state model to a dynamic model, as shown in Figure 7.67. We save the dynamic simulation file as WS7.7.dynf and the property file as WS7.7.dyn.appdf. We leave the default controller settings for the temperature (R1_TC) and level control (R1_LC), but delete the pressure controller since it is not critical for the liquid-phase reactor.

We consider the industrial correlation [21] of the MI as function of the MWW reactor outlet MI and assume that as the plant data.

 $$ \mathrm{Melt\_Index}=(11152.5/\mathrm{MWW})^{3.472} $$ 

---

<!-- PDF page 421 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_148_769_327.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.67 Dynamic HDPE process flowsheet.</div>


Following WS7.4 and Figure 7.41, we enter the MI correlation as a flowsheet constraint within AD as follows:

# Plant model (industrial MI correlation)
A_MI as realparameter(11152.5);
B_MI as realparameter(3.472);
Plant_MI as positive;
Melt_Index = (A_MI / (STREAMS("R1OUT").MWW))^B_MI;

where A_MI and B_MI are the parameters and STREAMS("R1OUT"), and MWW is the weight-average molecular weight of the polymer at the reactor outlet.

#### 7.9.4 Grade-Change Transition Using Basic H2-Based Controller

The basic traditional methodology of grade change is to change the grades by changing the hydrogen feed flow rate. From the steady-state model, we calculate the H2 feed flow value to produce a particular polymer MI. To change the grade from MI of value 10 to 20, we increase the hydrogen flow rate from 5.41 to 6.68 kg/hr, using the steady-state values obtained from the model to reach the respective MI value. Following our discussion of AD task in Section 7.5, and examples of tasks in Figures 7.28–7.33 and in Figure 7.41, we define the following task to increase H2 flow (STREAMS("H2").FmR) in minimum time (0.1 hr).

#Task for grade change using basic control using H2 feed flow rate
Task M1 runs at 5
SRamp (STREAMS ("H2").FmR, 6.68, 0.1);
End

This basic control grade-change process will lead to grade change, but with a constant H2-setpoint-based control, the transition will be slower, leading to a much larger amount of off-spec product. For the mentioned grade change, the amount of off-spec material is approximately 75 MT in 15 hr, as shown in Figure 7.68. Therefore, introducing an inferential control would become useful in reducing the off-spec material, as it would constantly update the hydrogen setpoint based on the controller error difference between the cumulative MI and the target MI.

---

<!-- PDF page 422 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Manual_Control</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>20.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.68 Grade change using H2-setpoint-based controller.</div>


#### 7.9.5 Open-Loop Inferential Controller Using Dynamic Model

To find a dynamic inferential control relationship, we use the methodology showcased by Ogawa et al. [9] to calculate the cumulative MI exiting the reactor. They derive the ordinary differential equation (ODE) using mass balance, quantifying the relation between the instantaneous MI and the cumulative MI formed at the exit of the reactor.

 $$ \frac{\mathrm{d}\ln(MI_{c}(t))}{dt}=\frac{1}{\tau_{1}}\log(\mathrm{MI}_{i}(t))-\frac{1}{\tau_{1}}\log(\mathrm{MI}_{c}(t)) $$ 

where  $ MI_{i} $ is the instantaneous MI and  $ MI_{c} $ is the cumulative MI at the exit of the reactor.

We substitute Eq. (7.4) into Eq. (7.6) to calculate the cumulative MI and then use the dynamic model to tune the time constant  $ \left(\tau_{1}\right) $ and build an inferential controller.

We model the inferential controller by simulating the dynamic differential equation (7.6) and try to iterate for an appropriate value of time constant so that the inferential model matches the plant MI correlation (7.5) with error less than 5% described by the industrial correlation. We find that a value of time constant of 4.077 hr gives a good match between plant and model values, as shown in Figure 7.69. By substituting Eq. (7.4) into Eq. (7.5) and considering value of time constant, we find the inferential model ODE as Eq. (7.7):

 $$ \frac{\mathrm{d}\left(\ln\left(MI_{c}\right)\right)}{\mathrm{d}t}=\frac{1}{4.077}\left[3.266\ln\left(\mathrm{H}_{2}\right)-3.215-\ln\left(\mathrm{MI}_{c}\right)\right] $$ 

MI $ _c $ gives the cumulative MI at the exit of the reactor, and its logarithm is defined as log\_mi in the AD tasks. The hydrogen feed flow rate (H $ _2 $) is represented by STREAMS("H2").FmR in the AD model. It is defined this way since AD does not allow the logarithm of a differential.

---

<!-- PDF page 423 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Mel_loss (pred. h)</th><th style='text-align: center;'>90.10</th><th style='text-align: center;'>90.70</th><th style='text-align: center;'>90.90</th><th style='text-align: center;'>90.95</th><th style='text-align: center;'>90.98</th><th style='text-align: center;'>90.99</th><th style='text-align: center;'>91.00</th><th style='text-align: center;'>91.01</th><th style='text-align: center;'>91.02</th><th style='text-align: center;'>91.03</th><th style='text-align: center;'>91.04</th><th style='text-align: center;'>91.05</th><th style='text-align: center;'>91.06</th><th style='text-align: center;'>91.07</th><th style='text-align: center;'>91.08</th><th style='text-align: center;'>91.09</th><th style='text-align: center;'>91.10</th><th style='text-align: center;'>91.11</th><th style='text-align: center;'>91.12</th><th style='text-align: center;'>91.13</th><th style='text-align: center;'>91.14</th><th style='text-align: center;'>91.15</th><th style='text-align: center;'>91.16</th><th style='text-align: center;'>91.17</th><th style='text-align: center;'>91.18</th><th style='text-align: center;'>91.19</th><th style='text-align: center;'>91.20</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.69 Comparison of MI values from the open-loop inferential control MI (predicted_MI) with the actual correlation-based MI (Melt_Index) (time constant = 4.07 hours).</div>


The flowsheet constraint commands for simulating the differential equation model are given below:

#Open Loop Inferential Model ODE
log_mi as realvariable;
$log_mi = (1/4.0775)*( (3.266*LOGe(STREAMS("H2").FmR))
- 3.2157 - log_mi);
predicted_mi as realvariable;
predicted_mi = EXP(log_mi);

In order to compare the MI values and iterate the value for the time constant for an open-loop controller, we perform grade transition by changing the values of H2 feed flow for grades of MI 1, 10, and 20 by creating task as explained previously. We change the grades by using tasks to change H2 flow rate (Streams("H2").FmR) at 2 hr to 5.46 kg/hr and at 25 hr to 2.67 kg/hr, respectively, as explained previously. We set the H2 flow rate as a fixed variable prior to implementing the task.

Figure 7.69 compares MI values from the open-loop inferential control with the actual correlation-based MI values at a time constant of 4.07 hr, resulting in the lowest error of 3%.

#### 7.9.6 Closed-Loop Inferential Controller

To automate the inferential controller, we need a closed-loop controller using the open-loop model ODE. This allows us to input a target MI, so that the inferential model can calculate the control action accordingly. To form the closed-loop inferential model, we need to discretize the inferential control ODE using the Euler method.

---

<!-- PDF page 424 -->

and simplify to get the following equation:

 $$ (\ln(\mathrm{MI_{target}})-\ln(\mathrm{MI_{c}}})/\Delta t=(1/4.07)*(3.266\ln(\mathrm{H2_{setpoint}})-3.215-\ln(\mathrm{MI_{c}})) $$ 

where  $ MI_{target} $ is the fixed target MI that the controller needs to achieve, and  $ MI_{c} $ is the cumulative MI at the exit of the reactor. We use the same open-loop time constant 4.07 hr for the closed-loop discretized ODE. Thus, Eq. (7.8) closes the loop since, by inputting a given target MI, it continuously back-calculates the hydrogen setpoint, which can then be used to equate to the hydrogen flow rate, resulting in the inferential control action. The time interval  $ \Delta t $ is a fixed parameter that can be used to tune the controller and reduce overshoot.

Following WS7.4 and Figure 7.42, we enter the closed-loop inferential control as a flowsheet constraint within AD.

#Closed Loop Inferential Control
target_mi as realvariable(fixed,1);
delta_t as realvariable(fixed, 1);
h2_setpoint as realvariable(free);
(LOGe(target_mi)-log_mi)/delta_t = (1/4.0775)*(3.2667*
LOGe(h2_setpoint)) - 3.2157 - log_mi);
h2_setpoint= STREAMS("H2").FmR;

The variables as defined in the constraint are  $ MI_{target} $ as target_mi,  $ Log(MI_C) $ as log_mi, and  $ \Delta t $ as delta_t. We create a new variable called ‘target_mi’ and set it as a fixed variable, and use log_mi as the initial variable condition for the discretized ODE. Also make Streams("H2").FmR as a free variable since it is equal to the H2 setpoint.

Figure 7.70 shows all three flowsheet constraints for the current workshop.

We simulate a grade change from 10 to 20 using AD tasks. The grade change for the MI happens in 5 hr with only 25 MT of off-spec material. Figure 7.71 illustrates

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_930_805_1217.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 7.70 Snapshot of the overall constraints and the local variable specification.</div>


---

<!-- PDF page 425 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>predicted_mi</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>20.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.71 MI grade change from 10 to 20 using inferential control.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Basic control</th><th style='text-align: center;'>Inferential control</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>16.5</td><td style='text-align: center;'>16.5</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>17.5</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>18.2</td><td style='text-align: center;'>18.2</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>18.8</td><td style='text-align: center;'>18.8</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>19.2</td><td style='text-align: center;'>19.2</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>19.7</td><td style='text-align: center;'>19.7</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>19.8</td><td style='text-align: center;'>19.8</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>19.9</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 7.72 Comparison of grade change process using the inferential control with the basic H2-based control.</div>


the inferential model prediction for grade change. The y-coordinate, predicted_mi, represents predicted MI value by the inferential controller.

Thus, we can compare the grade change due to the inferential control Melt Index with the basic constant hydrogen flow-based control, resulting in faster grade transition in inferential control (5 hr) compared to basic control (15 hr). Figure 7.72 illustrates that the inferential control reduces off-spec material by 50 MT and by 10 hr to reach the new MI target. Hence, we have showcased the utility of inferential control for polymer grade change.

---

<!-- PDF page 426 -->

This concludes the current workshop on inferential control applied to grade-change operations of a slurry HDPE process.

## References

1 Khare, N.P., Seavey, K.C., Liu, Y.A. et al. (2002). Steady-state and dynamic modeling of commercial slurry high-density polyethylene (HDPE) processes. Industrial and Engineering Chemistry Research 41: 5601.

2 Khare, N.P., Lucas, B., Seavey, K.C. et al. (2004). Steady-state and dynamic modeling of commercial gas-phase polypropylene processes using stirred-bed reactors. Industrial and Engineering Chemistry Research 43: 884.

3 Zheng, Z.W., Shi, D.P., Su, P.L. et al. (2011). Steady-state and dynamic modeling of the basell multireactor olefin polymerization process. Industrial and Engineering Chemistry Research 50: 322.

4 Luo, Z.H., Su, P.L., Shi, D.P., and Zhang, Z.W. (2009). Steady-state and dynamic modeling of commercial bulk polypropylene process of hypol technology. Chemical Engineering Journal 149: 370.

5 You, C. (2006). Modeling and analysis of polypropylene process in steady and dynamic states. MS thesis. College of Chemical Engineering, Tianjin University.

6 Aspen Technology, Inc. (2020). Aspen Plus Dynamics Online Help, V11. "Troubleshooting Aspen Plus Dynamics".

7 Smith, C.A. and Corripio, A.B. (1997). Principles and Practice of Automatic Process Control, 2e. New York: Wiley.

8 Sinclair, K.B. (1983). Characteristics of Linear LPPE and Description of UCC Gas Phase Process. Process Economics Report. Menlo Park, CA: SRI International.

9 Ogawa, M., Ohshima, M., Morinaga, K., and Watanabe, F. (1999). Quality inferential control of an industrial high density polyethylene process. Journal of Process Control 9: 51.

10 Lou, H.C., Su, H.Y., Xie, L. et al. (2012). Inferential model for industrial polypropylene melt index prediction with embedded priori knowledge and delay estimation. Industrial and Engineering Chemistry Research 51: 8510.

11 Marlin, T.A. (2004). Process Control: Designing Processes and Control Systems for Dynamic Performance, 555–580. McGraw-Hill Inc.

12 Ohshima, M. and Tanigaki, M. (2000). Quality control of polymer production processes. Journal of Process Control 10: 135.

13 Joseph, B. and Brosilow, C.B. (1978). Inferential control of processes: Part I. Steady state analysis and design. AIChE Journal 24: 485.

14 Joseph, B. and Brosilow, C. (1978). Inferential control of processes: Part III. Construction of optimal and suboptimal dynamic estimators. AIChE Journal 24: 500.

15 Parrish, J. and Brosilow, C. (1985). Inferential control applications. Automatica 21: 527.

16 Wang, J., Yu, N., Chen, M. et al. (2018). Composition control and temperature inferential control of dividing wall column based on model predictive control and PI strategies. Chinese Journal of Chemical Engineering 26: 1087.

---

<!-- PDF page 427 -->

17 Behrooz, H.A. (2019). Robust set-point optimization of inferential control system of crude oil distillation units. ISA Transactions 95: 93.

18 Choi, H.-K., Son, S.H., and Sang-Il Kwon, J. (2021). Inferential model predictive control of continuous pulping under grade transition. Industrial and Engineering Chemistry Research 60: 3699.

19 Dürr, R., Neugebauer, C., Palis, S. et al. (2020). Inferential control of product properties for fluidized bed spray granulation layering. IFAC-Papers OnLine 53: 11410.

20 Pachauri, N., Singh, V., and Rani, A. (2017). Two degree-of-freedom PID-based inferential control of continuous bioreactor for ethanol production. ISA Transactions 68: 235.

21 Mattos Neto, A.G., Freitas, M.F., Nele, M., and Pinto, J.C. (2005). Modeling ethylene/1-butene copolymerizations in industrial slurry reactors. Industrial and Engineering Chemistry Research 44: 2697.