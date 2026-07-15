Example: (Choice of (initial) temperature, for units see *UNIT SYSTEM.)

*TEMPERATURE

1200.D0

## 8 Keyword *PRESSURE

The block consist of one line with a positive real number setting the initial value of pressure. No initial pressure is required, if MODEL=1 or MODEL=2. If initial concentrations are not given in mole fractions and temperature is positive then the initial pressure is internally computed by means of the ideal gas law. In cases where the initial pressure can be computed internally and is given in this block, the latter value overwrites the computed one. Both values will be compared and different values will cause a warning message.

Example: (Choice of (initial) pressure, for units see *UNIT SYSTEM.)

 $ ^{*} $PRESSURE

4.36506

## 9 Keyword *DENSITY

The block consists of one line with a positive real number setting the initial value of density. No initial density is required for MODEL ≤ 4. A value for density is computed internally using the information from blocks *SPECIES and *ELEMENTS (to get species weights). Therefore this information should be complete and correct. If a value for density is given in this block, it will be used for the simulation.

Example: (Choice of (initial) pressure, for units see *UNIT SYSTEM.)

 $ ^{*} $DENSITY

1.4

## 10 Keyword *REACTION SYSTEM

In this block the whole reaction mechanism has to be defined. The reactions may be reversible or irreversible (internally counted as two reactions). The number of reactants (and products) of any equation is optional to allow the modeling of special effects – except third bodies for which only one appearance per equation is possible. Note, that the full declaration of species in block *SPECIES permits also the detection of typing errors.

Syntax rules:

i. A correct reaction equation is composed of the following components (all separated by blanks):

a. species symbols

b. delimiters

c. kinetic parameter fields

ii. A reaction may be written on several consecutive lines.