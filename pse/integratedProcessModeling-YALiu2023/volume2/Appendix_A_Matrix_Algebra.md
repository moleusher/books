# Appendix A. Matrix Algebra in Multivariate Data Analysis and MPC

<!-- PDF page 789 -->

## Appendix A

## Matrix Algebra in Multivariate Data Analysis and Model Predictive Control

This appendix discusses the basic elements of matrix algebra used in multivariate data analysis and in model predictive control. It is essentially a review of the requisite matrix tools and does not include complete development. We present most of the known theoretical results from general textbooks of matrix algebra without proof. Our focus is to present sufficient background from matrix algebra in order to enable its implementation by software tools, including MATLAB, Python, and R.

### A.1 Important Matrices in Multivariate Data Analysis

#### A.1.1 Data Matrix X

The most important matrix for any statistical procedure is the data matrix. We consider a  $ J \times K $ process data matrix  $ \mathbf{X} $, with  $ K $ columns of process variables  $ x_k $ ( $ k = 1, 2, \ldots, K $), and with each variable  $ x_k $ having  $ J $ observations or measured values,  $ x_{1k}, x_{2k}, x_{3k}, \ldots, x_{Jk} $ (or  $ x_{jk}, j = 1, 2, \ldots, J $). We use uppercase boldface letters to represent matrices and lowercase boldface letters to represent vectors. For example, a  $ 5 \times 3 $ data matrix  $ \mathbf{X} $ consists of three process variable vectors,  $ \mathbf{x}_1, \mathbf{x}_2 $, and  $ \mathbf{x}_3 $:

 $$ \mathbf{X}=[\mathbf{x}\mathbf{1}\mathbf{\Lambda}\mathbf{x}\mathbf{2}\mathbf{\Lambda}\mathbf{x}\mathbf{3}]=\begin{bmatrix}{{{5}}}&{{{1}}}&{{{8}}} \\{{{3}}}&{{{2}}}&{{{5}}} \\{{{2}}}&{{{2}}}&{{{5}}} \\{{{4}}}&{{{3}}}&{{{7}}} \\{{{1}}}&{{{4}}}&{{{3}}}\end{bmatrix} $$ 

#### A.1.2 Sample Mean  $ \overline{X} $

We find the sample mean of J measurements on each of the K variables by:

 $$ \bar{x}_{k}=\frac{1}{j}*\sum x_{kj} $$ 

The resulting  $ 1 \times K $ sample mean matrix, or row vector, is:

 $$ \overline{x}=[\overline{x}_{1}\ \overline{x}_{2}\ \ldots\ \overline{x}_{k}] $$ 

For our example, the 1 x 3 sample mean matrix, or row vector is:

 $$ \overline{x}=[3\ 2.4\ 5.6] $$ 

---

<!-- PDF page 790 -->

#### A.1.3 Sample Variance,  $ s_{kk} $ or  $ s_{k}^{2} $ and Sample Standard Deviation  $ s_{k} $

We define sample variance  $ s_{11} $ or  $ s_{1}^{2} $ as a measure of spread of the J measurements on the first variable from its sample mean  $ \bar{x}_{1} $:

 $$ s_{1}^{2}=s_{11}=\sum_{j=1}^{J}(x_{j1}-\overline{x_{j}})^{2} $$ 

where  $ \overline{x}_1 $ is the sample mean of the  $ x_{j1} $ ( $ j=1,2,\ldots,J $):

 $$ \bar{x}_{1}=\frac{1}{j}*\sum x_{j1} $$ 

In general, for K variables, we write the sample variance as:

 $$ s_{k}^{2}=s_{k k}=\sum_{j=1}^{J}(x_{j k}-\overline{x}_{k})^{2}\qquad k=1,2,\ldots,K $$ 

We note that some authors define the sample variance with a divisor of J rather than J−1. We follow the definition in [1, 2] and in MATLAB. Using a divisor of J or J−1 gives a slightly different result when J is small. In using any software tools to find the sample variance, we should pay attention to the divisor used.

We call the square root of the sample variance,  $ \sqrt{s_{kk}} $, as the sample standard deviation,  $ s_{k} $ for the kth process variable.

 $$ s_{k}=\sqrt{s_{k k}}=\sqrt{s_{k}^{2}} $$ 

#### A.1.4 Sample Covariance  $ s_{ik} $

Here, we follow the explanation in Ref. [3]. Consider J pairs of measurements for each of process variables 1 and 2:

 $$ \begin{bmatrix}x_{11}\\ x_{12}\end{bmatrix},\begin{bmatrix}x_{21}\\ x_{22}\end{bmatrix},\begin{bmatrix}x_{J1}\\ x_{J2}\end{bmatrix} $$ 

The sampled values of process variables 1 and 2 on the jth experimental item are  $ x_{j1} $ and  $ x_{j2} $, respectively. We define the sample covariance  $ s_{12} $ as a measure of the linear association between the measurements of process variables 1 and 2, or the average product of the deviations from their respective means:

 $$ s_{12}=\frac{1}{J-1}*\sum_{j=1}^{J}(x_{j1}-\overline{x}_{1})^{2}*(x_{j2}-\overline{x}_{2})^{2} $$ 

If the sampled values of variable 1 are large, and the sampled values of variable 2 are also large,  $ s_{12} $ will be positive. Likewise, if small sampled values of both variables 1 and 2 occur together,  $ s_{12} $ will be positive. If the sampled values of variable 1 are large but those of variable 2 are small, then  $ s_{12} $ is negative. If there is no particular association between the values of the two variables,  $ s_{12} $ will be approximately zero.

For K variables, we write the sample covariance as:

 $$ s_{jk}=\frac{1}{J-1}*\sum_{j=1}^{J}(x_{ji}-\overline{x}_{i})(x_{jk}-\overline{x}_{k})\quad i=1,2,\ldots,k\quad j=1,2,\ldots,K $$ 

---

<!-- PDF page 791 -->

#### A.1.5 Sample Correlation Coefficient  $ r_{ik} $

To quantify the linear association between two variables that is invariant to changes in scale, we can standardize the covariance by dividing by the standard deviations of the two variables. We call this standardized covariance a sample correlation coefficient for the ith and kth variables:

 $$ r_{ik}=\frac{s_{ik}}{\sqrt{s_{ii}}\sqrt{s_{kk}}}=\frac{\sum_{j=1}^{J}(x_{ji}-\overline{x}_{i})(x_{jk}-\overline{x}_{k})}{\sqrt{\sum_{j=1}^{J}(x_{ji}-\overline{x}_{i})^{2}}*\sqrt{\sum_{j=1}^{J}(x_{ki}-\overline{x}_{k})^{2}}} $$ 

for  $ i=1,2,\ldots,K $; and  $ k=1,2,\ldots,K $. Note that  $ r_{ik}=r_{ki} $ for all  $ i $ and  $ k $.

We note that the sample correlation coefficient is a standardized version of the sample covariance, where the product of the square roots of the sample variances provides the standardization. Additionally,  $ r_{ik} $ has the same value whether we use J or J-1 as the common divisor for sample variances  $ s_{ii} $,  $ s_{kk} $, or  $ s_{ik} $.

For our example, Eq. (A.4) gives the sample averages:

 $$ \begin{aligned}\overline{x}_{1}&=3\quad\overline{x}_{2}=2.4\quad\overline{x}_{3}=5.6\end{aligned} $$ 

We can find the sample variances and covariances as follows:

 $$ \begin{aligned}&s_{11}=2.5&s_{22}=1.3&s_{33}=3.8\\ &\\&s_{12}=s_{21}=-1.25&s_{13}=s_{31}=3.0&s_{23}=s_{32}=-1.55\\ \end{aligned} $$ 

Therefore, the sample variance and covariance matrix S is:

 $$ \mathbf{S}=\begin{bmatrix}{{{s_{11}}}}&{{{s_{12}}}}&{{{s_{13}}}} \\{{{s_{21}}}}&{{{s_{22}}}}&{{{s_{23}}}} \\{{{s_{31}}}}&{{{s_{32}}}}&{{{s_{33}}}}\end{bmatrix}=\begin{bmatrix}{{{2.5}}}&{{{-1.25}}}&{{{3}}} \\{{{-1.25}}}&{{{1.3}}}&{{{-1.55}}} \\{{{3}}}&{{{-1.55}}}&{{{3.8}}}\end{bmatrix} $$ 

The sample correlation coefficients are:

 $$ \begin{aligned}&r_{12}=r_{21}=\frac{s_{12}}{\sqrt{s_{11}}\sqrt{s_{22}}}=-\frac{1.25}{\sqrt{2.5}\sqrt{1.3}}=-0.6934\\ &\\ &r_{13}=r_{31}=\frac{s_{13}}{\sqrt{s_{11}}\sqrt{s_{33}}}=\frac{3}{\sqrt{2.5}\sqrt{3.8}}=0.9733\\ &\\ &r_{23}=r_{32}=\frac{s_{23}}{\sqrt{s_{22}}\sqrt{s_{33}}}=-\frac{1.55}{\sqrt{1.3}\sqrt{3.8}}=-0.6974\\ &\\ &r_{11}=r_{22}=r_{33}=1.0\\ \end{aligned} $$ 

The resulting sample correlation coefficient matrix R is:

 $$ \mathbf{R}=\begin{bmatrix}r_{11}&r_{12}&r_{13}\\ r_{21}&r_{22}&r_{23}\\ r_{31}&r_{32}&r_{33}\end{bmatrix}=\begin{bmatrix}1.0&-0.6934&0.9733\\ -0.6934&1.0&-0.6974\\ 0.9733&-0.6974&1.0\end{bmatrix} $$ 

---

<!-- PDF page 792 -->

#### A.1.6 Mean-Centered Data Matrix or Deviation Matrix  $ X_{d} $, and Diagonal Matrix of the Inverse of the Standard Deviation  $ D_{s} $

We can generate the sample variances and covariances for all process variables through a series of matrix operations involving a deviation matrix  $ \mathbf{X}_d $ and a diagonal matrix of the standard deviation  $ \mathbf{D}_s $.

