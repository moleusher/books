# Untitled

<!-- PDF page 429 -->

Integrated Process Modeling,

Advanced Control and Data Analytics for

Optimizing Polyolefin Manufacturing

---

<!-- PDF page 430 — MISSING, not yet parsed -->


---

<!-- PDF page 431 -->

# Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing

Volume 2

Y. A. Liu

Niket Sharma

WILEY vch

---

<!-- PDF page 432 -->

## Authors

##### Prof. Y. A. Liu

Department of Chemical Engineering

Virginia Polytechnic Institute and State

University

635 Prices Fork Road

245 Goodwin Hall

Blacksburg

VA, US, 24061

### Dr. Niket Sharma

Department of Chemical Engineering

Virginia Polytechnic Institute and State

University

635 Prices Fork Road

245 Godwin Hall

Blacksburg

VA, US, 24061

Cover Image:

© metamorworks/Shutterstock

All books published by WILEY-VCH are carefully produced. Nevertheless, authors, editors, and publisher do not warrant the information contained in these books, including this book, to be free of errors. Readers are advised to keep in mind that statements, data, illustrations, procedural details or other items may inadvertently be inaccurate.

Library of Congress Card No.: applied for

British Library Cataloguing-in-Publication Data

A catalogue record for this book is available

from the British Library.

## Bibliographic information published by the Deutsche Nationalbibliothek

The Deutsche Nationalbibliothek lists this publication in the Deutsche Nationalbibliografie; detailed bibliographic data are available on the Internet at <http://dnb.d-nb.de>.

© 2023 WILEY-VCH GmbH, Boschstraße 12, 69469 Weinheim, Germany

All rights reserved (including those of translation into other languages). No part of this book may be reproduced in any form – by photoprinting, microfilm, or any other means – nor transmitted or translated into a machine language without written permission from the publishers. Registered names, trademarks, etc. used in this book, even when not specifically marked as such, are not to be considered unprotected by law.

Print ISBN: 978-3-527-35269-2

ePDF ISBN: 978-3-527-84381-7

ePub ISBN: 978-3-527-84382-4

oBook ISBN: 978-3-527-84383-1

Cover Design: SCHULZ Grafik-Design Typesetting: Straive, Chennai, India

---

<!-- PDF page 433 -->

## Contents

## Volume 1

Foreword xxvii  
Preface xxxiii  
Acknowledgment xxxvii  
Copyright Notice xxxix  
About the Authors xli  
About the Companion Website xliii  
1 Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing 1  
2 Selection of Property Methods and Estimation of Physical Properties for Polymer Process Modeling 41  
3 Reactor Modeling, Convergence Tips, and Data-Fit Tool 87  
4 Free Radical Polymerizations: LDPE and EVA 115  
5 Ziegler–Natta Polymerization: HDPE, PP, LLDPE, and EPDM 163  
6 Free Radical and Ionic Polymerizations: PS and SBS Rubber 267  
7 Improved Polymer Process Operability and Control Through Steady-State and Dynamic Simulation Models 321

---

<!-- PDF page 434 -->

## Volume 2

Foreword xxv  
Preface xxxi  
Acknowledgment xxxv  
Copyright Notice xxxvii  
About the Authors xxxix  
About the Companion Website xli  
8  
Model-Predictive Control of Polyolefin Processes 381  
8.1 Introduction to Advanced Process Control (APC) 382  
8.1.1 Some Basic Definitions 382  
8.1.1.1 Independent and Dependent Variables 382  
8.1.1.2 Unit-Step Response Curve: Time to Steady State and Steady-State Gain 383  
8.1.1.3 Integrating Variable (Ramp Variable) 383  
8.1.2 Where Do the Benefits of APC Come from? 385  
8.1.2.1 Online Reconciliation of Model-based Predictions to the Process Measurements to Provide Robustness to the Multivariable Dynamic Step-response Model 385  
8.1.2.2 Steady-State Economic Optimization to Determine MV and CV Targets to Minimize Cost and Maximize Profit 389  
8.1.2.3 Determination of Future MV Moves to Minimize the Least-Squares Errors Between Predicted and Desired Economic Optimum Target Values of CVs 392  
8.1.3 Linear Modeling for Dynamic Matrix Control (DMC) 395  
8.1.3.1 Step-Response Model 395  
8.1.3.2 Finite-Impulse Response (FIR) Model 397  
8.1.4 Model Evaluation and Useful Tools 400  
8.1.4.1 Relative Gain Array (RGA) 400  
8.1.4.2 Ill-Conditioned Model Matrices and Collinear System 403  
8.1.5 Open-Loop Prediction, Prediction Error Filtering, and Prediction Update for Steady-State Variables 405  
8.1.5.1 Prediction Error (PREDER) 405  
8.1.5.2 Accumulated Prediction Error (ACPRER) 405  
8.1.5.3 Average Prediction Error (AVPRER) and Prediction Error Filtering 406  
8.1.5.4 Prediction Update for Control Variable Values 406  
8.1.6 Concepts and Parameters in Steady-State Economic Optimization and Dynamic Controller Simulation 406  
8.1.6.1 Variable Limits and Feasible Solution 406  
8.1.6.2 CV Limit Ranking Method to Handle Steady-State Feasibility 407  
8.1.6.3 Steady-State Equal Concern Error (SS ECE) to Handle Steady-State Feasibility 409  
8.1.6.4 Dynamic Equal Concern Errors for CV Limits in Dynamic Controller Simulation 411

---

<!-- PDF page 435 -->

8.1.6.5 Move Suppression for MV 413  
8.2 Workshop 8.1: Development and Application of a Predictive Controller Model for a Copolymerization Process 414  
8.2.1 Objective 414  
8.2.2 A Copolymerization Reactor 414  
8.2.3 Starting the DMC3 Builder Program: Creating a New Project 415  
8.2.4 DMC3 Builder Task One: Data Processing for Developing a Master Model – Import Process Data, Merge the Datasets, and Mark and Delete Bad Data Slices 416  
8.2.5 Create Manipulated Variable (MV) and Controlled Variable (CV) Lists 419  
8.2.6 DMC3 Builder Task One: Model Identification (ID) for Developing Master Model – Setting up the Model ID 421  
8.2.7 Guidelines for Selecting Model Parameters 424  
8.2.8 Uncertainty and Correlation Plots of the Master Model 426  
8.2.9 DMC3 Builder Task One: Building the Controller Model for Developing the Master Model 427  
8.2.10 DMC3 Builder Task One: Creating a Controller Model 429  
8.2.11 Identification of Dead Time in Model Response Curves 431  
8.2.12 Collinearity Analysis 433  
8.2.13 Open-Loop Prediction and Prediction Error (Model Bias) 439  
8.2.14 DMC3 Builder Task 2: Configuration – Model Configuration 440  
8.2.15 DMC3 Builder Task 2: Configuration – Configuring the Steady-State Optimization 443  
8.2.16 DMC3 Builder Task 3: Optimization – Performing the Steady-State Optimization 444  
8.2.17 DMC3 Builder Task 4: Simulation – Configuring and Simulating the Dynamic Controller 445  
8.2.18 DMC3 Builder Task 4: Simulation – Dynamic Controller Applications to Polymer Production and Setpoint Changes 447  
8.3 Model-Predictive Control of Nonlinear Polyolefin Processes 448  
8.3.1 Challenges of Developing Nonlinear Predictive Modeling for Polyolefin Process Control 448  
8.3.2 Nonlinear Steady-State Mapping by State-Space Bounded Derivative Network (SS-BDN) 449  
8.3.2.1 Possible Gain Inversion and Non-Monotonic Behavior of Conventional Neural Networks 449  
8.3.2.2 State-Space Bounded Derivative Network (SS-BDN) 451  
8.4 Workshop 8.2: Development of a Nonlinear Predictive Controller Model for a Polypropylene Process 453  
8.4.1 Objective 453  
8.4.2 Starting an APC Project and Choosing Nonlinear Controllers, and Data Preprocessing 453  
8.4.3 Aspen Nonlinear Controller: Task 1 – Model Identification 456  
8.4.3.1 Step-Response Plot 456

---

<!-- PDF page 436 -->

8.4.3.2 I/O Response Plot 458  
  
8.4.3.3 Gain Plot 459  
  
8.4.4 Aspen Nonlinear Controller: Task 1 – Model Identification; Building the Nonlinear State-Space Bounded Derivative Network (SS-BDN) 460  
  
