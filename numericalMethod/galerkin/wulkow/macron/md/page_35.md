Syntax rules (same as for file THERMO):

i. The total block consists of its keyword line and an arbitrary number of subblocks.

ii. A subblock is defined by one line containing the species name followed by 3 lines containing the coefficients for this species. The data must be in the following format:

5E15.8 (also be effective for the file THERMO)

Example: (Enthalpy coefficients for species 02)

*ENTHALPY COEFFICIENTS

02 MILLER J12/820 2 0 0 0G 300.000 5000.000

0.36811543E+01 0.61174575E-03-0.10959707E-06 0.10993072E-10-0.38448244E-15 2

-0.12226443E+04 0.32938614E+01 0.33175726E+01 0.34704781E-03 0.14182033E-05 3

-0.78923112E-09-0.99682740E-13-0.10160647E+04 0.55977631E+01

## 15 *ACCURACY

The block consists of one line with the required relative accuracy for the integrator.

Remark: The accuracy should be chosen in the range 1.E-2 – 1.E-6.

Example: (Relative accuracy for the integrator set to  $ 10^{-4} $)

 $ ^{*} $ACCURACY

1.D-4

Remark: Difficulties for the integration and approximation may arise in case of too low accuracy demands. The user can test this by increasing the required accuracy (for example by a factor 10).

## 16 *INTEGRATION BOUNDS

The block consists of two lines, containing the lower and upper integration bound in seconds.

Example: (Simulation from 0 s to 1200 s)

*INTEGRATION BOUNDS

0.0

1200.0

## 17 *OUTPUT POINTS

In the first line of this block the number of output points is defined. In the following lines the values of the output points have to be given line by line. The upper integration bound is a default output point.

Example: (Three additional output points at 300 s, 600 s and 900 s)

*OUTPUT POINTS

3

300

600

900