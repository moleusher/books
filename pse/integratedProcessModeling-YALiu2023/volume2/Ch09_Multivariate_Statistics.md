# 9. Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing

<!-- PDF page 567 -->

## Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing

Chapters 9–11 of this book cover the application of big data analytics, including multivariate statistics and machine learning, to optimizing polyolefin manufacturing. Chapter 9 focuses on the use of multivariate statistics. Section 9.1 introduces an important multivariate statistics tool in process data analytics, namely, principal component analysis (PCA). Section 9.2 presents a hands-on workshop on the application of PCA for analyzing the process variables that affect quality and conversion of low-density polyethylene (LDPE) product from a two-zone tubular reactor. We introduce the use of the software tool, Aspen ProMV, for multivariate statistics applications. This tool is available to universities at low cost. Section 9.3 introduces the projection to latent structures, or partial least squares (PLS). A key difference between PCA and PLS is that PCA involves only datasets of process variables (X) or deals with the X-space; PLS involves datasets of both process variables (X) and product quality variables (Y) or deals with both X-space and Y-space. Section 9.4 presents two hands-on workshops on applying PLS to the LDPE problem of Section 9.2 and to the melt index prediction and causal analysis of a HDPE manufacturing process. Section 9.5 introduces PLS for process data analytics with measurement time lags and includes a hands-on workshop on PLS for a HDPE process for the melt index prediction and causal analysis, including the effect of time lags on melt index measurements. Section 9.6 covers the process data analytics for batch polymer processes and presents a hands-on workshop to demonstrate the multiway PCA and PLS methodologies, particularly the batch-wise unfolding (BWU) approach, for data analytics. Section 9.7 describes the implementation of multivariate statistics models, and Section 9.8 presents the conclusions and suggested resources for further reading. This chapter ends with references.

### 9.1 Introduction to Principal Component Analysis (PCA)

Beginning in late 1980 to early 1990, chemical engineers have been paying increasing attention to the emerging topics of artificial intelligence, neural computing, multivariate statistics, machine learning, and big data analytics and their applications to bioprocessing and chemical engineering [1-5]. MacGregor and others

---

<!-- PDF page 568 -->

have demonstrated the significant applications of multivariate statistics and big data analytics to optimizing the manufacturing of LDPE, HDPE, Nylon 6, and other polymers [6–10]. Multivariate statistical analysis [11–13] and its implementation using languages such as Python and R or software such as Aspen ProMV, SAS, and JMP are finding a growing number of applications in polymer manufacturing. These include: (1) data quality deviation analysis; (2) unit yield analysis; (3) production capacity degradation analysis; (4) offline production optimization (discovery and optimization of key variables); (5) online process monitoring and troubleshooting; and (6) batch process variable analysis.

This section introduces the PCA, following the multivariate statistical analysis textbooks of Johnson and Wichern  $ [11] $ and Rencher and Christensen  $ [12] $ and the excellent online book of Dunn  $ [13] $, which is continually updated. The online reader is allowed “to freely download, share, adapt, commercialize, and attribute” some of the book materials, as long as the reader acknowledges that “Portions of this work are the copyright of Kevin Dunn.” That is exactly what we wish to acknowledge here, as we shall use some of the explanations and figures from Ref.  $ [13] $ below.

Both textbooks [11, 12] include a chapter on matrix algebra relevant to multivariate statistical analysis. Therefore, we have included an Appendix A, Matrix Algebra in Multivariate Data Analysis and Model-Predictive Control Using MATLAB and Python, at the end of this book. This appendix also includes the basic implementation of the relevant matrix operations and PCA in both MATLAB and Python.

#### 9.1.1 Introduction to Principal Components

We follow [14] to illustrate the concept of principal components. Figure 9.1 shows a 3D image of some process data. When projecting the same data onto a 2D plane in Figure 9.2, we are unable to observe the same 3D relationship. However, we can observe sufficient characteristics of the original 3D image in two dimensions if we can identify two linear combinations of process variables x, y, and z in order to capture most of the variations in these three process variables. See Figure 9.3.

In Figure 9.3, we see the characteristics of the original 3D image on a two-dimensional plane of two linear combinations (LV1 and LV2) of the process variables  $ (x, y, \text{ and } z) $:

 $$ \mathrm{LV1}=0.1658x+0.6120y+0.7733z $$ 

 $$  LV2=-0.9652x+0.2615y $$ 

We call these linear combinations the latent variables or principal components of the process variables.

PCA is a data transformation method that rotates data such that the principal axis of the data is in the direction of maximum variation. See Figure 9.4. We follow the interpretation of [15] here. The first latent variable or first principal component of the process data or observations given by Eq. (9.1a) represents the linear combination of the original process variables whose sample variance (see Appendix A, Section A.1.6) is the greatest among all possible linear combinations. The second

---

<!-- PDF page 569 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th><th style='text-align: center;'>z</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>-2.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>-3.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>-4.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>-5.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>-6.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>-7.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>-8.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>-9.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>-10.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>-11.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>-12.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>-13.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>8.5</td><td style='text-align: center;'>-14.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>-15.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>-16.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>-17.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>10.5</td><td style='text-align: center;'>-18.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>-19.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>11.5</td><td style='text-align: center;'>-20.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>-21.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>-22.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>-23.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>13.5</td><td style='text-align: center;'>-24.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>-25.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>-26.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>-27.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>-28.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>16.0</td><td style='text-align: center;'>-29.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>16.5</td><td style='text-align: center;'>-30.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>-31.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>-32.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>-33.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>18.5</td><td style='text-align: center;'>-34.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>19.0</td><td style='text-align: center;'>-35.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>-36.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>-37.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>20.5</td><td style='text-align: center;'>-38.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>21.0</td><td style='text-align: center;'>-39.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>21.5</td><td style='text-align: center;'>-40.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>-41.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>22.5</td><td style='text-align: center;'>-42.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>23.0</td><td style='text-align: center;'>-43.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>23.5</td><td style='text-align: center;'>-44.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>24.0</td><td style='text-align: center;'>-45.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>24.5</td><td style='text-align: center;'>-46.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>-47.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>25.5</td><td style='text-align: center;'>-48.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>26.0</td><td style='text-align: center;'>-49.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>26.5</td><td style='text-align: center;'>-50.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>-51.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>27.5</td><td style='text-align: center;'>-52.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>28.0</td><td style='text-align: center;'>-53.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>28.5</td><td style='text-align: center;'>-54.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>-55.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>29.5</td><td style='text-align: center;'>-56.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>-57.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>30.5</td><td style='text-align: center;'>-58.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>31.0</td><td style='text-align: center;'>-59.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>31.5</td><td style='text-align: center;'>-60.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>-61.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>32.5</td><td style='text-align: center;'>-62.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>33.0</td><td style='text-align: center;'>-63.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>33.5</td><td style='text-align: center;'>-64.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>34.0</td><td style='text-align: center;'>-65.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>34.5</td><td style='text-align: center;'>-66.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>-67.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>35.5</td><td style='text-align: center;'>-68.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>36.0</td><td style='text-align: center;'>-69.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>36.5</td><td style='text-align: center;'>-70.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>37.0</td><td style='text-align: center;'>-71.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>37.5</td><td style='text-align: center;'>-72.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>-73.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>38.5</td><td style='text-align: center;'>-74.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>39.0</td><td style='text-align: center;'>-75.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>39.5</td><td style='text-align: center;'>-76.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>40.0</td><td style='text-align: center;'>-77.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>40.5</td><td style='text-align: center;'>-78.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>41.0</td><td style='text-align: center;'>-79.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>41.5</td><td style='text-align: center;'>-80.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>42.0</td><td style='text-align: center;'>-81.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>42.5</td><td style='text-align: center;'>-82.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>43.0</td><td style='text-align: center;'>-83.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>43.5</td><td style='text-align: center;'>-84.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>44.0</td><td style='text-align: center;'>-85.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>44.5</td><td style='text-align: center;'>-86.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>45.0</td><td style='text-align: center;'>-87.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>45.5</td><td style='text-align: center;'>-88.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>46.0</td><td style='text-align: center;'>-89.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>46.5</td><td style='text-align: center;'>-90.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>-91.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>47.5</td><td style='text-align: center;'>-92.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>48.0</td><td style='text-align: center;'>-93.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>48.5</td><td style='text-align: center;'>-94.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>49.0</td><td style='text-align: center;'>-95.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>49.5</td><td style='text-align: center;'>-96.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>-97.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>50.5</td><td style='text-align: center;'>-98.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>51.0</td><td style='text-align: center;'>-99.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>51.5</td><td style='text-align: center;'>-100.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>52.0</td><td style='text-align: center;'>-101.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>52.5</td><td style='text-align: center;'>-102.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>53.0</td><td style='text-align: center;'>-103.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>53.5</td><td style='text-align: center;'>-104.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>54.0</td><td style='text-align: center;'>-105.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>54.5</td><td style='text-align: center;'>-106.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>55.0</td><td style='text-align: center;'>-107.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>55.5</td><td style='text-align: center;'>-108.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>56.0</td><td style='text-align: center;'>-109.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>56.5</td><td style='text-align: center;'>-110.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>57.0</td><td style='text-align: center;'>-111.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>57.5</td><td style='text-align: center;'>-112.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>58.0</td><td style='text-align: center;'>-113.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>58.5</td><td style='text-align: center;'>-114.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>59.0</td><td style='text-align: center;'>-115.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>59.5</td><td style='text-align: center;'>-116.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>60.0</td><td style='text-align: center;'>-117.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>60.5</td><td style='text-align: center;'>-118.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>61.0</td><td style='text-align: center;'>-119.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>61.5</td><td style='text-align: center;'>-120.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'>-121.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>62.5</td><td style='text-align: center;'>-122.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>63.0</td><td style='text-align: center;'>-123.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>63.5</td><td style='text-align: center;'>-124.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>64.0</td><td style='text-align: center;'>-125.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>64.5</td><td style='text-align: center;'>-126.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>65.0</td><td style='text-align: center;'>-127.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>65.5</td><td style='text-align: center;'>-128.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>66.0</td><td style='text-align: center;'>-129.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>66.5</td><td style='text-align: center;'>-130.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>67.0</td><td style='text-align: center;'>-131.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>67.5</td><td style='text-align: center;'>-132.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>68.0</td><td style='text-align: center;'>-133.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>68.5</td><td style='text-align: center;'>-134.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>69.0</td><td style='text-align: center;'>-135.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>69.5</td><td style='text-align: center;'>-136.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>70.0</td><td style='text-align: center;'>-137.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>70.5</td><td style='text-align: center;'>-138.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>71.0</td><td style='text-align: center;'>-139.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>71.5</td><td style='text-align: center;'>-140.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>72.0</td><td style='text-align: center;'>-141.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>72.5</td><td style='text-align: center;'>-142.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>73.0</td><td style='text-align: center;'>-143.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>73.5</td><td style='text-align: center;'>-144.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>74.0</td><td style='text-align: center;'>-145.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>74.5</td><td style='text-align: center;'>-146.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>75.0</td><td style='text-align: center;'>-147.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>75.5</td><td style='text-align: center;'>-148.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>76.0</td><td style='text-align: center;'>-149.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>76.5</td><td style='text-align: center;'>-150.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>77.0</td><td style='text-align: center;'>-151.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>77.5</td><td style='text-align: center;'>-152.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>78.0</td><td style='text-align: center;'>-153.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>78.5</td><td style='text-align: center;'>-154.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>79.0</td><td style='text-align: center;'>-155.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>79.5</td><td style='text-align: center;'>-156.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>80.0</td><td style='text-align: center;'>-157.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>80.5</td><td style='text-align: center;'>-158.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>81.0</td><td style='text-align: center;'>-159.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>81.5</td><td style='text-align: center;'>-160.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>82.0</td><td style='text-align: center;'>-161.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>82.5</td><td style='text-align: center;'>-162.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>83.0</td><td style='text-align: center;'>-163.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>83.5</td><td style='text-align: center;'>-164.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>84.0</td><td style='text-align: center;'>-165.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>84.5</td><td style='text-align: center;'>-166.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>85.0</td><td style='text-align: center;'>-167.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>85.5</td><td style='text-align: center;'>-168.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>86.0</td><td style='text-align: center;'>-169.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>86.5</td><td style='text-align: center;'>-170.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>87.0</td><td style='text-align: center;'>-171.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>87.5</td><td style='text-align: center;'>-172.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>88.0</td><td style='text-align: center;'>-173.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>88.5</td><td style='text-align: center;'>-174.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>89.0</td><td style='text-align: center;'>-175.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>89.5</td><td style='text-align: center;'>-176.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>90.0</td><td style='text-align: center;'>-177.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>90.5</td><td style='text-align: center;'>-178.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>91.0</td><td style='text-align: center;'>-179.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>91.5</td><td style='text-align: center;'>-180.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>92.0</td><td style='text-align: center;'>-181.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>92.5</td><td style='text-align: center;'>-182.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>93.0</td><td style='text-align: center;'>-183.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>93.5</td><td style='text-align: center;'>-184.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>94.0</td><td style='text-align: center;'>-185.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>94.5</td><td style='text-align: center;'>-186.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>-187.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>95.5</td><td style='text-align: center;'>-188.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>96.0</td><td style='text-align: center;'>-189.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>96.5</td><td style='text-align: center;'>-190.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>97.0</td><td style='text-align: center;'>-191.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>97.5</td><td style='text-align: center;'>-192.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>98.0</td><td style='text-align: center;'>-193.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>98.5</td><td style='text-align: center;'>-194.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>99.0</td><td style='text-align: center;'>-195.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>99.5</td><td style='text-align: center;'>-196.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>-197.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>100.5</td><td style='text-align: center;'>-198.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>101.0</td><td style='text-align: center;'>-199.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>101.5</td><td style='text-align: center;'>-200.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>102.0</td><td style='text-align: center;'>-201.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>102.5</td><td style='text-align: center;'>-202.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>103.0</td><td style='text-align: center;'>-203.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>103.5</td><td style='text-align: center;'>-204.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>104.0</td><td style='text-align: center;'>-205.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>104.5</td><td style='text-align: center;'>-206.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>105.0</td><td style='text-align: center;'>-207.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>105.5</td><td style='text-align: center;'>-208.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>106.0</td><td style='text-align: center;'>-209.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>106.5</td><td style='text-align: center;'>-210.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>107.0</td><td style='text-align: center;'>-211.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>107.5</td><td style='text-align: center;'>-212.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>108.0</td><td style='text-align: center;'>-213.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>108.5</td><td style='text-align: center;'>-214.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>109.0</td><td style='text-align: center;'>-215.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>109.5</td><td style='text-align: center;'>-216.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>110.0</td><td style='text-align: center;'>-217.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>110.5</td><td style='text-align: center;'>-218.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>111.0</td><td style='text-align: center;'>-219.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>111.5</td><td style='text-align: center;'>-220.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>112.0</td><td style='text-align: center;'>-221.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>112.5</td><td style='text-align: center;'>-222.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>113.0</td><td style='text-align: center;'>-223.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>113.5</td><td style='text-align: center;'>-224.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>114.0</td><td style='text-align: center;'>-225.0</td></tr>
    <tr><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.1 The original 3D image of process data. Used with permission from Aspen Technology, Inc.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.2 Losing the characteristics of the original 3D image when projecting onto the x-y plane. Used with permission from Aspen Technology, Inc.</div>


latent variable or second principal component represents the linear combination of the original process variables that accounts for a maximum proportion of the remaining variance, subject to being uncorrelated with the first principal component. We can define subsequent principal components similarly.

We can view the rotated data on the new principal axes (components). We call the coordinates of the data in this new coordinate system as principal component scores. They are essentially the projection of the data onto the principal axes. As seen in Figure 9.4, the principal components are essentially vectors in the original variable

---

<!-- PDF page 570 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>LV 2 = (-0.9652*X) + (0.2615*Y)</th><th style='text-align: center;'>1st Principal component (direction of maximum variance)</th><th style='text-align: center;'>1st Principal component (direction of maximum variance)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.8</td><td style='text-align: center;'>-0.8</td><td style='text-align: center;'>-0.8</td></tr>
    <tr><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.5</td></tr>
    <tr><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>6.5</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.3 Retaining the characteristics of the original 3D image when displaying on the two-dimensional plane of latent variables LV1 and LV2 (or principal components 1 and 2). Source: Used with permission from Aspen Technology, Inc.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Variable</th><th style='text-align: center;'>Original variable 1</th><th style='text-align: center;'>Original variable 2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>Original</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>Principal component (direction of maximum variance)</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.85</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.4 An illustration of the principal component that shows the direction of maximum variation of the process data.</div>


space, and these vectors are called principal component loadings. We quantify both the principal component scores and loadings and their relationship to the original process data matrix in the following section.

#### 9.1.2 Data Preprocessing: Mean-Centered and Scaled Process Data Matrix X, Principal Component Score Matrix T, and Principal Component Loading Matrix P

We follow [13] for the development of the PCA model. Let us consider a  $ J \times K $ process data matrix  $ \mathbf{X} $ with  $ K $ columns of process variables  $ x_k $ ( $ k = 1, 2, \ldots, K $), and with each

---

<!-- PDF page 571 -->

<div style="text-align: center;">Figure 9.5 The projection of the kth process variable vector  $ \mathbf{x}_k $ onto the first principal component loading vector  $ \mathbf{p}_1 $.  $ t_{k,1} $ is the score value of  $ \mathbf{x}_k $ on  $ \mathbf{p}_1 $.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_433_149_797_384.jpg" alt="Image" width="37%" /></div>


variable  $ x_k $ having  $ J $ observations or measured values,  $ x_{1k} $,  $ x_{2k} $,  $ x_{3k} $, ...,  $ x_{Jk} $ (or  $ x_{jk} $,  $ j = 1 $, 2, ...,  $ J $). In Appendix A, Section A.1.7, we introduce the standardized data matrix, or mean-centered and scaled data matrix  $ \mathbf{X}\mathbf{s} $, and the correlation coefficient matrix  $ \mathbf{R} $ from the process data matrix  $ \mathbf{X} $.

To correctly carry out PCA, we first preprocess the data. Specifically, we start with a data standardization step to convert the process data matrix X to a standardized data matrix Xs that is mean-centered and scaled by standard deviation [11, 13]. For convenience in eliminating the letter “s” from a mean-centered and scaled data matrix Xs, we assume in the following discussion that our process data matrix X has already gone through a standardization procedure described in Appendix A, Sections A.1.5–A.1.7. As we demonstrate in Appendix A, it only takes a single command using Matlab [zscore(X)] or Python [stats.zscore()], to standardize a process data matrix X.

#### 9.1.3 Development of PCA Model

We write the standardized data matrix X as a matrix of K process variable vectors:

 $$ \mathbf{X}=[\mathbf{x}_{1}~\mathbf{x}_{2}~\ldots~\mathbf{x}_{\mathbf{K}}]=\begin{bmatrix}x_{11}&\cdots&x_{1k}\\ \vdots&\ddots&\vdots\\ x_{j1}&\cdots&x_{jk}\end{bmatrix} $$ 

In this matrix, the  $ k $th process variable vector  $ \mathbf{x}_k $ is a  $ (J \times 1) $ column vector,  $ [x_{1k}, x_{2k}, x_{3k}, \ldots, x_{Jk}]' $, where  $ J $ is the number of samples or measurements. The transpose of  $ \mathbf{x}_k $, or  $ \mathbf{x}_k' $, is a  $ (1 \times J) $ observation vector.

Figure 9.5 illustrates the projection of the vector  $ \mathbf{x}_k $ onto the first principal component vector  $ \mathbf{p}_1 $. The score value  $ t_{k,1} $ for this observation vector is the distance from the origin along the principal component loading vector,  $ \mathbf{p}_1 $, to the point where we find the perpendicular projection onto  $ \mathbf{p}_1 $ [13].

We can write from geometry that: (1) the cosine of an angle in a right-angled triangle is the ratio of the adjacent side to the hypotenuse; (2) the cosine of the angle defines the dot product of two vectors. See Eqs. (9.3) and (9.4):

 $$ \cos\theta=(adjacent length)/(hypotenuse)=t_{k,1}/||\mathbf{x_{k}}|| $$ 

 $$ \cos\theta=\mathbf{x}_{\mathbf{k}}^{\prime}\mathbf{p}_{1}/\|\mathbf{x}_{\mathbf{k}}\|\|\mathbf{p}_{1}\| $$ 

---

<!-- PDF page 572 -->

where  $ \|\cdot\| $ represents the length of the enclosed vector, and the length of the principal component loading vector,  $ \|\mathbf{p}_1\| $ is 1.0. Therefore, we find:

 $$ t_{k,1}=\mathbf{x}_{\mathbf{k}}^{\prime}\mathbf{p}_{1}=x_{k,1}p_{1,1}+x_{k,2}p_{2,1}+\cdots+x_{k,j}p_{j,1}\cdots+x_{k,J}p_{J,1} $$ 

Likewise, we write

 $$ t_{k,2}=\mathbf{x}_{\mathbf{k}}^{\prime}\mathbf{p}_{2}=x_{k,1}p_{1,2}+x_{k,2}p_{2,2}+\cdots+x_{k,j}p_{j,2}\cdots+x_{k,J}p_{J,2} $$ 

Generalizing Eqs. (9.5) and (9.6), we write the principal component score vector  $ \mathbf{t}_k $, resulting from projecting the process data vector  $ \mathbf{x}_k $ onto A principal component loading vectors, expressed by the  $ (K \times A) $ loading matrix  $ \mathbf{P} $:

 $$ \begin{aligned}\mathbf{t}_{\mathbf{k}}^{\prime}&=\mathbf{x}_{\mathbf{k}}^{\prime}\mathbf{P}\ $ 1\times A)&=(1\times K)(K\times A)\end{aligned} $$ 

Lastly, we can represent the projection of the entire process data matrix X in terms of a principal component score matrix T and a principal component loading matrix P:

 $$ \begin{aligned}\mathbf{T}&=\mathbf{X}\mathbf{P}\ $ J\times A)&=(J\times K)(K\times A)\end{aligned} $$ 

where J is the number of samples or measurements, A is the number of principal components, and K is the number of process variables.

#### 9.1.4 Prediction Errors from PCA Model

Figure 9.6 illustrates the projection of the original data vector  $ \mathbf{x}_k $ onto the first principal component vector  $ \mathbf{p}_1 $. The best estimate of  $ \mathbf{x}_k $ is a vector  $ \widehat{\mathbf{x}}_{k,1} $ along the first principal component loading vector  $ \mathbf{p}_1 $, where the original vector is projected. We call this estimate of the data vector,  $ \widehat{\mathbf{x}}_{k,1} $. We note the distance along the first principal component loading vector  $ \mathbf{p}_1 $ is the principal component score  $ t_{k,1} $. Based on vector geometry, we represent the error between  $ \mathbf{x}_k $ and  $ \widehat{\mathbf{x}}_{k,1} $ as an error vector  $ \mathbf{e}_{k,1} $.

We write the prediction vector as:

 $$ \begin{aligned}\widehat{\boldsymbol{x}}_{k,1}^{\prime}&=t_{k,1}\boldsymbol{p}_{1}^{\prime}\ $ 1\times K)&=(1\times1)(1\times K)\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_1025_507_1282.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">Figure 9.6 The projection of the kth process variable vector  $ \mathbf{x}_k $ onto the first principal component vector  $ \mathbf{p}_1 $, indicating an estimate of the data vector  $ \hat{\mathbf{x}}_{k,1} $, together with an error vector  $ \mathbf{e}_{k,1} \cdot t_{k,1} $ is the score value of  $ \mathbf{x}_k $ on  $ \mathbf{p}_1 $.</div>


---

<!-- PDF page 573 -->

and the corresponding prediction error vector is:

 $$ \begin{aligned}\mathbf{e}_{k,1}^{\prime}&=\mathbf{x}_{k}^{\prime}-\widehat{\mathbf{x}}_{K,1}^{\prime}\ $ 1\times K)&=(1\times K)-(1\times K)\end{aligned} $$ 

Adding the second principal component vector  $ \mathbf{p}_{2} $, we generalize the prediction vector from Eq. (9.9) as:

 $$ \begin{aligned}\widehat{\boldsymbol{x}}_{k,2}^{\prime}&=t_{k,1}\boldsymbol{p}_{1}^{\prime}+t_{k,2}\boldsymbol{p}_{2}^{\prime}\ $ 1\times K)&=(1\times K)+(1\times K)\end{aligned} $$ 

where  $ t_{k,1} $ and  $ t_{k,2} $ are the score values of  $ x_{k,2} $ on  $ p_{1} $ and  $ p_{2} $, respectively.

Extending Eq. (9.11) to A principal component vectors, we write the projector vector of the original data vector  $ \mathbf{x}_k $ onto the A principal component loading vectors  $ [\mathbf{p}_1 \mathbf{p}_2 \ldots \mathbf{p}_A] $ or principal component loading matrix  $ \mathbf{P} $, with  $ \mathbf{t}_k $ being the score vector:

 $$ \begin{aligned}\widehat{\boldsymbol{x}}_{k,A}^{\prime}&=\left[t_{k,1}t_{k,2}\ldots,t_{k,A}\right]\mathbf{P}^{\prime}=\mathbf{t}_{k}^{\prime}\mathbf{P}^{\prime}\ $ 1\times A)&=(1\times A)(A\times K)\end{aligned} $$ 

We generalize Eq. (9.12) to represent the entire data prediction matrix  $ \hat{X} $ in terms of the score matrix T and the principal component loading matrix P:

 $$ \begin{aligned}\hat{\mathbf{X}}=\mathbf{T}\mathbf{P}^{\prime}\ $ J\times K)=(J\times A)(A\times K)\end{aligned} $$ 

We define the residual vector  $ \mathbf{e}_{k,A} $ for the  $ k $th process variable using  $ \mathbf{A} $ principal components as the difference between the actual and predicted observations:

 $$ \begin{aligned}\boldsymbol{e}_{k,A}^{\prime}&=\boldsymbol{x}_{k}^{\prime}-\widehat{\boldsymbol{x}}_{k,A}=\boldsymbol{x}_{k}^{\prime}-\mathbf{t}_{k}^{\prime}\mathbf{P}^{\prime}\ $ 1\times A)&=(1\times A)-(1\times A)\end{aligned} $$ 

Referring to Figure 9.7, we define the row residual or the squared prediction error (SPE) for kth process variable as:

 $$ \begin{aligned}\mathrm{SPE}_{k}&=\left(\boldsymbol{e}_{k,A}^{\prime}\cdot\boldsymbol{e}_{k,A}\right)^{1/2}\\&=\left[\left(x_{k,1}-\widehat{x}_{k,1}^{\prime}\right)^{2}+\left(x_{k,2}-\widehat{x}_{k,2}^{\prime}\right)^{2}+\cdots\cdots+\left(x_{k,A}-\widehat{x}_{k,A}^{\prime}\right)\right]^{1/2}\end{aligned} $$ 

The corresponding vector representation of all  $  \mathrm{SPE}_{k} \left( k = 1, 2, \ldots, K \right)  $ for all K process variables is

 $$ \mathbf{S}\mathbf{P}\mathbf{E}=[\mathbf{S}\mathbf{P}\mathbf{E}_{1}~\mathbf{S}\mathbf{P}\mathbf{E}_{2}~\ldots~\mathbf{S}\mathbf{P}\mathbf{E}_{k}]^{\prime} $$ 

We write Eq. (9.14) as a prediction error or residual matrix E for all K process variables, J observations per variable, and A principal component loading vectors  $ [p_1 \quad p_2 \quad \ldots \quad p_A] $ or principal component loading matrix P as follows:

 $$ \mathbf{E}=\mathbf{X}-\widehat{\mathbf{X}}=\mathbf{X}-\mathbf{T}\mathbf{P}^{\prime}\quad or\quad\mathbf{X}=\mathbf{T}\mathbf{P}^{\prime}+\mathbf{E} $$ 

---

<!-- PDF page 574 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_144_826_302.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Figure 9.7 An illustration of the relationships among the prediction error matrix E, process variable matrix X, predicted process variable matrix  $ \hat{X} $, and squared prediction error matrix SPE.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_423_827_600.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">Figure 9.8 An illustration of the relationships among the prediction error matrix E, process variable matrix X, predicted process variable matrix  $ \hat{X} $, and column, or the prediction error for kth process variable (column).</div>


Figure 9.7 illustrates the relationship between E, X,  $ \hat{X} $, and SPE.

In Figure 9.7, each row of E contains the row residual or the prediction error for jth observation  $ (j=1,2,\ldots,J) $ for all K process variables.

Figure 9.8 shows a similar plot, focusing on the column residual, or the prediction error for each column that represents the kth process variable  $ (k=1,2,\ldots,K) $ in the residual matrix E [13].

Each column of E contains the prediction error for one variable. Referring to the discussion of least squares model analysis on pages 165–168 of [13], we can find the  $ R^{2} $ value for the kth process variable (column) as:

 $$ R_{k}^{2}=R_{X,k}^{2}=1-\frac{\mathrm{Var}(x_{k-}\widehat{\boldsymbol{x}}_{k})}{\mathrm{Var}(x_{k})}=\frac{\mathrm{Var}(e_{k})}{\mathrm{Var}(x_{k})} $$ 

The  $ R_k^2 $ value for each process variable will increase with every principal component that is added to the model. The minimum value is 0.0 when there is no principal component, and  $ \hat{x}_k = 0 $. The maximum value is 1.0 when we have added the maximum number of principal components with  $ x_i = \hat{x}_i $, and  $ e_i = 0 $.