8.4.4.1 Configure Dynamics and Output States 460  
  
8.4.4.2 Build Model with Gain Constraints 462  
  
8.4.4.3 Fine-Tune Steady-State BDN Gains 464  
  
8.4.4.4 Generate Model Predictions 464  
  
8.4.5 Aspen Nonlinear Controller: Task 2 – Configuration – Model Configuration 465  
  
8.4.6 Aspen Nonlinear Controller: Task 2 – Configuring and Running the Steady-State Optimization 466  
  
8.4.7 Aspen Nonlinear Controller: Task 3 – Configuring and Simulating the Dynamic Controller with Setpoint Changes 470  
  
8.5 Aspen Maestro for Automating the Model-Building Workflow 471  
  
References 475  
9 Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing 477  
  
9.1 Introduction to Principal Component Analysis (PCA) 477  
  
9.1.1 Introduction to Principal Components 478  
  
9.1.2 Data Preprocessing: Mean-Centered and Scaled Process Data Matrix X, Principal Component Score Matrix T, and Principal Component Loading Matrix P 480  
  
9.1.3 Development of PCA Model 481  
  
9.1.4 Prediction Errors from PCA Model 482  
  
9.1.5 Hotelling's T² Value from PCA Model 485  
  
9.2 Workshop 9.1: PCA of the Process Variables Affecting the Quality and Conversion of LDPE Product from a Two-Zone Tubular Reactor 486  
  
9.3 Partial Least Squares or Projection to Latent Structures (PLS) 498  
  
9.3.1 Introduction to PLS 498  
  
9.3.2 Nonlinear Iterative Partial Least Squares (NIPALS) Algorithm 500  
  
9.3.2.1 Deflation Step 1: Calculate a Loading Vector for the X Space 501  
  
9.3.2.2 Deflation Step 2: Remove the Predicted Variability from X and Y 501  
  
9.4 Hands-on Workshops of PLS of LDPE and HDPE Processes 502  
  
9.4.1 Workshop 9.2: PLS of Process and Quality Variables Affecting the Quality and Conversion of LDPE Product from a Two-Zone Tubular Reactor 502  
  
9.4.2 Workshop 9.3: Polymer Melt Index Prediction and Causal Analysis Using PLS 507  
  
9.5 Workshop 9.4: Polymer Melt Index Prediction and Causal Analysis with Measurement Time Lags Using PLS 515  
  
9.5.1 Introduction to PLS with Measurement Time Lags 515

---

<!-- PDF page 437 -->

9.5.2 Workshop 9.4: Application of Aspen ProMV to Polymer Melt Index Prediction and Causal Analysis with Measurement Time Lags Using PLS 516  
  
9.6 Multiway PCA and PLS for Batch Processes 518  
  
9.6.1 Batch-Wise Unfolding and Observation-Wise Unfolding Approaches to Multiway PLS 518  
  
9.6.2 Workshop 9.5: Application of Aspen ProMV to Batch-Wise Unfolding (BWU) Approach to Multiway PCA of Batch Polymerization Data 521  
  
9.7 Implementation of Multivariate Statistics Models 527  
  
9.8 Conclusion and Suggested Resources for Further Studies 529  
  
References 529  
  
10 Applications of Machine Learning to Optimizing Polyolefin Manufacturing 533  
  
10.1 Introduction 534  
  
10.1.1 The Time for AI, Particularly Machine Learning, in Chemical Industries Has Finally Arrived 534  
  
10.1.2 Data, Representation, and Learning 535  
  
10.1.2.1 Data 535  
  
10.1.2.2 Representation 536  
  
10.1.2.3 Learning 537  
  
10.1.3 Suggested Resources to Get Started with Machine Learning 540  
  
10.1.3.1 Reference Books on AI and ML 540  
  
10.1.3.2 Basic Training of Python 540  
  
10.1.3.3 Books with ML Principles and Coding Examples 540  
  
10.2 An Overview of Relevant Machine Learning Concepts and Models 541  
  
10.2.1 Supervised Learning Methods for Regression Applications 541  
  
10.2.1.1 Linear Regression 541  
  
10.2.1.2 Performance Evaluation Metrics for Regression Models 542  
  
10.2.1.3 Polynomial Regression, Underfitting, Overfitting, and Regularization 543  
  
10.2.1.4 Regularized Linear Regression Models: Ridge Linear Regression and Lasso Linear Regression 544  
  
10.2.2 Supervised Learning Methods for Classification Applications 546  
  
10.2.2.1 Logistic Regression 546  
  
10.2.2.2 Radial Basis Function Network (RBFN) 548  
  
10.2.2.3 Support Vector Machine (SVM) Classification and Regression 553  
  
10.2.2.4 Decision Trees for Classification and Regression Problems 559  
  
10.2.2.5 Performance Evaluation Metrics for Classification Models 567  
  
10.2.3 Unsupervised Learning for Dimensionality Reduction and Clustering Applications 568  
  
10.2.3.1 An Overview 568  
  
10.2.3.2 Kernel Principal Component Analysis (KPCA) 568  
  
10.2.3.3 K-Means Clustering 569  
  
10.2.3.4 Hierarchical Clustering 570

---

<!-- PDF page 438 -->

10.2.3.5 Density-Based Spatial Clustering of Applications with Noise (DBSCAN) 572  
10.2.3.6 Gaussian Mixture Model (GMM) 573  
10.3 Enhanced Learning by Ensemble Methods 575  
10.3.1 An Overview 575  
10.3.2 Bagging: Random Forest Algorithm 576  
10.3.3 Boosting: AdaBoost and XGBoost Algorithms 577  
10.3.4 Stacking: Stacked Regression 579  
10.4 Enhanced Learning by Deep Neural Networks 580  
10.4.1 Relevant Concepts of Conventional Neural Networks for Deep Learning Applications 580  
10.4.1.1 Basic Concepts and Parameters for a Multilayer Perceptron (MLP) 580  
10.4.1.2 Incorporation of a Momentum Coefficient 584  
10.4.1.3 Alternative Basic Network Configuration Using Bias Inputs Instead of Internal Thresholds 585  
10.4.1.4 Selection of Activation Functions, Vanishing Gradient, and Exploding Gradient Problems 587  
10.4.1.5 Batch Normalization (BN) 589  
10.4.1.6 Avoid Overfitting Through Regularization: Weight Decay and Dropout 589  
10.4.1.7 Using a Faster Optimizer 590  
10.4.1.8 Recommended Multilayer Perceptron (MLP) Architecture for Deep Learning Applications 591  
10.4.2 Deep Learning with Recurrent Neural Networks (RNNs) 591  
10.4.2.1 Recurrent Neural Networks for Predictive Modeling of Time-Dependent Processes 591  
10.4.2.2 Long Short-Term Memory (LSTM) RNNs 595  
10.4.2.3 Gated Recurrent Unit (GRU) 597  
10.4.2.4 Bidirectional RNNs 599  
10.4.3 Convolutional Neural Networks (CNNs) 600  
10.4.4 Attention is All You Need: Transformer Model 602  
10.4.4.1 Encoder-Decoder Stacks 605  
10.4.4.2 Self-Attention and Attention Mechanisms Within the Encoder-Decoder Stacks 606  
10.4.4.3 Softmax Function and Probability-Based Weighting Factors 607  
10.4.4.4 Attention Mechanisms in Encoder-Decoder Stacks 607  
10.4.4.5 Position-Wise Feedforward Networks 609  
10.5 General Guidelines for Choosing Appropriate ML Algorithms 609  
10.5.1 Factors to Consider in Selecting Appropriate ML Algorithms 609  
10.5.2 A Summary of Selected Machine Algorithms 611  
10.5.3 Decision Chart for Selecting Appropriate ML Algorithms 611  
10.6 Workshop 10.1: Prediction of HDPE Melt Index Using Random Forest and eXtreme Gradient Boosting (XGBoost) Ensemble Learning Models 614  
10.6.1 Objective and HDPE Process 614

---

<!-- PDF page 439 -->

