# 11. A Hybrid Science-Guided Machine Learning Approach

<!-- PDF page 741 -->

## A Hybrid Science-Guided Machine Learning Approach for Modeling Chemical and Polymer Processes

This chapter presents a broad perspective on hybrid modeling combining scientific knowledge and data analytics in chemical and polymer processes with a science-guided machine learning (SGML) approach. Section 11.1 introduces the hybrid SGML approach and describes our motivation for writing this chapter. Section 11.2 gives a review of the broad applications of hybrid SGML approach in chemical engineering. As the number of reported methodologies and applications continues to rise significantly, it is hard for a person unfamiliar with the subject to identify the appropriate approach for a specific application. This leads to our key focus in Sections 11.3–11.5, beginning with a systematic classification and exposition of hybrid SGML methodologies in Section 11.3. We divide the approach into two major categories: ML complements science, and science complements ML. Section 11.4 explains different categories of applying ML to complement science-based models and presents expositions of direct serial and parallel hybrid modeling and their combinations, inverse modeling, reduced-order modeling, quantifying uncertainty in the process, and even discovering governing equations of the process model. We discuss their requirements, strengths, and limitations, suggest potential areas of application, and present illustrative workshops from polyolefin manufacturing. Section 11.5 focuses on different categories of applying scientific principles to complement ML models. We discuss the science-guided design, learning, and refinement together with their requirements, strengths, and limitations, as well as their potential applications and application workshops to polyolefin manufacturing. Section 11.6 presents a workshop on a reduced-order model (ROM) for a polystyrene process using Aspen Multi-Case and Aspen AI Model Builder. Section 11.7 describes the challenges and opportunities for a hybrid SGML approach for modeling chemical and polymer processes. Section 11.8 summarizes our conclusions. The chapter also presents a reference section. Throughout this chapter, we use PYTHON codes in several workshops. We refer the interested reader to Appendix B of this text, which presents an introduction to Python for chemical engineers.

We thank Wiley publishers for granting us permission to prepare this chapter as an expanded version of our 2022 article, Sharma and Liu [1]. We have included the details of all applications to polyolefin manufacturing as workshops.

---

<!-- PDF page 742 -->

### 11.1 Introduction

Modeling of many physiochemical systems requires detailed scientific knowledge of the system, which is not always feasible for complex processes. We make some assumptions when modeling the system with first principles that ultimately lead to some knowledge gaps in describing the original system. Even for systems where the scientific knowledge is sufficient to model the system, there is limited data to estimate the multiple parameters of a first-principle model. We often apply data-based models to study systems where scientific data are available since they are more accurate in prediction. However, data-based/machine learning models are black-box models, which can overfit the data and also produce scientifically inconsistent results. For better accuracy, ML models also require more data, which is not always feasible for many problems. Therefore, it is important to integrate science-based knowledge and data-based knowledge for an accurate and scientifically consistent prediction, which we will refer to as hybrid SGML approach.

The most popular hybrid SGML approach that is being practiced in different fields of science is to combine a data-based ML model with a science-based first-principle model. However, there are more ways to combine scientific knowledge and data-based knowledge. In this work, we focus on both aspects of science complementing ML and ML complementing science.

In our development of the hybrid SGML approach, we have benefited from two latest references. In their 2017 article, Karpatne et al. [2] suggest theory-guided data science as a new paradigm for scientific discovery from data. They classify the theory-guided data science methods into different categories, such as theory-guided design of models, initialization, theory-guided refinement of data science outputs, hybrid models of theory of data science, and augmenting theory-based models using data science. In their 2020 article, Willard et al. [3] classify the integration of physics-based modeling with ML methodology according to the modeling objectives. The latter include, for example, improving the predictions beyond physical models, downscaling the complexity of physics-based models, generating data, quantifying uncertainty, and discovering governing equations of the data-based model.

The objective of this chapter is to present a review and exposition of scientific and engineering literature relating to the hybrid SGML approach and propose a systematic classification of hybrid SGML models focusing on both science complementing ML models and ML complementing science-based models. This work differentiates itself from several recent reviews of hybrid modeling in bioprocessing and chemical engineering through the following contributions: (1) presentation of a broader hybrid SGML methodology of integrating science-guided and data-based models, and not just the direct combinations of first-principle and ML models; (2) classification of the hybrid model applications according to their methodology and objectives instead of their areas of applications; (3) identification of the themes and methodologies, which have not been explored much in bioprocessing and chemical engineering applications, like the use of scientific knowledge to help improve the ML model architecture and learning process for more scientifically consistent solutions; and (4) illustrations of the use of these hybrid SGML methodologies applied to industrial polymer processes, such as inverse modeling and science-guided loss, which have not previously been applied in such applications.

---

<!-- PDF page 743 -->

### 11.2 Applications of Hybrid SGML Approach in Chemical Engineering

The integration of science-based models with data-based models has appeared in various fields like fluid mechanics [4], turbulence modeling [5], quantum physics [6], climate science [7], geology [8], and biological sciences [9].

This study focuses on applications of hybrid SGML methodologies in bioprocessing and chemical engineering. Among the earliest applications is the direct hybrid modeling involving the integration of first-principle model with data-based neural networks  $ [10] $. Psichogios and Unger  $ [11] $ combine a first-principle model based on prior process knowledge with a neural network, which serves as an estimator of unmeasured process parameters that are difficult to model from first principle. They apply the hybrid model to a fed-batch bioreactor, and the integrated model has better properties than the standard “black-box” neural network models. In particular, the integrated model is able to interpolate and extrapolate much more accurately, is easier to analyze and interpret, and requires significantly fewer training examples. Thompson and Kramer  $ [12] $ later demonstrate how to integrate simple process model and first-principle equations to improve the neural network predictions of cell biomass and secondary metabolite in a fed-batch penicillin fermentation reactor when trained on sparse and noisy process data.

Agarwal [13] develops a general qualitative framework for identifying the possible ways of combining neural networks with the prior knowledge and experience embedded in the available first-principle models and discusses the direct hybrid modeling with series or parallel configuration to combine the outputs of the science-based model and the ML model. Asprion et al. [14] present the term gray-box modeling for optimization of chemical processes. They consider the case where a predictive model is missing for a process unit within a larger process flowsheet and use measured operating data to set up hybrid models combining physical knowledge and process data. They report results of optimization using different gray-box models for process simulators applied to a cumene process. Actually, in a number of earlier studies, Bohlin and his coworkers have explored in detail the concepts of gray-box identification for process control and optimization, and Bohlin has summarized the concepts, tools, and applications of gray-box hybrid modeling in an excellent book [15].

Over the years, we have seen a growing number of applications of hybrid modeling in bioprocessing and chemical engineering as part of the advances in smart manufacturing  $ [16–18] $.

In their 2021 paper, Sansana et al. [17] discuss mechanistic modeling, data-based modeling, hybrid modeling structures, system identification methodologies, and applications. They classify their hybrid model into parallel, series, surrogate models (which are simpler mathematical representations of more complex models and similar to ROMs that we discuss below), and alternate structures (which include gray-box modeling mentioned above). In the alternate structures, they refer to some applications of semi-mechanistic model structures where the best hybrid model is selected using optimization concepts. They also classify the hybrid models based on some of the chemical industry applications into analysis of model-plant mismatch [18], model transfer, feasibility analysis, and predictive maintenance.

---

<!-- PDF page 744 -->

apart from the previously mentioned applications like process control, monitoring, and optimization.

Von Stosch et al. [19] have used the term hybrid semi-parametric modeling in their 2014 review and have summarized applications in bioprocessing for monitoring, control, optimization, scale-up, and model reduction. They emphasize that the application of hybrid semi-parametric techniques does not automatically lead to better results but that rational knowledge integration has the potential to significantly improve model-based process design and operation.

Qin and Chiang [20] review the advances in statistical ML and process data analytics that can provide efficient tools for developing future hybrid models. In a latest paper, Qin et al. [21] propose a statistical learning procedure integrating with process knowledge to handle the challenging problem of developing a predictive model for process impurity levels from more than 40 process variables in an industrial distillation system. Both studies highlight the power of statistical ML for developing future hybrid process models.

A survey of the literature has shown applications of hybrid modeling in bioprocesses [22–28], chemical and oil and gas processing industries [29–33], and polymer processes [34, 35] for more accurate and scientifically consistent predictions. This survey has also shown many topical focuses of applications in bioprocessing and chemical engineering, including process control [36–39], design of experiments (DOE) [40, 41], process development and scale-up [42, 43], process design [44], and optimization [14, 45, 46].

In a recent study, Zhou et al. [47] present a hybrid approach for integrating material and process design that holds much promise in process and product design. Cardillo et al. [48] demonstrate the importance of hybrid models in the in silico production of vaccines to accelerate the manufacturing process. Chopda et al. [24] apply integrated process analytical techniques and modeling and control strategies to enable the continuous manufacturing of monoclonal antibodies. McBride et al. [49] classify the hybrid modeling applications in different separation processes in chemical industry, namely, distillation [50–52], crystallization [53, 54], extraction [55–57], floatation [58, 59], filtration [60, 61], and drying [62]. Venkatasubramanian [63] gives an excellent exposition of the current state of development and applications of artificial intelligence in chemical engineering. The author highlights the intellectual challenges and rewards of developing the conceptual frameworks for hybrid models, mechanism-based causal explanations, domain-specific knowledge discovery engines, and analytical theories of emergence and presents examples from optimizing material design and process operations.

In an excellent edited volume, Glassey and Von Stosch [64] discuss some of the key strengths of hybrid modeling in chemical processes, particularly in the prediction of scientifically consistent results beyond the experimentally tested process conditions, which is crucial for process development, scale-up, control, and optimization. They also identify some challenges. For example, incorrect fundamental knowledge in a science-based model could impose bias on predictions; thus, the underlying

---

<!-- PDF page 745 -->

assumptions used in a model are important for analysis. Also, time and accuracy of parameter estimation are critical when deciding on a hybrid modeling strategy. Kahrs and Marquardt [65] discuss the approach of simplifying the complex hybrid models into sequence of simpler problems, such as data preprocessing, solving nonlinear equations, parameter estimation, and building empirical models using ML.

Herwing and Portner, in their latest book, showcase the applications of hybrid modeling in digital twins for smart biomanufacturing [66].

A recent patent by Chan et al. [67] presents Aspen Technology's approach to asset optimization using integrated modeling, optimization, and artificial intelligence. In a later white paper, Beck and Munoz [68] describe Aspen Technology's current focus on hybrid modeling, combining AI and domain expertise to optimize assets. In particular, based on their application experience in chemical industries, Aspen Tech has classified hybrid models into three categories: AI-driven, first-principle-driven, and ROMs [68]. They define an AI-driven hybrid model as an empirical model based on plant or experimental data and use first principles, constraints, and domain knowledge to create a more accurate model. Examples of AI-driven models are inferential sensors or online equipment models. They define a first-principle-driven hybrid model as an existing first-principle model augmented with data and AI to improve model's accuracy and predictability, which has seen many applications in bioprocessing and chemical engineering. Lastly, they define a ROM where we use ML to create an empirical data-based model based on data from first-principle process simulation runs, augmented with constraints and domain expertise, in order to build a fit-for-purpose low-dimensional model that can run more quickly. With ROMs, we can extend the scale of modeling from units to plant-wide models that can be deployed faster.

### 11.3 A Classification and Exposition of Hybrid SGML Models

As we have seen thus far, the majority of work in hybrid model applications in bioprocessing and chemical engineering focuses on the direct combination of science-based and data-based models. In this chapter, we portray a broad perspective on the combination of scientific knowledge and data analysis in bioprocessing and chemical engineering, as inspired by some of the applications in physics and other areas [2, 3]. We categorize these hybrid SGML applications in chemical process industry into two major categories, namely, ML complements science and science complements ML, together with their sub-categories, based on the methodologies and objectives of hybrid modeling, as illustrated in Figure 11.1. We also classify the applications in bioprocessing and chemical engineering according to our hybrid SGML approach. We present examples in several areas of SGML, which have not been explored much thus far, and which have great potential for process improvement and optimization.

---

<!-- PDF page 746 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_150_812_588.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.1 Classification of hybrid SGML models.</div>


### 11.4 ML Complements Science

We can integrate a first-principle scientific model with a data-based model to improve the model accuracy and consistency. In the following, we introduce the subcategories of direct hybrid modeling, inverse modeling approach, reducing model complexity, quantifying uncertainty in the process, and discovering governing equations.

#### 11.4.1 Direct Hybrid Modeling

A direct hybrid model combines the output of a first-principle or science-based model with the output of a data-based ML model to improve the prediction accuracy of dependent variables. These combinations could occur in a series configuration, a parallel configuration, or a series-parallel configuration. The direct hybrid modeling strategy is the most widely used approach in hybrid modeling in bioprocessing and chemical engineering.

##### 11.4.1.1 Parallel Direct Hybrid Model

Figure 11.2 illustrates the concept of a parallel direct hybrid model. The science-based model may use the initial conditions and boundary conditions as inputs to make a prediction (Ym), whereas the ML model uses dynamic, time-varying data to make the predictions (Yml). We then combine both outputs directly or with assigned weights (w1 and w2) to achieve higher prediction accuracy. We can determine the weights by least-squares optimization to minimize the

---

<!-- PDF page 747 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_152_783_435.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.2 Parallel direct hybrid model: Ym and YML are model predictions, and w1 and w2 are weights.</div>


total sum of squares of errors for the difference between the plant and the hybrid model.

Galvanauskas et al. [69] combine directly the data-based neural networks for kinetics and viscosity predictions with the first-principle mass balance ordinary differential equations to optimize the production rate of an industrial penicillin process. Chang et al. [34] showcase a parallel hybrid model for the dynamic simulation of a batch free radical polymerization of methyl methacrylate. They combine an approximate rate function for the concentration of the immeasurable initiator concentration with a black-box time-dependent or recurrent neural network (RNN) model [10] of the dependent variables representing the mass and moment balance equations of the polymerization reactor. They use the resulting hybrid neural network and rate function (HNNRF) model to optimize the batch polymerization system, identifying the optimal recipe or operating conditions of the batch polymerization system.

Hybrid residual modeling or parallel direct hybrid residual model is a class of the parallel direct hybrid model, where we use a first-principle or science-based process model to quantify the time-dependent prediction error or residual, Yres, between plant data  $ Y(t) $ and science-based model prediction  $ Y_{m} $ as a function of process variables [42, 70–72]. Figure 11.3 illustrates the concept of the parallel direct hybrid residual model. The correction to the model output, taking care of the prediction error or residual of the ML model in the hybrid residual configuration, improves the model accuracy over the nonresidual configuration of Figure 11.2.

We recommend that the use of hybrid models will generally perform better than stand-alone ML model for applications like process development. This follows because hybrid models are better at extrapolation, while stand-alone ML models can be adequate for prediction in a steady running plant.

Tian et al. [70] develop a hybrid residual model for a batch polymerization reactor. First, they develop a simplified process model based on polymerization kinetics and mass and energy balances to predict the monomer conversion, number-average molecular weight (MWN), and weight-average molecular weight (MWW).

---

<!-- PDF page 748 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_149_804_441.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 11.3 Parallel direct hybrid residual model: Ym represents model outputs, Res are the time-dependent prediction errors or residues between plant data Y(t) and science-based model outputs Ym, and Ym + Yres are the corrected model outputs.</div>


This first-principle process model cannot predict these product quality targets accurately because of its neglect of the gel effect at high monomer conversion and other factors. Next, the authors develop a parallel configuration of three data-based, time-dependent, or recurrent neural networks [10] trained by process data to predict the residuals of monomer conversion, MWN, and MWW of the simplified first-principle process model. The predicted residuals are added to the predictions from the simplified process model to form the final hybrid model predictions. Because of focus in batch process control is on the end-of-batch product quality targets, the use of time-dependent or recurrent neural networks can usually offer good long-range predictions. Therefore, the resulting hybrid residual model performs well in many batch process control and optimization applications [42, 44, 70–72].

Simutis and Lübbert [37] present another application of the direct hybrid modeling methodology to state estimation for bioprocess control. This work combines a first-principle state Kalman filter based on mass balances of biomass, substrate and product, and an ML-based observation model for quantifying relationship between less established variables and measurements. Ghosh et al. [73, 74] apply the parallel hybrid modeling framework in process control, where they combined first-principle models with data-based model built by applying subspace identification for better prediction of batch polymer manufacturing and seed crystallization system. Hanachi et al. [75] showcase the application of direct hybrid modeling methodology for predictive maintenance. They combine a physics-based model with a data-based inferential model in an iterative, parallel combination for predicting manufacturing tool wear.