We define a  $ J \times K $ deviation matrix,  $ X_d $, by subtracting the respective sample mean from each element of the data matrix

 $$ \mathbf{X}_{\mathrm{d}}=\mathbf{X}-\overline{\mathbf{X}} $$ 

where the columns of the $J \times K$ sample mean matrix $\overline{X}$ are simply the $K \times 1$ column vector having identical column elements $X_k$ ($k = 1, 2, \ldots, K$). For our example, $\mathbf{X}_d$ is

 $$ \mathbf{X}_{\mathbf{d}}=\begin{bmatrix}{{{5}}}&{{{1}}}&{{{8}}} \\{{{3}}}&{{{2}}}&{{{5}}} \\{{{2}}}&{{{2}}}&{{{5}}} \\{{{4}}}&{{{3}}}&{{{7}}} \\{{{1}}}&{{{4}}}&{{{3}}}\end{bmatrix}-\begin{bmatrix}{{{3}}}&{{{2.4}}}&{{{5.6}}} \\{{{3}}}&{{{2.4}}}&{{{5.6}}} \\{{{3}}}&{{{2.4}}}&{{{5.6}}} \\{{{3}}}&{{{2.4}}}&{{{5.6}}} \\{{{3}}}&{{{2.4}}}&{{{5.6}}}\end{bmatrix}=\begin{bmatrix}{{{2}}}&{{{-1.4}}}&{{{2.4}}} \\{{{0}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{-1}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{1}}}&{{{0.6}}}&{{{1.4}}} \\{{{-2}}}&{{{0.6}}}&{{{2.6}}}\end{bmatrix} $$ 

We define a diagonal matrix  $ \mathbf{D}_s $ with  $ k $th diagonal element being the inverse of the standard deviation or the square root of the sample variance of the  $ k $th process variable, while all other nondiagonal elements of the matrix are zero:

 $$ \mathbf{D}_{\mathbf{s}}=\begin{bmatrix}{{{\frac{1}{\sqrt{s_{11}}}}}}&{{{\cdots}}}&{{{0}}} \\{{{\vdots}}}&{{{\ddots}}}&{{{\vdots}}} \\{{{0}}}&{{{\cdots}}}&{{{\frac{1}{\sqrt{s_{kk}}}}}}\end{bmatrix} $$ 

For our example with three process variables, the diagonal matrix  $ D_{s} $ is:

 $$ \mathbf{D}_{\mathbf{s}}=\begin{bmatrix}{{{\frac{1}{\sqrt{s_{11}}}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{\frac{1}{\sqrt{s_{22}}}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{\frac{1}{\sqrt{s_{33}}}}}}\end{bmatrix}=\begin{bmatrix}{{{\frac{1}{\sqrt{2.5}}}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{\frac{1}{\sqrt{1.3}}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{\frac{1}{\sqrt{3.8}}}}}\end{bmatrix}=\begin{bmatrix}{{{0.6325}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0.8771}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0.5130}}}\end{bmatrix} $$ 

#### A.1.7 Sum of Squares and Cross Products (SSCP), and Sample Variance and Covariance Matrix S

The sum of squares of the deviations from the mean and the sum of cross-product deviations are useful in multivariate data analysis. These quantities are:

 $$ w_{k k}=\sum_{j=1}^{J}(x_{j k}-\overline{{x}}_{k})^{2}\qquad\quad k=1,2,\ldots,K $$ 

and

 $$ w_{i k}=\sum_{j=1}^{J}(x_{j i}-\overline{x}_{i})(x_{j i}-\overline{x}_{k})\qquad i=1,2,\ldots,K\qquad k=1,2,\ldots,K $$ 

---

<!-- PDF page 793 -->

We can obtain both the sum of squares and cross products (SSCP) by multiplying the transpose of the deviation matrix  $ \mathbf{X}_d^\mathrm{T} $ by the deviation matrix  $ \mathbf{X}_d $ [2, 3]:

 $$ \mathbf{S S C P}=\mathbf{X}_{\mathrm{d}}^{\mathrm{T}}*\mathbf{X}_{\mathrm{d}} $$ 

For our example, we have

 $$ \mathbf{SSCP}=\begin{bmatrix}{{{2}}}&{{{0}}}&{{{-1}}}&{{{1}}}&{{{-2}}} \\{{{-1.4}}}&{{{-0.4}}}&{{{-0.4}}}&{{{0.6}}}&{{{1.6}}} \\{{{2.4}}}&{{{-0.6}}}&{{{-0.6}}}&{{{1.4}}}&{{{2.6}}}\end{bmatrix}*\begin{bmatrix}{{{2}}}&{{{-1.4}}}&{{{2.4}}} \\{{{0}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{-1}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{1}}}&{{{0.6}}}&{{{1.4}}} \\{{{-2}}}&{{{1.6}}}&{{{2.6}}}\end{bmatrix}=\begin{bmatrix}{{{10}}}&{{{-5}}}&{{{12}}} \\{{{-5}}}&{{{5.2}}}&{{{-6.2}}} \\{{{12}}}&{{{-6.2}}}&{{{15.2}}}\end{bmatrix} $$ 

We can find the sample variance and covariance matrix S from SSCP:

 $$ \mathbf{S}=\frac{1}{J-1}*\mathbf{SSCP}=\frac{1}{J-1}*\mathbf{X_{d}^{T}}*\mathbf{X_{d}} $$ 

For our example, we have:

 $$ \mathbf{S}=\frac{1}{5-1}*\mathbf{SSCP}=\frac{1}{4}*\begin{bmatrix}{{{10}}}&{{{-5}}}&{{{12}}} \\{{{-5}}}&{{{5.2}}}&{{{-6.2}}} \\{{{12}}}&{{{-6.2}}}&{{{15.2}}}\end{bmatrix}=\begin{bmatrix}{{{2.5}}}&{{{-1.25}}}&{{{3}}} \\{{{-1.25}}}&{{{1.3}}}&{{{-1.55}}} \\{{{3}}}&{{{-1.55}}}&{{{3.8}}}\end{bmatrix} $$ 

which is identical to Eq. (A.12).

#### A.1.8 Standardized Data Matrix, or Mean-Centered and Scaled Data Matrix  $ X_{s} $, and Sample Correlation Coefficient Matrix R

The standardized data matrix  $ \mathbf{X}_s $ results from scaling the mean-centered data matrix, or the deviation matrix  $ \mathbf{X}_d $, in standard deviation units.

Quantitatively, let us consider the sample correlation coefficients for the ith and kth variables, Eq. (A.11), again:

 $$ r_{ik}=\frac{s_{ik}}{\sqrt{s_{ii}}\sqrt{s_{kk}}}=\frac{\sum_{j=1}^{J}(x_{ji}-\overline{x}_{i})(x_{jk}-\overline{x}_{k})}{\sqrt{\sum_{j=1}^{J}(x_{ji}-\overline{x}_{i})^{2}}*\sqrt{\sum_{j=1}^{J}(x_{ki}-\overline{x}_{k})^{2}}} $$ 

Suppose that we replace the original values  $ x_{ji} $ and  $ x_{jk} $ by their standardized values  $ (x_{ji} - \bar{x}_i)/s_{ii} $ and  $ (x_{jk} - \bar{x}_k)/s_{kk} $. These standardized values for  $ x_{ji} $ and  $ x_{jk} $ are measurable by the same standard because both sets of data are mean-centered (“centered at zero”) and expressed in standard deviation units. The sample correlation coefficient is just the sample covariance of the standardized observations [3].

We find the standardized data matrix  $ \mathbf{X}_s $ by simply multiplying the deviation matrix  $ \mathbf{X}_d $, Eq. (A.14), by the diagonal matrix  $ \mathbf{D}_s $, Eq. (A.16):

 $$ \mathbf{X}_{\mathrm{s}}=\mathbf{X}_{\mathrm{d}}*\mathbf{D}_{\mathrm{s}} $$ 

We find the corresponding sample correlation coefficient matrix R by

 $$ \mathbf{R}=\left[\frac{1}{J-1}\right]\mathbf{X}_{\mathrm{s}}^{\mathrm{T}}*\mathbf{X}_{\mathrm{s}} $$ 

---

<!-- PDF page 794 -->

For our example, we have:

 $$ \begin{aligned}\mathbf{X}_{s}&=\mathbf{X}_{d}*\mathbf{D}_{s}=\begin{bmatrix}{{{2}}}&{{{-1.4}}}&{{{2.4}}} \\{{{0}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{-1}}}&{{{-0.4}}}&{{{-0.6}}} \\{{{1}}}&{{{0.6}}}&{{{1.4}}} \\{{{-2}}}&{{{1.6}}}&{{{2.6}}}\end{bmatrix}*\begin{bmatrix}{{{0.6325}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0.8771}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0.5130}}}\end{bmatrix}\\&=\begin{bmatrix}{{{1.2650}}}&{{{-1.2279}}}&{{{1.2312}}} \\{{{0}}}&{{{-0.3508}}}&{{{-0.3078}}} \\{{{-0.6325}}}&{{{-0.3508}}}&{{{-0.3078}}} \\{{{0.6325}}}&{{{0.5263}}}&{{{0.7182}}} \\{{{-1.2650}}}&{{{1.4034}}}&{{{-1.338}}}\end{bmatrix}\end{aligned} $$ 

 $$ \boldsymbol{R}=\frac{1}{4}*\mathbf{X}_{\mathrm{S}}^{\mathrm{T}}*\mathbf{X}_{\mathrm{S}}=\begin{bmatrix}1&-0.6934&0.9734\\ -0.6934&1&-0.6974\\ 0.9734&-0.6974&1\end{bmatrix} $$ 

which is identical to the sample correlation coefficient matrix R given in Eq. (A. 13).

#### A.1.9 A Summary: Three Important Matrices in Multivariate Data Analysis

Carey [4] gives some useful insights on the three important matrices in multivariate data analysis that we have discussed so far: (1) matrix of sample means  $ \overline{X} $; (2) diagonal matrix of sample standard deviations,  $ \mathbf{D}_s $; and (3) sample correlation coefficient matrix.  $ \mathbf{R} $. We follow his discussion below.

