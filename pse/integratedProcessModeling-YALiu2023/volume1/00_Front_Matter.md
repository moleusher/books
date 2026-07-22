# Untitled

<!-- PDF page 1 -->

Y.A. Liu and Niket Sharma

# Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing

Volumes 1–2

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_593_964_1381.jpg" alt="Image" width="100%" /></div>


---

<!-- PDF page 2 -->

## WILEY END USER LICENSE AGREEMENT

Go to www.wiley.com/go/eula to access Wiley's ebook EULA.

---

<!-- PDF page 3 -->

## About the pagination of this eBook

This eBook contains a multi-volume set.

To navigate the front matter of this eBook by page number, you will need to use the volume number and the page number, separated by a hyphen.

For example, to go to page v of volume 1, type "1-v" in the Go box at the bottom of the screen and click "Go."

To go to page v of volume 2, type "2-v"... and so forth.

---

<!-- PDF page 4 -->

Integrated Process Modeling,

Advanced Control and Data Analytics for

Optimizing Polyolefin Manufacturing

---

<!-- PDF page 5 -->

Integrated Process Modeling,

Advanced Control and Data Analytics for

Optimizing Polyolefin Manufacturing

---

<!-- PDF page 6 -->

# Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing

Volume 1

Y. A. Liu

Niket Sharma

WILEY vch

---

<!-- PDF page 7 -->

# Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing

Volume 1

Y. A. Liu

Niket Sharma

WILEY vch

---

<!-- PDF page 8 -->

## Authors

##### Prof. Y. A. Liu

Department of Chemical Engineering

Virginia Polytechnic Institute and State

University

635 Prices Fork Road

245 Goodwin Hall

Blacksburg

VA, US, 24061

### Dr. Niket Sharma

Department of Chemical Engineering

Virginia Polytechnic Institute and State

University

635 Prices Fork Road

245 Godwin Hall

Blacksburg

VA, US, 24061

Cover Image:

© metamorworks/Shutterstock

All books published by WILEY-VCH are carefully produced. Nevertheless, authors, editors, and publisher do not warrant the information contained in these books, including this book, to be free of errors. Readers are advised to keep in mind that statements, data, illustrations, procedural details or other items may inadvertently be inaccurate.

Library of Congress Card No.: applied for

British Library Cataloguing-in-Publication Data

A catalogue record for this book is available

from the British Library.

## Bibliographic information published by the Deutsche Nationalbibliothek

The Deutsche Nationalbibliothek lists this publication in the Deutsche Nationalbibliografie; detailed bibliographic data are available on the Internet at <http://dnb.d-nb.de>.

© 2023 WILEY-VCH GmbH, Boschstraße 12, 69469 Weinheim, Germany

All rights reserved (including those of translation into other languages). No part of this book may be reproduced in any form – by photoprinting, microfilm, or any other means – nor transmitted or translated into a machine language without written permission from the publishers. Registered names, trademarks, etc. used in this book, even when not specifically marked as such, are not to be considered unprotected by law.

Print ISBN: 978-3-527-35268-5

ePDF ISBN: 978-3-527-84381-7

ePub ISBN: 978-3-527-84382-4

oBook ISBN: 978-3-527-84383-1

Cover Design: SCHULZ Grafik-Design

Typesetting: Straive, Chennai, India

---

<!-- PDF page 9 -->

## Contents

## Volume 1

Foreword xvii

Preface xxxiii

Acknowledgment xxxvii

Copyright Notice xxxix

About the Authors xli

About the Companion Website xliii

1 Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing 1

1.1 Segment-Based Modeling of Polymerization Processes: Component Characterization and Polymer Attributes 1

1.1.1 Component Types in Polymer Process Modeling 1

1.1.2 Concept of Moments and Some Basic Polymer Attributes 3

1.1.3 Stream Initialization and Basic Polymer Attributes 5

1.2 Workshop 1.1: Finding the Resulting Stream Attributes After Mixing Two Copolymer Streams 7

1.2.1 Objective 7

1.2.2 Problem Statement 7

1.2.3 Process Flowsheet 7

1.2.4 Unit System, Components, and Characterization of Copolymers 7

1.2.5 Property Method and Property Parameters for Components 9

1.2.6 Specifications of Streams and Blocks 11

1.3 Workshop 1.2: A Simplified Simulation Model for a Slurry HDPE Process and the Workflow for Developing a Polymer Process Simulation Model 16

1.3.1 Objective 16

1.3.2 Step 1: Problem Setup 16

1.3.3 Step 2: Component Specifications 18

1.3.4 Step 3: Property Method 20

---

<!-- PDF page 10 -->

1.3.5 Step 4: Property Parameters – Obtaining Values from Databanks and Estimating Missing Parameters 20

1.3.6 Step 5: Verification of the Accuracy of the Selected Property Method by Comparing Predicted Pure-Component Property Values with Report Experimental Data 21

1.3.7 Step 6: Regress Component Liquid Density Data and Binary Vapor–Liquid Equilibrium (TPXY) Data to Estimate Missing Pure-component and Binary Interaction Parameters of Selected Property Method and Verify Predicted VLE Results with Experimental Data 22

1.3.8 Step 7: Develop Correlations for Polymer Product Quality Indices, Such as Density and Melt Index (Melt Flow Rate) Based on Plant Data 22

1.3.9 Step 8: Define the Polymerization Reactions and Enter the Initial Reaction Rate Constants 22

1.3.10 Step 9: Draw the Open-Loop Process Flowsheet and Enter the Inputs for Streams and Blocks 24

1.3.11 Step 10: Run the Initial Open-loop Process Simulation and Check if the Simulation Results Are Reasonable 25

1.3.12 Step 11: Close the Recycled Loops, Finalize a Converged Closed-loop Steady-state Simulation Model, and Investigate Applications to Improving Process Operations and Identifying Operating Conditions for New Product Design 26

1.3.13 Step 12: Convert the Steady-state Simulation Model in Aspen Plus to a Dynamic Simulation Model in Aspen Plus Dynamics; Add Appropriate Controllers; and Investigate Process Operability, Control, and Grade Changes 26

1.4 Industrial and Potential Applications of Integrated Process Modeling, Advanced Control, and Data Analytics to Optimizing Polyolefin Manufacturing 26

1.4.1 Industrial and Potential Applications of Process Modeling to Optimizing Polyolefin Manufacturing 26

1.4.2 Industrial and Potential Applications of Advanced Process Control to Optimizing Polyolefin Manufacturing 28

1.4.3 Industrial and Potential Applications of Data Analytics to Optimizing Polyolefin Manufacturing 31

1.4.4 Hybrid Modeling: Integrated Applications of Process Modeling, Advanced Control, and Data Analytics to Optimizing Polyolefin Manufacturing 34

References 36

2 Selection of Property Methods and Estimation of Physical Properties for Polymer Process Modeling 41

2.1 Property Methods and Thermophysical Parameter Requirements for Process Simulation 41

---

<!-- PDF page 11 -->

2.2 Polymer Activity Coefficient Models (ACM): Polymer Nonrandom Two-liquid (POLYNRTL) Model 42  
2.2.1 Vapor–Liquid Equilibrium for an Ideal Vapor Phase and a Nonideal Liquid Phase 42  
2.2.2 General Vapor–Liquid Equilibrium Relationships Based on Fugacity Coefficient and Liquid-phase Activity Coefficient 43  
2.2.3 Segment-based Mole Fraction Versus Species-based Mole Fraction 43  
2.2.4 POLYNRTL: Polymer Nonrandom Two-liquid Activity Coefficient Model 44  
2.2.5 Concept of Henry Components for Vapor–Liquid Equilibrium for a Vapor Phase and a Nonideal Liquid Phase Involving Supercritical Components 46  
2.3 Workshop 2.1. Estimating POLYNRTL Binary Parameters Using UNIFAC 50  
2.3.1 Objective 50  
2.3.2 Estimating POLYNRTL Binary Parameters Using UNIFAC for Polystyrene Manufacturing 51  
2.4 Prediction of Polymer Physical Properties by Van Krevelen Functional Group Method 53  
2.5 Workshop 2.2. Estimating the Physical Properties of a Copolymer Using the Van Krevelen Group Contribution Method 55  
2.5.1 Objective 55  
2.5.2 Draw the Process Flowsheet and Specify the Unit Set and Global Options 55  
2.5.3 Define Components, Segments, and Polymer and Characterize Their Structures 55  
2.5.4 Choosing Property Method and Entering or Estimating Property Parameters 56  
2.5.5 Specifications of Feed Stream and Flash Block 57  
2.5.6 Creating Property Sets 58  
2.5.7 Defining Property Analysis Run to Create Property Tables 58  
2.6 Polymer Sanchez–Lacombe Equation of State (POLYSL) 61  
2.7 Workshop 2.3. Estimating Property Parameters Using Data Regression Tool 64  
2.7.1 Objective 64  
2.7.2 Defining a DRS Run 64  
2.7.3 Specifying a Unit Set and Global Options 64  
2.7.4 Defining Components, Segments, Oligomers, and Polymer 65  
2.7.5 Choose Property Method and Enter Known Property Parameters from Aspen Enterprise Databanks 66  
2.7.6 Enter Experimental Data for Data Regression, Run the Regression, and Examine the Results 67  
2.7.7 Specifying a Regression Run and the Parameters to be Regressed 69  
2.7.8 Running the Regression Case and Examining the Results 69

---

<!-- PDF page 12 -->

Contents  
  
2.8 Polymer Perturbed-chain Statistical Fluid Theory (POLYPCSF) Equation of State 72  
  
2.9 Workshop 2.4. Regression of Property Parameters for POLYPCSF EOS 74  
  
2.9.1 Objective and Data Sources 74  
  
2.9.2 Regression of Pure Component Parameters for POLYPCSF EOS 75  
  