##### 11.4.1.2 Series-Direct Hybrid Model

Figure 11.4 illustrates the series-direct hybrid model. The science-based process model serves to augment the data needs of the ML model, while the ML model can help in estimating the parameters of the science-based model. Babanezhad et al. [76] consider the computational fluid dynamics (CFD) for two-phase flows in chemical

---

<!-- PDF page 749 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_151_779_324.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.4 Series direct hybrid model.</div>


reactors and couple science-based CFD results to a ML model based on an adaptive network-based fuzzy inference system (ANFIS). Once the ML model captures the pattern of the CFD results, they use the hybrid model for process simulation and optimization. Some features calculated from a science-based CFD model can augment the data as inputs to a ML model. Chan et al. [67] have discussed the advantages of data augmentation by combining simulation and plant data to generate a more accurate data-based analysis. In an application to crude distillation in petroleum refining, Mahalec and Sanchez [52] use a science-based model to calculate the internal reflux to augment other plant data as inputs to a ML model in order to calculate the relationship to the product's true boiling point curves for quality analysis. The data augmentation in series hybrid models is more relevant when some feature measurements are missing in the original data, so we use a first-principle model to calculate those features and then augment those calculated data to the ML model to study the combined multivariate effects. The goal is more toward causal effect of the added science model features and less toward improving accuracy. If we find that some missing feature measurements cause a mismatch between a science-based model and the actual plant, data augmentation may improve the training performance of the hybrid model.

Kriplp et al. [77] present the hybrid modeling of an ultrafiltration process where they calculate the flux using a ML model to act as an input to a science-based model. Similarly, Luo et al. [30] develop a hybrid model for a fixed-bed reactor for ethylene oxidation, integrating first-principle reaction kinetics and reactor model with a ML catalyst deactivation model. The latter is developed with support vector regression from operating data, assuming the deactivation property decreases monotonically with time. With the hybrid model, the prediction error is less than 5% for the prediction of an industrial reactor. The approach can predict the production more accurately and have more reliable extrapolation.

Figure 11.4 shows that a ML model can also help in estimating the parameters of the science-based model. Mantovanelli et al. [78] develop a hybrid model for an industrial alcoholic fermentation process, combining first-principle mass- and energy-balance equations for a series of five fermenters with a data-based, functional link network [76] to identify the kinetic parameters of the fermentation reactors trained by plant data. The hybrid model includes the effect of temperature on the fermentation kinetics and shows good nonlinear approximation capability. Sharma and Liu [79] show how to use plant data to estimate kinetic parameters.

---

<!-- PDF page 750 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_147_811_389.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.5 Combined direct hybrid model: Ym are outputs, Yres are residuals, and Ym + Tres are corrected outputs.</div>


of first-principle models for industrial polyolefin processes. In a recent study, Bangi and Kwong [80] estimate process parameters in hydraulic fracturing process using deep neural network (DNN), which are then input to a first-principle model. Finally, we note that, as illustrated in Figure 11.4, we can interchangeably use a science-based model or a ML model first in the hybrid framework, depending on whether we need to add more features to augment the dataset or estimate model parameters.

##### 11.4.1.3 Series-Parallel or Combined Direct Hybrid Model

Figure 11.5 shows a combined direct hybrid model, where we use the steady-state data from the plant to estimate the unknown parameters of a science-based process model and then use the hybrid residual modeling strategy of Figure 11.3 for prediction. This series–parallel combination or feedback system can improve model predictions, depending on the application.

Bhutani et al. [81] present a definitive study comparing first-principle, data-based, and hybrid models applied to an industrial hydrocracking process. In particular, they couple a first-principle hydrocracking model based on pseudocomponents with data-based neural network models of different configurations in Figures 11.3–11.5 that quantify the variations in operating conditions, feed quality, and catalyst deactivation. The neural network component of the hybrid model either provides updated model parameters in the first-principle process model connected in series or corrects predictions of the first-principle process models. The hybrid models are able to represent the behavior of an industrial hydrocracking unit to provide accurate and consistent predictions in the presence of process variations and changing operating scenarios.

Song et al. [82] also apply the direct hybrid model configurations of Figures 11.3–11.5 to an industrial hydrocracking process and analyze the strengths and weaknesses of these configurations. They call a model a mechanism-dominated model if the accuracy of its outputs is mainly dominated by the available theoretical knowledge used to develop the model, and they also call a model a data-dominated model if the accuracy of its outputs is mainly dominated by the quality of the training data and the performance of the resulting data-based model. In particular, they give

---

<!-- PDF page 751 -->

both the first-principle model and the series-direct hybrid model of Figure 11.4 as examples of mechanism-dominated models and cite the data-based model, parallel direct residual model of Figure 11.3, and the combined direct hybrid model of Figure 11.5 as examples of data-dominated models.

In their work, Song et al. [82] combine a mechanism-dominated model with a data-dominated model as a hybrid direct model of Figure 11.2, with the weighting factors for the outputs of two individual models being determined in an adaptive fashion. For their application, Song et al. work with a mechanism-dominated model of an industrial hydrocracking process based on kinetic lumping [81, 82] and with a data-dominated model based on a self-organizing map (SOM) followed by a convolutional neural network (CNN), with being trained by simulated process data based on Aspen HYSYS [82]. They evaluate the performance of the hybrid model for operational optimization of the hydrocracking process producing different product scenarios. While this study includes new conceptual development, it needs much simplification of its relatively complex methodology to make it readily applicable by data scientists and practicing engineers.

In a recent study, Chen and Lerapetritou [18] demonstrate how to use partial correlation analysis from multivariate statistics and mutual information analysis from information theory to identify and improve the plant-model mismatch in using a direct combined hybrid model for a pharmaceutical manufacturing process. As the authors state, implementing this plant-model mismatch strategy requires active excitation of variables online in order to capture the corresponding response data from the plant, which is often difficult to perform in manufacturing plants and in experimental settings and could benefit from new developments in computing and information technology.

Lima et al. [83] propose a semi-mechanistic model-building framework based on selective and localized model extensions. They use a symbolic reformulation of a set of first-principle model equations in order to derive hybrid mechanistic–empirical models. The symbolic reformation permits the addition of empirical elements selectively and locally to the model. They apply the approach to the identification of a nonideal reactor and to the optimization of the Otto–Williams benchmark reactor.

This combined strategy is generally more useful in cases where the science-based model has unknown parameters. We could use ML to determine these unknown parameters and then apply a hybrid residual ML approach. By doing so, we could improve the model prediction accuracy as well.

###### 11.4.1.4 Workshop 11.1: An Application of Combined Direct Hybrid Modeling to Polymer Manufacturing

The objective of this workshop is to predict polymer melt index (MI) using a combined direct hybrid modeling methodology to build a more accurate and scientifically consistent quality sensor.

We apply the combined direct modeling strategy to an industrial polyethylene process for the prediction of MI. We build a first-principle steady-state model of a Mitsui slurry high-density polyethylene (HDPE) process by following the methodology and kinetic parameters presented in Supplement 5.1b of Chapter 5.

---

<!-- PDF page 752 -->

For this application, it is easier to first estimate the complex multisite Ziegler–Natta polymerization kinetic parameters using steady-state production targets (Section 5.5) and then convert the resulting steady-state simulation model based on Aspen Plus to a dynamic simulation model using Aspen Plus Dynamics (Sections 7.7 and 7.8). The resulting dynamic simulation model has similar independent process variables, including the feed flow and compositions and the reactor operating conditions. For less complex applications, dynamic data could be used for parameter estimation. The following equations relate the residue (Res) or the difference between the plant and model values of the MI (MI_Plant - MI_Model) as a function of independent process variables,  $ f(X_{\text{Process}}) $. Additionally, we wish the MI value predicted by the hybrid model, MI_Hybrid, matches the plant value, MI_Plant:

 $$ \mathrm{MI}_{\mathrm{Plant}}-\mathrm{MI}_{\mathrm{Model}}=\mathrm{Res}=f(X_{\mathrm{Process}}) $$ 

 $$ \mathrm{MI_{Hybrid}=MI_{Model}+Res} $$ 

We consider an industrial slurry HDPE process similar to that in Workshop 9.3, Section 9.4.2, using actual plant data from LG Petrochemicals in South Korea. We build a dynamic model following the procedure described in Chapters 7 and 9. We use tasks in Aspen Plus Dynamics (Section 7.5) to simulate grade change (Section 7.6) and simulate plant data similar to the industrial process. In the Aspen dynamic model (Plant HDPE Hybrid.dynf), we use the Melt_Index value in the stream R1OUT to calculate the MI model. We copy the model data to a csv file containing the plant data.

Using the csv, we calculate the difference between the MI Plant and the MI Model, and label the difference as Res MI in the column in the sheet (Data_Hybrid2.xlsx).

Next, we use a ML model called a Random Forest Regressor [84] to predict the residual as a function of input process variables. We load the data and then split the dataset into test and train subsets. We follow the details of training a ML model described in Sections 10.3.2 and 10.6 of Chapter 10. Note that when using ensemble models, normalizing the data is not mandatory. Then, we train the random forest regressor model. We predict the Res MI using the model. The predicted residual (yt) can be output in the form of the csv file and then copied to a combined data file (hybrid_result.xlsx).

Figure 11.6 shows a part of the code, Hybrid_Direct_HPDE.ipynb, available in the supplement under Workshop 11.1.

We can do final calculations of the plant data using Pandas data-frame. As the dataset is not very large, we just explain the csv details in the Excel file, Hybrid_results.xlsx, available in the supplement for Workshop 11.1.

The ML predictions are labeled as ML Predicted Res MI. Then we add the ML predicted Res to the MI Model to give the Predicted Hybrid MI.

 $$  Hybrid Predicted MI=Model MI+ML Res $$ 

We can then calculate the difference between the “Hybrid Predicted MI” and the “Plant MI,” calling that Hybrid Res. We calculate the final RMSE of the predictions, which comes out to be 0.17 for the hybrid model compared to a RMSE of 1.74 for a stand-alone model MI.

---

<!-- PDF page 753 -->

df = pd.read_excel('Data_Hybrid.xlsx')
df.head()

X = df.iloc[:, 1:10]

Y1 = df.iloc[:, 12]

#Splitting data into test-train
X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1)

#Random Forest Model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, Y1_train)

cv = cross_val_score(rf, X_train, Y1_train, cv = 10,
                      scoring='neg_mean_squared_error')
cv_score = cv.mean()
rmse_train = np.sqrt(abs(cv_score))
print(rmse_train)

#print(cv_score)

Y_rf = rf.predict(X_test)
rmse = np.sqrt(mean_squared_error(Y1_test, Y_rf))
print(rmse)

#rf.predict(X)

<div style="text-align: center;">Figure 11.6 A part of the ML Python code, Hybrid_Direct_HPDE.ipynb.</div>


We can plot the model results. Figure 11.7 compares the predictions of the first-principle dynamic simulation model (in red) with the plant data with grade transitions (in green). We see much deviation between the model predictions and plant data. We compare the MI values from the model with the plant data and calculate the error residuals. The root-mean-squares error (RMSE) value of the model residual is 1.7 for the actual MI data with a standard deviation of 5.1.

Figure 11.6 shows that the hybrid model predictions (with a RMSE value of 0.17) match the plant data much better than a first-principle dynamic simulation model alone. We note that a data-based model alone has a similar accuracy, but it may give scientifically inconsistent results for predictions beyond process operating data, which the model uses. Thus, the hybrid model is not only accurate, but also gives scientifically consistent results beyond current operating range.

#### 11.4.2 Inverse Modeling

In inverse modeling, we use the output of a system to infer its corresponding input or independent variables; this is different from the forward modeling, where we use the known independent variables to predict the output of the system [3]. Figure 11.8 illustrates the inverse modeling framework. We see that in the traditional data-based

---

<!-- PDF page 754 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Model MI</th><th style='text-align: center;'>Hybrid MI</th><th style='text-align: center;'>Plant MI</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td><td style='text-align: center;'>17.0</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>9.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>7.5</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>3.5</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.7 Melt index prediction of a combined direct hybrid model compared to the first-principle model and plant data.</div>


approach, we use process variable data (X) and quality target data (Y) to train and test a ML model. Because the plant does not measure most quality targets continuously, we can apply a science-based process model, developed by first principles and validated by plant data, to predict and augment the quality target data (Y) for given process variable (X).

One of the earliest applications of inverse modeling for chemical processes was by Savkovic-Stevanovic et al. [85]. They use a neural network controller for product composition control of a distillation plant based on the process inverse dynamic model relating the product composition to the reflux flow rate. The results illustrate the feasibility of using neural network for learning nonlinear dynamic model of the distillation column from plant input–output data. Their results also demonstrate the importance of taking the time delay of the plant into account.

'pharmaceutical product design and development typically uses the design of experiments (DOE) and response surface modeling (RSM) for steady-state process modeling while neglecting the process dynamics and time delays. Tomba et al. [86] demonstrate how to use the inverse modeling concept to generate process understanding with dynamic process models, quantifying the impact of temporal deviations and production dynamics. Specifically, they perform data-based latent variable regression model inversion to find the best combination of raw materials and process variables to achieve the desired quality targets. The authors propose to combine DOE studies with hvbrid modeling for process characterization.

Bayer et al. [87] apply the inverse modeling approach to Escherichia coli fed-batch cultivations, evaluating the impact of three critical process variables. They compare

---

<!-- PDF page 755 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_145_733_523.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 11.8 Inverse Modeling framework.</div>


the performance of a hybrid model to a pure data-driven model and the widely adopted RSM of the process endpoints, and show the superior behavior of the hybrid model compared to the pure black-box approaches for process characterization. The inverse modeling methodology makes the decision-making process in pharmaceutical product development faster while minimizing the number of experiments and reducing raw material consumption.

Raccuglia et al. [88] train the ML model using reaction data to predict reaction outcomes for the crystallization of templated vanadium selenites. They demonstrate the use of ML to assist material discovery using data from previously unsuccessful or failed material synthesis experiments. The resulting ML model outperforms traditional human strategies and successfully predicts conditions for new organically templated, inorganic product formation with a success rate of nearly 90%. Significantly, they show that inverting the ML model reveals new hypotheses regarding the conditions for successful product formation.

There is a growing interest in the inverse approach to material design, in which the desired target properties are used as input to identify the atomic identity, composition, and structure (ACS) that exhibit such properties. Liao and Li [89] present a metaheuristic approach to material design that incorporates the inverse modeling framework.

Venkatasubramanian [63] also mentions the importance of inverse problem being solved by the application of artificial intelligence in chemical engineering processes.

Note that the inverse modeling approach may lead to nonunique solutions, which can give a range of predictions of input parameters within the operating range. By adding additional constraints to the input parameters (such as their operating range), we may obtain a unique solution.

---

<!-- PDF page 756 -->

##### 11.4.3 Workshop 11.2: An Application of Inverse Modeling to Polymer Manufacturing

We illustrate the application of an inverse modeling approach that integrates steady-state and dynamic simulation models of a Mitsui slurry HDPE process, developed from first principles and validated by plant data, with a data-based ML model. The goal is to predict the operating conditions for producing new polymer grades, given the desired product quality targets, such as MI, polymer density (Rho), polydispersity index (PDI), and polymer production rate (P). The details of the steady-state simulation model are available in Supplement 5.1b of Chapter 5.

We first estimate the polymerization kinetic parameters from plant production targets in a steady-state model using Aspen Polymers based on our methodology in Section 5.7. This results in a validated Aspen Polymers steady-state simulation model. Next, we convert the steady-state model to a dynamic model using Aspen Plus Dynamics, following Sections 7.7 and 7.8. We use the dynamic model to simulate the product quality data for different process operating conditions, which include the data characterizing the polymer grade transitions.

Then, we use a Python-based, ensemble ML regression model [90] (Section 10.3) to regress the simulated data, with the simulated product quality data as input and the process operating conditions (flow rates of all input streams) as the output. Given the desired quality targets for a new polymer grade, we apply the trained ML model to predict the operating conditions for the new polymer grade.

