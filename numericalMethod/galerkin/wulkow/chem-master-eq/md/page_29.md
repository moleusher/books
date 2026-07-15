### 3.2 A Challenging Test Problem

As a second example, we chose a comparatively simple model problem which, however, represents a real challenge for any numerical method based on a tensor product ansatz. The corresponding reaction system (with species A, B, C) reads

 $$ \left.\begin{array}{l l l l}{{{R_{1}:}}}&{{{A}}}&{{{\xrightarrow{c_{1}}}}}&{{{B,}}} \\{{{R_{2}:}}}&{{{B}}}&{{{\xrightarrow{c_{2}}}}}&{{{A,}}} \\{{{R_{3}:}}}&{{{C}}}&{{{\xrightarrow{c_{3}}}}}&{{{A,}}} \\{{{R_{4}:}}}&{{{A+B}}}&{{{\xrightarrow{c_{4}}}}}&{{{B+B,}}} \\{{{R_{5}:}}}&{{{A+B}}}&{{{\xrightarrow{c_{5}}}}}&{{{A+A}}}\end{array}\right\} $$ 

or, in different notation,

 $$ \begin{aligned}&R_{1}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{1}}\quad(A_{i-1},B_{j+1},C_{k})\\&R_{2}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{2}}\quad(A_{i+1},B_{j-1},C_{k})\\&R_{3}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{(N-i-j)\cdot c_{3}}\quad(A_{i+1},B_{j},C_{k-1})\\&R_{4}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{4}}\quad(A_{i-1},B_{j+1},C_{k})\\&R_{5}:\quad(A_{i},B_{j},C_{k})\quad\xrightarrow{i\cdot j\cdot c_{5}}\quad(A_{i+1},B_{j-1},C_{k})\\ \end{aligned} $$ 

where again the indices refer to the molecule numbers. Since there are three species involved, the state space is actually three dimensional, but since the total number N of molecules remains invariant in all reactions, the molecule numbers of one of the species, say C, can be expressed in terms of the other ones:

 $$ x_{3}=N-x_{1}-x_{2}. $$ 

This actually reduces the three-dimensional problem to a two-dimensional one. The corresponding CME reads

 $$ \begin{aligned}\frac{\partial}{\partial t}P(t,x_{1},x_{2})\quad&=\quad c_{1}(x_{1}+1)P(t,x_{1}+1,x_{2}-1)-c_{1}x_{1}P(t,x_{1},x_{2})\quad(3.31)\\&+c_{2}(x_{2}+1)P(t,x_{1}-1,x_{2}+1)-c_{2}x_{2}P(t,x_{1},x_{2})\\&+c_{3}(N-x_{1}-x_{2}+1)P(t,x_{1}-1,x_{2})-c_{3}(N-x_{1}-x_{2})P(t,x_{1},x_{2})\\&+c_{4}(x_{1}+1)(x_{2}-1)P(t,x_{1}+1,x_{2}-1)-c_{4}x_{1}x_{2}P(t,x_{1},x_{2})\\&+c_{5}(x_{1}-1)(x_{2}+1)P(t,x_{1}-1,x_{2}+1)-c_{5}x_{1}x_{2}P(t,x_{1},x_{2}).\end{aligned} $$ 