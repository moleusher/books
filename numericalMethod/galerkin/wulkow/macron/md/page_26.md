## 4 APPENDIX : MACRON-INPUT

This input description of MACRON is based on a not published manual of LARKIN [7]. Since the development of the program is in a state of flux, many details of the implementation will be subject to change. Updates will be announced in the respective version of MACRON. The possibility to consider thermodynamic effects is restricted to some extent if macromolecular reactions are involved. Necessary information like molecular weights or enthalpy coefficients are not defined for a macromolecular species in general. At best mean values are available. The same is true for a stoichiometric balance check. But we recommend to make use of these features for large pre-reaction systems as far as possible and applicable.

The chemical input is contained in a file called CHEMIN. Depending on the special situation, a second input file THERMO (described under the keyword *ENTHALPY COEFFICIENTS) or an input file describing an initial chain length distributions (see under *GALERKIN PROJECTION) can be used.

In Sections 4.1–2 the format directions of the input are described, in Section 4.3 the available macromolecular reactions are listed.

### 4.1 GENERAL DESCRIPTION OF THE INPUT FILE CHEMIN

The input is organized in blocks, which are opened by a keyword-line. A block is closed by opening a next one. Inside the block the user has to supply information according to a special format described below. The order of appearance of the blocks is prescribed in Table 6, but blocks, which are not necessary for the actual model, may be omitted. As far as possible a default option will be used in this case.

The following general rules should be observed by creating an input file:

i. A keyword line must start in column 1. The space after the keyword may be filled with characters according to the corresponding syntax form.

ii. A keyword may be abbreviated by its first letters, i.e. *E for *ELEMENTS, *EN for *ENTHALPY and so on. For the abbreviations see also Table 6.

iii. Comment lines must start with "*C" in column 1 and may contain any text after that.

iv. Only keyword and comment lines may start with a "*" in column 1.

v. No blank lines are allowed in the input file.

vi. The first 72 columns of each input line are read. Further information is ignored. There is an exception for the block *ENTHALPY COEFFICIENTS: in this case the first 75 columns are read with a fixed format.

### 4.2 DESCRIPTION OF THE INPUT BLOCKS

## 1 Keyword *HEAD

This block offers the possibility to identify the actual input file during the whole MACRON session by any text. Maximum number of lines for this block: 5 lines (Comment lines not counted).