We can extend the preceding row residual and column residual concepts to the whole process data matrix X and calculate the  $ R^2 $ value of the entire matrix [13]. This value is the ratio of the variance of X that we can explain with the PCA model over the ratio of variance initially present in X.

 $$ R^{2}=1-\frac{\mathrm{Var}(\boldsymbol{X}-\widehat{\boldsymbol{X}})}{\mathrm{Var}(\boldsymbol{X})}=1-\frac{\mathrm{Var}(\boldsymbol{E})}{\mathrm{Var}(\boldsymbol{X})} $$ 

---

<!-- PDF page 575 -->

By using ML or Python (see Appendix A) or Aspen Technology’s software Aspen ProMV, we can evaluate the  $ R^2 $ value and identify the number of principal components needed to adequately explain the data variability in X. We have demonstrated this aspect in Appendix A and will illustrate this aspect in our hands-on workshop WS9.1, in which Aspen ProMV shows the  $ R^2 $ value as R2 for different numbers of principal components.

Lastly, page 380 of Dunn [13] explains the concept of determining the number of principal components to use in a model based on cross-validation (CV), originally proposed by Wold [16]. We follow Dunn’s exposition below.

The general idea is to divide the process data matrix  $ \mathbf{X} $ into  $ G $ groups of rows. These rows should be selected randomly, but they are often selected in order: row 1 goes in group 1, row 2 goes in group 2, and so on. We can collect the rows belonging to the first group into a new matrix called  $ \mathbf{X}_{(1)} $ and leave behind all the other rows from all other groups, which we will call group  $ \mathbf{X}_{(-1)} $. So in general, for the  $ 6\text{th} $ group, we can split matrix  $ \mathbf{X} $ into  $ \mathbf{X}_{(g)} $ and  $ \mathbf{X}_{(-g)} $. Wold's cross-validation procedure asks to build the PCA model on the data in  $ \mathbf{X}_{(-1)} $ using  $ A $ components. Then use data in  $ \mathbf{X}_{(1)} $ as new, testing data. In other words, we preprocess the  $ \mathbf{X}_{(1)} $ rows, calculate their score values,  $ \mathbf{T}_{(1)} = \mathbf{X}_{(1)} \mathbf{P} $, calculate their predicted values,  $ \tilde{\mathbf{X}}_{(1)} = \mathbf{T}_{(1)} \mathbf{P}' $ and their residuals,  $ \mathbf{E}_{(1)} = \mathbf{X}_{(1)} - \hat{\mathbf{X}}_{(1)} $. We repeat this process, building the model on  $ \mathbf{X}_{(-2)} $ and testing it with  $ \mathbf{X}_{(2)} $, to eventually obtain  $ \mathbf{E}_{(2)} $. After repeating this on  $ G $ groups, we gather up  $ \mathbf{E}_1 $,  $ \mathbf{E}_2 $, ...,  $ \mathbf{E}_G $ and assemble a type of residual matrix,  $ \mathbf{E}_{A,CV} $, where the  $ A $ represents the number of components used in each of the  $ G $ PCA models. The CV subscript indicates that this is not the usual error matrix,  $ E $. From this, we can calculate a type of  $ R^2 $ value. We do not call this  $ R^2 $, but it follows the same definition for an  $ R^2 $ value. We will call it  $ Q^{2}_A $ instead, where  $ A $ is the number of components used to fit the  $ G $ models.

 $$ Q2_{A}=1-\operatorname{Var}(E_{A,CV})/\operatorname{Var}(X) $$ 

Essentially,  $ Q2_A $ is a measure of how well the process variables will be predicted with new data calculated by cross-validation. In our hands-on workshop WS9.1, Aspen ProMV shows the  $ Q^2 $ value as Q2 for different numbers of principal components with cross-validation.

#### 9.1.5 Hotelling's  $ T^{2} $ Value from PCA Model

In Figure 9.6, we illustrate the score value  $ \mathbf{t}_{\mathbf{k},1} $ of process variable vector  $ \mathbf{x}_{\mathbf{k}} $ on the first principal component  $ \mathbf{p}_{1} $. Let  $ t_{k,a} $ ( $ k=1,2,\ldots,K $;  $ a=1,2,\ldots,A $) be the score value of  $ k $th process variable  $ \mathbf{x}_{\mathbf{k}} $ on the  $ a $th principal component, and  $ s_{a} $ ( $ a=1,2,\ldots,A $) be the variance of the  $ a $th principal component. Then, the Hotelling's  $ \mathbf{T}^{2} $ value for the  $ k $th process variable is:

 $$ T^{2}=\Sigma(t_{k,a}/s_{a})^{2} $$ 

 $ T^{2} $ value is a positive, scalar number that summarizes all the score values. It represents the distance from the center of the hyperplane of process variables to the projection of the sample onto the hyperplane. Samples that are very close to the sample mean give a  $ T^{2} $ value of zero [15].

---

<!-- PDF page 576 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>t₁</th><th style='text-align: center;'>t₂</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>-3.2</td></tr>
    <tr><td style='text-align: center;'>-3.2</td><td style='text-align: center;'>-3.0</td></tr>
    <tr><td style='text-align: center;'>-2.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>-2.2</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>-1.5</td></tr>
    <tr><td style='text-align: center;'>-1.8</td><td style='text-align: center;'>-2.5</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>-3.5</td></tr>
    <tr><td style='text-align: center;'>-1.2</td><td style='text-align: center;'>-3.8</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>-3.0</td></tr>
    <tr><td style='text-align: center;'>-0.8</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>-0.2</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>-0.5</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>-2.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>-0.5</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>2.2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.9 An illustration of the concept of Hotelling's  $ T^{2} $ value in a two-latent variable or a two-principal-component space,  $ t_{2} $ versus  $ t_{1} $.</div>


Figure 9.9 illustrates the concept of Hotelling's  $ \mathbf{T}^{2} $ value for an example with two principal components (A = 2):

 $$ T^{2}=\frac{t_{1}^{2}}{S_{1}^{2}}+\frac{t_{2}^{2}}{S_{2}^{2}} $$ 

In the figure, the equation for  $ \mathbf{T}^2 $, Eq. (9.21), is that of an ellipse.  $ \mathbf{T}^2 $ expresses how far an observation is from the center of the model on the plane. All points on the ellipse have the same  $ \mathbf{T}^2 $ value.

We note that references [11, 15], among others, have presented the detailed development, showing that the variances of principal components  $ s_a $ ( $ a = 1, 2, \ldots, A $) are actually the eigenvalues of the correlation coefficient matrix  $ \mathbf{R} $, which is introduced in Appendix A, Section A.1.7, and Eq. (A.24), based on the standardized data matrix  $ \mathbf{X}\mathbf{s} $. Additionally, the eigenvectors of  $ \mathbf{R} $ correspond to principal component loading vectors  $ \mathbf{p}_a $ ( $ a = 1, 2, \ldots, A $). Extracting principal components as the eigenvectors of  $ \mathbf{R} $ is equivalent to calculating the principal components from the original variables after each has been standardized to have zero mean and unit variance [13], as we discussed in Appendix A, Sections A.1.5–A.1.7.

In Appendix B of this book, code B.8 and Table B.1 at the end give the Python implementation of the PCA algorithm, together with a list of common parameters and their suggested values.

#### 9.2 Workshop 9.1: PCA of the Process Variables Affecting the Quality and Conversion of LDPE Product from a Two-Zone Tubular Reactor

We demonstrate the development of a PCA model for analyzing the quality and conversion of a two-zone tubular reactor for producing LDPE. The problem comes from references  $ [6, 17] $, and the process data for LDPE are available in  $ [17] $. We use

---

<!-- PDF page 577 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_149_777_436.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 9.10 A schematic diagram of a two-zone tubular reactor for producing LDPE.</div>


<div style="text-align: center;">Table 9.1 Process and quality variables for Workshop 9.1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Process variables (X)</td><td style='text-align: center; word-wrap: break-word;'>Quality variables (Y)</td></tr><tr><td rowspan="2">T_{max1}, T_{max2}</td><td style='text-align: center; word-wrap: break-word;'>Maximum temperature of the reaction mixture (K)</td><td rowspan="2">Conv Cumulative conversion of the monomer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(subscripts 1 and 2 refer to zones 1 and 2)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_{out1}, T_{out2}</td><td style='text-align: center; word-wrap: break-word;'>Outlet temperature of the reaction mixture (K)</td><td style='text-align: center; word-wrap: break-word;'>MWN Number-average molecular weight</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_{cin1}, T_{cin2}</td><td style='text-align: center; word-wrap: break-word;'>Inlet temperature of the coolant (K) $ ^{a)} $</td><td style='text-align: center; word-wrap: break-word;'>MWW Weight-average molecular weight</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Z_{1}, Z_{2}</td><td style='text-align: center; word-wrap: break-word;'>Axial reactor length of T_{max1} and T_{max2} (% of the reactor length)</td><td style='text-align: center; word-wrap: break-word;'>LCB Long-chain branching per 1000 carbon atoms</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>F_{i1}, F_{i2}</td><td style='text-align: center; word-wrap: break-word;'>Flow rate of the initiator (g/s)</td><td style='text-align: center; word-wrap: break-word;'>SCB Short-chain branching per 1000 carbon atoms</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>F_{s1}, F_{s2}</td><td style='text-align: center; word-wrap: break-word;'>Flow rate of the solvent in the inlet feed and in the intermediate feed (% of the ethylene flow rate)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T_{in}</td><td style='text-align: center; word-wrap: break-word;'>Inlet temperature of the reaction mixture (K)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Press</td><td style='text-align: center; word-wrap: break-word;'>Reactor pressure (atom)</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

a) The outlet temperature of the coolant in two zones is fixed.

Source: Adapted from Dunn [17].

Aspen Technology’s multivariate statistical analysis software, Aspen ProMV, for this workshop. Figure 9.10 shows a schematic diagram of the two-zone reactor, and Table 9.1 defines the 14 process variables (X) and 5 product quality variables (Y).

Step 1: Start Aspen ProMV. Select new projects. See Figure 9.11.

Step 2: Load the process data file and save the project file.

Click on Add/Edit Data and Import from File, LDPE.xls. Choose Process Variables only. See Figure 9.12. Figure 9.13 displays a portion of the imported process variable data. By clicking OK twice, we see the Standard Data Specification. See

---

<!-- PDF page 578 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_152_808_551.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.11 Choose New project in Aspen ProMV.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_164_637_796_1068.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 9.12 Import process data from file LDPE.xls and choose process variable worksheet only.</div>


Figure 9.14. We then click OK and see the observation summary in Figure 9.15. Highlight the observation ID column to include all observations, and the Include observations button turns “green” to indicate that we have included all observation data. See Figure 9.16. Click OK. Save the project as WS9.1_PCA-X.pmvx. See Figure 9.17.

---

<!-- PDF page 579 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_152_774_236.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_251_777_697.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.13 A display of imported process variable data.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_766_778_1051.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.14 Specify block type for process variables, X.</div>


## Step 3: Build a PCA model for process variables X

After saving the project file, we see the New Model dialog. We click on the Blocks/Variables name, “Process Variables,” to display the 14 process variables. Both the Block name and Variable name are in green. See Figure 9.18. In the figure, “MC” and “UV” represent the preprocessing of data to make them Mean-Centered with Unit Variance Scaling, as we discuss in Appendix A, Sections A.1.5 and A.1.7 for

---

<!-- PDF page 580 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_146_647_750.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 9.15 A display of observation summary.</div>


standard data matrix. “Custom” in the figure refers to Custom Scaling, that is, the variables will be multiplied by this custom value after we have applied data centering and scaling.

We then click OK and fill in the model name, WS9.1_PCA-X.pmvx. See Figure 9.19. Select Model→Active Model→Auto Fit→See Figure 9.20. Figure 9.21 shows the resulting R2 and Q2 values, Eqs. (9.18)–(9.20), versus the number of principal components. We can right-mouse-click on this plot and select “Create Table” to see a table of R2 and Q2 values in the plot, as seen on the right of Figure 9.21.

Figure 9.21 shows the cumulative R2 and Q2 values for each model component. The R2 of the final component is the total amount of variability in the dataset that the model explains, and the Q2 value of the final component is a measure of how well the dataset is predicted by unseen data in cross-validation. If the R2 and Q2 values are low, it could mean that there is significant noise in the data, existence of significant outliers, or not enough information in the data to fit an acceptable model. The figure indicates that increasing the number of principal components, or latent variables, increases the R2 value, as explained previously in Section 9.1.4. With seven principal components, an R2 value of 0.9149 says

---

<!-- PDF page 581 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_150_617_783.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">Figure 9.16 Highlight all observations to include them in the model development.</div>


that the PCA model can explain 91.49% of the variability of the dataset for process variables (X). Likewise, with cross-validation, a Q2 value of 0.8406 says the model can explain 84.07% of the variability of the dataset for process variables.

Step 4: Generating PCA plots and their interpretations.

We follow the Aspen ProMV online help section on Interpreting Plots to demonstrate some useful plots and their interpretations.

(1) Model summary (R2 and Q2) plots for a selected maximum number of principal components

Choose the # button in the middle of the top of the screen and fill in a maximum number of four principal components, we get a R2-Q2 plot of Figure 9.22.

(2) Variable summary plot

We follow the path: Analyze → Model → Variable summary → Block: Choose X-space and Component: Choose 7, and see Figure 9.23. We also right-mouse-click on this figure and select “Create Table” to see a table of R2 and Q2 values in the figure, as seen on the right of Figure 9.23. This figure

---

<!-- PDF page 582 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_159_745_482.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 9.17 Saving the Aspen ProMV project file as WS9.1_PCA-X.pmvx.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_168_574_808_1168.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.18 Process variables (X) for developing a PCA model on X.</div>


---

<!-- PDF page 583 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_161_778_451.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.19 Filling in model name, WS9.1_PCA-X.pmvx.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_135_547_618_834.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 9.20 Auto-fitting the PCA model with the number of principal components (A) equal to half of the number of process variables (N = 14), A = 14/2 = 7.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>T1-T2</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>P1-P2</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>P1 Bar</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>Hef's T2</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>SPE'K</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>VP</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>ObsV'Pred</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>T1-U1</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>W*<sub>i</sub>ct Bar Coeffs</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>W*<sub>i</sub>ct W*<sub>i</sub>c2</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[8]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[9]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[10]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[11]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[12]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[13]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[14]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[15]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[16]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[17]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[18]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[19]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[20]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[21]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[22]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[23]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[24]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[25]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[26]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[27]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[28]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[29]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[30]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[31]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[32]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[33]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[34]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[35]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[36]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[37]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[38]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[39]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[40]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[41]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[42]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[43]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[44]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[45]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[46]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[47]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[48]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[49]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[50]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[51]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[52]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[53]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[54]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[55]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[56]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[57]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[58]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[59]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[60]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[61]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[62]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[63]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[64]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[65]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[66]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[67]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[68]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[69]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[70]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[71]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[72]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[73]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[74]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[75]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[76]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[77]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[78]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[79]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[80]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[81]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[82]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[83]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[84]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[85]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[86]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[87]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[88]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[89]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[90]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[91]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[92]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[93]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[94]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[95]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[96]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[97]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[98]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[99]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[100]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[101]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[102]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[103]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[104]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[105]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[106]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[107]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[108]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[109]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[110]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[111]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[112]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[113]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[114]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[115]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[116]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[117]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[118]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[119]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[120]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[121]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[122]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[123]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[124]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[125]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[126]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[127]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[128]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[129]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[130]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[131]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[132]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[133]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[134]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[135]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[136]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[137]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[138]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[139]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[140]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[141]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[142]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[143]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[144]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[145]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[146]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[147]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[148]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[149]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[150]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'></td><td style='text-align: center;'>[151]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.21 R2 and Q2 values versus the number of principal components.</div>


---

<!-- PDF page 584 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.19</td></tr>
    <tr><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.58</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.22 R2–Q2 plot with a maximum number of four principal components.</div>


Model Analyze Monitor Window Help

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Variable</th><th style='text-align: center;'>Model 1 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 1 - Table</th><th style='text-align: center;'>Model 2 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 2 - Table</th><th style='text-align: center;'>Model 3 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 3 - Table</th><th style='text-align: center;'>Model 4 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 4 - Table</th><th style='text-align: center;'>Model 5 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 5 - Table</th><th style='text-align: center;'>Model 6 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 6 - Table</th><th style='text-align: center;'>Model 7 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 7 - Table</th><th style='text-align: center;'>Model 8 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 8 - Table</th><th style='text-align: center;'>Model 9 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 9 - Table</th><th style='text-align: center;'>Model 10 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 10 - Table</th><th style='text-align: center;'>Model 11 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 11 - Table</th><th style='text-align: center;'>Model 12 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 12 - Table</th><th style='text-align: center;'>Model 13 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 13 - Table</th><th style='text-align: center;'>Model 14 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 14 - Table</th><th style='text-align: center;'>Model 15 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 15 - Table</th><th style='text-align: center;'>Model 16 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 16 - Table</th><th style='text-align: center;'>Model 17 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 17 - Table</th><th style='text-align: center;'>Model 18 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 18 - Table</th><th style='text-align: center;'>Model 19 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 19 - Table</th><th style='text-align: center;'>Model 20 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 20 - Table</th><th style='text-align: center;'>Model 21 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 21 - Table</th><th style='text-align: center;'>Model 22 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 22 - Table</th><th style='text-align: center;'>Model 23 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 23 - Table</th><th style='text-align: center;'>Model 24 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 24 - Table</th><th style='text-align: center;'>Model 25 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 25 - Table</th><th style='text-align: center;'>Model 26 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 26 - Table</th><th style='text-align: center;'>Model 27 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 27 - Table</th><th style='text-align: center;'>Model 28 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 28 - Table</th><th style='text-align: center;'>Model 29 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 29 - Table</th><th style='text-align: center;'>Model 30 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 30 - Table</th><th style='text-align: center;'>Model 31 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 31 - Table</th><th style='text-align: center;'>Model 32 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 32 - Table</th><th style='text-align: center;'>Model 33 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 33 - Table</th><th style='text-align: center;'>Model 34 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 34 - Table</th><th style='text-align: center;'>Model 35 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 35 - Table</th><th style='text-align: center;'>Model 36 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 36 - Table</th><th style='text-align: center;'>Model 37 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 37 - Table</th><th style='text-align: center;'>Model 38 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 38 - Table</th><th style='text-align: center;'>Model 39 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 39 - Table</th><th style='text-align: center;'>Model 40 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 40 - Table</th><th style='text-align: center;'>Model 41 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 41 - Table</th><th style='text-align: center;'>Model 42 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 42 - Table</th><th style='text-align: center;'>Model 43 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 43 - Table</th><th style='text-align: center;'>Model 44 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 44 - Table</th><th style='text-align: center;'>Model 45 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 45 - Table</th><th style='text-align: center;'>Model 46 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 46 - Table</th><th style='text-align: center;'>Model 47 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 47 - Table</th><th style='text-align: center;'>Model 48 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 48 - Table</th><th style='text-align: center;'>Model 49 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 49 - Table</th><th style='text-align: center;'>Model 50 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 50 - Table</th><th style='text-align: center;'>Model 51 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 51 - Table</th><th style='text-align: center;'>Model 52 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 52 - Table</th><th style='text-align: center;'>Model 53 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 53 - Table</th><th style='text-align: center;'>Model 54 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 54 - Table</th><th style='text-align: center;'>Model 55 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 55 - Table</th><th style='text-align: center;'>Model 56 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 56 - Table</th><th style='text-align: center;'>Model 57 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 57 - Table</th><th style='text-align: center;'>Model 58 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 58 - Table</th><th style='text-align: center;'>Model 59 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 59 - Table</th><th style='text-align: center;'>Model 60 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 60 - Table</th><th style='text-align: center;'>Model 61 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 61 - Table</th><th style='text-align: center;'>Model 62 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 62 - Table</th><th style='text-align: center;'>Model 63 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 63 - Table</th><th style='text-align: center;'>Model 64 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 64 - Table</th><th style='text-align: center;'>Model 65 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 65 - Table</th><th style='text-align: center;'>Model 66 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 66 - Table</th><th style='text-align: center;'>Model 67 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 67 - Table</th><th style='text-align: center;'>Model 68 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 68 - Table</th><th style='text-align: center;'>Model 69 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 69 - Table</th><th style='text-align: center;'>Model 70 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 70 - Table</th><th style='text-align: center;'>Model 71 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 71 - Table</th><th style='text-align: center;'>Model 72 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 72 - Table</th><th style='text-align: center;'>Model 73 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 73 - Table</th><th style='text-align: center;'>Model 74 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 74 - Table</th><th style='text-align: center;'>Model 75 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 75 - Table</th><th style='text-align: center;'>Model 76 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 76 - Table</th><th style='text-align: center;'>Model 77 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 77 - Table</th><th style='text-align: center;'>Model 78 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 78 - Table</th><th style='text-align: center;'>Model 79 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 79 - Table</th><th style='text-align: center;'>Model 80 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 80 - Table</th><th style='text-align: center;'>Model 81 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 81 - Table</th><th style='text-align: center;'>Model 82 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 82 - Table</th><th style='text-align: center;'>Model 83 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 83 - Table</th><th style='text-align: center;'>Model 84 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 84 - Table</th><th style='text-align: center;'>Model 85 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 85 - Table</th><th style='text-align: center;'>Model 86 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 86 - Table</th><th style='text-align: center;'>Model 87 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 87 - Table</th><th style='text-align: center;'>Model 88 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 88 - Table</th><th style='text-align: center;'>Model 89 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 89 - Table</th><th style='text-align: center;'>Model 90 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 90 - Table</th><th style='text-align: center;'>Model 91 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 91 - Table</th><th style='text-align: center;'>Model 92 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 92 - Table</th><th style='text-align: center;'>Model 93 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 93 - Table</th><th style='text-align: center;'>Model 94 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 94 - Table</th><th style='text-align: center;'>Model 95 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 95 - Table</th><th style='text-align: center;'>Model 96 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 96 - Table</th><th style='text-align: center;'>Model 97 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 97 - Table</th><th style='text-align: center;'>Model 98 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 98 - Table</th><th style='text-align: center;'>Model 99 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 99 - Table</th><th style='text-align: center;'>Model 100 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 100 - Table</th><th style='text-align: center;'>Model 101 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 101 - Table</th><th style='text-align: center;'>Model 102 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 102 - Table</th><th style='text-align: center;'>Model 103 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 103 - Table</th><th style='text-align: center;'>Model 104 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 104 - Table</th><th style='text-align: center;'>Model 105 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 105 - Table</th><th style='text-align: center;'>Model 106 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 106 - Table</th><th style='text-align: center;'>Model 107 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 107 - Table</th><th style='text-align: center;'>Model 108 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 108 - Table</th><th style='text-align: center;'>Model 109 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 109 - Table</th><th style='text-align: center;'>Model 110 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 110 - Table</th><th style='text-align: center;'>Model 111 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 111 - Table</th><th style='text-align: center;'>Model 112 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 112 - Table</th><th style='text-align: center;'>Model 113 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 113 - Table</th><th style='text-align: center;'>Model 114 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 114 - Table</th><th style='text-align: center;'>Model 115 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 115 - Table</th><th style='text-align: center;'>Model 116 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 116 - Table</th><th style='text-align: center;'>Model 117 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 117 - Table</th><th style='text-align: center;'>Model 118 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 118 - Table</th><th style='text-align: center;'>Model 119 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 119 - Table</th><th style='text-align: center;'>Model 120 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 120 - Table</th><th style='text-align: center;'>Model 121 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 121 - Table</th><th style='text-align: center;'>Model 122 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 122 - Table</th><th style='text-align: center;'>Model 123 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 123 - Table</th><th style='text-align: center;'>Model 124 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 124 - Table</th><th style='text-align: center;'>Model 125 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 125 - Table</th><th style='text-align: center;'>Model 126 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 126 - Table</th><th style='text-align: center;'>Model 127 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 127 - Table</th><th style='text-align: center;'>Model 128 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 128 - Table</th><th style='text-align: center;'>Model 129 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 129 - Table</th><th style='text-align: center;'>Model 130 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 130 - Table</th><th style='text-align: center;'>Model 131 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 131 - Table</th><th style='text-align: center;'>Model 132 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 132 - Table</th><th style='text-align: center;'>Model 133 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 133 - Table</th><th style='text-align: center;'>Model 134 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 134 - Table</th><th style='text-align: center;'>Model 135 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 135 - Table</th><th style='text-align: center;'>Model 136 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 136 - Table</th><th style='text-align: center;'>Model 137 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 137 - Table</th><th style='text-align: center;'>Model 138 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 138 - Table</th><th style='text-align: center;'>Model 139 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 139 - Table</th><th style='text-align: center;'>Model 140 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 140 - Table</th><th style='text-align: center;'>Model 141 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 141 - Table</th><th style='text-align: center;'>Model 142 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 142 - Table</th><th style='text-align: center;'>Model 143 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 143 - Table</th><th style='text-align: center;'>Model 144 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 144 - Table</th><th style='text-align: center;'>Model 145 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 145 - Table</th><th style='text-align: center;'>Model 146 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 146 - Table</th><th style='text-align: center;'>Model 147 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 147 - Table</th><th style='text-align: center;'>Model 148 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 148 - Table</th><th style='text-align: center;'>Model 149 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 149 - Table</th><th style='text-align: center;'>Model 150 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 150 - Table</th><th style='text-align: center;'>Model 151 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 151 - Table</th><th style='text-align: center;'>Model 152 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 152 - Table</th><th style='text-align: center;'>Model 153 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 153 - Table</th><th style='text-align: center;'>Model 154 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 154 - Table</th><th style='text-align: center;'>Model 155 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 155 - Table</th><th style='text-align: center;'>Model 156 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 156 - Table</th><th style='text-align: center;'>Model 157 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 157 - Table</th><th style='text-align: center;'>Model 158 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 158 - Table</th><th style='text-align: center;'>Model 159 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 159 - Table</th><th style='text-align: center;'>Model 160 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 160 - Table</th><th style='text-align: center;'>Model 161 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 161 - Table</th><th style='text-align: center;'>Model 162 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 162 - Table</th><th style='text-align: center;'>Model 163 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 163 - Table</th><th style='text-align: center;'>Model 164 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 164 - Table</th><th style='text-align: center;'>Model 165 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 165 - Table</th><th style='text-align: center;'>Model 166 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 166 - Table</th><th style='text-align: center;'>Model 167 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 167 - Table</th><th style='text-align: center;'>Model 168 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 168 - Table</th><th style='text-align: center;'>Model 169 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 169 - Table</th><th style='text-align: center;'>Model 170 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 170 - Table</th><th style='text-align: center;'>Model 171 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 171 - Table</th><th style='text-align: center;'>Model 172 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 172 - Table</th><th style='text-align: center;'>Model 173 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 173 - Table</th><th style='text-align: center;'>Model 174 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 174 - Table</th><th style='text-align: center;'>Model 175 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 175 - Table</th><th style='text-align: center;'>Model 176 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 176 - Table</th><th style='text-align: center;'>Model 177 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 177 - Table</th><th style='text-align: center;'>Model 178 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 178 - Table</th><th style='text-align: center;'>Model 179 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 179 - Table</th><th style='text-align: center;'>Model 180 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 180 - Table</th><th style='text-align: center;'>Model 181 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 181 - Table</th><th style='text-align: center;'>Model 182 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 182 - Table</th><th style='text-align: center;'>Model 183 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 183 - Table</th><th style='text-align: center;'>Model 184 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 184 - Table</th><th style='text-align: center;'>Model 185 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 185 - Table</th><th style='text-align: center;'>Model 186 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 186 - Table</th><th style='text-align: center;'>Model 187 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 187 - Table</th><th style='text-align: center;'>Model 188 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 188 - Table</th><th style='text-align: center;'>Model 189 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 189 - Table</th><th style='text-align: center;'>Model 190 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 190 - Table</th><th style='text-align: center;'>Model 191 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 191 - Table</th><th style='text-align: center;'>Model 192 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 192 - Table</th><th style='text-align: center;'>Model 193 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 193 - Table</th><th style='text-align: center;'>Model 194 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 194 - Table</th><th style='text-align: center;'>Model 195 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 195 - Table</th><th style='text-align: center;'>Model 196 - Model Variable Summary for X-Space</th><th style='text-align: center;'>Model 19</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.23 Variable summary plot in the X-space in a PCA model.</div>


shows the total R2 and Q2 of each X variable in a PCA model. As explained previously with Figure 9.21, if there are many variables and a few variables are not predicted well, this may mean there is no information in the dataset that can well explain these variables, not enough variation in the variables, too much noise, or significant outliers.

---

<!-- PDF page 585 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_486_152_617_183.jpg" alt="Image" width="13%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.51</td><td style='text-align: center;'>0.44</td></tr>
    <tr><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.74</td><td style='text-align: center;'>0.73</td></tr>
    <tr><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.77</td></tr>
    <tr><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.86</td><td style='text-align: center;'>0.79</td></tr>
    <tr><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.87</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.84</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.24 R2 and Q2 values for all components for a specific X or Y variable.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Training Method</th><th style='text-align: center;'>Training Time (s)</th><th style='text-align: center;'>Training Time (s)</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.25 T[2] versus T[1] score plot and P[2] versus P[1] loading plot.</div>


(3) “Components by variable” plot

We show Figure 9.24 by following the path: Analyze → Model → Components by variable → Block: choose process variables, and Variable: choose Tin (displayed in Figure 9.10, inlet temperature of the reaction mixture). This figure shows the R2 and Q2 values for all of the components for a specific X or Y variable. In this case, it is the X variable, inlet temperature, Tin.

(4) T1–T2 score plot and P1–P2 loading plot

We discussed in Section 9.1.4 the score matrix T and the loading matrix P. In Appendix A, Section B.4, we demonstrate the use of ML to generate these matrices. By choosing T1–T2 and P1–P2 buttons on the left side pane, we generate the score plot and loading plot of Figure 9.25. These figures plot the score

