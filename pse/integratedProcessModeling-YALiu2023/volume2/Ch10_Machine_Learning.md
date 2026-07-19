# 10. Applications of Machine Learning to Optimizing Polyolefin Manufacturing

<!-- PDF page 623 -->

## Applications of Machine Learning to Optimizing Polyolefin Manufacturing

This chapter covers the applications of machine learning (ML) to optimizing chemical and polymer processes, particularly polyolefin manufacturing. Our goal is to prepare an overview of ML for university students and faculty, practicing engineers and scientists who are new to the field, and also for those who are knowledgeable but wish to know the new developments and application literature in chemical and polymer processes.

Section 10.1 presents an introduction, beginning in Section 10.1.1 with the historical developments of artificial intelligence (AI) and ML in chemical process industries (CPIs), and suggests the time for actively adopting AI and ML in CPIs has arrived. Section 10.1.2 continues with three key components of ML applications, namely data, representations, and learning, and explains the concepts of supervised learning, semi-supervised learning, unsupervised learning, and reinforcement learning. Section 10.1.3 suggests resources for the readers to get started with ML, including reference books, list of top free online Python training courses, Python reference libraries, and books with ML principles and coding examples. Appendix B of the book gives an introduction to Python for chemical engineers.

Section 10.2 gives an overview of selected ML methods and their applications to regression and classification problems. Section 10.2.1 covers supervised learning methods for regression applications. We discuss linear regression, polynomial regression, underfitting, overfitting and regularization, Ridge linear regression and Lasso linear regression, bias-variance tradeoff, and performance evaluation metrics for regression problems. Section 10.2.2 discusses supervised learning methods for classification applications. We cover logistic regression (classification), radial basis function network, K-means clustering, P-nearest neighbor algorithm, support vector machine (SVM) classification and regression, decision trees for classification and regression, and performance evaluation metrics for classification problems. Section 10.2.3 covers unsupervised learning for dimensionality reduction, outlier detection, and clustering applications. We have already introduced principal component analysis (PCA) in Chapter 9. In this section, we introduce kernel PCA, K-means clustering, hierarchical clustering, density-based spatial clustering of applications with noise (DBSCAN), and Gaussian mixture model (GMM), together with their similarities and differences.

Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing, First Edition. Y. A. Liu and Niket Sharma.

© 2023 WILEY-VCH GmbH. Published 2023 by WILEY-VCH GmbH.

Companion website: www.wiley-vch.de/ISBN9783527352678

---

<!-- PDF page 624 -->

Section 10.3 presents enhanced learning by ensemble methods, including bagging, boosting, and stacking, and introduces the popular methods of random forest, adaptive boosting (AdaBoost) and eXtreme Gradient Boosting (XGBoost), among others.

Section 10.4 discusses enhanced learning by deep neural networks (DNNs). Section 10.4.1 first reviews the key concepts, parameters, and training of a multilayer perceptron (MLP), focusing on its limitations and required changes when applied to DNNs. We explain the vanishing and exploding gradient problems in the popular gradient descent training algorithm and discuss techniques to improve the performance of DNNs, such as batch normalization (BN), regularization by weight decay and dropout, and fast optimizer. Section 10.4.2 covers deep learning by recurrent neural networks (RNNs) for modeling time-dependent processes, including backpropagation through time, long short-term memory (LSTM) RNNs, gated recurrent units (GRUs), and bidirectional RNNs. Section 10.4.3 introduces convolutional neural networks (CNNs). Section 10.4.4 presents the transformer neural network that finds growing applications in chemistry, drug discovery, and chemical processes. Section 10.5 discusses the general guidelines for choosing appropriate ML algorithms for specific applications.

Section 10.5.3 presents a workshop to predict the HDPE melt index (MI) using random forest and XGBoost ensemble learning models. Section 10.6 covers a workshop to predict the HDPE MI using a DNN. Section 10.7 presents a workshop on time-dependent RNNs to predict the HDPE MI in dynamic operations using LSTM and GRU RNNs. Section 10.8 presents a workshop for polymer property prediction based on molecular structures using both transformer networks and CNNs. Section 10.9 covers a workshop for MI using automated ML. Section 10.10 presents an example demonstrating the limitations of stand-alone data-based ML model, which leads to Chapter 11, focusing on integrating first-principle-based model with a data-based ML model to improve both the interpolative and extrapolative accuracies of the resulting model. This chapter gives detailed references for further studies and software implementation by the readers.

Overall, this chapter represents a comprehensive introduction to the literature on the fundamentals, practice, and hands-on workshops of applying ML techniques to chemical and polymer processes, particularly polyolefin manufacturing. We are not aware of any published references with a similar coverage.

A growing trend is to integrate science-guided fundamental models with data-based ML in a hybrid science-guided machine learning (SGML) approach to modeling chemical processes. We recommend our readers to continue studying Chapter 11 about the hybrid SGML approach and its applications to modeling chemical processes and optimizing polyolefin manufacturing.

### 10.1 Introduction

#### 10.1.1 The Time for AI, Particularly Machine Learning, in Chemical Industries Has Finally Arrived

ML is the most important subfield of AI, focusing on the science and art of programming computers so they can learn from data [1, p. 2]. Turing and Haugeland [2]

---

<!-- PDF page 625 -->

first put forward the concept of AI and explained how computers or machines could learn. In mid-1980s to early 1990s, when chemical engineers began to get involved in AI research and practice, the term “machine learning” did not appear in most textbooks [3, 4] and research monographs [5]. The focuses then were on rule-based expert systems [3] and neural networks [4].

Venkatasubramanian [6] gives an excellent perspective on the evolution of AI in chemical engineering. He divides the historical development up to the present into three phases: phase I – expert system era (~1983 to ~1995); phase II – neural network era (~1990 to ~2008); and phase III – data science and deep learning era (~2005 to present). He attributes the lack of impact of AI during phases I and II to: (1) the problems we were attacking are extremely challenging even today; (2) the lack of powerful computing, storage, communication, and programming environments; (3) the lack of sufficient data for ML model development; and (4) the lack of inexpensive and free resources.

It is truly amazing that new developments in ML over the past two decades have touched every aspect of chemical industry. In fact, it would not be possible for us to adequately review the broad range of reported and potential applications of ML in chemical industries in this short chapter. We trust that a study of representative published reviews, such as Refs. [6–23], arranged in year of publication from 2003 to 2022, should convince the reader that the time for AI, particularly ML, in chemical industries has finally arrived.

In addition to Venkatasubramanian [6], we suggest the reader to study Dobbelaere et al. [17] who present a SWOT (strengths, weaknesses, opportunities, and threats) analysis of ML in chemical engineering; Sharma and Liu [22] on a SGML approach to modeling chemical processes; and Chiang et al. [23] on a holistic view of how the chemical industry is transforming digitally toward AI at scale.

#### 10.1.2 Data, Representation, and Learning

##### 10.1.2.1 Data

The first key component of an ML application is data, which could consist of numeric data, text data, image data, etc. [17]. In this chapter, we focus on numerical data only. Qin [8] discusses the 4Vs of big data in CPIs:

(1) Volume: There are massive process data available from process operation databases due to digital control systems.

(2) Velocity: Most of the process data are time-sensitive, and thus dynamic process monitoring and fault diagnosis using big data analytics become increasingly important.

(3) Variety: Depending on the manufacturing process, there are different varieties of process data available like numeric data and non-numeric data such as texts, images, audio, and video.

(4) Veracity: Precision, trust, correctness, reliability, etc., of the data are important. Establishing trust in big data and conclusions based on them is a continuing challenge in the process industries.

---

<!-- PDF page 626 -->

Our task for ML is to develop good models from datasets. A dataset generally consists of feature vectors, where each feature vector describes an object (e.g. polymer product quality) by using a set of features (e.g. melt index MI, density RHO, weight-average molecular weight MWW, number-average molecular weight MWN, polydispersity index PDI, ...). A feature vector is also called an instance, and a dataset is often called a sample. We designate a dataset containing both input (independent variables, denoted by X) and output (dependent variables, denoted by Y) data as a labeled dataset, and a dataset containing only the input (X) data as an unlabeled dataset.

Two basic practices for preparing the dataset for ML are normalization and standardization. Normalization involves converting an actual range of values, which a numerical feature (independent variable) can take into a standard range of values, typically between -1 and +1, or between 0 and 1. We demonstrate this application in our neural network example in Section 10.4.1. Standardization (also called z-score normalization) converts the given data to a zero mean, and is scaled by their standard deviation. We show the details in Section A.1.7 of Appendix A of this book.

##### 10.1.2.2 Representation

The second component of an ML application is to develop the appropriate representation of the data inputs for ML model building, which depends much on the domain of application [17]. In our view, this component is the most challenging part of developing a ML model.

As we will discuss more in Section 10.4 below, DNNs find growing applications in predicting physical properties, chemical reactions, catalyst synthesis, drug design, etc. [13, 14, 16, 24].

Developing effective molecular representations as inputs to DNNs in such applications continues to attract much attention. For example, based on molecular graph theory, SMILES (Simplified Molecular Input Line Entry System) [25] uses a linear string of characters to represent atoms, bonds, branches, cyclic structures, disconnected structures, and aromaticity with coding rules. RInChI (Reaction International Chemical Identifier) [26] presents a machine-readable character string based on the InChI (IUPAC International Chemical Identifier) algorithm suitable for data storage and indexing. SMILES2Vec [27] is a DNN that automatically learns features (independent variables) from SMILES to predict chemical properties without the need for additional explicit feature engineering. The representations in these prior reports [25–27] consider little chemical information beyond atom type and connectivity and ignore some important characteristics such as polarity and non-covalent interactions.

Overcoming some of these limitations, Maginn and his team [28] demonstrated in 2022 the use of sigma profiles as a universal molecular descriptor for data representation in DNNs. The resulting ML model accurately correlates and predicts a wide range of thermophysical properties of 1432 chemical components contained in our freely available VT-2005 sigma profile database [29]. Note that the sigma profile is the probability distribution of a molecular surface segment having a

---

<!-- PDF page 627 -->

specific charge density. Our database enables the public to apply the sigma profiles to predict thermophysical properties without doing tedious calculations of solvation thermodynamics and computational quantum mechanics. Maginn and coworkers [28] further demonstrate the ability of the resulting DNN model to incorporate thermodynamic conditions (such as temperature) as additional inputs to broaden the applicability of the model.

We refer the reader to articles describing the current data representations of ML model inputs in different applications, for example: catalyst design and discovery [12, 14]; fermentation and biochemical engineering [20, 21, 30]; quality predictions in polymerization processes [31–37]; drug discovery [38, 39]; air pollution forecasting [40]; solubility prediction [41]; chemical product engineering [19]; fault diagnosis [42–45]; process monitoring [46]; classification applications [47–49]; process control [50–54]; soft sensor development [55–57]; quality structure–property relationships (QSPR) [58, 59]; composite manufacturing [24, 60, 61]; and image classification [62].

##### 10.1.2.3 Learning

Learning (training) is the process for generating models from data. A learning algorithm is the computational method used to carry out the learning. A learner is a learned or trained model.

We use available data to train, validate, and test a ML model, such as a regression (prediction) model. To do this, we typically divide the available dataset of independent variables (feature data) and dependent variables (labeled data) into training data, validation data, and test data.

• Training data refer to those data that we use to build the model and find the model parameter values.

- Validation data represent the new data that we use to check the accuracy of the developed model in predicting the dependent variable values (labeled data) that the model has not seen during training. We use the validation data to choose an appropriate learning algorithm and to find the best values of hyperparameters. We refer to properties in the learning algorithm that must be set before training as hyperparameters, such as the learning rate in the backpropagation algorithm in training a neural network (see Eq. (10.51), Section 10.4.1.1). Hyperparameter is different from a parameter that the algorithm is learning during training; for example, those parameters are the weights and biases in a neural network model (see Figure 10.23).

- Test data are those new data that we use to assess the validated model before delivering it to the client or putting it in production.

Heuristically, we use 70% of the dataset for training, 15% for validation, and 15% for testing (in a 70:15:15 ratio). Alternatively, some users choose an 80:10:10 ratio. In the era of big data, datasets could have millions of examples; in such cases, it could be reasonable to use a 95:2.5:2.5 ratio [63, p. 49].

Learning can be supervised, semi-supervised, unsupervised, and reinforced.

---

<!-- PDF page 628 -->

Supervised Learning In the context of process data analytics, the majority of ML applications use supervised learning techniques, which basically means that both independent variables or features (expressed as a feature vector  $ \mathbf{X} $) and dependent variables or labels (expressed as a label vector  $ \mathbf{Y} $) are available in the data. In this book, we limit each label within the label vector  $ \mathbf{Y} $ as a real number or one of a finite set of classes. For process applications, independent variables ( $ X $) are the process input variables and operating conditions like feed flows, temperature, pressure, etc.; dependent variables ( $ Y $) are the process outputs and product quality measurements like concentrations, molecular weights, density, etc. Denote  $ x_i $ and  $ y_i $ as ith scalar components of feature vector  $ \mathbf{X} $ and label vector  $ \mathbf{Y} $. The task of supervised learning is [1, p. 653]: Given a training set of  $ N $ sample input-output pairs,  $ (x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N) $, where each pair was generated by an unknown function  $ y = f(x) $, discover a function  $ h(x) $ that approximates the true function  $ f $.

The resulting function is a learned model, often called a hypothesis. How good is a learned model or hypothesis? It depends on how well it does in predicting the outputs or labels for inputs or features that it has not seen before. We say that a learned model or hypothesis  $ h(x) $ generalizes well if it accurately predicts the outputs of test data.

The bias refers to the tendency of a learned model or hypothesis to deviate from the expected value when averaged over different training data. The variance represents the amount of change in the learned model or hypothesis due to fluctuation in the training data.

Often there is a bias-variance tradeoff, that is, a choice between more complex, low-bias hypotheses that fit training data well with simpler, low-variance hypotheses that may generalize better. We illustrate this aspect more in Figure 10.2 and Section 10.2.1.4, Bias, Variance, and Noise (Irreducible Error): The Bias-Variance Tradeoff.

In supervised learning applications like process monitoring and control and soft sensors, we use regression models to fit an empirical model for any process outputs/product quality as a function of process inputs. For some applications, we might also need to use classification models, for example, to classify some product batches into different categories given the product data labels.

Most supervised learning algorithms dealing with process data analytics can be classified into two major categories of predictive and causal models. Popular ML models are known for predictive modeling. Neural networks (NN) are one of the most popular algorithms that are known to give the highest prediction accuracy. They are made up of interconnected nodes (neurons or processing elements) that process information by its dynamic state to external inputs [4]. These are known to be kind of black box models, which do not require much feature engineering and can predict the output with high accuracy. As we will discuss in Section 10.2, there are other conventional algorithms like Ridge regression [64], SVMs [31–35, 38, 47, 55, 65–67], decision trees [68–73], etc., which can be used for predictive modeling.

Unsupervised Learning Unsupervised learning methods are useful when data of independent variables or features (X) are available as inputs but in a process,

---

<!-- PDF page 629 -->

dependent variables or labels (Y) are not available as outputs. The unsupervised learning algorithm creates a model that takes the input vector X and transforms it into another vector or into a value that can be used to solve a practical problem. For example, in clustering, the model returns the id of the cluster of each feature vector in the dataset. In dimensionality reduction, the output of the model is a feature vector that has fewer features than the input X. In outlier detection, the output is a real number that indicates how a scalar component of the feature vector is different from a typical sample in the dataset [63].

For example, PCA, covered in Sections 9.1 and 9.2, is a well-known unsupervised learning method for dimensionality reduction and outlier detection. In Section 10.2.3, we will give examples of unsupervised learning algorithms.

Semi-Supervised Learning In semi-supervised learning, the dataset contains both labeled examples (with X and Y) and unlabeled examples (with X only). Usually, the quantity of unlabeled examples is much higher than the number of labeled examples. We use a few labeled examples to mine more information from a large collection of unlabeled examples. This happens to be the case in polymer manufacturing, where the output quality measurements (Y) are measured at lower frequency compared to the input process variables (X).

The goal of a semi-supervised learning algorithm is identical to that of the supervised learning algorithm. By using many unlabeled examples, we hope to help the learning algorithm to produce a better model than using labeled examples alone.

Reinforcement Learning This description follows [63, 74]. Reinforcement learning is a subfield of ML where the learning system, called an agent (e.g. an algorithm or a decision-maker), “lives” in a prescribed environment (e.g. process plant) and is capable of observing the “state” (e.g. temperature, pressure, etc.) of that environment as a vector of independent variables or features. The agent can execute sequential actions (e.g. a controller) in every state, and different actions bring different rewards (e.g. product yields) in return (or in the terminology of psychology, reinforcements) and could also move the machine to another state of the environment. Some actions bring penalties as negative rewards. The goal of a reinforcement learning algorithm is to learn a “policy” (e.g. controller action), which is similar to a learned model or hypothesis  $ f(x) $ as in supervised learning. Specifically, a policy takes the feature vector of a state as input and outputs an optimal action to execute in that state. This action is optimal if it maximizes the expected average reward or the cumulative reward. We note that in reinforcement learning, the decision-making is sequential and the goal is long-term.

According to Geron [74], many robots implement reinforcement learning algorithms to learn how to walk. DeepMind's AlphaGo program is an example of reinforcement learning. It made the headlines in May 2017 when it beat the world champion Ke Jie in the game Go. It learned its winning "policy" by analyzing millions of games, and then playing many games against itself. During the game, the learning was turned off; AlphaGo was just playing the "policy" it had learned.

---

<!-- PDF page 630 -->

In this book, we focus on short-term or one-shot decision-making, where input examples are independent of one another and the predictions are made before the decision-making. Thus, we will not focus on reinforcement learning.

Hoskins and Himmelblau [50] published the first article on process control via neural networks and reinforcement learning in 1992. This article inspired a number of subsequent studies of reinforcement learning applied to process control of polymerization reactors [52–54]. Reviews on reinforcement learning for process control are available [51, 75].

#### 10.1.3 Suggested Resources to Get Started with Machine Learning

##### 10.1.3.1 Reference Books on AI and ML

We recommend Russel and Norvig [1] as a modern reference for AI and ML, despite that the book is huge with 1115 pages. The book by Turning and Haugeland [2] is an early reference on AI. Our textbooks [3, 4], as well as the excellent reference by Stephanopoulos and Han [5] cover the development of intelligent systems, including expert systems and neural networks, within phase I – expert system era (~1983 to ~1995) and phase II – neural network era (~1990 to ~2008). Haykin [76] is a comprehensive book on neural networks and learning machines, although the book does not cover the latest development of deep learning since 2009. We recommend Burkov's The Hundred-Page Machine Learning Book [63], which is short, explaining most of the modern ML concepts in easy-to-understand terms.

##### 10.1.3.2 Basic Training of Python

We assume the reader has some Python programming experience. If not, get started with http://learnpython.org. Try the official tutorials on Python.Org (https://docs.python.org/3/tutorial) and study Appendix B of this book, “Introduction to Python for Chemical Engineers.”

There are many suggested lists of top free online Python training courses. See, for example: (1) Top 10 free Python training courses: https://www.bestcolleges.com/bootcamps/guides/learn-python-free (2) Top 10 best online Python classes of 2022: https://www.intelligent.com/best-online-courses/python-classes; (3) Top 10 websites to learn Python programming for free in 2022: https://medium.com/javarevisited/10-free-python-tutorials-and-courses-from-google-microsoft-and-coursera-for-beginners-96b9ad20b4e6; (4) 14 great free online courses for learning Python: https://www.onlinecoursereport.com/free/learning-python.

The reader should become familiar with Python’s main scientific libraries, particularly NumPy (https://numpy.org), pandas (https://pandas.pydata.org), Matplotlib – visualization with Python (https://matplotlib.org).

##### 10.1.3.3 Books with ML Principles and Coding Examples

We highly recommend the 2022 book by Geron [74]. It covers the concepts, tools, and techniques to build ML models using Scikit-learn, Keras, and TensorFlow. Another 2022 book by Marsland [77] introduces ML concepts well, covering a wide range of topics with coding examples. Grus [78] covers the basic ML principles with

---

<!-- PDF page 631 -->

examples of Python implementations. Chollet [79] is a practical book explaining many mathematical concepts well with coding examples, from the author of the excellent Keras library. The book by Raschka and Mirjalili [80] is also a good introduction to ML and leverages Python open-source libraries. Lastly, Refs. [81, 82] describe Scikit-learn and TensorFlow libraries.

### 10.2 An Overview of Relevant Machine Learning Concepts and Models

This section introduces the basic concepts and applications of common ML algorithms. Our goal is to cover the essential concepts to enable our readers to study the literature and to choose potential algorithms for specific applications. We present common ML methods following the categories of supervised and unsupervised learning, together with their applications to problems of regression (prediction), classification, clustering, dimensionality reduction, and outlier detection, as we discussed previously in Section 10.1.2.3 (we do not cover semi-supervised and reinforcement learning).

While neural networks are an important supervised learning method for regression, prediction, and classification applications, we delay our discussion of new developments of neural networks to Section 10.4 (enhanced learning by DNNs).

In this section, we limit our discussion of neural networks to radial-basis-function networks (RBFNs), the most popular neural network for classification and clustering applications. This follows because the key concepts of RBFNs, such as clustering, nearest neighbors, and decision boundaries, are also important to other supervised and unsupervised learning methods for classification and clustering applications, such as support vector machines, K-nearest neighbors, and K-means clustering.

#### 10.2.1 Supervised Learning Methods for Regression Applications

##### 10.2.1.1 Linear Regression

This section follows [1, pp. 679–680]. We represent a linear regression by the following equation:

 $$ \begin{aligned}y_{\mathrm{p}}&=a_{0}+a_{1}x_{1}+a_{2}x_{2}+\cdots a_{n}x_{n}=\begin{bmatrix}a_{0}&a_{1}&a_{2}&\cdots&a_{n}\end{bmatrix}*\begin{bmatrix}x_{0}\\ x_{1}\\ x_{2}\\ \vdots\\ x_{n}\end{bmatrix}=\mathbf{a}^{\mathrm{T}}\cdot\mathbf{x}=f_{a}(\mathbf{x})\end{aligned} $$ 

In the equation,  $ y_p $ is the predicted value of the dependent variable,  $ a_0 $ is the bias term,  $ a_j $ is the jth model parameter,  $ x_0 $ is a pseudo-independent variable and is always equal to 1, and  $ x_j $ is the jth independent variable.  $ \mathbf{a} $ is the model's parameter vector containing the bias term  $ a_0 $ plus the weight factors  $ a_1 $ to  $ a_n $ (the model parameters are also called weight factors).  $ \mathbf{x} $ is the independent variable vector.  $ f_a(\mathbf{x}) $ is the resulting regression model or hypothesis.

---

<!-- PDF page 632 -->

We extend Eq. (10.1) to an $m$-dimensional vector of predicted value of dependent variable $\mathbf{y}_p$; a $m \times (n+1)$-dimensional data matrix $\mathbf{X}$, that is, the matrix of one $(n+1)$-dimensional example per row of the bias term $(x_0)$ plus $n$ independent variables $(x_1, x_2, \ldots, x_n)$; and a $(n+1)$-dimensional model parameter vector $\mathbf{a}$ containing the bias term $a_0$ plus the feature parameters or weight factors $a_1$ to $a_n$. We write:

 $$ \mathbf{y}_{\mathbf{p}}=\begin{bmatrix}y_{\mathrm{p},1}&y_{\mathrm{p},2}&\cdots&y_{\mathrm{p},m}\end{bmatrix}^{\mathrm{T}}=\begin{bmatrix}x_{10}&\cdots&x_{1n}\\\vdots&\ddots&\vdots\\x_{m0}&\cdots&x_{mn}\end{bmatrix}*\begin{bmatrix}a_{0}\\a_{1}\\a_{2}\\\vdots\\a_{n}\end{bmatrix}=\mathbf{X}*\mathbf{a} $$ 

Let the vector of outputs for the training examples be denoted  $ \mathbf{y} = [y_1 \; y_2 \; \cdots \; y_m]^T $. We try to minimize a MSE (mean squared error) cost or loss function to find the model parameter vector  $ \mathbf{a} $, denoted by  $ \mathbf{a}^* $, that minimizes the MSE loss function, denoted by  $ L(\mathbf{a}) $:

 $$  Min L(\mathbf{a})=Min MSE(\mathbf{a})=Min\|\mathbf{y}_{\mathbf{p}}-\mathbf{y}\|^{2}=Min\|\mathbf{X}^{*}\mathbf{a}-\mathbf{y}\|^{2} $$ 

Setting the gradient with respect to a to zero gives:

 $$ \nabla_{\mathbf{a}}L(\mathbf{a})=\nabla_{\mathbf{a}}\mathrm{MSE}(\mathbf{a})=2\mathbf{X}^{\mathrm{T}}(\mathbf{X}^{*}\mathbf{a}-\mathbf{y})=0 $$ 

Rearranging, we find the minimum-loss weight factor vector  $ \mathbf{a}^{*} $ as:

 $$ \mathbf{a}^{*}=(\mathbf{X}^{\mathrm{T}}\mathbf{X})^{-1}\mathbf{X}^{\mathrm{T}}\mathbf{y} $$ 

Equation (10.5) is known as the normal equation. We call  $ \mathbf{X}^{\mathrm{T}}\mathbf{X}^{-1}\mathbf{X}^{\mathrm{T}} $ the pseudoinverse of the data matrix  $ \mathbf{X} $. We note that not every matrix has an inverse, but every matrix has a pseudoinverse, even non-square matrices. It's easy to compute the pseudoinverse using the singular value decomposition (SVD). See Section A.2.5.3 of Appendix A of this book. Reference [74, p. 113] shows how to implement the solution in Python. Additionally, Code B.1 at the end of Appendix B of this book gives the Python implementation of the linear regression model.

For a more complete discussion of multivariate linear regression, please refer to the free online book by Dunn [83, chapter 4] or to any textbook on multivariate statistical analysis such as Johnson and Wichern [84, chapter 7].

##### 10.2.1.2 Performance Evaluation Metrics for Regression Models

For regression applications, we evaluate the ML model's performance based on the following metrics:

(a) Mean squared error (MSE): It measures how close the predictions are to the actual target values (labeled values). Let  $ y_i = \text{original observation} $,  $ y_p = \text{model-predicted value} $, and  $ n = \text{number of observations} $. We write:

 $$ \mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_{i}-y_{\mathrm{p}})^{2} $$ 

---

<!-- PDF page 633 -->

(b) Root mean squared error (RMSE): It creates a single value to summarize the model error. By squaring the difference, this metric ignores the difference between overprediction and underprediction.

 $$  RMSE=\sqrt{MSE} $$ 

(c) % Normalized RMSE: Let  $ y_{m} = $ mean value of observations. We write:

 $$ y_{m}=\frac{1}{n}\sum_{1}^{n}y_{i}\quad nRMSE=\frac{RMSE}{y_{m}}\times100 $$ 

(d) Coefficient of determination ( $ R^{2} $): It is a goodness-of-fit measure for regression models. This statistic indicates the percentage of the variance in the dependent variable that the independent variables explain collectively. R-squared measures the strength of the relationship between the model and the dependent variable on a convenient scale of 0–1.

##### 10.2.1.3 Polynomial Regression, Underfitting, Overfitting, and Regularization

We modify a figure from [74, p. 130] to illustrate the concepts of underfitting, overfitting, and regularization. Figure 10.1 shows that the simple, linear model (straight line) underfits the training data, resulting in large deviations (bias) between the model line and the training data (generated by a quadratic algebraic equation in the form of  $ y = 0.3x^2 - 0.3x + 0.3 + \text{noise} $).

The quadratic-equation model fits the training data best with smaller deviations, and the sixth-order polynomial-equation model (in the form of  $ y = a_6 x^6 + a_5 x^5 + \ldots + a_2 x^2 + a_1 x^1 + a_0 $) is severely overfitting the training data.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-Value</th><th style='text-align: center;'>Data</th><th style='text-align: center;'>Linear</th><th style='text-align: center;'>Quadratic</th><th style='text-align: center;'>Sixth order Poly</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-4.0</td><td style='text-align: center;'>7.2</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>16.5</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>-1.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>10.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.1 A comparison of good fitting with underfitting by a linear-equation (straight line) model, good fitting by a quadratic-equation model, and overfitting by a sixth-order polynomial-equation model.</div>


---

<!-- PDF page 634 -->

(that is, trying to fit the training data perfectly). By overfitting, we mean that the model fits well on the training data, but does not predict accurately new validation and test data, which the model has not seen, that is, it does not generalize well. In other words, we say that a model is overfitting the training data when it pays too much attention to a particular dataset it is trained on, causing it to perform poorly on unseen data [1, p. 655]. To reduce the generalization error with new validation data, we should feed the model with more training data until the validation error reaches the training error [74, p. 133].

Constraining the model to make it simpler and reduce the risk of overfitting is called regularization [1, p. 671; 74, p. 27]. In particular, regularization attempts to limit the complexity of a model, as we want to find the right balance between fitting the data perfectly and keeping the model simple enough to ensure that it generalizes well with new validation and test data.

##### 10.2.1.4 Regularized Linear Regression Models: Ridge Linear Regression and Lasso Linear Regression

Regularization is a good way to reduce overfitting by constraining the model, that is, by lowering the degrees of freedom a model has, which will make it harder to overfit the data. An example of how to regularize a polynomial regression model is to reduce the number of polynomial degrees [74, pp. 134–135].

For linear regression models, regularization typically involves constraining the model parameters or weight factors. Two well-known regularized linear regression models are Ridge regression [74, p. 135; 64] and Lasso (Least Absolute Shrinkage and Selection Operator) regression [74, p. 137; 85, 86].

Ridge Linear Regression Also called Tikhonov regularization, Ridge linear regression adds a regularization term,  $ \alpha \sum_{i=0}^{n} a_i^2 $ to the cost function, Eq. (10.3):

 $$ \begin{aligned}\operatorname{Min}L(\mathbf{a},\alpha)&=\operatorname{Min}\operatorname{MSE}(\mathbf{a},\alpha)=\operatorname{Min}\|\mathbf{y}_{\mathbf{p}}-\mathbf{y}\|^{2}\\&=\operatorname{Min}\left\{\|\mathbf{X}*\mathbf{a}-\mathbf{y}\|^{2}+\alpha\left(\frac{1}{2}\right)\sum_{i=1}^{n}a_{i}^{2}\right\}\end{aligned} $$ 

where  $ \alpha $ is a hyperparameter. We note in Eq. (10.9) that the last term does not include the bias term  $ a_0 $ and the sum starts at  $ i = 1 $, not 0. We may also represent the last term using the notation for Euclidean norm or  $ L_2 $ norm,  $ \|\mathbf{a}\|_2 $. This gives:

 $$  Min L2(\mathbf{a},\alpha)=Min MSE(\mathbf{a},\alpha)=Min\left\{\|\mathbf{X}*\mathbf{a}-\mathbf{y}\|^{2}+\alpha\left(\frac{1}{2}\right)[\|\mathbf{a}\|_{2}]^{2}\right\} $$ 

Reference [63, p. 53] calls this the L2 regularization for Ridge linear regression. There is a closed-form solution to the Ridge linear regression [74, p. 136]:

 $$ \mathbf{a}^{*}=(\mathbf{X}^{\mathrm{T}}\mathbf{X}+\boldsymbol{\alpha}\mathbf{I})^{-1}\mathbf{X}^{\mathrm{T}}\mathbf{y} $$ 

where  $ \mathbf{I} $ is an  $ (n+1)\times(n+1) $ identity matrix with 0 in the top-left cell, corresponding to the bias term. The same reference shows how to implement the solution in Python.

---

<!-- PDF page 635 -->

Lasso Linear Regression Lasso linear regression replaces the Euclidean or L2 norm in the loss function, Eq. (10.10), by a simple vector or L1 norm:

 $$  Min L1(\mathbf{a},\alpha)=Min MSE(\mathbf{a},\alpha)=Min\left\{\|\mathbf{X}*\mathbf{a}-\mathbf{y}\|^{2}+\alpha\sum_{i=1}^{n}|a_{i}|\right\} $$ 

Reference [63, p. 53] calls this the L1 regularization for Lasso linear regression. The hyperparameter for Lasso linear regression is typically between 0 and 1. This regularization method tends to eliminate those model parameters or weight factors  $ a_{i} $ of the least important features or independent variable  $ x_{i} $, that is, to set  $ a_{i} $ to zero [74, p. 137]. This results in a sparse regression model with few nonzero model parameters or weight factors. Reference [74, p. 139] shows how to implement the solution in Python.

Bias, Variance, and Noise (Irreducible Error): The Bias-Variance Tradeoff Applying a ML model to new validation data that the model has not seen previously results in a model's generalization error, which is commonly expressed as the sum of three components, namely, bias, variance, and noise (irreducible error) [74, p. 133]:

(1) Bias: this error typically results from having a wrong model assumption, such as using a linear model while the actual data were generated from a quadratic-equation model. A model that underfits the data leads to a high bias value.

(2) Variance: this error typically results from the model's excessive sensitivity to small variations in the training data. A model with a high degree of freedom, such as a sixth-order polynomial model with a bias term  $ a_{0} $ and six model parameters  $ a_{1} $, to  $ a_{2} $, is likely to lead to a high variance and to overfit the data.

(3) Noise (irreducible error): this error results from the noisiness of the data itself. To lower this error, we must clean up the data by fixing the data sources, such as removing the outliers and fixing the broken sensors.

Increasing a model's complexity (such as going from a linear regression model to a six-order polynomial regression model) typically increases the model's variance and reduces its bias. By contrast, reducing a model's complexity increases its bias and reduces its variance. This corresponds to the well-known bias-variance tradeoff, as illustrated in Figure 10.2.

Effect of Ridge Regularization on Linear and Polynomial Regression Models We adopt an example from [74, p. 136] to illustrate both linear and polynomial regressions using different levels of Ridge regularization, and explain the concept of bias-variance tradeoff in ML models. Figure 10.3 shows the effect of imposing different levels of Ridge regularization on the variance and bias of a linear regression model (a) and a polynomial regression model (b). We see that increasing the level of Ridge regularization through increasing the value of the hyperparameter  $ \alpha $ in Eq. (10.9) for the linear regression model on the left figure from  $ \alpha = 0 $ to 1 to 10 and to 100 results in less extreme, and more reasonable predictions, thus reducing the variance of the model from the data, while increasing its bias [74, p. 136]. Likewise, increasing the

---

<!-- PDF page 636 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Bias</th><th style='text-align: center;'>Variance</th><th style='text-align: center;'>Optimal balance</th><th style='text-align: center;'>Overfitting (high bias)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>test error</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>Bias</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.2 An illustration of the bias-variance tradeoff in ML models.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>Y (Data)</th><th style='text-align: center;'>Y (α = 0)</th><th style='text-align: center;'>Y (α = 1)</th><th style='text-align: center;'>Y (α = 10)</th><th style='text-align: center;'>Y (α = 100)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.7</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>2.9</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>2.7</td><td style='text-align: center;'>2.9</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2.9</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>2.9</td><td style='text-align: center;'>2.9</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>4.7</td><td style='text-align: center;'>3.1</td><td style='text-align: center;'>3.1</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>5.3</td><td style='text-align: center;'>3.4</td><td style='text-align: center;'>3.4</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X</th><th style='text-align: center;'>Y (Data)</th><th style='text-align: center;'>Y (a = 0)</th><th style='text-align: center;'>Y (a = 0.01)</th><th style='text-align: center;'>Y (a = 1)</th><th style='text-align: center;'>Y (a = 10)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>-1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>-1.2</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>3.9</td></tr>
    <tr><td style='text-align: center;'>-0.8</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>4.7</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>5.3</td><td style='text-align: center;'>4.2</td><td style='text-align: center;'>4.2</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>3.8</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 10.3 A linear regression model (a) and a polynomial regression model (b) with Ridge regularization with increasing values of hyperparameter  $ \alpha $: increasing  $ \alpha $ value results in a smaller variance and a larger bias.</div>


level of Ridge regularization for the polynomial regression model on the right figure gives a similar result.

#### 10.2.2 Supervised Learning Methods for Classification Applications

##### 10.2.2.1 Logistic Regression

Why do we include a “regression” model within a section for “classification” model? Logistic regression is commonly used for classification, as it can output a value that corresponds to the probability of belonging to a class (e.g. 10% of being spam).

Using the same notations as in Eqs. (10.1)–(10.3), we write the estimated probability  $ \hat{p} $ as:

 $$ \hat{p}=f_{a}(\mathbf{x})=\sigma(\mathbf{a}^{\mathrm{T}}\cdot\mathbf{x}) $$ 

---

<!-- PDF page 637 -->

where  $ \sigma $ represents the sigmoid activation function:

 $$ \sigma(x_{i})=\frac{1}{1+\mathrm{e}^{-x_{i}}} $$ 