The matrix of sample means X shows us where variables are located along the number lines in a multidimensional space. For example, a vector consisting of two means tells us where the “dots” in a scatter plot are centered, and a vector of three means shows us where the dots in a three-dimensional space are centered.

The diagonal matrix of sample standard deviations,  $ D_s $, is a measure of the extent to which the dots in space are spread out around their center. We can think of standard deviations as “scaling factors” for the variables, analogous to currency conversions. For example, if variable  $ x_1 $ has a standard deviation of 3 and variable  $ x_2 $ has a standard deviation of 1.5, then one unit of  $ x_1 $ is “worth” 2 units of  $ x_2 $, and one unit of  $ x_2 $ is “worth” 0.5 units of  $ x_1 $.

Finally, the sample correlation coefficient matrix (or simply the correlation matrix)  $ \mathbf{R} $ expresses the geometric shape of the dots in a hyperspace when each variable is measured on the same scale (i.e. each variable has a standard deviation of 1.0).

Specifically, the correlation matrix R informs us about the extent to which the dots are spherical or elliptical in various dimensions. For example, the correlation matrix for two variables tells us whether the dots in a scatter diagram are circular (when the correlation is close to 0), elliptical (when the correlation is greater than 0, but not close to 1.0 or -1.0), or approach forming a straight line (when the correlation approaches 1.0 or -1.0). The correlation matrix also indicates the direction of the

---

<!-- PDF page 795 -->

dots. For example, a positive correlation for two variables implies that the dots are oriented from the “southwest towards the northeast,” while a negative correlation denotes that the dots are going from the “northwest towards the southeast.”

To summarize, we use three summary statistics to quantify three properties of the data points in a hyperspace. The first property is location and is summarized by the means. The second property is spread or scale and is summarized by the standard deviations. The third property is shape and is summarized by the correlations.

### A.2 Review of Selected Matrix Concepts

#### A.2.1 Rank of a Data Matrix

We call a set of data vectors,  $ \mathbf{x}_1, \mathbf{x}_2, \ldots \mathbf{x}_K $ linearly dependent if there are constants  $ c_1, c_2, \ldots, c_K $ (not all zero) to satisfy

 $$ c1\mathbf{x}_{1}+c2\mathbf{x}_{2}+\cdots+ck\mathbf{x}_{\mathbf{k}}=0 $$ 

If we cannot find any constants  $ c_1 $,  $ c_2 $, ...,  $ c_k $ to satisfy Eq. (A.25), we call the set of data vectors  $ x_1, x_2, ..., x_k $ linearly independent.

The rank of any data matrix  $ \mathbf{X} $, rank( $ \mathbf{X} $), refers to the number of linearly independent rows (or columns) of  $ \mathbf{X} $. We can show that the number of linearly independent rows of a matrix is always equal to the number of linearly independent columns [2].

The rank of our  $ 5 \times 3 $ data matrix, X, Eq. (A.1), is

 $$ \mathrm{rank}(\mathbf{X})=3 $$ 

In general, for a  $ J \times K $ process data matrix  $ \mathbf{X} $, the maximum possible rank of  $ \mathbf{X} $ is the smaller of  $ J $ and  $ K $, in which case,  $ \mathbf{X} $ is said to be of full rank (sometimes said full row rank or full column rank).

#### A.2.2 Inverse of A Matrix

If a matrix A is square (that is, with an equal number of rows and columns) and of full rank, A is said to be nonsingular, and A has a unique inverse, denoted by A^{-1}. The inverse satisfies the relationship

 $$ \mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=1 $$ 

where I is an identity matrix with diagonal elements being 1 and nondiaqonal elements being 0.

#### A.2.3 Determinant of A Matrix

The determinant of a $n \times n$ matrix $\mathbf{A}$, denoted by $|\mathbf{A}|$, is defined as the scalar sum of $n$! possible products of $n$ elements such that: (1) Each product contains one element from every row and every column, and (2) we write the factors in each product so that the column subscripts appear in order of magnitude, and we add a plus or minus

---

<!-- PDF page 796 -->

sign before each product according to whether the number of inversions in the row subscripts is even or odd. An inversion occurs whenever a larger number precedes a smaller one.