2.10 Correlation of Polymer Product Quality Indices and Structure–Property Correlations 77  
  
2.10.1 Polyolefin Product Quality Indices 77  
  
2.10.2 Empirical Correlations of Polymer Product Quality Targets 80  
  
2.10.3 Estimation of Apparent Newtonian Viscosity from MI-MWW Measurement 81  
  
References 83  
  
3 Reactor Modeling, Convergence Tips, and Data-Fit Tool 87  
  
3.1 Kinetic or Rate-Based Reactors 87  
  
3.2 Continuous Stirred-Tank Reactor Model (RCSTR) 87  
  
3.2.1 RCSTR Configurations 87  
  
3.2.2 RCSTR Specifications 88  
  
3.3 Plug-Flow Reactor Model (RPLUG) 89  
  
3.3.1 RPLUG Configurations 89  
  
3.3.2 RPLUG Specifications 90  
  
3.4 Batch Reactor Model (RBATCH) 91  
  
3.4.1 RBATCH Configuration 91  
  
3.4.2 RBATCH Specifications 92  
  
3.5 Representation of Nonideal Reactors 93  
  
3.6 RCSTR Convergence 93  
  
3.6.1 Initialization 93  
  
3.6.2 Scaling Factors 95  
  
3.6.3 Residence Time Loop 95  
  
3.6.4 Energy Balance Loop 96  
  
3.6.5 Mass Balance Loop 97  
  
3.6.6 Flash Loop 98  
  
3.6.7 Recommendation for RCSTR Mass Balance Algorithm for Polyolefin Process Simulation 99  
  
3.7 RPLUG/RBATCH Model Convergence 100  
  
3.8 Data Fit (Simulation Data Regression) 101  
  
3.9 Workshop 3.1: Data Fit of Kinetic Parameters for Styrene Polymerization Using Concentration Profile Data 103  
  
3.9.1 Objective 103  
  
3.9.2 A Simplified Kinetic Model for Styrene Polymerization 103  
  
3.9.3 Datasets 106  
  
3.9.4 Simulation Data Regression (Data Fit) 107  
  
3.10 Workshop 3.2: Data Fit of Kinetic Parameters for Styrene Polymerization Using Point Data 111

---

<!-- PDF page 13 -->

3.10.2 Dataset 111  
3.10.3 Simulation Data Regression (Data Fit) 112  
References 114  
  
4 Free Radical Polymerizations: LDPE and EVA 115  
4.1 Polymers by Free Radical Polymerization 115  
4.2 Kinetics of Free Radical Polymerization 115  
4.2.1 Initiator and Its Decomposition-Rate Parameters 116  
4.2.2 Chain Initiation Reactions 118  
4.2.3 Chain Propagation Reactions 119  
4.2.4 Chain Transfer Reactions 120  
4.2.5 Termination Reactions 121  
4.2.6 Autoacceleration, Trommsdorff Effect, or Gel Effect 122  
4.2.7 Other Free Radical Polymerization Reactions 123  
4.3 Thermodynamic Methods and Property Parameter Requirements 123  
4.4 Workshop 4.1: Simulation of an Autoclave High-pressure LDPE Process 124  
4.4.1 Objectives 124  
4.4.2 Process Flowsheet and Simulation Representation 124  
4.4.3 Unit System, Components, and Characterization of Polymer 126  
4.4.4 Thermodynamic Methods and Property Parameters for Components, Segment, and Polymer 129  
4.4.5 PCES (Physical Constant Estimation System) for Estimating Missing-Property Parameters 130  
4.4.6 Defining Free Radical Polymerization Reactions for LDPE 130  
4.4.7 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks 133  
4.4.8 Methodology for Improving Simulation Convergence and for Kinetic Parameter Estimation 133  
4.4.9 Base-Case Simulation Results 136  
4.4.10 Model Applications 138  
4.4.11 Separation Section 139  
4.5 Workshop 4.2: Simulation of Tubular Reactors for HP LDPE Process 140  
4.5.1 Objectives 140  
4.5.2 Process Flowsheet and Simulation Representation 141  
4.5.3 Unit System, Components, and Characterization of Polymer 141  
4.5.4 Thermodynamic Method and Property Parameters for Components 142  
4.5.5 PCES (Physical Constant Estimation System) for Estimating Missing-Property Parameters 144  
4.5.6 Free Radical Polymerization Reactions for LDPE 144  
4.5.7 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks 144

---

<!-- PDF page 14 -->

4.5.8 User FORTRAN Subroutine for Heat Transfer Calculations for the LDP Reactor 145  
  
4.5.9 Base-Case Simulation Targets and Kinetic Parameter Estimation 147  
  
4.5.10 Model Applications 149  
  
4.6 Workshop 4.3: Simulation of Tubular Reactors for Ethylene-Vinyl Acetate (EVA) Copolymerization Process 151  
  
4.6.1 Objective 151  
  
4.6.2 Process Background 151  
  
4.6.3 Unit System, Components, and Characterization of Polymer 153  
  
4.6.4 Thermodynamic Method and Property Parameters for Components and Polymer 155  
  
4.6.5 Free Radical Polymerization Kinetics for EVA Copolymerization 156  
  
4.6.6 Specifications of Inlet Process Streams and Unit Operation and Reactor Blocks 156  
  
4.6.7 Base-Case Simulation Targets and Kinetic Parameter Estimation 158  
  
References 160  
  
5 Ziegler–Natta Polymerization: HDPE, PP, LLDPE, and EPDM 163  
  
5.1 Ziegler–Natta (ZN) Polymerization 164  
  
5.1.1 Introduction 164  
  
5.1.2 Ziegler–Natta Catalysts 164  
  
5.2 Ziegler–Natta Polymerization Kinetics 165  
  
5.2.1 Catalyst Activation (ACT) 165  
  
5.2.2 Chain Initiation (CHAIN-INI) 166  
  
5.2.3 Chain Propagation (PROP) 166  
  
5.2.4 Chain-Transfer Reaction (CHAT) 167  
  
5.2.5 Catalyst Deactivation (DEACT) 167  
  
5.2.6 Catalyst Inhibition (INH) 167  
  
5.2.7 Copolymerization Kinetics 168  
  
5.3 Modeling Considerations 170  
  
5.3.1 Reactor Types 170  
  
5.3.2 Process Flowsheets 171  
  
5.3.3 Polymer Types 172  
  
5.3.4 Molecular Weight Distribution (MWD) and Multi-Modal Distributions 173  
  
5.3.5 Thermodynamics 174  
  
5.3.6 Global Kinetics Versus Local Kinetics 174  
  
5.4 Commercial Polyolefin Production Targets 175  
  
5.4.1 General Production Targets 175  
  
5.4.1.1 Production Rate 175  
  
5.4.1.2 MWN 175  
  
5.4.1.3 MI 176  
  
5.4.1.4 Conversion 176  
  
5.4.1.5 PDI 176

---

<!-- PDF page 15 -->

5.4.1.6 SMWN and SPFRAC 176  
5.4.1.7 SFRAC and SCB 176  
5.4.1.8 Rho 176  
5.4.1.9 Residence Time 177  
5.4.2 Polymer-Specific Targets 177  
5.4.2.1 CISFRAC 177  
5.4.2.2 ATFRAC 177  
5.5 Methodology for Polyolefin Kinetic Estimation 178  
5.5.1 Efficient Use of Software Tool: Data Fit 179  
5.5.2 Flowchart of the Methodology for Kinetic Parameter Estimation 179  
5.5.2.1 Multiple Product Grades and Single Active Catalyst Site 180  
5.5.2.2 Multisite Model and Deconvolution Analysis 183  
5.5.2.3 GPC Data and Deconvolution Analysis to Estimate the Number of Active Catalyst Sites 185  
5.5.3 Efficient Use of Software Tools: Sensitivity Analysis 188  
5.5.4 Efficient Use of Software Tools: Design Specification 191  
5.5.5 Model Applications 194  
5.6 Workshop 5.1: Simulation of a Slurry HDPE Process 195  
5.6.1 Objective 195  
5.6.2 Process Flowsheet 195  
5.6.3 Unit System, Components, and Characterization of Oligomer, Polymer, and Site-Based Species 195  
5.6.4 The Role of Solid Polymer in Phase-Equilibrium Calculations 199  
5.6.5 Thermodynamic Model and Parameters 199  
5.6.6 Pure-Component Parameters 200  
5.6.7 Feed Streams 203  
5.6.8 Ziegler–Natta Kinetics Specifications 204  
5.6.9 Specifications of Unit Operations and Chemical Reactor Blocks 207  
5.6.9.1 Mixers (Figure 5.38) 207  
5.6.9.2 Reactors (Figures 5.39–5.42) 207  
5.6.9.3 Specification of Flash Drums (Figure 5.42) 208  
5.6.10 Simulation Results 209  
5.6.11 Sensitivity Analysis 209  
5.6.12 Closing the Recycle Loops 210  
5.7 Workshop 5.2: Simulation of Stirred-Bed Gas-Phase PP Process 214  
5.7.1 Objective 214  
5.7.2 Process Description 214  
5.7.3 Modeling the Stirred-Bed Reactor 215  
5.7.4 Process Flowsheet 218  
5.7.5 Unit System, Components, and Characterization of Polymer and Site-Based Species 218  
5.7.6 Thermodynamic Model and Parameters 220  
5.7.7 Feed Streams 222  
5.7.8 Ziegler–Natta Kinetics Specifications 223  
5.7.9 Specifications of Unit Operation and Chemical Reactor Blocks 225

---

<!-- PDF page 16 -->

