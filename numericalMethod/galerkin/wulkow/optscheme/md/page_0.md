Data IO line

- Stream line (physical)

## Base reaction parameters

- rgroup: category of reactants

- onm: indicates the reaction's active on metal

- ona: indicates the reactions' active on acid

- ifads: reactions' influenced by adsorption

- ifeq: reactions' influenced by equalibrim

- k: reactivity index (species structural or thermal properties)

- kv: correlation coefficients

- oH2: hydrogen order

- oR: reactants order

- description

## Adsorption parameters

Model parameters

group: category of species

k: reactivity index (species structural or thermal properties)

k*a: correlation coefficients for acid phase

k*m: correlation coefficients for metal phase

## Reactivity multiplier

-id: reaction family code

- fzc105, fzc106 ...

  (unique reactive content)

- Matrix member:

  reactivity multiplier to modify the reactivity of a

  certain reaction family on varied catalyst

Packing activity multiplier

- Metal activity multiplier

- Acid activity multiplier

## fractions properties calculation Extern, AS provided)

## Calc gasoline

- SOLs (gasoline range)

- Mass fractions

- Gasoline properties

+ Calculate gasoline pro

## lc diesel

- Mass fractions

- Diesel properties

+ Calculate diesel properties

ut: molecules and composition of fractic output: calculated fraction properties

Separation units:

- High/Low pressure system

- Stripping column

- Distillation column

Required data for fractionation study:

Flow rates

Reflux ratio/rates

Reboiler

Stream temperature/pressure

Column temperature/pressure

Parameters separation

- 1 rid (Family code)

properties dependends on rid:

rgroup, onm/a, ifads, ifeq, oH2, oR

- 2 k (Reactive index)

- 3 kv (coefficients for k)

- 4 RM (reactivity of rid on catid)

- 5 RE (effective reactivity of the cat on bedid)

## Simulation

initialize network given SOLs and reaction families set/get reaction/adsorption/equilibrium constants

## Thermodynamics

- EOS

- Mixture properties

+ Get components thermodynamic data

+ Get reaction thermodynamics data

## Network

<div style="text-align: center;"><img src="imgs/img_in_image_box_455_482_2277_6236.jpg" alt="Image" width="55%" /></div>


- Overall reaction network all components combined stoichiometric matrix

+ Set coefficients

+ Gather parameters

+ Get net production rates

Predefined methods

Reaction rules (SOL based)

- Hydrotreating rules

- Hydrocracking rules

Process separation

① Network generation:

Each bed:

② Quenching

③ Reacting (correlated T profile)

④ Reacting (with energy balance)

⑤ Cut

⑥ Equation properties calculation

## Reaction family

- Basic info

- Reactions matrix

- Stoichiometric matrix

+ Get species structures

+ Set correlation coefficients

- Current states (T, P, X, Y, F, G)

- Initialized with reactor inlet conditions

+ Advancing: while meeting quench zone: quenching inert packings: developing active packings: reacting + Output states

## Optimization/Regression Scheme (Dev)

## Molecular data preparation (Extern, ZJN provided)

- Density

- Distillation range

- Heteros contents

- Groups

- SR/(SR+LCO)

## Molecular representation

- SOLs (Designed for diesel)

- PDFs (SR and LCO)

-  $ \gamma $ (mass fractions, results)

+ Molecular representation (GA)

## Species

- Thermodynamics

- memberName

- Group contributions

+ Properties database

Provides feed SOLs and composition and all required properties

## Operational data (Seq)

- Mass flow of LCO and SR mixture

- temperature

- pressure

- new(pure) hydrogen volumetric flow

- quench hydrogen volumetric flow

- quench hydrogen purity

- quench hydrogen temperature

Inlet states of each bed:

- inlet temperature

- inlet pressure

- inlet quench hydrogen

Outlet states of each bed:

- outlet temperature

- outlet pressure

## Reactor section output

############ Profiles (~ vs. height) [Reactor1[Bed1[Packing1, ...], ...], ...]

- Temperature profiles (T)

- Concentration profiles (C)

- Flow (F, G)

- Fractions (X, Y)

- To show:

* Temperature profiles

* S, N profiles

* H2 profiles

* Groups at the end of each bed

- To compare with plant data:

* Temperature rise (due to reaction)

* Temperature drop (due to quenching)

* R101 products properties

Separation section output

## Products:

Molecules

Yields:

LPG, LN, HN, D

Products properties:

Cut points (Distillation column)

Density

Sulfur, nitrogen content

Distillation range

Fraction specific properties:

LN: RON/MON

PIONA

Aromatic potential

PIONA

Cetane number

Flash point

Group

Red items: comparable to plant data

## Operational data (reactor & separation units)

- outlet temperature

- outlet pressure

Mass flow (Yields): Stripping column:

- Cold oil (in)

- Hot oil (in)

- Top vapor&liquid (LPG?)

- Bottom liquid (to distillation)

Distillation column

- Light naphtha

- Heavy naphtha to reforming to tank

## Plant Data

## Analytical data (products)

- Density

- Distillation range

- Heteros contents

R101 outlet:

- Diesel groups analysis

Light naphtha:

- RON/MON

- PIONA

Heavy naphtha:

- Aromatic potential

- PIONA

Diesel product:

- Cetane number

- Diesel group analysis

Sim to meet plant data

## Plant data processing

- Trise

- Correlate T profile:

T = f(z) as reactor input, to perform the calculation without energy balance (Thermodynamics data might not be realizable to justify energy balance)

② After separation:

- Yields or mass flows (DCS)

- Groups (diesel, LIMS)

- PIONA (LN, HN, LIMS)

① R1 out (LIMS):

- Groups of treated products

Caution: light components removed (how?)

- S, N content

① R2 out (LIMS x DCS):

Since no direct analysis of R2 products

- Naphtha PIONA (Trusted C range)

C6 ~ C8 perhaps

- Groups (Diesel group + LN/HN PIONA)

PIO: Chains

R: Alkyl-Cyclohexane/cyclopentane

A: Alkylbenzene

Group based network, reaction route and sensitivity analysis

③ Products properties

Calculated by SOLs and mass fractions