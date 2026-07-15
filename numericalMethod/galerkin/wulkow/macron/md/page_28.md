
<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>MODEL</td><td style='text-align: center; word-wrap: break-word;'>thermodynamical modeling</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>constant temperature</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>prescribed time-dependent temperature</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>constant density</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>prescribed time-dependent density</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>constant pressure</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>prescribed time-dependent pressure</td></tr></table>

<div style="text-align: center;">Table 7: Possibilities of thermodynamical modeling.</div>


Example: (Choice of constant temperature model)

*MODEL PARAMETER

## 3 Keyword *ELEMENTS

In this block the elements, which compose a chemical species (an element must not necessarily be a chemical element), are defined. The definition of elements (and the associated species composition in block *SPECIES) allows to make a stoichiometric balance check for each chemical equation defined in block *REACTION SYSTEM. If, in addition, the atomic weight of each element is given, species molecular weights are computed and can be used to compute the initial density of the actual system internally.

Stoichiometric analysis does not work whenever macromolecular species are involved. However, it is recommended to check large pre-reaction systems separately.

Syntax rules:

i. A maximum number of MAXEL=10 elements can be declared.

ii. Element names may be composed of up to ELEML=5 alphanumeric digits (but no blank, "[ " or " ] " ), but may not start with "*" or "(".

iii. Each line of this block may contain only one element declaration.

iv. Each element name may be followed by its atomic weight (as a real number) separated by at least one blank.

v. Each element may be declared only once.

vi. The element declaration may appear anywhere in the line.

## Example: (Declaration of elements H and 0)


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">$ ^{*} $ELEMENTS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H</td><td style='text-align: center; word-wrap: break-word;'>1.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>O</td><td style='text-align: center; word-wrap: break-word;'>16.0</td></tr></table>