5.7.9.1 Mixers MIX1 to MIX8 (Figure 5.62) 225  
5.7.9.2 Reactors R1 to R8 (Figures 5.63 and 5.64) 225  
5.7.9.3 Other Blocks 225  
5.7.9.4 Convergence Blocks 226  
5.7.10 Open-Loop Simulation Results and Closing the Loop 227  
5.7.11 Model Applications 229  
5.8 Workshop 5.3: Simulation of a Gas-Phase Fluid-Bed LLDPE Process with Condensed Mode Cooling 229  
5.8.1 Objective 229  
5.8.2 Condensed Mode Cooling in Ethylene Polymerization in a Fluidized-Bed Reactor 230  
5.8.3 Process Flowsheet 234  
5.8.4 Unit System, Components, and Characterization of Oligomer, Polymer, and Site-Based Species 234  
5.8.5 Deconvolution Analysis of GPC Data to Determine the Number of Active Catalyst Sites 235  
5.8.6 Thermodynamic Model and Parameters 237  
5.8.7 Inlet Stream Specifications for Grades A and B 238  
5.8.8 Specifications of Unit Operation and Chemical Reactor Blocks 238  
5.8.9 Ziegler–Natta Kinetics Specifications 241  
5.8.10 Reactor and Flowsheet Simulation to Match Plant Production Targets 242  
5.8.11 Model Applications 242  
5.9 Workshop 5.4: Simulation of a Solution Polymerization Process for Producing Ethylene–Propylene Copolymer (EPM) or an Ethylene–Propylene–Diene Terpolymer (EPDM) with Metallocene Catalysts 247  
5.9.1 Objective 247  
5.9.2 Process Background 247  
5.9.3 EPM Copolymerization Kinetics and EPDM Terpolymerization Using a Metallocene Catalyst System 249  
5.9.4 Unit System, Components, and Characterization of Polymer 250  
5.9.5 Thermodynamic Method and Property Parameters for Components and Polymer 254  
5.9.6 Process Flowsheet and Inlet Stream and Block Specifications 255  
5.9.7 Base-Case Simulation Results 256  
5.9.8 Extension to EPDM (Ethylene–Propylene–Diene Terpolymer) 257  
5.10 Conclusions 260  
References 261  
6 Free Radical and Ionic Polymerizations: PS and SBS Rubber 267  
6.1 Workshop 6.1: Simulation of Polystyrene Reactors with Gel Effect and Oligomer Formation 268  
6.1.1 Objective 268

---

<!-- PDF page 17 -->

6.1.2 Process Flowsheet 269

6.1.2 Process Flowsheet 209  
6.1.3 Unit System, Components, and Characterization of Polymer 270  
6.1.4 Characterization of Oligomers 271  
6.1.5 Thermodynamic Method and Property Parameters for Components and Oligomers 276  
6.1.6 PCES (Physical Constant Estimation System) for Estimating Property Parameters for Oligomers 278  
6.1.7 Defining Free Radical Reactions and Oligomer Reactions 279  
6.1.8 Specification of Inlet Process Streams and Unit Operation and Reactor Blocks 284  
6.1.9 Kinetic Parameter Estimation and Model Validation 286  
6.1.10 Model Applications 288  
6.2 Workshop 6.2: Production of Poly(Styrene–Butadiene–Styrene) or SBS Rubber by Ionic Polymerization 292  
6.2.1 Motivation and Objective for Modeling Ionic Polymerization Processes 292  
6.2.2 Reactor Configurations and Copolymer Products 293  
6.2.2.1 Tapered Block Copolymer 293  
6.2.2.2 Di-/Tri-Block Copolymer and a Star-Shaped Block Copolymer 294  
6.2.2.3 Random Copolymer 294  
6.2.3 Components, Segments, and Polymer in Anionic Copolymerization of Styrene and Butadiene 294  
6.2.4 Thermodynamic Method and Property Parameters of Components and Polymer 294  
6.2.5 Kinetics of Anionic Copolymerization of Styrene and Butadiene 295  
6.2.5.1 Initiator Disassociation (INIT-DISSOC) 295  
6.2.5.2 Chain Initiation (CHAIN-INI) 296  
6.2.5.3 Chain Propagation (PROPAGATION) 300  
6.2.5.4 Association or Aggregation (ASSOCIATION) 300  
6.2.5.5 Chain Transfer (CHAT) 301  
6.2.5.6 Chain Termination (TERM-AGENT) 302  
6.2.5.7 Equilibrium with Counter-Ion or Reversible Ionization (EQUILIB-CION) 302  
6.2.5.8 Batch Reactor for Producing a Tapered Block Copolymer 302  
6.2.5.9 Semi-Batch Reactor for Producing a Tri-Block SBS Copolymer by an Industrial Batch-Sequence Recipe 306  
6.2.5.10 Semi-Batch Reactor for Producing a Tri-Block SBS Copolymer by a Literature Batch-Sequence Recipe 313  
References 318  
7 Improved Polymer Process Operability and Control Through Steady-State and Dynamic Simulation Models 321  
7.1 Workshop 7.1: Workflow for Dynamic Process Modeling Using Aspen

7.1 Workshop 7.1: Workflow for Dynamic Process Modeling Using Aspen Plus and Aspen Plus Dynamics 322

7.2 Running Simulation in Aspen Plus Dynamics 325

---

<!-- PDF page 18 -->

7.2.1 Types of Dynamic Simulations: Flow-Driven and Pressure-Driven 325  
7.2.2 Graphical Interface of Aspen Plus Dynamics 325  
7.2.3 Simulation Run Modes and Run Control 326  
7.2.4 Viewing Simulation Results Using Predefined Tables and Plots 328  
7.2.5 Specification Status and Analysis 329  
7.2.6 Creating New Tables and Plots 332  
7.2.7 Variable Finding in Aspen Plus Dynamics (AD) 334  
7.3 Process Control in Aspen Plus Dynamics 335  
7.3.1 Workshop 7.2: Adding a PID Controller 335  
7.3.2 Configuring a PID Controller 337  
7.4 Snapshots 344  
7.5 Workshop 7.3: Tasks for Implementing Discrete Events 344  
7.6 Workshop 7.4: Dynamic Simulation and Grade Change of a Slurry HPDE Process 350  
7.6.1 Objectives 350  
7.6.2 Stepwise Procedure to Develop Aspen Plus Dynamics (AD) Simulation Model 350  
7.6.3 Simulation of Grade-Change Operations 355  
7.7 Workshop 7.5: Dynamic Simulation and Control of a Commercial Slurry HDPE Process 359  
7.7.1 Objectives 359  
7.7.2 Converting a Steady-State Simulation Model to a Dynamic Simulation Model 359  
7.7.3 Initial Adjustments of the AD Model 361  
7.7.3.1 Polymer Attributes for Streams and Blocks 361  
7.7.3.2 Implementation of Reactor Level Control Using Mechanical Weir 361  
7.7.3.3 Improvement of the Reactor Temperature Controller 362  
7.7.3.4 Deletion of Pressure Controllers 363  
7.7.3.5 Adding a Hydrogen–Ethylene Ratio Controller to the Recycle Gas 363  
7.8 Workshop 7.6: Dynamic Simulation and Control of a Gas-Phase Fluidized-Bed Process for Producing LLDPE in Condensed Mode Operation 367  
7.8.1 Objectives 367  
7.8.2 Converting a Steady-State Simulation Model to a Dynamic Simulation Model 367  
7.9 Workshop 7.7: Dynamic Simulation and Control of a Slurry HDPE Process Using an Inferential Controller 370  
7.9.1 Objective 370  
7.9.2 Inferential Control Theory and Recent Applications 370  
7.9.3 HDPE Process Description and Steady-State Model Empirical Correlation 372  
7.9.4 Grade-Change Transition Using Basic H2-Based Controller 373  
7.9.5 Open-Loop Inferential Controller Using Dynamic Model 374  
7.9.6 Closed-Loop Inferential Controller 375  
References 378

---

<!-- PDF page 19 -->

## Volume 2

Foreword xxv  
Preface xxxi  
Acknowledgment xxxv  
Copyright Notice xxxvii  
About the Authors xxxix  
About the Companion Website xli  
8 Model-Predictive Control of Polyolefin Processes 381  
9 Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing 477  
10 Applications of Machine Learning to Optimizing Polyolefin Manufacturing 533  
11 A Hybrid Science-Guided Machine Learning Approach for Modeling Chemical and Polymer Processes 651  
Appendix A Matrix Algebra in Multivariate Data Analysis and Model Predictive Control 699  
Appendix B Introduction to Python for Chemical Engineers 737  
Aman Aggarwal  
Index 759

---

<!-- PDF page 20 -->

## Foreword

Polyolefins are among the most widely used commodity and specialty polymers, with uses in films and packaging, medical, consumer, and industrial goods, and the automotive industry. Polyolefins have wide applications requiring different properties with different molecular weight distributions and branching distributions. With the increase in the world population and a growing consumer class, the high demand for polyolefins presents a dual challenge to the chemical industry to produce more polyolefins to meet these growing needs while minimizing the environmental impact. Modeling and optimization of polyolefin processes will enable engineers to achieve this important challenge. However, the complex nature of polyolefin processes requires the understanding and application of a unique combination of relevant thermodynamics, polymerization kinetics, reactor design, product separation, and process control in a manner not typically required for more conventional chemical processes. This textbook is a comprehensive and practical guide for tackling the technical complexities that engineering practitioners will face while modeling and optimizing industrial polyolefin processes in both steady-state and dynamic operations.

Professor Y. A. Liu has, for many decades, been a tireless and enthusiastic advocate and educator in the application of computer-aided modeling and simulation to solve real industrial problems. Prof. Liu has worked with many leading companies around the world and trained thousands of engineers to apply process simulation, optimization, and advanced process control to a variety of industries, including petroleum refining, industrial water savings, carbon capture, and polymer production. This book is the latest in a series of excellent textbooks authored by Prof. Liu and his students, which provide a detailed technical and practical engineering approach to solving real-world problems.