This definition is not useful to find the scalar value of  $ |\mathbf{A}| $, except for  $ 2 \times 2 $ or  $ 3 \times 3 $ matrixes. For example:

 $$ \begin{aligned}\left|\mathbf{A}\right|&=\left|\begin{matrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{matrix}\right|=a_{11}a_{22}-a_{21}a_{12}\\\left|\mathbf{A}\right|&=\left|\begin{matrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{matrix}\right|=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{32}a_{21}\\&\quad-a_{31}a_{22}a_{13}-a_{32}a_{23}a_{11}-a_{33}a_{12}a_{21}\end{aligned} $$ 

For larger matrices, we need software tools to find the determinant value, as we discuss in Section A.3.

#### A.2.4 Orthogonal Vectors and Matrices

We define two vectors  $ \mathbf{a} $ and  $ \mathbf{b} $ with elements  $ a_i $ and  $ b_i $ ( $ i = 1, 2, \ldots, n $):

 $$ \mathbf{a}=[a_{1}\;a_{2}\ldots\ldots a_{n}]^{\prime}\qquad\qquad\mathbf{b}=[b_{1}b_{2}\ldots\ldots b_{n}]^{\prime} $$ 

where we use a superscript “T” or an apostrophe (/) to indicate the transpose of a vector or matrix.

Vectors a and b are orthogonal if

 $$ \mathbf{a}^{\prime}\mathbf{b}=a_{1}b_{1}+a_{2}b_{2}+\cdots\cdots+a_{n}b_{n}=0 $$ 

Geometrically, two orthogonal vectors are perpendicular to each other.

Additionally, if  $ \mathbf{a}' \mathbf{a} = 1 $, we call the vector  $ \mathbf{a} $ normalized. We can make vector  $ \mathbf{a} $ normalized by dividing by its norm or length  $ \sqrt{\mathbf{a}' \mathbf{a}} $. Therefore, vector  $ \mathbf{c} $ is normalized if  $ \mathbf{c}' \mathbf{c} = 1 $ and

 $$ \mathbf{c}=\mathbf{a}/\sqrt{\mathbf{a}^{\prime}\mathbf{a}}=\mathbf{a}/\mathbf{norm}(\mathbf{a}) $$ 

We can extend the orthogonal and normalized concepts to matrices. A matrix  $ \mathbf{C} = [c_1 c_2 \ldots c_n] $ is called orthogonal if its column vectors  $ \mathbf{c}_1 \mathbf{c}_2 \ldots \mathbf{c}_n $ are normalized and mutually orthogonal. This implies that

 $$ \mathbf{c}^{\prime}\mathbf{c}=\mathbf{I} $$ 

where I is an  $ n \times n $ identity matrix with all diagonal elements being 1, and nondia-

onal elements being 0.

#### A.2.5 Eigenvalues and Eigenvectors

The concepts of eigenvalues and eigenvectors are important in multivariate data analysis, such as principal component analysis (PCA).

For every square matrix A, we can find a scalar  $ \lambda $ and a nonzero vector x such that

 $$ \mathbf{A}\mathbf{x}=\lambda\mathbf{x} $$ 

---

<!-- PDF page 797 -->

We call  $ \lambda $ an eigenvalue of A and x an eigenvector. To find  $ \lambda $ and x, we write Eq. (A.32) as

 $$ (\mathbf{A}-\lambda\mathbf{I})\mathbf{x}=0 $$ 

We call this equation the characteristic equation of matrix A. For example, the characteristic equation for the matrix

 $$ A=\begin{bmatrix}{{{7}}}&{{{3}}} \\{{{3}}}&{{{-1}}}\end{bmatrix} $$ 

is

 $$ \left|\mathbf{A}-\lambda\mathbf{I}\right|=\left|\begin{matrix}{{{7-\lambda}}}&{{{3}}} \\{{{3}}}&{{{-1-\lambda}}}\end{matrix}\right|=(7-\lambda)(-1-\lambda)-9=\lambda^{2}-6\lambda-16=0 $$ 

from which we find the eigenvalues as  $ \lambda_{1}=8,\lambda_{2}=-2 $.

To find the corresponding eigenvectors, we write Eq. (A.33) as

 $$ \left(\mathbf{A}-\lambda\mathbf{I}\right)\mathbf{x}=\begin{bmatrix}{{{7-\lambda}}}&{{{3}}} \\{{{3}}}&{{{-1-\lambda}}}\end{bmatrix}\begin{bmatrix}{{{x_{11}}}} \\{{{x_{21}}}}\end{bmatrix}=\begin{bmatrix}{{{0}}} \\{{{0}}}\end{bmatrix} $$ 

For  $ \lambda_{1}=8 $, the eigenvector is:

 $$ x_{1}=\begin{bmatrix}1\\ 3\end{bmatrix} $$ 

For  $ \lambda_{2} = -2 $, the eigenvector is:

 $$ \boldsymbol{x}_{2}=\begin{bmatrix}1\\ -3\end{bmatrix} $$ 

For  $ 3 \times 3 $ or larger matrices, we need software tools to find eigenvalues and eigenvectors, which we will discuss in Section A.2.5.

#### A.2.6 Factorization or Decomposition of Matrices

Factorization or decomposition of matrices tries to express a given matrix A as a product of two or three other matrices, BC or BCD. A number of such decompositions, such as singular value decomposition (SVD), are useful in PCA in multivariate data analysis [2, 3] and in the pairing of manipulated and control variables in multivariable predictive control [5–7, 10]. We introduce several below.

##### A.2.6.1 LU Factorization

LU factorization converts a square matrix A of an equal number of rows and columns into a product of a lower triangular matrix L with elements being zero below the diagonal and an upper diagonal matrix U with elements being zero above the diagonal:

 $$ \mathbf{A}=\mathbf{L}*\mathbf{U} $$ 

---

<!-- PDF page 798 -->

For a  $ 3 \times 3 $ square matrix A, we write:

 $$ \mathbf{A}=\begin{bmatrix}{{{8}}}&{{{1}}}&{{{6}}} \\{{{3}}}&{{{5}}}&{{{7}}} \\{{{4}}}&{{{9}}}&{{{2}}}\end{bmatrix} $$ 

As an example, we write:

 $$ \begin{bmatrix}{{{8}}}&{{{1}}}&{{{6}}} \\{{{3}}}&{{{5}}}&{{{7}}} \\{{{4}}}&{{{9}}}&{{{2}}}\end{bmatrix}=\boldsymbol{L}*\boldsymbol{U}=\begin{bmatrix}{{{1}}}&{{{0}}}&{{{0}}} \\{{{0.3750}}}&{{{0.5441}}}&{{{1}}} \\{{{0.5}}}&{{{1}}}&{{{0}}}\end{bmatrix}*\begin{bmatrix}{{{8}}}&{{{1}}}&{{{6}}} \\{{{0}}}&{{{8.5}}}&{{{-1}}} \\{{{0}}}&{{{0}}}&{{{5.2941}}}\end{bmatrix} $$ 

##### A.2.6.2 Cholesky Factorization

A  $ I \times J $ matrix A is symmetric if it has elements  $ a_{ij} $ equal to  $ a_{ji} $. An example is:

 $$ \mathbf{A}=\begin{pmatrix}{{{3}}}&{{{0}}}&{{{-3}}} \\{{{0}}}&{{{6}}}&{{{3}}} \\{{{-3}}}&{{{3}}}&{{{6}}}\end{pmatrix} $$ 

A symmetric matrix is positive definite if  $ \mathbf{x}'\mathbf{A}\mathbf{x}>0 $ for all possible vectors  $ \mathbf{x} $ (except  $ \mathbf{x}=0 $). We can factor a positive definite matrix  $ \mathbf{A} $ into

 $$ \mathbf{A}=\mathbf{T}^{\prime}*\mathbf{T} $$ 

where matrix T is an upper triangular matrix “whose determinant is not zero” (that is, “nonsingular”).

Let  $ \mathbf{A} = (a_{ij}) $ and  $ \mathbf{T} = (t_{ij}) $ with  $ i $ and  $ j = 1, 2, \ldots, n $. We can find the elements of  $ \mathbf{T} $ as follows [2]:

 $$ \begin{aligned}&t_{11}=\sqrt{a_{11}}\quad t_{1j}=\frac{u_{ij}}{t_{11}}\quad2\leq j\leq n\\ &\\ &t_{i1}=\sqrt{a_{ii}-\sum_{j=1}^{i-1}t_{ki}^{2}}\quad2\leq i\leq n\\ &\\ &t_{ij}=\frac{a_{ij}-\sum_{k=1}^{i-1}t_{ki}t_{kj}}{t_{ii}}\quad2\leq i<j\leq n\\ &\\ &t_{ij}=0\quad i\leq j<i\leq n\\ \end{aligned} $$ 

It is convenient to apply software tools to find the L and U matrices. For our example, we can find:

 $$ \mathbf{A}=\mathbf{T}^{\prime}*\mathbf{T}=\begin{pmatrix}{{{3}}}&{{{0}}}&{{{-3}}} \\{{{0}}}&{{{6}}}&{{{3}}} \\{{{-3}}}&{{{3}}}&{{{6}}}\end{pmatrix}=\begin{pmatrix}{{{\sqrt{3}}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{\sqrt{6}}}}&{{{0}}} \\{{{-\sqrt{3}}}}&{{{\sqrt{1.5}}}}&{{{\sqrt{1.5}}}}\end{pmatrix}=\begin{pmatrix}{{{\sqrt{3}}}}&{{{0}}}&{{{\sqrt{-3}}}} \\{{{0}}}&{{{\sqrt{6}}}}&{{{\sqrt{1.5}}}} \\{{{0}}}&{{{0}}}&{{{\sqrt{1.5}}}}\end{pmatrix} $$ 

---

<!-- PDF page 799 -->

##### A.2.6.3 Singular Value Decomposition (SVD)

We can express any matrix  $ \mathbf{A} $ in terms of eigenvalues and eigenvectors of  $ \mathbf{A}'*\mathbf{A} $ and  $ \mathbf{A}*\mathbf{A}' $. Let  $ \mathbf{A} $ be an  $ n \times p $ matrix of rank  $ k $. Then, the SVD of  $ \mathbf{A} $ is:

 $$ \mathbf{A}=\mathbf{U}^{*}\mathbf{D}^{*}\mathbf{V}^{\prime} $$ 

where  $ \mathbf{U} $ is  $ n \times k $,  $ \mathbf{D} $ is  $ k \times k $, and  $ \mathbf{V} $ is  $ p \times k $. Matrix  $ \mathbf{D} $ is diagonal, with elements  $ \lambda_1 $,  $ \lambda_2 $, ...,  $ \lambda_k $ being the nonzero eigenvalues of  $ \mathbf{A}^* \mathbf{A} $ or  $ \mathbf{A}^* \mathbf{A}' $. The values  $ \lambda_1 $,  $ \lambda_2 $, ...,  $ \lambda_k $ are called the singular values of matrix  $ \mathbf{A} $. Since the columns of  $ \mathbf{U} $ and  $ \mathbf{V} $ are normalized eigenvectors [see Eq. (A.30) about normalized vectors] of symmetric matrices, they are mutually orthogonal, that is,  $ \mathbf{U}' \mathbf{U} = \mathbf{V}' \mathbf{V} = \mathbf{I} $ (identity matrix).

We must use software tools to carry out the complex operations for SVD. In applying software tools, there are minor variations of Eq. (A.37), depending on the number of rows n and the number of columns p in matrix A. We consider two cases.

(1) If $n < p$, the SVD results is: $\mathbf{U}: n \times n$, $\mathbf{U}'*\mathbf{U} = \mathbf{I} (n \times n)$, $\mathbf{D}: n \times p$, $\mathbf{D} = [\mathbf{D}\mathbf{1}:\mathbf{0}]$, where $\mathbf{D}\mathbf{1}$ is a $n \times n$ diagonal matrix, $\mathbf{0}$ is a $n \times 1$ zero matrix, and $\mathbf{V}: p \times p$. For our example matrix, $\mathbf{X}$, Eq. (A.1):

 $$ \mathbf{X}^{\prime}\left(3\mathrm{x}5\right)=\mathbf{U}*\mathbf{D}*\mathbf{V}=\begin{bmatrix}{{{5}}}&{{{3}}}&{{{2}}}&{{{4}}}&{{{1}}} \\{{{1}}}&{{{2}}}&{{{2}}}&{{{3}}}&{{{4}}} \\{{{8}}}&{{{5}}}&{{{5}}}&{{{7}}}&{{{3}}}\end{bmatrix} $$ 

 $$ \mathbf{U}\left(3\times3\right)=\begin{bmatrix}-0.4634&-0.3425&0.8173\\ -0.3046&0.9276&0.2161\\ -0.8322&-0.1488&-0.5342\end{bmatrix} $$ 

 $$ \mathbf{D}\left(3\times5\right)=\left[\mathbf{D}\mathbf{1}\left(3\times3\right):\mathbf{0}\left(3\times2\right)\right]=\begin{bmatrix}{{{15.7412}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{3.5728}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0.6703}}}&{{{0}}}&{{{0}}}\end{bmatrix} $$ 

 $$ \mathbf{V}\left(5\times5\right)=\begin{bmatrix}-0.5895&-0.5530&0.0433&-0.3069&0.5006\\-0.3913&0.0233&0.3179&-0.4486&-0.5375\\-0.3619&0.1192&-0.9014&0.0194&-0.2046\\-0.5459&0.1038&0.2657&0.7847&-0.0694\\-0.2654&0.8177&0.1179&-0.2972&0.3983\end{bmatrix} $$ 

(2) If $n > p$, the SVD results is: $\mathbf{U}: n \times n$, $\mathbf{U}' * \mathbf{U} = \mathbf{I} (n \times n)$, $\mathbf{D}: n \times p$, $\mathbf{D} = [\mathbf{D}\mathbf{1}:\mathbf{0}]^\mathrm{T}$, where $\mathbf{D}\mathbf{1}$ is a $p \times p$ diagonal matrix, $\mathbf{0}$ is a $1 \times n$ zero matrix, and $\mathbf{V}: p \times p$. See an example below:

 $$ \mathbf{X}\left(5\times3\right)=\mathbf{U}\mathbf{1}^{*}\mathbf{D}\mathbf{1}^{*}\mathbf{V}\mathbf{1}=\begin{bmatrix}{{{5}}}&{{{1}}}&{{{8}}} \\{{{3}}}&{{{2}}}&{{{5}}} \\{{{2}}}&{{{2}}}&{{{5}}} \\{{{4}}}&{{{3}}}&{{{7}}} \\{{{1}}}&{{{4}}}&{{{3}}}\end{bmatrix} $$ 

---

<!-- PDF page 800 -->

 $$ \mathbf{U1}\left(5\times5\right)=\begin{bmatrix}-0.5895&-0.5530&0.0433&-0.3069&0.5006\\-0.3913&0.0233&0.3179&-0.4486&-0.5375\\-0.3619&0.1192&-0.9014&0.0194&-0.2046\\-0.5459&0.1038&0.2657&0.7847&-0.0694\\-0.2654&0.8177&0.1179&-0.2972&0.3983\\\end{bmatrix} $$ 

 $$ \begin{aligned}&\mathbf{D}\mathbf{1}\left(5\times3\right)=\left[\mathbf{D}\mathbf{1}\left(3\times3\right):\mathbf{0}\left(2\times3\right)\right]=\begin{bmatrix}{{{15.7412}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{3.5728}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0.6703}}} \\{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0}}}\end{bmatrix}\\ \end{aligned} $$ 

 $$ \mathbf{V1}\left(3\times3\right)=\begin{bmatrix}-0.4634&-0.3425&0.8173\\ -0.3046&0.9276&0.2161\\ -0.8322&-0.1488&-0.5342\end{bmatrix} $$ 

We note that  $ \mathbf{U} = \mathbf{V}\mathbf{1} $ and  $ \mathbf{V} = \mathbf{U}\mathbf{1} $ in both cases.

##### A.2.6.4 Spectral or Eigenvalue Decomposition

