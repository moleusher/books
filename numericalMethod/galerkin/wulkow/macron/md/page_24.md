<div style="text-align: center;"><img src="imgs/img_in_image_box_292_365_981_790.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 9: Time evolution of  $ P_i X $ up to  $ t = 200000 $ s,  $ k_f = 10^{-2} $.</div>


situation of the step function of Sect. 2.2. In principle a polynomial approximation of the CLD's at t=0.001 is possible, but describing the fine structure of the distribution  $ P_i $ is a difficult task and polynomials of higher degree are needed. Compared to the expensive direct solution, plotted in [9], the approximation with NPROJ=80 polynomials shown in Figure 7 can be regarded as the exact solution (with the exception of slight oscillations). MACRON needed 45 s CPU time (in the mode  $ \rho = \text{constant} = 0.99 $) to obtain this result.

Note that this distribution is just the worst case of a CLD we found for this example. At processing times of technical interest (in order of hours), the distributions have not these narrow peaks and steps, which lead to this naughty error behavior. A user of MACRON, interested in the results of a reaction system after a specific reaction time, should know the grade of precision he needs. If he is really interested in P[s] at t = 0.001 with accuracy 10 %, NPROJ≈12 would be sufficient. In Figure 9 the time evolution of the species  $ P_iX $ is presented for  $ k_f = 10^{-2} $ from t = 0 up to t = 20000s, NPROJ = 80.

As a conclusion we can say that compared to present methods used in the