10.6.2 Data Collection and Visualization 615  
10.6.3 Data Cleaning and Preprocessing 618  
10.6.3.1 Feature Selection 618  
10.6.3.2 Defining Training and Evaluation Datasets 620  
10.6.3.3 Standardization 620  
10.6.4 Build Machine Learning Model 620  
10.6.5 Analysis of ML Model Results 621  
10.6.6 Melt Index Prediction Using XGBoost 624  
10.7 Workshop 10.2: Prediction of HDPE Melt Index Using Deep Neural Networks 626  
10.7.1 Objective 626  
10.7.2 Deep Neural Network Configuration 626  
10.7.3 Prediction of Neural Network Configuration 627  
10.8 Workshop 10.3: Prediction of Time-Dependent HDPE Melt Index Using Dynamic Deep Recurrent Neural Networks 629  
10.8.1 Objective 629  
10.8.2 Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) 629  
10.8.3 Gated Recurrent Unit (GRU) 630  
10.9 Workshop 10.4: Polymer Property Prediction Based on Molecular Structure Using Convolutional Neural Network 631  
10.9.1 Objective 631  
10.9.2 Transformer Network for Deep Learning for Chemical Image Recognition (DECIMER) to Convert a Molecular Structure Image to SMILES Representation 633  
10.9.3 Convolutional Neural Network for Predicting Polymer Property Using SMILES Representation 633  
10.10 Workshop 10.5: Melt Index Prediction Using Automated Machine Learning 636  
10.11 Limitations of Stand-Alone Data-Based Models 639  
References and Further Reading 640  
11 A Hybrid Science-Guided Machine Learning Approach for Modeling Chemical and Polymer Processes 651  
11.1 Introduction 652  
11.2 Applications of Hybrid SGML Approach in Chemical Engineering 653  
11.3 A Classification and Exposition of Hybrid SGML Models 655  
11.4 ML Complements Science 656  
11.4.1 Direct Hybrid Modeling 656  
11.4.1.1 Parallel Direct Hybrid Model 656  
11.4.1.2 Series-Direct Hybrid Model 658  
11.4.1.3 Series-Parallel or Combined Direct Hybrid Model 660  
11.4.1.4 Workshop 11.1: An Application of Combined Direct Hybrid Modeling to Polymer Manufacturing 661  
11.4.2 Inverse Modeling 663

---

<!-- PDF page 440 -->

11.4.3 Workshop 11.2: An Application of Inverse Modeling to Polymer Manufacturing 666

11.4.4 Reduced-Order Models 668

11.4.5 Workshop 11.3: An Application of Reduced-Order Modeling to Polymer Manufacturing 670

11.4.6 Hybrid SGML Modeling for Uncertainty Quantification 671

11.4.7 Workshop 11.4: An Application of SGML Modeling to Uncertainty Quantification in Polymer Manufacturing 673

11.4.8 Hybrid SGML Modeling to Aid in Discovering Scientific Laws Using ML 675

11.5 Science Complements ML 677

11.5.1 Science-Guided Design 677

11.5.2 Science-Guided Learning 678

11.5.3 Workshop 11.5: An Illustrative Example of Science-Guided Learning 679

11.5.4 Science-Guided Refinement 681

11.6 Workshop 11.6: Reduced-Order Model for a Polystyrene Process Using Aspen Multi-Case and Aspen AI Model Builder 682

11.6.1 Introduction to Aspen Multi-Case and Aspen AI Model Builder 682

11.6.2 Developing a Hybrid Reduced-Order Model (ROM) for a Polystyrene Process 683

11.7 Challenges and Opportunities of Hybrid SGML Approach for Modeling Chemical and Polymer Processes 689

11.8 Conclusion 689

References 690

Appendix A Matrix Algebra in Multivariate Data Analysis and Model Predictive Control 699

A.1 Important Matrices in Multivariate Data Analysis 699

A.1.1 Data Matrix X 699

A.1.2 Sample Mean  $ \overline{X} $ 699

A.1.3 Sample Variance,  $ s_{kk} $ or  $ s_{k}^{2} $ and Sample Standard Deviation  $ s_{k} $ 700

A.1.4 Sample Covariance  $ s_{ik} $ 700

A.1.5 Sample Correlation Coefficient  $ r_{ik} $ 701

A.1.6 Mean-Centered Data Matrix or Deviation Matrix  $ X_{d} $, and Diagonal Matrix of the Inverse of the Standard Deviation  $ D_{s} $ 702

A.1.7 Sum of Squares and Cross Products (SSCP), and Sample Variance and Covariance Matrix S 702

A.1.8 Standardized Data Matrix, or Mean-Centered and Scaled Data Matrix  $ X_{s} $ and Sample Correlation Coefficient Matrix R 703

A.1.9 A Summary: Three Important Matrices in Multivariate Data Analysis 704

A.2 Review of Selected Matrix Concepts 705

A.2.1 Rank of a Data Matrix 705

A.2.2 Inverse of A Matrix 705

---

<!-- PDF page 441 -->

A.2.3 Determinant of A Matrix 705

A.2.4 Orthogonal Vectors and Matrices 706

A.2.5 Eigenvalues and Eigenvectors 706

A.2.6 Factorization or Decomposition of Matrices 707

A.2.6.1 LU Factorization 707

A.2.6.2 Cholesky Factorization 708

A.2.6.3 Singular Value Decomposition (SVD) 709

A.2.6.4 Spectral or Eigenvalue Decomposition 710

A.3 Implementing Basic Matrix Operations in MATLAB 710

A.4 Implementing Basic Multivariate Data Analysis in MATLAB 713

A.5 Eigenvalues, Eigenvectors, and Factorization (Decomposition) of Matrices 715

A.6 Principal Component Analysis (PCA) 717

A.7 Implementing Basic Matrix Operations in Python 722

A.8 Implementing Basic Multivariate Data Analysis in Python 726

A.9 Eigenvalues, Eigenvectors, and Factorization (Decomposition) of Matrices 728

A.10 Principal Component Analysis (PCA) 731

A.10.1 Principal Component Loading Matrix, coeff or P (5 × 5) 732

A.10.2 Principal Component Score Matrix, score or T (8 × 5) 732

A.10.3 Principal Component Variances, Column Vector Latent 734

A.10.4 Hotelling's T-Squared Statistic Column Vector, Tsquared 735

A.10.5 Percent of Data Variability Explained by Principal Components, Vect Explained 736

## Appendix B Introduction to Python for Chemical Engineers 737

Aman Aggarwal

B.1 Introduction 737

B.2 Installing Python 738

B.3 Basics with Python 739

B.4 Different Data Types in Python 740

B.5 Functions and Loops in Python 743

B.5.1 "For loop" Example 744

B.5.2 "While loop" Example 744

B.5.3 "Break" and "Continue" Statement Example 745

B.6 Libraries in Python 745

B.6.1 Chemics 746

B.6.2 Fluids 746

B.6.3 TensorFlow 747

B.6.4 Scikit-learn (Sklearn) 747

B.6.5 Numpy 747

B.6.6 Pandas 748

B.6.7 Matplotlib 748

---

<!-- PDF page 442 -->

Contents

B.7 Machine-learning Algorithms with Python: Hyperparameter Optimization and Sample Codes 749

B.8 Sample Codes for Table B.1 751

References 758

Index 759

---

<!-- PDF page 443 -->

## Foreword

Polyolefins are among the most widely used commodity and specialty polymers, with uses in films and packaging, medical, consumer, and industrial goods, and the automotive industry. Polyolefins have wide applications requiring different properties with different molecular weight distributions and branching distributions. With the increase in the world population and a growing consumer class, the high demand for polyolefins presents a dual challenge to the chemical industry to produce more polyolefins to meet these growing needs while minimizing the environmental impact. Modeling and optimization of polyolefin processes will enable engineers to achieve this important challenge. However, the complex nature of polyolefin processes requires the understanding and application of a unique combination of relevant thermodynamics, polymerization kinetics, reactor design, product separation, and process control in a manner not typically required for more conventional chemical processes. This textbook is a comprehensive and practical guide for tackling the technical complexities that engineering practitioners will face while modeling and optimizing industrial polyolefin processes in both steady-state and dynamic operations.

Professor Y. A. Liu has, for many decades, been a tireless and enthusiastic advocate and educator in the application of computer-aided modeling and simulation to solve real industrial problems. Prof. Liu has worked with many leading companies around the world and trained thousands of engineers to apply process simulation, optimization, and advanced process control to a variety of industries, including petroleum refining, industrial water savings, carbon capture, and polymer production. This book is the latest in a series of excellent textbooks authored by Prof. Liu and his students, which provide a detailed technical and practical engineering approach to solving real-world problems.