---

<!-- PDF page 586 -->

and loading values of the second principal component, T[2] and P[2], versus those of the first principal component, T[1] and P[1].

The scores are the latent variables, which are the weighted averages of the original process variables, X's. The score plot enables us to find clusters (such as in the middle of the left score plot in Figure 9.25) and outliers (such as observation 54). On the score plot, the inner dashed ellipse represents 95% confidence limit, while the outer solid ellipse represents 99% confidence limit. Observations that fall outside the 95% or 99% confidence intervals may be outliers; however, 5% and 1% of the observations are expected to naturally fall outside of the 95% and 99% confidence intervals, respectively. This plot shows the scores for a PCA model where there is both data clustering and a possible outlier.

The loadings are the model variables that explain the relationship between the X variables in PCA (or X and Y variables in the case of PLS, discussed in Sections 9.3 and 9.4) and the latent variables (scores). In the right loading plot of Figure 9.25, variables that are close to the center of the plot are not significant for explaining the variation in the plotted components. By contrast, variables that are far from the center are important for explaining the variation in the dataset. Variables that are close together on the loading plot are correlated, and variables that lie on the opposite sides of the plot are negatively correlated.

## (5) Hotelling's  $ T^{2} $ plot

Select the Hot’s T2 button on the left-side pane. We see the Hotelling’s  $ T^{2} $ plot in Figure 9.26. This plot measures the deviation of an observation from the

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>HT2 [1-7]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>7</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>8</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>9</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>10</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>11</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>12</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>13</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>14</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>15</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>16</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>17</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>18</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>19</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>21</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>22</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>23</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>24</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>26</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>27</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>28</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>29</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>31</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>32</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>33</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>34</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>35</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>36</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>37</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>38</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>39</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>40</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>41</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>42</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>43</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>44</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>45</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>46</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>47</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>48</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>49</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>51</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>52</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>53</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>54</td><td style='text-align: center;'>19.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.26 The Hotelling's  $ T^{2} $ plot.</div>


---

<!-- PDF page 587 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>SQuared Prediction Error (S.Q. Space - S.Q. Space_1_PCA-X) [comp.]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>3.8</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>16.0</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>40.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>42.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>45.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>54.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>55.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>57.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>58.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>60.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>65.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>68.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>70.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>72.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>75.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>78.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>80.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>82.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>85.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>88.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>90.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>92.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>98.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>102.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>105.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>108.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>110.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>112.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>115.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>118.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>120.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>122.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>125.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>128.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>130.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>132.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>135.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>138.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>140.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>142.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>145.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>148.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>150.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>152.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>155.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>158.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>160.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>162.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>165.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>168.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>170.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>172.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>175.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>178.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>180.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>182.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>185.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>188.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>190.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>192.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>195.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>198.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>200.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>202.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>205.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>208.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>210.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>212.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>215.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>218.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>220.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>222.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>225.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>228.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>230.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>232.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>235.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>238.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>240.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>242.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>245.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>248.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>250.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>252.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>255.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>258.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>260.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>262.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>265.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>268.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>270.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>272.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>275.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>278.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>280.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>282.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>285.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>288.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>290.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>292.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>295.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>298.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>300.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>302.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>305.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>308.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>310.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>312.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>315.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>318.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>320.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>322.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>325.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>328.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>330.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>332.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>335.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>338.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>340.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>342.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>345.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>348.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>350.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>352.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>355.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>358.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>360.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>362.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>365.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>368.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>370.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>372.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>375.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>378.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>380.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>382.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>385.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>388.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>390.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>392.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>395.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>398.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>400.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>402.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>405.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>408.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>410.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>412.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>415.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>418.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>420.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>422.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>425.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>428.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>430.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>432.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>435.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>438.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>440.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>442.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>445.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>448.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>450.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>452.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>455.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>458.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>460.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>462.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>465.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>468.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>470.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>472.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>475.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>478.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>480.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>482.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>485.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>488.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>490.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>492.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>495.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>498.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>500.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>502.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>505.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>508.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>510.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>512.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>515.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>518.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>520.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>522.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>525.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>528.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>530.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>532.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>535.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>538.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>540.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>542.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>545.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>548.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>550.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>552.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>555.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>558.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>560.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>562.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>565.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>568.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>570.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>572.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>575.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>578.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>580.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>582.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>585.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>588.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>590.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>592.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>595.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>598.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>600.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>602.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>605.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>608.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>610.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>612.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>615.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>618.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>620.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>622.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>625.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>628.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>630.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>632.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>635.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>638.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>640.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>642.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>645.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>648.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>650.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>652.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>655.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>658.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>660.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>662.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>665.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>668.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>670.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>672.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>675.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>678.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>680.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>682.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>685.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>688.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>690.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>692.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>695.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>698.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>700.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>702.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>705.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>708.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>710.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>712.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>715.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>718.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>720.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>722.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>725.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>728.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>730.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>732.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>735.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>738.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>740.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>7</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.27 The SPE-X plot.</div>


origin, that is, from the average operating point. Note the two horizontal lines labeled 0.99 and 0.95 for 99% and 95% confidence limits, respectively. We see observation #54 lying above the 95% confidence limit. This is acceptable, as there are generally on average 5 out 100 observations lying outside the 95% confidence limit.

(6) Row residual or squared prediction error SPE-X plot

We discussed the SPE in Eqs. (9.15) and (9.16) and in Figure 9.7. Choosing SPE-X button on the left-side pane gives the SPE-X plot of Figure 9.27. In the plot, we see that observation 54 has the largest SPE value.

(7) Variable importance to projection (VIP) plot

Choosing the VIP button on the left-side pane gives the VIP plot of Figure 9.28. The VIP plot gives a quantitative metric of the relative importance of a variable to a PCA model. A rule of thumb is that variables with a VIP value close to or greater than 1 are important. Referring to Figure 9.10 and Table 9.1 for the definitions of process variables, we see that  $ T_{out1} $,  $ T_{max2} $,  $ T_{cin1} $, and  $ T_{cin2} $ are the four most important process variables in the PCA model.

## (8) Contribution plots

When a single observation is selected on a score plot or Hotelling's T² plot, the contribution plot shows the difference between that observation and the average observation. Following the path: Analyze → Contributions → This opens the contribution plot window. In this window, we specify analysis between our apparent outlier, observation 54, and the average observation using the specifications shown in Figure 9.29, left. These inputs yield the contribution plot on the right side of Figure 9.29. We see that z2 (the axial reactor length at the maximum temperature of the reaction mixture in zone 2,

---

<!-- PDF page 588 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Variable</th><th style='text-align: center;'>Model 1 - Variable Importance Plot for X-Space</th><th style='text-align: center;'>Model 1 - Variable Importance Plot for X-Space - W59_1_PCA-X</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>T1-T2</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>P1-P2</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>P1 Bar</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>Hot's T2</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>SPE-X</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>VIP</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>ObsVsPred</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>T1-U1</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>W",c1-W",c2</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.05</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.28 Variable importance plot.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_166_618_520_857.jpg" alt="Image" width="36%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Variable</th><th style='text-align: center;'>Controls: Weights=wT1 to wT7</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Tin</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>Tmem1</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>Tthat1</td><td style='text-align: center;'>-4.5</td></tr>
    <tr><td style='text-align: center;'>Tmem2</td><td style='text-align: center;'>-4.5</td></tr>
    <tr><td style='text-align: center;'>Tos2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>Tcin1</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>Tos2</td><td style='text-align: center;'>0.6</td></tr>
    <tr><td style='text-align: center;'>Z1</td><td style='text-align: center;'>0.3</td></tr>
    <tr><td style='text-align: center;'>Z2</td><td style='text-align: center;'>8.3</td></tr>
    <tr><td style='text-align: center;'>F1</td><td style='text-align: center;'>-0.1</td></tr>
    <tr><td style='text-align: center;'>F2</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>F31</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>F62</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>Prtss</td><td style='text-align: center;'>-0.2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.29 Point-to-average contribution point.</div>


Tmax2, Figure 9.10) is higher than the average, and Tmax2 is lower than the average.

This concludes workshop WS9.1_PCA-X, and we save the file as WS9.1_PCA-X.pmvx.

### 9.3 Partial Least Squares or Projection to Latent Structures (PLS)

#### 9.3.1 Introduction to PLS

When applying data analytics to chemical processes, we often deal with not only process variables and their measurements but also focus on quality or productivity

---

<!-- PDF page 589 -->

variables. Let  $ \mathbf{X} $ be a  $ J \times K $ process variable matrix with  $ K $ columns of process variables ( $ k = 1 $ to  $ K $), and  $ J $ rows of measurements per variable ( $ j = 1 $ to  $ K $), and  $ \mathbf{Y} $ be a  $ J \times M $ process quality variable matrix with  $ M $ columns of quality variables ( $ m = 1 $ to  $ M $), and  $ J $ rows of measurements per variable ( $ j = 1 $ to  $ J $).

As discussed in Section 9.1.1, PCA rotates the process data such that the principal axis of the data represents the direction of maximum variation. The projection of the data in the new coordinate system of A principal components is called the principal components or latent variable scores, which are represented by a J×A score matrix T, where J represents the rows of measurements per variable, and A denotes the number of principal components. Additionally, the principal components are vectors in the original variable space, and we call these vectors principal component or latent variable loadings, which are represented by a (K×A) principal loading matrix P, where K represents the number of process variables, and A is the number of principal components.

Since PCA only uses X-data to find the principal component scores, T, these components explain variation in X-data and not necessarily the most predictive of Y-data. In this section, we wish to use both X-data and Y-data simultaneously to identify the latent variables that explain the variation in X and are predictive of Y.

In Figure 9.30, we decompose the standardized  $ J \times K $ process variable matrix  $ \mathbf{X} $ and  $ J \times M $ product quality matrix  $ \mathbf{Y} $ into their principal component loading vectors  $ (\mathbf{p}_a $ and  $ \mathbf{c}_a $,  $ a = 1, 2, \ldots, A) $, and principal component score vectors  $ (\mathbf{t}_a $ and  $ \mathbf{u}_a $;  $ a = 1, 2, \ldots, A) $. Alternatively, we can express the entire process variable matrix  $ \mathbf{X} $ in terms of a principal component loading matrix  $ \mathbf{P} $, a principal component score matrix  $ \mathbf{T} $, and a prediction error or residual matrix  $ \mathbf{E} $, as seen previously in Eq. (9.17). Likewise,

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_773_696_1159.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 9.30 An illustration of partial least squares (PLS) regression of both process variable matrix X and product quality matrix Y, their principal component loading matrices P and C, and score matrices T and U, together with the weight matrix W for relating the score matrix T with process variable matrix X. Source: Dunn [13].</div>


---

<!-- PDF page 590 -->

we represent the entire product quality matrix Y in terms of a principal component loading matrix C, a principal component score matrix U, and a prediction error or residual error matrix F. See Eq. (9.23).

 $$ \begin{aligned}\mathbf{X}&=\mathbf{T}\mathbf{P}^{\prime}+\mathbf{E}=\widehat{\mathbf{X}}+\mathbf{E}\ $ J\times K)&=(J\times A)(A\times K)\end{aligned} $$ 

 $$ \begin{aligned}\mathbf{Y}&=\mathbf{U}\mathbf{C}^{\prime}+\mathbf{F}=\widehat{\mathbf{Y}}+\mathbf{F}\ $ J\times M)&=(J\times A)(A\times M)\end{aligned} $$ 