See Table 10.6 and Figure 10.24 below for more about the sigmoid function, which has an output value bounded between 0 and 1. We pause to mention that Eqs. (10.13) and (10.14) are similar to the basic operation of a node or neuron in a neural network, as illustrated previously in Figure 8.101 in Section 8.3.2.1. In Section 10.4.1.1 below, we give details of a neural network operation.

Based on Eq. (10.13), if the estimated probability ( $ \hat{p} $) is greater than 50%, then the model predicts that the instance belongs to the positive class, labeled “1.” Otherwise, the model predicts that the instance belongs to the negative class, labeled “0” [74, p. 142]. Once the model applies Eqs. (10.13) and (10.14) to estimate the probability that an instance x belongs to the positive class, we can write the prediction of the output  $ y_{p} $:

 $$ \begin{aligned}y_{p}&=0,\quad if\hat{p}<0.5\\&=1,\quad if\hat{p}\geq0.5\end{aligned} $$ 

Figure 10.4 illustrates the logistic regression's prediction moving from negative class region  $ (y_{\mathrm{p}}=0) $ to positive class region  $ (y_{\mathrm{p}}=1) $, resulting in a decision boundary and a transition region. Understanding the decision boundary is important for the classification models discussed below.

How do we train a logistic regression model to find the model parameters or weight factors,  $ [a_0 \ a_1 \ a_2 \ \cdots\ a_n] $ or  $ \mathbf{a}^T $ so that the model estimates high probabilities of positive instances  $ (y_p = 1) $ and low probabilities of negative instances  $ (y_p = 0) $? For a single training instance, we define a cost function  $ C(\mathbf{a}) $ as [74, p. 144]:

 $$ \begin{aligned}C(\mathbf{a})&=-\log(\hat{p})\quad if y_{p}=1\\&=-\log(1-\hat{p})\quad if y_{p}=0\end{aligned} $$ 

<div style="text-align: center;">Figure 10.4 An illustration of classification regions, decision boundary, and transition regions.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Feature</th><th style='text-align: center;'>Probability</th><th style='text-align: center;'>Value</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Predicted value</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Negative class</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Negative class</td><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>Negative class</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.6</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>1.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>3.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>4.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>5.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>6.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>7.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>8.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>9.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>10.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>11.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>12.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>13.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>14.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>15.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>16.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>17.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>18.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>19.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>20.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>21.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>22.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>23.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>24.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>25.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>26.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.1</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.2</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.3</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.4</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.6</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.7</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>27.8</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Negative class region</td><td style='text-align: center;'>2</td></tr>
  </tbody>
</table>

---

<!-- PDF page 638 -->

We take the average cost over all training instances as the cost function over the whole training set. This gives [74, p. 144]:

 $$ \mathrm{Min}L(\mathbf{a})=-\frac{1}{m}\sum_{i=1}^{m}[y_{\mathrm{p},i}\log(\hat{p}_{i})+(1-y_{\mathrm{p},i})\log(1-\hat{p}_{i})] $$ 

Contrary to linear regression, there is no closed-form solution to the logistic regression problem defined by Eq. (10.17). We typically use a numerical procedure based on a gradient descent optimization. The gradient or the partial derivative of this cost function with respect to the model parameter or weight factor  $ a_{j} $ is:

 $$ \nabla\mathbf{a}L(\mathbf{a})=\frac{\partial}{\partial a_{j}}L(\mathbf{a})=\frac{1}{m}\sum_{i=1}^{m}(\boldsymbol{\sigma}(\mathbf{a}^{\mathrm{T}}\mathbf{x}_{i})-y_{\mathrm{p},i})x_{j,i} $$ 

This equation computes the prediction error and multiplies it by the jth feature or independent variable value  $ x_{j,i} $, and then it computes the average error over all training instances. Once we have the gradient vector containing all the partial derivatives, we can apply the gradient descent algorithm. Reference [74, p. 145] shows how to implement this solution in Python.

With the advances in neural computing since 1990, neural networks have essentially replaced logistic regression for classification applications. In Section 10.4.1.1, we present a detailed example of multilayer perceptron network applied to classification problems.

##### 10.2.2.2 Radial Basis Function Network (RBFN)

RBFN is among one of the several online lists of top 10 ML algorithms that beginners should know in 2022 [87–89]. It includes some key concepts of clustering, nearest neighbors, and decision boundary that are common to several other algorithms for both regression and classification applications. We update our previous discussion of RBFN [4, pp. 115–120] below.

RBFN Architecture Figure 10.5 illustrates the architecture of a RBFN [4], with N nodes (or neurons) in the input layer, L nodes in the hidden layer, and M nodes in the output layer.

The input layer uses a direct transfer function so that an input vector  $ \mathbf{x} $ with elements  $ x_i $ ( $ i = 1-N $) gives the same vector  $ \mathbf{x} $ as its output vector.

The most important processing step in a RBFN is the hidden layer. There are L nodes  $ (k=1-L) $ that are radially symmetric. Each hidden node has three key components:

(1) A centroid [74, p. 240] or a cluster center vector  $ \mathbf{c}_k $ in the input space, consisting of cluster centers with elements  $ c_{ik} $ ( $ i = 1-N $), which are stored as weight factors between the input and hidden layers (see Figure 10.5). Figure 10.7 below illustrates three cluster centers  $ \mathbf{c}_k $ ( $ k = 1-3 $) in a two-dimensional input space, which we will discuss more.

---

<!-- PDF page 639 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_154_628_546.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 10.5 The architecture of a RBFN. Source: Adapted from Baughman and Liu [4].</div>


(2) A distance measure to determine how far an input vector  $ \mathbf{x} $ with elements  $ x_i $ ( $ i = 1-N $) is from an assumed cluster center vector  $ \mathbf{c}_k $. We quantify this distance  $ I_k $ ( $ k = 1-L $) between the two vectors  $ \mathbf{x} $ and  $ \mathbf{c}_k $ by their Euclidean norm or  $ L_2 $ norm:

 $$ I_{k}=\|\mathbf{x}-\mathbf{c}_{k}\|=\left[\sum_{1}^{N}(x_{i}-c_{ik})^{2}\right]^{1/2} $$ 

(3) A transfer function, which converts the Euclidean norm, Eq. (10.19), to give an output for each node. A popular choice is the Gaussian transfer function, illustrated in Figure 10.6, which transforms  $ I_k $ ( $ k = 1-L $) to an output from the kth node,  $ \nu_k $ ( $ k = 1-L $), assuming a width of  $ \sigma_k $ ( $ k = 1-L $):

 $$ \nu_{k}=\exp\left(-\frac{\mathrm{I}_{k}^{2}}{\sigma_{k}^{2}}\right) $$ 

We see that the hidden layer processes the output from the input layer through a distance calculation, Eq. (10.19), and a transfer function, Eq. (10.20). To develop a RBFN, we assume initial values of the cluster center vector  $ \mathbf{c}_k $ and the Gaussian transfer function width  $ \sigma_k $, and use the training data to update their values, as we discuss below.

We now turn to the output layer of a RBFN. In Figure 10.5, we see the weight factors  $ w_{kj} $ ( $ k = 1-L $;  $ j = 1-M $) between the kth node in the hidden layer and the jth node of the output layer. We find the output  $ y_i $ from the output layer using a standard

---

<!-- PDF page 640 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>x</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-3.0</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-2.5</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>-2.0</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>-1.5</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.85</td></tr>
    <tr><td style='text-align: center;'>0.0</td><td style='text-align: center;'>1.00</td></tr>
    <tr><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.90</td></tr>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.6 The Gaussian transfer function.</div>


transfer function, as shown in Figure 8.101 previously and illustrated in detail in Section 10.4.1.1 below.

K-Means Clustering Algorithm for Finding the Cluster Center Vector,  $ c_k $ The K-means clustering algorithm begins with an initialization step. We assume a set of cluster center (or centroid) vectors  $ \mathbf{c}_k $ ( $ k = 1-L $) for the  $ L $ nodes in the hidden layer, with elements  $ c_{ik} $ ( $ i = 1-N $,  $ k = 1-L $), stored as weight factors between the input and hidden layers. We also assume that there are  $ T $ training examples available to the input layer with  $ N $ nodes, and represent them as  $ T $ training vectors  $ \mathbf{x}(t) $ with elements  $ x_{it} $ ( $ i = 1-N $;  $ t = 1-T $).

The algorithm continues with an iterative step to find a desirable set of L center vectors  $ \mathbf{c}_k $ ( $ k = 1-L $) that minimizes the sum of squares of the distance between T training vector  $ \mathbf{x}(t) $ and their nearest L centers  $ \mathbf{c}_k $ ( $ k = 1-L $).

Figure 10.7 illustrates three cluster centers (or centroids)  $ \mathbf{c}_1 $ to  $ \mathbf{c}_3 $, in a two-dimensional input space for a network having three nodes in the hidden layer ( $ L = 3 $). In the figure, we see that input value  $ x_{1t} $ has a moderate output response,  $ \nu_3 $, but it does not activate nodes 1 and 2 (no  $ \nu_1 $ and  $ \nu_2 $, respectively). Look at the cluster center  $ \mathbf{c}_3 $. The activation of node 3 by the input value  $ x_{1t} $ generates an output response  $ \nu_3 $, which reaches its maximum value at the center point and decreases as the distance between the input value  $ x_{1t} $ and the cluster center,  $ c_{3k} $, increases. We also note that input value  $ x_{2t} $ is not within any of the three cluster groups, and does not activate any output response associated with it.

With this background information, the K-means clustering algorithm involves the following iterative steps:

(1) Read the next training vector  $ \mathbf{x}(t) $ with elements  $ x_{it} $ ( $ i=1-N $) into the input layer as  $ t $ increases from 1 to  $ T $.

(2) Modify only the cluster center  $ \mathbf{c}_k $ ( $ k = 1-L $) closest to the training vector  $ \mathbf{x}(t) $ with elements  $ x_{it} $ ( $ i = 1-N $) in the Euclidian distance:

 $$ \boldsymbol{c}_{k}^{\mathrm{n e w}}=c_{k}^{\mathrm{o l d}}+\alpha\left[\mathbf{x}(t)-c_{k}^{\mathrm{o l d}}\right] $$ 

---

<!-- PDF page 641 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_148_638_508.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 10.7 An illustration of three cluster centers (centroids)  $ \mathbf{c}_1 $ to  $ \mathbf{c}_3 $, in a two-dimensional input space for a RBFN having three nodes in the hidden layer ( $ L = 3 $). Not the width of the Gaussian function  $ \sigma_k $ ( $ k = 1-3 $) and two training examples,  $ x_{1t} $ and  $ x_{2t} $. Source: Adapted from Baughman and Liu [4]/Elsevier, Inc.</div>


In the equation,  $ \alpha $ is a hyperparameter, the learning rate, which decreases as t increases from 1 to T.

(3) Repeat the process for a fixed number of iterations.

P-Nearest Neighbor Algorithm for Finding the Width of the Gaussian Transfer Function,  $ \sigma_k $ We now present the P-nearest neighbor algorithm [1, p. 691; 4, p. 117; 74, p. 21] for finding the values of the width of the Gaussian transfer function,  $ \sigma_k $, in Eq. (10.20) and displayed in Figure 10.7. Consider a given cluster center vector  $ \mathbf{c}_k $ ( $ k = 1-L $) and assume  $ c_{k1} $,  $ c_{k2}, \ldots, c_{kp} $ ( $ 1 \leq k_1, k_2, \ldots, k_p \leq L $) are the P nearest neighboring centers. We find the width of the Gaussian transfer function,  $ \sigma_k $, as the root-mean-squares (RMS) distance of the given cluster center vector  $ \mathbf{c}_k $ to the P nearest neighboring centers:

 $$ \sigma_{k}=\left[\frac{1}{P}\sum_{p=1}^{P}\|\mathbf{c}_{k}-\mathbf{c}_{kp}\|^{2}\right]^{1/2} $$ 

In Appendix B of this book, Code B.2 and Table B.1 at the end give the Python implementation of the P-nearest neighbor algorithm, together with a list of common parameters and their suggested values.

Weight Factors Between the Hidden Layer and the Output Layer,  $ w_{kj} $ In Figure 10.5, we see that the hidden layer has L nodes and the output layer has M nodes, and the weight factors between the two layers are  $ w_{kj} (k = 1-L; j = 1-M) $. In Section 10.4.1.1 below, we illustrate the well-known backpropagation algorithm for training a multilayer neural network and describe its limitation and required changes to train a

---

<!-- PDF page 642 -->

DNN. After completing the K-means clustering procedure, we train a RBFN using the backpropagation algorithm to find the weight factors  $ w_{kj} $ ( $ k=1-L; j=1-M $), and then compute the network output  $ y_j $ ( $ j=1-M $) using a sigmoid transfer function  $ f() $ defined in Table 10.6, displayed in Figure 10.24:

 $$ y_{j}=f\left(\sum_{k=1}^{L}w_{kj}v_{k}-T_{j}\right)=f\left(\sum_{k=0}^{L}w_{kj}v_{k}\right) $$ 

where  $ T_j $ is the internal threshold for node  $ j $ in the output layer. See Section 10.4.1.1, particularly Figures 10.20 and 10.23, about the internal threshold and its alternative representations by a bias node and the corresponding weight factor ( $ v_0 = 1 $,  $ w_{0j} = T_j $).

Insight and Experience for Training a RBFN and for Using the K-Means Clustering Algorithm We summarize some insight and experience for training a RBFN [4, pp. 118–120, 129, 130] and for applying the K-means clustering algorithm [74, pp. 247–249] in this section.

Training a RBFN using K-means clustering and P-nearest neighbor algorithms has two important features. First, we do not use any desired output to train the input connections to the hidden layer. Second, for any training example represented by the  $ t^{th} $ training vector  $ \mathbf{x}(t) $ with elements  $ x_{it} (i = 1-N) $, we iteratively modify only one cluster center  $ \mathbf{c}_{k} (k = 1-L) $ closest to the  $ t^{th} $ training vector in the Euclidean distance. This means that we only change those stored weight factors,  $ c_{ik} (i = 1-N; k = 1-L) $, between the input and hidden layers that are elements of one selected cluster center vector  $ \mathbf{c}_{k} (k = 1-L) $. Therefore, during the network training, we only evaluate a small fraction of input nodes with cluster centers very close to the training input. This localized training speeds up the network training considerably.

Next, we typically determine the weight factors between the input and hidden layers,  $ c_{ik} $ ( $ i = 1-N $;  $ k = 1-L $), using the K-means clustering during the first 2000 iterations. Over the same time period, we do not train the weight factors between the hidden and output layers,  $ w_{kj} $ ( $ k = 1-L $;  $ j = 1-M $), by setting both the learning rate (see Eq. (10.51), Section 10.4.1.1) and momentum coefficient (see Eq. (10.56), Section 10.4.1.2) to zero. We call this the data-clustering phase. This initial training gives the weight factors between the input and hidden layers,  $ c_{ik} $ ( $ i = 1-N $;  $ k = 1-L $), which are fixed while we continue to train the weight factors between the hidden and output layers,  $ w_{kj} $ ( $ k = 1-L $;  $ j = 1-M $).

It is important to scale the input features (i.e. preprocessing the dataset, such as mean-centered and scaled by standard deviation, as discussed in Sections A.1.5–A.1.7 in Appendix A) before we run K-means, or the clusters may be very stretched and K-means will perform poorly. Scaling does not guarantee that all the clusters will be nice and spherical, but it generally improves things [74, p. 249].

Additionally, we need to specify the number of clusters when applying the K-means clustering algorithm, which can be challenging. Therefore, we need to run the algorithm several times with different numbers of clusters in order to avoid suboptimal solutions. K-means algorithm does not perform well when the clusters have varying sizes, densities, and nonspherical shapes [74, p. 247]. Reference

---

<!-- PDF page 643 -->

[74, pp. 239–252] shows how to implement the K-means clustering algorithm in Python. A Google search will also give many Python coding examples for implementing the RBFN.

##### 10.2.2.3 Support Vector Machine (SVM) Classification and Regression

In the early 2000s, SVM was the most popular algorithm for supervised learning applications, especially for those who did not have specialized prior knowledge about a domain. Currently, that position has been taken over by enhanced learning by ensemble methods (Section 10.3) and by DNNs (Section 10.4) [1, p. 692]. SVM has found significant applications in soft sensing modeling [55] and process fault diagnosis [47], in prediction of polymer density and MI in polyolefin manufacturing [31–35], and in novel drug discovery [38]. SVM is among many online lists of top 10 ML algorithms that beginners should know in 2022 [87–89]. Two tutorial articles [65, 66] are available.

Linear SVM Classifier We follow [1, pp. 692–696; 63, pp. 3–7, 30–34; 74, pp. 153–172] to discuss the fundamentals and practice of SVM. We begin with some graphical illustrations that demonstrate the key concepts of the SVM. Following the concept of decision boundary in Figure 10.4, we show in Figure 10.8 the decision boundaries (lines 1–3) of three potential linear classifiers. We note that lines 1 and 3 separate the dataset into two classes, but there is essentially a minimum margin of separation between the two separated classes, making these classifiers impractical. The model that is represented by the decision boundary of line 2 performs poorly that it does not even separate the two classes properly.

In Figure 10.9, we show a better linear classifier, where there is a distinct decision boundary separating the two classes of the dataset with sufficient margins of separation.

Given an input feature (independent variable) vector  $ \mathbf{x} = \left[x_1 \quad x_2 \quad \cdots \quad x_D\right]^T $, where  $ D $ is the number of dimensions of the feature vector, the SVM algorithm puts all feature vectors on a  $ D $-dimensional “line” (actually a hyperplane) that separates

<div style="text-align: center;">Figure 10.8 Decision boundaries (lines 1–3) of three potential linear classifiers.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_446_929_803_1252.jpg" alt="Image" width="37%" /></div>


---

<!-- PDF page 644 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_146_519_468.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Figure 10.9 A SVM model for a two-dimensional feature vector illustrating the decision boundary  $ \mathbf{w}^{\top}\mathbf{x} - b = 0 $, constraints, margin of separation, and support vectors 1–3.</div>


examples with positive labels from examples with negative labels. We define the decision boundary with a real-valued weight factor vector  $ \mathbf{w} = \left[w_1 \ w_2 \ \cdots \ w_D\right]^T $ and a real-valued “intercept  $ b $”:

 $$ \mathbf{w}^{\mathrm{T}*}\mathbf{x}-b=0 $$ 

Assume that for each feature or independent variable  $ x_{i} $, there is a corresponding label or dependent variable  $ y_{i} $, which takes the value of  $ -1 $ or  $ +1 $, depending on the following constraints [63, p. 5]:

 $$ \begin{aligned}&\mathbf{w}^{\mathrm{T}*}\mathbf{x}-b\geq+1\quad if y_{i}=+1\\&\mathbf{w}^{\mathrm{T}*}\mathbf{x}-b<-1\quad if y_{i}=-1\\ \end{aligned} $$ 

Figure 10.9 displays the two constraint “lines” (hyperplanes). We also see the margin of separation, which is the distance between the closest examples of two classes as defined by the decision boundary. A large margin leads to a better generalization, that is, how well the model will classify new examples in the future. Geometrically, the constraint equations  $ \mathbf{w}^T\mathbf{x} - b = 1 $ and  $ \mathbf{w}^T\mathbf{x} - b = -1 $ represent two parallel hyperplanes.

We can think of the linear SVM classifier in Figure 10.9 as fitting the widest possible “street” bounded by two constraint “lines” (hyperplanes) between the classes, which is also called large margin classification [74, p. 153]. The width of the “street” is fully determined or “supported” by the instances or examples (labeled 1, 2, and 3 in Figure 10.9) located on the edge of the street, that is, on the two constraint “lines” (hyperplanes). We call instances 1–3 the support vectors because they “hold up” the separating plane [1, p. 694].

As seen in Figure 10.9, the distance between these hyperplanes is  $ 2/\|\mathbf{w}\| $, which suggests that the smaller the norm  $ \|\mathbf{w}\| $, the larger the distance between these hyperplanes. Therefore, to achieve a large margin classification, we need to minimize the Euclidean norm of  $ \mathbf{w} $, defined by  $ [\sum_{i=1}^{D} w_i^2]^{1/2} $. Minimizing  $ \mathbf{w} $ is equivalent to minimizing  $ \frac{1}{2} \mathbf{w}^T \mathbf{w} $ or  $ \frac{1}{2} \|\mathbf{w}\|^2 $. Note that  $ \frac{1}{2} \|\mathbf{w}\|^2 $ has a nice, simple derivative, which is just  $ \mathbf{w} $. By contrast,  $ \|\mathbf{w}\| $ is not differentiable when  $ \mathbf{w} = 0 $. Using the squared norm

---

<!-- PDF page 645 -->

form also makes it possible to use quadratic programming optimization that we will discuss below [63, p. 31; 74, p. 166].

We can now summarize the problem of developing a linear SVM classifier as follows [63, p. 31]:

 $$  Min\left\{\frac{1}{2}\|\mathbf{w}\|^{2}\right\}such that y_{i}(\mathbf{w}^{\mathrm{T}}*\mathbf{x}-b)-1\geq0,\quad i=1,2,\ldots,D $$ 

In Figure 10.9, we strictly require that all instances must be off the “street” and on the right side of the constraint “lines” (hyperplanes) for the two classes. We call this hard margin classification. This type of classification will not work: (1) when there is no hyperplane that can perfectly separate positive examples from negative ones (that is, the data are not linearly separable); or (2) when the data contain noise (with outlier or examples with wrong labels). We discuss how to extend SVM to handle both cases in the following section that leads to the concept of soft margin classification.

Soft Margin Classification by SVM Referring to Eqs. (10.10) and (10.12), we see that both Ridge and Lasso linear regressions incorporate a penalty term into the minimization objective function (loss function) to constrain the ML model by lowering the degrees of freedom that a model has. We adopt the same approach by imbedding the constraint “lines” (hyperplanes), Eq. (10.25), into our minimization loss function. To do this, we need to become familiar with the hinge loss function, illustrated in Figure 10.10 [74, p. 173].

The hinge loss function is not differentiable at z = 1, but just like for Lasso regression, we can still use the gradient descent algorithm for optimization using a “subderivative” of any value between 0 and 1 at t = 1 [74, p. 173].

We follow [63, p. 31] in the discussion below. First, by imbedding our constraints, Eq. (10.24), into the hinge loss function:  $ \max[0, 1 - y_i(\mathbf{w}^\mathrm{T}*\mathbf{x} - b)] $, we see that the

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>z</th><th style='text-align: center;'>y</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>3</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.10 An illustration of hinge loss function.</div>


---

<!-- PDF page 646 -->

hinge loss function is zero if the constraints of Eq. (10.25) are satisfied. This means that  $ \mathbf{w}^{T}*\mathbf{x} $ lies on the correct side of the decision boundary. For data on the wrong side of the decision boundary, the function's value is proportional to the distance from the decision boundary. Next, we modify the minimization problem of Eq. (10.26) by including a penalty term based on the hinge loss function [63, p. 31]:

 $$ \operatorname{Min}\left\{C\|\mathbf{w}\|^{2}+\frac{1}{D}\sum_{i=1}^{D}\max\left[0,1-y_{i}(\mathbf{w}^{\mathrm{T}}\mathbf{x}-b)\right]\right\}\quad i=1,2,\ldots,D $$ 

In the equation, the hyperparameter C characterizes the tradeoff between increasing the width of the decision boundary and ensuring that each input feature  $ x_{i} $ lies on the correct side of the decision boundary. We typically find the appropriate value of C through multiple trials. Equation (10.27) minimizes the hinge loss and is called the soft margin SVM classification, while Eq. (10.26) defines the hard margin SVM classification.

For sufficiently high values of C, the second term in Eq. (10.27) becomes negligible. Consequently, the SVM algorithm will try to find the highest margin by completely ignoring misclassification. When the value of C becomes small and makes classification errors costlier, the SVM algorithm will make fewer mistakes in classification by sacrificing the size (or distance) of the margin that separates the closest examples of positive and negative classes. A large margin contributes to a better generalization, that is, how well the model will classify new examples in the future. Therefore, hyperparameter C regulates the tradeoff between classifying the training data well (minimizing empirical risk) and classifying future examples well (improving generalization).

There is an alternative way of defining the SVM soft margin classification problem by introducing the slack variable  $ S_i $ for each instance. Specifically,  $ S_i $ measures how much the  $ i $th instance is allowed to violate the margin. We find  $ \mathbf{w} $,  $ b $, and  $ S_i $ ( $ i = 1, 2, \ldots, D $) to minimize [74, p. 166]:

 $$ \begin{aligned}\operatorname{Min}&\left\{\frac{1}{2}\|\mathbf{w}\|^{2}+C\sum_{i=1}^{D}s_{i}\right\}\text{such that}y_{i}\left(\mathbf{w}^{\mathrm{T}}*\mathbf{x}-b\right)\\&\geq1-S_{i}\text{and}S_{i}\geq0\quad i=1,2,\ldots,D\end{aligned} $$ 

Here, we wish to make the slack variables as small as possible to reduce the margin violations and make  $ \frac{1}{2}\|\mathbf{w}\|^2 $ as small as possible to increase the margin using the hyperparameter  $ C $ to quantify this tradeoff.

Dealing with Inherent Nonlinearity and the Kernel Trick We follow [1, pp. 693–696; 63, pp. 31–34; 74, pp. 153–172] to introduce the “kernel trick” for dealing with inherently nonlinear datasets that cannot be separated by a hyperplane in the original space. Basically, if we could transform a two-dimensional, non-separable dataset into a three-dimensional space, we could hope that the dataset will become linearly separable in the higher-dimensional space (see Figure 10.11).

In SVMs, using a function to implicitly transform the original space into a higher dimensional space during the loss function optimization is called the kernel trick. For

---

<!-- PDF page 647 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X₁</th><th style='text-align: center;'>X₂</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>2.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>3.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>3.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>4.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>5.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>6.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>6.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>7.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>7.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>8.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>8.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>9.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>9.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>10.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>10.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>11.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>11.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>12.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>12.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>13.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>13.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>14.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>14.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>15.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>15.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>16.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>16.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>17.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>17.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>18.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>18.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>19.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>19.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>20.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>20.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>21.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>21.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>22.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>22.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>23.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>23.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>24.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>24.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>25.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>25.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>26.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>26.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>27.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>27.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>28.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>28.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>29.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>29.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>30.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>30.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>31.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>31.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>32.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>32.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>33.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>33.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>34.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>34.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>35.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>35.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>36.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>36.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>37.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>37.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>38.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>38.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>39.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>39.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>40.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>40.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>41.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>41.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>42.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>42.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>43.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>43.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>44.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>44.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>45.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>45.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>46.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>46.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>47.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>47.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>48.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>48.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>49.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>49.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>50.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>50.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>51.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>51.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>52.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>52.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>53.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>53.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>54.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>54.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>55.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>55.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>56.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>56.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>57.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>57.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>58.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>58.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>59.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>59.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>60.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>60.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>61.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>61.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>62.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>62.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>63.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>63.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>64.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>64.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>65.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>65.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>66.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>66.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>67.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>67.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>68.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>68.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>69.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>69.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>70.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>70.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>71.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>71.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>72.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>72.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>73.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>73.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>74.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>74.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>75.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>75.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>76.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>76.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>77.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>77.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>78.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>78.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>79.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>79.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>80.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>80.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>81.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>81.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>82.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>82.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>83.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>83.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>84.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>84.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>85.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>85.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>86.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>86.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>87.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>87.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>88.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>88.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>89.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>89.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>90.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>90.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>91.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>91.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>92.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>92.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>93.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>93.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>94.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>94.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>95.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>95.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>96.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>96.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>97.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>97.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>98.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>98.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>99.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>99.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>101.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>101.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>102.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>102.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>103.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>103.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>104.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>104.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>105.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>105.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>106.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>106.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>107.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>107.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>108.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>108.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>109.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>109.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>110.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>110.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>111.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>111.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>112.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>112.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>113.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>113.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>114.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>114.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>115.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>115.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>116.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>116.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>117.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>117.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>118.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>118.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>119.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>119.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>120.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>120.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>121.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>121.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>122.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>122.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>123.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>123.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>124.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>124.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>125.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>125.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>126.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>126.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>127.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>127.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>128.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>128.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>129.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>129.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>130.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>130.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>131.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>131.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>132.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>132.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>133.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>133.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>134.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>134.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>135.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>135.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>136.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>136.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>137.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>137.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>138.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>138.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>139.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>139.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>140.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>140.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>141.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>141.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>142.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>142.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>143.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>143.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>144.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>144.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>145.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>145.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>146.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>146.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>147.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>147.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>148.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>148.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>149.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>149.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>150.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>150.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>151.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>151.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>152.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>152.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>153.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>153.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>154.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>154.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>155.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>155.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>156.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>156.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>157.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>157.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>158.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>158.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>159.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>159.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>160.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>160.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>161.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>161.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>162.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>162.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>163.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>163.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>164.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>164.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>165.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>165.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>166.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>166.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>167.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>167.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>168.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>168.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>169.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>169.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>170.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>170.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>171.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>171.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>172.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>172.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>173.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>173.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>174.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>174.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>175.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>175.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>176.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>176.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>177.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>177.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>178.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>178.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>179.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>179.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>180.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>180.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>181.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>181.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>182.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>182.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>183.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>183.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>184.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>184.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>185.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>185.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>186.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>186.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>187.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>187.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>188.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>188.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>189.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>189.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>191.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>191.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>192.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>192.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>193.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>193.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>194.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>194.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>195.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>195.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>196.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Color</th><th style='text-align: center;'>x1</th><th style='text-align: center;'>x2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>3.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>6.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>9.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>11.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>16.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>18.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>19.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>20.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>21.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>24.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>25.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>26.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>27.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>28.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>29.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>30.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>31.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>32.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>33.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>34.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>35.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>36.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>37.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>38.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>39.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>40.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>41.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>42.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>43.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>44.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>45.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>46.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>47.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>48.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>49.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>50.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>51.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>52.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>53.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>54.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>55.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>56.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>57.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>58.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>59.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>60.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>61.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>62.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>63.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>64.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>65.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>66.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>67.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>68.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>69.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>70.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>71.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>72.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>73.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>74.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>75.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>76.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>77.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>78.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>79.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>80.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>81.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>82.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>83.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>84.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>85.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>86.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>87.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>88.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>89.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>90.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>91.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>92.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>93.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>94.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>95.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>96.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>97.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>98.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>99.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>100.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>101.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>102.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>103.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>104.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>105.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>106.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>107.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>108.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>109.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>110.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>111.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>112.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>113.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>114.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>115.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>116.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>117.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>118.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>119.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>120.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>121.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>122.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>123.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>124.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>125.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>126.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>127.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>128.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>129.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>130.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>131.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>132.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>133.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>134.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>135.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>136.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>137.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>138.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>139.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>140.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>141.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>142.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>143.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>144.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>145.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>146.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>147.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>148.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>149.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>150.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>151.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>152.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>153.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>154.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>155.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>156.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>157.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>158.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>159.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>160.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>161.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>162.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>163.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>164.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>165.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>166.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>167.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>168.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>169.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>170.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>171.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>172.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>173.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>174.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>175.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>176.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>177.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>178.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>179.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>180.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>181.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>182.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>183.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>184.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>185.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>186.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>187.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>188.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>189.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>190.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>191.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>192.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>193.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>194.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>195.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>196.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>197.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>198.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>199.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>200.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>201.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>202.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>203.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>204.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>205.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>206.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>207.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>208.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>209.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>210.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>211.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>212.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>213.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>214.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>215.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>216.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>217.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>218.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>219.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>220.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>221.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>222.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>223.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>224.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>225.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>226.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>227.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>228.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>229.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>230.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>231.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>232.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>233.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>234.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>235.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>236.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>237.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>238.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>239.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>240.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>241.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>242.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>243.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>244.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>245.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>246.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>247.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>248.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>249.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>250.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>251.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>252.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>253.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>254.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>255.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>256.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>257.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>258.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>259.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>260.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>261.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>262.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>263.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>264.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>265.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>266.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>267.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>268.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>269.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>270.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>271.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>272.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>273.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>274.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>275.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>276.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>277.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>278.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>279.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>280.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>281.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>282.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>283.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>284.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>285.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>286.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>287.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>288.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>289.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>290.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>291.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>292.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>293.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>294.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>295.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>296.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>297.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>298.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>299.0</td></tr>
    <tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>30</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.11 An illustration of transforming a linear two-dimensional non-separable case into linear separable case in a three-dimensional space.</div>


the example of two-dimensional training data displayed on the left of Figure 10.11, we could convert a 2-D feature vector x by a second-degree polynomial transformation  $ \varphi(\mathbf{x}) $ to a 3-D space [1, p. 694; 63, p. 31; 74, p. 169]:

 $$ \varphi(\mathbf{x})=\varphi\left(\begin{pmatrix}x_{1}\\ x_{2}\end{pmatrix}\right)=\begin{pmatrix}x_{1}^{2}\\ \sqrt{2}x_{1}x_{2}\\ x_{2}^{2}\end{pmatrix} $$ 

Next, let us apply this transformation to two 2-D vectors of our training instances, a and b:

 $$ \begin{aligned}K(\mathbf{a},\mathbf{b})&=\varphi(\mathbf{a})^{\mathrm{T}}\varphi(\mathbf{b})=\left(a_{1}^{2}\ \sqrt{2}a_{1}a_{2}\ a_{2}^{2}\right)\begin{pmatrix}b_{1}^{2}\\ \sqrt{2}b_{1}b_{2}\\ b_{2}^{2}\end{pmatrix}\\&=a_{1}^{2}b_{1}^{2}+2a_{1}b_{1}a_{2}b_{2}+a_{2}^{2}b_{2}^{2}=(a_{1}b_{1}+a_{2}b_{2})^{2}\\&=\left[\left(a_{1}\ a_{2}\right)^{\mathrm{T}}\left(b_{1}\ b_{2}\right)\right]=(\mathbf{a}^{\mathrm{T}}\mathbf{b})^{2}\\ \end{aligned} $$ 

This result (or “trick”) is very significant. It says that we do not need to transform the training instances  $ \mathbf{a} $ and  $ \mathbf{b} $ at all; just replace the dot products of transformed vectors,  $ \varphi(\mathbf{a})^\text{T} \varphi(\mathbf{b}) $, simply by  $ (\mathbf{a}^\text{T} \mathbf{b})^2 $. The result is strictly the same even if we had gone through the trouble of transforming the training instances, and then fitting a linear SVM algorithm. This trick makes the whole process much more computationally efficient [74, p. 169].

The function  $ K(\mathbf{a}, \mathbf{b}) = (\mathbf{a}^{\mathrm{T}}\mathbf{b})^{2} $ represents a second-degree polynomial kernel. In ML, we refer to a function  $ \varphi $ as a kernel if it is capable of computing the dot product  $ \varphi(\mathbf{a})^{\mathrm{T}}\varphi(\mathbf{b}) $ based only on the original vectors of our training instances,  $ \mathbf{a} $ and  $ \mathbf{b} $, without having to compute (or even know about) the transformation  $ \varphi $. Table 10.1 lists several commonly used kernels for SVMs [74, p. 171]:

According to Mercer's theorem [74, p. 171; 33, 55, 67], if a function  $ K(\mathbf{a}, \mathbf{b}) $ respects a few mathematical conditions, called Mercer's conditions (e.g.  $ K $ must be continuous symmetric in its arguments so that  $ K(\mathbf{a}, \mathbf{b}) = K(\mathbf{b}, \mathbf{a}) $, etc.), then there exists a function  $ \varphi $ that maps vectors of training instances  $ \mathbf{a} $ and  $ \mathbf{b} $ into another space

---

<!-- PDF page 648 -->

<div style="text-align: center;">Table 10.1 Commonly used kernels for SVMs.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Kernel name</td><td style='text-align: center; word-wrap: break-word;'>Kernel form:  $ K(a, b) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Linear</td><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{a}^{\mathrm{T}}\mathbf{b} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Polynomial</td><td style='text-align: center; word-wrap: break-word;'>$ (\gamma\mathbf{a}^{\mathrm{T}}\mathbf{b} + r)^{d} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Gaussian Radial Basis Function (RBF)</td><td style='text-align: center; word-wrap: break-word;'>$ \exp(-\gamma\|\mathbf{a} - \mathbf{b}\|^{2}) $</td></tr></table>

(possibly with much higher dimensions) such that  $ K(\mathbf{a}, \mathbf{b}) = \varphi(\mathbf{a})^\top \varphi(\mathbf{b}) $. We can use  $ K $ as a kernel because we know  $ \varphi $ exists, even if we do not know what  $ \varphi $ is. For the Gaussian RBF kernel, research has shown that  $ \varphi $ maps each training instance to an infinite-dimensional space, so it is truly significant that the kernel trick says that we do not need to actually perform the mapping!

