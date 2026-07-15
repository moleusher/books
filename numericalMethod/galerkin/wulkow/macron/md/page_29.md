## 4 Keyword *SPECIES

This block can be used to define a list of species names which will appear in the reaction mechanism.

If a stoichiometric balance check is desired, all chemical species of the reaction mechanism must be declared line by line in this block, followed by their element composition. Otherwise the actual list of declared species can be a subset of all species appearing in the reaction mechanism. The information of the blocks *ELEMENT and *SPECIES can also be used for the internal computation of the initial density.

Syntax rules:

i. A maximum number of MAXSP=999 species can be declared.

ii. A species name may be composed of up to NAMEL =10 arbitrary alphanumeric digits (but no blank, " [ " or " ] " ), but may not start with a "*" or "(".

iii. Each line of this block may contain only one species declaration.

iv. Each species name may be followed by its element composition.

v. An element composition consists of a sequence of element names, each of them followed by an integer number indicating how many elements of this type compose the species.

vi. Each species may be declared only once.

vii. The species declaration may appear anywhere in the line.

Example: (Declaration of Species WATER, OH*, H2 and H*)


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">*SPECIES</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WATER</td><td style='text-align: center; word-wrap: break-word;'>H 2 0 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OH $ ^{*} $</td><td style='text-align: center; word-wrap: break-word;'>H 1 0 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H $ _{2} $</td><td style='text-align: center; word-wrap: break-word;'>H 2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H $ ^{*} $</td><td style='text-align: center; word-wrap: break-word;'>H 1</td></tr></table>

## 5 Keyword *NAME OF THIRD BODIES

This block can be used to define a list of third body species, which will appear in the reaction mechanism. See [12] for general information on third bodies.

Syntax rules:

i. A maximum number of 5 third bodies can be declared.

ii. A third body name may be composed of up to NAMEL= 10 alphanumeric digits (but no blank, "[" or "]), but may not start with a "*" or "(").

iii. Each line of this block may contain only one third body declaration.

iv. Each third body name can be followed by its species composition

v. A species composition starts with "=" followed by a sequence of species names each of them preceded by a real number which indicates the weight and followed by a "+" (except the last species). If the line ends with a real number or a "+" then the next line of input will be used also for the definition of the composition of the actual third