We can estimate the X-scores (i.e. principal component score vectors  $ \mathbf{t}_{a}' $s or principal component score matrix  $ \mathbf{T} $) as linear combinations of the original process variable vectors  $ \mathbf{x}_{\mathbf{k}} $ ( $ k=1,2\ldots,K $) with the coefficients, “weights,”  $ \mathbf{w} $

 $$ \mathbf{t}_{ja}=\Sigma x_{jk}\mathbf{w}_{ka}\quad\text{or}\quad\mathbf{T}=\mathbf{X}\mathbf{W} $$ 

#### 9.3.2 Nonlinear Iterative Partial Least Squares (NIPALS) Algorithm

We follow [13, 18, 19] to show how to compute the principal components sequentially and to handle missing data, with reference to the steps involved in Figure 9.31 [13].

Step 1: See the number or the numbered arrow direction in Figure 9.31 for the numbered step. Begin with the  $ J \times K $ process variable matrix  $ \mathbf{X} $ and  $ J \times M $ process quality matrix  $ \mathbf{Y} $.  $ \mathbf{X}_a $ and  $ \mathbf{Y}_a $ are both preprocessed versions of the raw data when the number of principal components (a) equals 1. Select a column  $ \mathbf{y}_a $ within the quality matrix  $ \mathbf{Y} $ as our initial estimate for a score vector  $ \mathbf{u}_a $. Regress a data column  $ \mathbf{X}_a $ within data matrix  $ \mathbf{X} $ onto a score vector  $ \mathbf{u}_a $ within score matrix  $ \mathbf{U} $. Store

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_870_754_1199.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 9.31 An illustration of the steps involved in computing the principal components by the NIPALS algorithm. Source: Dunn [13].</div>


---

<!-- PDF page 591 -->

the regressed slope coefficients in the weight vector  $ \mathbf{w}_a $. Large weight coefficients reflect that columns in  $ \mathbf{X}_a $ are strongly correlated with  $ \mathbf{u}_a $. We do this regression as follows:

 $$ \mathbf{w}_{a}=\left(1/\mathbf{u}_{a}^{\prime}\mathbf{u}_{a}\right)\mathbf{X}_{a}^{\prime}\mathbf{u}_{a} $$ 

Step 2: Normalize the weight vector to unit length.

 $$ \mathbf{w}_{a}=\mathbf{w}_{a}/\left(\mathbf{w}_{a}^{\prime}\mathbf{w}_{a}\right)^{1/2} $$ 

Step 3: Regress every row in  $ X_{a} $ onto the weight vector  $ w_{a} $. Store the regressed slope coefficients in the score vector  $ t_{a} $. Repeat doing this for all J rows of observations:

 $$ \mathbf{t}_{a}=\left(1/\mathbf{w}_{a}^{\prime}\mathbf{w}_{a}\right)\mathbf{X}_{a}^{\prime}\mathbf{w}_{a} $$ 

Step 4: Regress every column in  $ Y_a $ onto the vector  $ t_a $. Store the regressed slope coefficient in the loading vector  $ c_a $. Repeat doing this for all  $ M $ columns of quality variables:

 $$ \mathbf{c}_{a}=\left(1/\mathbf{c}_{a}^{^{\prime}}\mathbf{c}_{a}\right)\mathbf{Y_{a}^{^{\prime}}}\mathbf{c}_{a} $$ 

Step 5: Regress each of the J rows in quality matrix  $ \mathbf{Y}_{a} $ onto the weight vector  $ \mathbf{c}_{a} $. Large weight coefficients indicate rows in  $ \mathbf{Y}_{a} $ are strongly correlated with  $ \mathbf{c}_{a} $.

 $$ \mathbf{u}_{a}=\left(1/\mathbf{c}_{a}^{^{\prime}}\mathbf{c}_{a}\right)\mathbf{Y_{a}^{^{\prime}}}\mathbf{c}_{a} $$ 

The NIPLAS algorithm then continues with a procedure called “deflation” to remove variability already explained in  $ X_{a} $ and  $ Y_{a} $. This involves two steps.

##### 9.3.2.1 Deflation Step 1: Calculate a Loading Vector for the X Space

We calculate a loading vector  $ \mathbf{p}_{a} $ using the X-space scores, following Eqs. (9.7)–(9.8):

 $$ \mathbf{p}_{a}=\left(1/\mathbf{t}_{a}^{\prime}\mathbf{t}_{a}\right)\mathbf{X}_{a}^{\prime}\mathbf{t}_{a} $$ 

Here, the score vector  $ \mathbf{t}_{a} $ is normalized. This loading vector  $ \mathbf{p}_{a} $ contains the regression slope of every column in  $ \mathbf{X}_{a} $ onto the score vector  $ \mathbf{t}_{a} $. In this regression, the score vector  $ \mathbf{t}_{a} $ is the x-variable, and the column from  $ \mathbf{X}_{a} $ is the y-variable.

##### 9.3.2.2 Deflation Step 2: Remove the Predicted Variability from X and Y

Using the score vector  $ \mathbf{t}_a $ and the loading vector  $ \mathbf{p}_a $, we follow Eq. (9.19) to calculate the predicted value of  $ \mathbf{X}_a $, denoted by  $ \hat{\mathbf{X}}_a $:

 $$ \hat{\mathbf{X}}_{a}=\mathbf{t}_{a}\mathbf{p}_{a}^{\prime} $$ 

We then remove this best prediction  $ \hat{X}_{a} $ from the  $ \mathbf{X}_{a} $, that is, we remove the variability already explained well from the original data matrix  $ \mathbf{X}_{a} $:

 $$ \mathbf{E}_{a}=\mathbf{X}_{a}-\hat{\mathbf{X}}_{a}=\mathbf{X}_{a}-\mathbf{t}_{a}\mathbf{p}_{a}^{\prime} $$ 

We define the remaining data matrix as  $ \mathbf{X}_{a+1} $:

 $$ \mathbf{X}_{a+1}=\mathbf{E}_{a} $$ 

---

<!-- PDF page 592 -->

In the same way, we remove the variability from the quality data matrix Y, using the score vector  $ \mathbf{t}_{a} $ and the leading vector  $ \mathbf{c}_{a} $.

 $$ \hat{\mathbf{Y}}_{a}=\mathbf{t}_{a}\mathbf{c}_{a}^{\prime} $$ 

 $$ \mathbf{F}_{a}=\mathbf{Y}_{a}-\hat{\mathbf{Y}}_{a}=\mathbf{Y}_{a}-\mathbf{t}_{a}\mathbf{c}_{a}^{\prime} $$ 

 $$ \mathbf{Y}_{a+1}=\mathbf{F}_{a} $$ 

The NIPALS algorithm repeats all over again, using the deflated matrices for the subsequent iterations.

In Appendix B of this book, code B.5 and Table B.1 at the end give the Python implementation of the PLS algorithm, together with a list of common parameters and their suggested values.

### 9.4 Hands-on Workshops of PLS of LDPE and HDPE Processes

##### 9.4.1 Workshop 9.2: PLS of Process and Quality Variables Affecting the Quality and Conversion of LDPE Product from a Two-Zone Tubular Reactor

The procedure to carry out this workshop is similar to WS9.1_PCA-X in Section 9.2. We only highlight the changes to the previous workshop when considering both X and Y spaces (i.e. process and quality variables).

We follow Figure 9.11 to start a new project and follow Figure 9.12 to import data from file, LDPE.xls, but to choose to import both process variables and product quality variables. We change Figure 9.14 to Figure 9.32.

After importing the data file, LDPE.xls, we note that the original Ref. [17] for the LPDE data indicates that some observations, such as observation IDs from 51 to 54, reflect a gradual increasing level of impurities in the feed ethylene to both zones of the tubular reactor, and they progressively move outside the acceptable

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_973_743_1221.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 9.32 Specify block types for process variables, X, and product quality variables, Y.</div>


---

<!-- PDF page 593 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_148_783_446.jpg" alt="Image" width="67%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Mean</th><th style='text-align: center;'>Error Bar Lower Bound</th><th style='text-align: center;'>Error Bar Upper Bound</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2012-06-29 15:56</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>300.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 22:37</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 29:17</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 26:17</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 23:17</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 20:17</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 17:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 14:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 11:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 08:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 05:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 02:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 00:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 07:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 04:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td><td style='text-align: center;'>298.000</td></tr>
    <tr><td style='text-align: center;'>2012-06-29 01:07</td><td style='text-align: center;'>296.394</td><td style='text-align: center;'>295.000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.33 A display of observed values for process variable 3.</div>


<div style="text-align: center;">Figure 9.34 Delete observations 51–54.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_366_539_798_1097.jpg" alt="Image" width="44%" /></div>


region. Additionally, the values for observation IDs from 51 to 54 do not change for most of the 15 process variables. See Figure 9.33, in which the data plot on the right results from our highlighting process variable 3 on the left. Next, we see an observation summary in Figure 9.34 (similar to Figure 9.15), in which we delete observations 51–54.

---

<!-- PDF page 594 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Model 1 - Model Component Summary for Y-Space</th><th style='text-align: center;'>Model 1 - Table</th><th style='text-align: center;'>Model 2 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 2 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 3 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 4 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 5 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 6 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 7 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 8 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 9 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 10 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 11 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 12 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 13 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 14 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 15 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 16 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 17 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 18 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 19 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 20 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 21 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 22 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 23 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 24 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 25 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 26 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 27 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 28 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 29 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 30 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 31 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 32 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 33 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 34 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 35 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 36 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 37 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 38 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 39 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 40 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 41 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 42 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 43 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 44 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 45 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 46 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 47 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 48 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 49 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 50 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 51 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 52 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 53 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 54 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 55 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 56 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 57 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 58 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 59 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 60 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 61 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 62 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 63 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 64 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 65 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 66 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 67 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 68 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 69 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 70 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 71 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 72 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 73 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 74 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 75 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 76 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 77 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 78 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 79 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 80 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 81 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 82 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 83 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 84 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 85 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 86 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 87 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 88 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 89 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 90 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 91 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 92 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 93 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 94 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 95 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 96 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 97 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 98 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 99 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 100 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 101 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 102 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 103 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 104 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 105 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 106 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 107 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 108 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 109 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 110 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 111 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 112 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 113 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 114 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 115 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 116 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 117 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 118 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 119 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 120 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 121 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 122 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 123 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 124 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 125 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 126 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 127 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 128 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 129 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 130 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 131 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 132 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 133 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 134 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 135 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 136 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 137 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 138 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 139 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 140 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 141 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 142 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 143 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 144 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 145 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 146 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 147 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 148 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 149 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 150 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 151 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 152 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 153 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 154 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 155 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 156 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 157 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 158 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 159 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 160 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 161 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 162 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 163 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 164 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 165 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 166 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 167 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 168 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 169 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 170 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 171 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 172 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 173 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 174 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 175 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 176 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 177 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 178 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 179 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 180 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 181 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 182 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 183 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 184 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 185 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 186 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 187 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 188 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 189 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 190 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 191 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 192 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 193 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 194 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 195 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 196 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 197 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 198 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 199 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 200 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 201 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 202 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 203 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 204 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 205 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 206 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 207 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 208 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 209 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 210 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 211 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 212 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 213 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 214 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 215 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 216 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 217 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 218 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 219 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 220 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 221 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 222 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 223 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 224 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 225 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 226 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 227 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 228 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 229 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 230 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 231 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 232 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 233 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 234 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 235 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 236 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 237 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 238 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 239 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 240 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 241 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 242 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 243 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 244 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 245 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 246 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 247 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 248 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 249 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 250 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 251 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 252 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 253 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 254 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 255 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 256 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 257 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 258 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 259 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 260 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 261 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 262 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 263 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 264 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 265 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 266 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 267 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 268 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 269 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 270 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 271 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 272 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 273 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 274 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 275 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 276 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 277 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 278 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 279 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 280 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 281 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 282 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 283 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 284 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 285 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 286 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 287 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 288 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 289 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 290 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 291 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 292 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 293 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 294 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 295 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 296 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 297 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 298 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 299 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 300 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 301 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 302 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 303 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 304 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 305 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 306 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 307 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 308 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 309 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 310 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 311 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 312 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 313 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 314 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 315 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 316 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 317 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 318 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 319 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 320 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 321 - Model Summary for Y-Space</th><th style='text-align: center;'>Model 322 - Model Summary for Y-</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.35 R2 and Q2 values of PLS for Y-space with six principal components resulting from auto fit.</div>


We save the project file as WS9.2_PLS-XY.pmvx. In the following, we demonstrate the PLS model plots for the quality variable or Y-space, focusing on those new plots that we did not illustrate in Section 9.2, Workshop 9.1, with the PCA model.

## (1) PLS model for the Y-space

We follow the path: Model → Active Model → Auto Fit (follow Figure 9.20) and see the resulting model in Figure 9.35, displaying the R2 and Q2 values, Eqs. (9.19) and (9.20), versus the number of principal components. As demonstrated in Figure 9.21, we can right-mouse-click on the R2–Q2 plot and select “Create Table” to see a table of R2 and Q2 values in the plot. An R2 value of 0.9654 indicates that the PLS model for Y-space will explain 96.54% of the variability of the dataset for product quality variables with six principal components. A Q2 value of 0.9474 says that with cross-validation, the model can explain 94.74% of the variability of the dataset for product quality variables. Following Figure 9.19 and choosing the # button on the top of the screen and filling in a maximum number of seven principal components, we get a R2–Q2 plot of Figure 9.36. It appears that adding one principal component increases the R2 value from 0.9654 to 0.9712 and Q2 value from 0.9473 to 0.9566. We will use seven principal components in the example below.

## (2) Model variable summary for the Y-space

Next, we follow the path: Analyze → Model → Variable Summary → Choose Block: y-space, and Component: 7. We see in Figure 9.37 that except for Mw (or MWW) (weight-average molecular weight), the PLS model for Y-space predicts CONV, Mn (or MWN), LCB, and SCB reliability with R2 values above 0.9842.

## (3) T1–T2 score plot and W*C[1] versus W*C[2] loading plot

The T1–T2 score plot used to identify clusters and outliers, previously shown in Figure 9.25, applies to both PCA model for the X-space and PLS model for the X and Y spaces. For the PLS model, it is best to use the W*C[1] versus

---

<!-- PDF page 595 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Q2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.36 R2 and Q2 values of PLS for Y-space with seven principal components.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.37 R2 and Q2 values of PLS for Y-space with seven principal components.</div>


W*C[2] loading plot, because it also explains the relationship between the X and Y variables.

By choosing W*,c1-W*,c2 button on the left-side pane, we generate the preferred PLS loading plot on the right side of Figure 9.38. In the plot, we see 5 quality variables, or Y variables, in red, and 14 process variables, or X variables, in black. Referring to the variable definitions in Table 9.1, Section 9.2, we see that the quality variable SCB in red is positively correlated with process variables Fi1 and Tmax1; quality variables Mw, CONV, and LCB in red are negatively correlated with process variables Fi2, Tout2, and Tmax2 in black; and quality variable Mn in red is also negatively correlated with process variables z1 and Tcin2 in black.

---

<!-- PDF page 596 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>T[U]</th><th style='text-align: center;'>T[U] Error Bar Range</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>T1-T2</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>[-5.0, 0.0]</td></tr>
    <tr><td style='text-align: center;'>P1-P2</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>P1 Bar</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>[-3.5, 0.5]</td></tr>
    <tr><td style='text-align: center;'>Hot's T2</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>SPE-X</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>VIP</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>T1-U1</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 W",c2</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>T1-U1</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 W",c2</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>W",c1 Bar Coeffs</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.0]</td></tr>
    <tr><td style='text-align: center;'>Observed</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>[-3.0, 1.</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>W* [s]</th><th style='text-align: center;'>W* [s]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>M1</td><td style='text-align: center;'>-0.45</td><td style='text-align: center;'>-0.25</td></tr>
    <tr><td style='text-align: center;'>M2</td><td style='text-align: center;'>-0.35</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>M3</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>-0.58</td></tr>
    <tr><td style='text-align: center;'>M4</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>M5</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>M6</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M7</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M8</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M9</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M10</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M11</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M12</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M13</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M14</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M15</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M16</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M17</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M18</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M19</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M20</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M21</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M22</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M23</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M24</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M25</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M26</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M27</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M28</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M29</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M30</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M31</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M32</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M33</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M34</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M35</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M36</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M37</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M38</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M39</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M40</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M41</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M42</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M43</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M44</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M45</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M46</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M47</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M48</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M49</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M50</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M51</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M52</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M53</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M54</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M55</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M56</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M57</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M58</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M59</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M60</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M61</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M62</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M63</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M64</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M65</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M66</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M67</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M68</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M69</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M70</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M71</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M72</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M73</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M74</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M75</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M76</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M77</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M78</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M79</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M80</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M81</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M82</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M83</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M84</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M85</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M86</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M87</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M88</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M89</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M90</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M91</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M92</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M93</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M94</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M95</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M96</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M97</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M98</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M99</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M100</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M101</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M102</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M103</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M104</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M105</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M106</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M107</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M108</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M109</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M110</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M111</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M112</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M113</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M114</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M115</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M116</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M117</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M118</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M119</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M120</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M121</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M122</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M123</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M124</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M125</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M126</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M127</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M128</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M129</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M130</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M131</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M132</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M133</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M134</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M135</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M136</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M137</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M138</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M139</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M140</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M141</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M142</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M143</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M144</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M145</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M146</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M147</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M148</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M149</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M150</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M151</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M152</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M153</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M154</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M155</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M156</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M157</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M158</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M159</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M160</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M161</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M162</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M163</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M164</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M165</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M166</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M167</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M168</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M169</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M170</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M171</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M172</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M173</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M174</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M175</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M176</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M177</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M178</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M179</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M180</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M181</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M182</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M183</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M184</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M185</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M186</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M187</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M188</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M189</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M190</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M191</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M192</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M193</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M194</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M195</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M196</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M197</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M198</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M199</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M200</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M201</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M202</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M203</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M204</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M205</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M206</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M207</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M208</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M209</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M210</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M211</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M212</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M213</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M214</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M215</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M216</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M217</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M218</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M219</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M220</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M221</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M222</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M223</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M224</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M225</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M226</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M227</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M228</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M229</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M230</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M231</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M232</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M233</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M234</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M235</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M236</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M237</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M238</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M239</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M240</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M241</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M242</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M243</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M244</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M245</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M246</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>M247</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.38 T[2] versus T[1] score plot and W*C[1]s versus W*C[2] loading plot.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>T[1]</th><th style='text-align: center;'>T[2]</th><th style='text-align: center;'>W* [c1]</th><th style='text-align: center;'>W* [c2]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-5.5</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-5.0</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-4.5</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-4.0</td><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Mn</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-5.5</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-5.0</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-4.5</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-4.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-3.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>8.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>10.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>11.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>13.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>8.5</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>16.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>16.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>10.5</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>11.5</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>18.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>19.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>13.5</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>20.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>21.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>21.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>16.0</td><td style='text-align: center;'>22.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>16.5</td><td style='text-align: center;'>23.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>23.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>24.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>24.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>18.5</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>19.0</td><td style='text-align: center;'>25.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>26.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>26.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>20.5</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>21.0</td><td style='text-align: center;'>27.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>21.5</td><td style='text-align: center;'>28.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>28.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>22.5</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>23.0</td><td style='text-align: center;'>29.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>23.5</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>24.0</td><td style='text-align: center;'>30.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>24.5</td><td style='text-align: center;'>31.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>31.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>25.5</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>26.0</td><td style='text-align: center;'>32.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>26.5</td><td style='text-align: center;'>33.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>33.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>27.5</td><td style='text-align: center;'>34.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>28.0</td><td style='text-align: center;'>34.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>28.5</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>35.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>29.5</td><td style='text-align: center;'>36.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>36.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>30.5</td><td style='text-align: center;'>37.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>31.0</td><td style='text-align: center;'>37.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>31.5</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>38.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>32.5</td><td style='text-align: center;'>39.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>33.0</td><td style='text-align: center;'>39.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>33.5</td><td style='text-align: center;'>40.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>34.0</td><td style='text-align: center;'>40.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>34.5</td><td style='text-align: center;'>41.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>41.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>35.5</td><td style='text-align: center;'>42.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>36.0</td><td style='text-align: center;'>42.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>36.5</td><td style='text-align: center;'>43.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>37.0</td><td style='text-align: center;'>43.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>37.5</td><td style='text-align: center;'>44.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>44.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>38.5</td><td style='text-align: center;'>45.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>39.0</td><td style='text-align: center;'>45.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>39.5</td><td style='text-align: center;'>46.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>40.0</td><td style='text-align: center;'>46.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>40.5</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>41.0</td><td style='text-align: center;'>47.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>41.5</td><td style='text-align: center;'>48.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>42.0</td><td style='text-align: center;'>48.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>42.5</td><td style='text-align: center;'>49.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>43.0</td><td style='text-align: center;'>49.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>43.5</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>44.0</td><td style='text-align: center;'>50.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>44.5</td><td style='text-align: center;'>51.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>45.0</td><td style='text-align: center;'>51.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>45.5</td><td style='text-align: center;'>52.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>46.0</td><td style='text-align: center;'>52.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>46.5</td><td style='text-align: center;'>53.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>47.0</td><td style='text-align: center;'>53.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>47.5</td><td style='text-align: center;'>54.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>48.0</td><td style='text-align: center;'>54.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>48.5</td><td style='text-align: center;'>55.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>49.0</td><td style='text-align: center;'>55.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>49.5</td><td style='text-align: center;'>56.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>56.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>50.5</td><td style='text-align: center;'>57.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>51.0</td><td style='text-align: center;'>57.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>51.5</td><td style='text-align: center;'>58.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>52.0</td><td style='text-align: center;'>58.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>52.5</td><td style='text-align: center;'>59.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>53.0</td><td style='text-align: center;'>59.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>53.5</td><td style='text-align: center;'>60.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>54.0</td><td style='text-align: center;'>60.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>54.5</td><td style='text-align: center;'>61.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>55.0</td><td style='text-align: center;'>61.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>55.5</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>56.0</td><td style='text-align: center;'>62.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>56.5</td><td style='text-align: center;'>63.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>57.0</td><td style='text-align: center;'>63.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>57.5</td><td style='text-align: center;'>64.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>58.0</td><td style='text-align: center;'>64.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>58.5</td><td style='text-align: center;'>65.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>59.0</td><td style='text-align: center;'>65.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>60.0</td><td style='text-align: center;'>66.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>60.5</td><td style='text-align: center;'>66.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>61.0</td><td style='text-align: center;'>67.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>61.5</td><td style='text-align: center;'>67.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'>68.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>62.5</td><td style='text-align: center;'>68.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>63.0</td><td style='text-align: center;'>69.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>63.5</td><td style='text-align: center;'>69.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>64.0</td><td style='text-align: center;'>70.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>64.5</td><td style='text-align: center;'>70.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>65.0</td><td style='text-align: center;'>71.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>65.5</td><td style='text-align: center;'>71.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>66.0</td><td style='text-align: center;'>72.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.39 Loading bi-plot.</div>


## (4) Loading bi-plot

A loading bi-plot superimposes the loadings and scores, such as Figure 9.38 (left and right) for easier interpretation of the relationship between the variables and observations. Following the path, Analyze → Loading bi-plot → Worksets: training, Block: X-space; X-axis: component 1; Y-axis: component 2, we generate a loading bi-plot of Figure 9.39.

## (5) Obs versus Pred plot

By choosing Obs versus Pred on the left-side pane and specifying the following: worksets – training; observation – 1; block – product quality variable; variable – Mn; component: 7; raw units, we generate the Obs versus pred plot of Figure 9.40. The root-mean-squared-error (RMSE) of 35.5144 is only 0.013% of the average observed value of 27,400.

---

<!-- PDF page 597 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_556_151_714_185.jpg" alt="Image" width="16%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Predicted [7 comp.]</th><th style='text-align: center;'>Observed</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26820</td><td style='text-align: center;'>26800</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26840</td><td style='text-align: center;'>26820</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26860</td><td style='text-align: center;'>26840</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26880</td><td style='text-align: center;'>26860</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26900</td><td style='text-align: center;'>26880</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26920</td><td style='text-align: center;'>26900</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26940</td><td style='text-align: center;'>26920</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26960</td><td style='text-align: center;'>26940</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>26980</td><td style='text-align: center;'>26960</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27000</td><td style='text-align: center;'>26980</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27020</td><td style='text-align: center;'>27000</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27040</td><td style='text-align: center;'>27020</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27060</td><td style='text-align: center;'>27040</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27080</td><td style='text-align: center;'>27060</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27100</td><td style='text-align: center;'>27080</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27120</td><td style='text-align: center;'>27100</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27140</td><td style='text-align: center;'>27120</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27160</td><td style='text-align: center;'>27140</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27180</td><td style='text-align: center;'>27160</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27200</td><td style='text-align: center;'>27180</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27220</td><td style='text-align: center;'>27200</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27240</td><td style='text-align: center;'>27220</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27260</td><td style='text-align: center;'>27240</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27280</td><td style='text-align: center;'>27260</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27300</td><td style='text-align: center;'>27280</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27320</td><td style='text-align: center;'>27300</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27340</td><td style='text-align: center;'>27320</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27360</td><td style='text-align: center;'>27340</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27380</td><td style='text-align: center;'>27360</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27400</td><td style='text-align: center;'>27380</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27420</td><td style='text-align: center;'>27400</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27440</td><td style='text-align: center;'>27420</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27460</td><td style='text-align: center;'>27440</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27480</td><td style='text-align: center;'>27460</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27500</td><td style='text-align: center;'>27480</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27520</td><td style='text-align: center;'>27500</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27540</td><td style='text-align: center;'>27520</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27560</td><td style='text-align: center;'>27540</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27580</td><td style='text-align: center;'>27560</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27600</td><td style='text-align: center;'>27580</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27620</td><td style='text-align: center;'>27600</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27640</td><td style='text-align: center;'>27620</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27660</td><td style='text-align: center;'>27640</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27680</td><td style='text-align: center;'>27660</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27700</td><td style='text-align: center;'>27680</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27720</td><td style='text-align: center;'>27700</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27740</td><td style='text-align: center;'>27720</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27760</td><td style='text-align: center;'>27740</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27780</td><td style='text-align: center;'>27760</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27800</td><td style='text-align: center;'>27780</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27820</td><td style='text-align: center;'>27800</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27840</td><td style='text-align: center;'>27820</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27860</td><td style='text-align: center;'>27840</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27880</td><td style='text-align: center;'>27860</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27900</td><td style='text-align: center;'>27880</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27920</td><td style='text-align: center;'>27900</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27940</td><td style='text-align: center;'>27920</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27960</td><td style='text-align: center;'>27940</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>27980</td><td style='text-align: center;'>27960</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28000</td><td style='text-align: center;'>27980</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28020</td><td style='text-align: center;'>28000</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28040</td><td style='text-align: center;'>28020</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28060</td><td style='text-align: center;'>28040</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28080</td><td style='text-align: center;'>28060</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28100</td><td style='text-align: center;'>28080</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28120</td><td style='text-align: center;'>28100</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28140</td><td style='text-align: center;'>28120</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28160</td><td style='text-align: center;'>28140</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28180</td><td style='text-align: center;'>28160</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28200</td><td style='text-align: center;'>28180</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28220</td><td style='text-align: center;'>28200</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28240</td><td style='text-align: center;'>28220</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28260</td><td style='text-align: center;'>28240</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28280</td><td style='text-align: center;'>28260</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28300</td><td style='text-align: center;'>28280</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28320</td><td style='text-align: center;'>28300</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28340</td><td style='text-align: center;'>28320</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28360</td><td style='text-align: center;'>28340</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28380</td><td style='text-align: center;'>28360</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28400</td><td style='text-align: center;'>28380</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28420</td><td style='text-align: center;'>28400</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28440</td><td style='text-align: center;'>28420</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28460</td><td style='text-align: center;'>28440</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28480</td><td style='text-align: center;'>28460</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28500</td><td style='text-align: center;'>28480</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28520</td><td style='text-align: center;'>28500</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28540</td><td style='text-align: center;'>28520</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28560</td><td style='text-align: center;'>28540</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28580</td><td style='text-align: center;'>28560</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28600</td><td style='text-align: center;'>28580</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28620</td><td style='text-align: center;'>28600</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28640</td><td style='text-align: center;'>28620</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28660</td><td style='text-align: center;'>28640</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28680</td><td style='text-align: center;'>28660</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28700</td><td style='text-align: center;'>28680</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28720</td><td style='text-align: center;'>28700</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28740</td><td style='text-align: center;'>28720</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28760</td><td style='text-align: center;'>28740</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28780</td><td style='text-align: center;'>28760</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28800</td><td style='text-align: center;'>28780</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28820</td><td style='text-align: center;'>28800</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28840</td><td style='text-align: center;'>28820</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28860</td><td style='text-align: center;'>28840</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28880</td><td style='text-align: center;'>28860</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28900</td><td style='text-align: center;'>28880</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28920</td><td style='text-align: center;'>28900</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28940</td><td style='text-align: center;'>28920</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28960</td><td style='text-align: center;'>28940</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>28980</td><td style='text-align: center;'>28960</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29000</td><td style='text-align: center;'>28980</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29020</td><td style='text-align: center;'>29000</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29040</td><td style='text-align: center;'>29020</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29060</td><td style='text-align: center;'>29040</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29080</td><td style='text-align: center;'>29060</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29100</td><td style='text-align: center;'>29080</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29120</td><td style='text-align: center;'>29100</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29140</td><td style='text-align: center;'>29120</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29160</td><td style='text-align: center;'>29140</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29180</td><td style='text-align: center;'>29160</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29200</td><td style='text-align: center;'>29180</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29220</td><td style='text-align: center;'>29200</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29240</td><td style='text-align: center;'>29220</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29260</td><td style='text-align: center;'>29240</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29280</td><td style='text-align: center;'>29260</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29300</td><td style='text-align: center;'>29280</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29320</td><td style='text-align: center;'>29300</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29340</td><td style='text-align: center;'>29320</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29360</td><td style='text-align: center;'>29340</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29380</td><td style='text-align: center;'>29360</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29400</td><td style='text-align: center;'>29380</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29420</td><td style='text-align: center;'>29400</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29440</td><td style='text-align: center;'>29420</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29460</td><td style='text-align: center;'>29440</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29480</td><td style='text-align: center;'>29460</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29500</td><td style='text-align: center;'>29480</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29520</td><td style='text-align: center;'>29500</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29540</td><td style='text-align: center;'>29520</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29560</td><td style='text-align: center;'>29540</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29580</td><td style='text-align: center;'>29560</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29600</td><td style='text-align: center;'>29580</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29620</td><td style='text-align: center;'>29600</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29640</td><td style='text-align: center;'>29620</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29660</td><td style='text-align: center;'>29640</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29680</td><td style='text-align: center;'>29660</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29700</td><td style='text-align: center;'>29680</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29720</td><td style='text-align: center;'>29700</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29740</td><td style='text-align: center;'>29720</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29760</td><td style='text-align: center;'>29740</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29780</td><td style='text-align: center;'>29760</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29800</td><td style='text-align: center;'>29780</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29820</td><td style='text-align: center;'>29800</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29840</td><td style='text-align: center;'>29820</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29860</td><td style='text-align: center;'>29840</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29880</td><td style='text-align: center;'>29860</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29900</td><td style='text-align: center;'>29880</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29920</td><td style='text-align: center;'>29900</td></tr>
    <tr><td style='text-align: center;'>R2 = 0.98429</td><td style='text-align: center;'>29940</td><td style='text-align: center;'>29920</td></tr>
    <tr><td style='text-align: center;'>R</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.40 Obs versus Pred plot of product quality variable, Mn (number-average molecular weight).</div>


This concludes workshop WS9.2_PLS-XY, and we save the file as WS9.2_PLS-XY.pmvx.

##### 9.4.2 Workshop 9.3: Polymer Melt Index Prediction and Causal Analysis Using PLS

The objective of this workshop is to demonstrate the application of PLS model for predicting the MI and causal analysis of a HDPE manufacturing process. We consider an industrial slurry HDPE process with two reactors in parallel using plant data from LG Petrochemicals in South Korea [20]. See Figure 9.41.

We convert a steady-state simulation model based on Aspen Plus to a dynamic (time-dependent) simulation model using Aspen Plus Dynamics. The resulting dynamic simulation model has similar independent variables as explained before. Both steady-state and dynamic simulation models are developed from first principles such as phase-equilibrium calculations and mass and energy balances. Therefore, they are scientifically consistent models.

Park et al. [20] correlate the MI data by considering the independent variables shown in Table 9.2. The dataset consists of 5000 observations, 9 main independent process variables, and 1 dependent variable, MI, as the quality target. We first make sure the data are in Excel format and the process variable (X) and (Y) data are in different sheets within HDPE_XY Data.xlsx.

---

<!-- PDF page 598 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_147_814_519.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 9.41 Process simulation flowsheet of an industrial parallel slurry HDPE process.</div>


<div style="text-align: center;">Table 9.2 Process and quality variables of the parallel slurry HDPE process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process and quality variables</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2</td><td style='text-align: center; word-wrap: break-word;'>Ethylene feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>Hydrogen feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>Catalyst feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>Hexane solvent feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3</td><td style='text-align: center; word-wrap: break-word;'>Comonomer feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T</td><td style='text-align: center; word-wrap: break-word;'>Temperature of the reactor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P</td><td style='text-align: center; word-wrap: break-word;'>Pressure in the reactor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2/C2</td><td style='text-align: center; word-wrap: break-word;'>Feed concentration ratio in the reactor of ethylene to hydrogen</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3/C4</td><td style='text-align: center; word-wrap: break-word;'>Feed concentration ratio of propylene to butylene monomer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI (quality variable)</td><td style='text-align: center; word-wrap: break-word;'>Melt Index of polymer</td></tr></table>

We open a new project in Aspen ProMV. Following Figure 9.27 in Workshop 9.2, we import both process (X) and quality (Y) variable datasets, HDPE_XY Data.xlsx, into Aspen ProMV. On the data manager, we choose the X block and highlight all "Obs ID" for X variables to "Include" all X observations (see Figure 9.42). Clicking on OK in "Observation Summary" leads to the "New Model" screen, and choosing the X block generates the details of nine process variables, including their mean, standard deviation, and min/max value (see Figure 9.43). Likewise, choosing the Y block shows the details of the single quality variable, MI (see Figure 9.44). We then name the new model as WS9.3_PLS-XY.pmvx.

---

<!-- PDF page 599 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_159_713_686.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 9.42 Highlighting all X variable Obs ID in “Observation Summary” to include all observations.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_133_776_783_1210.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 9.43 Process variable details in the new model.</div>


---

<!-- PDF page 600 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_149_812_463.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.44 Quality variable details in the new model.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Model 1</th><th style='text-align: center;'>Model 2</th><th style='text-align: center;'>Model 3</th><th style='text-align: center;'>Model 4</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.82</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.94</td></tr>
    <tr><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.84</td><td style='text-align: center;'>0.86</td><td style='text-align: center;'>0.91</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.96</td></tr>
    <tr><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.93</td><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.97</td></tr>
  </tbody>
</table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_167_536_813_787.jpg" alt="Image" width="67%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Model 1 - Table</th><th style='text-align: center;'>Model 2 - Table</th><th style='text-align: center;'>Model 3 - Table</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>A</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>B</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>C</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>D</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Training</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Num.</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Q2 Cumul...</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>[1]</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>[2]</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>[3]</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td><td style='text-align: center;'>4</td></tr>
    <tr><td style='text-align: center;'>[4]</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td><td style='text-align: center;'>5</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.45 R2 and Q2 values of PLS for Y-space with four principal components resulting from auto fit.</div>


## (1) PLS Model for the Y-space

We follow the path: Model → Active Model → Auto Fit (follow Figure 9.20) and see the R2 and Q2 values of the resulting model in Figure 9.45. The figure shows that with four principal components, an R2 value of 0.9534 says that the PLS model can explain 95.34% of the variability of the product quality variable, the melt index (MI); a Q2 value of 0.9533 means that with cross-validation, the PLS model can explain 95.33% of the data variability.

(2) Obs versus Pred plot

Following Figure 9.40, we generate an Obs versus Pred plot in Figure 9.46. The RMSEE (root-mean-square error of estimation) is 1.08266.

(3) Loading bi-plot and VIP plot

Following Figure 9.39, we show a loading bi-plot that superimposes the T[2] versus T[1] score plot and W*c[1] versus W*c[2] plot in Figure 9.47.

We see that from the scores, T[2] versus T[1], process variables CAT and H2/C2 in black are both outside the 99% confidence limit and are potentially outliers.

---

<!-- PDF page 601 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Predicted [4 comp.]</th><th style='text-align: center;'>Observed</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-0.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>-0.1</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>0.1</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>0.2</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>0.3</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>0.4</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>0.6</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>0.7</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>0.8</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>0.9</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>1.1</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>1.2</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>1.3</td><td style='text-align: center;'>16.0</td></tr>
    <tr><td style='text-align: center;'>1.4</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>1.6</td><td style='text-align: center;'>19.0</td></tr>
    <tr><td style='text-align: center;'>1.7</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>1.8</td><td style='text-align: center;'>21.0</td></tr>
    <tr><td style='text-align: center;'>1.9</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>2.1</td><td style='text-align: center;'>24.0</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>2.3</td><td style='text-align: center;'>26.0</td></tr>
    <tr><td style='text-align: center;'>2.4</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>2.6</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>2.7</td><td style='text-align: center;'>30.0</td></tr>
    <tr><td style='text-align: center;'>2.8</td><td style='text-align: center;'>31.0</td></tr>
    <tr><td style='text-align: center;'>2.9</td><td style='text-align: center;'>32.0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>33.0</td></tr>
    <tr><td style='text-align: center;'>3.1</td><td style='text-align: center;'>34.0</td></tr>
    <tr><td style='text-align: center;'>3.2</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>3.3</td><td style='text-align: center;'>36.0</td></tr>
    <tr><td style='text-align: center;'>3.4</td><td style='text-align: center;'>37.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>38.0</td></tr>
    <tr><td style='text-align: center;'>3.6</td><td style='text-align: center;'>39.0</td></tr>
    <tr><td style='text-align: center;'>3.7</td><td style='text-align: center;'>40.0</td></tr>
    <tr><td style='text-align: center;'>3.8</td><td style='text-align: center;'>41.0</td></tr>
    <tr><td style='text-align: center;'>3.9</td><td style='text-align: center;'>42.0</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>43.0</td></tr>
    <tr><td style='text-align: center;'>4.1</td><td style='text-align: center;'>44.0</td></tr>
    <tr><td style='text-align: center;'>4.2</td><td style='text-align: center;'>45.0</td></tr>
    <tr><td style='text-align: center;'>4.3</td><td style='text-align: center;'>46.0</td></tr>
    <tr><td style='text-align: center;'>4.4</td><td style='text-align: center;'>47.0</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>48.0</td></tr>
    <tr><td style='text-align: center;'>4.6</td><td style='text-align: center;'>49.0</td></tr>
    <tr><td style='text-align: center;'>4.7</td><td style='text-align: center;'>50.0</td></tr>
    <tr><td style='text-align: center;'>4.8</td><td style='text-align: center;'>51.0</td></tr>
    <tr><td style='text-align: center;'>4.9</td><td style='text-align: center;'>52.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>53.0</td></tr>
    <tr><td style='text-align: center;'>5.1</td><td style='text-align: center;'>54.0</td></tr>
    <tr><td style='text-align: center;'>5.2</td><td style='text-align: center;'>55.0</td></tr>
    <tr><td style='text-align: center;'>5.3</td><td style='text-align: center;'>56.0</td></tr>
    <tr><td style='text-align: center;'>5.4</td><td style='text-align: center;'>57.0</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>58.0</td></tr>
    <tr><td style='text-align: center;'>5.6</td><td style='text-align: center;'>59.0</td></tr>
    <tr><td style='text-align: center;'>5.7</td><td style='text-align: center;'>60.0</td></tr>
    <tr><td style='text-align: center;'>5.8</td><td style='text-align: center;'>61.0</td></tr>
    <tr><td style='text-align: center;'>5.9</td><td style='text-align: center;'>62.0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>63.0</td></tr>
    <tr><td style='text-align: center;'>6.1</td><td style='text-align: center;'>64.0</td></tr>
    <tr><td style='text-align: center;'>6.2</td><td style='text-align: center;'>65.0</td></tr>
    <tr><td style='text-align: center;'>6.3</td><td style='text-align: center;'>66.0</td></tr>
    <tr><td style='text-align: center;'>6.4</td><td style='text-align: center;'>67.0</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>68.0</td></tr>
    <tr><td style='text-align: center;'>6.6</td><td style='text-align: center;'>69.0</td></tr>
    <tr><td style='text-align: center;'>6.7</td><td style='text-align: center;'>70.0</td></tr>
    <tr><td style='text-align: center;'>6.8</td><td style='text-align: center;'>71.0</td></tr>
    <tr><td style='text-align: center;'>6.9</td><td style='text-align: center;'>72.0</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>73.0</td></tr>
    <tr><td style='text-align: center;'>7.1</td><td style='text-align: center;'>74.0</td></tr>
    <tr><td style='text-align: center;'>7.2</td><td style='text-align: center;'>75.0</td></tr>
    <tr><td style='text-align: center;'>7.3</td><td style='text-align: center;'>76.0</td></tr>
    <tr><td style='text-align: center;'>7.4</td><td style='text-align: center;'>77.0</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>78.0</td></tr>
    <tr><td style='text-align: center;'>7.6</td><td style='text-align: center;'>79.0</td></tr>
    <tr><td style='text-align: center;'>7.7</td><td style='text-align: center;'>80.0</td></tr>
    <tr><td style='text-align: center;'>7.8</td><td style='text-align: center;'>81.0</td></tr>
    <tr><td style='text-align: center;'>7.9</td><td style='text-align: center;'>82.0</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>83.0</td></tr>
    <tr><td style='text-align: center;'>8.1</td><td style='text-align: center;'>84.0</td></tr>
    <tr><td style='text-align: center;'>8.2</td><td style='text-align: center;'>85.0</td></tr>
    <tr><td style='text-align: center;'>8.3</td><td style='text-align: center;'>86.0</td></tr>
    <tr><td style='text-align: center;'>8.4</td><td style='text-align: center;'>87.0</td></tr>
    <tr><td style='text-align: center;'>8.5</td><td style='text-align: center;'>88.0</td></tr>
    <tr><td style='text-align: center;'>8.6</td><td style='text-align: center;'>89.0</td></tr>
    <tr><td style='text-align: center;'>8.7</td><td style='text-align: center;'>90.0</td></tr>
    <tr><td style='text-align: center;'>8.8</td><td style='text-align: center;'>91.0</td></tr>
    <tr><td style='text-align: center;'>8.9</td><td style='text-align: center;'>92.0</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>93.0</td></tr>
    <tr><td style='text-align: center;'>9.1</td><td style='text-align: center;'>94.0</td></tr>
    <tr><td style='text-align: center;'>9.2</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>9.3</td><td style='text-align: center;'>96.0</td></tr>
    <tr><td style='text-align: center;'>9.4</td><td style='text-align: center;'>97.0</td></tr>
    <tr><td style='text-align: center;'>9.5</td><td style='text-align: center;'>98.0</td></tr>
    <tr><td style='text-align: center;'>9.6</td><td style='text-align: center;'>99.0</td></tr>
    <tr><td style='text-align: center;'>9.7</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>9.8</td><td style='text-align: center;'>101.0</td></tr>
    <tr><td style='text-align: center;'>9.9</td><td style='text-align: center;'>102.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>103.0</td></tr>
    <tr><td style='text-align: center;'>10.1</td><td style='text-align: center;'>104.0</td></tr>
    <tr><td style='text-align: center;'>10.2</td><td style='text-align: center;'>105.0</td></tr>
    <tr><td style='text-align: center;'>10.3</td><td style='text-align: center;'>106.0</td></tr>
    <tr><td style='text-align: center;'>10.4</td><td style='text-align: center;'>107.0</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>108.0</td></tr>
    <tr><td style='text-align: center;'>10.6</td><td style='text-align: center;'>109.0</td></tr>
    <tr><td style='text-align: center;'>10.7</td><td style='text-align: center;'>110.0</td></tr>
    <tr><td style='text-align: center;'>10.8</td><td style='text-align: center;'>111.0</td></tr>
    <tr><td style='text-align: center;'>10.9</td><td style='text-align: center;'>112.0</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>113.0</td></tr>
    <tr><td style='text-align: center;'>11.1</td><td style='text-align: center;'>114.0</td></tr>
    <tr><td style='text-align: center;'>11.2</td><td style='text-align: center;'>115.0</td></tr>
    <tr><td style='text-align: center;'>11.3</td><td style='text-align: center;'>116.0</td></tr>
    <tr><td style='text-align: center;'>11.4</td><td style='text-align: center;'>117.0</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>118.0</td></tr>
    <tr><td style='text-align: center;'>11.6</td><td style='text-align: center;'>119.0</td></tr>
    <tr><td style='text-align: center;'>11.7</td><td style='text-align: center;'>120.0</td></tr>
    <tr><td style='text-align: center;'>11.8</td><td style='text-align: center;'>121.0</td></tr>
    <tr><td style='text-align: center;'>11.9</td><td style='text-align: center;'>122.0</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>123.0</td></tr>
    <tr><td style='text-align: center;'>12.1</td><td style='text-align: center;'>124.0</td></tr>
    <tr><td style='text-align: center;'>12.2</td><td style='text-align: center;'>125.0</td></tr>
    <tr><td style='text-align: center;'>12.3</td><td style='text-align: center;'>126.0</td></tr>
    <tr><td style='text-align: center;'>12.4</td><td style='text-align: center;'>127.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>128.0</td></tr>
    <tr><td style='text-align: center;'>12.6</td><td style='text-align: center;'>129.0</td></tr>
    <tr><td style='text-align: center;'>12.7</td><td style='text-align: center;'>130.0</td></tr>
    <tr><td style='text-align: center;'>12.8</td><td style='text-align: center;'>131.0</td></tr>
    <tr><td style='text-align: center;'>12.9</td><td style='text-align: center;'>132.0</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>133.0</td></tr>
    <tr><td style='text-align: center;'>13.1</td><td style='text-align: center;'>134.0</td></tr>
    <tr><td style='text-align: center;'>13.2</td><td style='text-align: center;'>135.0</td></tr>
    <tr><td style='text-align: center;'>13.3</td><td style='text-align: center;'>136.0</td></tr>
    <tr><td style='text-align: center;'>13.4</td><td style='text-align: center;'>137.0</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>138.0</td></tr>
    <tr><td style='text-align: center;'>13.6</td><td style='text-align: center;'>139.0</td></tr>
    <tr><td style='text-align: center;'>13.7</td><td style='text-align: center;'>140.0</td></tr>
    <tr><td style='text-align: center;'>13.8</td><td style='text-align: center;'>141.0</td></tr>
    <tr><td style='text-align: center;'>13.9</td><td style='text-align: center;'>142.0</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>143.0</td></tr>
    <tr><td style='text-align: center;'>14.1</td><td style='text-align: center;'>144.0</td></tr>
    <tr><td style='text-align: center;'>14.2</td><td style='text-align: center;'>145.0</td></tr>
    <tr><td style='text-align: center;'>14.3</td><td style='text-align: center;'>146.0</td></tr>
    <tr><td style='text-align: center;'>14.4</td><td style='text-align: center;'>147.0</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>148.0</td></tr>
    <tr><td style='text-align: center;'>14.6</td><td style='text-align: center;'>149.0</td></tr>
    <tr><td style='text-align: center;'>14.7</td><td style='text-align: center;'>150.0</td></tr>
    <tr><td style='text-align: center;'>14.8</td><td style='text-align: center;'>151.0</td></tr>
    <tr><td style='text-align: center;'>14.9</td><td style='text-align: center;'>152.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>153.0</td></tr>
    <tr><td style='text-align: center;'>15.1</td><td style='text-align: center;'>154.0</td></tr>
    <tr><td style='text-align: center;'>15.2</td><td style='text-align: center;'>155.0</td></tr>
    <tr><td style='text-align: center;'>15.3</td><td style='text-align: center;'>156.0</td></tr>
    <tr><td style='text-align: center;'>15.4</td><td style='text-align: center;'>157.0</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>158.0</td></tr>
    <tr><td style='text-align: center;'>15.6</td><td style='text-align: center;'>159.0</td></tr>
    <tr><td style='text-align: center;'>15.7</td><td style='text-align: center;'>160.0</td></tr>
    <tr><td style='text-align: center;'>15.8</td><td style='text-align: center;'>161.0</td></tr>
    <tr><td style='text-align: center;'>15.9</td><td style='text-align: center;'>162.0</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>163.0</td></tr>
    <tr><td style='text-align: center;'>16.1</td><td style='text-align: center;'>164.0</td></tr>
    <tr><td style='text-align: center;'>16.2</td><td style='text-align: center;'>165.0</td></tr>
    <tr><td style='text-align: center;'>16.3</td><td style='text-align: center;'>166.0</td></tr>
    <tr><td style='text-align: center;'>16.4</td><td style='text-align: center;'>167.0</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>168.0</td></tr>
    <tr><td style='text-align: center;'>16.6</td><td style='text-align: center;'>169.0</td></tr>
    <tr><td style='text-align: center;'>16.7</td><td style='text-align: center;'>170.0</td></tr>
    <tr><td style='text-align: center;'>16.8</td><td style='text-align: center;'>171.0</td></tr>
    <tr><td style='text-align: center;'>16.9</td><td style='text-align: center;'>172.0</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>173.0</td></tr>
    <tr><td style='text-align: center;'>17.1</td><td style='text-align: center;'>174.0</td></tr>
    <tr><td style='text-align: center;'>17.2</td><td style='text-align: center;'>175.0</td></tr>
    <tr><td style='text-align: center;'>17.3</td><td style='text-align: center;'>176.0</td></tr>
    <tr><td style='text-align: center;'>17.4</td><td style='text-align: center;'>177.0</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>178.0</td></tr>
    <tr><td style='text-align: center;'>17.6</td><td style='text-align: center;'>179.0</td></tr>
    <tr><td style='text-align: center;'>17.7</td><td style='text-align: center;'>180.0</td></tr>
    <tr><td style='text-align: center;'>17.8</td><td style='text-align: center;'>181.0</td></tr>
    <tr><td style='text-align: center;'>17.9</td><td style='text-align: center;'>182.0</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>183.0</td></tr>
    <tr><td style='text-align: center;'>18.1</td><td style='text-align: center;'>184.0</td></tr>
    <tr><td style='text-align: center;'>18.2</td><td style='text-align: center;'>185.0</td></tr>
    <tr><td style='text-align: center;'>18.3</td><td style='text-align: center;'>186.0</td></tr>
    <tr><td style='text-align: center;'>18.4</td><td style='text-align: center;'>187.0</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>188.0</td></tr>
    <tr><td style='text-align: center;'>18.6</td><td style='text-align: center;'>189.0</td></tr>
    <tr><td style='text-align: center;'>18.7</td><td style='text-align: center;'>190.0</td></tr>
    <tr><td style='text-align: center;'>18.8</td><td style='text-align: center;'>191.0</td></tr>
    <tr><td style='text-align: center;'>18.9</td><td style='text-align: center;'>192.0</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>193.0</td></tr>
    <tr><td style='text-align: center;'>19.1</td><td style='text-align: center;'>194.0</td></tr>
    <tr><td style='text-align: center;'>19.2</td><td style='text-align: center;'>195.0</td></tr>
    <tr><td style='text-align: center;'>19.3</td><td style='text-align: center;'>196.0</td></tr>
    <tr><td style='text-align: center;'>19.4</td><td style='text-align: center;'>197.0</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>198.0</td></tr>
    <tr><td style='text-align: center;'>19.6</td><td style='text-align: center;'>199.0</td></tr>
    <tr><td style='text-align: center;'>19.7</td><td style='text-align: center;'>200.0</td></tr>
    <tr><td style='text-align: center;'>19.8</td><td style='text-align: center;'>201.0</td></tr>
    <tr><td style='text-align: center;'>19.9</td><td style='text-align: center;'>202.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>203.0</td></tr>
    <tr><td style='text-align: center;'>20.1</td><td style='text-align: center;'>204.0</td></tr>
    <tr><td style='text-align: center;'>20.2</td><td style='text-align: center;'>205.0</td></tr>
    <tr><td style='text-align: center;'>20.3</td><td style='text-align: center;'>206.0</td></tr>
    <tr><td style='text-align: center;'>20.4</td><td style='text-align: center;'>207.0</td></tr>
    <tr><td style='text-align: center;'>20.5</td><td style='text-align: center;'>208.0</td></tr>
    <tr><td style='text-align: center;'>20.6</td><td style='text-align: center;'>209.0</td></tr>
    <tr><td style='text-align: center;'>20.7</td><td style='text-align: center;'>210.0</td></tr>
    <tr><td style='text-align: center;'>20.8</td><td style='text-align: center;'>211.0</td></tr>
    <tr><td style='text-align: center;'>20.9</td><td style='text-align: center;'>212.0</td></tr>
    <tr><td style='text-align: center;'>21.0</td><td style='text-align: center;'>213.0</td></tr>
    <tr><td style='text-align: center;'>21.1</td><td style='text-align: center;'>214.0</td></tr>
    <tr><td style='text-align: center;'>21.2</td><td style='text-align: center;'>215.0</td></tr>
    <tr><td style='text-align: center;'>21.3</td><td style='text-align: center;'>216.0</td></tr>
    <tr><td style='text-align: center;'>21.4</td><td style='text-align: center;'>217.0</td></tr>
    <tr><td style='text-align: center;'>21.5</td><td style='text-align: center;'>218.0</td></tr>
    <tr><td style='text-align: center;'>21.6</td><td style='text-align: center;'>219.0</td></tr>
    <tr><td style='text-align: center;'>21.7</td><td style='text-align: center;'>220.0</td></tr>
    <tr><td style='text-align: center;'>21.8</td><td style='text-align: center;'>221.0</td></tr>
    <tr><td style='text-align: center;'>21.9</td><td style='text-align: center;'>222.0</td></tr>
    <tr><td style='text-align: center;'>22.0</td><td style='text-align: center;'>223.0</td></tr>
    <tr><td style='text-align: center;'>22.1</td><td style='text-align: center;'>224.0</td></tr>
    <tr><td style='text-align: center;'>22.2</td><td style='text-align: center;'>225.0</td></tr>
    <tr><td style='text-align: center;'>22.3</td><td style='text-align: center;'>226.0</td></tr>
    <tr><td style='text-align: center;'>22.4</td><td style='text-align: center;'>227.0</td></tr>
    <tr><td style='text-align: center;'>22.5</td><td style='text-align: center;'>228.0</td></tr>
    <tr><td style='text-align: center;'>22.6</td><td style='text-align: center;'>229.0</td></tr>
    <tr><td style='text-align: center;'>22.7</td><td style='text-align: center;'>230.0</td></tr>
    <tr><td style='text-align: center;'>22.8</td><td style='text-align: center;'>231.0</td></tr>
    <tr><td style='text-align: center;'>22.9</td><td style='text-align: center;'>232.0</td></tr>
    <tr><td style='text-align: center;'>23.0</td><td style='text-align: center;'>233.0</td></tr>
    <tr><td style='text-align: center;'>23.1</td><td style='text-align: center;'>234.0</td></tr>
    <tr><td style='text-align: center;'>23.2</td><td style='text-align: center;'>235.0</td></tr>
    <tr><td style='text-align: center;'>23.3</td><td style='text-align: center;'>236.0</td></tr>
    <tr><td style='text-align: center;'>23.4</td><td style='text-align: center;'>237.0</td></tr>
    <tr><td style='text-align: center;'>23.5</td><td style='text-align: center;'>238.0</td></tr>
    <tr><td style='text-align: center;'>23.6</td><td style='text-align: center;'>239.0</td></tr>
    <tr><td style='text-align: center;'>23.7</td><td style='text-align: center;'>240.0</td></tr>
    <tr><td style='text-align: center;'>23.8</td><td style='text-align: center;'>241.0</td></tr>
    <tr><td style='text-align: center;'>23.9</td><td style='text-align: center;'>242.0</td></tr>
    <tr><td style='text-align: center;'>24.0</td><td style='text-align: center;'>243.0</td></tr>
    <tr><td style='text-align: center;'>24.1</td><td style='text-align: center;'>244.0</td></tr>
    <tr><td style='text-align: center;'>24.2</td><td style='text-align: center;'>245.0</td></tr>
    <tr><td style='text-align: center;'>24.3</td><td style='text-align: center;'>246.0</td></tr>
    <tr><td style='text-align: center;'>24.4</td><td style='text-align: center;'>247.0</td></tr>
    <tr><td style='text-align: center;'>24.5</td><td style='text-align: center;'>248.0</td></tr>
    <tr><td style='text-align: center;'>24.6</td><td style='text-align: center;'>249.0</td></tr>
    <tr><td style='text-align: center;'>24.7</td><td style='text-align: center;'>250.0</td></tr>
    <tr><td style='text-align: center;'>24.8</td><td style='text-align: center;'>251.0</td></tr>
    <tr><td style='text-align: center;'>24.9</td><td style='text-align: center;'>252.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>253.0</td></tr>
    <tr><td style='text-align: center;'>25.1</td><td style='text-align: center;'>254.0</td></tr>
    <tr><td style='text-align: center;'>25.2</td><td style='text-align: center;'>255.0</td></tr>
    <tr><td style='text-align: center;'>25.3</td><td style='text-align: center;'>256.0</td></tr>
    <tr><td style='text-align: center;'>25.4</td><td style='text-align: center;'>257.0</td></tr>
    <tr><td style='text-align: center;'>25.5</td><td style='text-align: center;'>258.0</td></tr>
    <tr><td style='text-align: center;'>25.6</td><td style='text-align: center;'>259.0</td></tr>
    <tr><td style='text-align: center;'>25.7</td><td style='text-align: center;'>260.0</td></tr>
    <tr><td style='text-align: center;'>25.8</td><td style='text-align: center;'>261.0</td></tr>
    <tr><td style='text-align: center;'>25.9</td><td style='text-align: center;'>262.0</td></tr>
    <tr><td style='text-align: center;'>26.0</td><td style='text-align: center;'>263.0</td></tr>
    <tr><td style='text-align: center;'>26.1</td><td style='text-align: center;'>264.0</td></tr>
    <tr><td style='text-align: center;'>26.2</td><td style='text-align: center;'>265.0</td></tr>
    <tr><td style='text-align: center;'>26.3</td><td style='text-align: center;'>266.0</td></tr>
    <tr><td style='text-align: center;'>26.4</td><td style='text-align: center;'>267.0</td></tr>
    <tr><td style='text-align: center;'>26.5</td><td style='text-align: center;'>268.0</td></tr>
    <tr><td style='text-align: center;'>26.6</td><td style='text-align: center;'>269.0</td></tr>
    <tr><td style='text-align: center;'>26.7</td><td style='text-align: center;'>270.0</td></tr>
    <tr><td style='text-align: center;'>26.8</td><td style='text-align: center;'>271.0</td></tr>
    <tr><td style='text-align: center;'>26.9</td><td style='text-align: center;'>272.0</td></tr>
    <tr><td style='text-align: center;'>27.0</td><td style='text-align: center;'>273.0</td></tr>
    <tr><td style='text-align: center;'>27.1</td><td style='text-align: center;'>274.0</td></tr>
    <tr><td style='text-align: center;'>27.2</td><td style='text-align: center;'>275.0</td></tr>
    <tr><td style='text-align: center;'>27.3</td><td style='text-align: center;'>276.0</td></tr>
    <tr><td style='text-align: center;'>27.4</td><td style='text-align: center;'>277.0</td></tr>
    <tr><td style='text-align: center;'>27.5</td><td style='text-align: center;'>278.0</td></tr>
    <tr><td style='text-align: center;'>27.6</td><td style='text-align: center;'>279.0</td></tr>
    <tr><td style='text-align: center;'>27.7</td><td style='text-align: center;'>280.0</td></tr>
    <tr><td style='text-align: center;'>27.8</td><td style='text-align: center;'>281.0</td></tr>
    <tr><td style='text-align: center;'>27.9</td><td style='text-align: center;'>282.0</td></tr>
    <tr><td style='text-align: center;'>28.0</td><td style='text-align: center;'>283.0</td></tr>
    <tr><td style='text-align: center;'>28.1</td><td style='text-align: center;'>284.0</td></tr>
    <tr><td style='text-align: center;'>28.2</td><td style='text-align: center;'>285.0</td></tr>
    <tr><td style='text-align: center;'>28.3</td><td style='text-align: center;'>286.0</td></tr>
    <tr><td style='text-align: center;'>28.4</td><td style='text-align: center;'>287.0</td></tr>
    <tr><td style='text-align: center;'>28.5</td><td style='text-align: center;'>288.0</td></tr>
    <tr><td style='text-align: center;'>28.6</td><td style='text-align: center;'>289.0</td></tr>
    <tr><td style='text-align: center;'>28.7</td><td style='text-align: center;'>290.0</td></tr>
    <tr><td style='text-align: center;'>28.8</td><td style='text-align: center;'>291.0</td></tr>
    <tr><td style='text-align: center;'>28.9</td><td style='text-align: center;'>292.0</td></tr>
    <tr><td style='text-align: center;'>29.0</td><td style='text-align: center;'>293.0</td></tr>
    <tr><td style='text-align: center;'>29.1</td><td style='text-align: center;'>294.0</td></tr>
    <tr><td style='text-align: center;'>29.2</td><td style='text-align: center;'>295.0</td></tr>
    <tr><td style='text-align: center;'>29.3</td><td style='text-align: center;'>296.0</td></tr>
    <tr><td style='text-align: center;'>29.4</td><td style='text-align: center;'>297.0</td></tr>
    <tr><td style='text-align: center;'>29.5</td><td style='text-align: center;'>298.0</td></tr>
    <tr><td style='text-align: center;'>29.6</td><td style='text-align: center;'>299.0</td></tr>
    <tr><td style='text-align: center;'>29.7</td><td style='text-align: center;'>300.0</td></tr>
    <tr><td style='text-align: center;'>29.8</td><td style='text-align: center;'>301.0</td></tr>
    <tr><td style='text-align: center;'>29.9</td><td style='text-align: center;'>302.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>303.0</td></tr>
    <tr><td style='text-align: center;'>30.1</td><td style='text-align: center;'>304.0</td></tr>
    <tr><td style='text-align: center;'>30.2</td><td style='text-align: center;'>305.0</td></tr>
    <tr><td style='text-align: center;'>30.3</td><td style='text-align: center;'>306.0</td></tr>
    <tr><td style='text-align: center;'>30.4</td><td style='text-align: center;'>307.0</td></tr>
    <tr><td style='text-align: center;'>30.5</td><td style='text-align: center;'>308.0</td></tr>
    <tr><td style='text-align: center;'>30.6</td><td style='text-align: center;'>309.0</td></tr>
    <tr><td style='text-align: center;'>30.7</td><td style='text-align: center;'>310.0</td></tr>
    <tr><td style='text-align: center;'>30.8</td><td style='text-align: center;'>311.0</td></tr>
    <tr><td style='text-align: center;'>30.9</td><td style='text-align: center;'>312.0</td></tr>
    <tr><td style='text-align: center;'>31.0</td><td style='text-align: center;'>313.0</td></tr>
    <tr><td style='text-align: center;'>31.1</td><td style='text-align: center;'>314.0</td></tr>
    <tr><td style='text-align: center;'>31.2</td><td style='text-align: center;'>315.0</td></tr>
    <tr><td style='text-align: center;'>31.3</td><td style='text-align: center;'>316.0</td></tr>
    <tr><td style='text-align: center;'>31.4</td><td style='text-align: center;'>317.0</td></tr>
    <tr><td style='text-align: center;'>31.5</td><td style='text-align: center;'>318.0</td></tr>
    <tr><td style='text-align: center;'>31.6</td><td style='text-align: center;'>319.0</td></tr>
    <tr><td style='text-align: center;'>31.7</td><td style='text-align: center;'>320.0</td></tr>
    <tr><td style='text-align: center;'>31.8</td><td style='text-align: center;'>321.0</td></tr>
    <tr><td style='text-align: center;'>31.9</td><td style='text-align: center;'>322.0</td></tr>
    <tr><td style='text-align: center;'>32.0</td><td style='text-align: center;'>323.0</td></tr>
    <tr><td style='text-align: center;'>32.1</td><td style='text-align: center;'>324.0</td></tr>
    <tr><td style='text-align: center;'>32.2</td><td style='text-align: center;'>325.0</td></tr>
    <tr><td style='text-align: center;'>32.3</td><td style='text-align: center;'>326.0</td></tr>
    <tr><td style='text-align: center;'>32.4</td><td style='text-align: center;'>327.0</td></tr>
    <tr><td style='text-align: center;'>32.5</td><td style='text-align: center;'>328.0</td></tr>
    <tr><td style='text-align: center;'>32.6</td><td style='text-align: center;'>329.0</td></tr>
    <tr><td style='text-align: center;'>32.7</td><td style='text-align: center;'>330.0</td></tr>
    <tr><td style='text-align: center;'>32.8</td><td style='text-align: center;'>331.0</td></tr>
    <tr><td style='text-align: center;'>32.9</td><td style='text-align: center;'>332.0</td></tr>
    <tr><td style='text-align: center;'>33.0</td><td style='text-align: center;'>333.0</td></tr>
    <tr><td style='text-align: center;'>33.1</td><td style='text-align: center;'>334.0</td></tr>
    <tr><td style='text-align: center;'>33.2</td><td style='text-align: center;'>335.0</td></tr>
    <tr><td style='text-align: center;'>33.3</td><td style='text-align: center;'>336.0</td></tr>
    <tr><td style='text-align: center;'>33.4</td><td style='text-align: center;'>337.0</td></tr>
    <tr><td style='text-align: center;'>33.5</td><td style='text-align: center;'>338.0</td></tr>
    <tr><td style='text-align: center;'>33.6</td><td style='text-align: center;'>339.0</td></tr>
    <tr><td style='text-align: center;'>33.7</td><td style='text-align: center;'>340.0</td></tr>
    <tr><td style='text-align: center;'>33.8</td><td style='text-align: center;'>341.0</td></tr>
    <tr><td style='text-align: center;'>33.9</td><td style='text-align: center;'>342.0</td></tr>
    <tr><td style='text-align: center;'>34.0</td><td style='text-align: center;'>343.0</td></tr>
    <tr><td style='text-align: center;'>34.1</td><td style='text-align: center;'>344.0</td></tr>
    <tr><td style='text-align: center;'>34.2</td><td style='text-align: center;'>345.0</td></tr>
    <tr><td style='text-align: center;'>34.3</td><td style='text-align: center;'>346.0</td></tr>
    <tr><td style='text-align: center;'>34.4</td><td style='text-align: center;'>347.0</td></tr>
    <tr><td style='text-align: center;'>34.5</td><td style='text-align: center;'>348.0</td></tr>
    <tr><td style='text-align: center;'>34.6</td><td style='text-align: center;'>349.0</td></tr>
    <tr><td style='text-align: center;'>34.7</td><td style='text-align: center;'>350.0</td></tr>
    <tr><td style='text-align: center;'>34.8</td><td style='text-align: center;'>351.0</td></tr>
    <tr><td style='text-align: center;'>34.9</td><td style='text-align: center;'>352.0</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>353.0</td></tr>
    <tr><td style='text-align: center;'>35.1</td><td style='text-align: center;'>354.0</td></tr>
    <tr><td style='text-align: center;'>35.2</td><td style='text-align: center;'>355.0</td></tr>
    <tr><td style='text-align: center;'>35.3</td><td style='text-align: center;'>356.0</td></tr>
    <tr><td style='text-align: center;'>35.4</td><td style='text-align: center;'>357.0</td></tr>
    <tr><td style='text-align: center;'>35.5</td><td style='text-align: center;'>358.</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.46 The Obs versus Pred plot with four principal components.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Label</th><th style='text-align: center;'>T[1]</th><th style='text-align: center;'>T[2]</th><th style='text-align: center;'>W* [c1] [1] [1] [2] [1] [</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.47 Loading bi-plot.</div>


Additionally, quality variable, MI Plant, in red, is positively correlated with process variables H2, H2/C2, and CAT in black (since they lie closer to each other). We can confirm this strong correlation by selecting the VIP button on the left-side pane to generate a variable importance to projection plot (VIP) in Figure 9.48.

---

<!-- PDF page 602 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Variable</th><th style='text-align: center;'>VIP [4 comp.]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>H2/C2</td><td style='text-align: center;'>1.42</td></tr>
    <tr><td style='text-align: center;'>H2</td><td style='text-align: center;'>1.36</td></tr>
    <tr><td style='text-align: center;'>CAT</td><td style='text-align: center;'>1.28</td></tr>
    <tr><td style='text-align: center;'>P</td><td style='text-align: center;'>1.00</td></tr>
    <tr><td style='text-align: center;'>C3/CH</td><td style='text-align: center;'>0.76</td></tr>
    <tr><td style='text-align: center;'>C3</td><td style='text-align: center;'>0.74</td></tr>
    <tr><td style='text-align: center;'>Q1</td><td style='text-align: center;'>0.69</td></tr>
    <tr><td style='text-align: center;'>HX</td><td style='text-align: center;'>0.66</td></tr>
    <tr><td style='text-align: center;'>T</td><td style='text-align: center;'>0.60</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.48 Variable importance to projection, VIP plot.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Observation Number</th><th style='text-align: center;'>Model 1 - Hotelling's T2 Plot - Training</th><th style='text-align: center;'>Model 1 - Hotelling's T2 Plot - Testing</th><th style='text-align: center;'>Model 2 - Heterogeneity</th><th style='text-align: center;'>Model 2 - Heterogeneity</th><th style='text-align: center;'>Model 2 - Coefficient</th><th style='text-align: center;'>Model 2 - Coefficient</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>29.0</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.49 The Hotelling's plot and the menu to display observation number, "Display Point Tooltips." The data points within the red circle represent potential outliers outside the 95% confidence limit.</div>


## (4) Hotelling's  $ T^{2} $ plot

Following Figure 9.26, we show the Hotelling's  $ T^{2} $ plot in Figure 9.49 and want to demonstrate new tools to identify the cause of a selected outlier in our dataset. We right-click within the plot to show the menu to display observation number. We click on “Display Point Tooltips” and then put the mouse on one of the outliers. We see in Figure 9.50 the observation number as 2697.

How do we identify the cause of data number 2697 as an outlier? We use the contribution plot below.

---

<!-- PDF page 603 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>HT2[=4]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>2500</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>2600</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2700</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>2800</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2900</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>3000</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>3100</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>3200</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>3300</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>3400</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>3500</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>3600</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>3700</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>3800</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>3900</td><td style='text-align: center;'>5.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.50 Displaying data number 2697 for an outlier located on the far right, top data point.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_136_591_666_967.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 9.51 Specifying a contribution plot from average to data point 2697.</div>


## (5) Contribution plot

We follow the path: Analyze → Contributions → Specify according to Figure 9.51 → Contribution plot of Figure 9.52.

Next, we start a new project and import the data file, HDPX_XY_Data.xlsx, again. We then follow Figures 9.15–9.16 and Figure 9.34 to remove observation

---

<!-- PDF page 604 -->

## Model 1 - Contributions to Scores for X-Space

<div style="text-align: center;"><img src="imgs/img_in_image_box_554_151_695_180.jpg" alt="Image" width="14%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Variable</th><th style='text-align: center;'>Contribution</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>C2</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>H2</td><td style='text-align: center;'>-0.8</td></tr>
    <tr><td style='text-align: center;'>CAT</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>HX</td><td style='text-align: center;'>2.8</td></tr>
    <tr><td style='text-align: center;'>C3</td><td style='text-align: center;'>-0.5</td></tr>
    <tr><td style='text-align: center;'>T</td><td style='text-align: center;'>-11.5</td></tr>
    <tr><td style='text-align: center;'>P</td><td style='text-align: center;'>-3.2</td></tr>
    <tr><td style='text-align: center;'>H2/C2</td><td style='text-align: center;'>-3.8</td></tr>
    <tr><td style='text-align: center;'>C3/C4</td><td style='text-align: center;'>-0.2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.52 Contribution plot indicating temperature of data point 2697 being much lower than the average value, causing an outlier in the Hotelling's  $ T^{2} $ plot.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th><th style='text-align: center;'>R2 Cumulative Error</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.02</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Predicted [4 comp.]</th><th style='text-align: center;'>Observed</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>16.0</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>19.0</td></tr>
    <tr><td style='text-align: center;'>8.5</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>21.0</td></tr>
    <tr><td style='text-align: center;'>9.5</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>24.0</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>26.0</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>30.0</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>31.0</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>32.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>33.0</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>34.0</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>36.0</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>37.0</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>38.0</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>39.0</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>40.0</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>41.0</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>42.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>43.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.53 The R2–Q2 plot and Obs versus Pred Plot after removing potential outliers.</div>


IDs 2412–2415 and 2695–2698 (potential outliers highlighted within the red circle in Figure 9.49), and save the resulting model file as WS9.3-1_PLS-XY.pmvx. Following the path: Model→Active Model→Auto Fit, we generate the model resulting from removing observation IDs 2412–2415 and 2695–2698. Figure 9.53 shows the corresponding R2-Q2 plot and the Obs versus Pred plot.

Comparing Figures 9.46 and 9.53, we find the change in R2 from 0.953395 to 0.9534 and RMSE from 1.08266 to 1.08267 quite insignificant. Therefore, we can stay

---

<!-- PDF page 605 -->

with the original model. This concludes workshop WS9.2_PLS-XY, and we save the file as WS9.2_PLS-XY.pmvx.

#### 9.5 Workshop 9.4: Polymer Melt Index Prediction and Causal Analysis with Measurement Time Lags Using PLS

#### 9.5.1 Introduction to PLS with Measurement Time Lags

In many chemical processes, there is some lag between the time when the quality variable, like MI, at the process outlet is measured and the process variable measurements. The output of a dynamic process is related to the past process variable inputs and past outputs as well. To handle the autocorrelation data, we mimic the concept of auto-regressive moving average exogenous (ARMAX) time series models by forming the data matrix with previous observation in each observation vector. The time series model relates quality (dependent) variable y at present time to past quality variable y's and process (independent) variable x's.

The model equation is represented below:

 $$ y_{t}=\beta_{1}y_{t-1}+\beta_{2}y_{t-2}+\cdots+\gamma_{1}x_{t-1}+\gamma_{2}x_{t-2}+e_{t} $$ 

This eventually means that we need to use a lagged value of the quality variable to account for the time lags. Thus, we consider the autocorrelation in the data in ProMV by introduction of the lag of variable order. This time series-modeling technique is also referred to as PLS with observation time lags. When applied the technique to batch processes with time lags, Chen and Liu [21] refer the method as batch dynamic partial least squares (BDPLS).

When a quality (Y) variable in a PLS model contains measurement time lags, we introduce a lagged quality variable to the Y block to which it belongs. Following Aspen ProMV online help, we show in Figure 9.54 an example of a Y data block with a single quality variable that is lagged three time units. In the figure, we add three lagged quality variables. The resulting quality data block with lags (called LagsY block) now has three more variables due to time lags but three fewer observations. We define a lagged variable with the original name with the suffix _L#, where # represents the lag value for that particular value.

In the following, we demonstrate how to apply PLS with observation time lags using Aspen ProMV.

<div style="text-align: center;">Figure 9.54 An illustration of a single quality variable that is lagged three time units.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_424_1071_800_1265.jpg" alt="Image" width="39%" /></div>


---

<!-- PDF page 606 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_148_811_386.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 9.55 The “Lags” button in the New Model screen.</div>


##### 9.5.2 Workshop 9.4: Application of Aspen ProMV to Polymer Melt Index Prediction and Causal Analysis with Measurement Time Lags Using PLS

We use the same industrial HDPE process in Workshop 9.3 in Section 9.4.2 and the same industrial dataset, HDPE_XY_Data.xlsx.

We load the data using the same procedure. In this case, we introduce a lag of order 1 in both the input process variables and the process output MI, so that the MI at the current time is function of the historical value of process variables and past MI value.

We follow the steps from Figures 9.12–9.18 but import both process and quality variable data (X and Y spaces) as in Figure 9.32 and save the file as WS9.4_PLS-X and LagsY.pmvx. On the New Model screen, we pay attention to the “Lags” button. See Figure 9.55.

Referring to Figure 9.56, we choose quality variable, Plant MI, specify a lag of 1 time unit, and use the arrow key to move the data to the LagsY block on the right. We then save the model file as WS9.4_PLS-X and LagsY.pmvx.

We build a PLS model following the path: Model→Active Model→Auto Fit (Figure 9.20) and see the resulting PLS model with time lag in Figure 9.57. An R2 value of 0.9938 says that the PLS model with time lag can explain 99.38% of the variability of the quality variable, Plant MI (melt index); a Q2 value of 0.9938 says that with cross-validation, the model can explain 99.38% of the data variability. From Figure 9.45, we see that the corresponding R2 and Q2 values without time lag are 0.9534 and 0.9533, respectively. This comparison shows that by introducing the time lag, both R2 and Q2 values increase significantly when compared to those values without time lag.

Following Figures 9.40 and 9.46, we generate an Obs versus Pred plot in Figure 9.58. It is significant to note that by adding a time lag, the PLS model significantly lowers the RMSEE value from 1.08266 without time lag (Figure 9.46) to 0.393567 with time lag (Figure 9.58).

---

<!-- PDF page 607 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_138_148_781_524.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 9.56 Specifying a lag of one time-unit for the quality variable, MI Plant. The new variable is named MI Plant_L1.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 (Q2 Cumulative)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summi</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summi</td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summi</td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summi</td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>A</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>B</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>C</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>Training</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>Num.</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>0.85867164...</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>Q2 Cumula...</td><td style='text-align: center;'>0.85867160...</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>0.93661048...</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>0.97220351...</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>0.99383270...</td></tr>
    <tr><td style='text-align: center;'>Model Summary for Y-Space - PLS-X and LagsYpmvx</td><td style='text-align: center;'>R2 Cumula...</td><td style='text-align: center;'>0.99381995...</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.57 R2 and Q2 values of PLS for Y-space with time lag with four principal components resulting from auto-fit.</div>


Figure 9.59 shows a VIP plot for the PLS model with time lag. By comparing this plot with the corresponding VIP plot without time lag, Figure 9.48, we see that the lagged quality variable, Plant MI, becomes the most important variable for the PLS model with time lag.

Thus, we can actually use the data from PLS model and separately plot the results with the actual plant data. Figure 9.59 demonstrates that predictions from a PLS model with measurement time lag compare well with the time-dependent plant MI data.

This concludes our Workshop 9.4, and we save the resulting simulation file as WS9.4_PLS-X and LagsY.pmvx.

---

<!-- PDF page 608 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Predicted [4 comp.]</th><th style='text-align: center;'>Observed</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>16.0</td></tr>
    <tr><td style='text-align: center;'>8.5</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>9.5</td><td style='text-align: center;'>19.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>21.0</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>24.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>26.0</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>30.0</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>31.0</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>32.0</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>33.0</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>34.0</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>36.0</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>37.0</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>38.0</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>39.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>40.0</td></tr>
    <tr><td style='text-align: center;'>20.5</td><td style='text-align: center;'>41.0</td></tr>
    <tr><td style='text-align: center;'>21.0</td><td style='text-align: center;'>42.0</td></tr>
    <tr><td style='text-align: center;'>21.5</td><td style='text-align: center;'>43.0</td></tr>
    <tr><td style='text-align: center;'>22.0</td><td style='text-align: center;'>44.0</td></tr>
    <tr><td style='text-align: center;'>22.5</td><td style='text-align: center;'>45.0</td></tr>
    <tr><td style='text-align: center;'>23.0</td><td style='text-align: center;'>46.0</td></tr>
    <tr><td style='text-align: center;'>23.5</td><td style='text-align: center;'>47.0</td></tr>
    <tr><td style='text-align: center;'>24.0</td><td style='text-align: center;'>48.0</td></tr>
    <tr><td style='text-align: center;'>24.5</td><td style='text-align: center;'>49.0</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>50.0</td></tr>
    <tr><td style='text-align: center;'>25.5</td><td style='text-align: center;'>51.0</td></tr>
    <tr><td style='text-align: center;'>26.0</td><td style='text-align: center;'>52.0</td></tr>
    <tr><td style='text-align: center;'>26.5</td><td style='text-align: center;'>53.0</td></tr>
    <tr><td style='text-align: center;'>27.0</td><td style='text-align: center;'>54.0</td></tr>
    <tr><td style='text-align: center;'>27.5</td><td style='text-align: center;'>55.0</td></tr>
    <tr><td style='text-align: center;'>28.0</td><td style='text-align: center;'>56.0</td></tr>
    <tr><td style='text-align: center;'>28.5</td><td style='text-align: center;'>57.0</td></tr>
    <tr><td style='text-align: center;'>29.0</td><td style='text-align: center;'>58.0</td></tr>
    <tr><td style='text-align: center;'>29.5</td><td style='text-align: center;'>59.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>60.0</td></tr>
    <tr><td style='text-align: center;'>30.5</td><td style='text-align: center;'>61.0</td></tr>
    <tr><td style='text-align: center;'>31.0</td><td style='text-align: center;'>62.0</td></tr>
    <tr><td style='text-align: center;'>31.5</td><td style='text-align: center;'>63.0</td></tr>
    <tr><td style='text-align: center;'>32.0</td><td style='text-align: center;'>64.0</td></tr>
    <tr><td style='text-align: center;'>32.5</td><td style='text-align: center;'>65.0</td></tr>
    <tr><td style='text-align: center;'>33.0</td><td style='text-align: center;'>66.0</td></tr>
    <tr><td style='text-align: center;'>33.5</td><td style='text-align: center;'>67.0</td></tr>
    <tr><td style='text-align: center;'>34.0</td><td style='text-align: center;'>68.0</td></tr>
    <tr><td style='text-align: center;'>34.5</td><td style='text-align: center;'>69.0</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>70.0</td></tr>
    <tr><td style='text-align: center;'>35.5</td><td style='text-align: center;'>71.0</td></tr>
    <tr><td style='text-align: center;'>36.0</td><td style='text-align: center;'>72.0</td></tr>
    <tr><td style='text-align: center;'>36.5</td><td style='text-align: center;'>73.0</td></tr>
    <tr><td style='text-align: center;'>37.0</td><td style='text-align: center;'>74.0</td></tr>
    <tr><td style='text-align: center;'>37.5</td><td style='text-align: center;'>75.0</td></tr>
    <tr><td style='text-align: center;'>38.0</td><td style='text-align: center;'>76.0</td></tr>
    <tr><td style='text-align: center;'>38.5</td><td style='text-align: center;'>77.0</td></tr>
    <tr><td style='text-align: center;'>39.0</td><td style='text-align: center;'>78.0</td></tr>
    <tr><td style='text-align: center;'>39.5</td><td style='text-align: center;'>79.0</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>80.0</td></tr>
    <tr><td style='text-align: center;'>40.5</td><td style='text-align: center;'>81.0</td></tr>
    <tr><td style='text-align: center;'>41.0</td><td style='text-align: center;'>82.0</td></tr>
    <tr><td style='text-align: center;'>41.5</td><td style='text-align: center;'>83.0</td></tr>
    <tr><td style='text-align: center;'>42.0</td><td style='text-align: center;'>84.0</td></tr>
    <tr><td style='text-align: center;'>42.5</td><td style='text-align: center;'>85.0</td></tr>
    <tr><td style='text-align: center;'>43.0</td><td style='text-align: center;'>86.0</td></tr>
    <tr><td style='text-align: center;'>43.5</td><td style='text-align: center;'>87.0</td></tr>
    <tr><td style='text-align: center;'>44.0</td><td style='text-align: center;'>88.0</td></tr>
    <tr><td style='text-align: center;'>44.5</td><td style='text-align: center;'>89.0</td></tr>
    <tr><td style='text-align: center;'>45.0</td><td style='text-align: center;'>90.0</td></tr>
    <tr><td style='text-align: center;'>45.5</td><td style='text-align: center;'>91.0</td></tr>
    <tr><td style='text-align: center;'>46.0</td><td style='text-align: center;'>92.0</td></tr>
    <tr><td style='text-align: center;'>46.5</td><td style='text-align: center;'>93.0</td></tr>
    <tr><td style='text-align: center;'>47.0</td><td style='text-align: center;'>94.0</td></tr>
    <tr><td style='text-align: center;'>47.5</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>48.0</td><td style='text-align: center;'>96.0</td></tr>
    <tr><td style='text-align: center;'>48.5</td><td style='text-align: center;'>97.0</td></tr>
    <tr><td style='text-align: center;'>49.0</td><td style='text-align: center;'>98.0</td></tr>
    <tr><td style='text-align: center;'>49.5</td><td style='text-align: center;'>99.0</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>50.5</td><td style='text-align: center;'>101.0</td></tr>
    <tr><td style='text-align: center;'>51.0</td><td style='text-align: center;'>102.0</td></tr>
    <tr><td style='text-align: center;'>51.5</td><td style='text-align: center;'>103.0</td></tr>
    <tr><td style='text-align: center;'>52.0</td><td style='text-align: center;'>104.0</td></tr>
    <tr><td style='text-align: center;'>52.5</td><td style='text-align: center;'>105.0</td></tr>
    <tr><td style='text-align: center;'>53.0</td><td style='text-align: center;'>106.0</td></tr>
    <tr><td style='text-align: center;'>53.5</td><td style='text-align: center;'>107.0</td></tr>
    <tr><td style='text-align: center;'>54.0</td><td style='text-align: center;'>108.0</td></tr>
    <tr><td style='text-align: center;'>54.5</td><td style='text-align: center;'>109.0</td></tr>
    <tr><td style='text-align: center;'>55.0</td><td style='text-align: center;'>110.0</td></tr>
    <tr><td style='text-align: center;'>55.5</td><td style='text-align: center;'>111.0</td></tr>
    <tr><td style='text-align: center;'>56.0</td><td style='text-align: center;'>112.0</td></tr>
    <tr><td style='text-align: center;'>56.5</td><td style='text-align: center;'>113.0</td></tr>
    <tr><td style='text-align: center;'>57.0</td><td style='text-align: center;'>114.0</td></tr>
    <tr><td style='text-align: center;'>57.5</td><td style='text-align: center;'>115.0</td></tr>
    <tr><td style='text-align: center;'>58.0</td><td style='text-align: center;'>116.0</td></tr>
    <tr><td style='text-align: center;'>58.5</td><td style='text-align: center;'>117.0</td></tr>
    <tr><td style='text-align: center;'>59.0</td><td style='text-align: center;'>118.0</td></tr>
    <tr><td style='text-align: center;'>59.5</td><td style='text-align: center;'>119.0</td></tr>
    <tr><td style='text-align: center;'>60.0</td><td style='text-align: center;'>120.0</td></tr>
    <tr><td style='text-align: center;'>60.5</td><td style='text-align: center;'>121.0</td></tr>
    <tr><td style='text-align: center;'>61.0</td><td style='text-align: center;'>122.0</td></tr>
    <tr><td style='text-align: center;'>61.5</td><td style='text-align: center;'>123.0</td></tr>
    <tr><td style='text-align: center;'>62.0</td><td style='text-align: center;'>124.0</td></tr>
    <tr><td style='text-align: center;'>62.5</td><td style='text-align: center;'>125.0</td></tr>
    <tr><td style='text-align: center;'>63.0</td><td style='text-align: center;'>126.0</td></tr>
    <tr><td style='text-align: center;'>63.5</td><td style='text-align: center;'>127.0</td></tr>
    <tr><td style='text-align: center;'>64.0</td><td style='text-align: center;'>128.0</td></tr>
    <tr><td style='text-align: center;'>64.5</td><td style='text-align: center;'>129.0</td></tr>
    <tr><td style='text-align: center;'>65.0</td><td style='text-align: center;'>130.0</td></tr>
    <tr><td style='text-align: center;'>65.5</td><td style='text-align: center;'>131.0</td></tr>
    <tr><td style='text-align: center;'>66.0</td><td style='text-align: center;'>132.0</td></tr>
    <tr><td style='text-align: center;'>66.5</td><td style='text-align: center;'>133.0</td></tr>
    <tr><td style='text-align: center;'>67.0</td><td style='text-align: center;'>134.0</td></tr>
    <tr><td style='text-align: center;'>67.5</td><td style='text-align: center;'>135.0</td></tr>
    <tr><td style='text-align: center;'>68.0</td><td style='text-align: center;'>136.0</td></tr>
    <tr><td style='text-align: center;'>68.5</td><td style='text-align: center;'>137.0</td></tr>
    <tr><td style='text-align: center;'>69.0</td><td style='text-align: center;'>138.0</td></tr>
    <tr><td style='text-align: center;'>69.5</td><td style='text-align: center;'>139.0</td></tr>
    <tr><td style='text-align: center;'>70.0</td><td style='text-align: center;'>140.0</td></tr>
    <tr><td style='text-align: center;'>70.5</td><td style='text-align: center;'>141.0</td></tr>
    <tr><td style='text-align: center;'>71.0</td><td style='text-align: center;'>142.0</td></tr>
    <tr><td style='text-align: center;'>71.5</td><td style='text-align: center;'>143.0</td></tr>
    <tr><td style='text-align: center;'>72.0</td><td style='text-align: center;'>144.0</td></tr>
    <tr><td style='text-align: center;'>72.5</td><td style='text-align: center;'>145.0</td></tr>
    <tr><td style='text-align: center;'>73.0</td><td style='text-align: center;'>146.0</td></tr>
    <tr><td style='text-align: center;'>73.5</td><td style='text-align: center;'>147.0</td></tr>
    <tr><td style='text-align: center;'>74.0</td><td style='text-align: center;'>148.0</td></tr>
    <tr><td style='text-align: center;'>74.5</td><td style='text-align: center;'>149.0</td></tr>
    <tr><td style='text-align: center;'>75.0</td><td style='text-align: center;'>150.0</td></tr>
    <tr><td style='text-align: center;'>75.5</td><td style='text-align: center;'>151.0</td></tr>
    <tr><td style='text-align: center;'>76.0</td><td style='text-align: center;'>152.0</td></tr>
    <tr><td style='text-align: center;'>76.5</td><td style='text-align: center;'>153.0</td></tr>
    <tr><td style='text-align: center;'>77.0</td><td style='text-align: center;'>154.0</td></tr>
    <tr><td style='text-align: center;'>77.5</td><td style='text-align: center;'>155.0</td></tr>
    <tr><td style='text-align: center;'>78.0</td><td style='text-align: center;'>156.0</td></tr>
    <tr><td style='text-align: center;'>78.5</td><td style='text-align: center;'>157.0</td></tr>
    <tr><td style='text-align: center;'>79.0</td><td style='text-align: center;'>158.0</td></tr>
    <tr><td style='text-align: center;'>79.5</td><td style='text-align: center;'>159.0</td></tr>
    <tr><td style='text-align: center;'>80.0</td><td style='text-align: center;'>160.0</td></tr>
    <tr><td style='text-align: center;'>80.5</td><td style='text-align: center;'>161.0</td></tr>
    <tr><td style='text-align: center;'>81.0</td><td style='text-align: center;'>162.0</td></tr>
    <tr><td style='text-align: center;'>81.5</td><td style='text-align: center;'>163.0</td></tr>
    <tr><td style='text-align: center;'>82.0</td><td style='text-align: center;'>164.0</td></tr>
    <tr><td style='text-align: center;'>82.5</td><td style='text-align: center;'>165.0</td></tr>
    <tr><td style='text-align: center;'>83.0</td><td style='text-align: center;'>166.0</td></tr>
    <tr><td style='text-align: center;'>83.5</td><td style='text-align: center;'>167.0</td></tr>
    <tr><td style='text-align: center;'>84.0</td><td style='text-align: center;'>168.0</td></tr>
    <tr><td style='text-align: center;'>84.5</td><td style='text-align: center;'>169.0</td></tr>
    <tr><td style='text-align: center;'>85.0</td><td style='text-align: center;'>170.0</td></tr>
    <tr><td style='text-align: center;'>85.5</td><td style='text-align: center;'>171.0</td></tr>
    <tr><td style='text-align: center;'>86.0</td><td style='text-align: center;'>172.0</td></tr>
    <tr><td style='text-align: center;'>86.5</td><td style='text-align: center;'>173.0</td></tr>
    <tr><td style='text-align: center;'>87.0</td><td style='text-align: center;'>174.0</td></tr>
    <tr><td style='text-align: center;'>87.5</td><td style='text-align: center;'>175.0</td></tr>
    <tr><td style='text-align: center;'>88.0</td><td style='text-align: center;'>176.0</td></tr>
    <tr><td style='text-align: center;'>88.5</td><td style='text-align: center;'>177.0</td></tr>
    <tr><td style='text-align: center;'>89.0</td><td style='text-align: center;'>178.0</td></tr>
    <tr><td style='text-align: center;'>89.5</td><td style='text-align: center;'>179.0</td></tr>
    <tr><td style='text-align: center;'>90.0</td><td style='text-align: center;'>180.0</td></tr>
    <tr><td style='text-align: center;'>90.5</td><td style='text-align: center;'>181.0</td></tr>
    <tr><td style='text-align: center;'>91.0</td><td style='text-align: center;'>182.0</td></tr>
    <tr><td style='text-align: center;'>91.5</td><td style='text-align: center;'>183.0</td></tr>
    <tr><td style='text-align: center;'>92.0</td><td style='text-align: center;'>184.0</td></tr>
    <tr><td style='text-align: center;'>92.5</td><td style='text-align: center;'>185.0</td></tr>
    <tr><td style='text-align: center;'>93.0</td><td style='text-align: center;'>186.0</td></tr>
    <tr><td style='text-align: center;'>93.5</td><td style='text-align: center;'>187.0</td></tr>
    <tr><td style='text-align: center;'>94.0</td><td style='text-align: center;'>188.0</td></tr>
    <tr><td style='text-align: center;'>94.5</td><td style='text-align: center;'>189.0</td></tr>
    <tr><td style='text-align: center;'>95.0</td><td style='text-align: center;'>190.0</td></tr>
    <tr><td style='text-align: center;'>95.5</td><td style='text-align: center;'>191.0</td></tr>
    <tr><td style='text-align: center;'>96.0</td><td style='text-align: center;'>192.0</td></tr>
    <tr><td style='text-align: center;'>96.5</td><td style='text-align: center;'>193.0</td></tr>
    <tr><td style='text-align: center;'>97.0</td><td style='text-align: center;'>194.0</td></tr>
    <tr><td style='text-align: center;'>97.5</td><td style='text-align: center;'>195.0</td></tr>
    <tr><td style='text-align: center;'>98.0</td><td style='text-align: center;'>196.0</td></tr>
    <tr><td style='text-align: center;'>98.5</td><td style='text-align: center;'>197.0</td></tr>
    <tr><td style='text-align: center;'>99.0</td><td style='text-align: center;'>198.0</td></tr>
    <tr><td style='text-align: center;'>99.5</td><td style='text-align: center;'>199.0</td></tr>
    <tr><td style='text-align: center;'>100.0</td><td style='text-align: center;'>200.0</td></tr>
    <tr><td style='text-align: center;'>100.5</td><td style='text-align: center;'>201.0</td></tr>
    <tr><td style='text-align: center;'>101.0</td><td style='text-align: center;'>202.0</td></tr>
    <tr><td style='text-align: center;'>101.5</td><td style='text-align: center;'>203.0</td></tr>
    <tr><td style='text-align: center;'>102.0</td><td style='text-align: center;'>204.0</td></tr>
    <tr><td style='text-align: center;'>102.5</td><td style='text-align: center;'>205.0</td></tr>
    <tr><td style='text-align: center;'>103.0</td><td style='text-align: center;'>206.0</td></tr>
    <tr><td style='text-align: center;'>103.5</td><td style='text-align: center;'>207.0</td></tr>
    <tr><td style='text-align: center;'>104.0</td><td style='text-align: center;'>208.0</td></tr>
    <tr><td style='text-align: center;'>104.5</td><td style='text-align: center;'>209.0</td></tr>
    <tr><td style='text-align: center;'>105.0</td><td style='text-align: center;'>210.0</td></tr>
    <tr><td style='text-align: center;'>105.5</td><td style='text-align: center;'>211.0</td></tr>
    <tr><td style='text-align: center;'>106.0</td><td style='text-align: center;'>212.0</td></tr>
    <tr><td style='text-align: center;'>106.5</td><td style='text-align: center;'>213.0</td></tr>
    <tr><td style='text-align: center;'>107.0</td><td style='text-align: center;'>214.0</td></tr>
    <tr><td style='text-align: center;'>107.5</td><td style='text-align: center;'>215.0</td></tr>
    <tr><td style='text-align: center;'>108.0</td><td style='text-align: center;'>216.0</td></tr>
    <tr><td style='text-align: center;'>108.5</td><td style='text-align: center;'>217.0</td></tr>
    <tr><td style='text-align: center;'>109.0</td><td style='text-align: center;'>218.0</td></tr>
    <tr><td style='text-align: center;'>109.5</td><td style='text-align: center;'>219.0</td></tr>
    <tr><td style='text-align: center;'>110.0</td><td style='text-align: center;'>220.0</td></tr>
    <tr><td style='text-align: center;'>110.5</td><td style='text-align: center;'>221.0</td></tr>
    <tr><td style='text-align: center;'>111.0</td><td style='text-align: center;'>222.0</td></tr>
    <tr><td style='text-align: center;'>111.5</td><td style='text-align: center;'>223.0</td></tr>
    <tr><td style='text-align: center;'>112.0</td><td style='text-align: center;'>224.0</td></tr>
    <tr><td style='text-align: center;'>112.5</td><td style='text-align: center;'>225.0</td></tr>
    <tr><td style='text-align: center;'>113.0</td><td style='text-align: center;'>226.0</td></tr>
    <tr><td style='text-align: center;'>113.5</td><td style='text-align: center;'>227.0</td></tr>
    <tr><td style='text-align: center;'>114.0</td><td style='text-align: center;'>228.0</td></tr>
    <tr><td style='text-align: center;'>114.5</td><td style='text-align: center;'>229.0</td></tr>
    <tr><td style='text-align: center;'>115.0</td><td style='text-align: center;'>230.0</td></tr>
    <tr><td style='text-align: center;'>115.5</td><td style='text-align: center;'>231.0</td></tr>
    <tr><td style='text-align: center;'>116.0</td><td style='text-align: center;'>232.0</td></tr>
    <tr><td style='text-align: center;'>116.5</td><td style='text-align: center;'>233.0</td></tr>
    <tr><td style='text-align: center;'>117.0</td><td style='text-align: center;'>234.0</td></tr>
    <tr><td style='text-align: center;'>117.5</td><td style='text-align: center;'>235.0</td></tr>
    <tr><td style='text-align: center;'>118.0</td><td style='text-align: center;'>236.0</td></tr>
    <tr><td style='text-align: center;'>118.5</td><td style='text-align: center;'>237.0</td></tr>
    <tr><td style='text-align: center;'>119.0</td><td style='text-align: center;'>238.0</td></tr>
    <tr><td style='text-align: center;'>119.5</td><td style='text-align: center;'>239.0</td></tr>
    <tr><td style='text-align: center;'>120.0</td><td style='text-align: center;'>240.0</td></tr>
    <tr><td style='text-align: center;'>120.5</td><td style='text-align: center;'>241.0</td></tr>
    <tr><td style='text-align: center;'>121.0</td><td style='text-align: center;'>242.0</td></tr>
    <tr><td style='text-align: center;'>121.5</td><td style='text-align: center;'>243.0</td></tr>
    <tr><td style='text-align: center;'>122.0</td><td style='text-align: center;'>244.0</td></tr>
    <tr><td style='text-align: center;'>122.5</td><td style='text-align: center;'>245.0</td></tr>
    <tr><td style='text-align: center;'>123.0</td><td style='text-align: center;'>246.0</td></tr>
    <tr><td style='text-align: center;'>123.5</td><td style='text-align: center;'>247.0</td></tr>
    <tr><td style='text-align: center;'>124.0</td><td style='text-align: center;'>248.0</td></tr>
    <tr><td style='text-align: center;'>124.5</td><td style='text-align: center;'>249.0</td></tr>
    <tr><td style='text-align: center;'>125.0</td><td style='text-align: center;'>250.0</td></tr>
    <tr><td style='text-align: center;'>125.5</td><td style='text-align: center;'>251.0</td></tr>
    <tr><td style='text-align: center;'>126.0</td><td style='text-align: center;'>252.0</td></tr>
    <tr><td style='text-align: center;'>126.5</td><td style='text-align: center;'>253.0</td></tr>
    <tr><td style='text-align: center;'>127.0</td><td style='text-align: center;'>254.0</td></tr>
    <tr><td style='text-align: center;'>127.5</td><td style='text-align: center;'>255.0</td></tr>
    <tr><td style='text-align: center;'>128.0</td><td style='text-align: center;'>256.0</td></tr>
    <tr><td style='text-align: center;'>128.5</td><td style='text-align: center;'>257.0</td></tr>
    <tr><td style='text-align: center;'>129.0</td><td style='text-align: center;'>258.0</td></tr>
    <tr><td style='text-align: center;'>129.5</td><td style='text-align: center;'>259.0</td></tr>
    <tr><td style='text-align: center;'>130.0</td><td style='text-align: center;'>260.0</td></tr>
    <tr><td style='text-align: center;'>130.5</td><td style='text-align: center;'>261.0</td></tr>
    <tr><td style='text-align: center;'>131.0</td><td style='text-align: center;'>262.0</td></tr>
    <tr><td style='text-align: center;'>131.5</td><td style='text-align: center;'>263.0</td></tr>
    <tr><td style='text-align: center;'>132.0</td><td style='text-align: center;'>264.0</td></tr>
    <tr><td style='text-align: center;'>132.5</td><td style='text-align: center;'>265.0</td></tr>
    <tr><td style='text-align: center;'>133.0</td><td style='text-align: center;'>266.0</td></tr>
    <tr><td style='text-align: center;'>133.5</td><td style='text-align: center;'>267.0</td></tr>
    <tr><td style='text-align: center;'>134.0</td><td style='text-align: center;'>268.0</td></tr>
    <tr><td style='text-align: center;'>134.5</td><td style='text-align: center;'>269.0</td></tr>
    <tr><td style='text-align: center;'>135.0</td><td style='text-align: center;'>270.0</td></tr>
    <tr><td style='text-align: center;'>135.5</td><td style='text-align: center;'>271.0</td></tr>
    <tr><td style='text-align: center;'>136.0</td><td style='text-align: center;'>272.0</td></tr>
    <tr><td style='text-align: center;'>136.5</td><td style='text-align: center;'>273.0</td></tr>
    <tr><td style='text-align: center;'>137.0</td><td style='text-align: center;'>274.0</td></tr>
    <tr><td style='text-align: center;'>137.5</td><td style='text-align: center;'>275.0</td></tr>
    <tr><td style='text-align: center;'>138.0</td><td style='text-align: center;'>276.0</td></tr>
    <tr><td style='text-align: center;'>138.5</td><td style='text-align: center;'>277.0</td></tr>
    <tr><td style='text-align: center;'>139.0</td><td style='text-align: center;'>278.0</td></tr>
    <tr><td style='text-align: center;'>139.5</td><td style='text-align: center;'>279.0</td></tr>
    <tr><td style='text-align: center;'>140.0</td><td style='text-align: center;'>280.0</td></tr>
    <tr><td style='text-align: center;'>140.5</td><td style='text-align: center;'>281.0</td></tr>
    <tr><td style='text-align: center;'>141.0</td><td style='text-align: center;'>282.0</td></tr>
    <tr><td style='text-align: center;'>141.5</td><td style='text-align: center;'>283.0</td></tr>
    <tr><td style='text-align: center;'>142.0</td><td style='text-align: center;'>284.0</td></tr>
    <tr><td style='text-align: center;'>142.5</td><td style='text-align: center;'>285.0</td></tr>
    <tr><td style='text-align: center;'>143.0</td><td style='text-align: center;'>286.0</td></tr>
    <tr><td style='text-align: center;'>143.5</td><td style='text-align: center;'>287.0</td></tr>
    <tr><td style='text-align: center;'>144.0</td><td style='text-align: center;'>288.0</td></tr>
    <tr><td style='text-align: center;'>144.5</td><td style='text-align: center;'>289.0</td></tr>
    <tr><td style='text-align: center;'>145.0</td><td style='text-align: center;'>290.0</td></tr>
    <tr><td style='text-align: center;'>145.5</td><td style='text-align: center;'>291.0</td></tr>
    <tr><td style='text-align: center;'>146.0</td><td style='text-align: center;'>292.0</td></tr>
    <tr><td style='text-align: center;'>146.5</td><td style='text-align: center;'>293.0</td></tr>
    <tr><td style='text-align: center;'>147.0</td><td style='text-align: center;'>294.0</td></tr>
    <tr><td style='text-align: center;'>147.5</td><td style='text-align: center;'>295.0</td></tr>
    <tr><td style='text-align: center;'>148.0</td><td style='text-align: center;'>296.0</td></tr>
    <tr><td style='text-align: center;'>148.5</td><td style='text-align: center;'>297.0</td></tr>
    <tr><td style='text-align: center;'>149.0</td><td style='text-align: center;'>298.0</td></tr>
    <tr><td style='text-align: center;'>149.5</td><td style='text-align: center;'>299.0</td></tr>
    <tr><td style='text-align: center;'>150.0</td><td style='text-align: center;'>300.0</td></tr>
    <tr><td style='text-align: center;'>150.5</td><td style='text-align: center;'>301.0</td></tr>
    <tr><td style='text-align: center;'>151.0</td><td style='text-align: center;'>302.0</td></tr>
    <tr><td style='text-align: center;'>151.5</td><td style='text-align: center;'>303.0</td></tr>
    <tr><td style='text-align: center;'>152.0</td><td style='text-align: center;'>304.0</td></tr>
    <tr><td style='text-align: center;'>152.5</td><td style='text-align: center;'>305.0</td></tr>
    <tr><td style='text-align: center;'>153.0</td><td style='text-align: center;'>306.0</td></tr>
    <tr><td style='text-align: center;'>153.5</td><td style='text-align: center;'>307.0</td></tr>
    <tr><td style='text-align: center;'>154.0</td><td style='text-align: center;'>308.0</td></tr>
    <tr><td style='text-align: center;'>154.5</td><td style='text-align: center;'>309.0</td></tr>
    <tr><td style='text-align: center;'>155.0</td><td style='text-align: center;'>310.0</td></tr>
    <tr><td style='text-align: center;'>155.5</td><td style='text-align: center;'>311.0</td></tr>
    <tr><td style='text-align: center;'>156.0</td><td style='text-align: center;'>312.0</td></tr>
    <tr><td style='text-align: center;'>156.5</td><td style='text-align: center;'>313.0</td></tr>
    <tr><td style='text-align: center;'>157.0</td><td style='text-align: center;'>314.0</td></tr>
    <tr><td style='text-align: center;'>157.5</td><td style='text-align: center;'>315.0</td></tr>
    <tr><td style='text-align: center;'>158.0</td><td style='text-align: center;'>316.0</td></tr>
    <tr><td style='text-align: center;'>158.5</td><td style='text-align: center;'>317.0</td></tr>
    <tr><td style='text-align: center;'>159.0</td><td style='text-align: center;'>318.0</td></tr>
    <tr><td style='text-align: center;'>159.5</td><td style='text-align: center;'>319.0</td></tr>
    <tr><td style='text-align: center;'>160.0</td><td style='text-align: center;'>320.0</td></tr>
    <tr><td style='text-align: center;'>160.5</td><td style='text-align: center;'>321.0</td></tr>
    <tr><td style='text-align: center;'>161.0</td><td style='text-align: center;'>322.0</td></tr>
    <tr><td style='text-align: center;'>161.5</td><td style='text-align: center;'>323.0</td></tr>
    <tr><td style='text-align: center;'>162.0</td><td style='text-align: center;'>324.0</td></tr>
    <tr><td style='text-align: center;'>162.5</td><td style='text-align: center;'>325.0</td></tr>
    <tr><td style='text-align: center;'>163.0</td><td style='text-align: center;'>326.0</td></tr>
    <tr><td style='text-align: center;'>163.5</td><td style='text-align: center;'>327.0</td></tr>
    <tr><td style='text-align: center;'>164.0</td><td style='text-align: center;'>328.0</td></tr>
    <tr><td style='text-align: center;'>164.5</td><td style='text-align: center;'>329.0</td></tr>
    <tr><td style='text-align: center;'>165.0</td><td style='text-align: center;'>330.0</td></tr>
    <tr><td style='text-align: center;'>165.5</td><td style='text-align: center;'>331.0</td></tr>
    <tr><td style='text-align: center;'>166.0</td><td style='text-align: center;'>332.0</td></tr>
    <tr><td style='text-align: center;'>166.5</td><td style='text-align: center;'>333.0</td></tr>
    <tr><td style='text-align: center;'>167.0</td><td style='text-align: center;'>334.0</td></tr>
    <tr><td style='text-align: center;'>167.5</td><td style='text-align: center;'>335.0</td></tr>
    <tr><td style='text-align: center;'>168.0</td><td style='text-align: center;'>336.0</td></tr>
    <tr><td style='text-align: center;'>168.5</td><td style='text-align: center;'>337.0</td></tr>
    <tr><td style='text-align: center;'>169.0</td><td style='text-align: center;'>338.0</td></tr>
    <tr><td style='text-align: center;'>169.5</td><td style='text-align: center;'>33</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.58 The Obs versus Pred plot with four principal components and with time lag.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hr)</th><th style='text-align: center;'>Predicted MI (PLS)</th><th style='text-align: center;'>Actual MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>18.5</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.59 Development of a soft sensor of MI based on Causal PLS model.</div>


### 9.6 Multiway PCA and PLS for Batch Processes

#### 9.6.1 Batch-Wise Unfolding and Observation-Wise Unfolding Approaches to Multiway PLS

Our discussion of data analytics in the preceding sections has been mostly about continuous processes. For data analytics of batch processes, we require a different approach. Industrial batch process data with multiple batches have a three-dimensional structure with the three data dimensions, namely, process variables, time, and number of batches. Wold et al. [22] and Nomikos and MacGregor [23] explain those three data dimensions as an example of a multiway approach.

---

<!-- PDF page 609 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_148_770_489.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 9.60 An illustration of batch-wide unfolding (BWU) of the three-way  $ (I \times J \times K) $ array of trajectory data  $ (X) $ of  $ i = 1 $ to  $ I $ (number of batches),  $ j = 1 $ to  $ J $ (number of process variables), and  $ k = 1 $ to  $ K $ (time step of data observation).</div>


to multivariate data analytics, and they specifically demonstrated two approaches when applied to PCA or PLS.

The first approach is the BWU approach that extracts the batch trajectory observations horizontally in a time-wise manner, as illustrated in Figure 9.60. Each batch becomes a single row of data. In the figure, we have a three-way array of trajectory data (X) with i = 1 to I (number of batches), j = 1 to J (number of process variables), and k = 1 to K (time step of data observation). We also append an initial condition matrix Z and a product quality matrix Y at time k = 0 (beginning time) an k = K (ending time), respectively. In BWU, the data are unfolded into a two-way array X (I × J by K), where the rows of the unfolded matrix represent the batches. Each batch becomes a single row of data in the model.

We develop PLS models based on the unfolded data matrices. The BWU principal component score predicts the final state of each batch based on all the time history of that batch up to the current time. The resulting principal component scores show differences among batches. The BWU approach is useful for predicting the final product quality and monitoring, controlling, and optimizing batch processes.

Refer to our discussion of PLS in Section 9.3.1, particularly Eqs. (9.17), (9.23), and (9.24), and to Figure 9.30. We show in Figure 9.61 an extension of the PLS structural diagram to BWU. In the figure, Z is the initial condition vector; X is the process data matrix; Y is the quality data matrix; T is the principal component score matrix; V is the initial condition vector; W is the weight matrix; and C is the principal component loading matrix. Based on Figure 9.30 and Eq. (9.24), we write the principal component score matrix T and the predicted product quality matrix  $ \hat{Y} $ as:

 $$ \mathbf{T}=\mathbf{X}\mathbf{W}\quad(9.24) $$ 

 $$ \hat{\mathbf{Y}}=\mathbf{T}\mathbf{C}^{\mathrm{T}}=[\mathbf{X}\mathbf{W}]\mathbf{C}^{\mathrm{T}}=\mathbf{X}\left[\mathbf{W}\mathbf{C}^{\mathrm{T}}\right]=\mathbf{X}\boldsymbol{\beta} $$ 

---

<!-- PDF page 610 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_150_795_523.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 9.61 PLS of batch-wise unfolded data.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_599_819_931.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Figure 9.62 An illustration of observation-wise unfolding (OWU of the three-way  $ (I \times J \times K) $ array of trajectory data  $ (X) $ of  $ i = 1 $ to  $ I $ (number of batches),  $ j = 1 $ to  $ J $ (number of process variables), and  $ k = 1 $ to  $ K $ (time step of data observation).</div>


where  $ \beta $ is the regression coefficient matrix of PLS. We have a row of coefficients for each Y variable. These coefficients show the relative importance of the X's to each individual Y variable.

The second approach is the observation-wide unfolding (OWU) approach, in which the process data for each batch are stacked on top of one another, following the way we typically read batch data. The analysis will summarize the instantaneous condition of each batch using the measured values at the current time. Figure 9.62 illustrates the OWU approach, which is useful for reducing the dimension of data collected in batches.

---

<!-- PDF page 611 -->

##### 9.6.2 Workshop 9.5: Application of Aspen ProMV to Batch-Wise Unfolding (BWU) Approach to Multiway PCA of Batch Polymerization Data

We consider a polymer batch dataset (polymer.xls) provided by Dunn [17] consisting of 10 process variables X (j = 1–10) in 55 batches (j = 1–55). Within each batch, we have 100 time steps of data observations (k = 1–100). We use PCA along with BWU analysis to identify the abnormal/bad batches using Aspen Pro MV.

We first load polymer.xls as follows. Start Aspen ProMV, and select "New Project." Within the Data Manager, we choose "Batch Blocks," and then click on "Import Batch Block" to upload polymer.xls into the software. Figure 9.63 shows part of the imported data with 10 process variables in different batches.

We then choose the batch number column (column 1) and click on “Observation IDs” button on the left-side pane to designate column 1 to contain Observation IDs. For batch dataset, one “observation” represents a batch. Referring to Figure 9.64, we can explain how the three-way database is displayed. First, we see that the column to the left of the Observation ID (i.e. batch number) goes from 2 to 5501 (currently displaying columns 2–3, 100–103, and 5498–5501 in the figure), which represents a total of 5500 time steps of data observations, with each observation ID or each batch number containing 100 time steps (that is,  $ k = 1–100 $) from 2 to 101 for batch 1, 102 to 201 for batch 2, 202 to 301 for batch 3, ..., and from 5402 to 5501 for batch 55.

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_694_782_903.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 9.63 A part of the imported batch polymerization dataset.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td rowspan="2">1 ObslDs</td><td rowspan="2">2 BWU</td><td rowspan="2">3 BWU</td><td rowspan="2">4 BWU</td><td rowspan="2">5 BWU</td><td rowspan="2">6 BWU</td><td rowspan="2">7 BWU</td><td rowspan="2">8 BWU</td><td rowspan="2">9 BWU</td><td rowspan="2">10 BWU</td><td rowspan="2">11 BWU</td></tr><tr></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Batch Num...</td><td style='text-align: center; word-wrap: break-word;'>X1</td><td style='text-align: center; word-wrap: break-word;'>X2</td><td style='text-align: center; word-wrap: break-word;'>X3</td><td style='text-align: center; word-wrap: break-word;'>X4</td><td style='text-align: center; word-wrap: break-word;'>X5</td><td style='text-align: center; word-wrap: break-word;'>X6</td><td style='text-align: center; word-wrap: break-word;'>X7</td><td style='text-align: center; word-wrap: break-word;'>X8</td><td style='text-align: center; word-wrap: break-word;'>X9</td><td style='text-align: center; word-wrap: break-word;'>X10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>0.57039</td><td style='text-align: center; word-wrap: break-word;'>0.887247</td><td style='text-align: center; word-wrap: break-word;'>0.546655</td><td style='text-align: center; word-wrap: break-word;'>0.98417</td><td style='text-align: center; word-wrap: break-word;'>0.5202</td><td style='text-align: center; word-wrap: break-word;'>0.989112</td><td style='text-align: center; word-wrap: break-word;'>0.933139</td><td style='text-align: center; word-wrap: break-word;'>0.954723</td><td style='text-align: center; word-wrap: break-word;'>0.727997</td><td style='text-align: center; word-wrap: break-word;'>1.387073</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>0.576384</td><td style='text-align: center; word-wrap: break-word;'>0.862227</td><td style='text-align: center; word-wrap: break-word;'>0.552975</td><td style='text-align: center; word-wrap: break-word;'>0.979343</td><td style='text-align: center; word-wrap: break-word;'>0.7248</td><td style='text-align: center; word-wrap: break-word;'>0.989199</td><td style='text-align: center; word-wrap: break-word;'>0.933337</td><td style='text-align: center; word-wrap: break-word;'>0.956171</td><td style='text-align: center; word-wrap: break-word;'>0.72632</td><td style='text-align: center; word-wrap: break-word;'>1.44286</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>0.946678</td><td style='text-align: center; word-wrap: break-word;'>0.969153</td><td style='text-align: center; word-wrap: break-word;'>0.925244</td><td style='text-align: center; word-wrap: break-word;'>0.411393</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.86282</td><td style='text-align: center; word-wrap: break-word;'>0.684238</td><td style='text-align: center; word-wrap: break-word;'>0.858061</td><td style='text-align: center; word-wrap: break-word;'>0.437273</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>101</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>0.952396</td><td style='text-align: center; word-wrap: break-word;'>0.969384</td><td style='text-align: center; word-wrap: break-word;'>0.926992</td><td style='text-align: center; word-wrap: break-word;'>0.415084</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.860972</td><td style='text-align: center; word-wrap: break-word;'>0.678943</td><td style='text-align: center; word-wrap: break-word;'>0.857308</td><td style='text-align: center; word-wrap: break-word;'>0.433641</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>102</td><td style='text-align: center; word-wrap: break-word;'>2.0</td><td style='text-align: center; word-wrap: break-word;'>0.561848</td><td style='text-align: center; word-wrap: break-word;'>0.885173</td><td style='text-align: center; word-wrap: break-word;'>0.537042</td><td style='text-align: center; word-wrap: break-word;'>0.941331</td><td style='text-align: center; word-wrap: break-word;'>0.1247</td><td style='text-align: center; word-wrap: break-word;'>0.988564</td><td style='text-align: center; word-wrap: break-word;'>0.932068</td><td style='text-align: center; word-wrap: break-word;'>0.954694</td><td style='text-align: center; word-wrap: break-word;'>0.723945</td><td style='text-align: center; word-wrap: break-word;'>1.29536</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>103</td><td style='text-align: center; word-wrap: break-word;'>2.0</td><td style='text-align: center; word-wrap: break-word;'>0.568978</td><td style='text-align: center; word-wrap: break-word;'>0.891526</td><td style='text-align: center; word-wrap: break-word;'>0.541479</td><td style='text-align: center; word-wrap: break-word;'>0.984845</td><td style='text-align: center; word-wrap: break-word;'>0.4529</td><td style='text-align: center; word-wrap: break-word;'>0.988332</td><td style='text-align: center; word-wrap: break-word;'>0.9323</td><td style='text-align: center; word-wrap: break-word;'>0.954578</td><td style='text-align: center; word-wrap: break-word;'>0.722688</td><td style='text-align: center; word-wrap: break-word;'>1.369561</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5498</td><td style='text-align: center; word-wrap: break-word;'>35.0</td><td style='text-align: center; word-wrap: break-word;'>0.939995</td><td style='text-align: center; word-wrap: break-word;'>0.954471</td><td style='text-align: center; word-wrap: break-word;'>0.919361</td><td style='text-align: center; word-wrap: break-word;'>0.403691</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.869607</td><td style='text-align: center; word-wrap: break-word;'>0.83017</td><td style='text-align: center; word-wrap: break-word;'>0.844947</td><td style='text-align: center; word-wrap: break-word;'>0.387119</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5499</td><td style='text-align: center; word-wrap: break-word;'>35.0</td><td style='text-align: center; word-wrap: break-word;'>0.940305</td><td style='text-align: center; word-wrap: break-word;'>0.955261</td><td style='text-align: center; word-wrap: break-word;'>0.919899</td><td style='text-align: center; word-wrap: break-word;'>0.407631</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.867585</td><td style='text-align: center; word-wrap: break-word;'>0.827682</td><td style='text-align: center; word-wrap: break-word;'>0.843181</td><td style='text-align: center; word-wrap: break-word;'>0.385303</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5500</td><td style='text-align: center; word-wrap: break-word;'>35.0</td><td style='text-align: center; word-wrap: break-word;'>0.940546</td><td style='text-align: center; word-wrap: break-word;'>0.955359</td><td style='text-align: center; word-wrap: break-word;'>0.920874</td><td style='text-align: center; word-wrap: break-word;'>0.406247</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.865563</td><td style='text-align: center; word-wrap: break-word;'>0.82502</td><td style='text-align: center; word-wrap: break-word;'>0.841386</td><td style='text-align: center; word-wrap: break-word;'>0.38656</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5501</td><td style='text-align: center; word-wrap: break-word;'>35.0</td><td style='text-align: center; word-wrap: break-word;'>0.940822</td><td style='text-align: center; word-wrap: break-word;'>0.954866</td><td style='text-align: center; word-wrap: break-word;'>0.92195</td><td style='text-align: center; word-wrap: break-word;'>0.412067</td><td style='text-align: center; word-wrap: break-word;'>0.0</td><td style='text-align: center; word-wrap: break-word;'>0.863397</td><td style='text-align: center; word-wrap: break-word;'>0.822387</td><td style='text-align: center; word-wrap: break-word;'>0.839562</td><td style='text-align: center; word-wrap: break-word;'>0.378737</td><td style='text-align: center; word-wrap: break-word;'>0.0</td></tr></table>

<div style="text-align: center;">Figure 9.64 A display of parts of the unfolded dataset.</div>


---

<!-- PDF page 612 -->

<div style="text-align: center;">Figure 9.65 Option to align the batch trajectory.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_143_817_714.jpg" alt="Image" width="67%" /></div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>Display Mean</th><th style='text-align: center;'>Zoom Off</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.89</td><td style='text-align: center;'>0.89</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.94</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.96</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.96</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.97</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.97</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.98</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.66 A display of the time-dependent changes of variable X1 for 100 time steps in batch 1.</div>


Next, we see column 1 (ObsIDs), Batch Number, varies from 1 to 55 (i.e. i = 1–55). Lastly, we see columns 2–11 for X1–X10, representing 10 process variables (that is, j = 1–10).

On the same window screen as Figures 9.63 and 9.64, we click on OK and then choose "No" to align the batch trajectory. See Figure 9.65. We then see the "View/Edit Batch Block" screen, and we highlight column 1 and see the time-dependent change of variable X1 over the 100 time steps within batch 1. See Figure 9.66. We click on "Save."

We click on OK on the screen of Figure 9.67 and see the observation summary (as illustrated previously in Figure 9.15), and then click on OK. We save the resulting file as WS9.5_PCA_BWU-X.pmvx.

Following Figure 9.20, we develop a PCA model of the batch-wide unfolded dataset with 10 principal components (A = 10). Figure 9.68 shows the resulting R2 and Q2 values versus the number of principal components. We note that both R2 and Q2 increase with an increase in the number of principal components. Should we choose to use auto-fitting tool following Figure 9.20, the number of principal components (A) is equal to half of the total number of process variables (j = 1–10), that is, A = 5. The corresponding R2 and Q2 values are 0.7049 and 0.6096, respectively.

---

<!-- PDF page 613 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_149_738_407.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 9.67 A summary of imported dataset.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th><th style='text-align: center;'>Q2 Cumulative</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.34</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.54</td><td style='text-align: center;'>0.52</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.63</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.68</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.62</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[6]</td><td style='text-align: center;'>0.74</td><td style='text-align: center;'>0.63</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[7]</td><td style='text-align: center;'>0.76</td><td style='text-align: center;'>0.64</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[8]</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[9]</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.66</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[10]</td><td style='text-align: center;'>0.81</td><td style='text-align: center;'>0.67</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[11]</td><td style='text-align: center;'>0.82</td><td style='text-align: center;'>0.68</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[12]</td><td style='text-align: center;'>0.83</td><td style='text-align: center;'>0.69</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[13]</td><td style='text-align: center;'>0.84</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[14]</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.71</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[15]</td><td style='text-align: center;'>0.86</td><td style='text-align: center;'>0.72</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[16]</td><td style='text-align: center;'>0.87</td><td style='text-align: center;'>0.73</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[17]</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.74</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[18]</td><td style='text-align: center;'>0.89</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[19]</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.76</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[20]</td><td style='text-align: center;'>0.91</td><td style='text-align: center;'>0.77</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[21]</td><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.78</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[22]</td><td style='text-align: center;'>0.93</td><td style='text-align: center;'>0.79</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[23]</td><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.80</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[24]</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.81</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[25]</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.82</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[26]</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.83</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[27]</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.84</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[28]</td><td style='text-align: center;'>0.99</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[29]</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.86</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[30]</td><td style='text-align: center;'>1.01</td><td style='text-align: center;'>0.87</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[31]</td><td style='text-align: center;'>1.02</td><td style='text-align: center;'>0.88</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[32]</td><td style='text-align: center;'>1.03</td><td style='text-align: center;'>0.89</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[33]</td><td style='text-align: center;'>1.04</td><td style='text-align: center;'>0.90</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[34]</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>0.91</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[35]</td><td style='text-align: center;'>1.06</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[36]</td><td style='text-align: center;'>1.07</td><td style='text-align: center;'>0.93</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[37]</td><td style='text-align: center;'>1.08</td><td style='text-align: center;'>0.94</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[38]</td><td style='text-align: center;'>1.09</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[39]</td><td style='text-align: center;'>1.10</td><td style='text-align: center;'>0.96</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[40]</td><td style='text-align: center;'>1.11</td><td style='text-align: center;'>0.97</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[41]</td><td style='text-align: center;'>1.12</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[42]</td><td style='text-align: center;'>1.13</td><td style='text-align: center;'>0.99</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[43]</td><td style='text-align: center;'>1.14</td><td style='text-align: center;'>1.00</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[44]</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>1.01</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[45]</td><td style='text-align: center;'>1.16</td><td style='text-align: center;'>1.02</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[46]</td><td style='text-align: center;'>1.17</td><td style='text-align: center;'>1.03</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[47]</td><td style='text-align: center;'>1.18</td><td style='text-align: center;'>1.04</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[48]</td><td style='text-align: center;'>1.19</td><td style='text-align: center;'>1.05</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[49]</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.06</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[50]</td><td style='text-align: center;'>1.21</td><td style='text-align: center;'>1.07</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[51]</td><td style='text-align: center;'>1.22</td><td style='text-align: center;'>1.08</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[52]</td><td style='text-align: center;'>1.23</td><td style='text-align: center;'>1.09</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[53]</td><td style='text-align: center;'>1.24</td><td style='text-align: center;'>1.10</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[54]</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>1.11</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[55]</td><td style='text-align: center;'>1.26</td><td style='text-align: center;'>1.12</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[56]</td><td style='text-align: center;'>1.27</td><td style='text-align: center;'>1.13</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[57]</td><td style='text-align: center;'>1.28</td><td style='text-align: center;'>1.14</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[58]</td><td style='text-align: center;'>1.29</td><td style='text-align: center;'>1.15</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[59]</td><td style='text-align: center;'>1.30</td><td style='text-align: center;'>1.16</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[60]</td><td style='text-align: center;'>1.31</td><td style='text-align: center;'>1.17</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[61]</td><td style='text-align: center;'>1.32</td><td style='text-align: center;'>1.18</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[62]</td><td style='text-align: center;'>1.33</td><td style='text-align: center;'>1.19</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[63]</td><td style='text-align: center;'>1.34</td><td style='text-align: center;'>1.20</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[64]</td><td style='text-align: center;'>1.35</td><td style='text-align: center;'>1.21</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[65]</td><td style='text-align: center;'>1.36</td><td style='text-align: center;'>1.22</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[66]</td><td style='text-align: center;'>1.37</td><td style='text-align: center;'>1.23</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[67]</td><td style='text-align: center;'>1.38</td><td style='text-align: center;'>1.24</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[68]</td><td style='text-align: center;'>1.39</td><td style='text-align: center;'>1.25</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[69]</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.26</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[70]</td><td style='text-align: center;'>1.41</td><td style='text-align: center;'>1.27</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[71]</td><td style='text-align: center;'>1.42</td><td style='text-align: center;'>1.28</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[72]</td><td style='text-align: center;'>1.43</td><td style='text-align: center;'>1.29</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[73]</td><td style='text-align: center;'>1.44</td><td style='text-align: center;'>1.30</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[74]</td><td style='text-align: center;'>1.45</td><td style='text-align: center;'>1.31</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[75]</td><td style='text-align: center;'>1.46</td><td style='text-align: center;'>1.32</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[76]</td><td style='text-align: center;'>1.47</td><td style='text-align: center;'>1.33</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[77]</td><td style='text-align: center;'>1.48</td><td style='text-align: center;'>1.34</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[78]</td><td style='text-align: center;'>1.49</td><td style='text-align: center;'>1.35</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[79]</td><td style='text-align: center;'>1.50</td><td style='text-align: center;'>1.36</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[80]</td><td style='text-align: center;'>1.51</td><td style='text-align: center;'>1.37</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[81]</td><td style='text-align: center;'>1.52</td><td style='text-align: center;'>1.38</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[82]</td><td style='text-align: center;'>1.53</td><td style='text-align: center;'>1.39</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[83]</td><td style='text-align: center;'>1.54</td><td style='text-align: center;'>1.40</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[84]</td><td style='text-align: center;'>1.55</td><td style='text-align: center;'>1.41</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[85]</td><td style='text-align: center;'>1.56</td><td style='text-align: center;'>1.42</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[86]</td><td style='text-align: center;'>1.57</td><td style='text-align: center;'>1.43</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[87]</td><td style='text-align: center;'>1.58</td><td style='text-align: center;'>1.44</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[88]</td><td style='text-align: center;'>1.59</td><td style='text-align: center;'>1.45</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[89]</td><td style='text-align: center;'>1.60</td><td style='text-align: center;'>1.46</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[90]</td><td style='text-align: center;'>1.61</td><td style='text-align: center;'>1.47</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[91]</td><td style='text-align: center;'>1.62</td><td style='text-align: center;'>1.48</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[92]</td><td style='text-align: center;'>1.63</td><td style='text-align: center;'>1.49</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[93]</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.50</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[94]</td><td style='text-align: center;'>1.65</td><td style='text-align: center;'>1.51</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[95]</td><td style='text-align: center;'>1.66</td><td style='text-align: center;'>1.52</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[96]</td><td style='text-align: center;'>1.67</td><td style='text-align: center;'>1.53</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[97]</td><td style='text-align: center;'>1.68</td><td style='text-align: center;'>1.54</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[98]</td><td style='text-align: center;'>1.69</td><td style='text-align: center;'>1.55</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[99]</td><td style='text-align: center;'>1.70</td><td style='text-align: center;'>1.56</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[100]</td><td style='text-align: center;'>1.71</td><td style='text-align: center;'>1.57</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[101]</td><td style='text-align: center;'>1.72</td><td style='text-align: center;'>1.58</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[102]</td><td style='text-align: center;'>1.73</td><td style='text-align: center;'>1.59</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[103]</td><td style='text-align: center;'>1.74</td><td style='text-align: center;'>1.60</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[104]</td><td style='text-align: center;'>1.75</td><td style='text-align: center;'>1.61</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[105]</td><td style='text-align: center;'>1.76</td><td style='text-align: center;'>1.62</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[106]</td><td style='text-align: center;'>1.77</td><td style='text-align: center;'>1.63</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[107]</td><td style='text-align: center;'>1.78</td><td style='text-align: center;'>1.64</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[108]</td><td style='text-align: center;'>1.79</td><td style='text-align: center;'>1.65</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[109]</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.66</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[110]</td><td style='text-align: center;'>1.81</td><td style='text-align: center;'>1.67</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[111]</td><td style='text-align: center;'>1.82</td><td style='text-align: center;'>1.68</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[112]</td><td style='text-align: center;'>1.83</td><td style='text-align: center;'>1.69</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[113]</td><td style='text-align: center;'>1.84</td><td style='text-align: center;'>1.70</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[114]</td><td style='text-align: center;'>1.85</td><td style='text-align: center;'>1.71</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[115]</td><td style='text-align: center;'>1.86</td><td style='text-align: center;'>1.72</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[116]</td><td style='text-align: center;'>1.87</td><td style='text-align: center;'>1.73</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[117]</td><td style='text-align: center;'>1.88</td><td style='text-align: center;'>1.74</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[118]</td><td style='text-align: center;'>1.89</td><td style='text-align: center;'>1.75</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[119]</td><td style='text-align: center;'>1.90</td><td style='text-align: center;'>1.76</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[120]</td><td style='text-align: center;'>1.91</td><td style='text-align: center;'>1.77</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[121]</td><td style='text-align: center;'>1.92</td><td style='text-align: center;'>1.78</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[122]</td><td style='text-align: center;'>1.93</td><td style='text-align: center;'>1.79</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[123]</td><td style='text-align: center;'>1.94</td><td style='text-align: center;'>1.80</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[124]</td><td style='text-align: center;'>1.95</td><td style='text-align: center;'>1.81</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[125]</td><td style='text-align: center;'>1.96</td><td style='text-align: center;'>1.82</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[126]</td><td style='text-align: center;'>1.97</td><td style='text-align: center;'>1.83</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[127]</td><td style='text-align: center;'>1.98</td><td style='text-align: center;'>1.84</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[128]</td><td style='text-align: center;'>1.99</td><td style='text-align: center;'>1.85</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[129]</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>1.86</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[130]</td><td style='text-align: center;'>2.01</td><td style='text-align: center;'>1.87</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[131]</td><td style='text-align: center;'>2.02</td><td style='text-align: center;'>1.88</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[132]</td><td style='text-align: center;'>2.03</td><td style='text-align: center;'>1.89</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[133]</td><td style='text-align: center;'>2.04</td><td style='text-align: center;'>1.90</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[134]</td><td style='text-align: center;'>2.05</td><td style='text-align: center;'>1.91</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[135]</td><td style='text-align: center;'>2.06</td><td style='text-align: center;'>1.92</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[136]</td><td style='text-align: center;'>2.07</td><td style='text-align: center;'>1.93</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[137]</td><td style='text-align: center;'>2.08</td><td style='text-align: center;'>1.94</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[138]</td><td style='text-align: center;'>2.09</td><td style='text-align: center;'>1.95</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[139]</td><td style='text-align: center;'>2.10</td><td style='text-align: center;'>1.96</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S</td><td style='text-align: center;'>[140]</td><td style='text-align: center;'>2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.68 R2 and Q2 values versus the number of principal components.</div>


Following Figure 9.25, we show in Figure 9.69 the score plot, T[2] versus T[1], for the case with five principal components. In the plot, we use the button highlighted by an arrow on the top ribbon to select points located close to the 95% confidence limit (dashed ellipse), batch 51; points located between 95% and 99% confidence limits (dashed and solid ellipses), batches 50, 52, 53, and 55; and points outside the 99% confidence limit, batch 54. These batches represent the apparent outliers or abnormal batches among the 55 batches (i = 1–55).

We confirm batches 50–55 being abnormal by following Figure 9.26 to draw the Hotelling's  $ T^{2} $ plot in Figure 9.70. Significantly, this plot shows another abnormal batch 49 that is not apparent in Figure 9.69.

Following Figure 9.27, we show in Figure 9.71 the squared prediction error SPE-X plot, which reveals that batch 51 has the largest SPE-X.

We conclude this workshop by finding out what happens when applying the OWU approach to the same polymer dataset. We first load polymer.xls as follows. Start Aspen ProMV and select "New Project." To use OWU on the same dataset, we need to import batch data using "Standard Blocks" within the Data Manager, not

---

<!-- PDF page 614 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Label</th><th style='text-align: center;'>T[1]</th><th style='text-align: center;'>T[2]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>54.0</td><td style='text-align: center;'>-55.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>52.0</td><td style='text-align: center;'>-48.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>-45.0</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>51.0</td><td style='text-align: center;'>-35.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>55.0</td><td style='text-align: center;'>-30.0</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>53.0</td><td style='text-align: center;'>-25.0</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>56.0</td><td style='text-align: center;'>-20.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>58.0</td><td style='text-align: center;'>-15.0</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>59.0</td><td style='text-align: center;'>-10.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>60.0</td><td style='text-align: center;'>-5.0</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>61.0</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>62.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>63.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>64.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>65.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>66.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>67.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>68.0</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>69.0</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>70.0</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>71.0</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>72.0</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>73.0</td><td style='text-align: center;'>28.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>74.0</td><td style='text-align: center;'>30.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>75.0</td><td style='text-align: center;'>32.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>76.0</td><td style='text-align: center;'>35.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>77.0</td><td style='text-align: center;'>38.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>78.0</td><td style='text-align: center;'>40.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>79.0</td><td style='text-align: center;'>42.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>80.0</td><td style='text-align: center;'>45.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>81.0</td><td style='text-align: center;'>48.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>82.0</td><td style='text-align: center;'>50.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>83.0</td><td style='text-align: center;'>52.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>84.0</td><td style='text-align: center;'>55.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>85.0</td><td style='text-align: center;'>58.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>86.0</td><td style='text-align: center;'>60.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>87.0</td><td style='text-align: center;'>62.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>88.0</td><td style='text-align: center;'>65.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>89.0</td><td style='text-align: center;'>68.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>90.0</td><td style='text-align: center;'>70.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>91.0</td><td style='text-align: center;'>72.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>92.0</td><td style='text-align: center;'>75.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>93.0</td><td style='text-align: center;'>78.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>94.0</td><td style='text-align: center;'>80.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>95.0</td><td style='text-align: center;'>82.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>96.0</td><td style='text-align: center;'>85.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>97.0</td><td style='text-align: center;'>88.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>98.0</td><td style='text-align: center;'>90.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>99.0</td><td style='text-align: center;'>92.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>100.0</td><td style='text-align: center;'>95.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>101.0</td><td style='text-align: center;'>98.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>102.0</td><td style='text-align: center;'>100.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>103.0</td><td style='text-align: center;'>102.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>104.0</td><td style='text-align: center;'>105.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>105.0</td><td style='text-align: center;'>108.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>106.0</td><td style='text-align: center;'>110.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>107.0</td><td style='text-align: center;'>112.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>108.0</td><td style='text-align: center;'>115.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>109.0</td><td style='text-align: center;'>118.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>110.0</td><td style='text-align: center;'>120.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>111.0</td><td style='text-align: center;'>122.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>112.0</td><td style='text-align: center;'>125.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>113.0</td><td style='text-align: center;'>128.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>114.0</td><td style='text-align: center;'>130.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>115.0</td><td style='text-align: center;'>132.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>116.0</td><td style='text-align: center;'>135.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>117.0</td><td style='text-align: center;'>138.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>118.0</td><td style='text-align: center;'>140.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>119.0</td><td style='text-align: center;'>142.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>120.0</td><td style='text-align: center;'>145.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>121.0</td><td style='text-align: center;'>148.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>122.0</td><td style='text-align: center;'>150.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>123.0</td><td style='text-align: center;'>152.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>124.0</td><td style='text-align: center;'>155.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>125.0</td><td style='text-align: center;'>158.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>126.0</td><td style='text-align: center;'>160.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>127.0</td><td style='text-align: center;'>162.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>128.0</td><td style='text-align: center;'>165.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>129.0</td><td style='text-align: center;'>168.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>130.0</td><td style='text-align: center;'>170.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>131.0</td><td style='text-align: center;'>172.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>132.0</td><td style='text-align: center;'>175.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>133.0</td><td style='text-align: center;'>178.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>134.0</td><td style='text-align: center;'>180.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>135.0</td><td style='text-align: center;'>182.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>136.0</td><td style='text-align: center;'>185.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>137.0</td><td style='text-align: center;'>188.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>138.0</td><td style='text-align: center;'>190.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>139.0</td><td style='text-align: center;'>192.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>140.0</td><td style='text-align: center;'>195.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>141.0</td><td style='text-align: center;'>198.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>142.0</td><td style='text-align: center;'>200.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>143.0</td><td style='text-align: center;'>202.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>144.0</td><td style='text-align: center;'>205.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>145.0</td><td style='text-align: center;'>208.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>146.0</td><td style='text-align: center;'>210.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>147.0</td><td style='text-align: center;'>212.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>148.0</td><td style='text-align: center;'>215.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>149.0</td><td style='text-align: center;'>218.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>150.0</td><td style='text-align: center;'>220.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>151.0</td><td style='text-align: center;'>222.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>152.0</td><td style='text-align: center;'>225.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>153.0</td><td style='text-align: center;'>228.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>154.0</td><td style='text-align: center;'>230.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>155.0</td><td style='text-align: center;'>232.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>156.0</td><td style='text-align: center;'>235.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>157.0</td><td style='text-align: center;'>238.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>158.0</td><td style='text-align: center;'>240.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>159.0</td><td style='text-align: center;'>242.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>160.0</td><td style='text-align: center;'>245.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>161.0</td><td style='text-align: center;'>248.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>162.0</td><td style='text-align: center;'>250.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>163.0</td><td style='text-align: center;'>252.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>164.0</td><td style='text-align: center;'>255.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>165.0</td><td style='text-align: center;'>258.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>166.0</td><td style='text-align: center;'>260.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>167.0</td><td style='text-align: center;'>262.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>168.0</td><td style='text-align: center;'>265.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>169.0</td><td style='text-align: center;'>268.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>170.0</td><td style='text-align: center;'>270.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>171.0</td><td style='text-align: center;'>272.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>172.0</td><td style='text-align: center;'>275.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>173.0</td><td style='text-align: center;'>278.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>174.0</td><td style='text-align: center;'>280.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>175.0</td><td style='text-align: center;'>282.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>176.0</td><td style='text-align: center;'>285.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>177.0</td><td style='text-align: center;'>288.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>178.0</td><td style='text-align: center;'>290.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>179.0</td><td style='text-align: center;'>292.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>180.0</td><td style='text-align: center;'>295.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>181.0</td><td style='text-align: center;'>298.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>182.0</td><td style='text-align: center;'>300.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>183.0</td><td style='text-align: center;'>302.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>184.0</td><td style='text-align: center;'>305.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>185.0</td><td style='text-align: center;'>308.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>186.0</td><td style='text-align: center;'>310.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>187.0</td><td style='text-align: center;'>312.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>188.0</td><td style='text-align: center;'>315.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>189.0</td><td style='text-align: center;'>318.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>190.0</td><td style='text-align: center;'>320.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>191.0</td><td style='text-align: center;'>322.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>192.0</td><td style='text-align: center;'>325.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>193.0</td><td style='text-align: center;'>328.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>194.0</td><td style='text-align: center;'>330.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>195.0</td><td style='text-align: center;'>332.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>196.0</td><td style='text-align: center;'>335.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>197.0</td><td style='text-align: center;'>338.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>198.0</td><td style='text-align: center;'>340.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>199.0</td><td style='text-align: center;'>342.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>200.0</td><td style='text-align: center;'>345.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>201.0</td><td style='text-align: center;'>348.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>202.0</td><td style='text-align: center;'>350.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>203.0</td><td style='text-align: center;'>352.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>204.0</td><td style='text-align: center;'>355.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>205.0</td><td style='text-align: center;'>358.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>206.0</td><td style='text-align: center;'>360.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>207.0</td><td style='text-align: center;'>362.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>208.0</td><td style='text-align: center;'>365.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>209.0</td><td style='text-align: center;'>368.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>210.0</td><td style='text-align: center;'>370.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>211.0</td><td style='text-align: center;'>372.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>212.0</td><td style='text-align: center;'>375.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>213.0</td><td style='text-align: center;'>378.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>214.0</td><td style='text-align: center;'>380.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>215.0</td><td style='text-align: center;'>382.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>216.0</td><td style='text-align: center;'>385.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>217.0</td><td style='text-align: center;'>388.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>218.0</td><td style='text-align: center;'>390.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>219.0</td><td style='text-align: center;'>392.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>220.0</td><td style='text-align: center;'>395.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>221.0</td><td style='text-align: center;'>398.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>222.0</td><td style='text-align: center;'>400.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>223.0</td><td style='text-align: center;'>402.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>224.0</td><td style='text-align: center;'>405.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>225.0</td><td style='text-align: center;'>408.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>226.0</td><td style='text-align: center;'>410.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>227.0</td><td style='text-align: center;'>412.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>228.0</td><td style='text-align: center;'>415.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>229.0</td><td style='text-align: center;'>418.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>230.0</td><td style='text-align: center;'>420.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>231.0</td><td style='text-align: center;'>422.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>232.0</td><td style='text-align: center;'>425.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>233.0</td><td style='text-align: center;'>428.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>234.0</td><td style='text-align: center;'>430.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>235.0</td><td style='text-align: center;'>432.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>236.0</td><td style='text-align: center;'>435.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>237.0</td><td style='text-align: center;'>438.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>238.0</td><td style='text-align: center;'>440.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>239.0</td><td style='text-align: center;'>442.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>240.0</td><td style='text-align: center;'>445.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>241.0</td><td style='text-align: center;'>448.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>242.0</td><td style='text-align: center;'>450.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>243.0</td><td style='text-align: center;'>452.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>244.0</td><td style='text-align: center;'>455.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>245.0</td><td style='text-align: center;'>458.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>246.0</td><td style='text-align: center;'>460.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>247.0</td><td style='text-align: center;'>462.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>248.0</td><td style='text-align: center;'>465.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>249.0</td><td style='text-align: center;'>468.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>250.0</td><td style='text-align: center;'>470.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>251.0</td><td style='text-align: center;'>472.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>252.0</td><td style='text-align: center;'>475.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>253.0</td><td style='text-align: center;'>478.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>254.0</td><td style='text-align: center;'>480.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>255.0</td><td style='text-align: center;'>482.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>256.0</td><td style='text-align: center;'>485.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>257.0</td><td style='text-align: center;'>488.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>258.0</td><td style='text-align: center;'>490.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>259.0</td><td style='text-align: center;'>492.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>260.0</td><td style='text-align: center;'>495.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>261.0</td><td style='text-align: center;'>498.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>262.0</td><td style='text-align: center;'>500.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>263.0</td><td style='text-align: center;'>502.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>264.0</td><td style='text-align: center;'>505.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>265.0</td><td style='text-align: center;'>508.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>266.0</td><td style='text-align: center;'>510.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>267.0</td><td style='text-align: center;'>512.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>268.0</td><td style='text-align: center;'>515.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>269.0</td><td style='text-align: center;'>518.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>270.0</td><td style='text-align: center;'>520.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>271.0</td><td style='text-align: center;'>522.</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.69 Score plot, T[2] versus T[1].</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>H12[1-5]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.95</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>10.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.70 The Hotelling  $ T^{2} $ plot.</div>


---

<!-- PDF page 615 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Observation number</th><th style='text-align: center;'>SPE [S comp.]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>2</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>4</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5</td><td style='text-align: center;'>380</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>6</td><td style='text-align: center;'>400</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>7</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>8</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>9</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>10</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>11</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>12</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>13</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>14</td><td style='text-align: center;'>320</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>15</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>16</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>17</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>18</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>19</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>20</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>21</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>22</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>21.0</td><td style='text-align: center;'>23</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>22.0</td><td style='text-align: center;'>24</td><td style='text-align: center;'>280</td></tr>
    <tr><td style='text-align: center;'>23.0</td><td style='text-align: center;'>25</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>24.0</td><td style='text-align: center;'>26</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>27</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>26.0</td><td style='text-align: center;'>28</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>27.0</td><td style='text-align: center;'>29</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>28.0</td><td style='text-align: center;'>30</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>29.0</td><td style='text-align: center;'>31</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>32</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>31.0</td><td style='text-align: center;'>33</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>32.0</td><td style='text-align: center;'>34</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>33.0</td><td style='text-align: center;'>35</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>34.0</td><td style='text-align: center;'>36</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>37</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>36.0</td><td style='text-align: center;'>38</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>37.0</td><td style='text-align: center;'>39</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>38.0</td><td style='text-align: center;'>40</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>39.0</td><td style='text-align: center;'>41</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>42</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>41.0</td><td style='text-align: center;'>43</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>42.0</td><td style='text-align: center;'>44</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>43.0</td><td style='text-align: center;'>45</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>44.0</td><td style='text-align: center;'>46</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>45.0</td><td style='text-align: center;'>47</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>46.0</td><td style='text-align: center;'>48</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>47.0</td><td style='text-align: center;'>49</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>48.0</td><td style='text-align: center;'>50</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>49.0</td><td style='text-align: center;'>51</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>52</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>51.0</td><td style='text-align: center;'>53</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>54.0</td><td style='text-align: center;'>55</td><td style='text-align: center;'>250</td></tr>
    <tr><td style='text-align: center;'>55.0</td><td style='text-align: center;'>56</td><td style='text-align: center;'>200</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.71 The SPE-X plot.</div>


“Batch Block” (see Figure 9.14 shown previously). Since the dataset (polymer.xls) contains 55 batches, with each batch containing 100 time steps, following the same procedure as in the BWU approach will lead to the error of having “duplicate Observation IDs” (see Figure 9.72). We need to do some manipulations of the dataset to prevent the error. We use the Pandas package in Python (see Appendix 9.1) to delete the “Batch Number” column in the Excel sheet and add an index column from 1 to 5500 observation instances. This column serves as “Observation IDs” for data import by “Standard Blocks.” We save the Excel file after data manipulation as Polymer_OWU_No duplicate ObsIDs.xls.

We use the Pandas package in Python (see Appendix 9.1) to delete the “Batch Number” column in the dataset Excel sheet and add an index column from 1 to 5500 observation instances. This column serves as “Observation IDs” for the “Standard Blocks” data import. The file after data manipulation is saved as Polymer_OWU_No duplicate ObsIDs.xls.

We now follow Figures 9.11–9.21 to develop a PCA model using standard blocks with the modified dataset, Polymer_OWU_No duplicate ObsIDs.xls. Figure 9.73 shows part of the imported dataset, and we do not see the error of having duplicate observation IDs. We save the resulting PCA model as WS9.5_OWS_PCA-X.pmvx. Figure 9.73 shows the resulting R2 and Q2 versus the number of principal components, and Figure 9.74 gives the corresponding score and loading plots. It is unfortunate that the score plot in Figure 9.74 (left) shows no interpretable trends and no observable outliers with the OWU approach. This is in contrast to the outliers

---

<!-- PDF page 616 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_146_744_618.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 9.72 Error of having duplicate Observations IDs.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Component</th><th style='text-align: center;'>R2 Cumulative</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S₁</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>0.63993649...</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S₁</td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>0.85610948...</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S₁</td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>0.90587804...</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S₁</td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>0.93993649...</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Model Component Summary for X-S₁</td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>0.9611891...</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>[1]</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>[2]</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>[3]</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>[4]</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>Model 1 - Table</td><td style='text-align: center;'>[5]</td><td style='text-align: center;'>5.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.73 R2 and Q2 values versus the number of principal component.</div>


(batches 50–55) depicted in the score plot of Figure 9.69 resulting from applying the BWU approach. The loading plot on the right of Figure 9.74 shows some variables located closely together that are correlated and some variables that lie on the opposite sides of the plot that are negatively correlated.

We conclude that the BWU approach is more effective than observation-wise unfolding (OWU) for batch data analytics.

---

<!-- PDF page 617 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>T[k]</th><th style='text-align: center;'>T[k] - 1</th><th style='text-align: center;'>T[k] - 2</th><th style='text-align: center;'>T[k] - 3</th><th style='text-align: center;'>T[k] - 4</th><th style='text-align: center;'>T[k] - 5</th><th style='text-align: center;'>T[k] - 6</th><th style='text-align: center;'>T[k] - 7</th><th style='text-align: center;'>T[k] - 8</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Label</th><th style='text-align: center;'>P[k]</th><th style='text-align: center;'>P[k] Error Bar</th><th style='text-align: center;'>P[k] Error Bar</th><th style='text-align: center;'>P[k] Error Bar</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>X1</td><td style='text-align: center;'>-0.28</td><td style='text-align: center;'>[-0.29, -0.27]</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.29, -0.27]</td></tr>
    <tr><td style='text-align: center;'>X2</td><td style='text-align: center;'>-0.27</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.29, -0.27]</td></tr>
    <tr><td style='text-align: center;'>X3</td><td style='text-align: center;'>-0.26</td><td style='text-align: center;'>[-0.27, -0.25]</td><td style='text-align: center;'>[-0.27, -0.25]</td><td style='text-align: center;'>[-0.28, -0.26]</td></tr>
    <tr><td style='text-align: center;'>X4</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>[0.27, 0.29]</td><td style='text-align: center;'>[0.26, 0.28]</td><td style='text-align: center;'>[0.25, 0.27]</td></tr>
    <tr><td style='text-align: center;'>X5</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>[0.27, 0.29]</td><td style='text-align: center;'>[0.26, 0.28]</td><td style='text-align: center;'>[0.25, 0.27]</td></tr>
    <tr><td style='text-align: center;'>X6</td><td style='text-align: center;'>0.32</td><td style='text-align: center;'>[0.31, 0.33]</td><td style='text-align: center;'>[0.30, 0.32]</td><td style='text-align: center;'>[0.29, 0.31]</td></tr>
    <tr><td style='text-align: center;'>X7</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td><td style='text-align: center;'>[0.30, 0.32]</td></tr>
    <tr><td style='text-align: center;'>X8</td><td style='text-align: center;'>0.34</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td></tr>
    <tr><td style='text-align: center;'>X9</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td><td style='text-align: center;'>[0.30, 0.32]</td></tr>
    <tr><td style='text-align: center;'>X10</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>[0.34, 0.36]</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td></tr>
    <tr><td style='text-align: center;'>X11</td><td style='text-align: center;'>0.34</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td></tr>
    <tr><td style='text-align: center;'>X12</td><td style='text-align: center;'>-0.28</td><td style='text-align: center;'>[-0.29, -0.27]</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.29, -0.27]</td></tr>
    <tr><td style='text-align: center;'>X13</td><td style='text-align: center;'>-0.27</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.28, -0.26]</td><td style='text-align: center;'>[-0.29, -0.27]</td></tr>
    <tr><td style='text-align: center;'>X14</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>[0.27, 0.29]</td><td style='text-align: center;'>[0.26, 0.28]</td><td style='text-align: center;'>[0.25, 0.27]</td></tr>
    <tr><td style='text-align: center;'>X15</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>[0.27, 0.29]</td><td style='text-align: center;'>[0.26, 0.28]</td><td style='text-align: center;'>[0.25, 0.27]</td></tr>
    <tr><td style='text-align: center;'>X16</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td><td style='text-align: center;'>[0.30, 0.32]</td></tr>
    <tr><td style='text-align: center;'>X17</td><td style='text-align: center;'>0.34</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td></tr>
    <tr><td style='text-align: center;'>X18</td><td style='text-align: center;'>0.34</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td></tr>
    <tr><td style='text-align: center;'>X19</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>[0.32, 0.34]</td><td style='text-align: center;'>[0.31, 0.33]</td><td style='text-align: center;'>[0.30, 0.32]</td></tr>
    <tr><td style='text-align: center;'>X20</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>[0.34, 0.36]</td><td style='text-align: center;'>[0.33, 0.35]</td><td style='text-align: center;'>[0.32, 0.34]</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.74 T[2] versus T[1] score plot and P[2] versus P[1] loading plot.</div>