This textbook by Prof. Liu and Dr. Sharma covers the full-scale modeling of industrial polymer processes in detail with easy-to-follow, step-by-step examples. This textbook covers advances in different areas of polymer process modeling, such as polymer thermodynamics, kinetics, reactor modeling, and process control. The book presents an industrially validated methodology for modeling and optimizing complex industrial polyolefin processes using commercially available computer-aided engineering tools.

---

<!-- PDF page 444 -->

This textbook starts with the fundamentals of polymer component characterization and thermodynamic property calculations, introducing the concept of the segment-based approach and polymer attributes, followed by evaluation and selection of thermodynamic models, parameter estimation, and data regression. Specific guidelines for the selection of an appropriate polymer property method for modeling specific polyolefin processes are discussed, drawing on knowledge from industrial experience. The authors present an effective methodology for estimating kinetics from plant data, which is critical since there are multitude of kinetic parameters to estimate for a catalytic polyolefin process. They also showcase the advantages of dynamic process models for applications such as polymer-grade transition that can have significant cost implications. This textbook covers the application of advanced process control and model predictive control for optimizing industrial polymer processes, including a discussion on controller tuning to optimize control performance.

In addition, this textbook has a comprehensive section on recent advances in multivariate data analysis and machine learning applications for process modeling. The authors introduce these concepts in a manner that is easily understandable and showcase how these technologies can be applied in the process industry. Especially significant for polymer processes is the application of data analytics to infer polymer quality measurements such as polymer melt index and molecular weight. The authors also highlight the importance and methodologies for combining first-principles engineering models with machine learning (hybrid science-guided machine learning) to develop hybrid models, which provide more accurate and consistent predictions in compliance with physical constraints.

This textbook, in my opinion, should be very beneficial to senior and graduate students, university faculty, and practicing engineers and industrial scientists who wish to learn the fundamentals and practice of process modeling, advanced control, and data analytics for sustainable design, operation, and optimization of polyolefin manufacturing processes. I am not aware of any similar books that cover the broad scope with excellent quality, while providing real-world examples.

By Willie K. Chan

Chief Technology Officer

Aspen Technology, Inc.

---

<!-- PDF page 445 -->

Professor Y. A. Liu has had an extraordinary career spanning over 40 years in teaching process design, authoring textbooks for process design and simulation, and ingenious and impactful scholarship in sustainable engineering. As someone who has collaborated with Prof. Liu and benefited from his kind advice and support for more than 25 years in the area of computer-aided chemical engineering, I admire and congratulate Prof. Liu for yet another exceptional achievement in the textbook "Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing."

This textbook on process modeling, advanced control, and data analytics applied to polyolefin manufacturing represents a particularly beneficial contribution to university students and faculty, industrial practitioners, and scientists, considering the fact that polyolefins represent approximately 60% of commercial polymer production. To truly appreciate the significance of this textbook on modeling and simulation of polyolefin processes, we must recognize this textbook as one more milestone in Prof. Liu's contributions over the years in authoring a series of textbooks that cover modeling and simulation of chemical processes and help shape the curriculum in chemical process design. Among them, I wish to highlight the following four recent textbooks: (1) Step-Growth Polymerization Process Modeling and Product Design by Wiley, New York (2008), (2) Refining Engineering: Integrated Process Modeling and Optimization by Wiley-VCH, Weinheim, Germany (2012), (3) Petroleum Refinery Process Modeling: Integrated Optimization Tools and Applications by Wiley-VCH, Weinheim, Germany (2018), and (4) Design, Simulation and Optimization of Adsorptive and Chromatographic Separations: A Hands-on Approach by Wiley-VCH, Weinheim, Germany (2018). All these textbooks capture the chemical engineering fundamentals for these critically important and complex chemical manufacturing processes, the modern-day process modeling and simulation technologies implemented in commercial process simulators, and the industrial practice of professional engineers dedicated to the design, control, and optimization of these processes. All four textbooks have received outstanding reviews by academic experts, industrial practitioners, and my own students at Texas Tech University. I have no doubt this new textbook on polyolefin processes will be another resounding success.

---

<!-- PDF page 446 -->

Personally, I had been deeply involved in the invention, implementation, testing, commercialization, and application of modern-day process simulators for modeling and simulation of varieties of chemical processes, including polyolefin processes. Knowing the challenges in developing modeling and simulation technologies and the tremendous efforts required of many top-notch software developers and industrial collaborators to overcome the challenges, I am particularly appreciative of the fact that Prof. Liu and his doctoral students dedicated their time and effort to writing textbooks based on their latest research and advances by others in the field. He and his students write detailed expositions and develop hands-on workshops to educate current and future workforce on how to apply the advances in process system engineering and computer-aided design using commercial software tools. Furthermore, Prof. Liu and his student co-authors have done so beautifully and effectively in many fields as diverse as neural networks, pinch technology for industrial water reuse, petroleum refining processes, adsorptive and chromatographic separations, industrial polymer manufacturing, among others.

Chapters 1–7 of this book present the fundamentals and practice of steady-state and dynamic simulation and control of polyolefin processes with 24 hands-on workshops with step-by-step instructions applied to industrial polyolefin processes with realistic plant data. Chapter 8 introduces the key concepts and software implementation of the third generation of dynamic matric control (DMC3) and nonlinear advanced control of polyolefin processes and includes two detailed hands-on workshops on advanced control copolymerization and polypropylene processes. Chapters 9–11 demonstrate how multivariate statistics and machine learning are playing an increasingly important role in optimizing polyolefin manufacturing with 16 hands-on application workshops. The authors state that their goal for this part is to prepare an overview of multivariate statistics and machine learning for university students and faculty, practicing engineers and scientists who are new to the field, and also for those who are knowledgeable but wish to know the new developments and application literature in chemical and polymer processes. A study of these chapters clearly shows that they have done an excellent job.

This book is beneficial to beginners and not only provides detailed tutorials and guides for many different applications but also describes more technical details that are useful to advanced practitioners. This book represents a milestone in advancing polymer process modeling, advanced control, and data analytics, and I cannot wait to learn what Prof. Liu has in mind for his next textbook.

By Chau-Chyun Chen

Horn Distinguished Professor and

Jack Maddox Distinguished Chair in Engineering

Texas Tech University

An inventor of segment-based modeling technology

for polymer processes

Member, National Academy of Engineering

---

<!-- PDF page 447 -->

Professor Y. A. Liu is well known in the chemical engineering community for his passion, mission, and dedication in teaching fundamentals and practice of process modeling in polymer manufacturing for many decades. The textbook Step-Growth Polymerization Process Modeling and Product Design that he co-authored with Kevin C. Seavey in 2008 has been an asset to students and industrial practitioners in understanding how to apply process modeling and product design concepts in industrial polymer processes.

Since 2008, availability of big data, advances of machine learning algorithms, and affordability of computing resources have propelled the digital transformation in the chemical and materials industry. Y. A. Liu is an award-winning researcher to incorporate AI, machine learning, and data analytics to enhance modeling, control, and optimization of polymer processes; he is also an inspiring teacher to pass along his knowledge. This textbook lays out the foundation of process modeling in Chapters 1–7, introduces important role of advanced process control in Chapter 8, and showcases the evolution of how data analytics are positively impacting polymer process in Chapters 9–11. Chapter 9 explains why multivariate statistics (principal component analysis and partial least squares) remain the "gold standard" for analyzing manufacturing data from polymer processes. Chapter 10 highlights recent advances in machine-learning algorithms (from supervised learning to reinforcement learning; from logistic regression to transformer deep neural network); and Chapter 11 outlines promising research direction on hybrid science-guided machine learning (also known as hybrid modeling or physics-informed machine learning).

The contents of Chapters 9–11 resonate with my two-decade long industrial research and implementation experience of AI, machine learning, and data analytics. In fact, in a recent AIChE Journal article, Toward AI at scale in the chemical industry that I co-authored, we positioned AI as a portfolio of enabling technologies that need to be applied in context to address a specific business need. Successful industrial AI applications have a common attribute that the right AI methods are selected based on domain process knowledge and data characteristics. Y. A. read my paper around the same time that I read his AIChE Journal article, A Science-Guided Machine Learning Approach to Modeling Chemical Processes: A Review. I am glad that we shared a common vision, and this textbook is a testimony on how AI has been successfully applied in the context of polymer manufacturing.

---

<!-- PDF page 448 -->

I am grateful that Y. A. Liu and Niket Sharma have written this textbook with plenty of hands-on examples and workshops with industrial relevance. This book explains the Why, What, and How of process modeling, advanced control, AI, and data analytics for industrial polymer processes, and it will impact the chemical engineering community for decades to come.