This textbook by Prof. Liu and Dr. Sharma covers the full-scale modeling of industrial polymer processes in detail with easy-to-follow, step-by-step examples. This textbook covers advances in different areas of polymer process modeling, such as polymer thermodynamics, kinetics, reactor modeling, and process control. The book presents an industrially validated methodology for modeling and optimizing complex industrial polyolefin processes using commercially available computer-aided engineering tools.

---

<!-- PDF page 21 -->

## Foreword

Polyolefins are among the most widely used commodity and specialty polymers, with uses in films and packaging, medical, consumer, and industrial goods, and the automotive industry. Polyolefins have wide applications requiring different properties with different molecular weight distributions and branching distributions. With the increase in the world population and a growing consumer class, the high demand for polyolefins presents a dual challenge to the chemical industry to produce more polyolefins to meet these growing needs while minimizing the environmental impact. Modeling and optimization of polyolefin processes will enable engineers to achieve this important challenge. However, the complex nature of polyolefin processes requires the understanding and application of a unique combination of relevant thermodynamics, polymerization kinetics, reactor design, product separation, and process control in a manner not typically required for more conventional chemical processes. This textbook is a comprehensive and practical guide for tackling the technical complexities that engineering practitioners will face while modeling and optimizing industrial polyolefin processes in both steady-state and dynamic operations.

Professor Y. A. Liu has, for many decades, been a tireless and enthusiastic advocate and educator in the application of computer-aided modeling and simulation to solve real industrial problems. Prof. Liu has worked with many leading companies around the world and trained thousands of engineers to apply process simulation, optimization, and advanced process control to a variety of industries, including petroleum refining, industrial water savings, carbon capture, and polymer production. This book is the latest in a series of excellent textbooks authored by Prof. Liu and his students, which provide a detailed technical and practical engineering approach to solving real-world problems.

This textbook by Prof. Liu and Dr. Sharma covers the full-scale modeling of industrial polymer processes in detail with easy-to-follow, step-by-step examples. This textbook covers advances in different areas of polymer process modeling, such as polymer thermodynamics, kinetics, reactor modeling, and process control. The book presents an industrially validated methodology for modeling and optimizing complex industrial polyolefin processes using commercially available computer-aided engineering tools.

---

<!-- PDF page 22 -->

This textbook starts with the fundamentals of polymer component characterization and thermodynamic property calculations, introducing the concept of the segment-based approach and polymer attributes, followed by evaluation and selection of thermodynamic models, parameter estimation, and data regression. Specific guidelines for the selection of an appropriate polymer property method for modeling specific polyolefin processes are discussed, drawing on knowledge from industrial experience. The authors present an effective methodology for estimating kinetics from plant data, which is critical since there are multitude of kinetic parameters to estimate for a catalytic polyolefin process. They also showcase the advantages of dynamic process models for applications such as polymer-grade transition that can have significant cost implications. This textbook covers the application of advanced process control and model predictive control for optimizing industrial polymer processes, including a discussion on controller tuning to optimize control performance.

In addition, this textbook has a comprehensive section on recent advances in multivariate data analysis and machine learning applications for process modeling. The authors introduce these concepts in a manner that is easily understandable and showcase how these technologies can be applied in the process industry. Especially significant for polymer processes is the application of data analytics to infer polymer quality measurements such as polymer melt index and molecular weight. The authors also highlight the importance and methodologies for combining first-principles engineering models with machine learning (hybrid science-guided machine learning) to develop hybrid models, which provide more accurate and consistent predictions in compliance with physical constraints.

This textbook, in my opinion, should be very beneficial to senior and graduate students, university faculty, and practicing engineers and industrial scientists who wish to learn the fundamentals and practice of process modeling, advanced control, and data analytics for sustainable design, operation, and optimization of polyolefin manufacturing processes. I am not aware of any similar books that cover the broad scope with excellent quality, while providing real-world examples.

By Willie K. Chan

Chief Technology Officer

Aspen Technology, Inc.

---

<!-- PDF page 23 -->

Professor Y. A. Liu has had an extraordinary career spanning over 40 years in teaching process design, authoring textbooks for process design and simulation, and ingenious and impactful scholarship in sustainable engineering. As someone who has collaborated with Prof. Liu and benefited from his kind advice and support for more than 25 years in the area of computer-aided chemical engineering, I admire and congratulate Prof. Liu for yet another exceptional achievement in the textbook "Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing."

This textbook on process modeling, advanced control, and data analytics applied to polyolefin manufacturing represents a particularly beneficial contribution to university students and faculty, industrial practitioners, and scientists, considering the fact that polyolefins represent approximately 60% of commercial polymer production. To truly appreciate the significance of this textbook on modeling and simulation of polyolefin processes, we must recognize this textbook as one more milestone in Prof. Liu's contributions over the years in authoring a series of textbooks that cover modeling and simulation of chemical processes and help shape the curriculum in chemical process design. Among them, I wish to highlight the following four recent textbooks: (1) Step-Growth Polymerization Process Modeling and Product Design by Wiley, New York (2008), (2) Refining Engineering: Integrated Process Modeling and Optimization by Wiley-VCH, Weinheim, Germany (2012), (3) Petroleum Refinery Process Modeling: Integrated Optimization Tools and Applications by Wiley-VCH, Weinheim, Germany (2018), and (4) Design, Simulation and Optimization of Adsorptive and Chromatographic Separations: A Hands-on Approach by Wiley-VCH, Weinheim, Germany (2018). All these textbooks capture the chemical engineering fundamentals for these critically important and complex chemical manufacturing processes, the modern-day process modeling and simulation technologies implemented in commercial process simulators, and the industrial practice of professional engineers dedicated to the design, control, and optimization of these processes. All four textbooks have received outstanding reviews by academic experts, industrial practitioners, and my own students at Texas Tech University. I have no doubt this new textbook on polyolefin processes will be another resounding success.

---

<!-- PDF page 24 -->

Personally, I had been deeply involved in the invention, implementation, testing, commercialization, and application of modern-day process simulators for modeling and simulation of varieties of chemical processes, including polyolefin processes. Knowing the challenges in developing modeling and simulation technologies and the tremendous efforts required of many top-notch software developers and industrial collaborators to overcome the challenges, I am particularly appreciative of the fact that Prof. Liu and his doctoral students dedicated their time and effort to writing textbooks based on their latest research and advances by others in the field. He and his students write detailed expositions and develop hands-on workshops to educate current and future workforce on how to apply the advances in process system engineering and computer-aided design using commercial software tools. Furthermore, Prof. Liu and his student co-authors have done so beautifully and effectively in many fields as diverse as neural networks, pinch technology for industrial water reuse, petroleum refining processes, adsorptive and chromatographic separations, industrial polymer manufacturing, among others.

Chapters 1–7 of this book present the fundamentals and practice of steady-state and dynamic simulation and control of polyolefin processes with 24 hands-on workshops with step-by-step instructions applied to industrial polyolefin processes with realistic plant data. Chapter 8 introduces the key concepts and software implementation of the third generation of dynamic matric control (DMC3) and nonlinear advanced control of polyolefin processes and includes two detailed hands-on workshops on advanced control copolymerization and polypropylene processes. Chapters 9–11 demonstrate how multivariate statistics and machine learning are playing an increasingly important role in optimizing polyolefin manufacturing with 16 hands-on application workshops. The authors state that their goal for this part is to prepare an overview of multivariate statistics and machine learning for university students and faculty, practicing engineers and scientists who are new to the field, and also for those who are knowledgeable but wish to know the new developments and application literature in chemical and polymer processes. A study of these chapters clearly shows that they have done an excellent job.

This book is beneficial to beginners and not only provides detailed tutorials and guides for many different applications but also describes more technical details that are useful to advanced practitioners. This book represents a milestone in advancing polymer process modeling, advanced control, and data analytics, and I cannot wait to learn what Prof. Liu has in mind for his next textbook.

By Chau-Chyun Chen

Horn Distinguished Professor and

Jack Maddox Distinguished Chair in Engineering

Texas Tech University

An inventor of segment-based modeling technology

for polymer processes

Member, National Academy of Engineering

---

<!-- PDF page 25 -->

Professor Y. A. Liu is well known in the chemical engineering community for his passion, mission, and dedication in teaching fundamentals and practice of process modeling in polymer manufacturing for many decades. The textbook Step-Growth Polymerization Process Modeling and Product Design that he co-authored with Kevin C. Seavey in 2008 has been an asset to students and industrial practitioners in understanding how to apply process modeling and product design concepts in industrial polymer processes.

Since 2008, availability of big data, advances of machine learning algorithms, and affordability of computing resources have propelled the digital transformation in the chemical and materials industry. Y. A. Liu is an award-winning researcher to incorporate AI, machine learning, and data analytics to enhance modeling, control, and optimization of polymer processes; he is also an inspiring teacher to pass along his knowledge. This textbook lays out the foundation of process modeling in Chapters 1–7, introduces important role of advanced process control in Chapter 8, and showcases the evolution of how data analytics are positively impacting polymer process in Chapters 9–11. Chapter 9 explains why multivariate statistics (principal component analysis and partial least squares) remain the "gold standard" for analyzing manufacturing data from polymer processes. Chapter 10 highlights recent advances in machine-learning algorithms (from supervised learning to reinforcement learning; from logistic regression to transformer deep neural network); and Chapter 11 outlines promising research direction on hybrid science-guided machine learning (also known as hybrid modeling or physics-informed machine learning).

The contents of Chapters 9–11 resonate with my two-decade long industrial research and implementation experience of AI, machine learning, and data analytics. In fact, in a recent AIChE Journal article, Toward AI at scale in the chemical industry that I co-authored, we positioned AI as a portfolio of enabling technologies that need to be applied in context to address a specific business need. Successful industrial AI applications have a common attribute that the right AI methods are selected based on domain process knowledge and data characteristics. Y. A. read my paper around the same time that I read his AIChE Journal article, A Science-Guided Machine Learning Approach to Modeling Chemical Processes: A Review. I am glad that we shared a common vision, and this textbook is a testimony on how AI has been successfully applied in the context of polymer manufacturing.