We consider the correlation coefficient matrix  $ \mathbf{R} $, (A.24):

 $$ \mathbf{R}=\begin{pmatrix}1&-0.6934&0.9734\\-0.6934&1&-0.6974\\0.9734&-0.6974&1\end{pmatrix} $$ 

which is a symmetric matrix. We may express  $ \mathbf{R} $ by

 $$ \mathbf{R}=\mathbf{P}*\lambda*\mathbf{P}^{\mathrm{T}} $$ 

where  $ \lambda $ is a diagonal matrix,  $ \mathrm{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{K}\right) $, and K is the number of process variables. For  $ \mathbf{R} $ given by Eq. (A.24), we find:

 $$ \mathbf{P}=\begin{bmatrix}{{{-0.7050}}}&{{{0.3777}}}&{{{0.6003}}} \\{{{0.0059}}}&{{{0.8496}}}&{{{-0.5275}}} \\{{{0.7092}}}&{{{0.3683}}}&{{{0.6012}}}\end{bmatrix}\qquad\lambda=\begin{bmatrix}{{{0.0266}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0.3894}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{2.5840}}}\end{bmatrix} $$ 

### A.3 Implementing Basic Matrix Operations in MATLAB

This section follows Ref. [9]. We begin by coding Eq. (A.1) in MATLAB following the coding prompt “$\gg$”

 $$ \gg\mathbf{X}=[5\;1\;8;3\;2\;5;2\;2\;5;4\;3\;7;1\;4\;3] $$ 

By hitting enter, MATLAB gives the output:

 $$ \mathbf{X}=\begin{bmatrix}{{{5}}}&{{{1}}}&{{{8}}} \\{{{3}}}&{{{2}}}&{{{5}}} \\{{{2}}}&{{{2}}}&{{{5}}} \\{{{4}}}&{{{3}}}&{{{7}}} \\{{{1}}}&{{{4}}}&{{{3}}}\end{bmatrix} $$ 

---

<!-- PDF page 801 -->

MATLAB uses “;” as a row separator. Square brackets are for defining matrices, and parentheses are for using matrices. For the coding,

 $$ \gg size(\textbf{X}) $$ 

MATLAB gives the answer

 $$ \mathrm{a n s}=5\mathrm{~3~} $$ 

which says that  $ \mathbf{X} $ is a  $ (5\times3) $ matrix, with 5 rows and 3 columns. In MATLAB, it is always row first and then column.

MATLAB uses an “apostrophe (′)” to express the transpose of a matrix:

 $$ \gg\mathbf{X}^{\prime} $$ 

MATLAB gives the matrix transpose:

 $$ \mathrm{ans}=\begin{bmatrix}{{{5}}}&{{{3}}}&{{{2}}}&{{{4}}}&{{{1}}} \\{{{1}}}&{{{2}}}&{{{2}}}&{{{3}}}&{{{4}}} \\{{{8}}}&{{{5}}}&{{{5}}}&{{{7}}}&{{{3}}}\end{bmatrix} $$ 

The function sum outputs the sum of all the row elements of a matrix:

 $$ \gg\operatorname{sum}(X) $$ 