By Leo H. Chiang

Senior R&D Fellow, AI and Data Analytics

The Dow Chemical Company

Member, National Academy of Engineering

---

<!-- PDF page 449 -->

Polyolefin manufacturing is a huge industry that comprises the majority of global polymer production. The 2021 world market size was US$ 278 billion, and the 2030 projected market size varies from US$ 438 to 604 billion, depending on compounded annual growth rate (CAGR) estimates. Small improvements in the design and operation of a polyolefin plant can produce significant economic payback.

For most of my career, I have worked on the development of computer models of chemical processes. Beginning with my work with the Advanced System for Process Engineering (ASPEN) Project at MIT, my team later formed Aspen Technology, Inc., to develop the chemical industry's first computer-based modeling and simulation technology. Over the past four decades, I have fond memories of many transformative solutions developed by my colleagues at AspenTech that have helped a variety of industries run their businesses in a safe, profitable, and sustainable manner. In particular, in 1997, two of my former doctoral students at MIT and later R&D staff at AspenTech, Chau-Chyun Chen and Michael Barrera (Michael happened to be a senior in design courses and undergraduate research under Prof. Y. A. Liu at Virginia Tech), and others developed a groundbreaking patent for the segment-based modeling methodology and the associated software tool, Polymers Plus (now called Aspen Polymers), for polymerization processes. This methodology has become the foundation of polymerization process modeling and product design over the past 25+ years.

In early 1999, Prof. Liu at Virginia Tech and his graduate students, working closely with AspenTech's polymer process modeling team, started a multiyear industrial outreach effort to promote sustainable design, operation, and optimization of commercial polymer production processes at companies such as Honeywell Specialty Materials and China Petroleum and Chemical Corporation (SINOPEC). In addition to generating significant cost savings and payback, this effort has resulted in a number of joint AspenTech–Virginia Tech publications in the journal Industrial and Engineering Chemistry Research from 2002 to 2007. Two of those papers (cited as papers 3 and 9 in Chapter 1) have presented the foundational development of the methodology for sustainable design and optimization of polyolefin processes and have become the standard references for subsequent papers on polyolefin process

---

<!-- PDF page 450 -->

modeling, such as polypropylene and high-density polyethylene, reported in the literature. Their work with step-growth polymers resulted in a textbook, “Step-Growth Polymerization Process Modeling and Product Design” (Wiley, 2008).

In 1997, Y. A. worked with SINOPEC to establish a training center in Beijing co-sponsored by AspenTech. In the following 20-plus years, Y. A. (during his summer and winter university breaks) and the instructors he trained have taught thousands of practicing engineers to use fundamental process modeling and advanced process control to promote sustainable engineering with the latest software tools. They have also led engineering teams to develop steady-state and dynamic simulation models of petrochemical processes, including essentially all of the polyolefin production units within SINOPEC. I have visited the training center several times, and the senior executives of SINOPEC have told me that the training has been invaluable to the Chinese petrochemical industries.

The COVID pandemic has prevented Y. A. from dedicating his university breaks to training practicing engineers in China over the past three years. I applaud the wise decision of Y. A. and his graduate student, Niket Sharma, to devote the last three years to studying the literature, running workshop examples, and writing the manuscript for the current textbook. They are doing a great professional service by sharing with the new generation of students, engineers, and scientists the many years of knowledge and insights of the Virginia Tech team in performing creative research and industrial training in polyolefin process modeling and advanced control (see Chapters 1–8). I also praise their effort in adding a significant section on recent developments in multivariate statistics and machine learning, together with their applications to chemical and polymer processes, particularly polyolefin manufacturing. They have achieved their goal very well, having prepared an overview of multivariate statistics and machine learning for university students and faculty, practicing engineers and scientists who are new to the field, and also for those who are knowledgeable but wish to know the new developments and application literature in chemical and polymer processes (see Chapters 9–11).

A unique strength of this book is that it includes 42 hands-on workshops of industrial applications, teaching the readers how to apply easy-to-use commercial software tools and Python machine learning codes to develop quantitative models for sustainable design, control, and optimization of polyolefin processes based on mostly actual plant data. These workshops discuss the very practical problems of how to work with real data, how to develop the right level of detail for the problem you are solving and the data you have, and how to tune the model to plant data. The book contains numerous literature references up to 2022. Individuals who wish to contribute to the development of sustainable design and operation of polyolefin processes or explore new directions will find the review of existing work valuable.

Overall, this book by Y. A. and Niket represents a major advance by enabling students and engineers who are not experts to develop and use state-of-the-art computer models for simulating and optimizing polyolefin processes to make them safer, more sustainable, and more profitable. Both step-growth polymers (e.g. Nylon and PET) and polyolefins (PE, LDPE, HDPE, PP, etc.) represent about 70% of the commercial polymer production. The contributions by Y. A. and his students, through their two

---

<!-- PDF page 451 -->

textbooks on step-growth polymers and polyolefins, to sustainable design education and practice in polymer manufacturing are truly unique and significant.

By Lawrence B. Evans

Professor Emeritus of Chemical Engineering

Massachusetts of Institute of Technology

Founder, Aspen Technology, Inc.

Member, National Academy of Engineering

Past President, American Institute of

Chemical Engineers

---

<!-- PDF page 452 -->

I am happy to write this foreword of a timely and significant textbook, Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing, written by Prof. Y. A. Liu and his graduate student, Niket Sharma.

Concerning my expertise and background in writing this Foreword, I was active for 34 years, from 1985 to 2017, in teaching, research, and industrial outreach as a faculty member at the Technical University of Denmark. In 2018, I started my own consulting work related to process system engineering, and I continue to serve as an adjunct faculty at several universities in the United States and Asia. I was fortunate to serve as Editor-in-Chief of Computers and Chemical Engineering (2009–2015) and President of European Federation of Chemical Engineering (2015–2018), both of which have given me a global perspective of scholarly achievements, research trends, and industrial opportunities in our profession. Among my research interests over the years have been the development and application of computer-aided methods and tools for modeling, including thermodynamic modeling and property estimation, steady-state and dynamic process simulation, and machine learning and big data analytics. With this background, I find the focus of the current textbook particularly timely and significant, covering the latest advances in fundamental research and industrial applications of integrated process modeling, advanced control, multivariate statistics, and machine learning for optimizing polyolefin manufacturing.

In 2010, following my seminar visit to Virginia Tech, my team at the Technical University of Denmark collaborated with Y. A.'s team at Virginia Tech, and in 2011, we published an article on the selection of prediction methods for thermodynamic properties for process modeling and product design of biodiesel. Through this collaboration, I became well aware of Y. A.'s continuing effort to devote his university breaks since 1997 to training practicing engineers and scientists in the United States and Asia to promote sustainable design and practice. Y. A. and the instructors he trained have led project teams to develop the steady-state and dynamic simulation models of essentially all of the polyolefin production units within SINOPEC. These models, validated with plant data, enable the engineers to quantitatively investigate the impact of new operating conditions on product yield, energy consumption, waste generation, and polymer quality (e.g. melt index and molecular weight) and identify the desired operating conditions to produce new polymer grades while minimizing the generation of off-specification wastes. In this text, Y. A. and his Virginia Tech

---

<!-- PDF page 453 -->

team are sharing their years of knowledge and experiences gained from their creative research and industrial training in process modeling and advanced control of polyolefins.

A review of process modeling in Chapters 1–7 will find, among other topics: a detailed introduction of the segment-based methodology for modeling polymer processes; the workflows to develop both steady-state and dynamic simulation models; instruction of advanced equations of state and activity coefficient models applicable to polyolefin processes, and how to choose an appropriate thermodynamic model and estimate the relevant parameters from routine measurements; detailed reviews of the polymerization kinetics literature and recommendation of the appropriate kinetic models for different polyolefin productions, together with the methodology for kinetic parameter estimation from plant data using efficient software tools; guidelines to accelerate the convergence of the simulation of large commercial polyolefin processes with product separations and recycle loops; how to convert a steady-state simulation model to a dynamic simulation model and incorporate appropriate PID controllers to improve process operability and safety; and hands-on application workshops incorporating actual plant data to teach the reader how to design and optimize polyolefin processes with improved safety, profit, and sustainability.