Quadratic Programming and Solution to Primal and Dual Problems of Soft Margin SVM Classification The soft margin SVM classification problem, defined previously in Eq. (10.27), is to find w, b, and slack variable  $ s_{i} $ ( $ i=1,2,\ldots,D $) to minimize

 $$ \begin{aligned}\operatorname{Min}&\left\{\frac{1}{2}\|\mathbf{w}\|^{2}+C\sum_{i=1}^{D}s_{i}\right\}\quad such that y_{i}(\mathbf{w}^{\mathrm{T}}*\mathbf{x}-b)\\&\geq1-s_{i}\text{and}s_{i}\geq0\quad i=1,2,\ldots,D\end{aligned} $$ 

Denoting a slack variable vector  $ \mathbf{s} = [s_1, s_2, \cdots, s_D] $, we can modify this minimization problem by incorporating the two linear constraints into the minimization loss function by introducing the Lagrange multipliers,  $ \boldsymbol{\alpha} = [\alpha_1, \alpha_2, \cdots, \alpha_D] $ and  $ \boldsymbol{\beta} = [\beta_1, \beta_2, \cdots, \beta_D] $ such that:

 $$ \begin{aligned}\operatorname{Min}&L(\mathbf{w},b,\mathbf{s},\boldsymbol{\alpha},\boldsymbol{\beta})\\&=\operatorname{Min}\left\{\frac{1}{2}\|\mathbf{w}\|^{2}+C\sum_{i=1}^{D}s_{i}+\sum_{i=1}^{D}\alpha_{i}[y_{i}(\mathbf{w}^{\mathrm{T}}*\mathbf{x}-b)-1+s_{i}]-\sum_{i=1}^{D}\beta_{i}s_{i}\right\}\end{aligned} $$ 

This is a constrained optimization problem with two linear constraints, known as quadratic programming, for which there are many “off-the-shelf” solvers available. Given this constrained optimization problem, for which the optimization literature calls it a primal problem, it is possible to develop a slightly different and closely related problem, called its dual problem. The solution to the dual problem typically gives a lower bound to the solution of the primal problem. Under some conditions, the dual problem can have the same solution as the primal problem. Luckily, the current SVM minimization problem happens to meet these conditions; we can choose to solve the primal or the dual problem to find the same solution  $ [74, p. 168] $.

For the primal problem defined by Eq. (10.32), interested readers may refer to [74, pp. 761–764; 67] for the details in developing a dual problem. We only write

---

<!-- PDF page 649 -->

the resulting dual problem as follows:

 $$  Min\left\{\frac{1}{2}\sum_{i=1}^{D}\sum_{j=1}^{D}y_{i}y_{j}\alpha_{i}\alpha_{j}\mathbf{x}_{i}^{\mathrm{T}}\mathbf{x}_{j}-\sum_{i=1}^{D}\alpha_{i}\right\} $$ 

subject to

 $$ \sum_{i=1}^{D}y_{i}\alpha_{i}=0and0\leq\alpha_{i}\leq C $$ 

SVM for Regression and for Outlier Detection Referring to Figure 10.9, how do we apply the existing concepts of SVM for classification to regression? The answer is simple. Instead of finding the widest margin of separation, or the largest possible “street” between the two classes without violating the margins, SVM regression (i.e. SVR) tries to fit as many instances as possible on the street, that is, between the constraint lines (hyperplanes), while limiting margin violations (i.e. instances off the street). The basic idea behind SVR is to find the best-fit line. In SVR, the best fit “line” is the hyperplane that has the maximum number of feature points.

Unlike other regression models that try to minimize the error between the real and predicted values, the SVR tries to fit the best “line” (hyperplane) within a threshold value. The threshold value is the distance between the hyperplane and boundary “line” (hyperplane).

Our preceding discussion of SVM has already provided sufficient background to enable the readers to understand many online resources on SVR principles and its implementation.

In Appendix B of this book, Code B.7 and Table B.1 at the end give the Python implementation of the SVM algorithm, together with a list of common parameters and their suggested values.

Lastly, SVM can also be applied to outlier detection; see the online Scikit-learn's documentation for more details.

##### 10.2.2.4 Decision Trees for Classification and Regression Problems

Introduction to Decision Trees A decision tree has a structure similar to a conventional flow chart that uses a branching to illustrate every possible outcome of a decision. Each node with a tree represents a test on a specific variable, and each branch uses the outcome of that test.

Decision trees are versatile ML algorithms for both classification and regression applications. They are also the fundamental components of ensemble methods for enhanced learning, such as random forest that we will discuss in Section 10.4 [74, p. 175–186; 70]. One of the many qualities of decision trees is that they require very little data preparation. In fact, they require no feature centering or scaling at all [74, p. 176].

Figure 10.12 shows a decision tree corresponding to the dataset of Table 10.2. This example first appeared in Quinlan [69] and was repeated in many papers and online tutorials [70–73]. However, none of these references gives sufficient details for developing the decision tree, as we do below.

---

<!-- PDF page 650 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_148_806_607.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.12 A decision tree example.</div>


In the figure, we represent each attribute name in a rectangle, each attribute value in an oval, and each decision (class) in a diamond with No or N for negative and Yes or P for positive. “Outlook” represents the entire dataset, and it is a root node (or a parent node) from which the decision tree starts; it is split into three branches or sub-trees, namely, sunny, overcast, and rain labeled in ovals. Upon calculations of some splitting criteria that we will introduce shortly, the “sunny” outlook is split further into two branches or sub-trees based on humidity being high or normal; likewise, the “rain” outlook is split further into two branches or sub-trees based on wind being strong or weak. Finally, we see that normal humidity leads to a leaf node or final output node, labeled positive or yes within a diamond; and high humidity leads to a leaf node labeled negative or no within a diamond. The same interpretations apply to weak wind being positive or yes and strong wind being negative or no within diamonds on the branches or sub-trees split from the wind rectangle. Finally, we note that we may call the subsequent nodes in different branches split from the root node or parent node the child nodes.

There are three basic algorithms to help with the development of decision trees: (1) CART (Classification and Regression Trees) algorithm by Breiman et al. [68]; (2) ID3 algorithm (Iterative Dichotomiser 3) by Quinlan [69]; and (3) C4.5 algorithm by Quinlan [70]. The CART algorithm produces only binary trees with non-leaf nodes always having two children (that is, questions have only yes/no answers). Other algorithms, such as ID3, can produce decision trees with nodes that have more than two children. In the following, we first define some terminologies that we use as criteria for splitting trees and then demonstrate their applications to the problem specified by Figure 10.12 and Table 10.2 following the ID3 and C4.5 algorithms.

---

<!-- PDF page 651 -->

<div style="text-align: center;">Table 10.2 Training dataset for the decision tree example of Figure 10.12.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Day</td><td colspan="4">Attribute</td><td style='text-align: center; word-wrap: break-word;'>Class</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Outlook</td><td style='text-align: center; word-wrap: break-word;'>Temperature</td><td style='text-align: center; word-wrap: break-word;'>Humidity</td><td style='text-align: center; word-wrap: break-word;'>Wind</td><td style='text-align: center; word-wrap: break-word;'>N (Negative); P (Positive)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Sunny</td><td style='text-align: center; word-wrap: break-word;'>Hot</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>N</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Sunny</td><td style='text-align: center; word-wrap: break-word;'>Hot</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>N</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>Overcast</td><td style='text-align: center; word-wrap: break-word;'>Hot</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Rain</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>Rain</td><td style='text-align: center; word-wrap: break-word;'>Cool</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>Rain</td><td style='text-align: center; word-wrap: break-word;'>Cool</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>N</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>Overcast</td><td style='text-align: center; word-wrap: break-word;'>Cool</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>Sunny</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>N</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>Sunny</td><td style='text-align: center; word-wrap: break-word;'>Cool</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>Rain</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>Sunny</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>Overcast</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>Overcast</td><td style='text-align: center; word-wrap: break-word;'>Hot</td><td style='text-align: center; word-wrap: break-word;'>Normal</td><td style='text-align: center; word-wrap: break-word;'>Weak</td><td style='text-align: center; word-wrap: break-word;'>P</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>Rain</td><td style='text-align: center; word-wrap: break-word;'>Mild</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Strong</td><td style='text-align: center; word-wrap: break-word;'>N</td></tr></table>

Terminologies for Tree Splitting Criteria All decision tree algorithms require splitting criteria for splitting a node to form a tree. In many cases, an internal node is split based on the value of a single attribute, and the algorithm searches for the best attribute upon which to split. The main goal of splitting is to reduce the impurity of a node. The node impurity is a measure of the homogeneity of the labels at the node. The current implementation provides two impurity measures for classification (entropy and Gini index) and one impurity measure for regression (variance).

1. Entropy: This term derives from Shannon's entropy (https://en.wikipedia.org/wiki/Entropy_(information_theory)). Any correct decision tree for dataset S will classify objects in the same proportion as their presentation in S. An arbitrary object will be determined to belong to class P (positive or yes) with probability  $ p(p + n) $ and to class N (negative or no) with probability  $ n(p + n) $. A decision tree is a source of a massage "P" or "N," with the expected information needed to generate this message as [69]:

 $$ Entropy I(p,n)=-\left(\frac{p}{p+n}\right)\log_{2}\left(\frac{p}{p+n}\right)-\left(\frac{n}{p+n}\right)\log_{2}\left(\frac{n}{p+n}\right) $$ 

To generalize this expression to the case with multiple instances in a given node t, we write [72, 73]:

 $$  Entropy I(p,n)=-\sum_{i=1}^{n}p\left(\frac{i}{t}\right)\log_{2}p\left(\frac{i}{t}\right) $$ 

---

<!-- PDF page 652 -->

where  $ p\left(\frac{i}{t}\right) $ denotes the fraction of class i instances to the total training instances in a given node t.

2. Gini Index [74, p. 177; 72]: The Gini index is a function that determines how well a decision tree was split. Basically, it helps us determine which splitter is best so that we can build a pure decision tree. Gini index has a maximum value of 0.5, which is the worst we can get, and a minimum value of 0 means the best we can get.

 $$ G_{i}=1-\sum_{i=1}^{n}\left[p\left(\frac{i}{t}\right)\right]^{2} $$ 

3. Information Gain [69, 72, 73]: Information gain,  $ G(S, A) = \text{Entropy}(\text{parent nodes}) - \text{Entropy}(\text{child nodes}) $

 $$ \begin{aligned}Information\ gain,\ G(S,A)&=Entropy(parent\ nodes)-Entropy(child\ nodes)\\&=Entropy(S)-\sum[p(S\mid A)*Entropy(S\mid A)]\\&\quad(10\ 37)\end{aligned} $$ 

For a subset  $ A $ splitting into child nodes  $ \{C_1, C_2, \ldots, C_v\} $, let us assume that  $ C_i $ contains  $ p_i $ objects of class  $ P $ (positive or yes) and  $ n_i $ of class  $ N $ (negative or no), the expected information required for the subtree for  $ C_i $ is  $ I(p_i, n_i) $. We find the expected information required for the tree with  $ A $ as root as the weighted average [69]:

 $$ Entropy(child nodes)=E(A)=\sum_{i=1}^{v}\frac{p_{i}+n_{i}}{p+n}I(p_{i},n_{i}) $$ 

Substituting Eqs. (10.35) and (10.38) into Eq. (10.37) gives

 $$  Information gain\left(A\right)=I(p,n)-E(A) $$ 

The ID3 algorithm examines all candidate attributes and chooses A to maximize information gain (A), forms the tree as above, and then uses the same process recursively to form trees for the residual subsets  $ C_1 $,  $ C_2 $, ...,  $ C_v $ [69].

4. Gain Ratio [72]: The C4.5 algorithm uses the gain ratio as the splitting criterion, which is defined as:

 $$ \mathrm{Gain ratio}=[\mathrm{Information gain}\left(A\right)]/[\mathrm{Entropy}I(p,n)] $$ 

Application of ID3 and C4.5 Algorithms to the Training Dataset We apply the ID3 and C4.5 algorithms as follows:

1. Calculate the entropy of the dataset.

2. For each attribute/feature, calculate the entropy for all its categorical values by Eq. (10.35). Calculate the information gain for the feature by Eq. (10.39). Calculate the gain ratio for the feature by Eq. (10.40).

3. Find the feature with the maximum information gain for ID3 algorithm, and with the maximum gain ratio for the C4.5 algorithm.

4. Repeat it until we get the desired tree.

---

<!-- PDF page 653 -->

(Step 1) For the 14-day data of Table 10.2, we have 9 P (positive or yes) class and 5 N (negative or no) class.

With p = 9, n = 5, and  $ p + n = 14 $, Eq. (10.34) gives the complete entropy of the dataset as:

 $$ \begin{aligned}ntropy\left(S\right)&=Entropy I(p,\ n)\\&=-\left(\frac{p}{p+n}\right)\log_{2}\left(\frac{p}{p+n}\right)-\left(\frac{n}{p+n}\right)\log_{2}\left(\frac{n}{p+n}\right)\\&=-\left(\frac{9}{14}\right)*\log_{2}\left(\frac{9}{14}\right)-\left(\frac{5}{14}\right)*\log_{2}\left(\frac{5}{14}\right)=0.94\\ \end{aligned} $$ 

In Steps 2–4, we evaluate the four attributes for the dataset, including Outlook, Temperature, Humidity, and Wind.

(Step 2) First attribute – Outlook with categorical values of sunny  $ (p_{1}=2, n_{1}=3) $, overcast  $ (p_{2}=4, n_{2}=0) $, and rain  $ (p_{3}=3, n_{3}=2) $

 $$  Entropy(Outlook=sunny)=-\left(\frac{2}{5}\right)*\log_{2}\left(\frac{2}{5}\right)-\left(\frac{3}{5}\right)*\log_{2}\left(\frac{3}{5}\right)=0.971 $$ 

 $$  Entropy(Outlook=overcast)=-\left(\frac{4}{4}\right)*\log_{2}\left(\frac{4}{4}\right)-\left(\frac{0}{4}\right)*\log_{2}\left(\frac{0}{4}\right)=0 $$ 

 $$  Entropy(Outlook=rain)=-\left(\frac{3}{5}\right)*\log_{2}\left(\frac{3}{5}\right)-\left(\frac{2}{5}\right)*\log_{2}\left(\frac{2}{5}\right)=0.971 $$ 

 $$ \begin{aligned}E(outlook),&weighted-average entropy for Outlook according to Eq.(10.34)\\&=p(sunny)*entropy(outlook=sunny)+p(overcast)\\&*entropy(outlook=overcast)+p(rain)*entropy(outlook=rain)\\&=\left(\frac{5}{14}\right)*0.971+\left(\frac{4}{14}\right)*0+\left(\frac{5}{14}\right)*0.971=0.693\\ \end{aligned} $$ 

 $$ \begin{aligned}&Information gain according to Eq.(10.39)=Entropy(S)-E(Outlook)\\ &\quad=0.94-0.693=0.247\\ \end{aligned} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.247}{0.94}=0.262 $$ 

(Step 3) Second attribute – Temperature with categorical values of hot  $ (p_{1}=2, $  $ n_{1}=2) $, mild  $ (p_{2}=3, $  $ n_{2}=1) $ and cool  $ (p_{3}=4, $  $ n_{3}=2) $

 $$  Entropy(Temperature=hot)=-\left(\frac{2}{4}\right)*\log_{2}\left(\frac{2}{4}\right)-\left(\frac{2}{4}\right)*\log_{2}\left(\frac{2}{4}\right)=1 $$ 

 $$  Entropy(Temperature=mild)=-\left(\frac{3}{4}\right)*\log_{2}\left(\frac{3}{4}\right)-\left(\frac{1}{4}\right)*\log_{2}\left(\frac{1}{4}\right)=0.811 $$ 

 $$  Entropy(Temperature=cool)=-\left(\frac{4}{6}\right)*\log_{2}\left(\frac{4}{6}\right)-\left(\frac{2}{6}\right)*\log_{2}\left(\frac{2}{6}\right)=0.9179 $$ 

 $ E(\text{Temperature}) $, weighted-average entropy for

 $$ \begin{aligned}&Temperature according to Eq.(10.34)\\ &=p(hot)*entropy(temperature=hot)+p(mild)\\ &\quad*entropy(temperature=mild)+p(cool)*entropy(temperature=cool)\\ &=\left(\frac{4}{14}\right)*1+\left(\frac{4}{14}\right)*0.811+\left(\frac{6}{14}\right)*0.9179=0.9108\\ \end{aligned} $$ 

---

<!-- PDF page 654 -->

Information gain according to Eq. (10.39)

 $$ =Entropy(S)-E(Temperature)=0.94-0.9108=0.0292 $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.0292}{0.94}=0.032 $$ 

 $$ \begin{aligned}&(Step~4)Third attribute-Humidity with categorical values of high(p_{1}=3,n_{1}=4)\\&and normal(p_{2}=6,n_{2}=1)\end{aligned} $$ 

 $$  Entropy(humidity=high)=-\left(\frac{3}{7}\right)*\log_{2}\left(\frac{3}{7}\right)-\left(\frac{4}{7}\right)*\log_{2}\left(\frac{4}{7}\right)=0.983 $$ 

 $$  Entropy(humidity=normal)=-\left(\frac{6}{7}\right)*\log_{2}\left(\frac{6}{7}\right)-\left(\frac{1}{7}\right)*\log_{2}\left(\frac{1}{7}\right)=0.591 $$ 

 $$ \begin{aligned}E(Humidity),&weighted-average entropy for Humidity according to Eq.(10.34)\\&=p(high)*entropy(humidity=high)+p(normal)\\&*entropy(humidity=normal)\\&=\left(\frac{7}{14}\right)*0.983+\left(\frac{7}{14}\right)*0.591=\mathbf{0}.787\\ \end{aligned} $$ 

 $$ \begin{aligned}&Information gain according to Eq.(10.39)\\ &\quad=Entropy(S)-E(Temperature)=0.94-0.787=0.153\\ \end{aligned} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.153}{0.787}=0.1944 $$ 

 $$ \begin{aligned}&(Step5)Fourth attribute-Wind with categorical values of strong(p_{1}=3,n_{1}=3)\\&and weak(p_{2}=6,n_{2}=2)\end{aligned} $$ 

 $$  Entropy(Wind=strong)=-\left(\frac{3}{6}\right)*\log_{2}\left(\frac{3}{6}\right)-\left(\frac{3}{6}\right)*\log_{2}\left(\frac{3}{6}\right)=1 $$ 

 $$  Entropy(Wind=weak)=-\left(\frac{6}{8}\right)*\log_{2}\left(\frac{6}{8}\right)-\left(\frac{2}{8}\right)*\log_{2}\left(\frac{2}{8}\right)=0.811 $$ 

Weighted-average entropy for Wind according to Eq. (10.34)

 $$ \begin{aligned}&=p(strong)*entropy(wind=strong)+p(weak)*entropy(wind=weak)\\&=\left(\frac{6}{14}\right)*1+\left(\frac{8}{14}\right)*0.811=\mathbf{0.892}\end{aligned} $$ 

Information gain according to Eq. (10.39)

 $$ =Entropy(S)-E(Wind)=0.94-0.892=\mathbf{0.048} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.048}{0.892}=0.0538 $$ 

Up to now, the attribute with the maximum information gain of 0.247 (for ID3 algorithm) and the maximum gain ratio of 0.262 (for C4.5 algorithm) is Outlook (step 2). Figure 10.13 shows the decision tree built so far.

Next, we find the best attribute for splitting the data: (1) with Outlook = Sunny values (days 1, 2, 8, 9, and 11); (2) with Outlook = Overcast values (days 3, 7, 12, and 13); and (3) with Outlook = Rain values (days 4, 5, 6, 10, and 14). We note that the four instances of Outlook = Overcast (days 3, 7, 12, and 13) all lead to positive class P or Yes, and there is no need for further analysis. We can direct these Outlook-Overcast instances to a leaf node or final output node of Yes. We can apply the same procedure as in Steps 2–5 to analyze the Outlook-Sunny and Outlook-Rain instances to develop the decision tree further.

---

<!-- PDF page 655 -->

<div style="text-align: center;">Figure 10.13 Initial decision tree resulting from steps 1 to 5 of ID3 and C4.5 algorithms.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_375_146_799_331.jpg" alt="Image" width="43%" /></div>


From step 2, we see: Entropy (Outlook-Sunny) = 0.971.

In Steps 6–8, we analyze the three attributes (temperature, humidity, and wind) within Sunny.

(Step 6) First attribute – Temperature with categorical values of hot  $ (p_{1}=0, n_{1}=2) $, mild  $ (p_{2}=1, n_{2}=1) $, and cool  $ (p_{3}=1, n_{3}=0) $

 $$  Entropy(Sunny-Temperature=hot)=-\left(\frac{0}{2}\right)*\log_{2}\left(\frac{0}{2}\right)-\left(\frac{2}{2}\right)*\log_{2}\left(\frac{2}{2}\right)=0 $$ 

 $$  Entropy(Sunny-Temperature=mild)=-\left(\frac{1}{2}\right)*\log_{2}\left(\frac{1}{2}\right)-\left(\frac{1}{2}\right)*\log_{2}\left(\frac{1}{2}\right)=1 $$ 

 $$  Entropy(Sunny-Temperature=cool)=-\left(\frac{1}{1}\right)*\log_{2}\left(\frac{1}{1}\right)-\left(\frac{0}{1}\right)*\log_{2}\left(\frac{0}{1}\right)=0 $$ 

E(Temperature), weighted-average entropy for

Temperature according to Eq. (10.34)

 $$ =p(Sunny-Temperature=hot)*entropy(Sunny-Temperature=hot) $$ 

 $$ +p(Sunny-Temperature=mild)*entropy(Sunny-Temperature=mild) $$ 

 $$ +p(Sunny-Temperature=cool)*entropy(Sunny-Temperature=cool) $$ 

 $$ =\left(\frac{2}{5}\right)*0+\left(\frac{2}{5}\right)*1+\left(\frac{1}{5}\right)*0=\mathbf{0}.4 $$ 

 $$ Information gain according to Eq.(10.39)=Entropy(Outlook-Sunny) $$ 

 $$ -E(\mathrm{S u n n y-T e m p e r a t u r e})=0.971-0.4=\mathbf{0.571} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.571}{0.971}=0.588 $$ 

(Step 7) Second attribute – Humidity with categorical values of high  $ (p_{1}=3, n_{1}=0) $ and normal  $ (p_{2}=2, n_{2}=0) $

 $$  Entropy(Sunny-Humidity=high)==-\left(\frac{3}{3}\right)*\log_{2}\left(\frac{3}{3}\right)-\left(\frac{0}{3}\right)*\log_{2}\left(\frac{0}{3}\right)=0 $$ 

 $$  Entropy(Sunny-Humidity=normal)==-\left(\frac{2}{2}\right)*\log_{2}\left(\frac{2}{2}\right)-\left(\frac{0}{2}\right)*\log_{2}\left(\frac{2}{2}\right)=0 $$ 

E(Temperature), weighted-average entropy for

Temperature according to Eq. (10.34)

 $$ \begin{aligned}&=p(Sunny-Humidity=high)*entropy(Sunny-Humidity=high)\\&\quad+p(Sunny-Humidity=normal)*entropy(Sunny-Humidity=normal)\\&=\left(\frac{3}{5}\right)*0+\left(\frac{2}{5}\right)*0=\mathbf{0}.\mathbf{0}\end{aligned} $$ 

---

<!-- PDF page 656 -->

Information gain according to Eq. (10.39) = Entropy(Outlook – Sunny)

 $$ -E(Sunny-Humidity)=0.971-0.0=\mathbf{0.971} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.971}{0.971}=1.0 $$ 

(Step 8) Third attribute - Wind with categorical values of strong  $ (p_{1}=1, n_{1}=1) $ and weak  $ (p_{2}=2, n_{2}=1) $

 $$  Entropy(Sunny-Wind=strong)==-\left(\frac{1}{2}\right)*\log_{2}\left(\frac{1}{2}\right)-\left(\frac{1}{2}\right)*\log_{2}\left(\frac{1}{2}\right)=1 $$ 

 $$  Entropy(Sunny-Wind=weak)==-\left(\frac{2}{3}\right)*\log_{2}\left(\frac{2}{3}\right)-\left(\frac{1}{3}\right)*\log_{2}\left(\frac{1}{3}\right)=0.918 $$ 

 $ E(\text{Wind}) $, weighted – average entropy for Temperature according to Eq. (10.34)

 $$ \begin{aligned}&=p(Sunny-Wind=strong)*entropy(Sunny-Wind=strong)\\&\quad+p(Sunny-Wind=weak)*entropy(Sunny-Wind=weak)\\&=\left(\frac{2}{5}\right)*1+\left(\frac{3}{5}\right)*0.918=\mathbf{0.9508}\end{aligned} $$ 

Information gain according to Eq. (10.39) = Entropy(Outlook – Sunny)

 $$ -E(\mathrm{S u n n y-W i n d})=0.971-0.9508=\mathbf{0.0202} $$ 

 $$  Gain ratio according to Eq.(10.40)=\frac{0.0202}{0.971}=0.0208 $$ 

From steps 6–9, the attribute with the maximum information gain of 0.971 (for ID3 algorithm) and the maximum gain ratio of 1.0 (for C4.5 algorithm) is Humidity (step 7). Figure 10.14 shows the decision tree built so far.

The reader should be able to analyze the two attributes (temperature and wind) within Rain and obtain the final decision tree, as shown previously in Figure 10.12.

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_825_784_1195.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 10.14 Decision tree resulting from steps 6 to 9 of ID3 and C4.5 algorithms.</div>


---

<!-- PDF page 657 -->

Other Aspects of Decision Trees First, we note that the ID3 algorithm handles categorical feature values (e.g. high and normal) only, while C4.5 algorithm can deal with both categorical and numerical feature values. Refer to [73] for an example of how to apply the C4.5 algorithm to handle numerical values of humidity in the decision tree of Figure 10.12.

Decision tree pruning combats overfitting. Pruning works by deleting nodes that are not clearly relevant. For example, a node whose children are all leaf nodes or final output nodes may be unnecessary [74, p. 181]. We can apply a statistically significant test to check if those nodes have only leaf nodes as descendants. See Ref. [1, p. 663] for more information.

For additional details of the CART algorithm, refer to [68], and [74, pp. 178–179]. Scikit-learn uses the CART algorithm, which produces only binary trees, meaning that non-leaf nodes always have two children (that is, questions only have yes/no answers). Other algorithms, such as ID3, can produce decision trees with nodes having two more children [74, p. 177].

Decision trees are also capable of performing regression tasks. See Ref. [74, pp. 182–185] for additional details and the Python implementation. In Appendix B of this book, Code B.3 and Table B.1 at the end give the Python implementation of the decision tree algorithm, together with a list of common parameters and their suggested values.

Lastly, we refer the reader to Section 10.3, Enhanced Learning by Ensemble Methods, which are tree-based algorithms (See also Table 10.10, Section 10.5.2).

##### 10.2.2.5 Performance Evaluation Metrics for Classification Models

We follow [63, pp. 54–58; 30] to present the common evaluation metrics.

Confusion Matrix We adopt an example from [63, p. 55]. Table 10.3 gives a  $ 2 \times 2 $ confusion matrix that summarizes the performance of a classification model in predicting examples belonging to Spam and Not_Spam categories. Of the 20 examples that are actually spam, the model correctly classifies 18 as true positives, TP = 18. The model incorrectly classifies two examples as Not_Spam, that is, we have two false negatives, FN = 2. Likewise, 356 examples are Not_Spam or true negatives, TN = 356; nine examples are incorrectly classified, that is, false positives, FP = 9.

A confusion matrix has the same number of rows and columns as that of classes. It helps us identify the mistake patterns in some applications.

<div style="text-align: center;">Table 10.3 A confusion matrix for classification of spam and not_spam categories predicted by a classification model.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Spam (predicted)</td><td style='text-align: center; word-wrap: break-word;'>Not\_Spam (predicted)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Spam (actual)</td><td style='text-align: center; word-wrap: break-word;'>18 (true positives, TP)</td><td style='text-align: center; word-wrap: break-word;'>2 (false negatives, FN)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Not\_Spam (actual)</td><td style='text-align: center; word-wrap: break-word;'>9 (false positives, FP)</td><td style='text-align: center; word-wrap: break-word;'>356 (true negatives, TN)</td></tr></table>

---

<!-- PDF page 658 -->

Precision and Recall Precision is the ratio of true positive (TP) predictions to the total number of true positive (TP) and false positive (FP) predictions:

 $$  Precision=TP/(TP+FP) $$ 

Recall is the ratio of true positive (TP) to the total number of true positive (TP) and false negative (FN) predictions:

 $$ \mathrm{Recall}=\mathrm{TP}/(\mathrm{TP}+\mathrm{FN}) $$ 

F1 Score F1 score combines precision and recall using the harmonic mean defined by:

 $$ \mathrm{F1}=2\times1/[(1/precision)+(1/recall)] $$ 

Interested readers may refer to our paper [30] about applications of these metrics to an industrial classification problem.

#### 10.2.3 Unsupervised Learning for Dimensionality Reduction and Clustering Applications

##### 10.2.3.1 An Overview

We begin by quoting the thoughtful statement by Geron [74, p. 235]: “Although most of the applications of ML today are based on supervised learning (and as a result, this is where most of the investments go to), the vast majority of the available data is unlabeled: we have input features X but do not have labels y. The computer scientist Yann LeCun famously said that ‘if intelligence was a cake, unsupervised learning would be the cake, supervised learning would be the icing on the cake, and reinforcement would be the cherry on the cake’. In other words, there is a huge potential in unsupervised learning that we have barely started to sink our teeth into.”

In Chapter 9, we studied two of the most common unsupervised learning tasks: dimensionality reduction and outlier (anomaly) detection by PCA. For classification applications, we introduced the concepts of K-means clustering, and P-nearest neighbors in Section 10.2.2.2. We also discussed kernel trick for dealing with inherent nonlinearity.

In this section, we first integrate the kernel trick with PCA and present the kernel PCA to enable the complex nonlinear projections for dimensionality reduction and outlier detection.

We then introduce several unsupervised learning methods for identifying clusters and outliers. Table 10.4 summarizes these methods, as adopted from [91].

##### 10.2.3.2 Kernel Principal Component Analysis (KPCA)

We follow [74, pp. 226–229]. First, in Section 10.2.2.3, we introduce the “kernel trick” for dealing with inherently nonlinear datasets that cannot be separated by a hyperplane in the original space. In Section 10.2.2.3, we explain the “kernel trick,” using kernel functions of Table 10.1 to implicitly map instances into a higher dimensional space, called feature space, and enable nonlinear classification and regression using

---

<!-- PDF page 659 -->

<div style="text-align: center;">Table 10.4 A summary of several unsupervised learning methods for identifying clusters and detecting outliers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Method</td><td style='text-align: center; word-wrap: break-word;'>Basis</td><td style='text-align: center; word-wrap: break-word;'>Model input</td><td style='text-align: center; word-wrap: break-word;'>Need the number of clusters</td><td style='text-align: center; word-wrap: break-word;'>Cluster shaped identified</td><td style='text-align: center; word-wrap: break-word;'>Applicable to outlier detection</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>K-means clustering</td><td style='text-align: center; word-wrap: break-word;'>Distance between data and centroids</td><td style='text-align: center; word-wrap: break-word;'>Actual observations</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Spherical shape; with equal diagonal covariance</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hierarchical clustering</td><td style='text-align: center; word-wrap: break-word;'>Distance between data</td><td style='text-align: center; word-wrap: break-word;'>Pairwise distances between observations</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Arbitrary shapes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density-based spatial clustering of applications with noise (DBSCAN)</td><td style='text-align: center; word-wrap: break-word;'>Density of region in the data</td><td style='text-align: center; word-wrap: break-word;'>Actual observations; or pairwise distances between observations</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Arbitrary shapes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Gaussian mixture model</td><td style='text-align: center; word-wrap: break-word;'>Mixture of Gaussian distributions of data</td><td style='text-align: center; word-wrap: break-word;'>Actual observations</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Spherical clusters with different covariance structures</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr></table>

SVMs. Figure 10.11 shows an example of transforming a linear two-dimensional non-separable case into a linear separable case in a three-dimensional space.

We can also apply the kernel trick to PCA by applying a kernel function, making it possible to preserve clusters of instances after nonlinear projections. This is called the kernel PCA or kPCA, and is an effective tool for dimensionality reduction and outlier detection.

Table 10.1 lists the typical kernel functions. For the popular kernel function, Gaussian radial basis function (RBF), that is,  $ \exp(-\gamma||\mathbf{a}-\mathbf{b}||^2) $, corresponding to vectors of two instances,  $ \mathbf{a} $ and  $ \mathbf{b} $, we see an important superparameter,  $ \gamma $. As kPCA is an unsupervised learning algorithm, there is no specific performance measure to help us choose the best kernel function and superparameter value. Typically, we use repeated trials through a grid search to find the kernel and superparameters. Reference [74, pp. 277–281] gives examples of the Python implementation of this kernel and superparameter optimization.

For classification applications, we could reduce the dimensionality to two using kPCA with grid search for finding the best kernel and superparameter, followed by applying logistic “regression” (actually a classification algorithm) of Section 10.2.2.1.

##### 10.2.3.3 K-Means Clustering

In Section 10.2.2.3, we discussed K-means clustering in the context of supervised learning by RBFN. Most of the concepts presented previously are applicable to

---

<!-- PDF page 660 -->

unsupervised learning by K-means clustering. For unsupervised learning, when we neither have labels for dependent variables nor the cluster centers (or centroids) for features or independent variables, how do we proceed? We follow [63, pp. 110–114; 74, pp. 240–248] to discuss the highlights.

First, we mention that it is necessary to scale the input features before we run K-means clustering. Otherwise, the clusters could be very stretched and K-means will perform poorly.

Basically, we start by placing the cluster centers or centroids randomly, that is, by picking k instances at random and using their locations as centroids. We then label the instances, update the centroids, and repeat the tasks of labeling the instances and updating the centroids, and so on until the centroids stop moving. Significantly, computational experience shows that the algorithm is guaranteed to converge in a finite number of iterations (usually quite small) and it will not oscillate forever [74, p. 240].

The efficiency of this clustering scheme depends on the initiation of the centroid locations and the number of clusters. Heuristically, we could run the algorithm 10 times with different random initialization of the centroid locations, and keep the best solution [74, p. 242].

Finding the appropriate number of clusters  $ k $ is the most important question for applying the  $ K $-means clustering method. Geron [74, pp. 246–248] introduces an effective tool, called silhouette score, which can be readily implemented in Python libraries. The silhouette score is the average silhouette coefficient over all instances. An instance's silhouette coefficient is equal to  $ (b - a)/\text{Max}(a, b) $, where  $ a $ is the average distance between an instance and all other instances in the same cluster, that is, the average intra-cluster distance; and  $ b $ is the average distance between an instance and all other instances in the next-closest cluster, that is, the average distance to the instances of the next-closest cluster as the one that minimizes  $ b $, excluding the instance's own cluster. The silhouette coefficient varies between  $ -1 $ and  $ +1 $. A coefficient close to  $ +1 $ means that the instance is well inside its own cluster and far from other clusters. A coefficient close to  $ 0 $ means that it is close to a closer boundary. Lastly, a coefficient close to  $ -1 $ means that the instance may have been assigned to the wrong cluster. As an illustration, Figure 10.15 illustrates the silhouette scores for different numbers of clusters adopted from an example in [74, p. 246]. The figure shows that the number of clusters,  $ k = 4 $, is a very good choice;  $ k = 5 $ is quite good as well and is much better than  $ k = 6 $ or 7. Fortunately, existing Python libraries have codes to enable us to find the silhouette score when we vary the value of  $ k $.

Lastly, we note that K-means clustering does not behave very well when the clusters have varying sizes, different densities, or nonspherical shapes. For those with elliptical clusters, GMM that we introduce below would work better [74, p. 248].

##### 10.2.3.4 Hierarchical Clustering

Johnson [92] first proposed the concept of hierarchical clustering. The basic idea is to group data over a variety of scales and create a hierarchical series of nested clusters or a cluster tree, also called dendrogram. The cluster tree is not a single set of clusters, but a multilevel hierarchy, where clusters at one level combine to form clusters at

---

<!-- PDF page 661 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Number of clusters, k</th><th style='text-align: center;'>Silhouette score</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.70</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.60</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.55</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.15 Silhouette score versus the number of clusters k.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_131_512_520_891.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_562_572_741_852.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 10.16 Representing nested clusters (a) by a dendrogram (b).</div>


the next level. This multilevel hierarchy allows us to choose the level, or scale, of clustering that is most appropriate for our application [92]. Figure 10.16 gives an example of a group of nested clusters (a) and the corresponding dendrogram.