To find the sum of all the column elements of a matrix, we apply  $ \text{sum} $ to the transpose of the matrix:

 $ \gg \text{sum}(X') $

ans = 14 10 9 14 8

The command X(1 : 2,:) outputs the first two rows of X:

 $ \gg \mathbf{X}(1:2,:) \quad \text{ans} = \begin{array}{llll} 5 & 1 & 8 \\ 3 & 2 & 5 \end{array} $

Likewise, the command X(:, 1 : 2) gives the first two columns of X:

 $ \Rightarrow \mathbf{X}(:,1:2) $
ans = 5 1
3 2
2 2
4 3
1 4

For convenience, we show matrix X again:

 $$ \mathbf{X}=\begin{bmatrix}{{{5}}}&{{{1}}}&{{{8}}} \\{{{3}}}&{{{2}}}&{{{5}}} \\{{{2}}}&{{{2}}}&{{{5}}} \\{{{4}}}&{{{3}}}&{{{7}}} \\{{{1}}}&{{{4}}}&{{{3}}}\end{bmatrix} $$ 

---

<!-- PDF page 802 -->

We can output a submatrix with elements from the first two rows and columns two to three as follows:

 $ \Rightarrow \mathbf{X}(1:2,2:3) $
ans =  $ \begin{array}{cc} 1 & 8 \\ 2 & 5 \end{array} $

We introduce a diagonal matrix, which is a square matrix with an equal number of rows and columns:

 $$ \begin{aligned}&\gg\mathbf{D}=[1:4];\\&\gg\mathbf{A}=\mathbf{diag}(\mathbf{D})\\ \end{aligned} $$ 

Here, using a colon “:” in 1:4 means a set of values from 1 to 4. The function  $ \text{diag} $ creates a square-diagonal matrix with diagonal elements from 1 to 4.

MATLAB returns the following:

 $$ \begin{aligned}\mathbf{A}&=1&0&0&0\\&0&2&0&0\\&0&0&3&0\\&0&0&0&4\end{aligned} $$ 

The  $ \underline{diag} $ function also retrieves the diagonal elements from a matrix:

 $$ \gg\mathbf{X}=\mathbf{diag}(\mathbf{A}) $$ 

MATLAB gives:

 $ x = 1 $
2
3
4

The eye function creates a special diagonal matrix, which contains all zeros, except for a diagonal of ones running downward from upper left corner:

 $ \gg $ eye (4)

MATLAB returns:

 $$ \begin{aligned}ans&=1&0&0&0\\&0&0&0&0\\&0&0&0&0\\&0&0&0&0\end{aligned} $$ 

The function  $ \mathbf{inv} $ gives the inversion of a square matrix, defined previously by Eq. (A.26).

 $$ \gg\mathbf{A}=[2\ 1-1;-3-1\ 2;-2\ 1\ 2] $$ 

 $$ \mathbf{A}=2\quad1\quad-1 $$ 

---

<!-- PDF page 803 -->

-3 -1 2
-2 1 2
 $ \gg \mathbf{inv}(\mathbf{A}) $
ans = 4 3 -1
-2 -2 1
5 4 -1

We discuss the determinant of a square matrix in Eq. (A.27) and Eq. (A.28). The function  $ \det $ gives the determinant:

 $ \Rightarrow \det(\mathbf{A}) $

 $ \text{ans} = 4 \quad 3 \quad -1 $

 $ -2 \quad -2 \quad 1 $

 $ 5 \quad 4 \quad -1 $

### A.4 Implementing Basic Multivariate Data Analysis in MATLAB

We consider again the  $ 5 \times 3 $ data matrix X given by Eq. (A.41):

 $ \gg \mathbf{X} = [5\ 1\ 8;\ 3\ 2\ 5;\ 2\ 2\ 5;\ 4\ 3\ 7;\ 1\ 4\ 3] $

MATLAB outputs the matrix X:

 $$ \begin{aligned}\mathbf{X}&=5&1&8\\&3&2&5\\&2&2&5\\&4&3&7\\&1&4&3\end{aligned} $$ 

This matrix represents three columns of process variables, with each variable having five samples or (row values). We use the function mean to implement Eq. (A.2) to find the sample mean of  $ 5 \times 3 $ data matrix X, which gives a  $ 1 \times 3 $ sample mean matrix, or a row vector:

 $ \gg mean(X) $
ans = 3.0000 2.4000 5.6000

The function std gives the standard deviation for each process variable, as defined in Eq. (A.8).

 $ \gg\mathrm{std}(\mathrm{X}) $
ans = 1.5811 1.1402 1.9494

---

<!-- PDF page 804 -->

We find the sample variance and covariance matrix S, as defined in Eqs. (A.10) and (A.12), by using the function cov:

 $$ \begin{aligned}&\gg\mathbf{S}=\mathbf{cov}\left(\mathbf{X}\right)\\ &\begin{aligned}\\ &\mathbf{S}=2.5000&-1.2500&3.0000\\&-1.2500&1.3000&-1.5500\\&3.0000&-1.5500&3.8000\\ &\end{aligned}\\ \end{aligned} $$ 

In Section A.1.5, we discussed the mean-centered data matrix or deviation matrix,  $ X_{d} $, given by Eq. (A.14):

 $$ \mathbf{X}_{\mathrm{d}}=\mathbf{X}-\overline{\mathbf{X}} $$ 

We implement this in MATLAB by:

 $$ \begin{aligned}&\gg X_{\mathrm{d}}=X-mean(X)\\&X_{\mathrm{d}}=2.0000\quad-1.4000\quad2.4000\\&\quad0\quad-0.4000\quad-0.6000\\&\quad-1.0000\quad-0.4000\quad-0.6000\\&\quad1.0000\quad0.6000\quad1.4000\\&\quad-2.0000\quad1.6000\quad-2.6000\end{aligned} $$ 

This corresponds to Eq. (A.15).

We continue to find the SSCP matrix according to Eq. (A.20):

 $$ \gg\mathbf{SSCP}=\mathbf{X}_{\mathrm{d}}^{^{\prime}}*\mathbf{X}_{\mathrm{d}} $$ 

 $$ \begin{aligned}SSCP&=10.0000\quad-5.0000\quad12.0000\\&\quad-5.0000\quad5.2000\quad-6.2000\\&\quad12.0000\quad-6.2000\quad15.2000\end{aligned} $$ 

We then find the sample variance and covariance matrix S from SSCP by Eq. (A.21), noting that for each process variable, we have five samples, and the number of samples minus 1 (J-1) is 4:

 $$ \gg\mathbf{S}=(1/4)^{*}\mathbf{S S C P} $$ 

 $$ \begin{aligned}\mathbf{S}=&\quad2.5000\quad-1.2500\quad3.0000\\&-1.2500\quad1.3000\quad-1.5500\\&\quad3.0000\quad-1.5500\quad3.8000\end{aligned} $$ 

This is identical to Eq. (A.21). Actually, ML has a simple function, cov, that finds the sample variance and covariance matrix S from the original data matrix, X, directly:

 $$ \gg\mathsf{S}=\mathsf{cov}(\mathbf{X}) $$ 

 $$ \mathbf{S}=2.5000\quad-1.2500\quad3.0000 $$ 

---

<!-- PDF page 805 -->

 $$ \begin{aligned}&-1.2500\quad&1.3000\quad&-1.5500\\&3.0000\quad&-1.5500\quad&3.8000\end{aligned} $$ 

In Section A.1.7, we show how to convert the original data matrix X into a standardized data matrix, that is, a mean-centered and scaled data matrix  $ X_{s} $. In ML, we can do this conversion easily by a simple function zscore:

 $$ \gg\mathbf{X}\mathbf{s}=\mathbf{z}\mathbf{s}\mathbf{c}\mathbf{o}\mathbf{r}\mathbf{e}(\mathbf{X}) $$ 

 $$ \begin{aligned}\mathbf{X}\mathbf{s}=&\quad1.2649\quad-1.2279\quad1.2312\\&0\quad-0.3508\quad-0.3078\\&-0.6325\quad-0.3508\quad-0.3078\\&0.6325\quad0.5262\quad0.7182\\&-1.2649\quad1.4033\quad-1.3338\end{aligned} $$ 

We can follow Eq. (A.24) to find the sample correlation coefficient matrix,  $ \mathbf{R} $, from the standardized data matrix,  $ \mathbf{X}_s $. Fortunately, we can do this directly in MATLAB with a simple function,  $ \text{corr} $:

 $$ \gg\mathsf{R}=\mathsf{corr}(\mathsf{X}\mathsf{s}) $$ 

 $$ \begin{aligned}R=&\quad1.0000\quad-0.6934\quad0.9733\\&-0.6934\quad1.0000\quad-0.6974\\&\quad0.9733\quad-0.6974\quad1.0000\end{aligned} $$ 

Using functions zscore and corr makes it easier to implement PCA in Section A.6.

### A.5 Eigenvalues, Eigenvectors, and Factorization (Decomposition) of Matrices

We review the concepts of eigenvectors and eigenvalues of a square matrix in Section A.2.3. In MATLAB, we use function  $ \text{eig} $ to find eigenvectors and eigenvalues, for example, of the correlation coefficient matrix  $ \mathbf{R} $:

 $$ \gg[Eigenvectors,Eigenvalues]=eig(\boldsymbol{R}) $$ 

 $$ \begin{aligned}Eigenvectors=&\quad-0.7050\quad0.3777\quad0.6003\\&\quad0.0059\quad0.8495\quad-0.5275\\&\quad0.7092\quad0.3683\quad0.6011\end{aligned} $$ 

 $$ \begin{aligned}Eigenvalues&=0.0267&0&&0\\&&0&&0.3894&0\\&&0&&0&&2.5839\end{aligned} $$ 

The columns of the “eigenvectors” matrix represent eigenvectors  $ \mathbf{x1}, \mathbf{x2} $, and  $ \mathbf{x3} $. They follow the relationship, Eq. (A.30), that is,  $ \mathbf{R}*\mathbf{x1} = \lambda_1*\mathbf{x1} $. For  $ \mathbf{x1} $ and  $ \lambda_1 $, the relationship is:

---

<!-- PDF page 806 -->

 $$ \begin{array}{lllllll} 1.0000&-0.6934&0.9733&-0.7050& & -0.7050\\-0.6934&1.0000&-0.6974&0.0059&=(0.0267)&0.0059\\0.9733&-0.6974&1.0000&0.7092& & 0.7092 \end{array} $$ 

For our  $ (J \times K) $ standardized data matrix  $ \mathbf{X}_s $, with  $ K $ columns of normalized process variables,  $ J $ rows of samples or measurements per variable, and rank of  $ \mathbf{P} $, which is typically the smaller number between  $ K $ and  $ J $. Following Section A.2.6.3, we consider two cases of the SVD of  $ \mathbf{X}_s $.

(1) Full Singular Value Decomposition: This involves the decomposition of a  $ J \times K $ matrix  $ X_s $ by a  $ J \times J $ U1, a  $ J \times K $ D1, and a  $ K \times K $ V1. In other words, U1 and V1 are both square, and D1 is the same size as  $ X_s $:

 $$ \mathbf{X}_{\mathbf{s}}=\mathbf{U}\mathbf{1}*\mathbf{D}\mathbf{1}*\mathbf{V}\mathbf{1}^{\prime} $$ 

In MATLAB, we use the function svd to implement this:

 $$ \begin{aligned}\gg[U1,D1,V1]&=\operatorname{svd}(Xs)\\U1&=-0.6679\quad0.0897\quad0.0792\quad-0.1686\quad0.7150\\&-0.0000\quad0.3296\quad0.6749\quad0.6590\quad0.0393\\&\quad0.1181\quad0.5210\quad-0.6906\quad0.4333\quad0.2236\\&-0.1661\quad-0.7615\quad-0.2040\quad0.5838\quad0.1007\\&\quad0.7158\quad-0.1789\quad0.1405\quad-0.0934\quad0.6536\end{aligned} $$ 

 $$ \begin{aligned}D1&=3.2149&0&&0\\&&0&&1.2481&0\\&&0&&0&&0.3265\\&&0&&0&&0\\&&0&&0&&0\end{aligned} $$ 

 $$ \begin{aligned}\mathbf{V}\mathbf{1}&=-0.6003\quad-0.3777\quad0.7050\\&\quad0.5275\quad-0.8495\quad-0.0059\\&\quad-0.6011\quad-0.3683\quad-0.7092\end{aligned} $$ 

Significantly, matrix V1 is identical to the principal loading matrix P in PCA discussed in Section A.6. The three column vectors within matrix V1 correspond to the three principal component loading vectors,  $ p_1 $,  $ p_2 $, and  $ p_3 $. Additionally, we can obtain the principal component score matrix T using Eq. (A.48):

 $$ \mathbf{T}=\mathbf{X}_{s}*\mathbf{P}=\mathbf{X}_{s}*\mathbf{V}\mathbf{1} $$ 

We do this as follows:

 $$ \begin{aligned}>>\mathbf{P}&=\mathbf{V}\mathbf{1}\\ \mathbf{P}&=-0.6003\quad-0.3777\quad0.7050\\ &\quad0.5275\quad-0.8495\quad-0.0059\\ &\quad-0.6011\quad-0.3683\quad-0.7092\end{aligned} $$ 

---

<!-- PDF page 807 -->

 $$ \gg\mathbf{T}=\mathbf{X}_{s}*\mathbf{P} $$ 

 $$ \begin{aligned}\mathbf{T}&=-2.1472\quad&0.1120\quad&0.0259\\&&-0.0000\quad&0.4114\quad&0.2204\\&&0.3797\quad&0.6503\quad&-0.2255\\&&-0.5338\quad&-0.9504\quad&-0.0666\\&&2.3014\quad&-0.2232\quad&0.0459\end{aligned} $$ 

(2) Economy-sized Singular Value Decomposition: As our  $ (J \times K) $ standardized data matrix  $ X_s $ typically has more number of rows of samples per variable, J, than the number of process variables K (i.e. more rows than columns), the matrix U resulting from SVD could be quite large. In this situation, we can apply an economy-sized SVD to produce a  $ J \times K $ U, a  $ K \times K $ D, and a  $ K \times K $ V according to Eq. (A.39):

 $$ \mathbf{X}_{\mathbf{s}}=\mathbf{U}*\mathbf{D}*\mathbf{V}^{\prime} $$ 

In MATLAB, we still use the function svd to implement this, but with a minor change to the function argument from  $ (X_s) $ to  $ (X_s,0) $:

 $$ \begin{aligned}&\gg[U,D,V]=svd(Xs,0)\\ &\begin{aligned}\\ &U=-0.6679&0.0897&0.0792\\&-0.0000&0.3296&0.6749\\&0.1181&0.5210&-0.6906\\&-0.1661&-0.7615&-0.2040\\&0.7158&-0.1789&0.1405\\ &\end{aligned}\\ \end{aligned} $$ 

 $$ \begin{aligned}\mathbf{D}&=3.2149&0&&0\\&0&&1.2481&0\\&0&&0&&0.3265\end{aligned} $$ 

 $$ \begin{aligned}\mathbf{V}&=-0.6003\quad-0.3777\quad0.7050\\&\quad0.5275\quad-0.8495\quad-0.0059\\&\quad-0.6011\quad-0.3683\quad-0.7092\end{aligned} $$ 

### A.6 Principal Component Analysis (PCA)

This section shows how to implement PCA, discussed in Section 9.1, by MATLAB [9].

ML uses the SVD of a standardized data matrix  $ X_{s} $ as the default scheme to do PCA. We illustrate how to implement PCA in MATLAB by using an example of food

---

<!-- PDF page 808 -->

texture analysis [8] from a food manufacturer making a pastry product. The original process data file, food-texture.csv, is available from the valuable website for datasets associated with [8], https://openmv.net/. This dataset can form a  $ 50 \times 5 $ matrix with 5 columns of process variables (oil, density, crispiness, fracture, and hardness) and 50 rows of samples or measurements per variable. In the dataset, there is an extra column of sample label (column 1) that is irrelevant to our study, and we delete the column when forming the data matrix.

To begin with, we place the data file into the ML working folder and import the dataset into ML as a  $ (50 \times 6) $ matrix X1. We then read the first 8 rows of samples for the 5 columns of variables (from columns 2 to 6), and name the resulting  $ (8 \times 5) $ data matrix as X:

 $$ \gg\mathbf{X1}=readmatrix(^{\prime}food-texture.\ CSV^{\prime}); $$ 

 $$ \begin{aligned}&X=X\mathbf{I}(1:8,2:6)\\&X=1000*\\&\begin{aligned}\\ &0.0165&2.9550&0.0100&0.0230&0.0970\\&0.0177&2.6600&0.0140&0.0090&0.1390\\&0.0162&2.8700&0.0120&0.0170&0.1430\\&0.0167&2.9200&0.0100&0.0310&0.0950\\&0.0163&2.9750&0.0110&0.0260&0.1430\\&0.0191&2.7900&0.0130&0.0160&0.1890\\&0.0184&2.7500&0.0130&0.0170&0.1140\\&0.0175&2.7700&0.0100&0.0260&0.0630\\ &\end{aligned}\\ \end{aligned} $$ 

We choose a smaller set of eight samples per variable for illustration. We first standardize or normalize the dataset  $ \mathbf{X} $ to obtain  $ \mathbf{X}_s $ ( $ 8 \times 5 $):

 $$ \gg Xs=zscore(X) $$ 

 $$ \begin{aligned}Xs&=-0.7550\quad&1.0680\quad&-1.0169\quad&0.3340\quad&-0.6664\\&&0.3775\quad&-1.5852\quad&1.4862\quad&-1.6350\quad&0.4153\\&&-1.0381\quad&0.3035\quad&0.2347\quad&-0.5098\quad&0.5183\\&&-0.5662\quad&0.7532\quad&-1.0169\quad&1.4592\quad&-0.7179\\&&-0.9437\quad&1.2479\quad&-0.3911\quad&0.7560\quad&0.5183\\&&1.6987\quad&-0.4160\quad&0.8605\quad&-0.6505\quad&0.7031\\&&1.0381\quad&-0.7757\quad&0.8605\quad&-0.5098\quad&-0.2286\\&&0.1887\quad&-0.5958\quad&-1.0169\quad&0.7560\quad&-1.5421\end{aligned} $$ 

Applying the command for PCA based on  $ X_{s} $ gives the following:

» [coeff, score, latent, tsquared, explained, mu] = pca(Xs)

We discuss the six results listed inside the brackets of the command below.

---

<!-- PDF page 809 -->

## (1) Principal component loading matrix, coeff or P  $ (5 \times 5) $


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>coeff =</td><td style='text-align: center; word-wrap: break-word;'>0.4092</td><td style='text-align: center; word-wrap: break-word;'>-0.3479</td><td style='text-align: center; word-wrap: break-word;'>0.7220</td><td style='text-align: center; word-wrap: break-word;'>-0.3071</td><td style='text-align: center; word-wrap: break-word;'>0.1455</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-0.4414</td><td style='text-align: center; word-wrap: break-word;'>0.5457</td><td style='text-align: center; word-wrap: break-word;'>0.2043</td><td style='text-align: center; word-wrap: break-word;'>-0.4495</td><td style='text-align: center; word-wrap: break-word;'>0.5134</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.5226</td><td style='text-align: center; word-wrap: break-word;'>0.1505</td><td style='text-align: center; word-wrap: break-word;'>-0.1842</td><td style='text-align: center; word-wrap: break-word;'>0.4011</td><td style='text-align: center; word-wrap: break-word;'>0.7137</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-0.4964</td><td style='text-align: center; word-wrap: break-word;'>-0.1008</td><td style='text-align: center; word-wrap: break-word;'>0.4788</td><td style='text-align: center; word-wrap: break-word;'>0.7085</td><td style='text-align: center; word-wrap: break-word;'>0.1102</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0.3437</td><td style='text-align: center; word-wrap: break-word;'>0.7405</td><td style='text-align: center; word-wrap: break-word;'>0.3147</td><td style='text-align: center; word-wrap: break-word;'>0.2019</td><td style='text-align: center; word-wrap: break-word;'>-0.4400</td></tr></table>

The columns of the loading matrix P represent the principal component loading vectors  $ \mathbf{p}_a $ ( $ a=1,2,\ldots,A $), that is,  $ \mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3, \mathbf{p}_4 $, and  $ \mathbf{p}_5 $ (Section A.2.6.2), and the rows of P correspond to the coefficients multiplying the standardized process variables  $ x_{s1} $,  $ x_{s2} $,  $ x_{s3} $,  $ x_{s4} $, and  $ x_{s5} $. ML assumes as the default that the number of principal components A is identical to the number of process variables K with both being 5 in the current example.

## (2) Principal Component Score Matrix, Score or T  $ (8 \times 5) $


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>score = -1.7067</td><td style='text-align: center; word-wrap: break-word;'>0.1652</td><td style='text-align: center; word-wrap: break-word;'>-0.2272</td><td style='text-align: center; word-wrap: break-word;'>-0.5539</td><td style='text-align: center; word-wrap: break-word;'>0.0427</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.5853</td><td style='text-align: center; word-wrap: break-word;'>-0.3003</td><td style='text-align: center; word-wrap: break-word;'>-0.9582</td><td style='text-align: center; word-wrap: break-word;'>0.1181</td><td style='text-align: center; word-wrap: break-word;'>-0.0610</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-0.0049</td><td style='text-align: center; word-wrap: break-word;'>0.9973</td><td style='text-align: center; word-wrap: break-word;'>0.8636</td><td style='text-align: center; word-wrap: break-word;'>-0.0199</td><td style='text-align: center; word-wrap: break-word;'>-0.1119</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-2.0668</td><td style='text-align: center; word-wrap: break-word;'>-0.2238</td><td style='text-align: center; word-wrap: break-word;'>0.3767</td><td style='text-align: center; word-wrap: break-word;'>0.3164</td><td style='text-align: center; word-wrap: break-word;'>0.0552</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-1.3385</td><td style='text-align: center; word-wrap: break-word;'>1.2580</td><td style='text-align: center; word-wrap: break-word;'>0.1235</td><td style='text-align: center; word-wrap: break-word;'>0.2124</td><td style='text-align: center; word-wrap: break-word;'>0.0794</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2367</td><td style='text-align: center; word-wrap: break-word;'>0.6384</td><td style='text-align: center; word-wrap: break-word;'>1.2926</td><td style='text-align: center; word-wrap: break-word;'>-0.1066</td><td style='text-align: center; word-wrap: break-word;'>-0.1733</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.3914</td><td style='text-align: center; word-wrap: break-word;'>-0.7728</td><td style='text-align: center; word-wrap: break-word;'>0.1684</td><td style='text-align: center; word-wrap: break-word;'>-0.0324</td><td style='text-align: center; word-wrap: break-word;'>0.4113</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-1.0965</td><td style='text-align: center; word-wrap: break-word;'>-1.7620</td><td style='text-align: center; word-wrap: break-word;'>0.0879</td><td style='text-align: center; word-wrap: break-word;'>0.0262</td><td style='text-align: center; word-wrap: break-word;'>-0.2424</td></tr></table>

The columns of the score matrix T represent the principal component score vectors  $ \mathbf{t}_a $ ( $ k = 1, 2, \ldots, A $, the number of principal components;  $ A = K $, the number of process variables), that is,  $ \mathbf{t}_1 $,  $ \mathbf{t}_2 $,  $ \mathbf{t}_3 $,  $ \mathbf{t}_4 $, and  $ \mathbf{t}_5 $ (Section A.2.6.2). The rows of  $ \mathbf{T} $ correspond to the scores  $ t_{ka} $ of the  $ k $th sample or observation ( $ k = 1, 2, \ldots, 8 $) projected onto the  $ a $th principal component vector ( $ a = 1, 2, \ldots, 5 $). We plot the scores of the first two principal components in Figure A.1:

 $$ \gg plot(score(:,1),score(:,2),^{\prime}+^{\prime}) $$ 

 $$ \gg xlabel(^{\prime}1st principal component^{\prime}) $$ 

 $$ \gg\mathrm{y l a b e l}(^{\prime}2\mathrm{n d}\mathrm{p r i n c i p a l}\mathrm{c o m p o n e n t^{\prime}}) $$ 

We use the function biplot to plot the eight rows and first two columns of principal component score matrix,  $ \mathbf{score} $ or T, versus the first two columns of principal component loading matrix,  $ \mathbf{coeff} $ or P (Figure A.2):

 $$ \begin{aligned}&\gg biplot(coeff(:,1:2),^{\prime}scores^{\prime},score(:,1:2),^{\prime}variables,\\&\quad\{\prime PC1^{\prime},^{\prime}PC2^{\prime},^{\prime}PC3^{\prime},^{\prime}PC4^{\prime},^{\prime}PC5^{\prime}\})\\ \end{aligned} $$ 

---

<!-- PDF page 810 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>1st principal component</th><th style='text-align: center;'>2nd principal component</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.2</td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>-1.2</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>1.25</td></tr>
    <tr><td style='text-align: center;'>-0.8</td><td style='text-align: center;'>-1.8</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>-0.7</td></tr>
    <tr><td style='text-align: center;'>2.2</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>-0.3</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure A.1 First principal component score versus second principal component score for the eight samples of each process variable. See the score numbers in the first two columns of Eq. (A.49).</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Data Point</th><th style='text-align: center;'>Component 1</th><th style='text-align: center;'>Component 2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>PC1</td><td style='text-align: center;'>0.48</td><td style='text-align: center;'>-0.28</td></tr>
    <tr><td style='text-align: center;'>PC2</td><td style='text-align: center;'>-0.40</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>PC3</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>PC4</td><td style='text-align: center;'>-0.50</td><td style='text-align: center;'>-0.05</td></tr>
    <tr><td style='text-align: center;'>PC5</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.75</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure A.2 The eight rows and first two columns of principal component score matrix, score or T, versus the first two columns of principal component loading matrix, coeff or P.</div>


We can single out any one of the five principal component loading vectors. For the first principal component PC1, we have:

 $$ \gg T=score; $$ 

 $$  PC1=\mathbf{T}(:,1) $$ 

---

<!-- PDF page 811 -->

 $$ \begin{aligned}PC1&=-1.7067\\&\quad2.5853\\&\quad-0.0049\\&\quad-2.0668\\&\quad-1.3385\\&\quad2.2367\\&\quad1.3914\\&\quad1.0965\end{aligned} $$ 

(3) Principal component variances, column vector latent

 $$ \begin{aligned}latent&3.4002\\&0.9792\\&0.5114\\&0.0685\\&0.0408\end{aligned} $$ 

These principal component variances are the eigenvalues of the correlation coefficient matrix  $ \mathbf{R} $ of the standardized data matrix  $ \mathbf{X}_s $ [3, 8], as discussed in Section A.2.6.4. We can apply MATLAB to demonstrate this observation as follows.

 $$ \begin{aligned}\gg R&=corr(X_{s})\\R&=&\begin{aligned}\\ &1.0000&-0.7069&0.5990&-0.4816&0.3434\\&-0.7069&1.0000&-0.7206&0.7217&-0.1027\\&0.5990&-0.7206&1.0000&-0.9194&0.6830\\&-0.4816&0.7217&-0.9194&1.0000&-0.5684\\&0.3434&-0.1027&0.6830&-0.5684&1.0000\\&\gg[Eigenvectors,Eigenvalues]=eig(Rf)\\ &\end{aligned}\\ \end{aligned} $$ 

 $$ \begin{aligned}Eigenvectors&=-0.4092\quad0.3479\quad-0.7720\quad-0.3071-0.1455\\&\quad0.4414\quad-0.5457\quad-0.2043\quad-0.4495-0.5134\\&\quad-0.5226\quad-0.1505\quad0.1842\quad0.4011-0.7137\\&\quad0.4964\quad0.1008\quad-0.4788\quad0.7085-0.1102\\&\quad-0.3437\quad-0.7405\quad-0.3147\quad0.2019\quad0.4400\end{aligned} $$ 

 $$ \begin{aligned}Eigenvalues&=3.4002&0&&0&&0&&0\\&&0&&0.9792&&0&&0\\&&0&&0&&0.5114&&0&\\&&0&&0&&0&&0.0685&&0\\&&0&&0&&0&&0&&0.0408\end{aligned} $$ 

---

<!-- PDF page 812 -->

Significantly, we find that: (1) the eigenvectors of the correlation coefficient matrix  $ \mathbf{R} $ are identical to the principal component loading matrix  $ \mathbf{coeff} $ or  $ \mathbf{P} $ obtained from  $ \mathbf{pca}(\mathbf{X}_s) $; and (2) the diagonal eigenvalues of  $ \mathbf{R} $ are the same as the element values of principal component variance vector,  $ \text{latent} $, obtained from  $ \mathbf{pca}(\mathbf{X}_s) $.

(4) Hotelling's T-squared statistic column vector, tsquared

 $$ \begin{aligned}tsquared&=5.5099\\&\quad4.1481\\&\quad2.7874\\&\quad3.1211\\&\quad2.9861\\&\quad6.0571\\&\quad5.3994\\&\quad4.9909\end{aligned} $$ 

We define the Hotelling's  $ T^{2} $ value in Section 9.1.5, Eq. (9.21).

(5) Percent of data variability explained by principal components, vector explained

 $$ \begin{aligned}explained&=68.0034\\&\quad19.5835\\&\quad10.2276\\&\quad1.3700\\&\quad0.8156\end{aligned} $$ 

Figure A.3 plots this result in a pareto plot of variances explained by the first three principal components, which represent 97.8145% of the total data variances:

 $$ \begin{aligned}&\gg pareto(explained)\\&\gg xlabel(^{\prime}Principal Component^{\prime})\\&\gg ylabel(^{\prime}Principal Component^{\prime})\\ \end{aligned} $$ 

(6) Estimates of the mean of variables in  $ X_{s} $, mu

 $$ \begin{aligned}mu&=1.0e-15^{*}\\&\quad-0.8431\ 0.0139\ 0\ 0.0278-0.0278\end{aligned} $$ 

### A.7 Implementing Basic Matrix Operations in Python

To learn the basics of implementing matrix operations in Python, we can use most Python editing software tools. We use Jupyter Notebook (https://jupyter.org/) for

---

<!-- PDF page 813 -->

<div style="text-align: center;">Figure A.3 Percent of total data variances explained by the “rst three principal components.</div>


our Python editing. We use a package of methods namedumpy. This package provides several methods useful for matrix operations. To use this package, we start with importing the package by typing and running the following:

import numpy

This line imports the numpy package. We create a matrix by typing and running Eq. (A.1) in Python.

 $$ X=\mathsf{n u m p y.a r r a y}([[5,1,8],[3,2,5],[2,2,5],[4,3,7],[1,4,3]]) $$ 

This line of code creates the following matrix:

 $$ \begin{aligned}X&=5&1&8\\&3&2&5\\&2&2&5\\&4&3&7\\&1&4&3\end{aligned} $$ 

The numpy method, •numpy.array() ☐, creates a matrix. Each row of the matrix is contained within individual square brackets, •[]☐ The rows are separated by commas within the outer square brackets. To determine the shape of any given matrix, we type the following and run it in Python.

X.shape

This line of code has the following value:

 $ (5, 3) $

This output is a data type called ₫uple. This tuple has two entries, the number of rows and the number of columns. The rst entry is the number of rows, and the

---

<!-- PDF page 814 — MISSING, not yet parsed -->


---

<!-- PDF page 815 — MISSING, not yet parsed -->


---

<!-- PDF page 816 — MISSING, not yet parsed -->


---

<!-- PDF page 817 — MISSING, not yet parsed -->


---

<!-- PDF page 818 — MISSING, not yet parsed -->


---

<!-- PDF page 819 — MISSING, not yet parsed -->


---

<!-- PDF page 820 — MISSING, not yet parsed -->


---

<!-- PDF page 821 — MISSING, not yet parsed -->


---

<!-- PDF page 822 — MISSING, not yet parsed -->


---

<!-- PDF page 823 — MISSING, not yet parsed -->


---

<!-- PDF page 824 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>1st principal component</th><th style='text-align: center;'>Score matrix</th><th style='text-align: center;'>Loading matrix</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>-0.2</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>-1.2</td><td style='text-align: center;'>-1.2</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'></td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'></td><td style='text-align: center;'>-0.2</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>-0.6</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure A.5 The eight rows and first two columns of principal component score matrix, score or T, versus the first two columns of principal component loading matrix, coeff or P.</div>


 $ PC_{1} = -1.7067 $

2.5853

-0.0049

-2.0668

-1.3385

2.2367

1.3914

1.0965

#### A.10.3 Principal Component Variances, Column Vector Latent

The column vector latent is found by the following code:

latent = pca.explained_variance

latent = 3.4002

0.9792

0.5114

0.0685

0.0408

---

<!-- PDF page 825 -->

These principal component variances are the eigenvalues of the correlation coefficient matrix  $ \mathbf{R} $ of the standardized data matrix  $ \mathbf{X}_s $ [3, 8], as discussed in Section A.2.6.4. We can apply Python to demonstrate this observation as follows.

 $$ \mathbf{R}=\mathbf{n u m p y.c o r r c o e f}(\mathbf{X}_{s},\mathbf{r o w y a r}=\mathbf{F a l s e}) $$ 

 $$ \begin{aligned}R=&\begin{array}{cccc}1.0000&-0.7069&0.5990&-0.4816\\0.7069&1.0000&-0.7206&0.7217\\0.5990&-0.7206&1.0000&-0.9194\\-0.4816&0.7217&-0.9194&1.0000\\0.3434&-0.1027&0.6830&-0.5684\\\end{array}0.3434\end{aligned} $$ 

Eigenvectors, Eigenvalues = numpy.linalg.eig(R)

 $$ \begin{aligned}Eigenvectors&=-0.4092\quad0.3479\quad-0.7720\quad-0.3071\quad-0.1455\\&\quad0.4414\quad-0.5457\quad-0.2043\quad-0.4495\quad-0.5134\\&\quad-0.5226\quad-0.1505\quad0.1842\quad0.4011\quad-0.7137\\&\quad0.4964\quad0.1008\quad-0.4788\quad0.7085\quad-0.1102\\&\quad-0.3437\quad-0.7405\quad-0.3147\quad0.2019\quad0.4400\end{aligned} $$ 

 $$  Eigenvalue=[3.4002,0.9792,0.5114,0.0685,0.0408] $$ 

#### A.10.4 Hotelling's T-Squared Statistic Column Vector, Tsquared

Deriving the Hotelling's T-squared statistic is slightly more complicated in Python. We show the code for doing so below:

 $$ \begin{aligned}tsquared&=numpy.array([(s^{*}\left(pca.explained_variance_{-}^{**}-1)\right)\\&\quad.dot(s.T)for s in score])\end{aligned} $$ 

We define the Hotelling's  $ T^{2} $ value in Eq. (9.21), Section 9.1.5.

---

<!-- PDF page 826 -->

#### A.10.5 Percent of Data Variability Explained by Principal Components, Vector Explained

Finding the ratio is fairly simple. The code to do so is produced below:

 $$ \begin{aligned}explained&=68.0034\\&\quad19.5835\\&\quad10.2276\\&\quad1.3700\\&\quad0.8156\end{aligned} $$ 

In this particular example, the variances in the data explained by the first three principal components represent 97.8145% of the total data variances.

## References

1 Box, G.E.P., Hunter, W.G., and Hunter, J.S. (1987). Statistics for Experimenters. New York, NY: Wiley.

2 Rancher, A.C. and Christensen, W.F. (2012). Methods of Multivariate Analysis, 3e. New York, NY: Wiley.

3 Johnson, R.A. and Wichern, D.W. (2007). Applied Multivariate Statistical Analysis, 6e. Upper Saddle River, NJ: Pearson.

4 Carey, G. (1998). Important Matrices in Multivariate Analysis. psych.colorado.edu/~carey/Courses/PSYC7291/handouts/important.matrices.pdf.

5 Morari, M. and Zafiriou, E. (1989). Robust Process Control, 212–215. Englewood Cliffs, NJ: Prentice-Hall, and 337.

6 Seborg, D.E., Edgar, T.F., Mellichamp, D.A., and Doyle, F.J. III, (2017). Process Dynamics and Control, 4e, 338–340. New York, NY: Wiley.

7 Aspen Technology Inc. (2003). Training Course on Inferential Property Development and Control with Aspen IQ and DMCplus: Multivariate Statistics.

8 Dunn, K. (2019). Process Improvements Using Data, version: Release 485-524d, https://learnche.org/pid/PID.pdf.

9 Lockhart, S. and Tilleson, E. (2017). An Engineer's Introduction to Programming with MATLAB 2017. Mission, KS: SDC Publications.

10 McAvoy, T.J. (1983). Interaction Analysis: Principles and Applications. Instrument Society of America Monograph No. 6, Research Triangle Park, NC, 181–184.