To my knowledge, Chapter 8 is the most detailed introduction currently available to the basic concepts and software implementation of third-generation dynamic matrix control (DMC3) and nonlinear model-predictive control applied to polymer processes. The authors explain the three key steps of linear and nonlinear model identification, steady-state economic optimization, and dynamic controller simulation with step-by-step illustrations of software implementation for a copolymerization reactor and a polypropylene reactor. In particular, this chapter gives clear and explicit explanations of all the key parameters in model identification, economic optimization, and dynamic control so that a beginner in advanced process control can develop and fine-tune model-predictive controllers.

Concerning Chapters 9–11, I enthusiastically endorse the authors' view that any new textbook on process modeling and advanced control cannot ignore two important trends: (1) the tremendous advances in artificial intelligence (AI), particularly machine learning (ML), and big data analytics over the past 20 years; and (2) the growing importance of integrating science-guided fundamental models with data-based machine learning in a hybrid science-guided machine learning (SGML) approach to modeling chemical and polymer processes. In fact, in 2021, my colleagues and I published a paper on hybrid data-driven and mechanistic modeling approaches for multiscale material and process design, and I fully appreciate the importance of a SGML approach to modeling chemical and polymer processes, as presented in Chapter 11. In these chapters, Y. A. and Niket have done a fine job of preparing an overview of fundamentals and practice of multivariate statistics and machine learning with hands-on application workshops for optimizing polyolefin manufacturing. These chapters will be beneficial to students, faculty, engineers, and scientists who are new to the field, and also for those who are knowledgeable.

---

<!-- PDF page 454 -->

but wish to know the new developments and application literature in chemical and polymer processes.

I believe that this book belongs in a class by itself in providing a thorough coverage of the fundamentals of integrated process modeling, advanced control, and data analytics and illustrating their applications in 42 hands-on workshops with realistic plant data from polyolefin industries. Above all, it is a pleasure to read, and I congratulate Y. A. and Niket for completing this fine text.

By Rafiqul Gani

Professor of Chemical Engineering

Technical University of Denmark (1985–2017)

Co-founder and President, PSE for SPEED Company

Thailand–Denmark (since 2018)

Former Editor-in-Chief Computers and Chemical Engineering Journal

Past President, European Federation of Chemical Engineering

Recipient, AIChE Computing in Chemical Engineering

Award (2015) and Sustainable Engineering

Research Award (2020), and the IChemE Sargent Medal (2021)

---

<!-- PDF page 455 -->

It is a pleasure to write a foreword for this important new text, Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing, by Y. A. Liu and Niket Sharma. This book goes well beyond isolated fundamentals available mostly piecemeal in the literature and presents essentially all the relevant fundamental and empirical modeling techniques needed to quantify the steady-state and dynamic behavior of complex industrial manufacturing processes as well as the properties of the polymer products that they produce.

More than two decades ago, I embarked on a journey of discovering and learning about the fascinating world of polymer chemistry and engineering at Virginia Polytechnic Institute and State University. In 1999, I had the privilege of joining Y. A.'s research group as a doctoral student in chemical engineering, studying advanced polymerization process modeling. In collaboration with Aspen Technology as well as manufacturers such as Honeywell, SINOPEC, Formosa Plastics, and PetroChina, we consolidated and advanced fundamental process modeling technology and applied it to develop detailed steady-state and dynamic engineering models for entire polymerization production trains. We successfully used these models to identify process improvements that created new value and trained many professional engineers to develop and use their own process models based on fundamentals. Y. A.'s work in step-growth polymerization process modeling culminated in a joint text titled Step-Growth Polymerization Process Modeling and Product Design (Wiley, 2008).

In 2007, I joined the Dow Chemical Company, a world leader in polyethylene production. I enjoyed opportunities to work as a specialist in the modeling and simulation group within the corporate engineering organization, as an operations engineer in a polyolefins plant that produced both high-volume commodity polyethylene as well as specialty polyolefins, and as a global advanced control engineer for the solution polyethylene process technology. I currently serve as Global Process Automation Director within the Packaging and Specialty Plastics Technology Center. My experiences and current responsibilities have put me as well as my colleagues in a unique position to benefit greatly from Y. A.'s many decades of work.

The new text by Y. A. and Niket begins with the needed science and engineering fundamentals to create flowsheet models for polyolefin manufacturing processes. They extensively cover the physical property framework for modeling single component as well as mixture properties. Their description of the

---

<!-- PDF page 456 -->

segment-based methodology for tracking polymers allows engineers to follow later developments such as those for polymer-specific activity coefficient models and equations of state as well as models for polymerization mechanisms and kinetics. They also cover techniques for building models for polymer product properties. As in the text on step-growth polymerization, Y. A. and Niket illustrate how to apply these fundamentals in Aspen Plus, showing the user how to select the correct physical property models, how to regress physical property parameters, and how to build reaction mechanisms and characterize kinetics. When combined with traditional unit operation models, such as those for continuous stirred-tank reactors, plug-flow reactors, and phase equilibrium separators, it becomes possible for the user to build their own train models. The next several chapters show how to apply these fundamentals to model production processes, using concrete instructions, for low-density polyethylene, ethylene-vinyl acetate, high-density polyethylene, polypropylene, linear low-density polyethylene, and ethylene propylene diene monomer, polystyrene, styrene butadiene styrene rubber, and more (Chapters 1–6).

After teaching readers about the fundamentals of polymerization process modeling and applying them to both steady-state and dynamic models, Y. A. and Niket proceed to demonstrate how to use the models to improve both steady-state operating conditions as well as optimize grade transitions (Chapter 7). They then turn their attention to advanced process control, demonstrating how to use both dynamic matrix control as well as nonlinear control. Both topics are thoroughly explored using examples from a solution copolymerization reactor as well as a polypropylene reactor (Chapter 8).

Perhaps the most significant section of Y. A. and Niket's text relevant to digital manufacturing initiatives is that on applying multivariate statistics and machine learning to create value in polymer manufacturing processes in Chapters 9–11. The authors introduce the reader to many multivariate statistics and machine learning technologies, including simple regressions, dimensionality reduction and clustering methods, ensemble methods, and deep neural networks. They also include illustrative examples for developing models and guide the user on how to choose the most appropriate technology. Last, there is a chapter on hybrid modeling, where Y. A. and Niket blend first principles based and machine learning models to realize the benefits of both fundamental and empirical models. This technique is promising for developing high-performance models of manufacturing processes that are at the same time complex and suffer from a lack of data to fully characterize the underlying physics and chemistry.

I highly recommend this text for both applied research and development specialists as well as manufacturing engineers who work in either engineering or automation. I also enthusiastically recommend this text for senior and graduate students and university faculty who wish to learn the fundamentals and practice of polymer process modeling, control, and machine learning applied to polyolefins. It teaches the fundamentals and shows how to apply them using clear, step-by-step instructions applied to realistic case studies. I have no doubt that significant value can be realized, especially for industrial practitioners, by understanding and applying the

---

<!-- PDF page 457 -->

techniques outlined herein. I wholeheartedly wish to thank Y. A. and Niket for making this excellent effort to aggregate and document not only the key contributions to the field of computer-aided design, simulation, and control of polyolefin manufacturing processes but also their own work in the last decade to advance both theory and practice.

By Kevin C. Seavey

Global Process Automation Director

Packaging and Specialty Plastics Technology Center

The DOW Chemical Company

---

<!-- PDF page 458 — MISSING, not yet parsed -->


---

<!-- PDF page 459 -->

## Preface

Addition and step-growth polymerizations are two major routes for producing commercial polymers. The majority of commercial polymers are addition polymers, of which the most important are polyolefins. Examples of polyolefins are low-density polyethylene (LDPE), high-density polyethylene (HDPE), polypropylene (PP), and their copolymers, such as ethylene-vinyl acetate (EVA), ethylene-propylene copolymer (EPM), and ethylene-propylene-diene terpolymer (EPDM). Additionally, we include polystyrene (PS) and its copolymers, such as poly(styrene-butadiene-styrene) or SBS rubber, as polyolefins (see the introduction to Chapter 6). Together, polyolefins represent approximately 50% of commercial polymer production. Step-growth polymers, such as nylon-6, nylon-66, poly(ethylene terephthalate) (PET), polyurethane, and polylactide, represent approximately 20% of commercial polymer production. This book focuses on polyolefins.