### 9.7 Implementation of Multivariate Statistics Models

Should the reader wish to extract the equations and coefficients from developed PCA and PLS models from Aspen ProMV to implement elsewhere, follow the path: Model → Export Model → Model List → Model 1 → Included in Export → Training, Batch, Monitoring, and Alignment Data → Excel, e.g. WS9.2_PLS-XY_WS9.2_PLS-XY.xlsx. Figure 9.75 shows an information summary of the model.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">Aspen ProMV - Model Parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Model Type</td><td style='text-align: center; word-wrap: break-word;'>PLS</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Number of Blocks</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block Names</td><td style='text-align: center; word-wrap: break-word;'>process variables</td><td colspan="3">product quality variables</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Num Tags/Block</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block Widths</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Block Scaling</td><td style='text-align: center; word-wrap: break-word;'>None</td><td style='text-align: center; word-wrap: break-word;'>None</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Num. Components</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Num. Observations (N)</td><td style='text-align: center; word-wrap: break-word;'>54</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Num. Predictor Vars (K)</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Num. Response Vars (M)</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Model Name</td><td style='text-align: center; word-wrap: break-word;'>WS9.2_PLS-XY</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Date/Time</td><td style='text-align: center; word-wrap: break-word;'>2022/02/23-01:37:04</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Notes</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">Figure 9.75 An information summary of the exported model.</div>