Figure 10.17 illustrates two types of hierarchical clustering. The top diagram in Figure 10.17 illustrates the order in which a group of nested clusters is broken up. This represents a top-down view of hierarchical clustering, called divisive hierarchical clustering (DHC). Specifically, we consider all of the data points as a single cluster; and in every iteration, we separate the data points from the clusters, which are not comparable. This eventually leads to a number of clusters. The top diagram of Figure 10.17 demonstrates the concept of DHC further. The DHC works best when we have fewer but larger clusters, and it is computationally expensive and rarely used.

---

<!-- PDF page 662 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Step</th><th style='text-align: center;'>Step 6</th><th style='text-align: center;'>Step 5</th><th style='text-align: center;'>Step 4</th><th style='text-align: center;'>Step 3</th><th style='text-align: center;'>Step 2</th><th style='text-align: center;'>Step 1</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>a</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>b</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>c</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>d</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>e</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>f</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">(a)</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Step</th><th style='text-align: center;'>Step 1</th><th style='text-align: center;'>Step 2</th><th style='text-align: center;'>Step 3</th><th style='text-align: center;'>Step 4</th><th style='text-align: center;'>Step 5</th><th style='text-align: center;'>Step 6</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>a</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>b</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>c</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>d</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>e</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>f</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">Figure 10.17 Divisive (a) and agglomerative (b) hierarchical clustering.</div>


By contrast, the bottom diagram of Figure 10.17 illustrates the concept of a bottom-up view of hierarchical clustering, called agglomerative hierarchical clustering (AHC). In this case, we consider initially every data point as an individual entity or cluster. At every iteration, we merge these clusters with different clusters until we end up with a single large cluster. The AHC is useful when we have many smaller clusters. It is computationally simpler, more often used, and more available.

We also caution that hierarchical clustering could lead to a dendrogram that would be wrong. Unless we know the data inside out which is impossible for big datasets, we cannot really avoid this error. This follows because how we decide to create clusters could lead to significantly different dendrograms, for which we may not be able to tell which result is the most suitable.

The fact that hierarchical clustering would work even if presented with seemingly unrelated data could be a positive as well as a negative. As an illustration, in 2001, medical researchers have applied hierarchical clustering to identify gene expression patterns of breast carcinomas to distinguish tumor subclasses with clinical implications  $ [93] $. Interested readers may refer to many online examples of implementing agglomerative and divisive hierarchical clustering using Python.

##### 10.2.3.5 Density-Based Spatial Clustering of Applications with Noise (DBSCAN)

Easter et al. [94] first proposed a density-based clustering algorithm, called DBSCAN, in 1996. This algorithm overcomes the limitation of the K-means and hierarchical clustering algorithms, which fail in creating clusters of arbitrary shapes, and are unable to form clusters based on varying densities. Additionally, when compared to K-means clustering, DBSCAN does not require the number of clusters to be told beforehand.

We follow [63, p. 112] in describing the basic concept of the DBSCAN. Instead of guessing how many clusters we need, we define two hyperparameters, a limiting distance parameter  $ \varepsilon $ (epsilon) and a limiting number of clusters n, in DBSCAN. Epsilon is the radius of the cluster to be created around each data point, and n is the minimum number of samples (data points) required inside a cluster for that data point to be classified as a core point of the cluster.

We start by picking an example x from our dataset at random and assigning it to cluster 1. We then count how many examples (data points) have the distance from x less than or equal to  $ \varepsilon $. If this quantity is greater than or equal to n, then

---

<!-- PDF page 663 -->

<div style="text-align: center;">Figure 10.18 An illustration of the core points (red), noise (blue), and radius (epsilon) in the DBSCAN algorithm.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_408_147_802_453.jpg" alt="Image" width="40%" /></div>


we put all the  $ \varepsilon $-neighbors to the same cluster 1. We then examine each member of cluster 1 and find their respective  $ \varepsilon $-neighbors. If some member of cluster 1 has n or more  $ \varepsilon $-neighbors, we expand cluster 1 by adding those  $ \varepsilon $-neighbors to the cluster. We continue expanding cluster 1 until there are no more examples to put in it. We then pick another example from the dataset not belonging to any cluster and assign it to cluster 2. Continue like this until all examples either belong to some clusters or are marked as outliers. An outlier is an example whose  $ \varepsilon $-neighborhood contains less than n examples.

Figure 10.18 illustrates the circles of an equal radius  $ \varepsilon $ (epsilon) around every data point, with an assumed minimum number of samples required inside a cluster, n = 3. We see at least three samples or data points in the middle circles as the core points (in red). There are no other data points around the single data point within the upper right circle; we call this single data point a noise (in blue).

An advantage of DBSCAN over K-means clustering is that it can build clusters that have an arbitrary shape. However, specifying good values for the two required hyperparameters for DBSCAN could be challenging, and when epsilon is specified, the algorithm cannot effectively deal with clusters of varying density [63, p. 111]. We recommend that interested readers refer to online tutorials and examples of Python implementations of DBSCAN.

##### 10.2.3.6 Gaussian Mixture Model (GMM)

When clusters have different sizes and different correlation structures within them, the K-means clustering algorithm would not be effective. An alternative is to use the GMM. Here, we follow [1, pp. 738–741; 63, pp. 114–118; 74, pp. 259–274]. A GMM forms clusters as a mixture of multivariate normal density (Gaussian distribution) components. For a given observation, the GMM assigns a posterior probability to each component density (cluster). This probability indicates that the observation has some probability of belonging to the cluster. A GMM can perform hard clustering by choosing the component that maximizes the posterior probability as the assigned cluster for the observation. The GMM can also carry out a soft clustering by assigning the observations to multiple clusters based on the scores or posterior probabilities of the observations for the clusters.

---

<!-- PDF page 664 -->

There are several variants of the GMM, and we consider the simplest one here. To apply the algorithm, we must know in advance the number of k Gaussian distributions. Note that a standard Gaussian or normal probability distribution function with a mean  $ \mu $ and a standard deviation  $ \sigma $ is:

 $$ f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left[-\frac{1}{2}\Big(\frac{x-\mu}{\sigma}\Big)^{2}\right] $$ 

In Section A.1 of Appendix A of this book, we present the details of a  $ J \times K $ data matrix  $ \mathbf{X} $, where  $ K $ is the number of features or independent variables and  $ J $ is the number of observations or measurements. We also discuss the  $ 1 \times K $ sample mean for each of the  $ K $ features,  $ \overline{x}_k $, together with the sample standard deviation  $ \mathbf{s}_k $ and the sample covariance  $ s_{jk} $.

Figure 10.19, adopted from [74, p. 260], illustrates the basic structure of the GMM algorithm. We see the feature vector  $ \mathbf{x}_i $ and the corresponding label  $ y_i $ ( $ i = 1-j $). If  $ y_i = j $, it means that the  $ i $th instance has been assigned to the  $ j $th cluster, making the corresponding cluster label as  $ j $. The feature vectors within  $ j $th cluster follow a Gaussian (normal) probability distribution with a mean  $ \mu_j $ and a covariance matrix  $ \mathbf{\Sigma}_j $ ( $ j = 1-k $). This is indicated by  $ N(\boldsymbol{\mu}_j, \boldsymbol{\Sigma}_j) $.

In the figure, the circles represent random variables, and the squares represent fixed values. In the two large rectangles, we are to repeat the instance from $i=1-m$, and the cluster from $j=1-k$.

Given the dataset X, we start by estimating the weight factor vector w with components  $ w_j $ ( $ j = 1-k $), and all the Gaussian probability distribution parameters mean  $ \mu_j $ and covariance matrix  $ \Sigma_j $ ( $ j = 1-k $). The Python implementation of this procedure is “super easy,” according to [74, pp. 261–263], which gives the details of the GaussianMixture code.

Specifically, the algorithm includes two steps: first assigning instances to clusters (called the expectation step), and then updating the clusters (called the maximization step). Therefore, the core of the GMM algorithm is also called the EM algorithm. In the expectation step, the algorithm estimates the probability that each instance belongs to each cluster, based on the current cluster parameters. Then, during the

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_938_661_1219.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 10.19 The basic structure of the Gaussian mixture model.</div>


---

<!-- PDF page 665 -->

maximization step, the algorithm updates each cluster using all the instances in the dataset, with each instance weighted by the estimated probability that it belongs to the cluster. We call these probabilities the responsibilities of the clusters for the instances because each cluster's update will be most impacted by the instances it is most responsible for.

Lastly, when applying the GMM algorithm, we cannot use the silhouette score, illustrated previously in Figure 10.15, to choose the appropriate number of clusters, because the clusters in the GMM model are not spherical or have different sizes. Reference [74, pp. 267–269] presents the details and Python examples of using different criteria to choose an appropriate number of clusters.

### 10.3 Enhanced Learning by Ensemble Methods

#### 10.3.1 An Overview

Conventional learning methods try to develop a single learner from training data. By contrast, ensemble methods [30, 36, 40, 41, 95–106] train multiple learners to solve the same problem. Specifically, an ensemble contains a number of learners (trained models), called base learners, generated from training data by a base learning algorithm. We note that some references call a learned model a hypothesis [1, p. 696; 95, p. 2]. The generalization of an ensemble refers to the accuracy of the learners or trained models in predicting or classifying new data not used in the training process.

We often apply ensemble methods near the end of a project once we have already built a few good predictors as our base learners to combine them into an even better predictor [74, p. 189].

We focus on ensemble methods for the following reasons: (1) Gradient boosting, an ensemble method that we discuss below, implemented in the popular XGBoost package, is routinely used for both large-scale applications in industry for problems with billions of examples, and by the winners of data science competitions [1, p. 702]. In particular, over the past 15 years, ensemble methods have attracted the most attention and won the most times in the KDD-Cup, which is an annual data mining and knowledge discovery competition sponsored by the ACM special interest group on Knowledge Discovery and Data Mining [95, p. 17]. (2) The winning solutions in ML competitions often involve ensemble methods (the most famous in the Netflix Prize competition) [74, p. 189]. (3) According to the experience of Z.H. Zhou, the author of the excellent text, Ensemble Methods: Foundations and Algorithms, the best off-the-shelf learning techniques at present are ensemble methods [95, p. 21].

Ensemble methods are appealing mainly because they are able to boost weak learners, which are often just slightly better than random guesses, to become strong learners, which can make very accurate predictions, and give almost perfect performances. Schapire [96] has presented a theoretical proof that weak learners can be boosted to become strong learners. As it is easy to obtain base learners or weak learners from training data but difficult to generate strong learners in practice, ensemble methods present a promising path to generating strong learners.

---

<!-- PDF page 666 -->

Additionally, when we try to predict a target variable using any ML technique, the causes of difference in actual and predicted values are noise, variance, and bias. Ensemble methods do not lower the noise, which is an irreducible error. Depending on the type of ensemble learning algorithm that we use, an ensemble model may result in a lower bias than its component learners or in a lower variance than its component learners. It would be unlikely for an ensemble model to result in both lower bias and variance than its component learners, because of the well-known bias-variance tradeoff illustrated previously in Figure 10.3.

In general, we develop an ensemble in two steps, first to generate the base learners, which should be accurate and diverse, and then combine them appropriately to become strong learners. In this section, we apply the methods of bagging, boosting, and stacking in ML practice.

#### 10.3.2 Bagging: Random Forest Algorithm

The first method that we apply is bagging, which comes from the abbreviation of bootstrap aggregating, and thus implies two key ingredients of bootstrap and aggregation [99]. In statistics, a sample with replacement is called a bootstrap [1, p. 697]. Bootstrap involves the random sampling of a small subset of data from the dataset. When sampling is performed with replacement, this method is called bagging. When sampling is performed without replacement, it is called pasting [74, p. 192]. The method gives an equal probability to selecting all examples in the dataset. Suppose that we have a dataset with N samples and M features. Bagging begins by randomly selecting a sample from the dataset and a subset of features to create a model.

Most of the time, we use a single base learning algorithm so that we have homogeneous base learners that are trained in different ways. The algorithm then chooses the features from the subset that give the best split on the training data and repeats the same process to create many models, and every model is trained independently in parallel. Finally, the aggregations of predictions from all the models give the final prediction.

A popular bagging algorithm is the random forest algorithm [1, 101, pp. 697–698; 74, pp. 197–199; 95, pp. 57–60], which incorporates a randomized feature selection into the conventional bagging method for decision tree building. During the construction of a component decision tree, at each step of split selection, the algorithm randomly selects a subset of features, and then carries out the conventional split selection procedure within the selected features [95]. To obtain low-bias decision trees, each tree is grown to the maximum size and not pruned back. Random forest yields an ensemble of unstable individual learners, as their structures can drastically change with small changes in input. In general, aggregating the weak learners together can result in an ensemble model that achieves a lower variance than its component learners, even if the bias could also be reduced. The algorithm can handle multidimensional datasets and multiclass classification, and work well with noisy data [101].

With bagging, some instances may be sampled several times for any given predictor, while others may not be sampled at all. By default, the predictor samples m

---

<!-- PDF page 667 -->

training instances with replacement, where m is the size of the training set. This implies that only about 63.2% of the training instances are sampled on average for each predictor. This follows: as m grows, this ratio approaches  $ 1 - \exp[-1] = 63.2\% $ [5, p. 212]. The remaining 36.8% of the training instances that are not sampled are called out-of-bag (OOB) instances. Note that they are not the same 36.8% for all predictors. A bagging ensemble can be evaluated using the OOB instances without the need for a separate validation dataset [74, pp. 192–193].

Interested readers may refer to many Python implementations of random forest algorithms available online and in [74, pp. 192–198]. In Appendix B of this book, Code B.4 and Table B.1 at the end give the Python implementation of the random forest algorithm, together with a list of common parameters and their suggested values.

Workshop 10.1, Section 10.6, illustrates the actual implementation of the random forest algorithm for the prediction of MI in a slurry HDPE process. In this and other applications, the common procedure is as follows [30].

(1) Use existing libraries like Scikit-learn to import RandomForestRegressor.

(2) Load the required dataset and preprocess the data by following the steps for data cleaning, integration, and transformation.

(3) Split the dataset into test, validation, and training sets.

(4) Train the model and make baseline predictions.

(5) Tune the hyperparameters using GridSearch if advanced computing resources are available or using iteration methods with the aim of maximizing accuracy, speeding up processing, and minimizing overfitting. For random forest, GridSearch is preferred to select the right hyperparameters.

(6) Evaluate the model based on techniques like k-fold cross-validation or OOB instances and assess the performance using metrics like RMSE for accuracy.

Our recent article [30] explains more fundamentals and gives the details of each step of this implementation applied to an industrial fermentation process.

#### 10.3.3 Boosting: AdaBoost and XGBoost Algorithms

The most popular ensemble method is called boosting (originally called hypothesis boosting), which refers to a family of algorithms that are able to convert weak learners to strong learners. Briefly, boosting works by building a learner from the training data, and then creating a second learner that attempts to correct the errors from the first learner. We add learners sequentially, where the later learners focus more on the errors of the earlier learners. We stop adding learners when the training dataset is predicted almost perfectly, or a pre-specified maximum number of learners is reached. Roughly speaking, boosting the weak learners together can result in an ensemble model that achieves a lower bias than its component learners, even if variance could also be reduced.

We note that boosting is all about teamwork. Each model that runs will dictate what features the next model will focus on. It utilizes weighted averages to make weak learners into strong learners. By contrast, bagging has each model

---

<!-- PDF page 668 -->

run independently, and then aggregates the outputs at the end without giving preference to any model.

A well-known early boosting algorithm is the adaptive boosting (AdaBoost) algorithm, presented by Freund and Schapire in 1995 [103] initially for classifying datasets. This paper was recognized with the prestigious Gôdel Prize in 2003 for outstanding papers in theoretical computer science that is sponsored jointly by the European Association for Theoretical Computer Science (EATCS) and the Special Interest Group on Algorithms and Computation Theory of the Association for Computing Machinery (ACM SIGACT).

When training an AdaBoost classifier, the algorithm first trains a base classifier, such as a decision tree, and uses it to make predictions on the training set. The algorithm then increases the relative weights of misclassified training instances, and again makes predictions on the training set, updates the instance weights, and so on. Basically, the first classifier gets many instances wrong, so their weights get boosted. The second classifier therefore does a better job on these instances, and so on  $ [74, pp. 199–200] $.

Given a training set of N examples (features plus class labels), and a base learning model (e.g. a decision tree), AdaBoost trains a sequence of T base models or weak learners on T different sampling distributions defined upon the training set (D). The algorithm constructs a sample distribution  $ D_t $ for building the model t by modifying the sample distribution  $ D_{t-1} $ from the  $ (t-1) $-th step. In particular, examples classified incorrectly in the previous step receive higher weights in the new data, attempting to cover misclassified samples. Essentially, AdaBoost fits a sequence of weak learners on repeatedly modified versions of the training dataset, and then combines the predictions from all the weak learners through a weighted sum to give a more accurate, final prediction.

The other popular boosting algorithm is the gradient boosting algorithm presented by Friedman [104], who casts the boosting algorithm into a statistical framework as a numerical optimization problem. Just like AdaBoost, gradient boosting works by sequentially adding predictors to an ensemble, each one correcting its predecessors. However, instead of tweaking the instance weights at every iteration like AdaBoost does, gradient boosting tries to fit the new predictor to the residual errors made by the previous predictor [74, p. 203].

In the algorithm, one weak learner is added at a time, and existing learners in the model are frozen and left unchanged. This objective is to minimize the loss function of the model by adding weak learners using a gradient-decent-like procedure. The algorithm is attractive because it allows the use of arbitrary differentiable loss functions, thus expanding the boosting technique beyond traditional binary classification problems to support regression, multiclass classification, and more.

XGBoost is an optimized implementation of gradient boosting available in the popular Python library. It was first developed by Chen and Guestrin [105]. The advancements in XGBoost include regularization, flexibility, parallel processing, better tree pruning, and cross-validation at each iteration of the boosting process. XGBoost is designed to handle sparse data very well and is often an important element of the winning entries in ML competitions [74, p. 207].

---

<!-- PDF page 669 -->

The reader may refer to [74, pp. 202–207] and many online resources for examples of Python implementations of the AdaBoost and XGBoost algorithms.

The common procedure to implement XGBoost is similar to implementing random forest algorithm. It is as follows [30]:

(1) Install XGBoost for use with Python.

(2) Load the required dataset and preprocess the data by following the steps for data cleaning, integration, and transformation.

(3) Split the dataset into test, validation, and training sets.

(4) Train the model and make baseline predictions.

(5) Tune the hyperparameters based on iteration or GridSearch with the aim of maximizing accuracy, accelerating processing, and minimizing overfitting. For XGBoost, a lower learning rate and a higher number of boosting rounds accomplish the task.

(6) Evaluate the model based on techniques like k-fold cross-validation, and assess the performance using metrics like RMSE for accuracy.

Our recent article [30] explains more fundamentals and gives the details of each step of this implementation applied to an industrial fermentation process.

We refer the reader to Section 10.5.3, Workshop 10.1, and prediction of HDPE MI using random forest and XGBoost ensemble learning methods.

#### 10.3.4 Stacking: Stacked Regression

The third method that we apply is stacking [97, 98], which is a general procedure where a learner is trained to combine the individual learners. We call the individual learners the first-level learners and name the combined learner the second-level learner or meta-learner. To carry out stacking, we first train the first-level learners using the original training dataset, and then generate a new dataset for training the second-level learner [100]. In particular, we specify the outputs of the first-level learner as input features to the second-level learner and retain the original labels as labels of the new training dataset.

One way of applying stacking to regression, or stacked regression [98], is to form linear combinations of different predictors to give improved prediction accuracy. Specifically, we use different learning algorithms, with the complete training dataset, to construct the first-level learners. Then, a learning algorithm is used to train a second-level learner or a meta-regressor based on the first-level outputs. The idea is to use cross-validation and least squares under the constraint that all regression coefficients are nonnegative to determine the coefficients in the combination. This nonnegativity constraint guarantees that the performance of the stacked ensemble would be better than selecting the single best learner [98]. In his work introducing the concept of a super learner, van der Lann [106] theoretically proves the use of cross-validation to create an optimal learner by a weighted combination of many candidate learners. We use open-source ML libraries and ML extend for stacking regressor models along with the Scikit-learn library for the data analysis.

Interested readers may refer to [74, p. 211] and many online resources for Python implementation of the stacking algorithm.

---

<!-- PDF page 670 -->

### 10.4 Enhanced Learning by Deep Neural Networks

#### 10.4.1 Relevant Concepts of Conventional Neural Networks for Deep Learning Applications

##### 10.4.1.1 Basic Concepts and Parameters for a Multilayer Perceptron (MLP)

In Section 8.3.2.1 and Figure 8.101, we introduce the basic processing element (node or neuron) of a neural network. We did this to provide the context to introduce the nonlinear state-space-bounded derivative network (SSBDN) for nonlinear model-predictive control of polyolefin processes. In the following, we update the discussion in [4] to review the key concepts and parameters in a conventional neural network, focusing on their limitations and required changes when applied to a deep neural network (DNN). The word "deep" in deep learning refers to the number of hidden layers, that is, the depth of the neural network. Basically, every neural network with an input layer, an output layer, and two or more hidden layers is a deep neural network. In addition to referring to the number of hidden layers as "depth," we call the number of nodes or neurons in each layer as "width."

Figure 10.20 shows a three-layer perceptron. A perceptron is defined as a neural network with only feedforward interlayer connections. It has no interlayer or recurrent connections, as seen in the connection options in Figure 10.21.

We consider the neural network of Figure 10.20 for fault diagnosis of process data from a chemical reactor. Table 10.5 lists the input variables (features) and output variables (labels) for the network. For the inputs, we normalize the input values by dividing the actual input variable value by its maximum value, thus limiting each input value to a finite range, [0,1]. As included in Figure 10.20, the desired output, d, from the network is Boolean with 0 indicating no operational fault detected, and 1 indicating an operational fault detected, under the given conditions of input variables.

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_861_759_1223.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 10.20 A three-layer perceptron.</div>


---

<!-- PDF page 671 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_149_783_320.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 10.21 The connection options in a neural network.</div>


<div style="text-align: center;">Table 10.5 Input and output variables for the three-layer perceptron of Figure 10.20.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Input variable (feature)</td><td style='text-align: center; word-wrap: break-word;'>Output variable (label)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ I_{1} $: reactor inlet temperature ( $ ^{\circ} $F)</td><td style='text-align: center; word-wrap: break-word;'>$ c_{1} $: low conversion</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ I_{2} $: reactor inlet pressure (psia)</td><td style='text-align: center; word-wrap: break-word;'>$ c_{2} $: low catalyst selectivity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ I_{3} $: feed flow rate (lb/min)</td><td style='text-align: center; word-wrap: break-word;'>$ c_{3} $: catalyst sintering</td></tr></table>

The backpropagation algorithm consists of a forward activation flow and a backward error propagation to optimally select the network parameters, such as weight factors between neurons and internal thresholds of neurons.

We wish to train the network of Figure 10.20 to recognize the following specified conditions:  $ I_1 = 300/1000^\circ\text{F} = 0.3 $,  $ I_2 = 100/1000\text{psia} = 0.1 $,  $ I_3 = 200/1000\text{lb/min} = 0.2 $;  $ c_1 = 1 $ (low conversion),  $ c_2 = 0 $ (no problem),  $ c_3 = 0 $ (no problem).

Forward Activation Flow: Forward Output Prediction Step 1. Assume initial values of weight factors,  $ [v_{ij}] $ and  $ [w_{ij}] $, and internal thresholds,  $ [T_{ij}] $, within the range  $ [-1,+1] $.

 $$ [\nu_{i j}]=\begin{bmatrix}{{{-1}}}&{{{-0.5}}}&{{{0.5}}} \\{{{1}}}&{{{0}}}&{{{-0.5}}} \\{{{0.5}}}&{{{-0.5}}}&{{{0.5}}}\end{bmatrix}\quad[\boldsymbol{w}_{i j}]=\begin{bmatrix}{{{-1}}}&{{{-0.5}}}&{{{0.5}}} \\{{{1}}}&{{{0}}}&{{{0.5}}} \\{{{0.5}}}&{{{-0.5}}}&{{{0.5}}}\end{bmatrix}\quad[\boldsymbol{T}_{i j}]=\begin{bmatrix}{{{0}}}&{{{0}}}&{{{0}}} \\{{{0.5}}}&{{{0}}}&{{{-0.5}}} \\{{{0}}}&{{{0.5}}}&{{{-0.5}}}\end{bmatrix} $$ 

Step 2. Introduce the input vector I into the network of Figure 10.20. Calculate the output from the input layer, using a sigmoid transfer function:

 $$ x_{i}=I_{i}-T_{1i}\quad a_{i}=f(x_{i})=\frac{1}{1+\mathrm{e}^{-x_{i}}} $$ 

Substituting the values of  $ I_{1}=0.3 $,  $ I_{2}=0.1 $,  $ I_{3}=0.3 $,  $ T_{11}=T_{12}=T_{13}=0 $, we find  $ a_{1}=0.57444 $,  $ a_{2}=0.52498 $, and  $ a_{3}=0.54983 $.

Step 3. Given the output from the input layer, find the output from the hidden layer:

 $$ b_{j}=f\left(\sum_{1}^{3}(\mathbf{v}_{ij}a_{i})-T_{2j}\right) $$ 

---

<!-- PDF page 672 -->

where  $ f() $ is the sigmoid transfer function. We note that the terms inside the parenthesis represent the total activation; when the weighted sum of the inputs is larger than the internal threshold  $ T_{2j} $, we have a node firing, which generates a nonzero output from the hidden layer. This equation gives:

 $$ \begin{aligned}b_{1}&=f(v_{11}a_{1}+v_{21}a_{2}+v_{31}a_{3}-T_{21})\\&=f[(-1)(0.57444)+(1)(0.52498)+(0.5)(0.54983)-0.5]\\&=f(-0.27455)=0.43179\\ \end{aligned} $$ 

 $$ \begin{aligned}&b_{2}=f(v_{12}a_{1}+v_{22}a_{2}+v_{32}a_{3}-T_{22})=f(-0.56214)=0.36305\\ &\\ &b_{3}=f(v_{13}a_{1}+v_{23}a_{2}+v_{332}a_{3}-T_{23})=f(0.79965)=0.68990\\ \end{aligned} $$ 

Step 4. Given the output from the hidden layer, find the output from the output layer:

 $$ c_{k}=f\left(\sum_{1}^{3}(\mathbf{w}_{jk}\;b_{j})-T_{3k}\right) $$ 

This gives:

 $$ \begin{aligned}c_{1}&=f(w_{11}b_{1}+w_{21}b_{2}+w_{31}b_{3}-T_{31})\\&=f(0.27621)=0.56862(actual value,d_{1}=1)\\c_{2}&=f(w_{12}b_{1}+w_{22}b_{2}+w_{32}b_{3}-T_{32})\\&=f(-1.06085)=0.25715(actual value,d_{2}=0)\\c_{3}&=f(w_{13}b_{1}+w_{23}b_{2}+w_{33}b_{3}-T_{33})\\&=f(1.24237)=0.77598(actual value,d_{3}=0)\end{aligned} $$ 

Backward Error Propagation Step 5. Find improved network parameters  $ (v_{ij}, w_{ij}, $ and  $ T_{ij}) $ by minimizing the MSE (mean squared error), commonly called the loss function in training neural networks:

 $$  Loss function=MSE=\sum_{k}\varepsilon_{k}^{2}=\sum_{k}(d_{k}-c_{k})^{2} $$ 

In practice, we slightly modify the MSE equation by incorporating a gradient descent term of the transfer function. Specifically, we multiply the output error  $ (d_k - c_k) $ by a term of  $ c_k(1 - c_k) $, which results from differentiating the sigmoid transfer function:

 $$ f(x_{k})=\frac{1}{1+\mathrm{e}^{-x_{k}}}=c_{k} $$ 

The partial derivative is:

 $$ \frac{\partial f}{\partial x_{k}}=\frac{\mathrm{e}^{-x_{k}}}{(1+\mathrm{e}^{-x_{k}})^{2}}=\frac{1}{1+\mathrm{e}^{-x_{k}}}\left(1-\frac{1}{1+\mathrm{e}^{-x_{k}}}\right)=c_{k}(1-c_{k}) $$ 

---

<!-- PDF page 673 -->

For example, when we propagate the output error backward or backpropagate the output error from the output layer, the error term is:

 $$ \varepsilon_{1}=c_{1}(1-c_{1})(d_{1}-c_{1})=0.10581 $$ 

 $$ \varepsilon_{2}=c_{2}(1-c_{2})(d_{2}-c_{2})=-004912 $$ 

 $$ \varepsilon_{3}=c_{3}(1-c_{3})(d_{3}-c_{3})=-0.13489 $$ 

Step 6. Continue backpropagation from the output layer to the hidden layer. We find the jth component of the error vector,  $ \varepsilon_j $ of the hidden layer relative to each  $ \varepsilon_k $ using the following equation:

 $$ \varepsilon_{j}=b_{j}(1-b_{j})\left(\sum_{1}^{3}(\mathbf{w}_{jk}\varepsilon_{k})\right) $$ 

This equation applies the gradient term,  $ b_{j}(1 - b_{j}) $, to calculate the relative error. Applying this equation gives the relative errors of the hidden layer:

 $$ \varepsilon_{1}=b_{1}(1-b_{1})(w_{11}\varepsilon_{1}+w_{12}\varepsilon_{2}+w_{13}\varepsilon_{3})=-0.03648 $$ 

 $$ \varepsilon_{2}=b_{2}(1-b_{2})(w_{21}\varepsilon_{1}+w_{22}\varepsilon_{2}+w_{23}\varepsilon_{3})=0.008872 $$ 

 $$ \varepsilon_{3}=b_{3}(1-b_{3})(w_{31}\varepsilon_{1}+w_{32}\varepsilon_{2}+w_{33}\varepsilon_{3})=0.002144 $$ 

Step 7. Adjust weight factors according to the following formula:

 $$ \begin{bmatrix}new weight\\ factor\end{bmatrix}=\begin{bmatrix}old weight\\ factor\end{bmatrix}+\begin{bmatrix}learning\\ rate\end{bmatrix}\times\begin{bmatrix}input\\ term\end{bmatrix}\times\begin{bmatrix}gradient-descent\\ correction term\end{bmatrix} $$ 

or

 $$ w_{jk,\mathrm{new}}=w_{jk}+\eta_{3}b_{j}\varepsilon_{k}=w_{jk}+\eta_{3}b_{j}[c_{k}(1-c_{k})(d_{k}-c_{k})] $$ 

where  $ \eta_{3} $ is a positive constant with value between 0 and 1, called learning rate of the output layer; the input term is  $ b_{j} $ and the term within the bracket is the gradient-descent correction term.

Assume a constant learning rate of  $ \eta = 0.7 $. We adjust the weight factors as follows:

 $$ w_{11,new}=w_{11}+\eta b_{1}\varepsilon_{1}=-0.9680 $$ 

 $$ w_{12,new}=w_{11}+\eta b_{1}\varepsilon_{2}=-0.5149 $$ 

 $$ w_{13,new}=w_{11}+\eta b_{1}\varepsilon_{3}=0.4953 $$ 

Continuing these adjustments, we find the improved weight factors as follows:

 $$ \left[w_{jk}\right]=\begin{bmatrix}{{{-1}}}&{{{-0.5}}}&{{{0.5}}} \\{{{1}}}&{{{0}}}&{{{0.5}}} \\{{{0.5}}}&{{{-0.5}}}&{{{0.5}}}\end{bmatrix}\quad\left[w_{jk,new}\right]=\begin{bmatrix}{{{-0.9680}}}&{{{-0.5149}}}&{{{0.4593}}} \\{{{1.0269}}}&{{{-0.0125}}}&{{{0.4657}}} \\{{{0.5511}}}&{{{-0.5237}}}&{{{0.4349}}}\end{bmatrix} $$ 

Step 8. Adjust the internal thresholds for the output layer.

 $$ T_{3k,\mathrm{n e w}}=T_{3k}+\eta_{3}\varepsilon_{k} $$ 

---

<!-- PDF page 674 -->

With  $ \left[T_{31}\quad T_{32}\quad T_{33}\right]^{\mathrm{T}}=\left[0\quad0.5\quad-0.5\right] $ and a constant learning rate  $ \eta_{3}=0.7 $,  $ \varepsilon_{k} $ values from step 5, we find:

 $$ \left[T_{31,new}\ T_{32,new}\ T_{33,new}\right]=\left[0.0741\ 0.04656\ -0.5944\right] $$ 

Step 9. Adjust weight factors,  $ v_{ij} $, connecting the input and hidden layers according to:

 $$ v_{ij,new}=v_{ij}+\eta_{2}a_{i}\varepsilon_{j} $$ 

With  $ \eta_{2} $ of 0.7, we find:

 $$ \left[v_{ij}\right]=\begin{bmatrix}{{{-1}}}&{{{-0.5}}}&{{{0.5}}} \\{{{1}}}&{{{0}}}&{{{-0.5}}} \\{{{0.5}}}&{{{-0.5}}}&{{{0.5}}}\end{bmatrix}\quad\left[v_{ij,new}\right]=\begin{bmatrix}{{{-1.0147}}}&{{{-0.4964}}}&{{{0.5009}}} \\{{{0.9866}}}&{{{0.0033}}}&{{{-0.4992}}} \\{{{0.4860}}}&{{{-0.4966}}}&{{{0.5008}}}\end{bmatrix} $$ 

Step 10. Adjust the thresholds for the hidden layer,  $ T_{2j} $ in the hidden layer, following the equation:

 $$ T_{2j,\mathrm{n e w}}=T_{2j}+\eta_{2}\varepsilon_{j} $$ 

This gives

 $$ T_{21,new}=T_{21}+\eta_{2}\varepsilon_{1}=0.4745 $$ 

 $$ T_{22,new}=T_{22}+\eta_{2}\varepsilon_{2}=0.0062 $$ 

 $$ T_{23,new}=T_{22}+\eta_{2}\varepsilon_{2}=-0.4985 $$ 

Step 11. Repeat steps 2–10 until the MSE or the output-error vector  $ \varepsilon $ is zero or sufficiently small. It takes 3860 steps for deviation from the desired output  $ d_k $ to be less than 2%. We find:

 $$  Desired output:\left[d_{1}\ d_{2}\ d_{3}\right]=\begin{bmatrix}1&0&0\end{bmatrix} $$ 

 $$ \begin{aligned}Actual output:\begin{bmatrix}c_{1}&c_{2}&c_{3}\end{bmatrix}=\begin{bmatrix}0.9900&0.0156&0.0098\end{bmatrix}\end{aligned} $$ 

 $$  Percent error:\left[\varepsilon_{1}\ \varepsilon_{2}\ \varepsilon_{3}\right]=\left[1.00\%\ 1.56\%\ 0.98\%\right] $$ 

##### 10.4.1.2 Incorporation of a Momentum Coefficient

An improvement of the basic backpropagation algorithm illustrated in Example 10.1 is to use a technique known as momentum to speed up the training. Momentum is an extra weight factor added onto the weight factors when they are adjusted. By accelerating the change in the weight factors, we improve the training speed. Figure 10.22 illustrates the concept of momentum [4]. Suppose that we wish to reach the hill bottom B, which represents our global minimum. On the left plot of Figure 10.22, we encounter a rise in our downward path, and we may not be able to continue going downhill and get stuck at the local minimum A. One way to overcome this is to introduce an external momentum to help push us over the rise and eventually reach the hill bottom B, our global minimum, as illustrated in the

---

<!-- PDF page 675 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_755_326.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">Figure 10.22 An illustration of the concept of adding momentum to help reach a global minimum. (a) The object goes downhill, reaching a local minimum A. (b) Adding a momentum to push the object over a local maximum and then reach the global minimum B.</div>


right plot of Figure 10.22. To implement this concept, we add a momentum term to Eq. (10.51) as follows:

 $$ \begin{aligned}\begin{bmatrix}new weight\\ factor\end{bmatrix}&=\begin{bmatrix}old weight\\ factor\end{bmatrix}+\begin{bmatrix}learning\\ rate\eta\end{bmatrix}\times\begin{bmatrix}input\\ term\end{bmatrix}\\&\quad\times\begin{bmatrix}gradient-descent\\ correction term\end{bmatrix}+\begin{bmatrix}momentum\\ coefficient\\\alpha\end{bmatrix}\begin{bmatrix}previous\\ weight\\ change\end{bmatrix}\end{aligned} $$ 

Both the learning rate  $ \eta $ and momentum coefficient  $ \alpha $ have values greater than zero, and less than or equal to one. Heuristically, good values to use are:  $ \eta = 0.4 - 0.7 $;  $ \alpha = 0.4 $ [4]. We introduce their concepts here, as they are important “hyperparameters” in the training of DNNs. Note that we refer to properties in the learning algorithm that must be set before training as hyperparameter, such as the learning rate in the backpropagation algorithm. Hyperparameter is different from a parameter that the algorithm is trying to learn and optimize during training; for example, those parameters are the weights and biases in a neural network model. In fact, Geron [74, p. 325] claims that the learning rate is arguably the most important hyperparameter for training a MLP.