Industrial polymer producers have been modeling polymerization processes for decades. Steady-state and dynamic process models, validated by experimental and plant data, can be helpful to quantitatively: (1) investigate the effects of changing feed, catalyst, reaction, and separation conditions on polymer yields and properties; (2) achieve sustainability by minimizing energy consumption and waste by predicting optimal operating conditions for existing plants; (3) identify the operating conditions to produce new sustainable product grades of desired properties (e.g. polymer density and melt-flow rate or melt index); and (4) study different control schemes and choose one that is optimal for safety and operations.

In our 2008 Wiley textbook, Kevin C. Seavey and Y. A. Liu, Step-Growth Polymerization Process Modeling and Product Design, we have demonstrated that the successful modeling of industrial polymer production processes requires an integrated, quantitative consideration of physical property and thermodynamic modeling, polymerization reaction kinetics, transport phenomena, computer-aided design, and process dynamics and control. Our previous text also provided examples and step-by-step tutorials for user-friendly, hands-on software tools for implementing this integrated quantitative approach, such as Aspen Polymers, Aspen Plus Dynamics, and Aspen Custom Modeler. These tools can be very useful to faculty and students in academia and practicing engineers and scientists in industry.

---

<!-- PDF page 460 -->

Our research to develop the simulation and optimization models for sustainable polyolefin processes since 2000 has benefited greatly from studying apparently the only two available books on the topic: (1) N. A. Dobson, R. Galvan, R. L. Lawrence, and M. Tirrell, Polymerization Process Modeling, VCH (1996) and (2) J. B. P. Soares and T. F. L. McKenna, Polyolefin Reaction Engineering, Wiley-VCH (2012). The former book does a great job of describing polymerization kinetic mechanisms, but it includes only 13 pages of heterogeneous coordination (Ziegler-Natta) polymerization for polyolefins; the latter book includes excellent descriptions of polyolefin reaction engineering, but it has only 13 pages of developing models of industrial reactors. It was encouraging, however, to learn on page 323 of Soares and McKenna about their positive view of our two papers applying our integrated, quantitative approach to polyolefin process modeling that: “The two articles by Khare et al. (2002, 2004) (cited as Refs. [3, 9] in Chapter 1) provide an interesting overview of a simplified approach that can be used to model an entire process for an HDPE slurry process, and a gas-phase PP process using a commercial simulation package. They demonstrate the type of information required and the fact that a certain amount of process improvement can be obtained using well-defined, but manageable, reactor and unit operation models.”

Over the past 20 years, there have been hundreds of papers describing the advances in physical property modeling and prediction, polymer thermodynamics models, polyolefin reaction kinetics, kinetic parameter estimation, multiphase reactor modeling, and model-predictive control applied to polyolefin processes. Unfortunately, we cannot find a single textbook that covers these advances in polyolefin process modeling, optimization, and control and introduce those important ones for the benefit of university faculty and students, as well as industrial practitioners and scientists. This lack of a potentially valuable resource motivated us to write the current textbook.

However, any new textbook on process modeling and advanced control cannot ignore two important trends: (1) the tremendous advances in artificial intelligence (AI), particularly machine learning (ML), and in big data analytics over the past 20 years; and (2) the growing importance of integrating science-guided fundamental models with data-based machine learning in a hybrid science-guided machine learning (SGML) approach to modeling chemical and polymer processes.

In a thoughtful article published in the AIChE Journal in 2019, V. Venkatasubramanian (cited as Ref. [25] in Chapter 10) gives an excellent perspective on the evolution of AI in chemical engineering. He divides the historical development up to the present into three phases: phase I – expert system era (~1983 to ~1995); phase II – neural network era (~1990 to ~2008); and phase III – data science and deep learning era (~2005 to present). It is truly amazing that new developments in ML over the past two decades have touched every aspect of chemical industries. In a June 2022 article, also published in the AIChE Journal, Leo Chiang and his colleagues at DOW Chemical (cited as Ref. [32] in Chapter 10) give convincing evidence that the time for AI, particularly ML, in chemical industries has finally arrived. Additionally, in a May 2022 review published in the AIChE Journal (cited as Ref. [31] in Chapter 10), we presented a broad perspective on hybrid process

---

<!-- PDF page 461 -->

modeling combining the scientific knowledge and data analytics in bioprocessing and chemical engineering with a SGML approach. We have also presented examples demonstrating the increased prediction accuracy and enhanced extrapolative ability of the SGML models for polyolefin-manufacturing processes.

Therefore, this textbook also covers the applications of big data analytics, particularly multivariate statistics and machine learning, to optimizing polyolefin manufacturing in Chapters 9–11.

The contents of our eleven chapters are as follows:

1. Introduction to Integrated Process Modeling, Advanced Control, and Data Analytics in Optimizing Polyolefin Manufacturing

2. Selection of Property Methods and Estimation of Physical Properties for Polymer Process Modeling

3. Reactor Modeling, Convergence Tips, and Data-Fit Tool

4. Free Radical Polymerizations: LDPE and EVA

5. Ziegler–Natta Polymerization: HDPE, PP, LLDPE, and EPDM

6. Free Radical and Ionic Polymerizations: PS and SBS Rubber

7. Improved Polymer Process Operability and Control Through Steady-State and Dynamic Simulation Models

8. Model-Predictive Control of Polyolefin Processes

9. Application of Multivariate Statistics to Optimizing Polyolefin Manufacturing

10. Applications of Machine Learning to Optimizing Polyolefin Manufacturing

11. A Hybrid Science-Guided Machine Learning Approach for Modeling Chemical and Polymer Processes

In these chapters, we have included 42 hands-on workshops of industrial applications, teaching the readers how to apply easy-to-use commercial software tools and Python ML codes to develop quantitative models for sustainable design, operation, control, and optimization of polyolefin manufacturing processes, mostly based on real plant data. We provide all simulation files for our workshops in the Supplement Material. We also include two appendices in our book: Appendix A, matrix algebra in multivariate data analysis and model-predictive control in MATLAB and Python; and Appendix B, introduction to Python for chemical engineers.

From 1992 to the COVID-19 pandemic in 2020, the senior author has devoted his university breaks to industrial outreach at three global top 10 chemical companies (SINOPEC, Formosa Plastics, and PetroChina). He and the instructors he trained have taught thousands of engineers to apply our approach of integrating fundamental principles, industrial applications, and hands-on workshops using user-friendly, commercial software tools for the development and implementation of sustainable design, operation, and control models for polyolefin processes. According to a published SINOPEC report in the February 2014 issue of the CCIESC Journal (cited as Ref. [13] in Chapter 1), the teams trained by the senior author have completed modeling projects that resulted in an annual payback of over US$ 115.5 million for a total investment of less than US$ 10 million from 2002 to 2012. This training has included much of the polyolefin topics covered in the present text. Our trainees find our materials, particularly the hands-on workshops, easy to learn and very useful for their

---

<!-- PDF page 462 -->

industrial practice. Another motivation for writing this text is to share with the new generation of students, engineers, and scientists our years of knowledge and insights in advising and training project teams for the modeling, control, and optimization of industrial polyolefin processes.

Our review of currently available materials has failed to find any text that encompasses the broad range of process modeling, advanced control, and data analytics and emphasizes our approach of integrating fundamental principles, industrial applications, and hands-on workshops, which we focus on in this book. We hope this text will be beneficial to undergraduate and graduate students and faculty in chemistry and chemical, material, and polymer engineering, as well as practicing engineers and industrial scientists in polyolefin industries.

December 2022

Y. A. Liu and Niket Sharma

Virginia Polytechnic Institute and State University (“Virginia Tech”), Blacksburg, Virginia

---

<!-- PDF page 463 -->

## Acknowledgment

It is a pleasure to thank a number of very special persons and organizations that contributed to the preparation of this book.

We want to express our sincere gratitude to the following academic and industrial leaders who kindly took time to review our manuscripts and write the foreword for our text: Mr. Willie K. Chan, Chief Technology Officer of Aspen Technology, Inc.; Professor Chau-Chyun Chen, Hord Distinguished Professor of Texas Tech University and an inventor of the segment-based modeling technology for polymer processes; Dr. Leo H. Chiang, Senior R&D Fellow, DOW, Inc., and a top industrial leader of machine learning and big data analytics in chemical industries; Professor Lawrence B. Evans of Massachusetts Institute of Technology and founder of Aspen Technology, Inc.; Professor Rafiqul Gani of the Technical University of Denmark and Co-founder and President, PSE for SPEED, Bangkok, Thailand; and Dr. Kevin C. Seavey, Global Process Automation Director, Packaging and Specialty Plastics Technology Center, DOW, Inc.