---

<!-- PDF page 26 -->

I am grateful that Y. A. Liu and Niket Sharma have written this textbook with plenty of hands-on examples and workshops with industrial relevance. This book explains the Why, What, and How of process modeling, advanced control, AI, and data analytics for industrial polymer processes, and it will impact the chemical engineering community for decades to come.

By Leo H. Chiang

Senior R&D Fellow, AI and Data Analytics

The Dow Chemical Company

Member, National Academy of Engineering

---

<!-- PDF page 27 -->

Polyolefin manufacturing is a huge industry that comprises the majority of global polymer production. The 2021 world market size was US$ 278 billion, and the 2030 projected market size varies from US$ 438 to 604 billion, depending on compounded annual growth rate (CAGR) estimates. Small improvements in the design and operation of a polyolefin plant can produce significant economic payback.

For most of my career, I have worked on the development of computer models of chemical processes. Beginning with my work with the Advanced System for Process Engineering (ASPEN) Project at MIT, my team later formed Aspen Technology, Inc., to develop the chemical industry's first computer-based modeling and simulation technology. Over the past four decades, I have fond memories of many transformative solutions developed by my colleagues at AspenTech that have helped a variety of industries run their businesses in a safe, profitable, and sustainable manner. In particular, in 1997, two of my former doctoral students at MIT and later R&D staff at AspenTech, Chau-Chyun Chen and Michael Barrera (Michael happened to be a senior in design courses and undergraduate research under Prof. Y. A. Liu at Virginia Tech), and others developed a groundbreaking patent for the segment-based modeling methodology and the associated software tool, Polymers Plus (now called Aspen Polymers), for polymerization processes. This methodology has become the foundation of polymerization process modeling and product design over the past 25+ years.

In early 1999, Prof. Liu at Virginia Tech and his graduate students, working closely with AspenTech's polymer process modeling team, started a multiyear industrial outreach effort to promote sustainable design, operation, and optimization of commercial polymer production processes at companies such as Honeywell Specialty Materials and China Petroleum and Chemical Corporation (SINOPEC). In addition to generating significant cost savings and payback, this effort has resulted in a number of joint AspenTech–Virginia Tech publications in the journal Industrial and Engineering Chemistry Research from 2002 to 2007. Two of those papers (cited as papers 3 and 9 in Chapter 1) have presented the foundational development of the methodology for sustainable design and optimization of polyolefin processes and have become the standard references for subsequent papers on polyolefin process

---

<!-- PDF page 28 -->

modeling, such as polypropylene and high-density polyethylene, reported in the literature. Their work with step-growth polymers resulted in a textbook, “Step-Growth Polymerization Process Modeling and Product Design” (Wiley, 2008).

In 1997, Y. A. worked with SINOPEC to establish a training center in Beijing co-sponsored by AspenTech. In the following 20-plus years, Y. A. (during his summer and winter university breaks) and the instructors he trained have taught thousands of practicing engineers to use fundamental process modeling and advanced process control to promote sustainable engineering with the latest software tools. They have also led engineering teams to develop steady-state and dynamic simulation models of petrochemical processes, including essentially all of the polyolefin production units within SINOPEC. I have visited the training center several times, and the senior executives of SINOPEC have told me that the training has been invaluable to the Chinese petrochemical industries.

The COVID pandemic has prevented Y. A. from dedicating his university breaks to training practicing engineers in China over the past three years. I applaud the wise decision of Y. A. and his graduate student, Niket Sharma, to devote the last three years to studying the literature, running workshop examples, and writing the manuscript for the current textbook. They are doing a great professional service by sharing with the new generation of students, engineers, and scientists the many years of knowledge and insights of the Virginia Tech team in performing creative research and industrial training in polyolefin process modeling and advanced control (see Chapters 1–8). I also praise their effort in adding a significant section on recent developments in multivariate statistics and machine learning, together with their applications to chemical and polymer processes, particularly polyolefin manufacturing. They have achieved their goal very well, having prepared an overview of multivariate statistics and machine learning for university students and faculty, practicing engineers and scientists who are new to the field, and also for those who are knowledgeable but wish to know the new developments and application literature in chemical and polymer processes (see Chapters 9–11).

A unique strength of this book is that it includes 42 hands-on workshops of industrial applications, teaching the readers how to apply easy-to-use commercial software tools and Python machine learning codes to develop quantitative models for sustainable design, control, and optimization of polyolefin processes based on mostly actual plant data. These workshops discuss the very practical problems of how to work with real data, how to develop the right level of detail for the problem you are solving and the data you have, and how to tune the model to plant data. The book contains numerous literature references up to 2022. Individuals who wish to contribute to the development of sustainable design and operation of polyolefin processes or explore new directions will find the review of existing work valuable.

Overall, this book by Y. A. and Niket represents a major advance by enabling students and engineers who are not experts to develop and use state-of-the-art computer models for simulating and optimizing polyolefin processes to make them safer, more sustainable, and more profitable. Both step-growth polymers (e.g. Nylon and PET) and polyolefins (PE, LDPE, HDPE, PP, etc.) represent about 70% of the commercial polymer production. The contributions by Y. A. and his students, through their two

---

<!-- PDF page 29 -->

textbooks on step-growth polymers and polyolefins, to sustainable design education and practice in polymer manufacturing are truly unique and significant.

By Lawrence B. Evans

Professor Emeritus of Chemical Engineering

Massachusetts of Institute of Technology

Founder, Aspen Technology, Inc.

Member, National Academy of Engineering

Past President, American Institute of

Chemical Engineers

---

<!-- PDF page 30 -->

I am happy to write this foreword of a timely and significant textbook, Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing, written by Prof. Y. A. Liu and his graduate student, Niket Sharma.

Concerning my expertise and background in writing this Foreword, I was active for 34 years, from 1985 to 2017, in teaching, research, and industrial outreach as a faculty member at the Technical University of Denmark. In 2018, I started my own consulting work related to process system engineering, and I continue to serve as an adjunct faculty at several universities in the United States and Asia. I was fortunate to serve as Editor-in-Chief of Computers and Chemical Engineering (2009–2015) and President of European Federation of Chemical Engineering (2015–2018), both of which have given me a global perspective of scholarly achievements, research trends, and industrial opportunities in our profession. Among my research interests over the years have been the development and application of computer-aided methods and tools for modeling, including thermodynamic modeling and property estimation, steady-state and dynamic process simulation, and machine learning and big data analytics. With this background, I find the focus of the current textbook particularly timely and significant, covering the latest advances in fundamental research and industrial applications of integrated process modeling, advanced control, multivariate statistics, and machine learning for optimizing polyolefin manufacturing.

In 2010, following my seminar visit to Virginia Tech, my team at the Technical University of Denmark collaborated with Y. A.'s team at Virginia Tech, and in 2011, we published an article on the selection of prediction methods for thermodynamic properties for process modeling and product design of biodiesel. Through this collaboration, I became well aware of Y. A.'s continuing effort to devote his university breaks since 1997 to training practicing engineers and scientists in the United States and Asia to promote sustainable design and practice. Y. A. and the instructors he trained have led project teams to develop the steady-state and dynamic simulation models of essentially all of the polyolefin production units within SINOPEC. These models, validated with plant data, enable the engineers to quantitatively investigate the impact of new operating conditions on product yield, energy consumption, waste generation, and polymer quality (e.g. melt index and molecular weight) and identify the desired operating conditions to produce new polymer grades while minimizing the generation of off-specification wastes. In this text, Y. A. and his Virginia Tech

---

<!-- PDF page 31 -->

team are sharing their years of knowledge and experiences gained from their creative research and industrial training in process modeling and advanced control of polyolefins.

A review of process modeling in Chapters 1–7 will find, among other topics: a detailed introduction of the segment-based methodology for modeling polymer processes; the workflows to develop both steady-state and dynamic simulation models; instruction of advanced equations of state and activity coefficient models applicable to polyolefin processes, and how to choose an appropriate thermodynamic model and estimate the relevant parameters from routine measurements; detailed reviews of the polymerization kinetics literature and recommendation of the appropriate kinetic models for different polyolefin productions, together with the methodology for kinetic parameter estimation from plant data using efficient software tools; guidelines to accelerate the convergence of the simulation of large commercial polyolefin processes with product separations and recycle loops; how to convert a steady-state simulation model to a dynamic simulation model and incorporate appropriate PID controllers to improve process operability and safety; and hands-on application workshops incorporating actual plant data to teach the reader how to design and optimize polyolefin processes with improved safety, profit, and sustainability.

To my knowledge, Chapter 8 is the most detailed introduction currently available to the basic concepts and software implementation of third-generation dynamic matrix control (DMC3) and nonlinear model-predictive control applied to polymer processes. The authors explain the three key steps of linear and nonlinear model identification, steady-state economic optimization, and dynamic controller simulation with step-by-step illustrations of software implementation for a copolymerization reactor and a polypropylene reactor. In particular, this chapter gives clear and explicit explanations of all the key parameters in model identification, economic optimization, and dynamic control so that a beginner in advanced process control can develop and fine-tune model-predictive controllers.

Concerning Chapters 9–11, I enthusiastically endorse the authors' view that any new textbook on process modeling and advanced control cannot ignore two important trends: (1) the tremendous advances in artificial intelligence (AI), particularly machine learning (ML), and big data analytics over the past 20 years; and (2) the growing importance of integrating science-guided fundamental models with data-based machine learning in a hybrid science-guided machine learning (SGML) approach to modeling chemical and polymer processes. In fact, in 2021, my colleagues and I published a paper on hybrid data-driven and mechanistic modeling approaches for multiscale material and process design, and I fully appreciate the importance of a SGML approach to modeling chemical and polymer processes, as presented in Chapter 11. In these chapters, Y. A. and Niket have done a fine job of preparing an overview of fundamentals and practice of multivariate statistics and machine learning with hands-on application workshops for optimizing polyolefin manufacturing. These chapters will be beneficial to students, faculty, engineers, and scientists who are new to the field, and also for those who are knowledgeable.