When loading the data in inverse modeling, we use the quality variable as the inputs (X) and the process variables as outputs (Y1). We use the stacked ensemble regression model for prediction. We use a combination of ensemble regression models using stacking technique for the prediction (Section 10.3.4) of the operating conditions. We used the tree regression models like the gradient boosting, ada (adaptive) boosting, Random forest, and Xgboost (extreme gradient boosting) regression model for the stacked regression algorithm. We choose the combination of the regression models by first individually fitting the regression models, and then the regressor, which performs best is chosen as the Meta regressor while the other three regressors are chosen as the Initial regressors.

Figure 11.9 shows the stacked model code, inverse_HDPE.py. In the figure, variable  $ \text{stregr} $ is the stacked regression model,  $ \mathbf{Y\_stregr} $ is the model prediction, and the RMSE for inverse modeling is  $ \text{predc} $.

The stacked ML model predictions give a low RMSE of 0.9 when compared to actual plant data for a standard deviation of 20. We predict all process variables for the parallel HDPE process using the stacked regression model as listed in Table 11.1. The table consists of the mean and standard deviation of each of the process variables from the actual data and the RMSE and nRMSE predictions, defined in Eqs. (10.2) and (10.3).

Figure 11.10 illustrates that the inverse modeling approach predicts the hydrogen feed flow rate with a high accuracy (low RMSE = 0.9) when compared to actual plant data for a standard deviation of 20. Thus, if we want to produce a new polymer grade given its quality targets, we can predict the operating conditions required to produce that polymer grade using the inverse modeling approach.

---

<!-- PDF page 757 -->

df = pd.read_excel('inverse_HDPE_feature.xlsx')

X = df.iloc[:, 14:18]
Y1 = df.iloc[:, 1]

X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1)

from mlxtend.regressor import StackingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

gb = GradientBoostingRegressor()
adb = AdaBoostRegressor()
xgr = xgb.XGBRegressor()
rf = RandomForestRegressor(n_estimators=100)

stregr = StackingRegressor(regressors=[adb,gb,xgr], meta_regressor=rf)

cv = cross_val_score(stregr, X_train, Y1_train, cv = 5, scoring='r2')
cv_score = cv.mean()
print(cv_score)

stregr.fit(X_train, Y1_train)
Y_stegr = stregr.predict(X_test)
print(stregr.score(X_test, Y1_test))
print(np.sqrt(mean_squared_error(Y1_test, Y_stegr)))

<div style="text-align: center;">Figure 11.9 ML Python code inverse HDPE.py for Workshop 11.2.</div>