##### 10.4.1.3 Alternative Basic Network Configuration Using Bias Inputs Instead of Internal Thresholds

In Eqs. (10.46) and (10.47), we subtract the internal thresholds  $ T_{ij} $ ( $ i,j=1-3 $) from the weighted sum of inputs to each node or neuron, as the input to the transfer function to generate the output from each node. Figure 10.23 shows an alternative basic network configuration that has an extra “bias” input from a “bias” node that is fixed to +1 and weight factors ( $ v_{01}, v_{02}, v_{03}, w_{01}, w_{02} $, and  $ w_{03} $) going from that node to the nodes in the hidden and output layers. By doing so, we may re-write Eq. (10.46) as follows:

 $$ b_{j}=f\left(\sum_{1}^{3}(\mathbf{v}_{ij}a_{i})-T_{2j}\right) $$ 

 $$ b_{j}=f\left(\sum_{1}^{3}(\mathbf{v}_{ij}a_{i})+\mathbf{v}_{0j}a_{0}\right) $$ 

---

<!-- PDF page 676 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_144_757_503.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 10.23 Alternative basic network configuration using bias inputs instead of internal thresholds. Weight factors  $ (v_{01}, v_{02}, v_{03}, w_{01}, w_{02}, \text{and } w_{03}) $ connect the bias node to the nodes directed by the dashed arrow.</div>


 $$ b_{j}=f\left(\sum_{0}^{3}(\mathrm{v}_{ij}a_{i})\right)\quad(a_{0}=1,T_{2j}=-\nu_{0j}) $$ 

Following Eq. (10.58), we can re-write Eq. (10.47) in a similar way.

What is the advantage of using the bias inputs, instead of the internal thresholds? By setting the initial weight factors  $ (v_{01}, v_{02}, v_{03}, w_{01}, w_{02}, \text{and } w_{03}) $ to be nonzero, the total weighted sum of inputs to each node will be nonzero, even when the outputs of the preceding layer are all zero [1, p. 752].

Based on Eqs. (10.57) and (10.58), we can write the output of a fully connected layer in a vector-matrix form:

 $$ \mathbf{h}_{\mathbf{W},\mathbf{b}}(\mathbf{X})=\varphi(\mathbf{X}\mathbf{W}+\mathbf{b}) $$ 

In the equation,

X = the matrix of input features. It has one row per instance and one column per feature (independent variable);

W = the weight matrix, containing all the connection weights, except for the ones from the bias node (neuron). It has one row per input neuron and one column per artificial neuron in the layer.

b = the bias vector, containing all the connection weights between the bias neuron and the artificial neurons. It has one bias term per artificial neuron.

 $ \varphi = $ the activation function for the neurons in the layer.

Equation (10.59) will be useful when we discuss the structure of RNNs below.

---

<!-- PDF page 677 -->

<div style="text-align: center;">Table 10.6 Activation functions and their derivatives.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Activation function</td><td style='text-align: center; word-wrap: break-word;'>Function,  $ y = f(x) $</td><td style='text-align: center; word-wrap: break-word;'>Derivative,  $ y&#x27;(x) = f&#x27;(x) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. Sigmoid (Logistic)</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{1 + e^{-x}} $</td><td style='text-align: center; word-wrap: break-word;'>$ f(x)[1 - f(x)] = e^{-x}/(1 + e^{-x})^{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Hyperbolic tangent (tanh)</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} $</td><td style='text-align: center; word-wrap: break-word;'>$ 1 - [f(x)]^{2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Rectified linear unit (ReLU)</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) = 0 $, if  $ x &lt; 0 $;  $ f(x) = x $, if  $ x \geq 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ f&#x27;(x) = 0 $, if  $ x &lt; 0 $;  $ f&#x27;(x) = 1 $, if  $ x \geq 0 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. Softplus</td><td style='text-align: center; word-wrap: break-word;'>$ \ln(1 + e^{x}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{1 + e^{-x}} $ (sigmoid)</td></tr></table>

##### 10.4.1.4 Selection of Activation Functions, Vanishing Gradient, and Exploding Gradient Problems

Table 10.6 summarizes four activation functions that are commonly used in both conventional and deep neural networks. Figure 10.24 illustrates these functions and their derivatives. We note that for the sigmoid activation function, when the input (x) becomes large (negative or positive), the output (y) saturates or becomes constant at 0 or 1. We call this type of activation function a saturating activation function. By contrast, the rectified linear unit (ReLU) activation function is a nonsaturating activation function. This point is relevant to our discussion below relating to fighting unstable gradient problems in the training of DNNs.

For the first 25 years of research with multilayer neural networks (roughly 1985–2010), internal nodes used sigmoid and hyperbolic tangent (tanh) activation functions, almost exclusively. From around 2010 onwards, the ReLU and softplus activation functions became more popular, particularly because they had better derivative properties and could avoid the problems of vanishing/exploding gradients observed when using the gradient descent method to train the networks [1, p. 759].

As demonstrated in the example, during the backward error flow, the backpropagation algorithm works by going from the output layer to the input layer, propagating the error gradient along the way. Once the algorithm has computed the gradient of the loss function (the mean squared error) regarding each parameter (weight factor and internal threshold or bias input) in the network, it applies the gradient to update each parameter with a gradient descent step using, for example, Eq. (10.4). Unfortunately, the gradient tends to get smaller and smaller as the algorithm progresses, approaching the lower layers (i.e. approaching the input layer). Consequently, the gradient descent update leaves the parameters of the lower layers virtually unchanged, and training never converges to a good solution. We call this the vanishing gradient problem [74, p. 331].

The exploding gradient problem is the inverse of the vanishing gradient problem and occurs when large error gradients accumulate, resulting in extremely large updates to neural network model weights during training. As a result, the model is unstable and incapable of learning from training data.

---

<!-- PDF page 678 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-axis</th><th style='text-align: center;'>ReLU</th><th style='text-align: center;'>Sigmoid</th><th style='text-align: center;'>Tanh</th><th style='text-align: center;'>Softplus</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-5</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-4</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-1.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-0.9</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.0</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>X-axis</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Blue</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Black</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>-5</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-4</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-3</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-2</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>-1</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.24 An illustration of common activation functions and their derivatives.</div>


As shown in Table 10.7 and in Figure 10.24, when using the ReLU activation function and its smooth variant, softplus activation function, with their positive function and derivative values, the output from a node will always be positive. Using them as activation functions helps avoid the vanishing gradient problem. Research since 2010 has suggested that when training neural networks, particularly DNNs with two or more hidden layers, ReLU is the most used activation function. Many software libraries and hardware accelerators provide ReLU-specific optimizations. If training speed is your top priority, ReLU should be your best choice as the activation function to use [74, p. 338].

---

<!-- PDF page 679 -->

<div style="text-align: center;">Table 10.7 Typical architecture for regression MLP for deep learning applications.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Item</td><td style='text-align: center; word-wrap: break-word;'>Typical value or selection</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. # of input neurons</td><td style='text-align: center; word-wrap: break-word;'>1. One per feature (independent variable)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. # of hidden layers</td><td style='text-align: center; word-wrap: break-word;'>2. Typically 2-5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. # of neurons per hidden layer</td><td style='text-align: center; word-wrap: break-word;'>3. Typically 10-100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. # of output neurons</td><td style='text-align: center; word-wrap: break-word;'>4. One per label (dependent variable)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. Activation function, hidden layers</td><td style='text-align: center; word-wrap: break-word;'>5. ReLU or Softplus</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6. Output activation function</td><td style='text-align: center; word-wrap: break-word;'>6. None</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7. Loss function</td><td style='text-align: center; word-wrap: break-word;'>7. MSE (mean squared error)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8. Hyperparameter optimization algorithm</td><td style='text-align: center; word-wrap: break-word;'>8. Adam (Adaptive momentum estimation)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9. Hyperparameters</td><td style='text-align: center; word-wrap: break-word;'>9. Momentum coefficient, learning rate, weight decay, dropout, batch normalization</td></tr></table>

##### 10.4.1.5 Batch Normalization (BN)

We follow [74, p. 338] to introduce the concept of BN, proposed by Ioffe and Szegedy [107], to improve neural network training. While using ReLU activation function and its smooth variant, Softplus, can significantly reduce the vanishing/exploding gradients at the beginning of the training, it does not guarantee that they won't return during training. BN helps avoid these problems by adding an operation in the model just before or after the activation of each hidden layer.

This operation simply zero-centers and normalizes each input (we discuss standardized data by mean-centered data scaled by standard deviation in Section A.1.7 of Appendix A of this book). BN then scales and shifts the result using two new parameter vectors per layer: on for scaling, and the other for shifting. Essentially, the operation lets the model learn the optimal scale and mean of each layer's inputs. In many cases, you can implement BN by adding a BN layer as the very first layer of your neural network, and you do not need to standardize your training set (such as by using Python code, StandardScaler in Section 10.7.5) in Figure 10.45, the BN layer will do it for you.

Ioffe and Szegedy [107] have demonstrated that BN considerably improves all the DNNs they experimented with, leading to a huge improvement in image classification network and a significant reduction of the vanishing gradient problem. BN can also reduce the risk of overfitting, which we discussed in Section 10.2.1.1. Constraining a model to make it simpler and reduce the risk of overfitting is called regularization [74, p. 27], which we discuss more below.

##### 10.4.1.6 Avoid Overfitting Through Regularization: Weight Decay and Dropout

Regularization attempts to limit the complexity of a model, as we want to find the right balance between fitting the training data perfectly and keeping the model

---

<!-- PDF page 680 -->

simple enough to ensure that it will generalize well with validation data. An approach to regularization is called weight decay, which involves adding a penalty  $ \lambda(\sum_{ij} \left(v_{ij}^2 + w_{ij}^2\right)) $, where  $ v_{ij} $ and  $ w_{ij} $ are weight factors defined in Eqs. (10.46) and (10.47), to the loss function (MSE), Eq. (10.48).  $ \lambda $ is a hyperparameter of the ML training algorithm controlling the strength of the penalty, and the penalty term is to sum the squares of all the weights in the network. Using  $ \lambda = 0 $ is equivalent to not using weight decay, while using a larger value of  $ \lambda $ encourages the weights to become small. A heuristic value is for  $ \lambda $ to be near  $ 10^{-4} $ [1, p. 771].

Another popular regularization technique is to use dropout [1, p. 772; 74, p. 365; 108]. It is a fairly simple algorithm. At every training step, every neuron (including the input neurons but always excluding the output neurons) has a probability p of being temporarily “dropped out,” meaning it will be entirely ignored during this training step, but it may be active during the next step. The hyperparameter p is called the dropout rate, and its heuristic value to use is between 10% and 50%. For the RNNs discussed below, p is about 20–30%; and for CNNs discussed below, p is about 40–50%. After training, neurons don’t get dropped anymore. It has been proven that dropout improves the accuracy of state-of-the-art neural networks by 1–2%. In practice, this is significant because, if a model already has 95% accuracy, getting a 2% accuracy boost means dropping the error rate by almost 40% (going from 5% error to roughly 3%) [74, p. 365].

Finally, Zhou et al. [109] present a detailed hyperparameter optimization study of DNNs for absorption, distribution, metabolism, and excretion (ADME) properties of pharmaceutical industries. They tested the following hyperparameters: learning rate (0.01, 0.1, and 1), weight decay (0, 1E-6, 1E-5, 1E-4, and 1E-3), dropout rate (0, 0.2, 0.4, and 0.6), activation function (ReLU and sigmoid), and BN (with and without). We have already incorporated their observations in our preceding discussion, together with suggestions for heuristic hyperparameter values.

##### 10.4.1.7 Using a Faster Optimizer

Training a DNN can be painfully slow. There are ways to speed up the training. We refer the reader to [74, pp. 350–359] for a detailed discussion of these methods. We did discuss some of them, such as using a good activation function, ReLU, and applying BN. Another improvement to training speed comes from using a faster optimizer, instead of the regular gradient-descent algorithm. In particular, we recommend the reader to glance through a classic paper by Kingma and Ba [110] introducing Adam (Adaptive Moment Estimation), an algorithm for first-order gradient-based optimization of stochastic objective function or loss function.

Adam optimizer is the recommended scheme for minimizing the loss function for training a DNN. Without going through the specific equations for the algorithm (see [74], p. 356), we note that the default values for three hyperparameters in the algorithm are: learning rate, lr or  $ \eta = 0.001 $; momentum decay parameter  $ \beta_1 = 0.9 $; scaling decay hyperparameter  $ \beta_2 = 0.999 $. Implementing these parameters in Python using Keras is simple:

---

<!-- PDF page 681 -->

Optimizer = keras.optimizer.Adam(lr = 0.001, beta_1 = 0.9, beta_2 = 0.999)

We demonstrate in Section 10.7.3 how to apply the Adam optimizer using Python in Keras to predict the HDPE MI using a DNN.

##### 10.4.1.8 Recommended Multilayer Perceptron (MLP) Architecture for Deep Learning Applications

We adopt and expand the recommendations of Ref. [74, p. 292] and present Table 10.7 to summarize the typical MLP architecture for deep learning applications.

In Appendix B of this book, Code B.6 and Table B.1 at the end give the Python implementation of the DNN algorithm, together with a list of common parameters and their suggested values.

We refer the reader to Section 10.7, Workshop 10.2, and prediction of HDPE MI by a DNN.

Lastly, we share an important empirical finding about deep learning in choosing the number of layers and the number of neurons [1, p. 769]. When comparing two networks with similar numbers of weight factors, a deeper network with a higher number of layers usually gives better generalization performance, showing a higher accuracy in predicting the validation data that the network has not seen previously in its training, than a shallow network with a smaller number of layers.

#### 10.4.2 Deep Learning with Recurrent Neural Networks (RNNs)

##### 10.4.2.1 Recurrent Neural Networks for Predictive Modeling

## of Time-Dependent Processes

RNNs are mostly used to deal with sequential or time-dependent data types like time-series data. Our previous book [4, pp. 228–364] gives a detailed report on applying RNNs to process forecasting, modeling, and control of time-dependent processes in chemical engineering. References [45, 48, 50–54, 57, 75, 87, 111–117] present deep learning with RNNs with applications to chemical industries. In Section 10.8, we present Workshop 10.3 demonstrating the prediction of time-dependent HDPE MI using deep RNNs.

We can train RNNs by backpropagation through time, which is a popular method for training conventional neural networks [4]. In the following, we follow [74, pp. 499–502] to present the key concepts of deep RNNs.

Part (a) of Figure 10.25 shows that in recurrent connection, the output from a node feeds into itself. On the very right part of the figure, we see that the recurrent neuron receives the input vector  $ \mathbf{x}(t) $ and its own output vector from the previous time step,  $ \mathbf{y}(t-1) $. There is no previous output at the first time step, it is set to zero. Part (b) of Figure 10.25 illustrates how this recurrent neuron evolved over time.

For each recurrent neuron, we have two sets of weight factors (say,  $ \mathbf{w}_x $ and  $ \mathbf{w}_y $): one for the input vector  $ \mathbf{x}(t) $, and the other for the output vector from the previous time step,  $ \mathbf{y}(t-1) $. When considering the whole recurrent layer, instead of just one recurrent neuron, we can place all the weight factors in two weight matrices,  $ \mathbf{W}_x $.

---

<!-- PDF page 682 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_146_574_332.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">Figure 10.25 The recurrent connection (a) and recurrent neuron evolved over time (b).</div>


<div style="text-align: center;">(b)</div>


and  $ \mathbf{W}_{y} $. Following the concept of Eqs. (10.57)–(10.59), we can represent the output vector of the whole recurrent layer for a single instance (i.e. one sample) as follows:

 $$ \mathbf{y}(t)=\varphi\left(\mathbf{W}_{x}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{y}^{\mathrm{T}}\mathbf{y}(t-1)+\mathbf{b}\right) $$ 

In this equation,  $ \varphi $ is the activation function, and b is the bias vector consisting of the bias inputs to all neurons in the recurrent layer.

We can further extend this representation for a layer of recurrent neurons for all instances (samples) in a mini-batch by placing all the input vectors for different instances (samples) at time step t in an input matrix  $ \mathbf{X}(t) $ and all the output vectors for different instances (samples) from time step  $ t-1 $ in an output matrix  $ \mathbf{Y}(t-1) $. Therefore, we represent the outputs of a layer of recurrent neurons for all instances in a mini-batch as follows:

 $$ \begin{aligned}\mathbf{Y}(t)&=\varphi\left(\mathbf{W}_{x}^{\mathrm{T}}\mathbf{X}(t)+\mathbf{W}_{y}^{\mathrm{T}}\mathbf{Y}(t-1)+\mathbf{b}\right)\\&=\varphi(\mathbf{X}(t)\mathbf{W}_{x}+\mathbf{Y}(t-1)\mathbf{W}_{y}+\mathbf{b})\\&=\varphi[\mathbf{X}(t)\mathbf{Y}(t-1)]\mathbf{W}+\mathbf{b})\\ \end{aligned} $$ 