---

<!-- PDF page 32 -->

but wish to know the new developments and application literature in chemical and polymer processes.

I believe that this book belongs in a class by itself in providing a thorough coverage of the fundamentals of integrated process modeling, advanced control, and data analytics and illustrating their applications in 42 hands-on workshops with realistic plant data from polyolefin industries. Above all, it is a pleasure to read, and I congratulate Y. A. and Niket for completing this fine text.

By Rafiqul Gani

Professor of Chemical Engineering

Technical University of Denmark (1985–2017)

Co-founder and President, PSE for SPEED Company

Thailand–Denmark (since 2018)

Former Editor-in-Chief Computers and Chemical Engineering Journal

Past President, European Federation of Chemical Engineering

Recipient, AIChE Computing in Chemical Engineering

Award (2015) and Sustainable Engineering

Research Award (2020), and the IChemE Sargent Medal (2021)

---

<!-- PDF page 33 -->

It is a pleasure to write a foreword for this important new text, Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing, by Y. A. Liu and Niket Sharma. This book goes well beyond isolated fundamentals available mostly piecemeal in the literature and presents essentially all the relevant fundamental and empirical modeling techniques needed to quantify the steady-state and dynamic behavior of complex industrial manufacturing processes as well as the properties of the polymer products that they produce.

More than two decades ago, I embarked on a journey of discovering and learning about the fascinating world of polymer chemistry and engineering at Virginia Polytechnic Institute and State University. In 1999, I had the privilege of joining Y. A.'s research group as a doctoral student in chemical engineering, studying advanced polymerization process modeling. In collaboration with Aspen Technology as well as manufacturers such as Honeywell, SINOPEC, Formosa Plastics, and PetroChina, we consolidated and advanced fundamental process modeling technology and applied it to develop detailed steady-state and dynamic engineering models for entire polymerization production trains. We successfully used these models to identify process improvements that created new value and trained many professional engineers to develop and use their own process models based on fundamentals. Y. A.'s work in step-growth polymerization process modeling culminated in a joint text titled Step-Growth Polymerization Process Modeling and Product Design (Wiley, 2008).

In 2007, I joined the Dow Chemical Company, a world leader in polyethylene production. I enjoyed opportunities to work as a specialist in the modeling and simulation group within the corporate engineering organization, as an operations engineer in a polyolefins plant that produced both high-volume commodity polyethylene as well as specialty polyolefins, and as a global advanced control engineer for the solution polyethylene process technology. I currently serve as Global Process Automation Director within the Packaging and Specialty Plastics Technology Center. My experiences and current responsibilities have put me as well as my colleagues in a unique position to benefit greatly from Y. A.'s many decades of work.

The new text by Y. A. and Niket begins with the needed science and engineering fundamentals to create flowsheet models for polyolefin manufacturing processes. They extensively cover the physical property framework for modeling single component as well as mixture properties. Their description of the

---

<!-- PDF page 34 -->

segment-based methodology for tracking polymers allows engineers to follow later developments such as those for polymer-specific activity coefficient models and equations of state as well as models for polymerization mechanisms and kinetics. They also cover techniques for building models for polymer product properties. As in the text on step-growth polymerization, Y. A. and Niket illustrate how to apply these fundamentals in Aspen Plus, showing the user how to select the correct physical property models, how to regress physical property parameters, and how to build reaction mechanisms and characterize kinetics. When combined with traditional unit operation models, such as those for continuous stirred-tank reactors, plug-flow reactors, and phase equilibrium separators, it becomes possible for the user to build their own train models. The next several chapters show how to apply these fundamentals to model production processes, using concrete instructions, for low-density polyethylene, ethylene-vinyl acetate, high-density polyethylene, polypropylene, linear low-density polyethylene, and ethylene propylene diene monomer, polystyrene, styrene butadiene styrene rubber, and more (Chapters 1–6).

After teaching readers about the fundamentals of polymerization process modeling and applying them to both steady-state and dynamic models, Y. A. and Niket proceed to demonstrate how to use the models to improve both steady-state operating conditions as well as optimize grade transitions (Chapter 7). They then turn their attention to advanced process control, demonstrating how to use both dynamic matrix control as well as nonlinear control. Both topics are thoroughly explored using examples from a solution copolymerization reactor as well as a polypropylene reactor (Chapter 8).

Perhaps the most significant section of Y. A. and Niket's text relevant to digital manufacturing initiatives is that on applying multivariate statistics and machine learning to create value in polymer manufacturing processes in Chapters 9–11. The authors introduce the reader to many multivariate statistics and machine learning technologies, including simple regressions, dimensionality reduction and clustering methods, ensemble methods, and deep neural networks. They also include illustrative examples for developing models and guide the user on how to choose the most appropriate technology. Last, there is a chapter on hybrid modeling, where Y. A. and Niket blend first principles based and machine learning models to realize the benefits of both fundamental and empirical models. This technique is promising for developing high-performance models of manufacturing processes that are at the same time complex and suffer from a lack of data to fully characterize the underlying physics and chemistry.

I highly recommend this text for both applied research and development specialists as well as manufacturing engineers who work in either engineering or automation. I also enthusiastically recommend this text for senior and graduate students and university faculty who wish to learn the fundamentals and practice of polymer process modeling, control, and machine learning applied to polyolefins. It teaches the fundamentals and shows how to apply them using clear, step-by-step instructions applied to realistic case studies. I have no doubt that significant value can be realized, especially for industrial practitioners, by understanding and applying the

---

<!-- PDF page 35 -->

techniques outlined herein. I wholeheartedly wish to thank Y. A. and Niket for making this excellent effort to aggregate and document not only the key contributions to the field of computer-aided design, simulation, and control of polyolefin manufacturing processes but also their own work in the last decade to advance both theory and practice.

By Kevin C. Seavey

Global Process Automation Director

Packaging and Specialty Plastics Technology Center

The DOW Chemical Company

---

<!-- PDF page 36 -->

## Preface

Addition and step-growth polymerizations are two major routes for producing commercial polymers. The majority of commercial polymers are addition polymers, of which the most important are polyolefins. Examples of polyolefins are low-density polyethylene (LDPE), high-density polyethylene (HDPE), polypropylene (PP), and their copolymers, such as ethylene-vinyl acetate (EVA), ethylene-propylene copolymer (EPM), and ethylene-propylene-diene terpolymer (EPDM). Additionally, we include polystyrene (PS) and its copolymers, such as poly(styrene-butadiene-styrene) or SBS rubber, as polyolefins (see the introduction to Chapter 6). Together, polyolefins represent approximately 50% of commercial polymer production. Step-growth polymers, such as nylon-6, nylon-66, poly(ethylene terephthalate) (PET), polyurethane, and polylactide, represent approximately 20% of commercial polymer production. This book focuses on polyolefins.

Industrial polymer producers have been modeling polymerization processes for decades. Steady-state and dynamic process models, validated by experimental and plant data, can be helpful to quantitatively: (1) investigate the effects of changing feed, catalyst, reaction, and separation conditions on polymer yields and properties; (2) achieve sustainability by minimizing energy consumption and waste by predicting optimal operating conditions for existing plants; (3) identify the operating conditions to produce new sustainable product grades of desired properties (e.g. polymer density and melt-flow rate or melt index); and (4) study different control schemes and choose one that is optimal for safety and operations.

In our 2008 Wiley textbook, Kevin C. Seavey and Y. A. Liu, Step-Growth Polymerization Process Modeling and Product Design, we have demonstrated that the successful modeling of industrial polymer production processes requires an integrated, quantitative consideration of physical property and thermodynamic modeling, polymerization reaction kinetics, transport phenomena, computer-aided design, and process dynamics and control. Our previous text also provided examples and step-by-step tutorials for user-friendly, hands-on software tools for implementing this integrated quantitative approach, such as Aspen Polymers, Aspen Plus Dynamics, and Aspen Custom Modeler. These tools can be very useful to faculty and students in academia and practicing engineers and scientists in industry.

---

<!-- PDF page 37 -->

## Preface

Addition and step-growth polymerizations are two major routes for producing commercial polymers. The majority of commercial polymers are addition polymers, of which the most important are polyolefins. Examples of polyolefins are low-density polyethylene (LDPE), high-density polyethylene (HDPE), polypropylene (PP), and their copolymers, such as ethylene-vinyl acetate (EVA), ethylene-propylene copolymer (EPM), and ethylene-propylene-diene terpolymer (EPDM). Additionally, we include polystyrene (PS) and its copolymers, such as poly(styrene-butadiene-styrene) or SBS rubber, as polyolefins (see the introduction to Chapter 6). Together, polyolefins represent approximately 50% of commercial polymer production. Step-growth polymers, such as nylon-6, nylon-66, poly(ethylene terephthalate) (PET), polyurethane, and polylactide, represent approximately 20% of commercial polymer production. This book focuses on polyolefins.

Industrial polymer producers have been modeling polymerization processes for decades. Steady-state and dynamic process models, validated by experimental and plant data, can be helpful to quantitatively: (1) investigate the effects of changing feed, catalyst, reaction, and separation conditions on polymer yields and properties; (2) achieve sustainability by minimizing energy consumption and waste by predicting optimal operating conditions for existing plants; (3) identify the operating conditions to produce new sustainable product grades of desired properties (e.g. polymer density and melt-flow rate or melt index); and (4) study different control schemes and choose one that is optimal for safety and operations.