<div style="text-align: center;">Table 11.1 Process variable prediction for parallel HDPE process using inverse modeling.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Predicted variable (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Data mean (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>Data standard deviation (kg/hr)</td><td style='text-align: center; word-wrap: break-word;'>RMSE (test) kg/hr</td><td style='text-align: center; word-wrap: break-word;'>Normalized RMSE, nRMSE (%)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2</td><td style='text-align: center; word-wrap: break-word;'>52</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>1.04</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C2</td><td style='text-align: center; word-wrap: break-word;'>8873</td><td style='text-align: center; word-wrap: break-word;'>569</td><td style='text-align: center; word-wrap: break-word;'>68.5</td><td style='text-align: center; word-wrap: break-word;'>0.772005</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>26</td><td style='text-align: center; word-wrap: break-word;'>5.6</td><td style='text-align: center; word-wrap: break-word;'>1.03</td><td style='text-align: center; word-wrap: break-word;'>3.961538</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX</td><td style='text-align: center; word-wrap: break-word;'>22356</td><td style='text-align: center; word-wrap: break-word;'>2734</td><td style='text-align: center; word-wrap: break-word;'>219</td><td style='text-align: center; word-wrap: break-word;'>0.979603</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3</td><td style='text-align: center; word-wrap: break-word;'>51</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>2.83</td><td style='text-align: center; word-wrap: break-word;'>5.54902</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T</td><td style='text-align: center; word-wrap: break-word;'>84</td><td style='text-align: center; word-wrap: break-word;'>0.3</td><td style='text-align: center; word-wrap: break-word;'>0.11</td><td style='text-align: center; word-wrap: break-word;'>0.130952</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P</td><td style='text-align: center; word-wrap: break-word;'>3.1</td><td style='text-align: center; word-wrap: break-word;'>0.7</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>6.451613</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H2/C2</td><td style='text-align: center; word-wrap: break-word;'>0.95</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>1.052632</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C3/C4</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0.37</td><td style='text-align: center; word-wrap: break-word;'>0.014</td><td style='text-align: center; word-wrap: break-word;'>3.5</td></tr></table>

---

<!-- PDF page 758 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Predicted hydrogen flow rate</th><th style='text-align: center;'>Actual hydrogen flow rate</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>88</td><td style='text-align: center;'>88</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>91</td><td style='text-align: center;'>91</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>93</td><td style='text-align: center;'>93</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>85</td><td style='text-align: center;'>85</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>82</td><td style='text-align: center;'>82</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>78</td><td style='text-align: center;'>78</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>75</td><td style='text-align: center;'>75</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>72</td><td style='text-align: center;'>72</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>68</td><td style='text-align: center;'>68</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>65</td><td style='text-align: center;'>65</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>55</td><td style='text-align: center;'>55</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>50</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>45</td><td style='text-align: center;'>45</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>55</td><td style='text-align: center;'>55</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>57</td><td style='text-align: center;'>57</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>58</td><td style='text-align: center;'>58</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>59</td><td style='text-align: center;'>59</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>60</td><td style='text-align: center;'>60</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>61</td><td style='text-align: center;'>61</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>61</td><td style='text-align: center;'>61</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>62</td><td style='text-align: center;'>62</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>62</td><td style='text-align: center;'>62</td></tr>
    <tr><td style='text-align: center;'>185</td><td style='text-align: center;'>63</td><td style='text-align: center;'>63</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>63</td><td style='text-align: center;'>63</td></tr>
    <tr><td style='text-align: center;'>195</td><td style='text-align: center;'>64</td><td style='text-align: center;'>64</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>64</td><td style='text-align: center;'>64</td></tr>
    <tr><td style='text-align: center;'>205</td><td style='text-align: center;'>65</td><td style='text-align: center;'>65</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>65</td><td style='text-align: center;'>65</td></tr>
    <tr><td style='text-align: center;'>215</td><td style='text-align: center;'>66</td><td style='text-align: center;'>66</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>66</td><td style='text-align: center;'>66</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>67</td><td style='text-align: center;'>67</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>67</td><td style='text-align: center;'>67</td></tr>
    <tr><td style='text-align: center;'>235</td><td style='text-align: center;'>68</td><td style='text-align: center;'>68</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>68</td><td style='text-align: center;'>68</td></tr>
    <tr><td style='text-align: center;'>245</td><td style='text-align: center;'>69</td><td style='text-align: center;'>69</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>69</td><td style='text-align: center;'>69</td></tr>
    <tr><td style='text-align: center;'>255</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>70</td><td style='text-align: center;'>70</td></tr>
    <tr><td style='text-align: center;'>265</td><td style='text-align: center;'>71</td><td style='text-align: center;'>71</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>71</td><td style='text-align: center;'>71</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>72</td><td style='text-align: center;'>72</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>72</td><td style='text-align: center;'>72</td></tr>
    <tr><td style='text-align: center;'>285</td><td style='text-align: center;'>73</td><td style='text-align: center;'>73</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>73</td><td style='text-align: center;'>73</td></tr>
    <tr><td style='text-align: center;'>295</td><td style='text-align: center;'>74</td><td style='text-align: center;'>74</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>74</td><td style='text-align: center;'>74</td></tr>
    <tr><td style='text-align: center;'>305</td><td style='text-align: center;'>75</td><td style='text-align: center;'>75</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>75</td><td style='text-align: center;'>75</td></tr>
    <tr><td style='text-align: center;'>315</td><td style='text-align: center;'>76</td><td style='text-align: center;'>76</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>76</td><td style='text-align: center;'>76</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>77</td><td style='text-align: center;'>77</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>77</td><td style='text-align: center;'>77</td></tr>
    <tr><td style='text-align: center;'>335</td><td style='text-align: center;'>78</td><td style='text-align: center;'>78</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>78</td><td style='text-align: center;'>78</td></tr>
    <tr><td style='text-align: center;'>345</td><td style='text-align: center;'>79</td><td style='text-align: center;'>79</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>79</td><td style='text-align: center;'>79</td></tr>
    <tr><td style='text-align: center;'>355</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>80</td><td style='text-align: center;'>80</td></tr>
    <tr><td style='text-align: center;'>365</td><td style='text-align: center;'>81</td><td style='text-align: center;'>81</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>81</td><td style='text-align: center;'>81</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>82</td><td style='text-align: center;'>82</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>82</td><td style='text-align: center;'>82</td></tr>
    <tr><td style='text-align: center;'>385</td><td style='text-align: center;'>83</td><td style='text-align: center;'>83</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>83</td><td style='text-align: center;'>83</td></tr>
    <tr><td style='text-align: center;'>395</td><td style='text-align: center;'>84</td><td style='text-align: center;'>84</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>84</td><td style='text-align: center;'>84</td></tr>
    <tr><td style='text-align: center;'>405</td><td style='text-align: center;'>85</td><td style='text-align: center;'>85</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>85</td><td style='text-align: center;'>85</td></tr>
    <tr><td style='text-align: center;'>415</td><td style='text-align: center;'>86</td><td style='text-align: center;'>86</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>86</td><td style='text-align: center;'>86</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>87</td><td style='text-align: center;'>87</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>87</td><td style='text-align: center;'>87</td></tr>
    <tr><td style='text-align: center;'>435</td><td style='text-align: center;'>88</td><td style='text-align: center;'>88</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>88</td><td style='text-align: center;'>88</td></tr>
    <tr><td style='text-align: center;'>445</td><td style='text-align: center;'>89</td><td style='text-align: center;'>89</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>89</td><td style='text-align: center;'>89</td></tr>
    <tr><td style='text-align: center;'>455</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>90</td><td style='text-align: center;'>90</td></tr>
    <tr><td style='text-align: center;'>465</td><td style='text-align: center;'>91</td><td style='text-align: center;'>91</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>91</td><td style='text-align: center;'>91</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td></tr>
    <tr><td style='text-align: center;'>485</td><td style='text-align: center;'>93</td><td style='text-align: center;'>93</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>93</td><td style='text-align: center;'>93</td></tr>
    <tr><td style='text-align: center;'>495</td><td style='text-align: center;'>94</td><td style='text-align: center;'>94</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>94</td><td style='text-align: center;'>94</td></tr>
    <tr><td style='text-align: center;'>505</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td></tr>
    <tr><td style='text-align: center;'>515</td><td style='text-align: center;'>96</td><td style='text-align: center;'>96</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>96</td><td style='text-align: center;'>96</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>97</td><td style='text-align: center;'>97</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>97</td><td style='text-align: center;'>97</td></tr>
    <tr><td style='text-align: center;'>535</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td></tr>
    <tr><td style='text-align: center;'>545</td><td style='text-align: center;'>99</td><td style='text-align: center;'>99</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>99</td><td style='text-align: center;'>99</td></tr>
    <tr><td style='text-align: center;'>555</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>565</td><td style='text-align: center;'>101</td><td style='text-align: center;'>101</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>101</td><td style='text-align: center;'>101</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td></tr>
    <tr><td style='text-align: center;'>585</td><td style='text-align: center;'>103</td><td style='text-align: center;'>103</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>103</td><td style='text-align: center;'>103</td></tr>
    <tr><td style='text-align: center;'>595</td><td style='text-align: center;'>104</td><td style='text-align: center;'>104</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>104</td><td style='text-align: center;'>104</td></tr>
    <tr><td style='text-align: center;'>605</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td></tr>
    <tr><td style='text-align: center;'>615</td><td style='text-align: center;'>106</td><td style='text-align: center;'>106</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>106</td><td style='text-align: center;'>106</td></tr>
    <tr><td style='text-align: center;'>625</td><td style='text-align: center;'>107</td><td style='text-align: center;'>107</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>107</td><td style='text-align: center;'>107</td></tr>
    <tr><td style='text-align: center;'>635</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td></tr>
    <tr><td style='text-align: center;'>645</td><td style='text-align: center;'>109</td><td style='text-align: center;'>109</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>109</td><td style='text-align: center;'>109</td></tr>
    <tr><td style='text-align: center;'>655</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td></tr>
    <tr><td style='text-align: center;'>665</td><td style='text-align: center;'>111</td><td style='text-align: center;'>111</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>111</td><td style='text-align: center;'>111</td></tr>
    <tr><td style='text-align: center;'>675</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td></tr>
    <tr><td style='text-align: center;'>685</td><td style='text-align: center;'>113</td><td style='text-align: center;'>113</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>113</td><td style='text-align: center;'>113</td></tr>
    <tr><td style='text-align: center;'>695</td><td style='text-align: center;'>114</td><td style='text-align: center;'>114</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>114</td><td style='text-align: center;'>114</td></tr>
    <tr><td style='text-align: center;'>705</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td></tr>
    <tr><td style='text-align: center;'>715</td><td style='text-align: center;'>116</td><td style='text-align: center;'>116</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>116</td><td style='text-align: center;'>116</td></tr>
    <tr><td style='text-align: center;'>725</td><td style='text-align: center;'>117</td><td style='text-align: center;'>117</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>117</td><td style='text-align: center;'>117</td></tr>
    <tr><td style='text-align: center;'>735</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td></tr>
    <tr><td style='text-align: center;'>745</td><td style='text-align: center;'>119</td><td style='text-align: center;'>119</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>119</td><td style='text-align: center;'>119</td></tr>
    <tr><td style='text-align: center;'>755</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td></tr>
    <tr><td style='text-align: center;'>765</td><td style='text-align: center;'>121</td><td style='text-align: center;'>121</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>121</td><td style='text-align: center;'>121</td></tr>
    <tr><td style='text-align: center;'>775</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td></tr>
    <tr><td style='text-align: center;'>785</td><td style='text-align: center;'>123</td><td style='text-align: center;'>123</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>123</td><td style='text-align: center;'>123</td></tr>
    <tr><td style='text-align: center;'>795</td><td style='text-align: center;'>124</td><td style='text-align: center;'>124</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>124</td><td style='text-align: center;'>124</td></tr>
    <tr><td style='text-align: center;'>805</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td></tr>
    <tr><td style='text-align: center;'>815</td><td style='text-align: center;'>126</td><td style='text-align: center;'>126</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>126</td><td style='text-align: center;'>126</td></tr>
    <tr><td style='text-align: center;'>825</td><td style='text-align: center;'>127</td><td style='text-align: center;'>127</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>127</td><td style='text-align: center;'>127</td></tr>
    <tr><td style='text-align: center;'>835</td><td style='text-align: center;'>128</td><td style='text-align: center;'>128</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>128</td><td style='text-align: center;'>128</td></tr>
    <tr><td style='text-align: center;'>845</td><td style='text-align: center;'>129</td><td style='text-align: center;'>129</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>129</td><td style='text-align: center;'>129</td></tr>
    <tr><td style='text-align: center;'>855</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td></tr>
    <tr><td style='text-align: center;'>865</td><td style='text-align: center;'>131</td><td style='text-align: center;'>131</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>131</td><td style='text-align: center;'>131</td></tr>
    <tr><td style='text-align: center;'>875</td><td style='text-align: center;'>132</td><td style='text-align: center;'>132</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>132</td><td style='text-align: center;'>132</td></tr>
    <tr><td style='text-align: center;'>885</td><td style='text-align: center;'>133</td><td style='text-align: center;'>133</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>133</td><td style='text-align: center;'>133</td></tr>
    <tr><td style='text-align: center;'>895</td><td style='text-align: center;'>134</td><td style='text-align: center;'>134</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>134</td><td style='text-align: center;'>134</td></tr>
    <tr><td style='text-align: center;'>905</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td></tr>
    <tr><td style='text-align: center;'>915</td><td style='text-align: center;'>136</td><td style='text-align: center;'>136</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>136</td><td style='text-align: center;'>136</td></tr>
    <tr><td style='text-align: center;'>925</td><td style='text-align: center;'>137</td><td style='text-align: center;'>137</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>137</td><td style='text-align: center;'>137</td></tr>
    <tr><td style='text-align: center;'>935</td><td style='text-align: center;'>138</td><td style='text-align: center;'>138</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>138</td><td style='text-align: center;'>138</td></tr>
    <tr><td style='text-align: center;'>945</td><td style='text-align: center;'>139</td><td style='text-align: center;'>139</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>139</td><td style='text-align: center;'>139</td></tr>
    <tr><td style='text-align: center;'>955</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td></tr>
    <tr><td style='text-align: center;'>965</td><td style='text-align: center;'>141</td><td style='text-align: center;'>141</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>141</td><td style='text-align: center;'>141</td></tr>
    <tr><td style='text-align: center;'>975</td><td style='text-align: center;'>142</td><td style='text-align: center;'>142</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>142</td><td style='text-align: center;'>142</td></tr>
    <tr><td style='text-align: center;'>985</td><td style='text-align: center;'>143</td><td style='text-align: center;'>143</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>143</td><td style='text-align: center;'>143</td></tr>
    <tr><td style='text-align: center;'>995</td><td style='text-align: center;'>144</td><td style='text-align: center;'>144</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>144</td><td style='text-align: center;'>144</td></tr>
    <tr><td style='text-align: center;'>1005</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td></tr>
    <tr><td style='text-align: center;'>1010</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td></tr>
    <tr><td style='text-align: center;'>1015</td><td style='text-align: center;'>146</td><td style='text-align: center;'>146</td></tr>
    <tr><td style='text-align: center;'>1020</td><td style='text-align: center;'>146</td><td style='text-align: center;'>146</td></tr>
    <tr><td style='text-align: center;'>1025</td><td style='text-align: center;'>147</td><td style='text-align: center;'>147</td></tr>
    <tr><td style='text-align: center;'>1030</td><td style='text-align: center;'>147</td><td style='text-align: center;'>147</td></tr>
    <tr><td style='text-align: center;'>1035</td><td style='text-align: center;'>148</td><td style='text-align: center;'>148</td></tr>
    <tr><td style='text-align: center;'>1040</td><td style='text-align: center;'>148</td><td style='text-align: center;'>148</td></tr>
    <tr><td style='text-align: center;'>1045</td><td style='text-align: center;'>149</td><td style='text-align: center;'>149</td></tr>
    <tr><td style='text-align: center;'>1050</td><td style='text-align: center;'>149</td><td style='text-align: center;'>149</td></tr>
    <tr><td style='text-align: center;'>1055</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>1060</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>1065</td><td style='text-align: center;'>151</td><td style='text-align: center;'>151</td></tr>
    <tr><td style='text-align: center;'>1070</td><td style='text-align: center;'>151</td><td style='text-align: center;'>151</td></tr>
    <tr><td style='text-align: center;'>1075</td><td style='text-align: center;'>152</td><td style='text-align: center;'>152</td></tr>
    <tr><td style='text-align: center;'>1080</td><td style='text-align: center;'>152</td><td style='text-align: center;'>152</td></tr>
    <tr><td style='text-align: center;'>1085</td><td style='text-align: center;'>153</td><td style='text-align: center;'>153</td></tr>
    <tr><td style='text-align: center;'>1090</td><td style='text-align: center;'>153</td><td style='text-align: center;'>153</td></tr>
    <tr><td style='text-align: center;'>1095</td><td style='text-align: center;'>154</td><td style='text-align: center;'>154</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>154</td><td style='text-align: center;'>154</td></tr>
    <tr><td style='text-align: center;'>1105</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td></tr>
    <tr><td style='text-align: center;'>1110</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td></tr>
    <tr><td style='text-align: center;'>1115</td><td style='text-align: center;'>156</td><td style='text-align: center;'>156</td></tr>
    <tr><td style='text-align: center;'>1120</td><td style='text-align: center;'>156</td><td style='text-align: center;'>156</td></tr>
    <tr><td style='text-align: center;'>1125</td><td style='text-align: center;'>157</td><td style='text-align: center;'>157</td></tr>
    <tr><td style='text-align: center;'>1130</td><td style='text-align: center;'>157</td><td style='text-align: center;'>157</td></tr>
    <tr><td style='text-align: center;'>1135</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td></tr>
    <tr><td style='text-align: center;'>1140</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td></tr>
    <tr><td style='text-align: center;'>1145</td><td style='text-align: center;'>159</td><td style='text-align: center;'>159</td></tr>
    <tr><td style='text-align: center;'>1150</td><td style='text-align: center;'>159</td><td style='text-align: center;'>159</td></tr>
    <tr><td style='text-align: center;'>1155</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td></tr>
    <tr><td style='text-align: center;'>1160</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td></tr>
    <tr><td style='text-align: center;'>1165</td><td style='text-align: center;'>161</td><td style='text-align: center;'>161</td></tr>
    <tr><td style='text-align: center;'>1170</td><td style='text-align: center;'>161</td><td style='text-align: center;'>161</td></tr>
    <tr><td style='text-align: center;'>1175</td><td style='text-align: center;'>162</td><td style='text-align: center;'>162</td></tr>
    <tr><td style='text-align: center;'>1180</td><td style='text-align: center;'>162</td><td style='text-align: center;'>162</td></tr>
    <tr><td style='text-align: center;'>1185</td><td style='text-align: center;'>163</td><td style='text-align: center;'>163</td></tr>
    <tr><td style='text-align: center;'>1190</td><td style='text-align: center;'>163</td><td style='text-align: center;'>163</td></tr>
    <tr><td style='text-align: center;'>1195</td><td style='text-align: center;'>164</td><td style='text-align: center;'>164</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>164</td><td style='text-align: center;'>164</td></tr>
    <tr><td style='text-align: center;'>1205</td><td style='text-align: center;'>165</td><td style='text-align: center;'>165</td></tr>
    <tr><td style='text-align: center;'>1210</td><td style='text-align: center;'>165</td><td style='text-align: center;'>165</td></tr>
    <tr><td style='text-align: center;'>1215</td><td style='text-align: center;'>166</td><td style='text-align: center;'>166</td></tr>
    <tr><td style='text-align: center;'>1220</td><td style='text-align: center;'>166</td><td style='text-align: center;'>166</td></tr>
    <tr><td style='text-align: center;'>1225</td><td style='text-align: center;'>167</td><td style='text-align: center;'>167</td></tr>
    <tr><td style='text-align: center;'>1230</td><td style='text-align: center;'>167</td><td style='text-align: center;'>167</td></tr>
    <tr><td style='text-align: center;'>1235</td><td style='text-align: center;'>168</td><td style='text-align: center;'>168</td></tr>
    <tr><td style='text-align: center;'>1240</td><td style='text-align: center;'>168</td><td style='text-align: center;'>168</td></tr>
    <tr><td style='text-align: center;'>1245</td><td style='text-align: center;'>169</td><td style='text-align: center;'>169</td></tr>
    <tr><td style='text-align: center;'>1250</td><td style='text-align: center;'>169</td><td style='text-align: center;'>169</td></tr>
    <tr><td style='text-align: center;'>1255</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td></tr>
    <tr><td style='text-align: center;'>1260</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td></tr>
    <tr><td style='text-align: center;'>1265</td><td style='text-align: center;'>171</td><td style='text-align: center;'>171</td></tr>
    <tr><td style='text-align: center;'>1270</td><td style='text-align: center;'>171</td><td style='text-align: center;'>171</td></tr>
    <tr><td style='text-align: center;'>1275</td><td style='text-align: center;'>172</td><td style='text-align: center;'>172</td></tr>
    <tr><td style='text-align: center;'>1280</td><td style='text-align: center;'>172</td><td style='text-align: center;'>172</td></tr>
    <tr><td style='text-align: center;'>1285</td><td style='text-align: center;'>173</td><td style='text-align: center;'>173</td></tr>
    <tr><td style='text-align: center;'>1290</td><td style='text-align: center;'>173</td><td style='text-align: center;'>173</td></tr>
    <tr><td style='text-align: center;'>1295</td><td style='text-align: center;'>174</td><td style='text-align: center;'>174</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>174</td><td style='text-align: center;'>174</td></tr>
    <tr><td style='text-align: center;'>1305</td><td style='text-align: center;'>175</td><td style='text-align: center;'>175</td></tr>
    <tr><td style='text-align: center;'>1310</td><td style='text-align: center;'>175</td><td style='text-align: center;'>175</td></tr>
    <tr><td style='text-align: center;'>1315</td><td style='text-align: center;'>176</td><td style='text-align: center;'>176</td></tr>
    <tr><td style='text-align: center;'>1320</td><td style='text-align: center;'>176</td><td style='text-align: center;'>176</td></tr>
    <tr><td style='text-align: center;'>1325</td><td style='text-align: center;'>177</td><td style='text-align: center;'>177</td></tr>
    <tr><td style='text-align: center;'>1330</td><td style='text-align: center;'>177</td><td style='text-align: center;'>177</td></tr>
    <tr><td style='text-align: center;'>1335</td><td style='text-align: center;'>178</td><td style='text-align: center;'>178</td></tr>
    <tr><td style='text-align: center;'>1340</td><td style='text-align: center;'>178</td><td style='text-align: center;'>178</td></tr>
    <tr><td style='text-align: center;'>1345</td><td style='text-align: center;'>179</td><td style='text-align: center;'>179</td></tr>
    <tr><td style='text-align: center;'>1350</td><td style='text-align: center;'>179</td><td style='text-align: center;'>179</td></tr>
    <tr><td style='text-align: center;'>1355</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>1360</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>1365</td><td style='text-align: center;'>181</td><td style='text-align: center;'>181</td></tr>
    <tr><td style='text-align: center;'>1370</td><td style='text-align: center;'>181</td><td style='text-align: center;'>181</td></tr>
    <tr><td style='text-align: center;'>1375</td><td style='text-align: center;'>182</td><td style='text-align: center;'>182</td></tr>
    <tr><td style='text-align: center;'>1380</td><td style='text-align: center;'>182</td><td style='text-align: center;'>182</td></tr>
    <tr><td style='text-align: center;'>1385</td><td style='text-align: center;'>183</td><td style='text-align: center;'>183</td></tr>
    <tr><td style='text-align: center;'>1390</td><td style='text-align: center;'>183</td><td style='text-align: center;'>183</td></tr>
    <tr><td style='text-align: center;'>1395</td><td style='text-align: center;'>184</td><td style='text-align: center;'>184</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>184</td><td style='text-align: center;'>184</td></tr>
    <tr><td style='text-align: center;'>1405</td><td style='text-align: center;'>185</td><td style='text-align: center;'>185</td></tr>
    <tr><td style='text-align: center;'>1410</td><td style='text-align: center;'>185</td><td style='text-align: center;'>185</td></tr>
    <tr><td style='text-align: center;'>1415</td><td style='text-align: center;'>186</td><td style='text-align: center;'>186</td></tr>
    <tr><td style='text-align: center;'>1420</td><td style='text-align: center;'>186</td><td style='text-align: center;'>186</td></tr>
    <tr><td style='text-align: center;'>1425</td><td style='text-align: center;'>187</td><td style='text-align: center;'>187</td></tr>
    <tr><td style='text-align: center;'>1430</td><td style='text-align: center;'>187</td><td style='text-align: center;'>187</td></tr>
    <tr><td style='text-align: center;'>1435</td><td style='text-align: center;'>188</td><td style='text-align: center;'>188</td></tr>
    <tr><td style='text-align: center;'>1440</td><td style='text-align: center;'>188</td><td style='text-align: center;'>188</td></tr>
    <tr><td style='text-align: center;'>1445</td><td style='text-align: center;'>189</td><td style='text-align: center;'>189</td></tr>
    <tr><td style='text-align: center;'>1450</td><td style='text-align: center;'>189</td><td style='text-align: center;'>189</td></tr>
    <tr><td style='text-align: center;'>1455</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td></tr>
    <tr><td style='text-align: center;'>1460</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td></tr>
    <tr><td style='text-align: center;'>1465</td><td style='text-align: center;'>191</td><td style='text-align: center;'>191</td></tr>
    <tr><td style='text-align: center;'>1470</td><td style='text-align: center;'>191</td><td style='text-align: center;'>191</td></tr>
    <tr><td style='text-align: center;'>1475</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td></tr>
    <tr><td style='text-align: center;'>1480</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td></tr>
    <tr><td style='text-align: center;'>1485</td><td style='text-align: center;'>193</td><td style='text-align: center;'>193</td></tr>
    <tr><td style='text-align: center;'>1490</td><td style='text-align: center;'>193</td><td style='text-align: center;'>193</td></tr>
    <tr><td style='text-align: center;'>1495</td><td style='text-align: center;'>194</td><td style='text-align: center;'>194</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>194</td><td style='text-align: center;'>194</td></tr>
    <tr><td style='text-align: center;'>1505</td><td style='text-align: center;'>195</td><td style='text-align: center;'>1</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.10 Hydrogen feed predictions from inverse modeling of product quality features.</div>


#### 11.4.4 Reduced-Order Models

ROMs are simplified models that not only represent a complex process in a computationally inexpensive manner but also maintain high degree of accuracy of prediction in simulating the process. In bioprocessing and chemical engineering, we can apply the ROM methodology to simulate complex processes and then use ML models to optimize the processes. See Figure 11.9. We can use ROMs to simulate different scenarios and sensitivities in order to generate process data, which in turn can be combined with ML models to build accurate soft sensors to predict quality variables. This approach helps to make sure that the ML model is trained on process data with multiple variations, which is not possible in a steady plant run. Hence, data-based sensors will be accurate for any future process optimization, scale-up, etc. and it is also easier to deploy such models online.

In one of the earliest applications of ROM, MacGregor et al. [91] apply a PLS ML model of a polyethylene using process data simulated from a process model to develop inferential prediction models for polymer properties. This application involves a high-pressure tabular reactor system producing low-density polyethylene, in which all the fundamental polymer properties are extremely difficult to measure and are usually unavailable, and some on-line measurements such as the temperature profile down the reactor and the solvent flow rate are available on a frequent basis. The dimensionality reduction aspects of PLS facilitate the development of a

---

<!-- PDF page 759 -->

multivariate statistical control plot for monitoring the operating performance of the reactors.

Model reduction can be achieved through dimensional reduction methods like principal component analysis. Another approach is to apply the residual combination with ML model for a ROM model or to build a ML-based surrogate model for the full-order model. Reduced-order models have been called surrogate models in the context of gray-box modeling techniques, where first-principle models are combined with data-based optimization techniques. Rogers and Lerapetritou [92, 93] propose the use of surrogate models as ROMs that approximate the feasibility function for a process in order to evaluate the flexibility and operability of a science-based process model, since it is difficult to directly evaluate the feasibility due to black-box constraints.

In a recent study, Abdullah et al. [94] showcase a data-based reduced-order modeling of nonlinear processes that have time-scale multiplicity to identify the slow process state variables that can be used in a dynamic model. Agarwal et al. [95] use ROM for modeling pressure swing adsorption process, where they use a low-dimensional approximation of a dynamic partial differential equation model, which is more computationally efficient. In another study, Kumar et al. [46] use a reduced-order steam methane reformer model to optimize the furnace temperature distribution. Schafer et al. [96] use a reduced-dimensional dynamic model for the optimal control of air separation unit. The model combines compartmentalization to reduce the number of differential equations with artificial neural networks to quantify the nonlinear input–output relations within compartments. This work reduces the size of the differential equation system by 90% while limiting the additional error in product purity to below 1 ppm compared to a full-order stage-by-stage model.

Kumari et al. [97] use data-based reduced-order methods for computational fluid dynamic modeling applied to a case study of supercritical carbon dioxide rare event. They propose a k-nearest neighbor (kNN)-based parametric ROM (PROM) for consequence estimation of rare events to enhance numerical robustness with respect to parameter change. Recently, many operator-theoretic modeling identification and model reduction approaches like the Koopman operators have been applied to integrate first-principle knowledge into finding relationship among multiple process variables in chemical processes. Koopman operator offers great utility in data-driven analysis and control of nonlinear and high-dimensional systems. Narasingam and Kwon [98] develop a new local Dynamic Mode Decomposition (DMD) method to better capture local dynamics, which does temporal clustering of snapshot data using mixed integer nonlinear programming. The developed models are subsequently used to compute approximate solutions to the original high-dimensional system and to design a feedback control system of hydraulic fracturing processes for the computation of optimal pumping schedules.

Our focus on ROM is more toward using the science-based model to simulate process data that can be used by ML models to derive empirical correlations for process

---

<!-- PDF page 760 -->

optimization. ROM are particularly useful in chemical processes for dynamic optimization of a complex, large-scale process.

##### 11.4.5 Workshop 11.3: An Application of Reduced-Order Modeling to Polymer Manufacturing

The objective of this example is to illustrate the application of ROM methodology for process development of HYPOL polypropylene production.

The details of the steady-state simulation model are available in Supplement 5.1a of Chapter 5. The Hypol process is complex, with a series of reactors, separators, and recycle loops. The process has many operating variables, such as feed flow rates of propylene and hydrogen to each reactor and temperature and pressure in each reactor. It is critical to quantify the effects of operating variables on the polymer quality targets, particularly MI, in order to design or optimize the process. To achieve this, we need multivariate process data, which is not usually available in a steady running plant. Hence, we use the ROM methodology.

We model the HYPOL polypropylene production process following the methodology of Section 5.5 and then run multiple steady-state simulations to generate multivariate data with varying operating variables and the corresponding MI predictions.

In the Aspen steady-state model, we use sensitivity analysis to generate process data by varying the process conditions using the Sensitivity Analysis tool. We vary the temperature, pressure of each reactor, the input feed flow rates within operating ranges to generate sensitivity data. Table 11.2 lists the process and quality variables.

We compile the data in a spreadsheet (ROM_data.xlsx) and then use them to fit a random forest ML model [90] using the same procedure as described in previous examples and chapter 10.

We use a random forest ML model to train the simulated data to predict the MI as a function of the process variables and also understand the causality of important features affecting the polymer quality. The empirical ML model can serve as an

<div style="text-align: center;">Table 11.2 Process and quality variables of Hypol process.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Process variable and quality target</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C31, C32, C33, and C34</td><td style='text-align: center; word-wrap: break-word;'>Propylene monomer flow in each of the reactors (R1, R2, R3, and R4) (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>H21, H22, H23, and H24</td><td style='text-align: center; word-wrap: break-word;'>Hydrogen flow in each of the reactors (R1, R2, R3, and R4) (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAT</td><td style='text-align: center; word-wrap: break-word;'>Catalyst flow in the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HX1</td><td style='text-align: center; word-wrap: break-word;'>Solvent flow in the first reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C24</td><td style='text-align: center; word-wrap: break-word;'>Ethylene co-monomer flow in the 4th reactor (kg/hr)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T1, T2, T3, and T4</td><td style='text-align: center; word-wrap: break-word;'>Temperature in each of the reactors (R1, R2, R3, and R4) C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P1, P2, P3, and P4</td><td style='text-align: center; word-wrap: break-word;'>Pressure in each of the reactors (R1, R2, R3, and R4) Bar</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MI (quality variable)</td><td style='text-align: center; word-wrap: break-word;'>Melt Index (quality variable)</td></tr></table>

---

<!-- PDF page 761 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Empirical melt index</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>12.8</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>14.8</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>16.2</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>15.0</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>13.0</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>15.8</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>15.5</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>15.8</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>15.5</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>15.8</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>14.8</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>62</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>64</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>66</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>68</td><td style='text-align: center;'>14.5</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>12.0</td></tr>
    <tr><td style='text-align: center;'>72</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>74</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>76</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>78</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>82</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>84</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>86</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>88</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>92</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>94</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>96</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>98</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>102</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>104</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>106</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>108</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>112</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>114</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>116</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>118</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>122</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>124</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>126</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>128</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>132</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>134</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>136</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>138</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>142</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>144</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>146</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>148</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>152</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>154</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>156</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>158</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>162</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>164</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>166</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>168</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>172</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>174</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>176</td><td style='text-align: center;'>12.2</td></tr>
    <tr><td style='text-align: center;'>178</td><td style='text-align: center;'>12.2</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.11a Melt Index prediction at varying process variables.</div>


approximate quality sensor. We can use it to predict the MI at varying process variables. See Figure 11.11a.

For process development, it is also useful to study the relative importance of variables in predicting the output. The random forest ML model also decides the relative importance of different operating variables in reducing the mean decrease in “node impurity,” which is a measure of how much each operating variable features reduces the variance in the model. Figure 11.11b illustrates that the ROM calculates important features like hydrogen flow rate (H24) and the temperature to the fourth reactor (R4T) as the most important variables affecting the MI, which can then be used to find the optimum conditions to produce polymer of a specified MI value and to improve the process design for a new process.

Figure 11.12 shows the ML Python code for the feature importance, and the complete code for the example is available in the supplement as ROM_Hypol_PP.ipynb.

#### 11.4.6 Hybrid SGML Modeling for Uncertainty Quantification

A science-based model can produce results with some uncertainties, which can be quantified by ML-based techniques. The uncertainties in science-based models arise from uncertainty in model parameters and boundary and initial conditions. In some cases, the model bias and assumptions can be a source of uncertainty as well. We can use the predictions from a calibrated model to quantify uncertainties. Data-based ML models like Gaussian process and neural networks are used to help build a surrogate model that defines a relation between model inputs and outputs, which can then be used to quantify the uncertainty.

---

<!-- PDF page 762 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Category</th><th style='text-align: center;'>Mean decrease in impurity</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>R1T</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>R2T</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>R3T</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>R4T</td><td style='text-align: center;'>0.16</td></tr>
    <tr><td style='text-align: center;'>R1P</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>R2P</td><td style='text-align: center;'>-0.01</td></tr>
    <tr><td style='text-align: center;'>R3P</td><td style='text-align: center;'>-0.01</td></tr>
    <tr><td style='text-align: center;'>R4P</td><td style='text-align: center;'>-0.01</td></tr>
    <tr><td style='text-align: center;'>C31</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>C32</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>C33</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>C34</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>H21</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>H22</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>H23</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>H24</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>C24</td><td style='text-align: center;'>0.01</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.11b Feature importance for melt index prediction: RxT and RxP refer to the temperature and pressure of reactor x; C3x and H2x represent the mass flow rates of propylene and hydrogen to reactor x; C24 is the mass flow rate of ethylene to reactor 4; and CAT is the catalysts mass flow rate.</div>


import time
import numpy as np

start_time = time.time()
importances = rf.feature_importances_
std = np.std([
    tree.feature_importances_for tree in rf.estimators_], axis=0
    elapsed_time = time.time() - start_time
    print(f"Elapsed time to compute the importances: "
                     f:{elapsed_time:.3f} seconds")
    feature_names = [f'feature {i}' for i in range(X.shape[1])]
    feature_names = X.columns
    import pandas as pd
    forest_importances = pd.Series(importances, index=feature_names)
    fig, ax = plt.subplots()
    forest_importances.plot.bar(yerr=std, ax=ax)
    ax.set_title("Feature Importance for Melt Index Prediction")
    ax.set_ylabel("Mean decrease in impurity")
    fig.tight_layout

<div style="text-align: center;">Figure 11.12 ML Python code for ranking feature importance.</div>


---

<!-- PDF page 763 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_149_778_293.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.13 Uncertainty quantification-modeling framework.</div>


Because of the uncertainty in process inputs and process states in a chemical process model, the uncertainty propagates to the process outputs as well. The uncertainty in a science-based model due to any of the parameters or any of the prior knowledge can be used by a ML model to quantify uncertainty in a chemical process, as shown in Figure 11.13.

This surrogate data-based ML modeling reduces the computational expense of Monte Carlo methods, which are traditionally used for uncertainty quantification (UQ) [99].

Because of the uncertainty in process inputs and process states in a chemical process model, the uncertainty propagates to the process outputs as well. Duong et al. [100] use UQ for process design and sensitivity analysis of complex chemical processes using the polynomial chaos theory. Francis-Xavier et al. [101] utilize UQ for electrochemical synthesis, where they calculate simulation uncertainties and global parameter sensitivities for the hybrid model. UQ has also been applied to understand complex reaction mechanisms. Proppe et al. [102] showcase kinetic simulations in discrete-time space, considering the uncertainty in free energy and detecting regions of uncertainty in reaction networks. UQ techniques are popular in the fields of catalysis and material science as they are used to quantify the uncertainty of models based on density functional theory [103, 104]. In another study, Boukouvala and Ierapetritou [105] demonstrate the feasibility analysis of a science-based process model over a multivariate factor space. They use a stochastic data-based model for feasibility evaluation, referred to as Kriging, and develop an adaptive sampling strategy to minimize sampling cost while maintaining feasibility.

##### 11.4.7 Workshop 11.4: An Application of SGML Modeling to Uncertainty Quantification in Polymer Manufacturing

The objective of this workshop is to quantify the uncertainty of the chemical process model in predicting the MI for an industrial HDPE process.

This uncertainty in prediction may result from the estimated kinetic parameters of the process, which propagate to the quality output as well. We simulate the data using Aspen Plus Dynamics model similar to the strategy illustrated in Sections 7.6 and 7.7. Then, we use the simulated data from the first-principle model and fit a ML model to predict the MI. We make use of the concept of prediction intervals to showcase the uncertainty in prediction.

---

<!-- PDF page 764 -->

from sklearn.ensemble import GradientBoostingRegressor
# Set lower and upper quantile
LOWER_ALPHA = 0.1
UPPER_ALPHA = 0.9
# Each model has to be separate
lower_model = GradientBoostingRegressor(loss="quantile", alpha=LOWER_ALPHA)
# The mid model will use the default loss
mid_model = GradientBoostingRegressor(loss="ls")
upper_model = GradientBoostingRegressor(loss="quantile", alpha=UPPER_ALPHA)

# Fit models
lower_model.fit(X_train, y_train)
mid_model.fit(X_train, y_train)
upper_model.fit(X_train, y_train)

<div style="text-align: center;">Figure 11.14 ML Python sklearn code to calculate prediction intervals.</div>


In this case, we calculate the prediction intervals using a gradient-boosting ML model  $ [90] $ (Section 10.3.3). In this case, we use the concept of prediction intervals to determine the range of model prediction. We use the quantile regression loss with gradient-boosting model to predict the prediction intervals  $ [106] $. We define a lower and an upper quantile according to the desired prediction interval. We consider the uncertainty in the prediction of MI given by the range of the 90% prediction interval, which implies that there is 90% likelihood that the ML model prediction will lie in the given range.

The simulated data are compiled in the spreadsheet and follow the same methodology to load data. Then, we calculate the prediction intervals with the help of Python sklearn libraries, as shown in the python code shown in Figure 11.14. In the code, we define the upper and lower quantile values and then define the three gradient-boosting models, with the upper and lower models defined by quantile loss while the middle model has the default mean squared loss as shown.

Figure 11.15 shows a part of the ML Python code for uncertain quantification.

The full code is available as UQ_HDPE.ipynb in the supplement to this chapter.

We then predict the results for each model and plot them using the matplotlib library plots.

Figure 11.16 illustrates the uncertainty in the prediction of MI given by the range of the 90% prediction interval, which implies that there is a 90% likelihood that the ML model prediction will lie in the given range. The resulting RMSE value lies within the range of 1.2–1.5, with the standard deviation of MI data equaling 5.1. In the figure, we see that the prediction interval is the area between the two black lines, represented by the upper quantile (95th percentile) and the lower quantile (5th percentile). From the figure, we see a larger prediction interval that means a higher uncertainty in prediction for time less than 100 hours compared to the later stage because of a more appreciable change in MI in that interval. Thus, UQ helps in making better process decisions after knowing the error estimate of the model.

---

<!-- PDF page 765 -->

# Record actual values on test set
predictions = pd.DataFrame(y_test)

# Predict
predictions['lower'] = lower_model.predict(X_test)
predictions['mid'] = mid_model.predict(X_test)
predictions['upper'] = upper_model.predict(X_test)

y_lower = predictions['lower']
y_mid = predictions['mid']
y_upper = predictions['upper']

y_l = lower_model.predict(X_test)

# print (rf.score(X_test, Y1_test))
rmse_l = np.sqrt(mean_squared_error(y_test, y_l))
print(rmse_l)

y_m = mid_model.predict(X_test)

# print (rf.score(X_test, Y1_test))
rmse_m = np.sqrt(mean_squared_error(y_m, y_l))
print(rmse_m)

fig = plt.figure()

# plt.plot(xx, f(xx), 'g:', label=r'$f(x) = x,\sin(x)$')
plt.plot(t, y, 'g.', markersize=10, label=u'Observations')
plt.plot(t, y_mid, 'r-', label=u'Prediction')
plt.plot(t, y_upper, 'k-')
plt.plot(t, y_lower, 'k-')
plt.fill(np.concatenate([t, t::-1]]),
    np.concatenate([y_upper, y_lower[::-1]]),
    alpha=.5, fc='b', ec='None', label='prediction interval')
plt.xlabel('Time')
plt.ylabel('Melt Index')
plt.ylim(-10, 20)
plt.legend(loc='upper right')
plt.show()

<div style="text-align: center;">Figure 11.15 A part of the ML Python code for the uncertainty quantification example.</div>


#### 11.4.8 Hybrid SGML Modeling to Aid in Discovering Scientific Laws Using ML

One way in which ML can help science-based modeling is by discovering new scientific laws that govern the system. There is a growing application of ML in physics to rediscover or discover physical laws, mainly by data-driven discovery of partial differential equations. ML can be used to develop an empirical correlation, which can be used as a scientific law in a science-based model, or ML can be used to solve the partial differential equation defining scientific laws as illustrated in Figure 11.17.

Rudy et al. [107] showcase the discovery of physical laws like the Navier–Stokes equation and the reaction–diffusion equation in chemical processes by a sparse

---

<!-- PDF page 766 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>Observations</th><th style='text-align: center;'>Prediction</th><th style='text-align: center;'>Upper prediction limit (95%)</th><th style='text-align: center;'>Lower prediction limit (5%)</th><th style='text-align: center;'>Prediction interval</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td><td style='text-align: center;'>14.0</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>10.0</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>8.0</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.0</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>315</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.16 Uncertainty quantification of melt index prediction of a slurry HDPE process.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_160_591_805_850.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 11.17 Discovering scientific laws.</div>


regression method governing the PDE by using a system of time series measurements. Langley et al. [108] present the applications of ML in rediscovering some of the chemistry laws, such as the law of definite proportions, the law of combining volumes, the determination of atomic weights, and many others.

Another important application of ML is to discover some of the thermodynamic laws, which can be useful in defining the phase equilibrium and are critical for an accurate science-based process model. Nentwich and Engell [109] use data-based mixed adaptive sampling strategy to calculate the phase composition instead of the complex equation-of-state models. Thus, ML application can have promising use in discovering more accurate physics and chemistry laws that govern the chemical process. This methodology can be used to obtain the functional form of scientific laws as well as the estimation of the parameters of existing laws. Brunton et al. [110] demonstrate a novel framework for discovering governing equations underlying a dynamic system simply from data measurements, leveraging advances in sparsity techniques and ML. These scientific laws calculated by ML-based models can then be utilized in first-principle model to improve accuracy as well as reduce model complexity.

---

<!-- PDF page 767 -->

### 11.5 Science Complements ML

Referring to Figure 11.1, we can also improve ML models using scientific knowledge. We can improve the generalization or extrapolation capability and reduce the scientific inconsistency of ML models by using scientific knowledge in designing the ML models. The scientific knowledge can also help in improving the architecture of the data-based ML model or the learning process of the ML model and even with the final postprocessing of the ML model results.

#### 11.5.1 Science-Guided Design

In science-guided design, we choose the model architecture based on scientific knowledge. For a neural network, we can decide the intermediate variables expressed as hidden layers based on scientific knowledge of the system. This helps in improving the interpretative ability of the models. Figure 11.18 illustrates a neural network model whose architecture, like the number of neurons, hidden layers, and activation layers, can be decided by prior scientific knowledge.

In a bioprocess application, Rodriguez-Granrose et al. [40] use the DOE to create and evaluate a neural network architecture. They use DOE to evaluate activation functions and neurons on each layer to optimize the neural network. Wang et al. [111] design their theory-infused neural networks based on adsorption energy principles for interpretable reactivity prediction. The use of the novel neural differential equation [112] to solve a first-principle dynamic system represents a hybrid SGML approach, where the architecture of ML model is influenced by the system and finds applications in continuous time series models and scalable normalizing flows. The derivative of hidden state is parameterized using a neural network, and the output of the network is computed using a differential equation solver. De Jaegher et al. [113] use the neural differential equation to predict the dynamic behavior of electrodialysis fouling under varying process conditions. In a recent application of this theme in chemical process for model-predictive control, Wu et al. [114] use prior process knowledge to design the RNN structure [10]. They showcase a methodology to design the RNN structure using prior scientific knowledge of the system and also employ weight constraints in the optimization problem of the RNN-training process. Reis et al. [115] discuss the concept of incorporation of process-specific structure to improve process fault detection and diagnosis.

Fuzzy artificial neural networks (ANNs) are a class of neural networks, which utilize prior scientific knowledge of the system to formulate rules mapped onto

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_1097_719_1267.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Figure 11.18 Science-guided design framework of neural network architecture.</div>


---

<!-- PDF page 768 -->

the structure of the ANN [10, 116]. The weights of the ANN connecting process input to output can be connected to physical process variables [64]. Apart from making the models more scientifically consistent with prior knowledge, they also reduce computational complexity and provide interpretable results. The use of prior knowledge also makes them suitable for extrapolation. Fuzzy ANNs have been particularly useful for applications in process control [117]. Simutis et al. use fuzzy ANN system for industrial bioprocess monitoring and control [118, 119]. They also illustrate the application of fuzzy ANN process control expert to perform appropriate control actions based on process trends for bioprocess optimization and control [120].

Sparse Identification of Nonlinear Dynamics (SINDy) is another data-based modeling method that utilizes scientific knowledge for improving the model performance with the algorithms  $ [110] $. Bhadriraju et al.  $ [121] $ have used the SINDy algorithm to identify the nonlinear dynamics of a chemical process system (CSTR). They used sparse regression in combination with feature selection to identify accurate models in an adaptive model-identification methodology, which requires much less than data that current methods. In a similar study, Bhadriraju et al.  $ [122] $ have a modified adaptive SINDy approach that is helpful in cases of plant-model mismatch and does not require retraining and hence computationally less expensive.

#### 11.5.2 Science-Guided Learning

Here, we make use of scientific principles to improve the scientific consistency of data-based models by modifying the ML process. We do this by modifying the loss function, constraints, and even the initialization of ML models based on scientific laws. Specifically, in order to make the ML models physically consistent, we make the loss function of neural network model incorporate physical constraints [3]. A loss function in ML measures how far an estimated value is from its true value. A loss function maps decisions to their associated costs. Loss functions are not fixed; they change depending on the task in hand and the goal to be met. We can define a loss function (based on the mean squared error, MSE) of the ML model ( $ Loss_{M} $) for regression to calculate the difference between the true value ( $ Y_{true} $) and the model predicted value ( $ Y_{pred} $). Likewise, we can define a loss function for a science-based model ( $ Loss_{SC} $), which is a function of the model predicted value ( $ Y_{pred} $) consistent with science-based loss. We include a weighting factor  $ \lambda $ to express the relative importance of both loss terms. We write the overall loss function (Loss) as:

 $$  Loss=Loss_{M}(Y_{true}-Y_{pred})+\lambda Loss_{SC}(Y_{pred}) $$ 

Figure 11.19 illustrates the concept of science-guided loss function.

A science-guided initialization helps in deriving an initial choice of parameters before a model is trained so that it improves model training and also prevents from reaching a local minimum, which is the concept of transfer learning. Thus, we can use the data from a science-based model to pretrain an ML model based on

---

<!-- PDF page 769 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_150_708_474.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 11.19 Science-guided loss function representation.</div>


this concept of initialization [2, 3, 8]. This concept has been utilized in chemical process modeling in the form of process similarity and developing new process models through migration. In particular, Lu et al. [123] introduce the concept of process similarity and classify it into attribute-based and model-based similarities. They present a model migration strategy to develop a new process model by taking advantage of an existing base model and process attribute information. Adapting existing process models can allow for the use of fewer experiments for the development of a new process model, resulting in savings in time, cost, and effort. They apply the concept to predict the melt-flow length in injection molding and obtain satisfactory results.

In another study on a similar concept, Yan et al. [124] use the Bayesian method for migrating a ML Gaussian process regression model. They showcased an approach of iterative model migration and process optimization for an epoxy catalytic reaction process.

Kumar et al. [125] try to optimize the non-Newtonian fluid flow for industrial processes like crude oil transportation using a physics-based loss function for the shear stress calculation for more accurate flow predictions. In another study on a similar principle, Pun et al. [126] apply physics-informed neural networks for more accurate and transferable atomistic modeling of materials.

##### 11.5.3 Workshop 11.5: An Illustrative Example of Science-Guided Learning

The objective of this example is to illustrate the application of the science-guided loss function to the slurry HDPE process for the industrial HDPE process described in Section 2.1.4.

The goal is to predict the MI of the polymer. The plant only measures the polymer MI as the quality output, but we also want the data-based ML model to predict the scientifically consistent polymer density values.

---

<!-- PDF page 770 -->

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(n_features,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

<div style="text-align: center;">Figure 11.20 The ML Python code for a deep neural network for predicting melt index.</div>


We express polymer density as a function of the MI using some empirical correlations and modify the loss function (based on the MSE) to consider density as well. See Eq. (11.4) below. We then train a DNN model to predict the MI of the polymer.

 $$  Loss=Loss_{M}(MI_{true}-MI_{pred})+\lambda Loss_{SC}(\rho(MI_{true})-\rho(MI_{pred})) $$ 

The Python process of loading the data is similar, and we also normalize/preprocess the data.

We use the tensor flow framework for training the multilayer neural network model, as shown in the python code shown in Figure 11.20. The DNN (deep neural network) has two hidden layers with 64 and 2 neurons, respectively. It uses the Rectified Linear Unit (ReLU) transfer function (see Table 10.6).

In order to modify the loss function, we define a custom loss function using the ML Python code shown in Figure 11.21.

We then train and optimize the neural network and also output the RMSE and prediction using the ML Python code shown in Figure 11.22.

Figure 11.23 illustrates that the SGML hybrid model calculates the MI, resulting in a RMSE of the MI that is slightly higher (RMSE = 0.8) (standard deviation of data = 5) compared to a stand-alone ML model. In addition to predicting the MI values, the hybrid SGML model is simultaneously predicting the polymer density correctly within the physically consistent range of 0.94–0.97 g/c. By contrast, the density estimates by the ML model alone result in density values greater than 1, which is physically inconsistent.

def custom_loss_function(y_pred, y_true):
    k1 = 0.001

    #y_pred = tf.convert_to_tensor_v2(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    #loss = tf.reduce_mean(tf.square(y_pred - y_true), axis=-1)
    loss = tf.reduce_mean((tf.square(y_pred - y_true)) + k1 * (tf.math.log(abs(y_pred)) - tf.math.log(abs(y_true))))
    return loss

<div style="text-align: center;">Figure 11.21 The ML Python code for defining the loss function of Eq. (11.4).</div>


---

<!-- PDF page 771 -->

model.compile(optimizer='adam',loss=custom_loss_function)
history = model.fit(X_train, Y1_train, epochs=500)

Y_p = model.predict(X)
df1 = pd.DataFrame(Y_p)
df1.to_excel("SGloss.xlsx")

<div style="text-align: center;">Figure 11.22 The ML Python code to optimize the deep neural network model for melt index.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time (hours)</th><th style='text-align: center;'>MI plant (g/cc)</th><th style='text-align: center;'>MI hybrid model (g/cc)</th><th style='text-align: center;'>Density model (g/cc)</th><th style='text-align: center;'>Density ML model (g/cc)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>17.5</td><td style='text-align: center;'>12.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>23.5</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>20.0</td><td style='text-align: center;'>13.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>23.5</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>18.0</td><td style='text-align: center;'>12.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>23.5</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>10.0</td><td style='text-align: center;'>8.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>23.0</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>22.5</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>7.5</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>22.0</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>6.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.8</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>5.0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>5.2</td><td style='text-align: center;'>21.5</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11.23 Melt index and polymer density prediction with a ML model with a science-guided loss function.</div>


#### 11.5.4 Science-Guided Refinement

By science-guided refinement, we mean the postprocessing of ML model results based on scientific principles. This postprocessing of results of the ML model using science-based models can be useful to the design and prediction of material structure [117]. Thus, the discovery of materials forms the basis of chemical process development, from which the manufacturing process of any compound can be designed. This is different than the serial-direct hybrid model discussed in Section 4.1.2. In particular, we use the science-based model to merely test the scientific consistency of the ML model results. Hautier et al. [118] use first-principle models based on density functional model to refine the results of probabilistic ML models to discover ternary oxides. Figure 11.24 illustrates the science-guided refinement framework.

Another application for science-guided learning is data generation. ML techniques like generalized adversarial networks (GANs) are useful for generating data in unsupervised learning. GANs do have a problem of high sample complexity [3], which can be reduced by incorporating some science-based constraints and prior knowledge. Cang et al. [119] apply ML models to predict the structure and properties of materials and use the results of the ab initio calculations to refine the ML

---

<!-- PDF page 772 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_147_791_309.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 11.24 Science-guided refinement framework.</div>


model results. They generate more imaging data for property prediction using CNN and introduce a morphology constraint from scientific principles, while training the generative models so that it improves the prediction of the structure-property model.

Thus, some of these methodologies of having science complementing ML have much potential for future applications to chemical and polymer processes.

#### 11.6 Workshop 11.6: Reduced-Order Model for a Polystyrene Process Using Aspen Multi-Case and Aspen AI Model Builder

In Sections 11.4.4 and 11.4.5, we discussed the principles of a ROM and presented a workshop on developing a ROM for polyolefin manufacturing.

The objective of this workshop is to illustrate two useful AspenTech software tools for developing hybrid SGML models for polyolefin and other chemical processes.

#### 11.6.1 Introduction to Aspen Multi-Case and Aspen AI Model Builder

In Section 11.4.5, we use an Aspen Plus simulation model of a HYPOL polypropylene process and run multiple steady-state simulations to generate multivariate process data with varying operating variables and the corresponding MI predictions. We can speed up the process-data generation by using the software tool Aspen Multi-Case in conjunction with Aspen Plus to rapidly simulate alternative process scenarios in parallel and leveraging high-performance computing, ML, data analysis, and visualization tools. We refer the reader to an online demand webinar by Mofar and Baker [127] that explains the principles and practice of using Aspen Multi-Case. This webinar demonstrates how Aspen Multi-Case can help to: (1) leverage the computing power available to run Aspen Plus and Aspen HYSYS cases in a fraction of the time; (2) employ visualization to analyze multiple cases and evaluate tradeoffs on quality, economics, safety, and sustainability; and (3) share the simulation files and results seamlessly with other engineers and stakeholders. We will show an application below.

Another useful tool for building hybrid SGML model is the Aspen AI Model Builder. This is a SaaS (Software as a Service) product, which is a software distribution model in which a cloud provider hosts applications and makes them available to end users over the internet. In particular, referring to reference  $ [128] $,

---

<!-- PDF page 773 -->

We see that since August 1, 2020, AspenTech continues to roll out periodic updates of new features and modeling tools for Aspen AI Model Builder, which immediately become available to all of our users. These include, for example, creating a reduced-order sensor, planning, equipment, or production optimization model, and creating an AI-driven hybrid model. We illustrate its application to developing a hybrid ROM for a polystyrene process below.

#### 11.6.2 Developing a Hybrid Reduced-Order Model (ROM) for a Polystyrene Process

We consider a polystyrene production process with three reactors in series and three distillation columns for separation. We plan to build a hybrid ROM model for the whole process.

We reduce the process to one hierarchy with only main input and output streams. We do this by selecting the whole process and then right-clicking to move to a hierarchy. We make sure we add the input and output streams to the process correctly. Figure 11.25 shows the original polystyrene process flowsheet.

We use Aspen Multi-Case to generate the dataset from the process model. Figure 11.26 shows the interface of the Aspen Multi-Case for our problem.

The software generates the dataset by sampling the independent and dependent variables. We choose run scenario by selecting the whole process hierarchy, and the process generates the default independent and dependent stream variables, which are temperature, pressure, mass flow, and mass fraction of the input and output streams. We can add more independent variables as needed for our hybrid ROM model. We can also add more equipment variables, like reactor temperature and pressure, as needed for our hybrid ROM model.

We edit the lower and upper bounds for the independent variables as required. We then define the number of runs in the Multi-Case. After the model runs, we can download the dataset in the form of *.json model file.

Then we use Aspen AI Model builder to build the data-base model. Figure 11.27 illustrates the variable interface of the Aspen AI Model Builder. Note the work

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_928_781_1274.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.25 Original process flowsheet of a polystyrene process.</div>


---

<!-- PDF page 774 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_146_810_469.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 11.26 Interface for Aspen Multi-Case for data generation for ROM.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_542_810_835.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.27 Variable interface of Aspen AI Model Builder.</div>


flow as indicated at the top of the interface figure: Import data→Manage variables→Clean data→Build model→Validate model.

We first “import data,” that is, the *.json model file from Aspen Plus Multi-Case. The model “manages variables” by automatically identifying the independent and dependent stream variables. Then, the software “cleans data” in the form of data required for model building. To “build model,” we can add the engineering constraints, which include the overall mass balance and physical constraints like mass fraction equal to 1.

Figure 11.28 illustrates the interface for model building in Aspen AI Model Builder. On the right side of the figure, we choose “Lasso CV” as the ML method. The word “Lasso” stands for Least Absolute Shrinkage and Selection Operator, and the word “CV” means cross-validation. Lasso regression is a type of linear regression that uses shrinkage, where data values are shrunk toward a central point, like the mean. It is a statistical formula for the regularization of data models and feature

---

<!-- PDF page 775 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_147_780_444.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.28 Model building in Aspen AI Model Builder.</div>


selection to avoid overfitting of the data, especially when the trained and test data are much varying. Specifically, regularization adds a “penalty” term to the best fit derived from the trained data to achieve a lesser variance with the tested data and also restricts the influence of predictor variables over the output variable by compressing their coefficients. Cross-validation is a technique for evaluating ML models by training several ML models on subsets of the available input data and evaluating them on the complementary subset of the data. Use cross-validation to detect overfitting, i.e. failing to generalize a pattern.

In Figure 11.28, we see names of feed and product. Figure 11.29 shows the model validation results in Aspen AI Model Builder. This figure shows that the R2 values of

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_806_782_1219.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.29 Model validation results in Aspen AI Model Builder.</div>


---

<!-- PDF page 776 -->

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_151_812_374.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 11.30 Process flowsheet of ROM for polystyrene process.</div>


dependent variables are above 0.96656, and the Q2 values after a cross-validation are above .9961. We note that we defined both R2 and V2 values previously in Eqs. (9.19) and (9.20) in Section 9.14. In the figure, we also see the root-MSE (RMSE) values. These results indicate a very good model prediction.

Next, we download the hybrid model results from the side tab in the format of AspenTech hybrid model file, *.athm. We deploy the data-based ROM in Aspen Plus by following the path: Customize → Manage Hybrid Models → Browse for available models, *.ahtm → open. Figure 11.30 shows the resulting process flowsheet of the hybrid ROM for the polystyrene process.

When we run the hybrid ROM on Aspen Plus, we see that the hybrid ROM runs much faster than the original process model.

We can even set up an optimization problem using the ROM model to test the faster and easier convergence of the model. For this case, we set up a small optimization problem to maximize the polystyrene polymer flow in the bottom residue by varying the feed flow rate, and the model converges very fast with results displayed in Figure 11.31.

This process can be repeated for more complex plant flowsheets for easy analysis and optimization of the complex process using a hybrid ROM. We conclude this workshop and present the challenges and opportunities of hybrid SGML approach for modeling chemical and polymer processes below.

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_978_808_1216.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Figure 11.31 Results of optimization study using the hybrid reduced-order model (ROM).</div>


---

<!-- PDF page 777 -->

<div style="text-align: center;">Summary of the SGML approach to modeling chemical and polymer processes.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Hybrid SGML modeling</td><td style='text-align: center; word-wrap: break-word;'>Science-based model/knowledge</td><td style='text-align: center; word-wrap: break-word;'>ML model</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Limitations</td><td style='text-align: center; word-wrap: break-word;'>Potential applications</td></tr><tr><td colspan="6">ML complements science (base model science-based)</td></tr><tr><td rowspan="3">Direct hybrid modeling</td><td style='text-align: center; word-wrap: break-word;'>Series</td><td style='text-align: center; word-wrap: break-word;'>Science-based model (SBM)</td><td style='text-align: center; word-wrap: break-word;'>Regression</td><td style='text-align: center; word-wrap: break-word;'>Extrapolation; parameter estimation; data augmentation</td><td style='text-align: center; word-wrap: break-word;'>Limited by data for parameter estimation, interpolation, scientific knowledge-dominated</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Parallel</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Regression</td><td style='text-align: center; word-wrap: break-word;'>Improved accuracy of prediction, interpolation</td><td style='text-align: center; word-wrap: break-word;'>Scientific consistency depends on SBM, extrapolation data-dominated</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Series-parallel</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Regression</td><td style='text-align: center; word-wrap: break-word;'>Higher accuracy, interpolation</td><td style='text-align: center; word-wrap: break-word;'>Increased model complexity, data-dominated</td></tr><tr><td rowspan="3">Inverse modeling</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Probarabilistic, regression</td><td style='text-align: center; word-wrap: break-word;'>Computationally cheaper inverse problem</td><td style='text-align: center; word-wrap: break-word;'>Lower generality of the model</td><td style='text-align: center; word-wrap: break-word;'>Product design and development [86]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Series-parallel</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Probarabilistic, regression</td><td style='text-align: center; word-wrap: break-word;'>Computationally cheaper inverse problem</td><td style='text-align: center; word-wrap: break-word;'>Polymer grade change</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Series-parallel</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Probarabilistic, regression</td><td style='text-align: center; word-wrap: break-word;'>Computationally cheaper inverse problem</td><td style='text-align: center; word-wrap: break-word;'>Polymer grade change</td></tr></table>

(Continued)

---

<!-- PDF page 778 -->

<div style="text-align: center;">Table 11.3 (Continued)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Hybrid SGML modeling</td><td style='text-align: center; word-wrap: break-word;'>Science-based model/ knowledge</td><td style='text-align: center; word-wrap: break-word;'>ML model</td><td style='text-align: center; word-wrap: break-word;'>Advantages</td><td style='text-align: center; word-wrap: break-word;'>Limitations</td><td style='text-align: center; word-wrap: break-word;'>Potential applications</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reduced-order models</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Regression</td><td style='text-align: center; word-wrap: break-word;'>Fast online deployment, reduce model complexity</td><td style='text-align: center; word-wrap: break-word;'>Higher bias, limited by SBM accuracy</td><td style='text-align: center; word-wrap: break-word;'>Process optimization at plant scale [46, 95] Dynamic modelling [94, 96]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Uncertainty quantification</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Probabilistic</td><td style='text-align: center; word-wrap: break-word;'>Gives real error estimate and solution space</td><td style='text-align: center; word-wrap: break-word;'>Limited by SBM assumptions, parameters</td><td style='text-align: center; word-wrap: break-word;'>Process design and development [100] Reaction kinetics [100] Feasibility analysis [105]</td></tr><tr><td rowspan="2">Discovering scientific law</td><td rowspan="2">SBM</td><td rowspan="2">Regression probabilistic</td><td rowspan="2">System stability interpretability</td><td rowspan="2">Limited by data size/availability</td><td style='text-align: center; word-wrap: break-word;'>Physical chemistry [108] Fluid dynamics [107]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Thermodynamics phase equilibrium [109]</td></tr><tr><td colspan="6">Science complements ML (base model ML)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Science-guided design</td><td style='text-align: center; word-wrap: break-word;'>Laws or SBM</td><td style='text-align: center; word-wrap: break-word;'>Deep neural network (DNN; neural differential equation)</td><td style='text-align: center; word-wrap: break-word;'>Scientifically consistent and interpretable</td><td style='text-align: center; word-wrap: break-word;'>Requires deep scientific knowledge of system</td><td style='text-align: center; word-wrap: break-word;'>Dynamic system [113] Process control [113, 119] Process monitoring [115]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Science-guided learning</td><td style='text-align: center; word-wrap: break-word;'>Laws</td><td style='text-align: center; word-wrap: break-word;'>DNN</td><td style='text-align: center; word-wrap: break-word;'>Scientifically consistent and interpretable</td><td style='text-align: center; word-wrap: break-word;'>Possible lower prediction accuracy</td><td style='text-align: center; word-wrap: break-word;'>Process design and development [123, 124] Process monitoring</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Science-guided refinement</td><td style='text-align: center; word-wrap: break-word;'>SBM</td><td style='text-align: center; word-wrap: break-word;'>Probabilistic</td><td style='text-align: center; word-wrap: break-word;'>Less effort in feature selection</td><td style='text-align: center; word-wrap: break-word;'>Limited by SBM assumptions, parameters</td><td style='text-align: center; word-wrap: break-word;'>Process design Discovery of material [119, 126, 129, 130]</td></tr></table>

---

<!-- PDF page 779 -->

### 11.7 Challenges and Opportunities of Hybrid SGML Approach for Modeling Chemical and Polymer Processes

Along with all the merits of using the SGML methodology, there are challenges as well. Incorrect fundamental knowledge and the assumptions of the science-based first-principle model will lead to inaccurate hybrid model, so it is important for the scientific model to be very accurate. We must pay attention to the lack of engineer/scientists having expertise in both domain knowledge and ML. Computation infeasibility in certain modeling approaches like inverse modeling.

Data cleaning, preprocessing, and feature engineering may be difficult in certain cases but may be imperative in science-based model-parameter estimation; hence, in these cases, the hybrid models may increase the complexity compared to stand-alone ML models like Neural Network, which may not require feature engineering. Model predictions must not only be accurate but also with lower uncertainty, which may be difficult for certain hybrid model methods.

There is a lot of scope for using hybrid SGML methodologies in chemical process modeling; we summarize here some of the opportunities and areas where they can be beneficial. As we have seen, hybrid SGML models are useful for extrapolation and predicting beyond operating range; hence, they will be particularly useful for process development. Process fault diagnosis and anomaly detection is one such area where data-based methods have been extensively used, thus there is opportunity to combine scientific knowledge as well to make the anomaly detection process more scientifically consistent.

Table 11.3 summarizes all the hybrid SGML models and their requirements, advantages, limitations, and potential applications.

### 11.8 Conclusion

We present a broad perspective on hybrid modeling with a SGML approach and its application in bioprocessing and chemical engineering. We give a detailed review and exposition of the hybrid SGML modeling approach and its applications and classify the approach into two categories. The first refers to the case where a data-based ML model complements and makes the first-principle science-based model more accurate in prediction, and the second corresponds to the case where scientific knowledge helps make the ML model more scientifically consistent. We point out some of the areas of SGML, which have not been explored much in chemical process modeling and have potential for further use like in the areas where Science can help improve the data-based model by improving the model design, learning, and refinement. We also illustrate some of these applications of the hybrid SGML methodologies for industrial polymer/chemical process improvement.

Thus, based on our review, we recommend that the use of hybrid models will perform better than stand-alone ML for applications like process development, since they are better at extrapolation than standalone ML models, which can be adequate for prediction in a steady running plant.

---

<!-- PDF page 780 -->

## References

1 Sharma, N. and Liu, Y.A. (2022). A hybrid science-guided machine learning approach for modeling chemical processes: a review. AIChE Journal 68 (5): e17609.

2 Karpatne, A., Atluri, G., Faghmous, J.H. et al. (2017). Theory-guided data science: a new paradigm for scientific discovery from data. IEEE Transactions on Knowledge and Data Engineering 29: 2318.

3 Willard, J., Jia, X., Xu, S. et al. (2003). Integrating physics-based modeling with machine learning: a survey. arXiv preprint arXiv:2003.04919.2020.

4 Muralidhar, N., Bu, J., Cao, Z. et al. (2020). PhyNet: physics guided neural networks for particle drag force prediction in assembly. Proceedings of the 2020 SIAM International Conference on Data Mining. Society for Industrial and Applied Mathematics, 559–567.

5 Bode, M., Gauding, M., Lian, Z. et al. (2019). Using physics-informed super-resolution generative adversarial networks for subgrid modeling in turbulent reactive flows. arXiv preprint arXiv:1911.11380.

6 Schütt, K.T., Kindermans, P.J., Sauceda, H.E. et al. (2017). A continuous-filter convolutional neural network for modeling quantum interactions. arXiv preprint arXiv:1706.08566.

7 Faghmous, J.H. and Kumar, V. (2014). A big data guide to understanding climate change: the case for theory-guided data science. Big Data 2: 155.

8 Karpatne, A., Watkins, W., Read, J., and Kumar, V. (2017). Physics-guided neural networks (PGNN): an application in Lake temperature modeling. arXiv preprint arXiv:1710.11431.

9 Lee, D., Jayaraman, A., and Kwon, J.S. (2020). Development of a hybrid model for a partially known intracellular signaling pathway through correction term estimation and neural network modeling. PLoS Computational Biology 16: e1008472.

10 Baughman, D.R. and Liu, Y.A. (1995). Neural Networks in Bioprocessing and Chemical Engineering. San Diego, CA: Academic Press.

11 Psichogios, D.C. and Ungar, L.H. (1992). A hybrid neural network-first principles approach to process modeling. AIChE Journal 38: 1499.

12 Thompson, M.L. and Kramer, M.A. (1994). Modeling chemical process using prior knowledge and neural networks. AIChE Journal 40: 1328.

13 Agarwal, M. (1997). Combining neural and conventional paradigms for modelling, prediction and control. International Journal of Systems Science 28: 65.

14 Asprion, N., Böttcher, R., Pack, R. et al. (2019). Gray-box modeling for the optimization of chemical processes. Chemie Ingenieur Technik 91: 305.

15 Bohlin, T.P. (2006). Practical Grey-Box Process Identification: Theory and Applications. Springer Science & Business Media.

16 Yang, S., Navarathna, P., Ghosh, S., and Bequette, B.W. (2020). Hybrid modeling in the era of smart manufacturing. Computers and Chemical Engineering 140: 106.

---

<!-- PDF page 781 -->

17 Sansana, J., Joswiak, M.N., Castillo, I. et al. (2021). Recent trends on hybrid modeling for industry 4.0. Computers and Chemical Engineering 11: 107.

18 Chen, Y. and Ierapetritou, M. (2020). A framework of hybrid model development with identification of plant-model mismatch. AIChE Journal 66: e16996.

19 Von Stosch, M., Oliveira, R., Peres, J., and de Azevedo, S.F. (2014). Hybrid semi-parametric modeling in process systems engineering: past, present and future. Computers and Chemical Engineering 60: 86.

20 Qin, S.J. and Chiang, L.H. (2019). Advances and opportunities in machine learning for process data analytics. Computers and Chemical Engineering 126: 465.

21 Qin, S.J., Guo, S., Li, Z. et al. (2021). Integration of process knowledge and statistical learning for the dow data challenge problem. Computers and Chemical Engineering 153: 107451.

22 O'Brien, C.M., Zhang, Q., Daoutidis, P., and Hu, W.S. (2021). A hybrid mechanistic-empirical model for in silico mammalian cell bioprocess simulation. Metabolic Engineering 66: 31.

23 Pinto, J., de Azevedo, C.R., Oliveira, R., and von Stosch, M. (2019). A bootstrap-aggregated hybrid semi-parametric modeling framework for bioprocess development. Bioprocess and Biosystems Engineering 42: 1853.

24 Chopda, V., Gyorgypal, A., Yang, O. et al. (2021). Recent advances in integrated process analytical techniques, modeling, and control strategies to enable continuous biomanufacturing of monoclonal antibodies. Journal of Chemical Technology & Biotechnology https://doi.org/10.1002/jctb.6765.

25 Zhang, D., Del Rio-Chanona, E.A., Petsagkourakis, P., and Wagner, J. (2019). Hybrid physics-based and data-driven modeling for bioprocess online simulation and optimization. Biotechnology and Bioengineering 116: 2919.

26 Al-Yemni, M. and Yang, R.Y. (2005). Hybrid neural-networks modeling of an enzymatic membrane reactor. Journal of the Chinese Institute of Engineers 28: 1061.

27 Chabbi, C., Taibi, M., and Khier, B. (2008). Neural and hybrid neural modeling of a yeast fermentation process. International Journal of Computational Cognition 6: 42.

28 Corazza, F., Calsavara, L.P., Moraes, F.F. et al. (2005). Determination of inhibition in the enzymatic hydrolysis of cellobiose using hybrid neural modeling. Brazilian Journal of Chemical Engineering 22: 19.

29 Azarpour, A., Borhani, T.N., Alwi, S.R. et al. (2017). A generic hybrid model development for process analysis of industrial fixed-bed catalytic reactors. Chemical Engineering Research and Design 117: 149.

30 Luo, N., Du, W., Ye, Z., and Qian, F. (2012). Development of a hybrid model for industrial ethylene oxide reactor. Industrial and Engineering Chemistry Research 51: 6926.

31 Zahedi, G., Lohi, A., and Mahdi, K.A. (2011). Hybrid modeling of ethylene to ethylene oxide heterogeneous reactor. Fuel Processing Technology 92: 1725.

---

<!-- PDF page 782 -->

32 Simon, L.L., Fischer, U., and Hungerbühler, K. (2006). Modeling of a three-phase industrial batch reactor using a hybrid first-principle neural-network model. Industrial and Engineering Chemistry Research 45: 7336.

33 Bellos, G.D., Kallinikos, L.E., Gounaris, C.E., and Papayannakos, N.G. (2005). Modelling of the performance of industrial HDS reactors using a hybrid neural network approach. Chemical Engineering and Processing Process Intensification 44: 505.

34 Chang, J.S., Lu, S.C., and Chiu, Y.L. (2007). Dynamic modeling of batch polymerization reactors via the hybrid neural-network rate-function approach. Chemical Engineering Journal 130: 19.

35 Hinchliffe, M., Montague, G., Willis, M., and Burke, A. (2003). Hybrid approach to modeling an industrial polyethylene process. AIChE Journal 49: 3127.

36 Madar, J., Abonyi, J., and Szeifert, F. (2005). Feedback linearizing control using hybrid neural networks identified by sensitivity approach. Engineering Applications of Artificial Intelligence 36: 343.

37 Simutis, R. and Lübbert, A. (2017). Hybrid approach to state estimation for bioprocess control. Bioengineering 4: 21.

38 Cubillos, F., Callejas, H., Lima, E.L., and Vega, M.P. (2001). Adaptive control using a hybrid-neural model: application to a polymerization reactor. Brazilian Journal of Chemical Engineering 18: 113.

39 Doyle, F.J. III, Harrison, C.A., and Crowley, T.J. (2003). Hybrid model-based approach to batch-to-batch control of particle size distribution in emulsion polymerization. Computers and Chemical Engineering 27: 1153.

40 Rodriguez-Granrose, D., Jones, A., Loftus, H. et al. (2021). Design of experiment (DOE) applied to artificial neural network architecture enables rapid bioprocess improvement. Bioprocess and Biosystems Engineering 44: 1301.

41 Brendel, M. and Marquardt, W. (2008). Experimental design for the identification of hybrid reaction models from transient data. Chemical Engineering Journal 141: 264.

42 Bollas, G.M., Papadokonstadakis, S., Michalopoulos, J. et al. (2003). Using hybrid neural networks in scaling up an FCC model from a pilot plant to an industrial unit. Chemical Engineering and Processing Process Intensification 42: 697.

43 Von Stosch, M., Hamelink, J.M., and Oliveira, R. (2016). Hybrid modeling as a QbD/PAT tool in process development: an industrial E. coli case study. Bioprocess and Biosystems Engineering 39: 773.

44 Iwama, R. and Kaneko, H. (2021). Design of ethylene oxide production process based on adaptive design of experiments and Bayesian optimization. Journal of Advanced Manufacturing and Processing. 3: e10085.

45 Zhang, S., Wang, F., He, D., and Jia, R. (2012). Batch-to-batch control of particle size distribution in cobalt oxalate synthesis process based on hybrid model. Powder Technology 224: 253.

46 Kumar, A., Baldea, M., and Edgar, T.F. (2016). Real-time optimization of an industrial steam-methane reformer under distributed sensing. Control Engineering Practice 54: 140.

---

<!-- PDF page 783 -->

47 Zhou, T., Gani, R., and Sundmacher, K. (2021). Hybrid data-driven and mechanistic modeling approaches for multiscale material and process design. Engineering 7: 1231.

48 Cardillo, A.G., Castellanos, M.M., Desailly, B. et al. (2021). Towards in silico process modeling for vaccines. Trends in Biotechnology 39: 1120.

49 McBride, K., Sanchez Medina, E.I., and Sundmacher, K. (2020). Hybrid semi-parametric modeling in separation processes: a review. Chemie Ingenieur Technik 92: 842.

50 Safavi, A.A., Nooraii, A., and Romagnoli, J.A. (1999). A hybrid model formulation for a distillation column and the on-line optimisation study. Journal of Process Control 9: 125.

51 Mahalec, V. (2018). Hybrid modeling of petrochemical processes. In: Hybrid Modeling in Process Industries (ed. J. Glassey and M. Von Stosch), 129–165. CRC Press.

52 Mahalec, V. and Sanchez, Y. (2012). Inferential monitoring and optimization of crude separation units via hybrid models. Computers and Chemical Engineering 45: 15.

53 Peroni, C.V., Parisi, M., and Chianese, A. (2010). A hybrid modelling and self-learning system for dextrose crystallization process. Chemical Engineering Research and Design 88: 1653.

54 Xiong, Z. and Zhang, J. (2005). A batch-to-batch iterative optimal control strategy based on recurrent neural network models. Journal of Process Control 15: 11.

55 Zhang, S., Chu, F., Deng, G., and Wang, F. (2019). Soft sensor model development for cobalt oxalate synthesis process based on adaptive Gaussian mixture regression. IEEE Access 7: 118749.

56 Nentwich, C., Winz, J., and Engell, S. (2019). Surrogate modeling of fugacity coefficients using adaptive sampling. Industrial and Engineering Chemistry Research 58: 18703.

57 Kunde, C., Keßler, T., Linke, S. et al. (2019). Surrogate modeling for liquid–liquid equilibria using a parameterization of the binodal curve. Processes 7: 753.

58 Côte, M., Grandjean, B.P., Lessard, P., and Thibault, J. (1995). Dynamic modelling of the activated sludge process: improving prediction using neural networks. Water Research 29: 995.

59 Hwang, T.M., Oh, H., Choi, Y.J. et al. (2009). Development of a statistical and mathematical hybrid model to predict membrane fouling and performance. Desalination 247: 210.

60 Piron, E., Latrille, E., and Rene, F. (1997). Application of artificial neural networks for crossflow microfiltration modelling: “black-box” and semi-physical approaches. Computers and Chemical Engineering 21: 1021.

61 Zbiciński, I., Strumillo, P., and Kamiński, W. (1996). Hybrid neural model of thermal drying in a fluidized bed. Computers and Chemical Engineering 20: S695.

---

<!-- PDF page 784 -->

62 Cubillos, F.A., Alvarez, P.I., Pinto, J.C., and Lima, E.L. (1996). Hybrid-neural modeling for particulate solid drying processes. Powder Technology 87: 153.

63 Venkatasubramanian, V. (2019). The promise of artificial intelligence in chemical engineering: is it here, finally. AIChE Journal 65: 466.

64 Glassey, J. and Von Stosch, M. (ed.) (2018). Hybrid Modeling in Process Industries. Boca Raton, FL: CRC Press.

65 Kahrs, O. and Marquardt, W. (2008). Incremental identification of hybrid process models. Computers and Chemical Engineering 32: 694.

66 Herwig, C., Porter, R., and Moller, J. (ed.) (2021). Digital Twins: Tools and Concepts for Smart Biomanufacturing. New York: Springer.

67 Chan, W.K., Fischer, B., Varvarezos, D. et al. Inventors; Aspen Technology Inc., Assignee (2020). Asset optimization using integrated modeling, optimization, and artificial intelligence. United States Patent Application 16/434,793.

68 Beck, R. and Munoz, G. (2020). Hybrid Modeling: AI and Domain Expertise Combine to Optimize Assets. https://www.aspentech.com/en/resources/whitepapers/hybrid-modeling-ai-and-domain-expertise-combine-to-optimize-assets/?src=blog-global-wpt (accessed 25 February 2023).

69 Galvanauskas, V., Simutis, R., and Lübbert, A. (2004). Hybrid process models for process optimization, monitoring and control. Bioprocess and Biosystems Engineering 26: 393.

70 Tian, Y., Zhang, J., and Morris, J. (2001). Modeling and optimal control of a batch polymerization reactor using a hybrid stacked recurrent neural network model. Industrial and Engineering Chemistry Research 40: 4525.

71 Su, H.T., McAvoy, T.J., and Werbos, P. (1992). Long-term predictions of chemical processes using recurrent neural networks: a parallel training approach. Industrial and Engineering Chemistry Research 31: 1338.

72 Hermanto, M.W., Braatz, R.D., and Chiu, M.S. (2011). Integrated batch-to-batch and nonlinear model predictive control for polymorphic transformation in pharmaceutical crystallization. AIChE Journal 57: 1008.

73 Ghosh, D., Hermonat, E., Mhaskar, P. et al. (2019). Hybrid modeling approach integrating first-principle models with subspace identification. Industrial and Engineering Chemistry Research 58: 13533.

74 Ghosh, D., Moreira, J., and Mhaskar, P. (2021). Model predictive control embedding a parallel hybrid modeling strategy. Industrial and Engineering Chemistry Research 60: 2547.

75 Hanachi, H., Yu, W., Kim, I.Y. et al. (2019). Hybrid data-driven physics-based model fusion framework for tool wear prediction. The International Journal of Advanced Manufacturing Technology 101: 2861.

76 Babanezhad, M., Behroyan, I., Nakhjiri, A.T. et al. (2020). High-performance hybrid modeling chemical reactors using differential evolution based fuzzy inference system. Scientific Reports 10: 1–1.

77 Kripl, M., Dürauer, A., and Duerkop, M. (2020). Hybrid modeling of cross-flow filtration: predicting the flux evolution and duration of ultrafiltration processes. Separation and Purification Technology 248: 117064.

---

<!-- PDF page 785 -->

78 Mantovanelli, I.C., Rivera, E.C., Da Costa, A.C., and Maciel, F.R. (2007). Hybrid neural network model of an industrial ethanol fermentation process considering the effect of temperature. Applied Biochemistry and Biotechnology 137: 817.

79 Sharma, N. and Liu, Y.A. (2019). 110th anniversary: an effective methodology for kinetic parameter estimation for modeling commercial polyolefin processes from plant data using efficient simulation software tools. Industrial and Engineering Chemistry Research 58: 14209.

80 Bangi, M.S. and Kwon, J.S. (2020). Deep hybrid modeling of chemical process: application to hydraulic fracturing. Computers and Chemical Engineering 134: 106696.

81 Bhutani, N., Rangaiah, G.P., and Ray, A.K. (2006). First-principle, data-based, and hybrid modeling and optimization of an industrial hydrocracking unit. Industrial and Engineering Chemistry Research 45: 7807.

82 Song, W., Du, W., Fan, C. et al. (2021). Adaptive weighted hybrid modeling of hydrocracking process and its operational optimization. Industrial and Engineering Chemistry Research 60: 3617.

83 Lima, P.V., Saraiva, P.M., and GEPSI-PSE Group (2007). A semi-mechanistic model building framework based on selective and localized model extensions. Computers and Chemical Engineering 31: 361.

84 Breiman, L. (2001). Random forests. Machine Learning 45: 5.

85 Savkovic-Stevanovic, J. (1996). Neural net controller by inverse modeling for a distillation plant. Computers and Chemical Engineering 20: S925.

86 Tomba, E., Barolo, M., and García-Muñoz, S. (2014). In-silico product formulation design through latent variable model inversion. Chemical Engineering Research and Design 92: 534.

87 Bayer, B., von Stosch, M., Striedner, G., and Duerkop, M. (2020). Comparison of modeling methods for DoE-based holistic upstream process characterization. Biotechnology Journal 15: 1900551.

88 Raccuglia, P., Elbert, K.C., Adler, P.D. et al. (2016). Machine-learning-assisted materials discovery using failed experiments. Nature 533: 73.

89 Liao, T.W. and Li, G. (2020). Metaheuristic-based inverse design of materials—a survey. Journal of Materiomics 6: 414.

90 Zhou, Z.H. (2012). Ensemble Methods: Foundations and Algorithms. Chapman & Hall/CRC Machine Learning.

91 MacGregor, J.F., Skagerberg, B., and Kiparissides, C. (1992). Multivariate statistical process control and property inference applied to low density polyethylene reactors. Advanced Control of Chemical Processes. IFAC Symposia Series, 155–159.

92 Rogers, A. and Ierapetritou, M. (2015). Feasibility and flexibility analysis of black-box processes. Part 1: Surrogate-based feasibility analysis. Chemical Engineering Science 137: 986.

93 Rogers, A. and Ierapetritou, M. (2015). Feasibility and flexibility analysis of black-box processes. Part 2: Surrogate-based flexibility analysis. Chemical Engineering Science 137: 1005.

---

<!-- PDF page 786 -->

94 Abdullah, F., Wu, Z., and Christofides, P.D. (2021). Data-based reduced-order modeling of nonlinear two-time-scale processes. Chemical Engineering Research and Design 166: 1.

95 Agarwal, A., Biegler, L.T., and Zitney, S.E. (2009). Simulation and optimization of pressure swing adsorption systems using reduced-order modeling. Industrial and Engineering Chemistry Research 48: 2327.

96 Schäfer, P., Caspari, A., Kleinhans, K. et al. (2019). Reduced dynamic modeling approach for rectification columns based on compartmentalization and artificial neural networks. AIChE Journal 65: e16568.

97 Kumari, P., Bhadriraju, B., Wang, Q., and Kwon, J.S. (2021). Development of parametric reduced-order model for consequence estimation of rare events. Chemical Engineering Research and Design 169: 142.

98 Narasingam, A. and Kwon, J.S. (2017). Development of local dynamic mode decomposition with control: application to model predictive control of hydraulic fracturing. Computers and Chemical Engineering 106: 501.

99 Zhang, J., Yin, J., and Wang, R. (2020). Basic framework and main methods of uncertainty quantification. Mathematical Problems in Engineering https://doi.org/10.1155/2020/6068203.

100 Duong, P.L., Ali, W., Kwok, E., and Lee, M. (2016). Uncertainty quantification and global sensitivity analysis of complex chemical process using a generalized polynomial chaos approach. Computers and Chemical Engineering 90: 23.

101 Francis-Xavier, F., Kubannek, F., and Schenkendorf, R. (2021). Hybrid process models in electrochemical syntheses under deep uncertainty. Processes 9: 704.

102 Proppe, J., Husch, T., Simm, G.N., and Reiher, M. (2017). Uncertainty quantification for quantum chemical models of complex reaction networks. Faraday Discussions 195: 497.

103 Parks, H.L., McGaughey, A.J., and Viswanathan, V. (2019). Uncertainty quantification in first-principle predictions of harmonic vibrational frequencies of molecules and molecular complexes. Journal of Physical Chemistry C 123: 4072.

104 Wang, S., Pillai, H.S., and Xin, H. (2020). Bayesian learning of chemisorption for bridging the complexity of electronic descriptors. Nature Communications 11: 6132.

105 Boukouvala, F. and Ierapetritou, M.G. (2012). Feasibility analysis of black-box processes using an adaptive sampling kriging-based method. Computers and Chemical Engineering 36: 358.

106 Ghenis, M. (2018). Quantile regression, from linear regression to deep learning. https://towardsdatascience.com/quantile-regression-from-linear-models-to-trees-to-deep-learning-af3738b527c3 (accessed 5 August 2021).

107 Rudy, S.H., Brunton, S.L., Proctor, J.L., and Kutz, J.N. (2017). Data-driven discovery of partial differential equations. Science Advances 3: e1602614.

108 Langley, P., Bradshaw, G.L., and Simon, H.A. (1983). Rediscovering chemistry with the BACON system. In: Machine Learning. Symbolic Computation (ed. R.S. Michalski, J.G. Carbonell, and T.M. Mitchell), 307–329. Berlin, Heidelberg: Springer-Verlag. https://doi.org/10.1007/978-3-662-12405-5_10.

---

<!-- PDF page 787 -->

109 Nentwich, C. and Engell, S. (2019). Surrogate modeling of phase equilibrium calculations using adaptive sampling. Computers and Chemical Engineering 126: 204.

110 Brunton, S.L., Proctor, J.L., and Kutz, J.N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proceedings of the National Academy of Sciences of the United States of America 113: 3932.

111 Wang, S.H., Pillai, H.S., Wang, S. et al. (2021). Infusing theory into machine learning for interpretable reactivity prediction. arXiv preprint arXiv:2103.15210.

112 Chen, R.T., Rubanova, Y., Bettencourt, J., and Duvenaud, D. (2018). Neural ordinary differential equations. arXiv preprint arXiv:1806.07366.

113 De Jaegher, B., Larumbe, E., De Schepper, W. et al. (2020). Colloidal fouling in electrodialysis: a neural differential equations model. Separation and Purification Technology 249: 116939.

114 Wu, Z., Rincon, D., and Christofides, P.D. (2020). Process structure-based recurrent neural network modeling for model predictive control of nonlinear processes. Journal of Process Control 89: 74.

115 Reis, M.S., Gins, G., and Rato, T.J. (2019). Incorporation of process-specific structure in statistical process monitoring: a review. Journal of Quality Technology 51: 407.

116 Hayashi, Y., Buckley, J.J., and Czogala, E. (1993). Fuzzy neural network with fuzzy signals and weights. International Journal of Intelligent Systems 8: 527.

117 Brown, M. and Harris, C.J. (1994). Neurofuzzy Adaptive Modelling and Control. Hoboken, NJ: Prentice Hall.

118 Hautier, G., Jain, A., Ong, S.P. et al. (2011). Phosphates as lithium-ion battery cathodes: an evaluation based on high-throughput ab initio calculations. Chemistry of Materials 23: 3495.

119 Cang, R., Li, H., Yao, H. et al. (2018). Improving direct physical properties prediction of heterogeneous materials from imaging data via convolutional neural network and a morphology-aware generative model. Computational Materials Science 150: 212.

120 Schubert, J., Simutis, R., Dors, M. et al. (1994). Bioprocess optimization and control: application of hybrid modelling. Journal of Biotechnology 35: 51.

121 Bhadriraju, B., Narasingam, A., and Kwon, J.S. (2019). Machine learning-based adaptive model identification of systems: application to a chemical process. Chemical Engineering Research and Design 152: 372.

122 Bhadriraju, B., Bangi, M.S., Narasingam, A., and Kwon, J.S. (2020). Operable adaptive sparse identification of systems: application to chemical processes. AIChE Journal 66: e16980.

123 Lu, J., Yao, K., and Gao, F. (2009). Process similarity and developing new process models through migration. AIChE Journal 55: 2318.

124 Yan, W., Hu, S., Yang, Y. et al. (2011). Bayesian migration of Gaussian process regression for rapid process modeling and optimization. Chemical Engineering Journal 166: 1095.

---

<!-- PDF page 788 -->

125 Kumar, A., Ridha, S., Narahari, M., and Ilyas, S.U. (2021). Physics-guided deep neural network to characterize non-Newtonian fluid flow for optimal use of energy resources. Expert Systems with Applications 19: 115409.

126 Pun, G.P., Batra, R., Ramprasad, R., and Mishin, Y. (2019). Physically informed artificial neural networks for atomistic modeling of materials. Nature Communications 10: 1.

127 Moriar, W. and Baker, L. (2021). Aspen technology on-demand seminar: StreaMLine concurrent simulation scenarios to solve problems faster using Aspen multi-case. https://www.aspentech.com/en/resources/on-demand-webinars/streaMLine-concurrent-simulation-scenarios-to-solve-problems-faster (accessed 14 May 2022).

128 Aspen Technology, Inc. (2022). What Is New in AI Model Builder.

AspenTech online help. https://aimodelbuilder.aspentech.ai/assets/

AspenAIModelBuilderHelp/HybridModelingApplication.htm#htML/whatsnew.htm?TocPath=___2 (accessed 14 May 2022).

129 Fischer, C.C., Tibbetts, K.J., Morgan, D., and Ceder, G. (2006). Predicting crystal structure by merging data mining with quantum mechanics. Nature Materials 5: 641.

130 Hautier, G., Fischer, C.C., Jain, A. et al. (2010). Finding nature’s missing ternary oxide compounds using machine learning and density functional theory. Chemistry of Materials 22: 3762.