with  $ \mathbf{W} = \left[\mathbf{W}_x \mathbf{W}_y\right]^T $. Assume that  $ m $ is the number of instances (samples) in the mini-batch,  $ n_{\text{neurons}} $ is the number of neurons, and  $ n_{\text{inputs}} $ is the number of input features. In Eq. (10.61):

 $ \mathbf{Y}(t) = \text{an } m \times n_{\text{neurons}} \text{ matrix containing the recurrent layer's outputs at time step } t $ for each instance in the mini-batch

 $ \mathbf{X}(t) = \text{an } m \times n_{\text{inputs}} \text{ matrix containing the recurrent layer's inputs at time step } t \text{ for all instances in the mini-batch} $

 $ \mathbf{W}_x = \text{an } n_{\text{inputs}} \times n_{\text{neurons}} \text{ matrix containing the weight factors for the inputs of the current time step} $

 $ \mathbf{W}_y = \text{an } n_{\text{neurons}} \times n_{\text{neurons}} \text{ matrix containing the weight factors for the output of the previous time step} $

b = a vector of size n neurons containing each neuron's bias input

$$\mathbf{W}=\left[\mathbf{W}_{x}~\mathbf{W}_{y}\right]^{\mathrm{T}}.$$ The weight factor matrices $\mathbf{W}_{x}$ and $\mathbf{W}_{y}$ are linked together vertically in a single matrix $W$ of dimension $(n_{\mathrm{inputs}}+n_{\mathrm{neurons}})\times n_{\mathrm{neurons}}$

 $$ [\mathbf{X}(t)\mathbf{Y}(t-1)]=1 $$ 

Note that  $ \mathbf{Y}(t) $ depends on  $ \mathbf{X}(t) $ and  $ \mathbf{Y}(t-1) $, which are function of  $ \mathbf{X}(t-1) $ and  $ \mathbf{Y}(t-2) $, which is a function of  $ \mathbf{X}(t-2) $ and  $ \mathbf{Y}(t-3) $, and so on. Therefore,  $ \mathbf{Y}(t) $ depends on all the inputs since time = 0, that is,  $ \mathbf{X}(0) $,  $ \mathbf{X}(1) $,  $ \mathbf{X}(2) $, ...,  $ \mathbf{X}(t) $. At time = 0, there are no previous outputs, which are assumed to be all zeros.

---

<!-- PDF page 683 -->

<div style="text-align: center;">Figure 10.26 An illustration of backpropagation through time.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_403_145_800_338.jpg" alt="Image" width="41%" /></div>


Let us extend the backpropagation algorithm discussed in Section 10.4.1 to a time-dependent RNN. Figure 10.26 illustrates the concept of backpropagation through time for training a RNN.

We begin with a forward activation pass through the evolved network from the left to the right, represented by the dashed arrows. We then evaluate the output sequence using a cost or loss function,  $ C\left[\mathbf{Y}(0),\mathbf{Y}(1),\mathbf{Y}(2),\ldots,\mathbf{Y}(T)\right] $, where T is the maximum time step. Next, we proceed with the backward error propagation. The gradients of the cost function are propagated backward through the evolved network (represented by solid arrows). We update the model parameters using the gradients computed during the backpropagation through time.

We compute the cost function using the last three outputs of the network,  $ \mathbf{Y}(2) $,  $ \mathbf{Y}(3) $, and  $ \mathbf{Y}(4) $, so the gradient flows through these three outputs, but not through  $ \mathbf{Y}(0) $ and  $ \mathbf{Y}(1) $. In other words, the gradient flow background through all the outputs used by the cost function, not just the final output. Lastly, as the weight factor matrix  $ \mathbf{W} $ and the bias vector  $ \mathbf{b} $ are used at each time step, backpropagation should sum over all time steps.

There are several issues regarding the applicability of the recommendations for DNNs discussed in Sections 10.4.1–40.1.8 to train RNNs [74, pp. 511–512]. Training an RNN on long sequences with many time steps tends to make the evolved network (see the Part (b) of Figure 10.27) a very deep network. This means that training RNNs may suffer the same unstable (vanishing/exploding) gradient problems that we discussed with DNNs.

<div style="text-align: center;">Figure 10.27 A deep RNN (a) evolved through time (b).</div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_379_990_800_1249.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">(b)</div>


---

<!-- PDF page 684 -->

Many of the techniques that we discussed in Sections 10.4.1.4–10.4.1.8 for DNNs to overcome the unstable gradient problems are still applicable, but with some cautions and exceptions. First, we can still apply a faster optimizer (Section 10.4.1.7) and dropout (Section 10.4.1.6). However, we should apply BN (Section 10.4.1.5) only between recurrent layers (vertically in Figure 10.27), but not between time steps (horizontally in Figure 10.27). In other words, we could add a BN layer before each recurrent layer, but do not expect too much from it, as research [112] has shown that BN was only slightly beneficial when applied to the inputs at the current time step, but not to the outputs from the previous time step.

For developing deep RNNs, nonsaturating activation functions such as ReLU discussed in Section 10.4.1.4 and Figure 10.24 may not help much in fighting the unstable gradient problems. In fact, they may actually lead the RNN to be more unstable during training. Why? Suppose that the gradient descent updates the weight factors in a way that increases the output slightly in the first time step. Because the algorithm uses the same weight factors at every time step, it may slightly increase the outputs at the second time step. This increase in outputs continues in subsequent time steps, and the increasingly large output could eventually “explode.” We could reduce this risk by using a smaller learning rate and by using a saturating activation function like hyperbolic tangent (tanh), which is recommended as the default activation function for deep RNNs [74, p. 511].

Glorot and Bengio [108] suggest that a better initialization of weight factors could also help in alleviating the unstable gradient problems in RNNs. For both the forward activation flow and the backward error propagation to move properly, the authors argue that we need the variance of the outputs of each layer to be equal to the variance of its inputs, and we need the gradients to have equal variance before and after flowing through a layer in the reverse direction. In practice, we cannot satisfy this requirement unless the layer has an equal number of inputs and neurons (these numbers are called the fan-in and fan-out of the layer). Glorot and Bengio propose a good weight-factor initialization scheme, called the Glorot initialization in Python Keras code that works well in practice. Specifically, initialize the weight factors following a normal distribution with mean 0 and variance  $ \sigma^2 = 1/\text{fan}_{\text{avg}} = 2/(\text{fan}_{\text{in}} + \text{fan}_{\text{out}}) $ [74, p. 333].

Bengio and coworkers [112] proposed the concept of “scaling down the gradient” or “gradient clipping” to tackle vanishing/exploding gradients. Gradient clipping involves clipping the derivatives of the loss function (mean squared error) to have a given value if a gradient value is less than a negative threshold or more than a positive threshold. For example, we could specify a norm of 0.5, meaning that if a gradient value was less than -0.5, it is set to 0.5; and if it is larger than 0.5, then it will be set to 0.5.

Let  $ \|\mathbf{g}\| $ be the norm of the gradient vector, we replace  $ c(\mathbf{g}/\|\mathbf{g}\|) $ by  $ \mathbf{g} $, where  $ c $ is a hyperparameter called the threshold,  $ \mathbf{g} $ is the gradient, and  $ \mathbf{g}/\|\mathbf{g}\| $ is a unit vector. After  $ r $-scaling, the new gradient will have  $ \|\mathbf{g}\| = c $. If  $ \|\mathbf{g}\| < c $, then we do not need to do anything.

Alternatively, we can visualize gradient clipping as forcing the gradient values (element-wise) to a specific minimum or maximum value if the gradient exceeded

---

<!-- PDF page 685 -->

an expected range. When the traditional gradient descent method tends to make a large step, the gradient clipping intervenes to reduce the step size to be small enough that it is less likely to go outside the region where the gradient indicates the direction of approximately steepest descent.

In addition to the unstable gradient problems, deep RNNs suffer from a short-term memory problem, which we explain in Section 10.4.2.2.

##### 10.4.2.2 Long Short-Term Memory (LSTM) RNNs

This section introduces the concept of the LSTM RNNs. We refer the reader to [45, 48, 57, 118] for several reported applications of the LSTM RNNs to chemical processes and to Section 10.8 for a Workshop 10.3 for predicting the MI in a grade transition in a HDPE process.

Because of the data transformation through the transfer function when input data travel through an RNN, the network tends to lose some information at each time step. After a while, the RNN's state could contain virtually no trace of the first inputs. To tackle this problem, there are useful changes to the architecture of the conventional RNN that enable the data information to be preserved over many time steps.

We follow [1, p. 775; 74, pp. 514–517; 114] to introduce a special kind of RNN with memory units, called the long short-term memory (LSTM) cell, as illustrated in Figure 10.28. Basically, this cell includes three special gates: a forget gate to select memory or to forget the irrelevant part of the previous state; an input gate to update memory or to selectively update the cell-state values; and an output gate to select

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_714_778_1218.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 10.28 An illustration of a LSTM cell.</div>


---

<!-- PDF page 686 -->

output or to output certain parts of the cell state. A cell state vector  $ \mathbf{c}(t-1) $ goes through these three gating operations, the surviving memory becomes a state vector  $ \mathbf{c}(t) $, for which we call it a long-term state vector.

We see that the input vector  $ \mathbf{x}(t) $ at time  $ t $ (labeled vector 1 in the figure) and the output vector from the previous time step,  $ \mathbf{h}(t-1) $ (labeled vector 2) both enter a filtering unit with a sigmoid activation function, giving an output vector  $ \mathbf{f}(t) $ (labeled vector 4), which becomes an input vector to the forget gate. Following Eq. (10.60), we represent  $ \mathbf{f}(t) $ as:

 $$ \mathbf{f}(t)=\sigma\left[\mathbf{W}_{x f}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{h f}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{f}\right] $$ 

where  $ \sigma $ is the sigmoid activation function with an output vector with scalar components bounded between 0 and 1 (see Figure 10.24). In Eq. (10.62) and the subsequent Eqs. (10.63)–(10.66):

 $ W_{xi}, W_{xf}, W_{xo}, W_{xg} $ are the weight factor matrices for each of the three gates (input, forget, output) and gating unit for their connection to the input vector  $ \mathbf{x}(t) $.

 $ W_{hi}, W_{hf}, W_{ho}, W_{hg} $ are the weight factor matrices for each of the three gates (input, forget, output) and gating unit for their connection to the previous short-term state or output vector from the previous time step,  $ \mathbf{h}(t-1) $.

 $ b_{i}, b_{f}, b_{o}, b_{g} $ are the bias terms for each of the three gates (input, forget, output) and gating unit.

Next, we can represent a similar filtering operation to generate an output vector  $ \mathbf{i}(t) $ serving as an input vector to the input gate (labeled vector 6):

 $$ \mathbf{i}(t)=\sigma\left[\mathbf{W}_{x i}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{h i}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{i}\right] $$ 

We also represent a similar operation to generate an output vector  $ \mathbf{o}(t) $, which serves as an input vector to the output gate (labeled vector 7):

 $$ \mathbf{o}(t)=\sigma\left[\mathbf{W}_{xo}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{ho}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{o}\right] $$ 

Both  $ \mathbf{x}(t) $ and  $ \mathbf{h}(t-1) $ also enter a gating unit with a hyperbolic tangent (tanh) activation function, giving an output vector  $ \mathbf{g}(t) $ (labeled vector 5), which becomes an input vector to the input gate. We represent  $ \mathbf{g}(t) $ as:

 $$ \mathbf{g}(t)=\tanh\left[\mathbf{W}_{xg}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{hg}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{g}\right] $$ 

where  $ \tanh $ is the hyperbolic tangent activation function with an output vector with scalar components bounded between -1 and 1 (see Figure 10.24).

The key idea is that when the long-term state  $ \mathbf{c}(t-1) $ (labeled vector 3) flows through the network from left to right, it first goes through a forget gate f, which selects the information that needs to be discarded by combining the previous cell state  $ \mathbf{c}(t-1) $ (labeled vector 3) to the output vector  $ \mathbf{f}(t) $ from a filtering unit (labeled vector 4), defined by Eq. (10.58) above, through an element-wise multiplication (as indicated by symbol  $ \otimes $ below the words "Forget gate" in the figure). This results in an output vector 8 in the figure. Note that we covered the element-wise multiplication, called Hadamard product, in Section 8.1.4.1, Eq. (8.40).

---

<!-- PDF page 687 -->

Next, we drop some memories and then add new memories selected by an input gate i. Specifically, we carry out an element-wise multiplication of output vector  $ g(t) $ (labeled vector 5), defined by Eq. (10.55), and output vector  $ i(t) $ (labeled vector 6), defined by Eq. (10.53). This results in an output vector from the input gate, labeled vector 9. We then merge the output vector from the forget gate, vector 8, and the output vector from the input gate, vector 9. This gives an output vector that has survived through the operations within the forget and input gates. In the figure, we represent this output vector as a long-term state vector  $ c(t) $, labeled vector 10 in the figure. We present this operation as:

 $$ \mathbf{c}(t)=\mathbf{f}(t)\otimes\mathbf{c}(t-1)+\mathbf{i}(t)\otimes\mathbf{g}(t) $$ 

As we will send shortly the same information for the long-term state vector  $ \mathbf{c}(t) $ to an output gate for processing, we label that vector as vector 11 in the figure.

Vector 11 then goes through a hyperbolic tangent activation function with an output vector with scalar components bounded between -1 and 1 (see Figure 10.24). This results in an output vector labeled vector 12. This vector then multiplies with output vector 5 from the output gate element-wise to give an output vector, labeled vector 13, which is identical to the output vector  $ \mathbf{y}(t) $ at time step  $ t $, and to the short-term state vector,  $ \mathbf{h}(t) $. The latter will proceed to the next time step  $ (t+1) $ as an input vector  $ \mathbf{h}(t) $ to work with the input vector  $ \mathbf{x}(t+1) $. Both will go through the same steps illustrated above involving the forget gate to select memory, the input gate to update memory, and the output gate to select output.

##### 10.4.2.3 Gated Recurrent Unit (GRU)

This section presents the concept of the GRU, which is a simplified version of the LSTM memory cell. Burkov [63, p. 74] emphasizes that GRU is the most effective RNN used in practice. In Workshop 10.3, Section 10.8, we show that GRU performs more accurately than other deep RNNs in predicting time-dependent MI during grade transition in an industrial HDPE process.

Cho et al. [119] in their 2014 paper introducing the encoder–decoder network that we will discuss in Section 10.4.4.1, actually presented the concept of GRU for the first time.

Referring to Figure 10.29, we see the input vector  $ \mathbf{x}(t) $ at time  $ t $ (labeled vector 1 in the figure) and the output vector from the previous time step,  $ \mathbf{h}(t-1) $ (labeled vector 2) both enter a filtering unit, called the reset gate, with a sigmoid activation function, giving an output vector  $ \mathbf{r}(t) $ (labeled vector 3). Following Eq. (10.62), we represent  $ \mathbf{r}(t) $ as [74, p. 520]:

 $$ \mathbf{r}(t)=\sigma\left[\mathbf{W}_{x r}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{h r}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{r}\right] $$ 

where $\sigma$ is the sigmoid activation function with an output vector with scalar components bounded between 0 and 1 (see Figure 10.24). The reset gate decides if the output vector from the previous time step, $\mathbf{h}(t-1)$, will be ignored. Specifically, when the reset gate is close to 0, $\mathbf{r}(t)$ depends primarily on $\mathbf{x}(t)$ only [114]. The reader can interpret the relevant weight factor matrices and the bias term in Eq. (10.67) and subsequent Eqs. (10.56)–(10.69) in the same way as those in Eqs. (10.62)–(10.64).

---

<!-- PDF page 688 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_151_709_666.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 10.29 A GRU memory cell. Source: Adapted from Geron [74].</div>


The same input vector  $ \mathbf{x}(t) $ at time  $ t $ and the output vector from the previous time step,  $ \mathbf{h}(t-1) $ also enter another filtering unit, called the update gate, with a sigmoid activation function, giving an output vector  $ \mathbf{z}(t) $ (labeled vector 4). Following Eq. (10.67), we represent  $ \mathbf{z}(t) $ as [74, p. 520]:

 $$ \mathbf{z}(t)=\sigma\left[\mathbf{W}_{xz}^{\mathrm{T}}\mathbf{x}(t)+\mathbf{W}_{hz}^{\mathrm{T}}\mathbf{h}(t-1)+\mathbf{b}_{z}\right] $$ 

The update gate controls how much information from the output vector from the previous time step,  $ \mathbf{h}(t-1) $, will carry over the output vector from the current time step, producing an updated output vector  $ \mathbf{h}(t) $. This acts similarly to the memory cell in the LSTM network, and helps the RNN to remember long-term information.

In Figure 10.28, the activation unit has two inputs: the first is the input vector  $ \mathbf{c}(t) $ (labeled vector 1), and the second one is vector 5, which results from the element-wise multiplication of the output vector from the reset gate  $ \mathbf{r}(t) $ (labeled vector 3) and the output vector from the previous time step,  $ \mathbf{h}(t-1) $, that is,  $ \mathbf{r}(t)\otimes\mathbf{h}(t-1) $. Vectors 1 and 5 enter the activation unit with a hyperbolic tangent activation function with an output vector with scalar components bounded between -1 and 1 (see Figure 10.24). Following Eq. (10.67), we represent the output vector from this activation unit as  $ \mathbf{g}(t) $ (labeled as vector 8) [74, p. 520]:

 $$ \mathbf{g}(t)=\tanh\left[\left(\mathbf{x}(t)+\mathbf{W}_{hg}^{\mathrm{T}}[\mathbf{r}(t)\otimes\mathbf{h}(t-1)]+\mathbf{b}_{g}\right)\right] $$ 

---

<!-- PDF page 689 -->

Referring to Figure 10.28, we look at the element-wise multiplication between  $ \mathbf{g}(t) $ (labeled as vector 8) and vector 6, which results from applying the operator “1-” to vector 4, that is, the output vector from the update gate,  $ \mathbf{z}(t) $. The latter simply means  $ [1 - \mathbf{z}(t)] $. Therefore, we represent vector 9 resulting from this element-wise multiplication as vector  $ [1 - \mathbf{z}(t)]\otimes\mathbf{g}(t) $.

Next, we represent the element-wise multiplication of vector 4, that is, output vector  $ \mathbf{z}(t) $ exiting the update gate, with the output vector from the previous time step,  $ \mathbf{h}(t-1) $, labeled vector 2, as  $ \mathbf{z}(t)\otimes\mathbf{h}(t-1) $. The results are in vector 7 in the figure.

Finally, the element-wise addition of vector 7 and vector 9 gives vector 10, representing the output vector from the GRU at time t,  $ \mathbf{y}(t) $, which is also sent to the next GRU cell to work with the input vector from the next time step,  $ \mathbf{x}(t+1) $, as inputs to the following GRU memory cell. In the figure, we represent the same vector as  $ \mathbf{h}(t) $, also labeled as vector 10. We represent  $ \mathbf{y}(t) $ or  $ \mathbf{h}(t) $ as:

 $$ \mathbf{y}(t)=\mathbf{h}(t)=\mathbf{z}(t)\otimes\mathbf{h}(t-1)+[1-\mathbf{z}(t)]\otimes\mathbf{g}(t) $$ 

which is similar to Eq. (10.66) in the LSTM memory cell.

We pause to recommend that the reader takes time to study an instructive, step-by-step illustrated guide to LSTM and GRU by Phi [120]. LSTM and GRU are one of the main reasons behind the success of RNNs. They can handle much longer sequences, time-series data, or dynamic process data with approximately 100-time steps better than simple RNNs [74, p. 520].

##### 10.4.2.4 Bidirectional RNNs

Schuster and Paliwal [115] introduce the concept of bidirectional RNN. Figure 10.30 illustrates a bidirectional RNN. We see two hidden layers in the network, one forward layer and one backward layer. Each layer may consist of LSTMs or GRUs. The network essentially consists of two separate subnetworks, and they serve as separate “experts” for the specific problem on which the networks are trained. One way of merging the opinions of forward experts and backward is to assume the opinions

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_916_743_1223.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 10.30 An illustration of a bidirectional RNN.</div>


---

<!-- PDF page 690 -->

to be independent, which leads to arithmetic averaging for regression and geometric averaging (or arithmetic averaging in the log domain) for classification [115].

Zhang et al. [116] apply bidirectional LSTM and GRU RNNs to a problem in data-driven fault detection and diagnosis of the well-known Tennessee Eastman process [4, pp. 269–291; 117, 121]. They give the details of the application and demonstrate that bidirectional LSTM and GRU RNNs exhibit a dramatically improved performance over other methods for chemical process fault detection and diagnosis. With an additional backward RNN, bidirectional RNNs facilitate the detection of variable deviations over all time points, particularly when a fault has just happened. However, as with all data-based methods, the directional RNNs require adequate historical process data.

We refer the reader to the details of bidirectional RNNs [115] and many available online tutorials on the training of bidirectional RNNs. In Workshop 10.3, Section 10.7, we compare the performance of two types of deep RNNs (LSTM and GRU) in predicting time-dependent MI during grade transition in an industrial HDPE process.

#### 10.4.3 Convolutional Neural Networks (CNNs)

Since their development by LeCun et al. in 1990 [122], CNNs have become a key tool for identifying satellite images, processing medical images, forecasting time series, detecting data anomalies, and recognizing characters such as ZIP codes and digits. In chemical industries, we see growing applications of CNNs to polymer property predictions from chemical structure [123], classification of LC-MS spectral peaks [49], prediction of thermophysical properties of chemical components from their surface charge distributions (called sigma profiles) [28, 29], computer-aided molecular design and screening methodology for fragrance molecules [124], performance prediction of protein-exchange membrane fuel cells [125], image analytics for classifying industrial catalyst pallets [62], and identifying color changes in thermal food processing [126], among others.

In Section 10.9, we present Workshop 10.4 for polymer property prediction from molecular structure using CNNs [123].

We follow [1, pp. 760–764; 127, 128] to explain a few key concepts of CNNs. Our goal is to give sufficient background to enable the reader to understand the cited references for additional details of applications. First, we know that a camera scans photographs to encode the images into pixels. To represent an image, we cannot use a simple vector of input pixel values, as the adjacency of pixels that correlate with each other really matters. In particular, we must consider an important property of images, called local spatial invariance. Specifically, we can say roughly that anything that is detectable in one small region of the image (e.g. an eye) would look the same if it appeared in another small local region of the image. We can achieve this local spatial invariance by constraining weight factors connecting a local region to a unit in the hidden layer to be the same for each hidden unit. Therefore, a CNN contains spatially invariant, local connections, at least in the first few layers, and has patterns of weight factors that are replicated across units in each layer. Applying this local

---

<!-- PDF page 691 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_147_654_384.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 10.31 An illustration of a one-dimensional convolution operation with a kernel of size i = 3 and a stride s = 2.</div>


spatial invariance characteristic significantly reduces the number of parameters in a DNN with many units without losing too much in the quality of the model [63].

Figure 10.31, adopted from Ref. [1, p. 761], illustrates the concepts of kernel and stride that are important in characterizing a convolution layer. For simplicity, we limit this discussion to a one-dimensional convolution operation. The reader may refer to [74, pp. 446–460] for multi-dimensional examples. First, a kernel (also called a filter) is a pattern of weight factors that is replicated across multiple local regions. Convolution is the process of applying the kernel to the pixels of the image, or to spatially organized units in a subsequent layer.

We see in the figure that the kernel vector  $ \mathbf{k} = [+1 - -1 +1] $, and this vector is replicated three times. We say that this kernel is of size  $ i = 3 $. In this example, the pixel on which the kernel  $ \mathbf{k} = [+1 - -1 +1] $ is entered is separated by a distance of two pixels; we say that the kernel is applied with a stride of  $ s = 2 $. We can understand this more easily by using a single matrix operation as follows:

 $$ \begin{pmatrix}{{{+1}}}&{{{-1}}}&{{{+1}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{+1}}}&{{{-1}}}&{{{+1}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{+1}}}&{{{-1}}}&{{{+1}}}\end{pmatrix}\begin{pmatrix}{{{8}}} \\{{{7}}} \\{{{6}}} \\{{{5}}} \\{{{4}}} \\{{{3}}} \\{{{2}}}\end{pmatrix}=\begin{pmatrix}{{{7}}} \\{{{5}}} \\{{{3}}}\end{pmatrix} $$ 

In this matrix, the 3-element kernel  $ (i=3) $ appears in each row, shifting two positions to the right according to the stride  $ (s=2) $ relative to the previous row.

Figure 10.32 illustrates the concept of padding [1, p. 762]. In this example, we have a kernel size of i = 3, and a stride of s = 1. Padding inputs of zero are added to the left and right ends of the two hidden layers to keep the hidden layers the same size as the input.

We could also look at the concept of kernel and stride from the view of a receptive field originated in models of the visual cortex in neuroscience. Specifically, the receptive field of a neuron is the portion of the sensory inputs that can affect the activation of the neuron. In a convolutional network, the receptive field of a unit in the

---

<!-- PDF page 692 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_145_802_344.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.32 An illustration of padding inputs of zero on the left and right ends of hidden layers. In the plot, all slopped arrows have kernel value of +1.</div>


first hidden layer is just the size of the kernel, that is, i pixels. It is possible to connect a large input layer to a small layer by spacing out the receptive fields or kernels. We call the shift from one receptive field to the next the stride, such as s = 2 in the current example.

Figure 10.31 shows the output coming out of the ReLU, [7 5 3]. We call this a rectified feature map, which then feeds into a new layer, called the pooling layer. The goal of pooling is to reduce the computational load, the memory usage, and the number of parameters (thus limiting the risk of overfitting). Basically, a pooling layer in a convolutional network summarizes a set of adjacent units from the preceding layer by a single value. This layer works like a convolutional layer with the same kernel l and stride s, but there is no activation function to process the output from the layer. There are two types of pooling operations: (1) average pooling computes the average value of its l inputs. This is equivalent to a convolution with a uniform kernel vector,  $ \mathbf{k} = [1/l, 1/l, \ldots, 1/l] $. The effect of this operation is to coarsen the resolution of the image (i.e. “to downsample” or “to shrink”) by a factor of l. (2) Max-pooling computes the maximum value of its l inputs. For the outputs from the ReLU in Figure 10.31, we see that average pooling gives an output of  $ (7+5+3)/3 = 5 $; and max-pooling gives an output of  $ \text{Max}[7\ 5\ 3] = 7 $.

Following [118], we give another example of pooling and flattening in Figure 10.33.

Lastly, a fully connected layer (also called a dense layer) forms when the flattened matrix from a pooling layer is fed as an input, which classifies and identifies the image.

Applying all the concepts that we have explained thus far, we show in Figure 10.34 a block diagram of the CNN that Abranches et al. [28] used in their work on predicting physiochemical properties from sigma profiles [29] that we discussed previously in Section 10.1.2.2.

We refer the reader to Section 10.9, Workshop 10.4, and the prediction of polymer property based on molecular structure using CNN, together with the transformer network introduced in Section 10.4.4.

#### 10.4.4 Attention is All You Need: Transformer Model

In a 2017 groundbreaking paper, entitled “Attention Is All You Need,” Ashish Vaswani et al. [129] proposed the transformer architecture, which is a neural

---

<!-- PDF page 693 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_152_603_497.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">Figure 10.33 An example of max-pooling and average-pooling, and flattening.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_134_571_746_701.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 10.34 A block diagram of the CNN for predicting physiochemical properties from sigma profiles.</div>


network that learns context and thus meaning by tracking relationships to sequential data like the words in a sentence (similar to time-dependent process variable values in a dynamic chemical process). A transformer model applies an evolving set of mathematical techniques, called attention mechanisms, to detect subtle ways that distant data elements in a series can influence and depend on each other [130].

According to Merritt [130], transformer models are in many cases replacing RNNs and CNNs, which were the most popular types of DNNs for sequence-to-sequence (“seq2seq”) learning just five years ago. Transformer models overcome a significant deficiency of the sequential nature of both RNNs and CNNs that prevents parallel processing. We recommend some online tutorial articles on transformer models [131–133]. Selected examples of the rapidly growing applications of the transformer models in CPIs include molecular optimization for new drug discovery [39, 134], computational chemistry [135], COSMO-SAC sigma profile modeling for high-throughput solvent screening [136], and dynamic soft sensor modeling for polypropylene MI prediction [137].

We introduce the transformer model by referring to an application to new drug discovery for a protein target reported by Grechishnikova [39]. Previously, most methods for protein-specific new drug generation required prior knowledge of protein binders, their physiochemical characteristics, or the three-dimensional structure of the protein. By adopting the transformer model, the proposed method

---

<!-- PDF page 694 -->

generates novel molecules with predicted ability to bind a target protein by relying on amino acid sequence only. Grechishnikova considers the target-specific new drug design as a “translational” problem between the amino acid “language” and the SMILES representation of the molecule [25]. In Section 10.1.2.2, we briefly introduced SMILES and its extensions [25–27] as an effective molecular representation as inputs to DNNs, and SMILES uses a string of characters to represent atoms, bonds, branches, cyclic structures, disconnected structures, and aromaticity with coding rules. In Section 10.9 Workshop 10.4, we apply the SMILES representation [25] to predict polymer properties using CNNs [123].

We follow [63, pp. 541–547; 74, pp. 541–562; 129–133] to introduce the basic concepts of the transformer model. Figure 10.35 shows the original architecture of the transformer model [129], and we discuss the key concepts below. In the figure, we see that both the left and right parts of the model use a stack of N (typically six; indicated by Nx in the figure) identical encoder layers and a stack of N identical decoder layers. As the input sequences to the encoder and decoder are processed separately and in parallel, the transformer model reduces the number of computations required in comparison to a model, which processes both sequences together.

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_619_592_1261.jpg" alt="Image" width="44%" /></div>


Figure 10.35 The architecture of the transformer model [129].

---

<!-- PDF page 695 -->

##### 10.4.4.1 Encoder-Decoder Stacks

We follow [63, pp. 87–92] to introduce the encoder–decoder architecture adopted by the transformer models. The left part of Figure 10.35 represents an encoder, and the right part is a decoder. Briefly, the encoder reads the input and generates some sort of state (similar to the state in recurrent current networks that we discussed in Figure 10.28) that can be seen as a numerical representation of the meaning of the input that the machine can work with. In ML, we refer to the meaning of some entity, whether it be an image, a text, or a video, as a vector or a matrix that contains real numbers. We call this vector or matrix the embedding of the input, as we see the term input embedding on the left part of Figure 10.35.

The decoder takes an embedded input from the encoder and generates a sequence of outputs. Because the transformer encoder has neither recurrence nor convolution, in order for the transformer model to make use of the order of the sequence, we must add some information about the positions into the input embeddings. This is done using positional encoding, as illustrated at the bottom of Figure 10.35. Let pos be the position of the word in a sequence,  $ d_{model} $ be the length of the encoding vector (same as the embedding vector; typically,  $ d_{model} = 512 $), and i be the index value into this vector, Vaswani et al. [129] proposed to use sine and cosine functions of different frequencies to characterize the positional embedding (PE):

 $$ \mathrm{PE}(\mathrm{pos},2i)=\sin\left(\mathrm{pos}/10,000^{2i/d_{\mathrm{model}}}\right) $$ 

 $$ \mathrm{PE}(\mathrm{pos},2i+1)=\cos\left(\mathrm{pos}/10,000^{2i/d_{\mathrm{model}}}\right) $$ 

Here, sine values correspond to all even indexes, and cosine values represent all odd indexes.

Conceptually, the decoder takes a start-of-sequence input feature vector  $ \mathbf{x}(0) $, produces the first output  $ \mathbf{y}(1) $, and updates its state by combining the embedded input  $ \mathbf{x}(0) $ with the output  $ \mathbf{y}(1) $ to produce its next input  $ \mathbf{x}(1) $, which is similar to the architecture illustrated previously with RNNs in Figure 10.24. The resulting vector or matrix embedding the output, as we see the term output embedding on the right part of Figure 10.35.

For the new drug discovery problem [39], the encoder maps a protein acid sequence  $ (x_1, x_2, \ldots, x_n) $ to a sequence of continuous representation  $ \mathbf{z} = (z_1, z_2, \ldots, z_n) $. Given  $ \mathbf{z} $, the decoder then generates an output sequence  $ (y_1, y_2, \ldots, y_m) $ one element at a time. In this case, the output sequence is a SMILES string [25].

Referring to the representation of a single encoder layer (as a part of a stack of 6 identical encoder layers) displayed in the left part of Figure 10.35, we see two sublayers, namely: (1) a multi-head attention mechanism; and (2) a fully connected feedforward network, both of which are explained shortly below. The transformer model uses a residual connection [37] around each of the two sublayers, meaning that the encoder provides the data with an alternative path to reach latter parts of the network by skipping a sublayer. Additionally, the encoder employs layer normalization [138]. Unlike BN discussed in Section 10.4.1.5, layer normalization directly estimates the normalization statistics from the summed inputs to the neurons within a hidden layer so the normalization does not introduce any new dependencies between training cases.

---

<!-- PDF page 696 -->

Turning now to the right part of Figure 10.35, we see that within a single decoder layer (as a part of a stack of six identical decoder layers), the decoder has actually a “masked” multi-head attention that receives the output from the encoder stack, in addition to a multi-head attention that receives inputs from both the encoder and the decoder and a feedforward network. The decoder stack also applies residual connections around each of the sublayers, followed by layer normalization. We have previously explained the concept of peddling in Figure 10.32. Here, masking within the decoder layer through the “masked” multi-head attention attempts to zero attention output where there is paddling in the input sequences to ensure that paddling does not contribute to the self-attention. We discuss the attention mechanisms below.

##### 10.4.4.2 Self-Attention and Attention Mechanisms Within the Encoder-Decoder Stacks

As we see in the bottom of both left and right parts of Figure 10.35, transformer models use positional encoding to tag data elements coming in and out of the network. Attention units follow these tags, calculating a kind of algebraic map of how each element relates to each other. Attention queries are typically executed in parallel by calculating a matrix of equations in what is called multi-headed attention, a term we see within Figure 10.35 [130]. This is actually a self-attention mechanism.

What is self-attention, and how does it find meaning? Self-attention, sometimes called intra-attention, is an attention mechanism that relates different portions of a single sentence in order to compute a representation of the sequence [129]. Consider, for example, the sentence: “David pours water from the pitcher into the cup until it is full.” We know “it” refers to the cup. Being able to identify “it” as the cup is an example of the self-attention mechanism in action [130]. As we described above, the encoder reads the input and generates some sort of state that can be seen as a numerical representation of the meaning of the input that the machine can work with. This meaning represents a relationship between things.

The attention layer takes its input in the form of three parameters, known as Query  $ (Q) $, Key  $ (K) $, and Value  $ (V) $. In the original formulation of the transformer model involving sequential data like the words in a sentence, we can interpret the Query parameter as the word for which we are quantifying the attention, and interpret the Key and Value parameters as the words to which we are paying attention, that is, how relevant is that word to the Query word [131]. For sequential data, we typically represent Q, K, and V values in a sequential order as rows or columns of a matrix.

In the transformer model, the attention module repeats its computations multiple times in parallel. Each of these computation paths is called an attention head. The attention module splits its parameters in multiple ways and passes each split independently through a separate head. All of these similar calculations are then combined through appropriate probability-based weighting factors to produce an attention score, which we call multi-head attention [131].

---

<!-- PDF page 697 -->

##### 10.4.4.3 Softmax Function and Probability-Based Weighting Factors

The Softmax function is a function that turns a vector of J real values into a vector of J real values that sum to 1. The input values can be positive, zero, negative, or greater than one, and the Softmax function transforms them into values between 0 and 1. Specifically, the Softmax function is:

 $$ \sigma(\mathbf{z})_{i}=\frac{\mathrm{e}^{z_{i}}}{\sum_{j=1}^{J}\mathrm{e}^{z_{i}}} $$ 

Where do we apply the Softmax function to the transformer model? Let us look at the three steps of an attention-based learning system applying to a sequential data like translating an English sentence into Spanish.

(1) If we are processing an input sequence of words, we first feed the input sequence into an encoder, which will output a vector of every element in the sequence.

(2) A list of these vectors, together with the decoder’s previous hidden states, will be exploited by the attention mechanism to dynamically highlight which of the input information will be used to generate the output.

(3) At each time step, the attention mechanism takes the previous hidden state of the decoder and the list of encoded vectors and uses them to generate unnormalized score values that indicate how well the elements of the input sequence align with the current output. As the generated score values should make relative sense in terms of their importance, we normalize the scores by passing them through a Softmax function to generate weights, which will have values between 0 and 1, and the values also add up to 1. We can interpret the resulting weights as probabilities. Finally, the encoded vectors are scaled by the computed weights to generate a vector, called a context vector, which is then fed to the decoder to generate a translated output.

##### 10.4.4.4 Attention Mechanisms in Encoder-Decoder Stacks

Within Figure 10.35, we see three attention mechanisms in action. These are [131]:

(1) Self-attention in the encoder, called multi-head attention: the input sequence to the encoder pays attention to itself.

(2) Self-attention in the decoder, called masked multi-head attention: the input sequence to the decoder pays attention to itself.

(3) Encoder-decoder attention in the decoder, called multi-head attention: the target sequence pays attention to the input sequences from the encoder and from the decoder.

Vaswani et al. [129] proposed the multi-head attention mechanism on the left part of Figure 10.36, which includes the scaled dot-product attention mechanism that is displayed in more detail on the right part of Figure 10.36.

We recommend the reader to pause temporarily and go through parts 3 and 4 of Doshi [131] that use simple graphical demonstration of the vector–matrix operations

---

<!-- PDF page 698 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_150_620_492.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Figure 10.36 Multi-head attention and scaled dot-product attention. Source: Vaswani et al. [129]/arXiv/CC BY 4.0.</div>


to open up the black boxes involved in the two attention mechanisms of Figure 10.36 and in the brief description of the two attention mechanisms in Vaswani et al. [129].

According to Vaswani et al. [129], the input to the scaled dot-product attention mechanism consists of query and key vectors of dimension  $ d_k $, and the value vector of dimension  $ d_v $. The mechanism computes the dot products of queries with all keys, scales the dot products down by dividing each by  $ \sqrt{d_k} $, and then applies a softmax function to obtain the weights on the values. Here, dividing each dot product by  $ \sqrt{d_k} $ is to allow for more stable computations, as multiplying large values can have exploding effects.

In practice, the attention mechanism computes the attention score on a set of queries simultaneously, packed together into a matrix Q. The keys and values are also packed together into matrices K and V. We then calculate the attention score matrix by the following Softmax function of the matrix operation:

 $$  Attention(\mathbf{Q},\mathbf{K},\mathbf{V})=softmax\left(\frac{QK^{\mathrm{T}}}{\sqrt{d_{k}}}\right)*V $$ 

The reader may refer to Doshi [131] for an explicit graphical vector–matrix demonstration of this calculation.

Referring to the left part of Figure 10.36, Vaswani et al. [129] proposed the following steps for the multi-head attention mechanism. Instead of performing a single attention function with a single-dimension vector of query, key, and value, the attention mechanism linearly projects the queries, keys, and values  $ h $ (e.g. 8) times with different, learned linear projections to  $ d_k $,  $ d_k $, and  $ d_v $ dimensions, respectively (e.g.  $ d_k = d_v = d_{\text{model}} / h = 512 / 8 = 64 $). On each of these projected versions of queries, keys, and values, the attention mechanism then computes the attention function in parallel, resulting in  $ d_v $-dimensional values. These values are then concatenated and

---

<!-- PDF page 699 -->

once again linearly projected, resulting in the final values, as shown on the left part of Figure 10.36.

For multi-head attention mechanism produces h different representations of Q, K, and V values and computes an attention function for each representation:

 $$  Head_{i}=Attention\left(QW_{i}^{Q},KW_{i}^{K},VW_{i}^{V}\right)\quad i=1-h $$ 

The outputs are concatenated and projected one more time, giving the final values:

 $$  Multi-Head\left(Q,K,V\right)=\left(head_{1},head_{2},\ldots,head_{h}\right)^{*}W^{0} $$ 

where the dimensions of matrices are:  $ W_i^Q $ and  $ W_i^K $ are both  $ d_{\text{model}} \times d_k $;  $ W_i^V $ is  $ d_{\text{model}} \times d_v $;  $ W^0 $ is  $ hd_v \times d_{\text{model}} $ [39].

Again, we refer the reader to Doshi [131] for detailed graphical demonstration of all the calculation steps involved.

##### 10.4.4.5 Position-Wise Feedforward Networks

We see in both left and right parts of Figure 10.35, each of the layers in the encoder and decoder contains a fully connected feedforward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation function in between. Following Table 10.6 and Figure 10.24, we write the ReLU activation function as  $ f(x) = 0 $,  $ x < 0 $,  $ f(x) = x $,  $ x \geq 0 $, or  $ f(x) = \max(0, x) $. We can then represent the output from the feedforward network as:

 $$ \mathrm{FNN}(x)=\max(0,x\mathbf{W}_{1}+\mathbf{b}_{1})\mathbf{W}_{2}+\mathbf{b}_{2} $$ 

 $ W_{1} $ is the vector of weights of the first feedforward network of all the neurons and  $ b_{1} $ is its bias vector. The output from the first feedforward network then goes through a ReLU transform, and hence the max function. The transformed feature is again multiplied by the weight vector  $ W_{2} $ of the second layer and its bias vector  $ b_{2} $ to give the output.

### 10.5 General Guidelines for Choosing Appropriate ML Algorithms

#### 10.5.1 Factors to Consider in Selecting Appropriate ML Algorithms

We summarize the key points in [139–142], among many other online resources, the key factors to consider in choosing appropriate ML algorithms.

1. Interpretability: Interpretability is the ability to determine the cause and effect from a ML model. If a model can take the inputs, and routinely get the same outputs, the model is interpretable. If understanding the reason behind the model results is a requirement for our problem, we need to choose an interpretable method (e.g. a linear regression model), instead of a black-box model (e.g. a DNN).

---

<!-- PDF page 700 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_150_804_532.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.37 An empirical plot of accuracy versus interpretability of ML models: “o” – unsupervised learning; “$\Delta$” – supervised learning; “$\square$” – both.</div>


2. Accuracy: For regression or prediction problems, review the performance evaluation metrics, such as mean squared error (MSE), RMSE, and coefficient of determination ( $ R^{2} $), defined in Section 10.2.1.2. Understand the bias-variance tradeoff illustrated in Figure 10.2. For classification problems, review the performance metrics, such as precision, recall, and F1 score, defined in Section 10.2.2.5.

Figure 10.37, adopted from [168], gives an empirical plot of accuracy versus interpretability of ML algorithms. Highly accurate ML models typically have nonlinear or non-smooth relationships and require long training time, while highly interpretable ML models typically involve linear, smooth, and well-defined relationships and are easy to train. Decision trees are unique ML models that can have both good accuracy and high interpretability. We also note that for tabular data, some ensemble methods (e.g. XGBoost) could give comparable accuracy than DNNs.

3. Training Time: This is the time taken by a ML algorithm to learn and create a model. It depends on whether we wish to update the resulting model continuously, as in the case of stock price prediction.

Enhanced learning methods, such as ensemble methods and DNNs, typically take a much longer training time, while achieving the best accuracy. By contrast, linear regression and its variants have faster training time, but lower accuracy. Figure 10.38 gives an empirical plot of training time versus accuracy of ML models.

Table 10.8 summarizes additional key considerations, including:

4. Dataset: Size, type of features, number of features and examples, linearity characteristics, preprocessing (mean-centering and scaling of features);

---

<!-- PDF page 701 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_145_748_536.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 10.38 An empirical plot of training time versus accuracy of ML models.</div>


5. Parameters;

6. Constraints;

7. Accuracy versus interpretability;

8. Training time versus accuracy.

#### 10.5.2 A Summary of Selected Machine Algorithms

To help the readers choose appropriate ML algorithms, we adopt the summary of ML algorithms by DataCamp [168] in Tables 10.9–10.11 to summarize the linear regression, tree-based, and clustering algorithms according to the algorithm name, description, advantages, and disadvantages. We also compare DNNs, including the MLP, RNNs, CNN, and transformer networks in Table 10.12.

#### 10.5.3 Decision Chart for Selecting Appropriate ML Algorithms

The reader can Google the topic “Machine learning algorithm selection cheat sheets-images,” and can find several dozen, step-by-step, query-and-answer-type decision charts for choosing appropriate ML algorithms. Most of those charts agree on the basic guidelines for algorithm selection but differ on the specific recommendations for certain applications. Three popular algorithm selection “cheat sheets” are:

(1) Microsoft Azure: https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet

(2) Scikit-learn: https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

---

<!-- PDF page 702 -->

<div style="text-align: center;">Table 10.8 Factors to consider in choosing appropriate ML algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Factors</td><td style='text-align: center; word-wrap: break-word;'>Characteristics</td><td style='text-align: center; word-wrap: break-word;'>Suggested Algorithms</td></tr><tr><td rowspan="4">Problem input type</td><td style='text-align: center; word-wrap: break-word;'>1. Input data-labeled</td><td style='text-align: center; word-wrap: break-word;'>Supervised learning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Input data-unlabeled</td><td style='text-align: center; word-wrap: break-word;'>Unsupervised learning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Input data-both labeled and unlabeled</td><td style='text-align: center; word-wrap: break-word;'>Semi-supervised learning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. To optimize an objective function by interacting with the environment</td><td style='text-align: center; word-wrap: break-word;'>Reinforcement learning</td></tr><tr><td rowspan="4">Problem output type</td><td style='text-align: center; word-wrap: break-word;'>1. Numerical versus categorical</td><td style='text-align: center; word-wrap: break-word;'>Regression/prediction versus classification</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. A set of input groups</td><td style='text-align: center; word-wrap: break-word;'>Clustering</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. Outlier or anomaly</td><td style='text-align: center; word-wrap: break-word;'>Outlier or anomaly detection</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. Reduced dimension of features</td><td style='text-align: center; word-wrap: break-word;'>Dimensionality reduction</td></tr><tr><td rowspan="2">Dataset: size</td><td style='text-align: center; word-wrap: break-word;'>1. Small</td><td style='text-align: center; word-wrap: break-word;'>Favor high bias/low variance model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Large</td><td style='text-align: center; word-wrap: break-word;'>Favor low bias/high variance model</td></tr><tr><td rowspan="2">Dataset: type of features</td><td style='text-align: center; word-wrap: break-word;'>1. Numerical</td><td style='text-align: center; word-wrap: break-word;'>Regression models</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Categorical</td><td style='text-align: center; word-wrap: break-word;'>Classification models</td></tr><tr><td rowspan="2">Dataset: number of features and examples</td><td style='text-align: center; word-wrap: break-word;'>1. Small/modest</td><td style='text-align: center; word-wrap: break-word;'>Support vector machines</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Large</td><td style='text-align: center; word-wrap: break-word;'>Neural networks; ensemble methods</td></tr><tr><td rowspan="2">Dataset: linearity characteristic</td><td style='text-align: center; word-wrap: break-word;'>1. Linear</td><td style='text-align: center; word-wrap: break-word;'>Linear regression, logistic regression, SVM</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Nonlinear</td><td style='text-align: center; word-wrap: break-word;'>Ensembled models; Deep neural networks</td></tr><tr><td rowspan="4">Dataset: preprocessing (Mean-centering and scaling of features) Parameters</td><td style='text-align: center; word-wrap: break-word;'>1. Prefer preprocessing</td><td style='text-align: center; word-wrap: break-word;'>Most models</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Preprocessing not required</td><td style='text-align: center; word-wrap: break-word;'>Decision trees</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. With parameters (a) Set before training (b) Optimized during training</td><td style='text-align: center; word-wrap: break-word;'>Parametric models (a) Hyperparameters (b) Parameters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Without parameters</td><td style='text-align: center; word-wrap: break-word;'>Nonparametric models (e.g. decision trees)</td></tr><tr><td rowspan="2">Constraints</td><td style='text-align: center; word-wrap: break-word;'>1. Must update model continuously (e.g. Stock prediction)</td><td style='text-align: center; word-wrap: break-word;'>Fast training time required</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. Accuracy is more important than training time (e.g. detecting cancer cells)</td><td style='text-align: center; word-wrap: break-word;'>Accurate model required</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Accuracy versus interpretability</td><td style='text-align: center; word-wrap: break-word;'>See Figure 10.37</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Training time versus accuracy</td><td style='text-align: center; word-wrap: break-word;'>See Figure 10.38</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<!-- PDF page 703 -->

<div style="text-align: center;">Table 10.9 A summary of selected linear regression algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Algorithm</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Disadvantages</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Linear regression (Section 10.2.1.1)</td><td style='text-align: center; word-wrap: break-word;'>A simple algorithm that models a linear relationship between inputs and a continuous numerical output variable</td><td style='text-align: center; word-wrap: break-word;'>Explainable method; Interpretable results by its output coefficient; Fast to train</td><td style='text-align: center; word-wrap: break-word;'>Assumes linearity between inputs and output; Sensitive to outliers; Can underfit with small, high-dimensional data</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Logistic regression (Section 10.2.1.3)</td><td style='text-align: center; word-wrap: break-word;'>A simple algorithm that models a linear relationship between inputs and a categorical output (1 or 0)</td><td style='text-align: center; word-wrap: break-word;'>Interpretable and explainable; Less prone to overfitting with regularization; Applicable for multi-class predictions</td><td style='text-align: center; word-wrap: break-word;'>Assumes linearity between inputs and outputs; Can overfit with small, high-dimensional data</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ridge regression (Section 10.2.1.4)</td><td style='text-align: center; word-wrap: break-word;'>A regression method that penalizes features that have low predictive outcomes by shrinking their coefficients closer to zero. Can be used for classification or regression</td><td style='text-align: center; word-wrap: break-word;'>Explainable and interpretable; Less prone to overfitting; Best suited where data suffer from collinearity</td><td style='text-align: center; word-wrap: break-word;'>All the predictors are kept in the final model; Doesn&#x27;t perform feature selection</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lasso regression (Section 10.2.1.4)</td><td style='text-align: center; word-wrap: break-word;'>Same as Ridge regression</td><td style='text-align: center; word-wrap: break-word;'>Less prone to overfitting; Can handle high-dimensional data; No need for feature selection</td><td style='text-align: center; word-wrap: break-word;'>Can lead to poor interpretability as it can keep highly correlated variables</td></tr></table>

Source: Adapted from Rane [90].

(3) SAS - The Power to Know: https://blogs.sas.com/content/subconsciousmusings/2020/12/09/machine-learning-algorithm-use or https://www.reddit.com/r/learnmachinelearning/comments/r5l17z/brief_overview_which_machine_learning_algorithm

(4) Accel.AI: https://www.accel.ai/anthology/2022/1/24/machine-learning-algorithms-cheat-sheet

Figure 10.39 shows a decision chart adopted from (4) Accel.AI.

---

<!-- PDF page 704 -->

<div style="text-align: center;">Table 10.10 A summary of selected tree-based algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Algorithm</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Disadvantages</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Decision tree</td><td style='text-align: center; word-wrap: break-word;'>Decision Tree models make decision rules on the features to produce predictions. Can be used for classification or regression</td><td style='text-align: center; word-wrap: break-word;'>Explainable and interpretable; Can handle missing values</td><td style='text-align: center; word-wrap: break-word;'>Prone to overfitting; Sensitives to outliers</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Random forest</td><td style='text-align: center; word-wrap: break-word;'>An ensemble learning method that combines the output of multiple decision trees</td><td style='text-align: center; word-wrap: break-word;'>Reduces overfitting; Higher accuracy compared to other models</td><td style='text-align: center; word-wrap: break-word;'>Training complexity can be high; Not very interpretable</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Gradient boosting regression</td><td style='text-align: center; word-wrap: break-word;'>Gradient boosting regression employs boosting to make predictive models from an ensemble of weak predictive learners</td><td style='text-align: center; word-wrap: break-word;'>Better accuracy compared to other regression models; It can handle multicollinearity; It can handle nonlinear relationships</td><td style='text-align: center; word-wrap: break-word;'>Sensitive to outliers and can therefore cause overfitting; Computationally expensive and has high complexity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Extreme gradient boosting (XGBoost)</td><td style='text-align: center; word-wrap: break-word;'>Gradient boosting algorithm that is efficient and flexible. Can be used for both classification and regression tasks</td><td style='text-align: center; word-wrap: break-word;'>Provides accurate results; Captures nonlinear relationships</td><td style='text-align: center; word-wrap: break-word;'>Hyperparameter tuning can be complex; Does not perform well on sparse datasets</td></tr></table>

Source: Adapted from Rane [90].

#### 10.6 Workshop 10.1: Prediction of HDPE Melt Index Using Random Forest and eXtreme Gradient Boosting (XGBoost) Ensemble Learning Models

#### 10.6.1 Objective and HDPE Process

The objective of this workshop is to demonstrate the development and application of a predictive model for the HDPE MI using a random forest ensemble learning model.

We consider a slurry HDPE process at the LG Petrochemicals in South Korea [69] that we illustrated previously in Figure 1.44 with two reactors in parallel. We also showed the simulation flowsheet for one of the two reactors in the process in Figure 9.42.

---

<!-- PDF page 705 -->

<div style="text-align: center;">Table 10.11 A summary of selected clustering algorithms.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Algorithm</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Disadvantages</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>K-means clustering</td><td style='text-align: center; word-wrap: break-word;'>K-Means is the most widely used clustering approach. It determines K clusters based on Euclidean distances</td><td style='text-align: center; word-wrap: break-word;'>Scales to large datasets; Simple to implement and interpret; Results in tight clusters</td><td style='text-align: center; word-wrap: break-word;'>Requires the expected number of clusters from the beginning; Has trouble with varying cluster sizes and densities</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hierarchical clustering</td><td style='text-align: center; word-wrap: break-word;'>A “bottom-up” approach where each data point is treated as its own cluster - and then the closest two clusters are merged together iteratively</td><td style='text-align: center; word-wrap: break-word;'>There is no need to specify the number of clusters; The resulting dendrogram is informative</td><td style='text-align: center; word-wrap: break-word;'>Doesn’t always result in the best clustering; Not suitable for large datasets due to high complexity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Density-based spatial clustering of applications with noise (DBSCAN)</td><td style='text-align: center; word-wrap: break-word;'>A method to identify cluster based on the density of region in the data</td><td style='text-align: center; word-wrap: break-word;'>Identify cluster of arbitrary shapes; No need for initial number of clusters; Can identify outliers</td><td style='text-align: center; word-wrap: break-word;'>Challenging to specify hyperparameters - the radius of the cluster around each data point and the limiting number of clusters</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Gaussian mixture model</td><td style='text-align: center; word-wrap: break-word;'>A probabilistic model for modeling normally distributed clusters within a dataset</td><td style='text-align: center; word-wrap: break-word;'>Computes a probability for an observation belonging to a cluster; Can identify overlapping clusters and outliers; More accurate results compared to K-means</td><td style='text-align: center; word-wrap: break-word;'>Requires complex tuning; Requires setting the number of expected mixture components or clusters</td></tr></table>

#### 10.6.2 Data Collection and Visualization

Park et al. [34] correlate the MI data with nine independent variables listed in Table 10.13. We are grateful to Prof. Y.K. Yeo, a co-author of [34] for providing us the original data for this workshop. The dataset consists of 5000 observations and 14 main independent variables (X) and one dependent variable (Y), which is the polymer MI. The complete data appear in an Excel file, HDPE_LG_Plant_Data.csv, within Workshop 10.1. We choose only eight independent variables listed in Table 10.13 for the current workshop. Figure 10.39 illustrates the process data varying with time (in minute).

We load the CSV data and convert it into data frames using Pandas library in Python. We then use the Pandas DataFrame to define the independent features/variables (X) and dependent variables (y). Note that Pandas DataFrame is

---

<!-- PDF page 706 -->

<div style="text-align: center;">Table 10.12 A summary of selected deep neural networks.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Deep neural network type</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Input data</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Disadvantages</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Multilayer perceptron (MLP)</td><td style='text-align: center; word-wrap: break-word;'>Section 10.4.1.1</td><td style='text-align: center; word-wrap: break-word;'>Tabular data</td><td style='text-align: center; word-wrap: break-word;'>Capable of learning any nonlinear function</td><td style='text-align: center; word-wrap: break-word;'>(1) While solving an image classification problem using a MLP, one must convert a 2D image into a 1D vector before model loses the spatial features of an image. (2) Vanishing and exploding gradients (Section 10.4.1.4)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Recurrent neural Networks (RNNs): LSTM (long short-term memory) RNN, gated recurrent unit (GRU), bi-directional RNN</td><td style='text-align: center; word-wrap: break-word;'>Section 10.4.2 Has a recurrent connection to the hidden state. This looping constraint ensures that sequential information is captured in the input data</td><td style='text-align: center; word-wrap: break-word;'>Sequence data (text, audio, time series) (Not for tabular data, and image data)</td><td style='text-align: center; word-wrap: break-word;'>(1) Captures the sequential information present in the input data; (2) Can share the parameters across different time steps (called “parameter sharing”), resulting in fewer parameters to train and decreasing the computational cost</td><td style='text-align: center; word-wrap: break-word;'>(1) Not efficient in handling long sequences. Tends to forget the contents of the distant position, and mixes the contents of adjacent positions (2) Vanishing and exploding gradients</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Convolutional neural network (CNN)</td><td style='text-align: center; word-wrap: break-word;'>Section 10.4.3 Consists of filters (i.e. kernels) to extract relevant features from the input data using the convolution operation</td><td style='text-align: center; word-wrap: break-word;'>Image data</td><td style='text-align: center; word-wrap: break-word;'>(1) Able to capture the spatial features from an image, helping to identify the location of an object, as well as its relation with other objects in an image (2) Implementing parameter sharing with a single filter applied across different parts of an input to produce a feature map</td><td style='text-align: center; word-wrap: break-word;'>Vanishing and exploding gradients</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transformer network</td><td style='text-align: center; word-wrap: break-word;'>Section 10.4.4 Transformers perceive the entire input sequences simultaneously. It employs the attention mechanism.</td><td style='text-align: center; word-wrap: break-word;'>Allows processing multiple modalities (e.g. images, videos, text, and audio) Using similar processing blocks</td><td style='text-align: center; word-wrap: break-word;'>(1) Able to process entire sequences in parallel, increasing the speed and capacity of sequential deep learning models (2) “Attention mechanisms” tracks the relations between words across very long text sequences in both forward and reverse directions</td><td style='text-align: center; word-wrap: break-word;'>Take time to understand the encoder-decoder stacks</td></tr></table>

---

<!-- PDF page 707 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_153_783_686.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 10.39 An example of a ML algorithm selection decision chart.</div>


Figure 10.40 Defining independent variables (features) and dependent variables.

import pandas as pd
df = pd.read_excel('HDPE_LG_Plant_Data.xlsx')
df.head()

#Features
X = df.iloc[:, 1:10]
X.head()

#Dependent Variable
y = df.iloc[:, 10]
y.head()

two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Figure 10.40 shows the code.

We can also visualize and plot the data using Matplotlib library in Python. See the code in Figure 10.41.

---

<!-- PDF page 708 -->

<div style="text-align: center;">Table 10.13 Process variables for Workshop 10.1.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process variable</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2</td><td style='text-align: center; word-wrap: break-word;'>Monomer ethylene feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>Chain-transfer agent, hydrogen feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>Catalyst feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>Hexane solvent feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3</td><td style='text-align: center; word-wrap: break-word;'>Comonomer propylene feed flow rate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T</td><td style='text-align: center; word-wrap: break-word;'>Temperature of the reactor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P</td><td style='text-align: center; word-wrap: break-word;'>Pressure in the reactor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2/C2</td><td style='text-align: center; word-wrap: break-word;'>Feed concentration ratio in the reactor of monomer ethylene to hydrogen</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3/C4</td><td style='text-align: center; word-wrap: break-word;'>Feed concentration ratio of propylene to 1-butylene monomer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI (dependent or quality variable)</td><td style='text-align: center; word-wrap: break-word;'>Melt index of polymer</td></tr></table>

#Data Visualization
p = df.iloc[:, 1:11]
p.head()
plt.style.use('fivethirtyeight')
p.plot(subplots=True,
                layout=(6, 3),
                figsize=(22,22),
                fontsize=10,
                linewidth=2,
                sharex=False,
                title='Visualization of the HDPE plant data')
plt.show()

<div style="text-align: center;">Figure 10.41 Visualization of process data displayed in Figure 10.39.</div>


#### 10.6.3 Data Cleaning and Preprocessing

In order to handle any missing data, we can remove any of the observations with missing data using some of the functions of Pandas library like: df.dropna().

##### 10.6.3.1 Feature Selection

We can remove any highly correlated variables to make the models more efficient and capture the right causality in the data. We can first calculate the correlation matrix and plot them. We can use the Seaborn library for plotting the correlation mapping. Seaborn is a data visualization library built on top of Matplotlib and closely

---

<!-- PDF page 709 -->

<div style="text-align: center;">Figure 10.42 Finding the correlations of the dataset and plotting a correlation map.</div>


#Feature Selection
corr = X.corr()
import seaborn as sns
sns.heatmap(corr)

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_325_627_656.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">Figure 10.43 Correlation mapping of features (independent variables).</div>


integrated with Pandas data structures in Python. See Figure 10.42 for the code, and Figure 10.43 for the correlation mapping between all variables.

On the right of Figure 10.43, we see the correlation coefficient between two features (independent variables) going from -0.50 to 1.00. The figure shows that H2 is highly correlated with C2, having a correlation coefficient close to +1. We can also confirm this by removing those features for which the correlation value is greater than 0.95. See the code in Figure 10.44.

#Dropping Highly correlated variables
correlation_matrix = X.corr().abs()
correlated_features = set()

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.95:
            colname = correlation_matrix.columns[i]
            correlated_features.add(colname)

print(correlated_features)

Figure 10.44 Removing those features (independent variables) for which the correlation coefficient is greater than 0.95.

---

<!-- PDF page 710 -->

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler().fit(X_train)
X_train_std = sc_x.transform(X_train)
X_test_std = sc_x.transform(X_test)

y_train = y_train.values.reshape(-1,1)
y_test = y_test.values.reshape(-1,1)
sc_y = StandardScaler().fit(y_train)
y_train_std = sc_y.transform(y_train)
y_test_std = sc_y.transform(y_test)

n_train = np.count_nonzero(y_train)
y_train_std = y_train_std.reshape(n_train, )

Figure 10.45 Using the standard-scaler library to standardize the dataset to a zero mean and a unit variance.

In a larger dataset, we can drop highly correlated features to improve prediction accuracy; in the current workshop, we retain all features (independent variables).

##### 10.6.3.2 Defining Training and Evaluation Datasets

We divide the dataset using the Scikit-learn (“sklearn” for short) test train split library in Python. The default test split in the library is 0.25, which means that Python uses 75% of the dataset for training and cross-validation and uses the remaining 25% dataset for testing and evaluation. You may search the Internet for tutorials about train_test_split:

x_train, x_test, y_train, y_test = train_test_split(x, y)

##### 10.6.3.3 Standardization

We then standardize each of the training and test dataset using the sklearn standard-scaler library so that the features and outputs are in the same range and the prediction and model correlations are more accurate. The features are standardized by removing the mean and scaling to unit variance (see Appendix A, Section A.1.7). See Figure 10.45 for the code.

#### 10.6.4 Build Machine Learning Model

We use the standardized training data to train the ML model. In this case, we consider an ensemble learning random forest model for prediction. We use the sklearn random forest regressor library for model training. We can use cross-validation to find the training RMSE. We keep the default hyperparameters (see Table B.1, Appendix B). See Figure 10.46 for the Python code.

The training gives R2 = 0.99 and RMSE = 0.09734. The standard deviation of quality variable, y, is 5.

---

<!-- PDF page 711 -->

#Model training
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100)

rf.fit(X_train_std, y_train_std)

cv = cross_val_score(rf, X_train_std, y_train_std, cv = 10, scoring='neg_mean_squared_error')
cv_score = cv.mean()

rmse_train = np.sqrt(abs(cv_score))
print(rmse_train)

y_rf_train_std = rf.predict(X_train_std)
y_rf_train_std = y_rf_train_std.reshape(-1,1)
y_rf_train = sc_y_inverse_transform(y_rf_train_std)
rmse_train = np.sqrt(mean_squared_error(y_train, y_rf_train))
print(rmse_train)

<div style="text-align: center;">Figure 10.46 The Python code for ensemble learning random forest regressor.</div>


In this case, the default hyperparameter already performs well, but we will still showcase hyperparameter tuning below. We can also use cross-validation accuracy to prevent overfitting by finding the optimum hyperparameters that give the highest accuracy on the validation set.

The random forest model is a tree-based model and has many hyperparameters listed below (see also Table B.1, Appendix B).

• n_estimators = number of trees in the forest

• max_features = max number of features considered for splitting a node

• max_depth = max number of levels in each decision tree

• min_samples_split = min number of data points placed in a node before the node is split

• min_samples_leaf = min number of data points allowed in a leaf node

• bootstrap = method for sampling data points (with or without replacement)

We use grid search with fivefold cross-validation sklearn library to obtain the best hyperparameters. Fivefold cross-validation involves randomly dividing the dataset into five groups (folds) of approximately equal size. The first group is treated as a test set, and the remaining four groups are used to fit the model. We vary one of the hyperparameters, n_estimators, which represents the number of trees in the forest, to find the optimum hyperparameter using the cross-validation accuracy as the metric. Figure 10.47 shows the Python code.

#### 10.6.5 Analysis of ML Model Results

Figure 10.48 shows the code to evaluate the model results. The RMSE of the test dataset with standard deviation is 0.16 and R2 of 0.99, which is a very good prediction for data, which has standard deviation of 5.

The random forest ML model also decides the relative importance of different operating variables in reducing the mean decrease in “node Impurity” (called MDI),

---

<!-- PDF page 712 -->

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Create the parameter grid based on the results of random search
param_grid = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100, 110],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 200, 300, 1000]
}
# Create a Random Forest model
rf = RandomForestRegressor()
# Instantiate the grid search model

grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, cv = 3, n_jobs = -1, verbose = 2)

# Find optimum hyperparameters
best_grid = grid_search.best_estimator_

Y_train_best = best_grid.predict(X_train)
rmse_train = np.sqrt(mean_squared_error(y_test, Y_best))
print(rmse_train)

<div style="text-align: center;">Figure 10.47 Using grid search to find optimum hyperparameters.</div>


#Evaluate the results
Y_test_best = best_grid.predict(X_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_best))
print(rmse_test)

<div style="text-align: center;">Figure 10.48 The Python code to evaluate the model result.</div>


which is a measure of how much each independent (i.e. feature) reduces the variance in the model. Figure 10.49 shows the Python code for finding and plotting the mean decrease in impurity (MDI). Figure 10.50 shows the resulting MDI plot, showing the most important independent variables (features) for prediction of MI using a random forest regressor model. It indicates that the hydrogen feed flow rate (independent variable or feature) has the most significant impact on the resulting MI (quality variable) value.

We can finally plot the final prediction of MI with time and compare the prediction with plant data. Figure 10.51 shows the Python code for making the plot, and Figure 10.52 shows the resulting comparison plot. The figure validates the accurate prediction of random forest regressor.

---

<!-- PDF page 713 -->

import time
import numpy as np

start_time = time.time()
importances = rf.feature_importances_
std = np.std([
    tree.feature_importances_for tree in rf.estimators_], axis=0
    elapsed_time = time.time() - start_time
    print(f"Elapsed time to compute the importances: "
                     f.."elapsed_time:.3f} seconds")

feature_names = [f'feature {i}' for i in range(X.shape[1])]

import pandas as pd
forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()

<div style="text-align: center;">Figure 10.49 The Python code for model evaluation and finding the mean decrease in node impurity (MDI).</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Feature</th><th style='text-align: center;'>Mean decrease in impurity</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>C2</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>H2</td><td style='text-align: center;'>0.92</td></tr>
    <tr><td style='text-align: center;'>CAT</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>HX</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>C3</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>T</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>P</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>C3/C4</td><td style='text-align: center;'>0.01</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.50 Feature (independent variable) importance plot resulting from the random forest regressor.</div>


---

<!-- PDF page 714 -->

t = df.iloc[:,0]
import matplotlib.pyplot as plt
plt.style.use('default')
plt.scatter(t,y.iloc[:,1],c='green',label='Actual')
plt.plot(t,y_p[:,1],c='red',label='ML Predicted MI')
plt.xlabel('time')
plt.ylabel('Melt Index')

plt.legend()
plt.show()

<div style="text-align: center;">Figure 10.51 The Python code for comparing the model prediction with plant data for melt index.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>ML predicted MI</th><th style='text-align: center;'>Actual MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>19.5</td><td style='text-align: center;'>19.5</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>19.8</td><td style='text-align: center;'>19.8</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>7.8</td><td style='text-align: center;'>7.8</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>6.5</td><td style='text-align: center;'>6.5</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>5.2</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>4.8</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>4.8</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>4.8</td><td style='text-align: center;'>4.8</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.0</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.52 Comparison of predicted melt index with plant data resulting from the random forest model.</div>


#### 10.6.6 Melt Index Prediction Using XGBoost

We use the same dataset to predict the MI using XGBoost, follow the same procedure for data preprocessing and feature engineering as in random forest, and use the XGBoost ML model for training and prediction.

XGBoost is also a tree-based gradient boosting model, and it has three types of hyperparameters:

• General parameters relate to which booster we are using to do boosting, commonly tree or linear model

• Booster parameters depend on which booster you have chosen

---

<!-- PDF page 715 -->

#Model Training
import xgboost as xgb
xgr = xgb.XGBRFRegressor()
xgr.fit(X_train_std, y_train_std)

#Model Prediction
y_xgr_std = xgr.predict(X_test_std)
y_xgr_std = y_xgr_std.reshape(-1, 1)
y_xgr = sc_y.inverse_transform(y_xgr_std)
y_xgr = xgr.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_xgr))
print(rmse)

Figure 10.53 Python code to implement XGBoost applied to melt index prediction.

• Learning task parameters decide on the learning scenario. For example, regression tasks may use different parameters than ranking tasks.

For this model, we just use the default hyperparameters (see Figure 10.53).

The RMSE prediction for the stand-alone XGBoost model is around 0.25, which is slightly less than the random forest prediction for this dataset.

Similar to random forest, XGBoost can also give feature importance, which also predicts  $ H_{2} $ as the most important feature. See the Python coding in Figure 10.54 and the resulting feature importance plot in Figure 10.55.

This concludes the current workshop.

<div style="text-align: center;">Figure 10.54 The Python code to prepare the feature importance plot.</div>


xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Features</th><th style='text-align: center;'>F score</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>H2</td><td style='text-align: center;'>242</td></tr>
    <tr><td style='text-align: center;'>C2</td><td style='text-align: center;'>101</td></tr>
    <tr><td style='text-align: center;'>P</td><td style='text-align: center;'>94</td></tr>
    <tr><td style='text-align: center;'>C3/C4</td><td style='text-align: center;'>73</td></tr>
    <tr><td style='text-align: center;'>C3</td><td style='text-align: center;'>38</td></tr>
    <tr><td style='text-align: center;'>CAT</td><td style='text-align: center;'>34</td></tr>
    <tr><td style='text-align: center;'>HX</td><td style='text-align: center;'>22</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.55 The feature importance plot from XGBoost.</div>


---

<!-- PDF page 716 -->

#### 10.7 Workshop 10.2: Prediction of HDPE Melt Index Using Deep Neural Networks

#### 10.7.1 Objective

The objective of this workshop is to demonstrate the development and application of a predictive model for the HDPE MI using DNNs.

We consider the same slurry HDPE process at the LG Petrochemicals in South Korea [34] that we illustrated previously in Figure 1.44 with two reactors in parallel. We also showed in Figure 9.42 the simulation flowsheet for one of the two reactors in the process. We demonstrate below how to solve Workshop 10.1 of Section 10.6 using a DNN with the Google TensorFlow framework and Keras deep learning library.

#### 10.7.2 Deep Neural Network Configuration

Our DNN is similar to that illustrated in Figure 10.56, which has an input layer with 9 nodes, three hidden layers with 64 nodes each, and an output layer with a single node.

We note that the HDPE process flowsheet appears in Figure 9.42; the data file, HDPE_LG_Plant_Data.csv, is available in the file for Workshop 10.1; and Table 10.13 gives the list of nine independent variables (features) for the single quality variable, the MI. We use the same data preprocessing step described in Section 10.6.3. Specifically, we normalize the dataset using both the inputs X and y. Figure 10.57 shows the Python code for data normalization.

We use the ReLU activation function of Table 10.6 and Figure 10.24 for the hidden layers and use a linear activation function for the output layer. We use a dense layer type, meaning that each neuron in the dense layer receives inputs from all

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_878_808_1211.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.56 An illustration of a deep neural network.</div>


---

<!-- PDF page 717 -->

Figure 10.57 Python code for data normalization.
#Data Normalization

sc_x = StandardScaler().fit(X_train)
X_train_std = sc_x.transform(X_train)
X_test_std = sc_x.transform(X_test)

y_train = y_train.values.reshape(-1,1)
y_test = y_test.values.reshape(-1,1)
sc_y = StandardScaler().fit(y_train)
y_train_std = sc_y.transform(y_train)
y_test_std = sc_y.transform(y_test)

model = Sequential()
model.add(Dense(64, input_dim=9, kernel_initializer='normal', activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))
model.add(Dropout(0.25))
model.add(Dense(1, activation='linear'))
model.summary()

<div style="text-align: center;">Figure 10.58 The code to implement a deep neural network in Keras.</div>


the neurons of its previous layer. Figure 10.58 shows the Python code to define the DNN using Keras. We also use dropout (Section 10.4.1.6) to avoid overfitting with probability of 0.25.

#### 10.7.3 Prediction of Neural Network Configuration

We use the Adam optimization of Section 10.4.1.7 to train the neural network. As this is a regression problem, we choose the MSE, Eq. (10.6), as the loss function to quantify the error between model prediction and data. We then fit the DNN to the training data and check the history output for the results. Figure 10.59 shows the Python code to implement this model calculation.

#Compiling Model and Prediction
model.compile(loss='mse', optimizer='adam', metrics='mse', 'mae'])
history=model.fit(X_train_std, y_train_std, epochs=50, batch_size=150, verbose=1, validation_split=0.2)

#Loss history curve
print(history.history.keys())
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.label('loss')
plt.xlabel('epoch')
plt.legend['train', 'validation'], loc='upper left')
plt.show()

<div style="text-align: center;">Figure 10.59 The code for compiling model prediction and loss curve.</div>


---

<!-- PDF page 718 -->

#Model prediction on test data

y_pred_test_std = model.predict(X_test_std)
y_pred_test = sc_y.inverse_transform(y_pred_test_std)
r2_score(y_test, y_pred_test)

<div style="text-align: center;">Figure 10.60 The code to compare model prediction with test data.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Epoch</th><th style='text-align: center;'>Train</th><th style='text-align: center;'>Validation</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.045</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.005</td><td style='text-align: center;'>0.005</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.002</td><td style='text-align: center;'>0.002</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.001</td><td style='text-align: center;'>0.001</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.61 Loss function curve of deep neural network for melt index prediction.</div>


Figure 10.60 shows the Python code to compare the model prediction with test data that were not used in developing the prediction model.

We use inverse transform to scale the predictions to the original scale and then evaluate the predictions. The resulting RMSE, Eq. (10.7), of the MI prediction is 0.42 for a dataset with standard deviation of 0.5.

Figure 10.61 illustrates the value of loss function (that is, MSE) for training and validation versus the number of iterations (epochs).

In Workshop 10.1, Section 10.6, we demonstrate the use of random forest ensemble learning to improve the accuracy and minimize the RMSE of MI prediction. For the present workshop, we can lower the RMSE from a value of 0.42 for our DNN to a value of 0.16 using random forest ensemble (Section 10.6.5). By applying the ensemble learning methods, the reader would find that they can generally lower the RMSE of ML models, as reported in prior studies [30, 36, 40, 41].

---

<!-- PDF page 719 -->

#### 10.8 Workshop 10.3: Prediction of Time-Dependent HDPE Melt Index Using Dynamic Deep Recurrent Neural Networks

#### 10.8.1 Objective

Our objective is to build two different types of deep RNN structures to predict the MI for a dynamic process: (1) LSTM; and (2) GRU (see Sections 10.4.2.2 and 10.4.2.3).

We use the same HDPE dataset used in the previous workshops. The idea here is that we train the data on the model for past time periods and make predictions for a future time (see Sections 10.4.2.2 and 10.4.2.3).

#### 10.8.2 Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN)

We use the following steps as a step-by-step workflow to build the network architectures. We use the same preprocessing steps as in previous workshops to standardize and normalize the dataset. The only thing different is the way that we define our training, validation, and test sets. We use the observations for the first 1500 min for training, the next 500 min for validation, and the next 500 min for testing. The training and validation steps are defined below. Since this is a continuous process dataset with no seasonality, we do not need any extra data preparation steps. The input to a LSTM model for TensorFlow needs to be reshaped into a 3D format – [samples, timesteps, features]. For the training dataset, the number of samples are 1500, the features are 9, while the timestep is 1 equal to each observation. Figure 10.62 shows the Python code for the data preprocessing.

sc_x = StandardScaler().fit(X)
X = sc_x.transform(X)
y = y.values.reshape(-1,1)
sc_y = StandardScaler().fit(y)
y = sc_y.transform(y)

# Defining Test, Train and Validation dataset
X_train = X[:1500]
y_train = y[:1500]
X_val = X[1500:1800]
y_val = y[1500:1800]
X_test = X[1800:2400]
y_test = X[1800:2400]