We would like to thank the China Petroleum and Chemical Corporation (SINOPEC) and Aspen Technology, Inc., for challenging us to enter the field of polymerization process modeling by assigning us the task of developing a training program for polymerization process modeling for practicing engineers in 1998. We thank Mr. Cao Xianghong, Senior Vice President and Chief Technology Officer (retired) of SINOPEC, for his strong support over the past 30 years. We are grateful to Mr. Wilfred Wang, Board Chairman of Formosa Petrochemical Corporation, for his strong partnership during 2008–2013. We also thank Mr. He Shengbao, Chief Engineer, PetroChina Refining and Chemical Company and President of the PetroChina Petrochemical Research Institute, for his strong support in recent years.

We wish to thank Aspen Technology, Inc., for their support of the Center of Excellence in Process System Engineering in the Department of Chemical Engineering at Virginia Tech since 2002. We thank Dr. Lawrence B. Evans, Founder and former CEO; Mr. Antonio Pietri, CEO; Mr. Willie K. Chan, Chief Technology Officer; Dr. Steven Qi, Senior Vice President, Customer Success; Mr. David Reumuth, Senior Director, Customer Support and Training; and Mr. Daniel Clenzi, Director of University Programs of Aspen Technology, Inc., for their strong support.

We are grateful to Professor Chau-Chyun Chen, Texas Tech University; Mr. David Tremblay, Aspen Technology, Inc.; and Ms. Caijuan Yang and Mr. Dengzhou Song,

---

<!-- PDF page 464 -->

Petro-CyberWorks Information Technology Co., for sharing their expertise in polymer process modeling with us over the years. We thank Professor W. Harmon Ray, University of Wisconsin, for his many inspiring papers on polyolefin reaction engineering.

We would like to express our sincere appreciation to the help by the experts in process modeling, advanced process control, and machine learning and hybrid modeling at Aspen Technology, in particular: Yuhua Song, Lori Roth, Paul Turner, Alex Kalafatis, Krishnan Lakshminarayan, Ashok Rao, Ron Beck, and Gerardo Munoz.

Finally, we wish to thank Dr. Cyril Clarke, Executive Vice President and Provost at Virginia Tech, for his strong support and encouragement of the preparation of this textbook over the past three years and to our graduate students, Aman Agarwal, James Nguyen, and Adam McNeeley, for their invaluable assistance in the preparation of this book.

The junior author would like to thank his parents, Rekha Sharma and Raj Kumar Sharma, and the rest of his family, friends, and well-wishers for their continuing support throughout his graduate studies. The senior author would like to thank his wife, Hing-Har Lo Liu, for her support through the laborious process of this book writing and revision.

---

<!-- PDF page 465 -->

## Copyright Notice

References and screen images of Aspen Plus $ ^{\circledR} $, Aspen Polymers $ ^{\text{TM}} $, Aspen Plus Dynamics $ ^{\text{TM}} $, Aspen DMCplus $ ^{\text{TM}} $, Aspen DMC3 $ ^{\text{TM}} $, Aspen DMC3 Builder $ ^{\text{TM}} $, Aspen Nonlinear Controller $ ^{\text{TM}} $, Aspen Maestro $ ^{\text{TM}} $, Aspen Transition Management $ ^{\text{TM}} $, Aspen InfoPlus 21 $ ^{\text{TM}} $, aspenONE Process Explorer $ ^{\text{TM}} $, Aspen ProMV $ ^{\circledR} $, Aspen AI Model Builder $ ^{\text{TM}} $, and Aspen Multi-Case $ ^{\text{TM}} $ are reprinted with permission from Aspen Technology, Inc. The names of all products listed are trademarks of Aspen Technology, Inc. All rights reserved.

All of these software products are available from Aspen Technology, Inc., Bedford, Massachusetts (www.aspentech.com).

---

<!-- PDF page 466 — MISSING, not yet parsed -->


---

<!-- PDF page 467 -->

## About the Authors

Y. A. Liu, the Alumni Distinguished Professor and the Frank C. Vilbrandt Endowed Professor of Chemical Engineering at Virginia Tech, received his BS, MS, and PhD degrees from National Taiwan University, Tufts University, and Princeton University, respectively. His current interests in teaching, research, and industrial outreach are sustainable design, process modeling, big data analytics, and energy and water savings.

Liu has taught the capstone design courses for graduating seniors in chemical engineering since 1974, focusing on sustainable design and practice and industrial sustainable design projects. The American Society for Engineering Education honored Liu with the George Westinghouse Award for excellence in engineering education and the Fred Merryfield Design Award for excellence in teaching and research in sustainable design. The Chemical Manufacturers Association honored Liu with the National Catalyst Award for excellence in chemical education. The American Institute of Chemical Engineers (AIChE) honored Liu with the Outstanding Student Chapter Advisor Award, chosen from 380 student chapters across 54 countries, for his excellence in developing leadership and professionalism and creating enthusiasm for public service among undergraduates since 1995.

AIChE honored Liu's research and industrial outreach on sustainable design and practice with the Professional Achievement Award for Innovations in Green Process Engineering, and the Excellence in Process Development Research Award. He made special efforts to publish a substantial body of knowledge and insights about industrial applications of his research in eight groundbreaking textbooks. These books present the methodologies for: (1) industrial water savings; (2) sustainable design of polymer, refining, and adsorptive and chromatographic separation processes; and (3) intelligent design by artificial intelligence and neural computing in bioprocessing and chemical engineering. His textbooks have included 150 hands-on workshops targeted toward teaching undergraduate seniors, graduate students, and practicing engineers how to apply software tools for sustainable design and optimization.

He received the Distinguished Alumni Award and the Outstanding Career Achievement Award from Tufts University. He is a Fellow of the AIChE and a Fellow of the American Association for the Advancement of Science, cited “for excellence in design teaching, pioneering textbooks and creative scholarship in

---

<!-- PDF page 468 -->

sustainable engineering, and global leadership in implementing energy/water savings and  $ CO_{2} $ capture."

From 1986 to the worldwide pandemic in 2020, he devoted his university breaks helping petrochemical industries in developing countries and chemical industries in Virginia with technology development and engineering training. He has taught intensive training courses on computer-aided design, advanced process control, energy and water savings, and refinery and polymerization process modeling in China, Taiwan, and the USA. Liu and the instructors he trained have taught 7500 practicing engineers in courses sponsored by Aspen Technology, SINOPEC, PetroChina, Formosa Plastics Group, Honeywell, etc. For his effective blend of sustainable design education, research, and industrial outreach, he has received the Outstanding Faculty Award from Virginia's Governor, the National Friendship Award from China's Premier, and one of the U.S. Professors of the Year Awards from the Carnegie Foundation for the Advancement of Teaching and the Council for Advancement and Support of Education.

Niket Sharma received his PhD in chemical engineering and MEng in computer science with a specialization in machine learning from Virginia Tech in 2021. He is currently a senior engineer at Aspen Technology, Boston, where he is working on the development of machine learning and hybrid modeling applications combining chemical engineering and data science principles. His PhD dissertation focused on integrated process modeling and big data analytics for optimizing polyolefin manufacturing. During his PhD studies, he worked on developing an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data, for which he won the 2020 Process Development Student Paper Award from the American Institute of Chemical Engineers.

He had five years of industrial experience prior to joining graduate school at Virginia Tech. He has worked with SABIC for four years as a research engineer, where he worked on process development, scale-up, process modeling, and experiments measuring reaction kinetics and polymerization. He has also worked for a year with Indian Oil Corporation as a production engineer in the oil refinery. Niket also obtained a MEng (Chemical) from the Indian Institute of Science in 2013.

Niket is passionate about chemical engineering and the application of data science in diverse domains and wants to publish quality literature for practitioners in the industry.

---

<!-- PDF page 469 -->

## About the Companion Website

Integrated Process Modeling, Advanced Control and Data Analytics for Optimizing Polyolefin Manufacturing is accompanied by a companion website:

www.wiley-vch.de/ISBN9783527352678

<div style="text-align: center;"><img src="imgs/img_in_image_box_521_502_585_563.jpg" alt="Image" width="6%" /></div>


The website includes:

• Example and workshop files

Scan this QR code to visit the companion website.

<div style="text-align: center;"><img src="imgs/img_in_image_box_359_699_575_914.jpg" alt="Image" width="22%" /></div>


---

<!-- PDF page 470 — MISSING, not yet parsed -->