---

<!-- PDF page 618 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Model</th><th style='text-align: center;'>Model 1 - Loading Plot</th><th style='text-align: center;'>Model 1 - Table</th><th style='text-align: center;'>Model 2 - Loading Plot</th><th style='text-align: center;'>Model 2 - Table</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>P1 Bar</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>Hot's T2</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>SPE-X</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>VJP</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>ObsVsPred</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>T1-U1</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>W*,c1-W*,c2</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>W*,c1 Bar</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>Coeffs</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9.76 Weights for Y-space.</div>


For example, we see the following Excel folders of the exported model: The various sub-folders in the exported Excel model are as follows.

(1) Scores (T) and loadings (P): See Eqs. (9.8) and (9.17); Figures 9.25 and 9.38.

(2) Weights (W): See Eq. (9.24).

(3) Weights (WStar; W*): See Figure 9.38.

(4) Regression coefficients (coeffs)  $ \beta_{Conv} $,  $ \beta_{Mn} $,  $ \beta_{Mw} $,  $ \beta_{LCB} $, and  $ \beta_{SCB} $: Eq. (9.38)

(5) Y-Weights: See Figure 9.76 below.

If you do not have Aspen ProMV for outlier or anomaly detection, consider using Python that we introduce in Appendix B, Introduction to Python for Chemical Engineers, and refer to Section 10.1.3, Suggested Resources to Get Started with Machine Learning. Adopt the open-source Scikit-Learn PLS library for model building and getting the model coefficients: https://scikitlearn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html.