In our 2008 Wiley textbook, Kevin C. Seavey and Y. A. Liu, Step-Growth Polymerization Process Modeling and Product Design, we have demonstrated that the successful modeling of industrial polymer production processes requires an integrated, quantitative consideration of physical property and thermodynamic modeling, polymerization reaction kinetics, transport phenomena, computer-aided design, and process dynamics and control. Our previous text also provided examples and step-by-step tutorials for user-friendly, hands-on software tools for implementing this integrated quantitative approach, such as Aspen Polymers, Aspen Plus Dynamics, and Aspen Custom Modeler. These tools can be very useful to faculty and students in academia and practicing engineers and scientists in industry.

---

<!-- PDF page 38 -->

Our research to develop the simulation and optimization models for sustainable polyolefin processes since 2000 has benefited greatly from studying apparently the only two available books on the topic: (1) N. A. Dobson, R. Galvan, R. L. Lawrence, and M. Tirrell, Polymerization Process Modeling, VCH (1996) and (2) J. B. P. Soares and T. F. L. McKenna, Polyolefin Reaction Engineering, Wiley-VCH (2012). The former book does a great job of describing polymerization kinetic mechanisms, but it includes only 13 pages of heterogeneous coordination (Ziegler-Natta) polymerization for polyolefins; the latter book includes excellent descriptions of polyolefin reaction engineering, but it has only 13 pages of developing models of industrial reactors. It was encouraging, however, to learn on page 323 of Soares and McKenna about their positive view of our two papers applying our integrated, quantitative approach to polyolefin process modeling that: “The two articles by Khare et al. (2002, 2004) (cited as Refs. [3, 9] in Chapter 1) provide an interesting overview of a simplified approach that can be used to model an entire process for an HDPE slurry process, and a gas-phase PP process using a commercial simulation package. They demonstrate the type of information required and the fact that a certain amount of process improvement can be obtained using well-defined, but manageable, reactor and unit operation models.”

Over the past 20 years, there have been hundreds of papers describing the advances in physical property modeling and prediction, polymer thermodynamics models, polyolefin reaction kinetics, kinetic parameter estimation, multiphase reactor modeling, and model-predictive control applied to polyolefin processes. Unfortunately, we cannot find a single textbook that covers these advances in polyolefin process modeling, optimization, and control and introduce those important ones for the benefit of university faculty and students, as well as industrial practitioners and scientists. This lack of a potentially valuable resource motivated us to write the current textbook.

However, any new textbook on process modeling and advanced control cannot ignore two important trends: (1) the tremendous advances in artificial intelligence (AI), particularly machine learning (ML), and in big data analytics over the past 20 years; and (2) the growing importance of integrating science-guided fundamental models with data-based machine learning in a hybrid science-guided machine learning (SGML) approach to modeling chemical and polymer processes.

In a thoughtful article published in the AIChE Journal in 2019, V. Venkatasubramanian (cited as Ref. [25] in Chapter 10) gives an excellent perspective on the evolution of AI in chemical engineering. He divides the historical development up to the present into three phases: phase I – expert system era (~1983 to ~1995); phase II – neural network era (~1990 to ~2008); and phase III – data science and deep learning era (~2005 to present). It is truly amazing that new developments in ML over the past two decades have touched every aspect of chemical industries. In a June 2022 article, also published in the AIChE Journal, Leo Chiang and his colleagues at DOW Chemical (cited as Ref. [32] in Chapter 10) give convincing evidence that the time for AI, particularly ML, in chemical industries has finally arrived. Additionally, in a May 2022 review published in the AIChE Journal (cited as Ref. [31] in Chapter 10), we presented a broad perspective on hybrid process

---

<!-- PDF page 39 -->

modeling combining the scientific knowledge and data analytics in bioprocessing and chemical engineering with a SGML approach. We have also presented examples demonstrating the increased prediction accuracy and enhanced extrapolative ability of the SGML models for polyolefin-manufacturing processes.

Therefore, this textbook also covers the applications of big data analytics, particularly multivariate statistics and machine learning, to optimizing polyolefin manufacturing in Chapters 9–11.

The contents of our eleven chapters are as follows:

1. Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing

2. Selection of Property Methods and Estimation of Physical Properties for Polymer Process Modeling

3. Reactor Modeling, Convergence Tips, and Data-Fit Tool

4. Free Radical Polymerizations: LDPE and EVA

5. Ziegler–Natta Polymerization: HDPE, PP, LLDPE, and EPDM

6. Free Radical and Ionic Polymerizations: PS and SBS Rubber

7. Improved Polymer Process Operability and Control Through Steady-State and Dynamic Simulation Models

8. Model-Predictive Control of Polyolefin Processes

9. Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing

10. Applications of Machine Learning to Optimizing Polyolefin Manufacturing

11. A Hybrid Science-Guided Machine Learning Approach for Modeling Chemical and Polymer Processes

In these chapters, we have included 42 hands-on workshops of industrial applications, teaching the readers how to apply easy-to-use commercial software tools and Python ML codes to develop quantitative models for sustainable design, operation, control, and optimization of polyolefin manufacturing processes, mostly based on real plant data. We provide all simulation files for our workshops in the Supplement Material. We also include two appendices in our book: Appendix A, matrix algebra in multivariate data analysis and model-predictive control in MATLAB and Python; and Appendix B, introduction to Python for chemical engineers.

From 1992 to the COVID-19 pandemic in 2020, the senior author has devoted his university breaks to industrial outreach at three global top 10 chemical companies (SINOPEC, Formosa Plastics, and PetroChina). He and the instructors he trained have taught thousands of engineers to apply our approach of integrating fundamental principles, industrial applications, and hands-on workshops using user-friendly, commercial software tools for the development and implementation of sustainable design, operation, and control models for polyolefin processes. According to a published SINOPEC report in the February 2014 issue of the CCIESC Journal (cited as Ref. [13] in Chapter 1), the teams trained by the senior author have completed modeling projects that resulted in an annual payback of over US$ 115.5 million for a total investment of less than US$ 10 million from 2002 to 2012. This training has included much of the polyolefin topics covered in the present text. Our trainees find our materials, particularly the hands-on workshops, easy to learn and very useful for their

---

<!-- PDF page 40 -->

industrial practice. Another motivation for writing this text is to share with the new generation of students, engineers, and scientists our years of knowledge and insights in advising and training project teams for the modeling, control, and optimization of industrial polyolefin processes.

Our review of currently available materials has failed to find any text that encompasses the broad range of process modeling, advanced control, and data analytics and emphasizes our approach of integrating fundamental principles, industrial applications, and hands-on workshops, which we focus on in this book. We hope this text will be beneficial to undergraduate and graduate students and faculty in chemistry and chemical, material, and polymer engineering, as well as practicing engineers and industrial scientists in polyolefin industries.

December 2022

Y. A. Liu and Niket Sharma

Virginia Polytechnic Institute and State University (“Virginia Tech”), Blacksburg, Virginia

---

<!-- PDF page 41 -->

## Acknowledgment

It is a pleasure to thank a number of very special persons and organizations that contributed to the preparation of this book.

We want to express our sincere gratitude to the following academic and industrial leaders who kindly took time to review our manuscripts and write the foreword for our text: Mr. Willie K. Chan, Chief Technology Officer of Aspen Technology, Inc.; Professor Chau-Chyun Chen, Hord Distinguished Professor of Texas Tech University and an inventor of the segment-based modeling technology for polymer processes; Dr. Leo H. Chiang, Senior R&D Fellow, DOW, Inc., and a top industrial leader of machine learning and big data analytics in chemical industries; Professor Lawrence B. Evans of Massachusetts Institute of Technology and founder of Aspen Technology, Inc.; Professor Rafiqul Gani of the Technical University of Denmark and Co-founder and President, PSE for SPEED, Bangkok, Thailand; and Dr. Kevin C. Seavey, Global Process Automation Director, Packaging and Specialty Plastics Technology Center, DOW, Inc.

We would like to thank the China Petroleum and Chemical Corporation (SINOPEC) and Aspen Technology, Inc., for challenging us to enter the field of polymerization process modeling by assigning us the task of developing a training program for polymerization process modeling for practicing engineers in 1998. We thank Mr. Cao Xianghong, Senior Vice President and Chief Technology Officer (retired) of SINOPEC, for his strong support over the past 30 years. We are grateful to Mr. Wilfred Wang, Board Chairman of Formosa Petrochemical Corporation, for his strong partnership during 2008–2013. We also thank Mr. He Shengbao, Chief Engineer, PetroChina Refining and Chemical Company and President of the PetroChina Petrochemical Research Institute, for his strong support in recent years.

We wish to thank Aspen Technology, Inc., for their support of the Center of Excellence in Process System Engineering in the Department of Chemical Engineering at Virginia Tech since 2002. We thank Dr. Lawrence B. Evans, Founder and former CEO; Mr. Antonio Pietri, CEO; Mr. Willie K. Chan, Chief Technology Officer; Dr. Steven Qi, Senior Vice President, Customer Success; Mr. David Reumuth, Senior Director, Customer Support and Training; and Mr. Daniel Clenzi, Director of University Programs of Aspen Technology, Inc., for their strong support.

We are grateful to Professor Chau-Chyun Chen, Texas Tech University; Mr. David Tremblay, Aspen Technology, Inc.; and Ms. Caijuan Yang and Mr. Dengzhou Song,

---

<!-- PDF page 42 -->

Petro-CyberWorks Information Technology Co., for sharing their expertise in polymer process modeling with us over the years. We thank Professor W. Harmon Ray, University of Wisconsin, for his many inspiring papers on polyolefin reaction engineering.

We would like to express our sincere appreciation to the help by the experts in process modeling, advanced process control, and machine learning and hybrid modeling at Aspen Technology, in particular: Yuhua Song, Lori Roth, Paul Turner, Alex Kalafatis, Krishnan Lakshminarayan, Ashok Rao, Ron Beck, and Gerardo Munoz.