# Reshape into 3D for LSTM input
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_val = X_val.reshape((X_val.shape[0], 1, X_val.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

Figure 10.62 Data preprocessing and splitting the data into training, validation, and test sets for time series prediction by the LSTM/GRU models.

---

<!-- PDF page 720 -->

#LSTM Model
model = Sequential()
model.add(LSTM(units = 64, return_sequences = True, input_shape = (1, 9)))
model.add(Dropout(0.25))
model.add(LSTM(units = 32, return_sequences = True))
model.add(Dropout(0.25))
model.add(Dense(1))

### Figure 10.63 LSTM model code

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_383_803_683.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.64 Code for prediction using the LSTM model.</div>


We use a LSTM model with two stacked layers of 64 units and 32 units each and dense layer with 1 unit for output. We also add dropout to check for overfitting. Figure 10.63 shows the Python code for the LSTM model.

We use the Adam optimizer, and follow by using an inverse transform to reshape and make predictions for the test dataset. Figure 10.64 shows the Python code for the prediction using the LSTM model.

The LSTM test predictions are plotted and then compared with actual plant data and with actual predictions of the MI, as shown in Figure 10.65. The RMSE for the predictions is 1.2.

#### 10.8.3 Gated Recurrent Unit (GRU)

We repeat the same process using a GRU model in TensorFlow with a similar configuration of 64 and 32 units as shown in Figures 10.66 and 10.67.

Figure 10.68 compares the GRU model prediction with plan data. The GRU model has a RMSE of 0.9 for MI prediction, which is better than LSTM predictions as expected. This result confirms the statement by Burkov [63, p. 74] that GRU is the most effective RNN used in practice.

---

<!-- PDF page 721 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>LSTM prediction</th><th style='text-align: center;'>Actual</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.4</td></tr>
    <tr><td style='text-align: center;'>1850</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>4.6</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>1950</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>4.6</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>4.7</td></tr>
    <tr><td style='text-align: center;'>2050</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>5.8</td><td style='text-align: center;'>4.6</td></tr>
    <tr><td style='text-align: center;'>2150</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>4.4</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>2350</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>0.1</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.65 Comparison of LSTM model prediction with plant data.</div>


#GRU Model
model = Sequential()
model.add(GRU(units = 64, return_sequences = True, input_shape = (1, 9)))
model.add(Dropout(0.25))
model.add(GRU(units = 32, return_sequences = True))
model.add(Dropout(0.25))
model.add(Dense(1))

<div style="text-align: center;">Figure 10.66 The Python code for specifying the GRU model.</div>


import matplotlib.pyplot as plt

plt.plot(test_results['Test Predictions'][1800:2400], c = 'green', label = 'LSTM prediction')
plt.plot(test_results['Actuals'][1800:2400], c = 'red', label = 'Actual')

plt.xlabel('Time')

plt.ylabel('Melt Index')

plt.legend()

<div style="text-align: center;">Figure 10.67 The Python code to plot the GRU predictions compared to the actual data.</div>


#### 10.9 Workshop 10.4: Polymer Property Prediction Based on Molecular Structure Using Convolutional Neural Network

#### 10.9.1 Objective

The objective of this workshop is to demonstrate how to predict polymer properties, particularly glass transition temperature, based on its molecular structure using a

---

<!-- PDF page 722 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>GRU prediction</th><th style='text-align: center;'>Actual</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1800</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>1850</td><td style='text-align: center;'>5.8</td><td style='text-align: center;'>4.7</td></tr>
    <tr><td style='text-align: center;'>1900</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>4.6</td></tr>
    <tr><td style='text-align: center;'>1950</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>4.7</td></tr>
    <tr><td style='text-align: center;'>2000</td><td style='text-align: center;'>5.8</td><td style='text-align: center;'>4.6</td></tr>
    <tr><td style='text-align: center;'>2050</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>4.4</td></tr>
    <tr><td style='text-align: center;'>2100</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>2150</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>4.3</td></tr>
    <tr><td style='text-align: center;'>2200</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.0</td></tr>
    <tr><td style='text-align: center;'>2250</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>2300</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>2350</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>2400</td><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.1</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.68 A comparison of GRU model prediction and plant data.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_356_576_598_761.jpg" alt="Image" width="25%" /></div>


from DECIMER import predict_SMILES
image_path = "/content/drive/MyDrive/PolyData/DECIMER_test_0.png"
SMILES = predict_SMILES(image_path)
print(SMILES)

Downloading trained model to /root/.data/DECIMER-V2
/root/.data/DECIMER-V2/models.zip
... done downloading trained model!
C1=CC=C(C=C1)CC2=C(C3=CC=CC=C302)C4=CC=C(C=C4)OS=(0)=(0)(F)(F)

<div style="text-align: center;">Figure 10.69 The Python code to convert images to SMILES structure using DECIMER methodology.</div>


combination of a transformer network (Section 10.4.3) and CNN (Section 10.4.2.6). We note that A CNN or RNN (Section 10.4.2) model is rarely used alone. These networks are often used as layers in a larger model that also has one or multilayer perceptrons, thus forming a hybrid type of DNN. In this workshop, we illustrate an integration of a transformer network and a CNN.

---

<!-- PDF page 723 -->

#### 10.9.2 Transformer Network for Deep Learning for Chemical Image Recognition (DECIMER) to Convert a Molecular Structure Image to SMILES Representation

We can convert the molecular structure of a compound into an encoded form of linear strings known as Simplified Molecular Input Line Entry System (SMILES) [25], which can then be used for analysis and prediction of molecular properties based on its structure. In Section 10.1.2.1, we briefly introduced SMILES and its extensions [25–27] as an effective molecular representation as inputs to DNNs, and SMILES uses a string of characters to represent atoms, bonds, branches, cyclic structures, disconnected structures, and aromaticity with coding rules.

Rajan et al. [143] showcase a Deep Learning for Chemical Image Recognition (DECIMER) methodology for prediction of SMILES notation from structural images. DECIMER uses a standard transformer network of Figure 10.35 that converts the bitmap of chemical structure depiction into a computer-readable format. They use a CNN model to parse the images into extracted features, which are fed into a transformer network. They use four encoder-decoder stacks and eight parallel attention heads.

Here, we use the Python library of DECIMER developed by Rajan et al. [143] and show how to convert a structural image to SMILES notation. We convert the molecular structural image to SMILES using the code in Figure 10.70.

According to [144], the Python code for DECIMER and the trained models are available at https://github.com/Kohulan/DECIMER-TPU, https://doi.org/10.5281/zenodo.4730515. The data are available as SMILES at: https://doi.org/10.5281/zenodo.4766251.

Thus, using this transformer network, we can generate a database for polymer SMILES-encoded structures.

#### 10.9.3 Convolutional Neural Network for Predicting Polymer Property Using SMILES Representation

Next, we showcase here the methodology proposed by Miccio and Schwartz [123] to employ chemical structures to predict polymer properties using CNNs. The authors use the SMILES representation of the molecule [25]. The datasets are provided in the supplement material of the article (see: https://doi.org/10.1016/j.polymer.2020.122341). These datasets include 218 polymers, their SMILES representation code, and the corresponding glass transition temperatures in K.

In Python, one-hot encoding refers to the representation of categorical variables as binary vectors. These categorical values are first mapped to integer values. Each integer value is then represented as a binary vector that is all 0s (except the index of the integer, which is marked as 1). Using one-hot encoding, we can convert the SMILES strings into binary numerical data with matrices with zero and one. We then convert these matrices into binary images, which can then be used for analysis and prediction using CNN. Figure 10.70 illustrates the methodology of converting the SMILES code to an encoded binary image.

---

<!-- PDF page 724 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_152_735_357.jpg" alt="Image" width="59%" /></div>


Figure 10.70 The methodology for converting SMILES encoding into a binary image.

#One Hot encoding of SMILES data
d=[]
n=[['c'], ['n'], ['o'], ['c'], ['N'], ['F'], ['='], ['O'],
                  ['(', [''), ['1'], ['2'], ['#'], ['cl'], ['/'], ['S'], ['Bn']]
e = OneHotEncoder(handle_unknown='ignore')
e.fit(n)
e.categories_
df1=df["SMILES Structure"].apply(lambda x: pd.Series(list(x)))
for i in range(df1.shape[0]):
    x.e.transform(pd.DataFrame(df1.iloc[i,:]).dropna(how="all").values).tararray()
    y=np.zeros(((df1.shape[1]-x.shape[0]),len(n)))
    d.append(np.vstack((x,y)))

# Converting encoded SMILES to binary images
plt.figure(figsize=(20,100))
for i in range(len(d)):
    plt.subplot(len(d),s,i+1)
    plt.imshow(d[i])

#Dataset
X = np.array(d)
Y=df["Tg"].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=0)

<div style="text-align: center;">Figure 10.71 Converting the SMILES code to binary images.</div>


We first load the dataset using the Pandas library in Python. Figure 10.72 shows a snapshot of dataset, which contains the SMILES structure of polymer and the corresponding glass transition temperature,  $ T_{g} $.

Then, we convert the SMILES dataset to numerical matrix representation using one hot encoding library, considering each element of the structure in a dictionary form. The “one-hot encoding” then converts it into matrix form with 0,1, which can also be converted into binary form. The data are converted into numpy input form and the corresponding  $ T_g $ as the predictions. We then split the dataset into training set and test set.

Figure 10.71 shows the Python code of these operations, and Figure 10.72 illustrates the resulting binary images.

Figure 10.73 illustrates a schematic of a CNN used in the original work by Miccio and Schwartz [123]. The reader may refer to our discussion of DNNs about ReLU

---

<!-- PDF page 725 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_147_781_325.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 10.72 The binary images of the dataset.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_132_397_771_645.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 10.73 A schematic of a convolutional neural network used in Miccio and Schwartz. Source: Miccio and Schwartz [123]/with permission of Elsevier.</div>


activation (Section 10.4.1.4), BN (Section 10.4.1.5), dropout (Section 10.4.1.6), Adam optimizer (Section 10.4.1.7), kernel size and stride (Figure 10.31), zero padding (Figure 10.32), max-pooling and flattening (Figure 10.33), dense or fully connected (FC) layer (Figure 10.34), and CNN block diagram (Figure 10.34).

We analyze the binary images using CNN. The CNN architecture we use has two convolution layers and two dense layers, and an output. The first convolution 2D layer has 128 filters with a kernel size  $ (3,3) $. The input numpy shape of the dataset is  $ (65,17,1) $, since this is a binary image data with one channel. The activation function ReLU is used in all layers. The layer is flowed by Max Pool Layers of size  $ (3,3) $, which reduces size of the inputs to speed computations. The layer is followed by BN, which makes the training process stable and faster. We add a similar convolution layer with 64 filters, followed by max pool and BN layers, and the input is then flattened through a flatten layer, which is followed by two dense layers of 128 and 64 neurons and the 1 output dense layer. We also use dropout tool to prevent overfitting. Figure 10.74 shows the Python code of this CNN implementation.

We then compile the model using Adam optimizer, train the model, and make predictions. See the Python code in Figure 10.75. The model accuracy for the predictions using structural image is around 82% for the given CNN configuration. The loss curve for the predictions showcases good accurate predictions, as shown in Figure 10.76.

Hence, with reasonably accurate predictions, we can use the polymer structure to predict its properties, like glass transition temperature using CNN.

---

<!-- PDF page 726 -->

model=Sequential()
model.add(Conv2D(128,(3,3), activation="relu",input_shape=(65,17,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64,(3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(128,activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(1))

<div style="text-align: center;">Figure 10.74 The Python code to implement a convolutional neural network.</div>


model.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae'])
history=model.fit(x_X_train, y_y_train, epochs=500, batch_size=16, validation_split=0.1)
y_pretrain=model.predict(x_train)
y_pretest=model.predict(x_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pretest.reshape(y_test.shape)))
print(rmse_test)

r2_score(y_test, y_pretest.reshape(y_test.shape))

<div style="text-align: center;">Figure 10.75 The Python code to do model optimization and prediction.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Epoch</th><th style='text-align: center;'>Train Loss</th><th style='text-align: center;'>Validation Loss</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>78000</td><td style='text-align: center;'>78000</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>4000</td><td style='text-align: center;'>4000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>2500</td><td style='text-align: center;'>2500</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>2000</td><td style='text-align: center;'>2000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>1800</td><td style='text-align: center;'>1800</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>1500</td><td style='text-align: center;'>1500</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>1200</td><td style='text-align: center;'>1200</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>1000</td><td style='text-align: center;'>1000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>500</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>450</td><td style='text-align: center;'>450</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>400</td><td style='text-align: center;'>400</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>350</td><td style='text-align: center;'>350</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>300</td><td style='text-align: center;'>300</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>250</td><td style='text-align: center;'>250</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.76 Loss curve for CNN training and validation.</div>


#### 10.10 Workshop 10.5: Melt Index Prediction Using Automated Machine Learning

The objective of this workshop is to demonstrate the use of an automated ML tool to guide the development of a predictive model for the same MI prediction problem

---

<!-- PDF page 727 -->

#Data loading in H2O
h2o.init()

df = h2o.import_file(path = '/content/drive/MyDrive/PolyData/HDPE_LG_Plant_Data.csv')
df.describe(chunk_summary=True)

train, test = df.split_frame(ratios=[0.8], seed = 1)

Figure 10.77 The Python code to import the dataset into H₂O DataFrame.

in Workshop 10.1. We consider the same process dataset as in Workshop 10.1 and perform the same data preprocessing steps.

AutoML is the process of automating the task of ML model development, including feature selection and model selection. It makes the model more scalable and efficient and is easier for people who have limited knowledge of ML. In this workshop, we use the  $ H_{2}O $ AutoML library in Python, which automates the ML workflow, and includes the automatic training and tuning of ML models [145, 146]. The model training can be stopped at user defined time.

We import the dataset into H₂O DataFrame using Python, divide it into test, and train data. A DataFrame is a two-dimensional, size-mutable, potentially heterogeneous tabular data. Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. The Python code appears in Figure 10.77.

We choose the number of models that are evaluated by  $ H_2O $. The current version of  $ H_2O $ AutoML trains and cross-validates the following algorithms: three pre-specified XGBoost GBM (Gradient Boosting Machine) models, a fixed grid of GLMs (Generalized Linear Models), a default random forest (DRF), five pre-specified  $ H_2O $ GBMs, a near-default deep neural net, an extremely randomized forest (XRT), a random grid of XGBoost GBMs, a random grid of  $ H_2O $ GBMs, and a random grid of deep neural nets. Interested readers may refer to the documentation for  $ H_2O.ai $ [87] for details of these algorithms. Figure 10.78 illustrates the Python codes to specify the maximum number of ML models to be tested as 25.

The AutoML object includes a “leaderboard (lb)” of models that were trained in the process, including the fivefold cross-validated model performance. Figure 10.79 shows the Python code to display the specific algorithms tested, and Figure 10.80 shows the results.

In Figure 10.80, RMSE represents room mean squared error; MSE is mean squared error; MAE is mean absolute error; and RMSLE is root mean squared log error. The figure shows the algorithms used and their RMSE on the test dataset. The results show that, as expected, the stacked ensemble model of all the mentioned models gave the most accurate prediction.

We can also use the  $ H_{2}O $ AutoML tool to help in interpreting the model. We apply the tool, SHAP (Shapley Additive Explanations), proposed by Lundberg and Lee [147]. Figure 10.81 shows a SHAP summary plot. In the plot, the y-axis represents the independent variable (feature), where the variables with the highest importance are placed at the top, and those with the lowest importance are placed at the bottom.

---

<!-- PDF page 728 -->

#Train AutoML
aml = H20AutoML(max_models = 25,
                           balance_classes=True,
                           seed = 1)

train.head()

aml.train(training_frame = train, y = 'MI_Plant')

preds = aml.predict(test)
preds = aml.leader.predict(test)

<div style="text-align: center;">Figure 10.78 The Python code to specify the maximum number of models to be tested.</div>


lb = h2o.automl.get_leaderboard(aml, extra_columns = "ALL")
lb

# Get the best model using the metric
m = aml.leader
# this is equivalent to
m = aml.get_best_model()

Figure 10.79 The Python code to display the specific ML algorithms tested in the model development.

model_id
StackedEnsemble_BestOfAmin_1_Autoc05522_183810 10 02357 0104726 0.0540600 0.020499 0.0104728 2064 0.1502546
StackedEnsemble_AtaMode05_1_AutocML_1_20220522_183810 0.104057 0.010828 0.0056452 0.023781 0.010828 4460 0.699585 StacedEnsemble
GBM_5_AutoML_1_20220522_183810 0.108673 0.0118034 0.0615105 0.0240461 0.0118034 764 0.047608 GBM
GBM_2_AutoML_1_20220522_183810 0.117815 0.0139896 0.0663530 0.0226625 0.0138996 1329 0.044356 GBM
XRT_1_AutoML_1_20220522_183810 0.115000 0.0147612 0.0611941 0.0223284 0.0141621 1973 0.03827 ORF
GBM_3_AutoML_1_20220522_183810 0.120175 0.0144416 0.0656911 0.0246946 0.0144416 1342 0.048857 GBM
XGBoost_grd_1_AutoML_1_20220522_183810_14 0.121767 0.0148272 0.0563090 0.0222907 0.0148272 604 0.008242 XGBoost
DRF_1_AutoML_1_20220522_183810_14 0.129760 0.0169836 0.0619152 0.0228055 0.0168396 3032 0.031713 ORF
GBM_4_AutoML_1_20220522_183810_14 0.131085 0.0171834 0.0672527 0.0246912 0.0171834 1447 0.055435 GBM
XGBoost_grd_1_AutoML_1_20220522_183810_model_4 0.135872 0.0168415 0.0654633 0.0257321 0.0184511 480 0.070541 XGBoost

<div style="text-align: center;">Figure 10.80 Display of results from AutoML.</div>


For each feature, we see the positive and negative SHAP values of the feature (independent variable). For example, for the H2/C2 flow rate ratio, the SHAP values are mostly positive between 1 and 9, indicating that H2/C2 has mainly a positive impact on the dependent variable, MI. Likewise, SHAP values for H2 flow rate are mostly positive between 2 and 4, indicating that H2 has mainly a positive impact on the MI.

There are some advantages of SHAP-based plotting over traditional importance plots [148]: (1) SHAP-based plots can highlight both the importance of the independent variables (features) and the positive and negative relationships of the independent variables with the dependent variable; (2) the SHAP-based plot includes every single observation as shown by each dot in the plot; and (3) SHAP-based plots work with sparse datasets. Traditional importance plots based on partial least square (PLS) only show the trend on a generalized basis and do not account for individual cases.

---

<!-- PDF page 729 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>H2</th><th style='text-align: center;'>0.0</th><th style='text-align: center;'>0.0</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 10.81 SHAP summary plot of the H₂O Auto ML predictions.</div>


Lastly, we mention that there are a growing number of automated ML algorithms to help the user identify the right ML tool to deal with feature selection, preprocessing, model development, hyperparameter tuning, etc. This is important as the number of available ML algorithms is getting huge and almost exhaustive. Interested readers may refer to our recent article  $ [148] $ applying an automated ML algorithm, called TPOT (tree-based pipeline optimization tool) to an industrial fermentation operation.

### 10.11 Limitations of Stand-Alone Data-Based Models

The predictive ML models often cannot identify the important features correctly; hence, they often cannot quantify the model sensitivities accurately. Based on the knowledge of polyolefin reaction kinetics, we know that MI is highly dependent on the hydrogen flow rate and a small change in hydrogen flow leads to a significant change in MI.

Table 10.14 compares the actual plant values of MI at different hydrogen flow rates for a first-principle-based model, a causal PLS model, and a data-based ML model. While the ML predictions for the base case (MI = 4.7 and 4.9) are close to the actual plant value of 5, the ML models do not predict MI values accurately at an increased hydrogen flow of 90 m³/hr. By increasing the hydrogen flow rate, we observe much less change in ML prediction compared to a first-principle-based model. We find that the first-principle-based model is better able to predict the change since it is built on accurate reaction kinetics.

---

<!-- PDF page 730 -->

<div style="text-align: center;">Table 10.14 Model comparison based on MI values at varying hydrogen flow.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Model</td><td style='text-align: center; word-wrap: break-word;'>MI ( $ H_{2} = 60 \, m^{3}/hr $)</td><td style='text-align: center; word-wrap: break-word;'>MI ( $ H_{2} = 90 \, m^{3}/hr $)</td><td style='text-align: center; word-wrap: break-word;'>MI ( $ H_{2} = 180 \, m^{3}/hr $)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Actual plant value</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>17.5</td><td style='text-align: center; word-wrap: break-word;'>—</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>First-principle-based model prediction</td><td style='text-align: center; word-wrap: break-word;'>5.3</td><td style='text-align: center; word-wrap: break-word;'>20.3</td><td style='text-align: center; word-wrap: break-word;'>56</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data-based model prediction by causal partial least square (PLS)</td><td style='text-align: center; word-wrap: break-word;'>4.7</td><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>33</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data-based model prediction by ensemble machine learning</td><td style='text-align: center; word-wrap: break-word;'>4.9</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>19</td></tr></table>

We also test the data beyond the operating range at a hydrogen flow of  $ H_{2} $ of  $ 180 \, m^{3}/hr $ for which actual plant data are not available. We find that the first-principle-based model and the causal model are more accurate in their extrapolative predictions outside the range of hydrogen flow rate in the original plant data, when compared to a predictive ML model.

In Chapter 11, we explore a hybrid SGML approach to modeling chemical processes by integrating first-principle-based models with a data-based ML models. We show that the integrated approach can significantly improve both the interpolative and extrapolative accuracies of the resulting model.

## References and Further Reading

1 Russell, S. and Norvig, P. (2021). Artificial Intelligence: A Modern Approach, 4e, 1115 pages. Hoboken, NJ: Pearson.

2 Turning, A.M. and Haugeland, J. (1950). Computing Machinery and Intelligence. Cambridge, MA: MIT Press.

3 Quantrille, T.E. and Liu, Y.A. (1991). Artificial Intelligence in Chemical Engineering. Atlanta, GA: Elsevier, Inc.

4 Baughman, D.R. and Liu, Y.A. (1995). Neural Networks in Bioprocessing and Chemical Engineering. Atlanta, GA: Elsevier, Inc.

5 Stephanopoulos, G. and Han, C. (ed.) (1996). Intelligent Systems in Process Engineering: Paradigms from Design and Operations. Atlanta, GA; Elsevier, Inc.

6 Venkatasubramanian, V. (2019). The promise of artificial intelligence in chemical engineering: is it here, finally? AIChE Journal 65: 466.

7 Qin, S.L. (2003). Statistical process monitoring: basics and beyond. Journal of Chemometrics 17: 480.

8 Qin, S.J. (2014). Process data analytics in the era of big data. AIChE Journal 60: 3092.

---

<!-- PDF page 731 -->

9 Chemical Engineering Progress (2016). Special Section on Big Data Analytics, March, 27–50.

10 Chiang, L.H., Lu, B., and Castillo, I. (2017). Big data analytics in chemical engineering. Annual Review of Chemical and Biomolecular Engineering 8: 63.

11 Ge, Z., Song, Z., Ding, S.X., and Huang, B. (2017). Data mining and analytics in the process industry: the role of machine learning. IEEE Access 5: 20590.

12 Goldsmith, B.R., Esterhuizen, J., Liu, J.X. et al. (2018). Machine learning for heterogeneous catalyst design and discovery. AIChE Journal 64: 2311.

13 Zendehboudi, S., Rezael, N., and Lohi, A. (2018). Applications of hybrid models in chemical, petroleum, and energy systems: a systematic review. Applied Energy 228: 2539.

14 Lamoureux, P.S., Winther, K.T., Torres, J.A.G. et al. (2019). Machine learning for computational heterogeneous catalysis. ChemCatChem 11: 3581.

15 Qin, S.J. and Chiang, L.H. (2019). Advances and opportunities in machine learning for process data analytics. Computers and Chemical Engineering 126: 465.

16 Mater, A.C. and Coote, M.L. (2019). Deep learning in chemistry. Journal of Chemical Information and Modeling 59: 245.

17 Dobbelaere, M.R., Plehiers, P.P., Van de Vijver, R., and Stevens, C.V. (2021). Machine learning in chemical engineering: strengths, weaknesses, opportunities and threats. Engineering 7: 2101.

18 Qin, S.J., Guo, S., Li, Z. et al. (2021). Integration of process knowledge and statistical learning for the Dow data challenge problem. Computers and Chemical Engineering 153: 10741.

19 Trinh, X., Maimaroglou, D., and Hoppe, S. (2021). Machine learning in chemical product engineering: the state of the art and a guide for newcomers. Processes 9: 1456.

20 Khaleghi, M.K., Savizi, I.S.P., Lewis, N.E., and Shojaosadati, S.A. (2021). Synergisms of machine learning and constraint-based modeling of metabolism for analysis and optimization of fermentation parameters. Biotechnology Journal 16: 2100212.

21 Mowbray, M., Savage, T., Wu, C. et al. (2021). Machine learning for biochemical engineering: a review. Biochemical Engineering Journal 172: 108054.

22 Sharma, N. and Liu, Y.A. (2022). A hybrid science-guided machine learning approach for modeling chemical processes: a review. AIChE Journal 68: e17609.

23 Chiang, L.H., Braun, B., Wang, Z., and Castillo, I. (2022). Towards artificial intelligence at scale in the chemical industry. AIChE Journal 68: e17644.

24 KouMLeh, S.M., Hassanpour, H., Esmaeili, M., and Gholmi, A. (2021). Various deep learning techniques for the applications in polymer, polymer composite chemistry, structures and processing. Journal of Chemistry Letters 2: 157.

25 Weininger, D. (1988). SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules. Journal of Chemical Information and Computer Sciences 28: 31.

26 Grethe, G., Blanke, G., and Kraut, H. (2018). International chemical identifier for reactions (RINChi). Journal of Cheminformatics 10: 22.

---

<!-- PDF page 732 -->

27 Goh, G.B., Hodas, N.O., Siegel, C., and Vishnu, A. (2017). SMILES2Vec: an interpretable general-purpose deep neural network for predicting chemical properties. https://doi.org/10.48550/arXiv.1712.02034.

28 Abranches, D.O., Zhang, Y., Maginn, E.J., and Colo'n, Y. J. (2022). Sigma profiles in deep learning: towards a universal molecular descriptor. Royal Society of Chemistry ChemComm 58: 5630.

29 Mullins, E., Oldland, R.J., Liu, Y.A. et al. (2006). Sigma-profile database and application guidelines for COSMO-based thermodynamic models. Industrial and Engineering Chemistry Research 45: 3973.

30 Agarwal, A., Liu, Y.A., and McDowell, C. (2019). 110th anniversary: ensemble-based machine learning for industrial fermenter classification and foaming control. Industrial and Engineering Chemistry Research 58: 16170.

31 Lee, D.E., Song, J.-H., Song, S.-O., and Yoon, E.S. (2005). Weighted support vector machine for quality estimation in the polymerization process. Industrial and Engineering Chemistry Research 44: 2101.

32 Han, I.S., Han, C., and Chung, C.B. (2005). Melt index modeling with support vector machines, partial least squares, and artificial neural networks. Journal of Applied Polymer Science 95: 967.

33 Shi, J. and Liu, X. (2006). Melt index prediction by weighted least squares support vector machines. Journal of Applied Polymer Science 101: 285.

34 Park, T.C., Kim, T.Y., and Yeo, Y.K. (2010). Prediction of the melt flow index using partial least squares and support vector regression in high-density polyethylene (HDPE) process. Korean Journal of Chemical Engineering 27: 1662.

35 Liu, Y. and Chen, J. (2013). Integrated soft sensor using just-in-time support vector regression and probabilistic analysis for quality prediction of multi-grade processes. Journal of Process Control 23: 793.

36 Liu, Y., Liang, Y., and Gao, Z. (2017). Industrial polyethylene melt index prediction using ensemble manifold learning-based local model. Journal of Applied Polymer Science https://doi.org/10.1002/APP.45094.

37 He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 770.

38 Maltarollo, C.C., Kroenberger, T., Espinoza, G.Z. et al. (2019). Advances with support vector machines for novel drug discovery. Expert Opinion on Drug Discovery 14: 23.

39 Grechushnikova, D. (2021). Transformer neural network for protein-specific de novo drug generation as a machine learning problem. Scientific Reports 11: 321.

40 Chang, Y.S., Abimannn, S., Chiao, H.-T. et al. (2020). An ensemble learning based hybrid model and framework for air pollution forecasting. Environmental Science and Pollution Research 27: 38155.

41 Hu, P., Jiao, Z., Zhang, Z., and Wang, Q. (2021). Development of solubility prediction models with ensemble learning. Industrial and Engineering Chemistry Research 60: 11627.

---

<!-- PDF page 733 -->

42 Lee, H., Kim, C., Lim, S., and Lee, J.M. (2020). Data-driven fault diagnosis for chemical processes using transfer entropy and graphical lasso. Computers and Chemical Engineering 142: 107064.

43 Thomas, M.C., Zhu, W., and Romagnoli, J.A. (2018). Data mining and clustering in chemical process databases for monitoring and knowledge discovery. Journal of Process Control 67: 160.

44 Monroy, I., Benitez, R., Escudero, G., and Graells, M. (2010). A semi-supervised approach to fault diagnosis for chemical processes. Computers and Chemical Engineering 34: 631.

45 Madhu PK, R., Subbaiah, J., and Krithivasan, K. (2021). RF-LSTM-based method for prediction and diagnosis of fouling in heat exchanger. Asia-Pacific Journal of Chemical Engineering 16: e2684.

46 Zhou, L., Chen, J., and Song, Z. (2015). Recursive Gaussian process regression model for adaptive quality monitoring in batch processes. Mathematical Problems in Engineering https://doi.org/10.1155/2015/761280.

47 Chiang, L.H., Kotanchek, M.E., and Kordon, A.K. (2004). Fault diagnosis based on Fisher discriminant analysis and support vector machines. Computers and Chemical Engineering 28: 1389.

48 Agarwal, P. and Budman, H. (2019). Classification of profit-based operating regions for the tennessee eastman process using deep learning methods. IFAC-PapersOnLine 52: 556.

49 Kantz, E.D., Tiwari, S., Watrous, J.D. et al. (2019). Deep neural networks for classification of LC-MS spectral peaks. Analytical Chemistry 91: 12407.

50 Hoskins, J. and Himmelblau, D. (1992). Process control via artificial neural networks and reinforcement learning. Computers and Chemical Engineering 16: 241.

51 Shin, J., Badgwell, T.A., Liu, K.H., and Lee, J.H. (2019). Reinforcement learning: overview of recent progress and implications for process control. Computers and Chemical Engineering. 127: 282.

52 Bao, Y., Zhu, Y., and Qian, F. (2021). A deep reinforcement learning approach to improve the learning performance in process control. Industrial and Engineering Chemistry Research 60: 5504.

53 Zhu, W., Castillo, I., Wang, Z. et al. (2021). Benchmark study of reinforcement learning in controlling and optimizing batch processes. Journal of Manufacturing Processes 4: e10113.

54 Singh, V. and Kodamana, H. (2020). Reinforcement learning based control of batch polymerisation processes. IFAC PapersOnLine 53: 667.

55 Yan, W., Shao, H., and Wang, X. (2003). Soft sensing modeling based on support vector machine and Bayesian model selection. Computers and Chemical Engineering 28: 1489.

56 Yao, L. and Ge, Z. (2018). Deep learning of semi-supervised process data with hierarchical extreme learning machine and soft sensor application. IEEE Transactions on Industrial Electronics 65: 1490.

57 Ke, W., Huang, D., Yang, F., and Jiang, Y. (2017). Soft sensor development and applications based on LSTM in deep neural networks. 2017 IEEE Symposium

---

<!-- PDF page 734 -->

Series on Computational Intelligence (SSCI). https://ieeexplore.ieee.org/abstract/document/8280954 (accessed 2 June 2022).

58 Xu, Y., Ma, J., Liaw, A. et al. (2017). Demystifying multitask deep neural networks for quantitative structure–activity relationships. Journal of Chemical Information and Modeling 57: 2490.

59 Wu, J., Wang, S., Zhou, L. et al. (2020). Deep-learning architecture in QSPR modeling for the prediction of energy conversion efficiency of solar cells. Industrial and Engineering Chemistry Research 59: 18991.

60 Goli, E., Vyas, S., Koric, S. et al. (2020). ChemNet: a deep neural network for advanced composites manufacturing. Journal of Physical Chemistry B 124: 9428.

61 Goh, E., Siegel, C.M., Vishnu, A. and Hodas, N.O., (2017). Chemnet: A transferable and generalizable deep neural network for small-molecule property prediction. Conference: Machine Learning for Molecules and Materials (NIPS 2017 Workshop), December 8, 2017, Long Beach, California.

62 Rendall, R., Xastillo, I., Lu, B. et al. (2018). Image-based manufacturing analytics: improving the accuracy of an industrial pellet classification system using deep neural networks. Chemometrics and Intelligent Laboratory Systems 180: 26.

63 Burkov, A. (2019). The Hundred-Page Machine Learning Book. Andriy Burkov Publishers. (The author states that this book is distributed on the “read first, buy later” principle. It means that you can freely download the book, read it and share it with your friends and colleagues. If you liked the book, only then you have to buy it). See: http://order-papers.com/sites/default/files/tmp/webform/order_download/pdf-the-hundred-page-machine-learning-book-andriy-burkov-pdf-download-free-book-d835289.pdf.

64 Arashi, M., Saleh, A.K.M.E., and Kibria, B.M.G. (2019). Theory of Ridge Regression with Applications. New York: Wiley.

65 Smola, A.J. and Schölkopf, B. (2004). A tutorial on support vector regression. Statistics and Computing 14: 199.

66 Xu, Y., Zomer, S., and Bereton, R.G. (2006). Support vector machines: a recent method for classification in chemometrics. Critical Reviews in Analytical Chemistry 37: 177.

67 Jemwa, G.T. and Aldrich, C. (2005). Improving process operations using support vector machines and decision trees. AIChE Journal 51: 526.

68 Breiman, L., Friedman, J., Stone, C.J., and Olshen, R.A. (1984). Classification and Regression Trees. Monterey, CA: Wadsworth; expanded version (2009) by Chapman and Hall/CRC Press, Boca Raton, FL.

69 Quinlan, J.R. (1986). Induction of decision trees. Machine Learning 1: 81.

70 Quinlan, J.R. (1993). C4.5: Programs for Machine Learning. San Mateo, CA: Morgan Kaufmann Publishers.

71 Myles, A.J., Feudale, R.N., Liu, Y. et al. (2004). An introduction to decision tree modeling. Journal of Chemometrics 18: 275.

72 Singh, S. and Gupta, P. (2014). Comparative study ID3, cart and C4. 5 decision tree algorithm: a survey. International Journal of Advanced Information Science and Technology 27: 97.

---

<!-- PDF page 735 -->

73 Hssina, B., Merbouha, A., Ezzikouri, H., and Erritali, M. (2014). A comparative study of decision tree ID3 and C4.5. International Journal of Advanced Information Science and Technology 27: 13.

74 Geron, A. (2022). Hands-On Machine Learning with Scikit-Learn, Keras, and Tensor Flow: Concepts, Tools and Techniques to Build Intelligent Systems, 3e. Sebastopol, CA: O'Reilly.

75 Kaelbling, L.P., Littman, M.L., and Moore, A.W. (1996). Reinforcement learning: a survey. Journal of Artificial Intelligence Research 4: 237.

76 Haykin, S. (2009). Neural Networks and Learning Machines, 3e. Upper Saddle River, NJ: Pearson Education, Inc.

77 Marsland, S. (2022). Machine Learning: An Algorithmic Perspective, 2e. Boca Raton, FL: Chapman & Hill/CRC Press.

78 Grus, J. (2019). Data Science from Scratch: First Principles with Python, 2e. Sebastopol, CA: O'Reilly.

79 Chollet, F. (2021). Deep Learning with Python. New York: Simon and Schuster.

80 Raschka, S. and Mirjalili, V. (2019). Python Machine Learning: Machine Learning and Deep Learning with Python, Scikit-Learn and TensorFlow2, 3e. Birmingham: Packt Publishing.

81 Pedregosa, F., Varoquaux, G., Gramfort, A. et al. (2011). Scikit-learn: machine learning in python. Journal of Machine Learning Research 12: 2825.

82 Abadi, M., Barham, P., Chen, J. et al. (2016). TensorFlow: a system for large-scale machine learning. 12th {USENIX} Symposium on Operating Systems Design and Implementation (OSDI), 265–283.

83 Dunn, K. (2023) Process improvement using data. Creative Commons Attribution-ShareAlike. https://learnche.org/pid (accessed 30 March 2023).

84 Johnson, R.A. and Wichern, D.W. (2013). Applied Multivariate Statistical Analysis, 6e. Pearson Education, Inc.

85 Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological) 58: 267.

86 Rasmussen, M.A. and Bro, R. (2012). A tutorial on the Lasso approach to sparse modeling. Chemometrics and Intelligent Laboratory Systems 119: 21.

87 Biswal, A. (2022). Top 10 Deep Learning Algorithms You Should Know in 2022 https://www.simplilearn.com/tutorials/deep-learning-tutorial/deep-learning-algorithm (accessed 10 March 2023).

88 Analytics Insight (2022). Top 10 Deep Learning Algorithms Beginners Should Know in 2022. https://www.analyticsinsight.net/top-10-deep-learning-algorithms-beginners-should-know-in-2022 (accessed 11 March 2023).

89 Data Camp (2022). Machine Learning Cheat Sheet. https://www.datacamp.com/cheat-sheet/machine-learning-cheat-sheet (accessed 11 March 2023).

90 Rane, S. (2018). The balance: accuracy vs interpretability. https://towardsdatascience.com/the-balance-accuracy-vs-interpretability-1b3861408062 (accessed 11 March 2023).

91 MathWorks, Inc. (2022). Choose cluster analysis method. https://www.mathworks.com/help/stats/choose-cluster-analysis-method.html (accessed 10 March 2023).

---

<!-- PDF page 736 -->

92 Johnson, S.C. (1967). Hierarchical clustering schemes. Psychometrika 32: 241.

93 Sorlie, T., Perou, C.M., Tibshirani, R. et al. (2001). Gene expression patterns of breast carcinomas distinguish tumor subclasses with clinical implications. Proceedings of the National Academy of Sciences of the United States of America 98: 10869.

94 Easter, M., Kriegel, H.P., Sander, J., and Xu, X. (1996). Density-based spatial clustering of applications with noise. Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining (KDD-96).

95 Zhou, Z. (2012). Ensemble Methods: Foundations and Algorithms. Chapman & Hall/CRC Machine Learning.

96 Schapire, R.E. (1990). The strength of weak learnability. Machine Learning 5: 197.

97 Wolpert, D.H. (1992). Stacked generalization. Neural Networks 5: 241.

98 Breiman, L. (1996). Stacked regressions. Machine Learning 24: 49.

99 Breiman, L. (1996). Bagging predictors. Machine Learning 24: 123.

100 Breiman, L. (1999). Pasting small votes for classification in large databases and on-line. Machine Learning 36: 85.

101 Breiman, L. (2001). Random forests. Machine Learning 45: 5.

102 Druker, H. (1997). Improving regressors using boosting techniques. In: Proceedings of the 14th International Conference on Machine Learning (ed. D.H. Fisher Jr.), 107–115. Burlington, MA: Morgan Kaufmann.

103 Freund, Y. and Schapire, R.E. (1995). A decision-theoretic generalization of on-line learning and an application to boosting. Journal of Computer and System Sciences 55: 119.

104 Friedman, J.H. (2001). Greedy function approximation: a gradient boosting machine. Annals of Statistics 29: 1189.

105 Chen, T. and Guestrin, C. (2016). XGBoost: a scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD 16, San Francisco, CA (13–17 August 2016).

106 van der Lann, M.J., Polley, E.C., and Hunnard, A.E. (2007). Super learner. Statistical Applications in Genetics and Molecular Biology https://doi.org/10.2202/1544-6115.1309.

107 Ioffe, S. and Szegedy, C. (2015). Batch normalization: accelerating deep network training by reducing internal covariate shift. Proceedings of the 32nd International Conference on Machine Learning, PMLR, Volume 37, 448.

108 Glorot, X. and Bengio, Y. (2010). Understanding the difficulty of training deep feedforward neural networks. Proceedings of the 13th International Conference on Artificial Intelligence and Statistics, PMLR, Volume 9, p. 249. http://proceedings.MLr.press/v9/glorot10a (accessed 10 March 2023).

109 Zhou, Y., Cahya, S., Combs, S.A. et al. (2018). Exploring tunable hyperparameters for deep neural networks with industrial ADME data sets. Journal of Chemical Information and Modeling 59: 1005.

110 Kingma, D.P. and Ba, J. (2014). Adam: a method for stochastic optimization. https://doi.org/10.48550/arXiv.1412.6980.

---

<!-- PDF page 737 -->

111 Wang, K., Gopaluni, R.B., Chen, J., and Song, Z. (2018). Deep learning of complex batch process data and its application on quality prediction. IEEE Transactions on Industrial Informatics 16: 7233.

112 Pascanu, R., Mikolov, T., and Bengio, Y. (2013). On the difficulty of training recurrent neural networks. Proceedings of Machine Learning Research 28: 1310.

113 Laurent, C., Pereyra, G., Brakel, P. et al. (2016). Batch normalized recurrent neural networks. Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2657. https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7472159 (accessed 10 March 2023).

114 Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. Neural Computation 9: 1735.

115 Schuster, M. and Paliwal, K.K. (1997). Bidirectional recurrent neural networks. IEEE Transactions on Signal Processing 45: 2673.

116 Zhang, S., Bi, K., and Qiu, T. (2020). Bidirectional recurrent neural network-based chemical process fault diagnosis. Industrial and Engineering Chemistry Research 59: 824.

117 Downs, J.J. and Vogel, E.F. (1993). A plant-wide industrial process control problem. Computers and Chemical Engineering 17: 245.

118 Munshi, J., Chen, W., Chien, T.Y., and Balasubramanian, G. (2021). Transfer learned designer polymers for organic solar cells. Journal of Chemical Information and Modeling 61: 134.

119 Cho, K., Van Merrienboer, B., and Gulcehre, C. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, 1724.

120 Phi, M. (2018). Illustrated guide to LSTM's and GRU's: a step by step explanation. https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21 (accessed 10 March 2023).

121 Bathelt, A., Ricker, N.L., and Jelali, M. (2015). Revision of the Tennessee Eastman process model. IFAC-Papers Online 48: 309.

122 LeCun, Y., Boser, B., Denker, J. et al. (1990). Handwritten digit recognition in a backpropagation network. In: Advances in Neural Information Processing Systems, vol. 2 (ed. D. Touretzky), 396. San Mateo, CA: Morgan Kaufmann.

123 Miccio, L.A. and Schwartz, G.A. (2020). From chemical structure to quantitative polymer properties prediction through convolutional neural networks. Polymer 193: 122341.

124 Zhang, L., Liu, L., Du, J., and Gani, R. (2018). A machine learning based molecular design/screening methodology for fragrance molecules. Computers and Chemical Engineering 114: 295.

125 Huo, W., Li, W., Zhang, Z. et al. (2021). Performance prediction of proton-exchange membrane fuel cell based on convolutional neural network and random Forest feature selection. Energy Conversion and Management 243: 114367.

126 Cotrim, W.S.S., Felix, L.B., Minim, V.P.R. et al. (2021). Development of a hybrid system based on convolutional neural networks and support vector machines

---

<!-- PDF page 738 -->

for recognition and tracking color changes in food during thermal processing.

Chemical Engineering Science 240: 116679.

127 Zhou, Z., Li, X., and Zare, R.N. (2017). Optimizing chemical reactions with deep reinforcement learning. ACS Central Science 3: 1337.

128 Saha, S. (2018). A comprehensive guide to convolutional neural networks. https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 (accessed 11 March 2023).

129 Vaswani, A., Shazeer, N., Parmar, N. et al. (2017). Attention is all you need. 31st Conference on Natural Information Processing Systems (NIPS 2017), Long Beach, CA, 5998–6008. arXiv:1706.03762v5[cs.CL] 6 December 2017.

130 Merritt, R. (2022). What is a transformer model. https://blogs.nvidia.com/blog/2022/03/25/what-is-a-transformer-model (accessed 11 March 2023).

131 Doshi, K. (2021). Transformers Explained Visually (a four-part series). https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452; https://towardsdatascience.com/transformers-explained-visually-part-2-how-it-works-step-by-step-b49fa4a64f34; https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853; https://towardsdatascience.com/transformers-explained-visually-not-just-how-but-why-they-work-so-well-d840bd61a9d3 (accessed 11 March 2023).

132 Cristina, S. (2021). The Transformer Model (a four-part series). https://machinelearningmastery.com/the-transformer-model; https://machinelearningmastery.com/what-is-attention; https://machinelearningmastery.com/the-attention-mechanism-from-scratch; https://machinelearningmastery.com/the-transformer-attention-mechanism (accessed 11 March 2023).

133 Phi, M. (2020). Illustrated guide to transformer: step-by-step explanation. https://towardsdatascience.com/illustrated-guide-to-transformers-step-by-step-explanation-f74876522bc0 (accessed 11 March 2023).

134 Cai, C., Wang, S., Xu, Y. et al. (2020). Transfer learning for drug discovery. Journal of Medicinal Chemistry 63: 8683.

135 Irwin, R., Dimitriadis, S., He, J., and Bjerrum, E.J. (2022). Chemformer: a pre-trained transformer for computational chemistry. Machine Learning: Science and Technology 3: 015022.

136 Chen, G., Song, Z., and Qi, Z. (2021). Transformer-convolutional neural network for surface charge density profile prediction: Enabling high-throughput solvent screening with COSMO-SAC. Chemical Engineering Science 246: 117002.

137 Geng, Z., Chen, Z., Meng, Q., and Han, Y. (2022). Novel transformer based on gated convolutional neural network for dynamic soft sensor modeling of industrial processes. IEEE Transactions on Industrial Informatics 18: 1521–1529.

138 Ba, J.L., Kiros, J.R., and Hinton, G.E. (2016). Layer normalization. arXiv preprint, arXiv:1607.06450.

139 Li, H. (2020). Which machine learning algorithm should I use? The SAS Data Science Blog https://blogs.sas.com/content/subconsciousmusings/2020/12/09/machine-learning-algorithm-use (accessed 10 March 2023).

---

<!-- PDF page 739 -->

140 Metwali, S.A. (2020). How to choose the right machine learning algorithm for your application. https://towardsdatascience.com/how-to-choose-the-right-machine-learning-algorithm-for-your-application-1e36c32400b9 (accessed 10 March 2023).

141 Breton, D. (2021). A full guide to choosing the right machine learning algorithm. https://medium.com/&commat;davidbreton03/a-full-guide-on-choosing-the-right-machine-learning-algorithm-5fa282a0b2a1 (accessed 10 March 2023).

142 MathWorks (2022). Machine Learning in MathLab. https://www.mathworks.com/help/stats/machine-learning-in-ML.html (accessed 10 March 2023).

143 Rajan, K., Zielesny, A., and Steinbeck, C. (2020). DECIMER: towards deep learning for chemical image recognition. Journal of Cheminformatics 12: 65.

144 Goodfellow, I., Pouget-Abadie, J., Mirza, M. et al. (2014). Generative adversarial nets. In: Advances in Neural Information Processing Systems, 27. https://proceedings.neurips.cc/paper/2014/hash/5ca3e9b122f61f8f06494c97b1afccf3-Abstract.html.

145 LeDell, E. and Poirier, S. (2020). H₂O AutoML: scalable automatic machine learning. Proceedings of the AutoML Workshop at ICML. https://www.autoML.org/wp-content/uploads/2020/07/AutoML_2020_paper_61.pdf (accessed 11 March 2023).

146 H₂O.AI (2022). AutoML: Automatic Machine Learning — H₂O 3.36.1.2 Documentation. https://docs.h2o.ai/h2o/latest-stable/h2o-docs/autoML.html (accessed 11 March 2023).

147 Lundberg, S.M. and Lee, S.I. (2017). A unified approach to interpreting model predictions. 31st Conference on Neural Information Processing Systems, 4768.

148 Agarwal, A., Liu, Y.A., Dooley, L. et al. (2022). Large-scale industrial fermenter foaming control: automated machine learning for antifoam prediction and defoaming process implementation. Industrial and Engineering Chemistry Research 61: 5227.

149 Tera, J. (2022). Keras vs TensorFlow vs Pytorch: Key Differences Among the Deep Learning Framework. https://www.simplilearn.com/keras-vs-tensorflow-vs-pytorch-article#:~:text=TensorFlow%20is%20an%20open%2Dsourced,because%20it%27s%20built%2Din%20Python (accessed 10 March 2023).

150 Sheela, K.G. and Deepa, S.N. (2013). Review on methods to fix number of hidden neurons in neural networks. Mathematical Problems in Engineering https://doi.org/10.1155/2013/425740.

151 Shin-ike, K. (2010). A two-phase method for determining the number of neurons in the hidden layer of a 3-layer neural network. Proceedings of SICE Annual Conference 2010. https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5603258 (accessed 10 March 2023).

152 Srivastava, N., Hinton, G., Krizhevsky, A. et al. (2014). Dropout: a simple way to present neural networks from overfitting. Journal of Machine Learning Research 14: 1929.

153 Sheridan, R.P. (2013). Time-split cross-validation as a method for estimating the goodness of prospective prediction. Journal of Chemical Information and Modeling 53: 783.

---

<!-- PDF page 740 -->

154 LeCun, Y., Bengio, Y., and Hinton, G. (2015). Deep learning. Nature 521: 436.

155 Gers, F. and Schmidhuber, J. (2000). Recurrent nets that time and count. Proceedings of the IEEE-INNS-ENNS International Joint Conference on Neural Networks, 189.

156 Ma, Y., Zhu, W., Benton, M.G., and Romagnoli, J. (2019). Continuous control of a polymerization system with deep reinforcement learning. Journal of Process Control 75: 40.

157 Agarwal, P., Tamer, M., Sahraei, M.H., and Budman, H. (2019). Deep learning for classification of profit-based operating regions in industrial processes. Industrial and Engineering Chemistry Research 59: 2378.

158 Sun, Q. and Ge, Z. (2021). A survey on deep learning for data-driven software sensors. IEEE Transactions on Industrial Informatics 17: 5853.

159 Olson, R.S., Urbanowicz, R.J., Andrews, P.C. et al. (2016). Automating biomedical data science through tree-based pipeline optimization. In: Applications of Evolutionary Computation, 123. https://link.springer.com/chapter/10.1007/978-3-319-31204-0_9.

160 Gaulton, A., Arsey, A., Nowotka, M. et al. (2017). The ChEMBL database in 2017. Nucleic Acids Research 45: D945.

161 Spyridon, P. and Boutalis, Y.S. (2018). Generative adversarial networks for unsupervised fault diagnosis. Proceedings of 2018 European Control Conference, Limassol, Cyprus (12–15 June 2018). https://ieeexplore.ieee.org/abstract/document/8550560 (accessed 11 March 2023).

162 He, R., Li, X., Chen, G. et al. (2020). Generative adversarial network-based semi-supervised learning for real-time risk warning of process industries. Expert Systems with Applications 150: 113244.

163 Zhu, C.-H. and Zhang, J. (2020). Developing soft sensors for polymer melt index in an Industrial polymerization process using deep belief networks. International Journal of Automation and Computing 17: 44.

164 Gao, X., Shang, C., Jiang, Y. et al. (2014). Refinery scheduling with varying crude: a deep belief network classification and multimodel approach. AIChE Journal 60: 2525.

165 Li, F., Zhang, J., Shang, C. et al. (2018). Modelling of a post-combustion  $ CO_{2} $ capture process using deep belief network. Applied Thermal Engineering 130: 997.

166 Zhang, Z. and Zhao, J. (2017). A deep belief network based fault diagnosis model for complex chemical processes. Computers and Chemical Engineering 107: 395.

167 ProjectPro (2022). Top 10 Deep Learning Algorithms in Machine Learning [2022]. https://www.projectpro.io/article/deep-learning-algorithms/443#mcetoc_1g5it6rql20 (accessed 11 March 2023).