Additionally, in Section 10.2.3 and Table 10.5 of Chapter 10, we introduce additional machine learning-based methods for outlier or anomaly detection, which can be implemented by Python. Two of the popular methods are Density-Based Spatial Clustering of Applications with Noise (DBSCAN) (Section 10.2.3.4) and Gaussian mixture model (GMM) (Section 10.2.3.5).

Most of the multivariate statistical models in this chapter and machine-learning models in Chapters 10 and 11 use historical data. For online implementation, we need a real-time plant historian, such as Aspen InfoPlus.21 and Aspen Process Explorer, to demonstrate online model deployment. For example, Aspen Technology, Inc. has several software tools, such as Aspen Process Pulse™ and Aspen Scrambler™, to enable the monitoring, controlling, and optimizing of processes with real-time visibility of all types of process and spectral data. Interested readers may refer to Sharmin et al. [24] about a PCA-based fault-detection scheme for an industrial high-pressure polyethylene reactor using Aspen Process Explorer.

---

<!-- PDF page 619 -->

### 9.8 Conclusion and Suggested Resources for Further Studies

In this chapter, we have showcased the utility of latent variable models like PCA and PLS for causal analysis to identify correct correlations between inputs and outputs for polymer process application. We identify the dynamic PCA (DPCA) and PLS model utility in dynamic time series process data by considering the measurement lags. We also demonstrate the methodology for BWU and OWU analyses of batch data.