Finally, we wish to thank Dr. Cyril Clarke, Executive Vice President and Provost at Virginia Tech, for his strong support and encouragement of the preparation of this textbook over the past three years and to our graduate students, Aman Agarwal, James Nguyen, and Adam McNeeley, for their invaluable assistance in the preparation of this book.

The junior author would like to thank his parents, Rekha Sharma and Raj Kumar Sharma, and the rest of his family, friends, and well-wishers for their continuing support throughout his graduate studies. The senior author would like to thank his wife, Hing-Har Lo Liu, for her support through the laborious process of this book writing and revision.

---

<!-- PDF page 43 -->

## Copyright Notice

References and screen images of Aspen Plus $ ^{\circledR} $, Aspen Polymers $ ^{\text{TM}} $, Aspen Plus Dynamics $ ^{\text{TM}} $, Aspen DMCplus $ ^{\text{TM}} $, Aspen DMC3 $ ^{\text{TM}} $, Aspen DMC3 Builder $ ^{\text{TM}} $, Aspen Nonlinear Controller $ ^{\text{TM}} $, Aspen Maestro $ ^{\text{TM}} $, Aspen Transition Management $ ^{\text{TM}} $, Aspen InfoPlus 21 $ ^{\text{TM}} $, aspenONE Process Explorer $ ^{\text{TM}} $, Aspen ProMV $ ^{\circledR} $, Aspen AI Model Builder $ ^{\text{TM}} $, and Aspen Multi-Case $ ^{\text{TM}} $ are reprinted with permission from Aspen Technology, Inc. The names of all products listed are trademarks of Aspen Technology, Inc. All rights reserved.

All of these software products are available from Aspen Technology, Inc., Bedford, Massachusetts (www.aspentech.com).

---

<!-- PDF page 44 -->

## About the Authors

Y. A. Liu, the Alumni Distinguished Professor and the Frank C. Vilbrandt Endowed Professor of Chemical Engineering at Virginia Tech, received his BS, MS, and PhD degrees from National Taiwan University, Tufts University, and Princeton University, respectively. His current interests in teaching, research, and industrial outreach are sustainable design, process modeling, big data analytics, and energy and water savings.

Liu has taught the capstone design courses for graduating seniors in chemical engineering since 1974, focusing on sustainable design and practice and industrial sustainable design projects. The American Society for Engineering Education honored Liu with the George Westinghouse Award for excellence in engineering education and the Fred Merryfield Design Award for excellence in teaching and research in sustainable design. The Chemical Manufacturers Association honored Liu with the National Catalyst Award for excellence in chemical education. The American Institute of Chemical Engineers (AIChE) honored Liu with the Outstanding Student Chapter Advisor Award, chosen from 380 student chapters across 54 countries, for his excellence in developing leadership and professionalism and creating enthusiasm for public service among undergraduates since 1995.

AIChE honored Liu's research and industrial outreach on sustainable design and practice with the Professional Achievement Award for Innovations in Green Process Engineering, and the Excellence in Process Development Research Award. He made special efforts to publish a substantial body of knowledge and insights about industrial applications of his research in eight groundbreaking textbooks. These books present the methodologies for: (1) industrial water savings; (2) sustainable design of polymer, refining, and adsorptive and chromatographic separation processes; and (3) intelligent design by artificial intelligence and neural computing in bioprocessing and chemical engineering. His textbooks have included 150 hands-on workshops targeted toward teaching undergraduate seniors, graduate students, and practicing engineers how to apply software tools for sustainable design and optimization.

He received the Distinguished Alumni Award and the Outstanding Career Achievement Award from Tufts University. He is a Fellow of the AIChE and a Fellow of the American Association for the Advancement of Science, cited “for excellence in design teaching, pioneering textbooks and creative scholarship in

---

<!-- PDF page 45 -->

## About the Authors

Y. A. Liu, the Alumni Distinguished Professor and the Frank C. Vilbrandt Endowed Professor of Chemical Engineering at Virginia Tech, received his BS, MS, and PhD degrees from National Taiwan University, Tufts University, and Princeton University, respectively. His current interests in teaching, research, and industrial outreach are sustainable design, process modeling, big data analytics, and energy and water savings.

Liu has taught the capstone design courses for graduating seniors in chemical engineering since 1974, focusing on sustainable design and practice and industrial sustainable design projects. The American Society for Engineering Education honored Liu with the George Westinghouse Award for excellence in engineering education and the Fred Merryfield Design Award for excellence in teaching and research in sustainable design. The Chemical Manufacturers Association honored Liu with the National Catalyst Award for excellence in chemical education. The American Institute of Chemical Engineers (AIChE) honored Liu with the Outstanding Student Chapter Advisor Award, chosen from 380 student chapters across 54 countries, for his excellence in developing leadership and professionalism and creating enthusiasm for public service among undergraduates since 1995.

AIChE honored Liu's research and industrial outreach on sustainable design and practice with the Professional Achievement Award for Innovations in Green Process Engineering, and the Excellence in Process Development Research Award. He made special efforts to publish a substantial body of knowledge and insights about industrial applications of his research in eight groundbreaking textbooks. These books present the methodologies for: (1) industrial water savings; (2) sustainable design of polymer, refining, and adsorptive and chromatographic separation processes; and (3) intelligent design by artificial intelligence and neural computing in bioprocessing and chemical engineering. His textbooks have included 150 hands-on workshops targeted toward teaching undergraduate seniors, graduate students, and practicing engineers how to apply software tools for sustainable design and optimization.

He received the Distinguished Alumni Award and the Outstanding Career Achievement Award from Tufts University. He is a Fellow of the AIChE and a Fellow of the American Association for the Advancement of Science, cited “for excellence in design teaching, pioneering textbooks and creative scholarship in

---

<!-- PDF page 46 -->

sustainable engineering, and global leadership in implementing energy/water savings and  $ CO_{2} $ capture."

From 1986 to the worldwide pandemic in 2020, he devoted his university breaks helping petrochemical industries in developing countries and chemical industries in Virginia with technology development and engineering training. He has taught intensive training courses on computer-aided design, advanced process control, energy and water savings, and refinery and polymerization process modeling in China, Taiwan, and the USA. Liu and the instructors he trained have taught 7500 practicing engineers in courses sponsored by Aspen Technology, SINOPEC, PetroChina, Formosa Plastics Group, Honeywell, etc. For his effective blend of sustainable design education, research, and industrial outreach, he has received the Outstanding Faculty Award from Virginia's Governor, the National Friendship Award from China's Premier, and one of the U.S. Professors of the Year Awards from the Carnegie Foundation for the Advancement of Teaching and the Council for Advancement and Support of Education.

Niket Sharma received his PhD in chemical engineering and MEng in computer science with a specialization in machine learning from Virginia Tech in 2021. He is currently a senior engineer at Aspen Technology, Boston, where he is working on the development of machine learning and hybrid modeling applications combining chemical engineering and data science principles. His PhD dissertation focused on integrated process modeling and big data analytics for optimizing polyolefin manufacturing. During his PhD studies, he worked on developing an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data, for which he won the 2020 Process Development Student Paper Award from the American Institute of Chemical Engineers.

He had five years of industrial experience prior to joining graduate school at Virginia Tech. He has worked with SABIC for four years as a research engineer, where he worked on process development, scale-up, process modeling, and experiments measuring reaction kinetics and polymerization. He has also worked for a year with Indian Oil Corporation as a production engineer in the oil refinery. Niket also obtained a MEng (Chemical) from the Indian Institute of Science in 2013.

Niket is passionate about chemical engineering and the application of data science in diverse domains and wants to publish quality literature for practitioners in the industry.

---

<!-- PDF page 47 -->

## About the Companion Website

Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing is accompanied by a companion website:

www.wiley-vch.de/ISBN9783527352678

<div style="text-align: center;"><img src="imgs/img_in_image_box_521_502_585_563.jpg" alt="Image" width="6%" /></div>


The website includes:

• Example and workshop files

Scan this QR code to visit the companion website.

<div style="text-align: center;"><img src="imgs/img_in_image_box_359_699_575_914.jpg" alt="Image" width="22%" /></div>


---

<!-- PDF page 48 -->

## Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing

This chapter begins by introducing the segment-based modeling of polymerization processes developed by Aspen Technology in US Patent 5,687,090 in 1997 by Chau-Chyun Chen and Michael Barrera et al. [1]. We are happy to note that the second author of this groundbreaking patent, Michael Barrera, was a student of senior design and undergraduate research courses at Virginia Tech taught by the senior author of this book. Section 1.1 explains the component types in polymer process modeling, the concept of moments, and some basic polymer attributes (such as the number-average molecular weight, MWN, the weight-average molecular weight, MWW, and the polydispersity index, PDI). Section 1.2 presents a hands-on workshop on using Aspen Plus (which includes Aspen Polymers) to find the resulting stream attributes after mixing two copolymer streams. Section 1.3 presents a workshop for a simplified simulation model of a slurry high-density polyethylene (HDPE) process. We explain the workflow for developing a polymer process simulation model. In explaining this development, we pose motivating questions that demonstrate the significant advantages of having a process simulation model as the quantitative foundation for sustainable design and optimization, process improvement, capacity expansion, and new product design. Section 1.4 covers some examples of industrial and potential applications of polymer process modeling, advanced control, and data analytics, along with their integrated applications to optimizing polyolefin manufacturing. This chapter ends with a reference section.

### 1.1 Segment-Based Modeling of Polymerization Processes: Component Characterization and Polymer Attributes

#### 1.1.1 Component Types in Polymer Process Modeling

There are three types of components in simulating a polymer processes.

(1) Segments: They represent a repeat unit, end group, or branch point and have a well-defined molecular structure. You can see all the segments available using Aspen Plus online help and searching for “Segment databank components.”