For further studies, we recommend Refs. [21, 25, 26] in the below section. We discuss a number of topics, together with their relevant references, below.

Gracia-Munoz et al. [25] discussed the issue of time alignment in batch processes. Specifically, in many batch processes, batches can be of different time durations within certain phases or across the entire batch evaluation. A search of Aspen ProMV online help gives details and examples of alignment tools and their implementation in batch processes.

Park et al. [20] and Han et al. [26] presented interesting case studies of applying PLS and machine-learning tools (support vector machines and artificial neural networks) to modeling the melt index of high-density polyethylene (HDPE), styrene-acrylonitrile (SAN), and polypropylene (PP) processes operating in Korea.

Chen and Lu [21] integrated ARMAX time series model with PCA model and called it DPCA that involves the use of time lags, which we discussed in Sections 9.5.1 and 9.5.2. They also combined three-way OWU PLS (Section 9.6.1) with time-lagged windows and called it batch DPLS (BDPLS). They applied both methods to industrial batch polymerization datasets.

## References

1 Quantrille, T.E. and Liu, Y.A. (1991). Artificial Intelligence in Chemical Engineering. San Diego, CA (now Elsevier, New York): Academic Press, Inc.

2 Baughman, D.R. and Liu, Y.A. (1995). Neural Networks in Bioprocessing and Chemical Engineering. San Diego, CA (now Elsevier, New York): Academic Press, Inc.

3 Qin, S.J. (2014). Process data analytics in the era of big data. AIChE Journal 60: 3092–3100.

4 Chiang, L., Lu, B., and Castillo, I. (2017). Big data analytics in chemical engineering. Annual Review of Chemical and Biomolecular Engineering 8: 63.

5 Ge, Z., Song, Z., Ding, S.X., and Huang, B. (2017). Data mining and analytics in the process industry: the role of machine learning. IEEE Access 5: 20590.

6 Skagerberg, B., MacGregor, J.F., and Kiparissides, C. (1992). Multivariate data analysis applied to low-density polyethylene reactors. Chemometrics and Intelligent Laboratory Systems 14: 341.

---

<!-- PDF page 620 -->

7 Kourti, T. and MacGregor, J.F. (1995). Process analysis, monitoring and diagnosis using multivaraite projection methods. Chemometrics and Intelligent Laboratory Systems 28: 3.

8 MacGregor, J.F. and Kourti, T. (1995). Statistical process control of multivariate processes. Control Engineering Practice 3: 403.

9 MacGregor, J.F. (1997). Using on-line process data to improve quality: challenges for statisticians. International Statistical Review 65: 309.

10 MacGregir, J.F. and Bruwer, M.-J. (2017). Optimization of processes and products using historical data. Foundations of Computer Aided Process Operations / Chemical Process Control Conference, St. Antonio, Texas, January 2017. https://docplayer.net/42981979-Optimization-of-processes-products-using-historical-data.html (accessed 15 January 2022).

11 Johnson, R.A. and Wichern, D.W. (2013). Applied Multivariate Statistical Analysis, 6e. New York: Pearson Education, Inc.

12 Rencher, A.C. and Christiansen, W.F. (2012). Methods of Multivariate Analysis, 3e. New York: Wiley.

13 Dunn, K. (2023). Process improvement using data. Creative Commons Attribution-ShareAlike. https://learnche.org/pid/ (accessed 25 March 2023).

14 Aspen Technology, Inc. (2003). Training Course on Inferential Property Development and Control with Aspen IQ and DMCplus: Multivariate Statistics.

15 Everett, B. and Hothorn, T. (2011). An Introduction to Applied Multivariate Analysis with R. New York: Springer.

16 Wold, S. (1978). Cross-validatory estimation of the number of components in factor and principal component models. Technometrics 20: 397.

17 Dunn, K. (2023). LDPE Dataset. All OpenMV.net Databases. https://openmv.net/ (accessed 25 March 2023).

18 Wold, S., Sjostrom, M., and Erikson, L. (2001). PLS-regression: a basic tool for chemometrics. Chemometrics and Intelligent Laboratory Systems 58: 109.

19 Geladi, P. and Kowalski, B.R. (1986). Partial least-squares regression: a tutorial. Analytica Chimica Acta 185: 1.

20 Park, T.C., Kim, T.Y., and Yeo, Y.K. (2010). Prediction of the melt flow index using partial least squares and support vector regression in high-density polyethylene (HDPE) process. Korean Journal of Chemical Engineering 27: 1662.

21 Chen, J. and Liu, K.C. (2002). On-line batch process monitoring using dynamic PCA and dynamic PLS models. Chemical Engineering Science 57: 63.

22 Wold, S., Geladi, P., Esbensen, K., and Ohman, J. (1987). Multiway principal components and PLS analysis. Journal of Chemometrics 1: 41.

23 Nomikos, P. and MacGregor, J.F. (1994). Monitoring batch processes using multi-way principal component analysis. AIChE Journal 40: 1361.

24 Sharmin, R., Shah, S.L., and Sundararaj, U. (2008). A PCA based fault detection scheme for an industrial high pressure polyethylene reactor. Macromolecular Reaction Engineering 2: 12.

---

<!-- PDF page 621 -->

25 Garcia-Munoz, S., Khouri, T., MacGregor, J.F. et al. (2003). Troubleshooting of an industrial batch process using multivariate methods. Industrial and Engineering Chemistry Research 42: 3592.

26 Han, I.-S., Han, C., and Chung, C.-B. (2005). Melt index modeling with support vector machines, partial least squares, and artificial networks. Journal of Applied Polymer Science 95: 967.

---

<!-- PDF page 622 — MISSING, not yet parsed -->
