# Appendix B. Introduction to Python for Chemical Engineers

<!-- PDF page 827 -->

## Appendix B

# Introduction to Python for Chemical Engineers Aman Aggarwal

### B.1 Introduction

Python is a high-level general-purpose programming language designed by Guido van Rossum in the 1980s. Some of the characteristics of Python that make it such a popular programming language are simplicity, versatility, cross-platform, open-source, free software, large unique library, and exceptional handling capacity.

Simplicity: Python has been ranked among the top two most popular programming languages for by IEEE Spectrum in 2021 and 2022 [1]. Because of its user-friendliness, English language parallels, and adaptability, Python aids new programmers in mastering the concepts of programming in a simple manner. Engineers new to programming can easily learn the syntaxes of the language without having to learn complex syntaxes like the ones used for programs such as C++, Java, and PHP.

Versatility: Over the past decades, Python has emerged to be one of the most diverse programming languages, which can be used for software development, operations, visualization, data analytics, finance, design, machine learning, artificial intelligence, etc.

In chemical engineering, Python has a broad array of applications, like soft-sensor development, data analytics and visualization, operations, process optimization, simulation, process design, automatic calculation, and anomaly detection.

Cross-platform: Python programs can run across different operating systems like Windows, Mac, and Linux. Some operating systems like Mac and Linux, come with preinstalled versions of Python. While, for operating system like Windows, one can easily install Python and a graphical interface if needed.

Open-source: Python is publicly accessible with open-source license. Anyone can see, modify, and distribute the code, even for commercial use.

Free software: All the versions of Python, including the latest version, can be installed for free on multiple devices for all operating systems (Windows, Mac, Linux, Other).

Large unique library: One of the reasons for the popularity of Python is its huge collection of libraries, which is increasing exponentially as its simplicity attracts

---

<!-- PDF page 828 -->

thousands of developers to develop new libraries. Some of the popular libraries are Numpy, Scikit-Learn, TensorFlow, Pandas, Keras, etc.

Exception handling capacity: Errors in Python are of two types: Syntax errors and exceptions. Errors are the problems in a program due to which the program will stop the execution. Syntax errors are errors caused by a character or string incorrectly placed in a command or instruction that causes a failure in execution.

On the other hand, exceptions are raised when some internal events occur, which change the normal flow of the program. Python offers several exception handling mechanisms to elegantly handle errors without disturbing the workflow of majority of the code and solve problems, which can sometimes speed up the script.

### B.2 Installing Python

For installing and using Python, we recommend using Spyder, an open-source cross-platform integrated development environment (IDE) for scientific programming in the Python language.

The best way to install Spyder and get other useful programming toolkits is to install a group package called Anaconda. Anaconda is a free and open-source distribution of the Python and R programming languages for data science and machine learning. Anaconda comes with over 1500 packages (including the package management system Conda) and a graphic user interface (GUI) named Anaconda Navigator. The Anaconda Navigator also allows users to install some applications by default, such as Jupyter Notebook, Spyder IDE, and Rstudio (for R).

The step-by-step guide for installing Anaconda Navigator is:

(1) Go to anaconda.com

(2) From the products category, select Individual Edition.

(3) Click on Download.

(4) Select the right operating system and choose a 64-bit processor for the most advanced computer systems (ideal for RAM greater than 4 GB) or a 32-bit processor for older systems.

(5) Click on executable file, then click next, read the licensing agreement and click on agree to the terms.

(6) Select an install for “Just Me” unless you are installing for all users (which requires Windows Administrator privileges) and click Next.

(7) Select the installation location.

(8) Choose whether to add Anaconda to your PATH environment variable. We recommend not adding Anaconda to the PATH environment variable, since this can interfere with other software. Instead, use Anaconda software by opening Anaconda Navigator or the Anaconda Prompt from the Start Menu.

(9) Choose whether to register Anaconda as your default Python. We recommend selecting this option.

(10) Click on Install, then Next, and finally Finish to complete installation.

---

<!-- PDF page 829 -->

For more information and operating system specific guide, users can visit:

https://docs.anaconda.com/anaconda/install/

### B.3 Basics with Python

### 1. Opening Python

To use Python, we will be using Spyder IDE as a graphical interface. We open Spyder by searching for Spyder or using Anaconda Navigator.

### 2. Creating a new file

We create a new file by clicking on new file or pressing Ctrl+N; every new file is created as a Python script, and its directory location can be selected and is visible above the variable explorer window.

It is important to save the script in the right location before executing the script.

### 3. Writing a script

We write the script in the command window, and the executed script output can be seen in the IPython console window in Spyder. Stored functions, variables, and basic mathematical operations can be directly called in the console window.

### 4. Using Python as a calculator

We can use Python as a calculator to perform basic mathematical operations. For instance, we can directly use the console window for the calculation:

In [1]: 12/1.9926

Out[1]: 6.022282445046673

Such calculations are very basic; in order to do some complicated calculations, we need to learn about storing values in variables and some mathematical libraries, which we will look into in the sections ahead.

### 5. Storing values in variables

In Python, we can assign a value to a variable using the equals sign. For instance, we can store Avogadro's number:

In [2]: Avogadro_number=12/(1.9926*pow(10,-23))

We use the built-in power function (pow) to handle exponentials. The resulting variable is stored as Avogadro_number and can be seen in the variable explorer window. See Figure B.1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1123_784_1211.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure B.1 Variable explorer displaying the stored value of a variable.</div>


---

<!-- PDF page 830 -->

### B.4 Different Data Types in Python

Variables can store data of different types; Python has the following data types built-in by default:

### 1. Text Type ("str")

To create a string, we use single or double quotes around some text, for instance:

In [3]: closing_salutation='CHEers'

### 2. Numeric Types ("int, float, complex")

Figure B.2 shows that x, y, and z are stored as integer, float, and complex numbers, respectively.

Name Type Size Value
x int 1 5
y float 1 4.63
z complex 1 (2+5j)

<div style="text-align: center;">Figure B.2 Stored numerical types.</div>


### 3. Sequence Types ("list, tuple, range")

List: We use lists to store multiple items in a single variable. We create lists using square brackets. Lists are ordered, changeable, and allow duplicate values. List items are indexed; the first item has index [0], the second item has index [1], etc. For instance:

In [10]: George_Davis=['UK', 'Father_of_chemical_engineering', 1850, 1906]

Tuple: We use tuples to store multiple items in a single variable, like lists. Tuples are created using round brackets. They are ordered, unchangeable, and allow duplicate values. Tuple items are indexed as well; the first item has index [0], the second item has index [1], etc. For instance:

In [11]: George_Davis=( 'UK', 'Father_of_chemical_engineering', 1850, 1906)

Before we look into range, let us look at the differences between lists and tuples:

a. Syntax difference: As shown above, a list is created using square brackets, while a tuple is created using round brackets.

b. Mutability: We can easily change or modify list values based on index, while a tuple cannot be changed. Since lists are mutable, we cannot use a list as a key in a dictionary. This is because only an immutable object can be used as a key in a dictionary. Thus, we can use tuples as dictionary keys if needed. Figure B.3 shows the code and the resulting display of the change.

---

<!-- PDF page 831 -->

In [13]: George_Davis[0]='Birmingham, UK'

Variable explorer
Name Type Size Value
George_Davis list 4 ['Birmingham, UK', 'Father_of_chemical_engineering', 1850, 1906]

<div style="text-align: center;">Figure B.3 The code for changing a key in a dictionary and the resulting list after change.</div>


c. Copying and reusability: Since tuples are immutable, they can simply be reused without copying. However, lists can be copied, as shown in Figure B.4.

In [14]: copy_George_Davis=list(George_Davis)

copy_George_Davis list 4 ['Birmingham, UK', 'Father_of_chemical_engineering', 1850, 1906]

### Figure B.4 Copying a list and the resulting display

The elements in the copied list are identical to those in the original list. However, the list itself is different, as shown below:

In [15]: print(copy_George_Davis is George_Davis)
False

d. Memory difference: Python allocates memory to tuples in terms of larger blocks with a low overhead because they are immutable. On the other hand, for lists, Python allocates small memory blocks. Thus, tuples use less memory space compared to lists. This makes tuples a bit faster than lists when you have a large number of elements.

Range: The range() function returns a sequence of numbers, starting from 0 by default, incrementing by 1 (by default), and stopping before a specified number. Here, we store a range of multiples of 4 starting at 4 and ending at 21. Figure B.5 shows the script.

Four_multiples=range(4,21,4)
for n in Four_multiples:
    print(n)

Output:
4
8
12
16
20

<div style="text-align: center;">Figure B.5 The code for specifying a range and the resulting output.</div>


---

<!-- PDF page 832 -->

### 4. Mapping Type ("dict")

Dictionaries are used to store data values in “key:value” pairs. They are created using curly brackets. They are ordered (for Python 3.7 and above, unordered for other versions), changeable, and do not allow duplicate values. Here we store the information we used before as a dictionary:

In [26]: Father_of_chemical_engineering = {"Name": "George Davis", "Country": "United Kingdom", "Birth year": 1850}

With dictionaries, we can easily search for specific values for different keys. For instance, if we want to see the birth year for George Davis in our dictionary, we can simply use:

In [27]: print(Father_of_chemical_engineering["Birth year"])
1850

### 5. Set Types ("set," "frozenset")

Set: Sets are used to store multiple items in a single variable. They are also created using curly brackets. They are unordered, unchangeable, unindexed, and do not allow duplicate values. Sets are mutable, allowing us to add or remove values from them. For our example, the code is:

In [34]: Father_of_chemical_engineering = {"George Davis", "United Kingdom", "1850"}

We can see the unordered characteristic of the set when we call out the set:

In [36]: Father_of_chemical_engineering
Out[36]: {'1850', 'George Davis', 'United Kingdom'}

We can add new values to a set using add:

In [37]: Father_of_chemical_engineering.add(1906)

In [38]: Father_of_chemical_engineering
Out[38]: {'1850', 1906, 'George Davis', 'United Kingdom'}

Frozenset: They are nothing but immutable sets. We cannot add or remove values from a frozenset, once it is created. They are sometimes used as dictionary keys since they are immutable.

### 6. Boolean Type ("bool")

The bool() function allows you to evaluate any value and give you True or False in return. The following values are considered false for bool: None, False, Zero of any numeric type (0, 0.0, 0j), empty sequence, empty mapping, etc.

---

<!-- PDF page 833 -->

In [41]: bool(0)
Out[41]: False

In [42]: bool(Father_of_chemical_engineering)
Out[42]: True

Another way to use bool is by using the built-in Boolean function:

In [43]: print(10 > 9)
True
In [44]: print(10 == 9)
False

### 7. Binary Type ("bytes," "bytearray," "memoryview")

Bytes command can convert objects into byte objects or create empty byte object of the specified size. The resulting byte objects are immutable.

Bytearray are the same as bytes but are mutable.

Memoryview returns a memoryview object from bytes and bytearray. The resulting object can be obtained via slicing without copying the entire set of data.

### B.5 Functions and Loops in Python

Functions are blocks of code that perform specific tasks in Python. Generally, there are two types of functions: in-built functions and user-defined functions. As the name suggests, in-built functions are prebuilt functions, which can be directly used or called in a Python script. For instance, we used 'pow' function before in order to use exponentials to define Avogadro's number. The pow function is a built-in function.

In this section, we learn how to build user-defined functions. A function is defined by the def command. We build a function called my_first_function below:

 $$ \begin{aligned}def&my\_{f}irst\_{f}unction(x):\\&\quad return x^{**}2-4^{*}x+2^{*}x^{**}3\end{aligned} $$ 

After we save the function in a script, we can call it in the console window for different values of x as shown below:

In [3]: print(my_first_function(3))
51
In [4]: print(my_first_function(1))
-1

Functions are very useful in solving different linear and nonlinear equations using Python.

---

<!-- PDF page 834 -->

Loops are used to iterate over a sequence type, allowing us to execute a command over and over.

#### B.5.1 “For loop” Example

Father_of_chemical_engineering = {"George_Davis", "United_Kingdom", "1850"}
for x in Father_of_chemical_engineering:
    print(x)

1850
George_Davis
United_Kingdom

“For loop” is generally used to iterate over a sequence of numbers using range. We can use “for loop” for the function we built above as follows:

for x in range(1,6,1):
    print(my_first_function(x))

Here we calculate ‘my_first_function’ for the numbers 1–5, and get the following results:

-1
12
51
128
255

#### B.5.2 "While loop" Example

x=0
while (x<6):
    print(my_first_function(x))
    x=x+1

Using this loop, we calculate ‘my_first_function’ till the conditional statement x<6 is met (0 to 5). We get:

0
-1
12
51
128
255

With “while loop,” we can execute a set of statements if the condition for the loop is true.

---

<!-- PDF page 835 -->

#### B.5.3 “Break” and “Continue” Statement Example

for val in "Engineering":
    if val == "e":
        break
    print(val)

E
n
g
i
n

“Break” statement terminates the loop containing it and is used to control the flow of the program.

Similarly, “continue” statement instructs a loop to continue to the next iteration. For example:

for val in "Engineering":
    if val == "e":
        continue
    print(val)

E
n
g
i
n
r
i
n
g

<div style="text-align: center;">We can see that the output is everything other than the letter 'e'.</div>


### B.6 Libraries in Python

A library is a collection of modules or a set of precombined codes that can be used iteratively to reduce the time required to implement a function or code. They are reusable resources, which help improve effectiveness and efficiency within Python. Python by default has a standard library, which is a collection of exact syntax, token, and semantics of Python. With over 200 core modules, the Python standard library provides users with several data types, text processing, mathematical, and generic operational modules.

Because of its popularity, Python has an ocean of open-source libraries under its umbrella. We look at some of the libraries popular with chemical engineers:

---

<!-- PDF page 836 -->

#### B.6.1 Chemics

Chemics (https://github.com/chemics/chemics) is a Python library created by Wiggins et al. used for basic operational tools for chemical reactor engineering. This library allows users to perform several operations, like calculating dimensionless numbers, gas heat capacities, gas thermal conductivities, mass transfer correlations, transport velocities, pressure drops, and molecular weights.

The library is a handy tool for chemical engineers, who rely on multiple tables for such calculations. The library allows for the fast and efficient implementation of several useful chemical engineering formulas.

Here is an example how we calculate the Archimedes number for fluid transport

We know Archimedes number is a dimensionless number used to determine the motion of fluids due to density differences. It is the ratio of gravitational forces to viscous forces.

It is given by the formula:

 $$ Ar=\frac{d_{p}^{3}\rho_{g}\left(\rho_{s}-\rho_{g}\right)g}{\mu^{2}} $$ 

where  $ d_{p} $ is the particle diameter,  $ \rho_{g} $ is the gas density,  $ \rho_{s} $ is the solid density,  $ \mu $ is the dynamic viscosity, and g is the local external field like gravitational acceleration.

For  $ d_p = 0.001 $ (m),  $ \rho_g = 910 $ (kg/m $ ^3 $),  $ \rho_s = 2500 $ (kg/m $ ^3 $), and  $ \mu = 0.001307 $ (kg/(m·s)):

In [15]: import chemicals as ch
...: ch.archimedes(0.001,910,2500,0.001307)
Out[15]: 8309.14521243683

#### B.6.2 Fluids

Fluids (https://pythonlang.dev/repo/calebbell-fluids/) is another open-source library for chemical engineers, created by Bell et al. [2]. This vast library covers many essential tools for chemical engineers, ranging from piping, fittings, pumps, tanks, two-phase flows, control valve sizing, pressure drop calculations, etc.

As an example, we solve for the mass flow rate (in kg/s) of an isothermal compressible gas flowing through a pipe. The formula used for the calculation is:

 $$ \dot{m}^{2}=\frac{\left(\frac{\pi D^{2}}{4}\right)^{2}\rho_{\mathrm{avg}}\left(P_{1}^{2}-P_{2}^{2}\right)}{P_{1}\left(f_{d}\frac{L}{D}+2\ln\frac{P_{1}}{P_{2}}\right)} $$ 

where  $ \rho_{avg} $ is the average density of gas in pipe,  $ f_{d} $ is Darcy friction factor,  $ P_{1} $ and  $ P_{2} $ are the inlet and outlet pressures from pipe, L is the length of the pipe, D is the inner diameter of the pipe, and  $ \dot{m} $ is the mass flow rate of gas through the pipe.

For a gas with average density of 11.3 kg/m $ ^{3} $ flowing through a 1km long pipe with inner diameter of 0.5m, initially at 10 bar pressure going downstream to a pressure of 9 bar, we calculate the mass flow rate as follows:

In [16]: import fluids
...: fluids.isothermal_gas(rho=11.3,fd=0.00185,P1=1E6,P2=9E5,
                    L=1000,D=0.5)
Out[16]: 145.4847572636031

---

<!-- PDF page 837 -->

Here, we input the specifications in SI units and use 0.00185 as the Darcy factor. The same methodology can be used to find different variables in the formula. For example, to find the downstream pressure for the same pipe with a flow rate of 250 kg/s:

In [18]: fluids.isothermal_gas(rho=11.3,fd=0.00185,P1=1E6,L=1000,D=0.5,m=250)

Out[18]: 541423.4532578246

We get a downstream pressure of 5.4 bars or 541423.45 pascals.

#### B.6.3 TensorFlow

TensorFlow is a Python library created by the Google Brain Team used to create deep-learning models directly or by using wrapper libraries like Keras [3]. TensorFlow allows for a series of operations on tensors; tensors are mathematical objects that can be used to describe physical properties, like scalars and vectors. Since neural networks are easily expressed as computational graphs, they can be implemented using a series of operations on Tensors using TensorFlow.

Some of the features that make TensorFlow an ideal deep-learning library are flexibility, large community, open-source, visual construct, parallel neural network training, etc. Such features, as well as optimizing strategies like XLA (accelerated linear algebra) for compiling, make TensorFlow a useful library for building and optimizing deep neural networks, as shown in Chapter 10.

#### B.6.4 Scikit-learn (Sklearn)

Scikit-learn is a machine-learning library created by Cournpeau et al. [4]. It provides the users with a plethora of supervised and unsupervised machine-learning algorithms for different classification, regression, and clustering tasks. It covers algorithms like K-nearest neighbors, Support Vector Machine (SVM), and random forests.

Some of the features of Scikit-learn, which make it a standard for implementing some machine-learning algorithms are availability of model-evaluation techniques like cross-validation, unsupervised learning algorithms like factor analysis, unsupervised neural networks, and principal component analysis.

#### B.6.5 Numpy

Numpy is one of the most fundamental libraries in Python, offering support for multidimensional arrays and matrices with a large collection of mathematical functions to operate on these arrays/matrices. It was created by Oliphant et al. and is extensively used for array creation and manipulation [5].

We can use the Numpy interface for expressing images, sound waves, and other binary raw systems as an array of real numbers. Arrays are collections of values that can have one or more dimensions. A Numpy array of one dimension is called a vector, while one with two dimensions is called a matrix. With Numpy arrays, we can perform element-wise operations, which are not possible using Python lists.

---

<!-- PDF page 838 -->

#### B.6.6 Pandas

Similar to Numpy, Pandas is another popular library used to handle data as dataframes created by McKinney et al. [6]. Pandas is widely used for most data analysis due to its flexible and extremely thorough toolkit for data manipulation. It allows users to reshape and pivot datasets with flexibility and works well with dynamic data. In addition, it also allows for label-based data slicing, indexing, and subsetting.

Pandas library can be used to import or export data from/to Microsoft Excel, making it a very handy tool for data-related operations. Figure B.6 shows a basic step to read data from an excel file using Pandas:

In [3]: import pandas as pd
...: excel_file='HDPE_trainingdata.xlsx'
...: dataset= pd.read_excel(excel_file)
...: dataset.head()

Out[3]:
Time    CAT1    C21    H21    HX1    C22    C42    HX2    H22    Melt_index
0.00    255.31    7000.0    8.0    15000.0    7000.0    1000.0    2000.0    1.0    11.6419
1.02    255.31    7000.0    8.0    15000.0    7000.0    1000.0    2000.0    1.0    11.6420
2.04    255.31    7000.0    8.0    15000.0    7000.0    1000.0    2000.0    1.0    11.6421
3.06    255.31    7000.0    8.0    15000.0    7000.0    1000.0    2000.0    1.0    11.6421
4.08    255.31    7000.0    8.0    15000.0    7000.0    1000.0    2000.0    1.0    11.6421

<div style="text-align: center;">Figure B.6 The code to read data from an Excel file.</div>


We use head() to look at the first few rows of our dataset.

#### B.6.7 Matplotlib

Matplotlib is a widely used 2D plotting library created by Hunter et al. for creating static, animated, and interactive visualizations in Python [7]. It is used to produce publication-quality figures by using Python scripts. We can use Matplotlib to generate a variety of data visualization tools like plots, histograms, bar charts, error charts, and scatterplots. We can also use Matplotlib as a state-based interface by using “matplotlib.pyplot,” which provides users with a MATLAB-like way of plotting.

Figure B.7 shows the code to plot a line plot using Matplotlib.pyplot, and Figure B.8 displays the resulting plot.

import matplotlib.pyplot as plt

dataset.plot(x='Time', y='CAT1', xlabel='Time', ylabel='Catalyst flow rate', color='red', figsize=(10,6), title='Catalyst flow rate over time')

plt.show()

<div style="text-align: center;">Figure B.7 The code to plot a line.</div>


By using these libraries and many other open-source libraries, readers can handle several basic and complex engineering problems in Python with ease. This appendix introduces the readers to the fundamentals of Python, which is the most versatile and well-rounded programming language for chemical engineering applications.

---

<!-- PDF page 839 -->

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Time</th><th style='text-align: center;'>CAT1</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>255.25</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>255.25</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>255.25</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>254.00</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>254.00</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>254.00</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>255.00</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>255.00</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>255.00</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>255.50</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>255.50</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>255.50</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>255.50</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>255.75</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure B.8 Line plot for catalyst flow over time using Matplotlib.</div>


### B.7 Machine-learning Algorithms with Python: Hyperparameter Optimization and Sample Codes

In this section, we summarize some popular machine-learning algorithms that we discussed in Chapter 10, their standard algorithm parameters (called hyperparameters), commonly used values for parameters, methods for finding the “optimum” parameter values (called hyperparameter optimization), and the sample Python codes. We present these in Table B.1, followed by Codes B.1–B.8 below.

<div style="text-align: center;">Table B.1 Machine-learning algorithm, standard parameters, commonly used values of parameters, method to find the "optimum" parameters, and Python code.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Algorithm</td><td style='text-align: center; word-wrap: break-word;'>Standard parameters</td><td style='text-align: center; word-wrap: break-word;'>Commonly used values for parameters</td><td style='text-align: center; word-wrap: break-word;'>Method for selecting parameters</td><td style='text-align: center; word-wrap: break-word;'>Sample code</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Simple linear regression</td><td style='text-align: center; word-wrap: break-word;'>N/A</td><td style='text-align: center; word-wrap: break-word;'>N/A</td><td style='text-align: center; word-wrap: break-word;'>N/A</td><td style='text-align: center; word-wrap: break-word;'>Code B.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>K-nearest neighbor</td><td style='text-align: center; word-wrap: break-word;'>n_neighbors, weights, algorithm, leaf_size, p, metric</td><td style='text-align: center; word-wrap: break-word;'>n_neighbors= $ [3,5,10,15,20] $, weights=uniform, algorithm=auto, leaf_size=30, p=2, metric=&#x27;minkowski&#x27;</td><td style='text-align: center; word-wrap: break-word;'>GridSearch</td><td style='text-align: center; word-wrap: break-word;'>Code B.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Decision trees</td><td style='text-align: center; word-wrap: break-word;'>criterion, splitter, max_depth, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_features</td><td style='text-align: center; word-wrap: break-word;'>criterion=mse, splitter=best, max_depth= $ [2,3,4,5,6,7,8,9,20,50,100] $, min_samples_split= $ [2,5,10,15,20,40] $, min_samples_leaf= $ [1,3,5,10,15,20] $, min_weight_fraction_leaf=0, max_features=auto</td><td style='text-align: center; word-wrap: break-word;'>GridSearch</td><td style='text-align: center; word-wrap: break-word;'>Code B.3</td></tr></table>

---

<!-- PDF page 840 -->

<div style="text-align: center;">Table B.1 (Continued)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Algorithm</td><td style='text-align: center; word-wrap: break-word;'>Standard parameters</td><td style='text-align: center; word-wrap: break-word;'>Commonly used values for parameters</td><td style='text-align: center; word-wrap: break-word;'>Method for selecting parameters</td><td style='text-align: center; word-wrap: break-word;'>Sample code</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Random forest</td><td style='text-align: center; word-wrap: break-word;'>n_estimators, criterion, max_depth, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_features, bootstrap, oob_score,</td><td style='text-align: center; word-wrap: break-word;'>n_estimators=[100,200,500,1000, 2000], criterion=mse, max_depth=[2,3,4, 5,6,7,8,9,20,50,100], min_samples_split=[2,5,10,15,20,40], min_samples_leaf=[1,3,5,10,15,20], min_weight_fraction_leaf=0, max_features=auto</td><td style='text-align: center; word-wrap: break-word;'>GridSearch</td><td style='text-align: center; word-wrap: break-word;'>Code B.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Partial least squares</td><td style='text-align: center; word-wrap: break-word;'>n_components</td><td style='text-align: center; word-wrap: break-word;'>n_components=[Integer value]</td><td style='text-align: center; word-wrap: break-word;'>Obtained by calculating Q2_score and R2_score. As the scores stop increasing, we pick the number of components associated with the score.</td><td style='text-align: center; word-wrap: break-word;'>Code B.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Neural network/ deep neural networks</td><td style='text-align: center; word-wrap: break-word;'>Model, activation, loss, optimizer, batch_size,epochs, number_of_hidden_layers, input_layer_neurons, output_layer_neurons, hidden_layer_neurons, kernel_initializer</td><td style='text-align: center; word-wrap: break-word;'>Model=Sequential(), activation=relu, loss=mean_squared_error, optimizer=adam, batch_size=[1, size of training set, 32,64, 128], epochs=[10,100,500,1000], number_of_hidden_layers=[1,2,integer value], input_layer_neurons=number of input variables, output_layer_neurons=number of output variables, hidden_layer_neurons=2/3 of the input layer plus output layer neuron, kernel_initializer=normal</td><td style='text-align: center; word-wrap: break-word;'>Obtained by a thorough understanding of the data structure, gridsearch, understanding the computational limitations, and trial/error.</td><td style='text-align: center; word-wrap: break-word;'>Code B.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Support vector machine</td><td style='text-align: center; word-wrap: break-word;'>kernel, gamma, C,</td><td style='text-align: center; word-wrap: break-word;'>kernel=rbf, gamma=[0.001,0.01,0.1, 0.2,0.5, 0.6, 0.9], C=[10, 100, 1000], 10000]</td><td style='text-align: center; word-wrap: break-word;'>GridSearch and selecting suitable kernel for dataset</td><td style='text-align: center; word-wrap: break-word;'>Code B.7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Principal component analysis</td><td style='text-align: center; word-wrap: break-word;'>n_components</td><td style='text-align: center; word-wrap: break-word;'>n_components=[Integer value]</td><td style='text-align: center; word-wrap: break-word;'>Obtained by using scree plot, the number of components retained have eigenvalues &gt;1</td><td style='text-align: center; word-wrap: break-word;'>Code B.8</td></tr></table>

---

<!-- PDF page 841 -->

#### B.8 Sample Codes for Table B.1

### Code B.1 Linear Regression

from sklearn.linear_model import LinearRegression
import pandas as pd
import warnings
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
dataset=pd.read_excel("LDPE dataset_KevinMcGregor.xlsx",encoding='unicode_escape')
dataset=dataset.drop(36,axis=0)
X=dataset.iloc[0:39,1:23].values
y=dataset.iloc[0:39,23:29].values
# define model
model = LinearRegression()
model.fit(X,y)
X_test=dataset.iloc[39:49,1:23].values
y_test=dataset.iloc[39:49,23:29].values
y1_test=y_test[:,0:1]
y2_test=y_test[:,1:2]
y3_test=y_test[:,2:3]
y4_test=y_test[:,3:4]
y5_test=y_test[:,4:5]
y6_test=y_test[:,5:6]
y_cv = cross_val_predict(model, X_test, y_test, cv=10)
y_cv1=y_cv[:,0:1]
y_cv2=y_cv[:,1:2]
y_cv3=y_cv[:,2:3]
y_cv4=y_cv[:,3:4]
y_cv5=y_cv[:,4:5]
y_cv6=y_cv[:,5:6]
score=r2_score(y_test, y_cv)
score1=r2_score(y1_test, y_cv1)
score2=r2_score(y2_test, y_cv2)
score3=r2_score(y3_test, y_cv3)
score4=r2_score(y4_test, y_cv4)
score5=r2_score(y5_test, y_cv5)
score6=r2_score(y6_test, y_cv6)
rmse=np.sqrt(mean_squared_error(y_test, y_cv))
rmse1=np.sqrt(mean_squared_error(y1_test, y_cv1))
rmse2=np.sqrt(mean_squared_error(y2_test, y_cv2))
rmse3=np.sqrt(mean_squared_error(y3_test, y_cv3))
rmse4=np.sqrt(mean_squared_error(y4_test, y_cv4))
rmse5=np.sqrt(mean_squared_error(y5_test, y_cv5))
rmse6=np.sqrt(mean_squared_error(y6_test, y_cv6))

### Code B.2 K-Means Clustering

from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import warnings
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

---

<!-- PDF page 842 -->

dataset=pd.read_excel("LDPE dataset_KevinMcgregor.xlsx",encoding='unicode_escape')
dataset=dataset.drop(36,axis=0)
X=dataset.iloc[0:39,1:23].values
y=dataset.iloc[0:39,23:29].values
# define model
model = KNeighborsRegressor(n_neighbors=9)
model.fit(X,y)
X_test=dataset.iloc[39:49,1:23].values
y_test=dataset.iloc[39:49,23:29].values
y1_test=y_test[:,0:1]
y2_test=y_test[:,1:2]
y3_test=y_test[:,2:3]
y4_test=y_test[:,3:4]
y5_test=y_test[:,4:5]
y6_test=y_test[:,5:6]
y_cv = cross_val_predict(model, X_test, y_test, cv=10)
y_cv1=y_cv[:,0:1]
y_cv2=y_cv[:,1:2]
y_cv3=y_cv[:,2:3]
y_cv4=y_cv[:,3:4]
y_cv5=y_cv[:,4:5]
y_cv6=y_cv[:,5:6]
score=r2_score(y_test,y_cv)
score1=r2_score(y1_test,y_cv1)
score2=r2_score(y2_test,y_cv2)
score3=r2_score(y3_test,y_cv3)
score4=r2_score(y4_test,y_cv4)
score5=r2_score(y5_test,y_cv5)
score6=r2_score(y6_test,y_cv6)
rmse=np.sqrt(mean_squared_error(y_test,y_cv))
rmse1=np.sqrt(mean_squared_error(y1_test,y_cv1))
rmse2=np.sqrt(mean_squared_error(y2_test,y_cv2))
rmse3=np.sqrt(mean_squared_error(y3_test,y_cv3))
rmse4=np.sqrt(mean_squared_error(y4_test,y_cv4))
rmse5=np.sqrt(mean_squared_error(y5_test,y_cv5))
rmse6=np.sqrt(mean_squared_error(y6_test,y_cv6))

### Code B.3 Decision Trees

from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import warnings
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
dataset=pd.read_excel("LDPE dataset_KevinMcgregor.xlsx",encoding='unicode_escape')
dataset=dataset.drop(36,axis=0)
X=dataset.iloc[0:39,1:23].values
y=dataset.iloc[0:39,23:29].values
# define model
model = DecisionTreeRegressor()
model.fit(X,y)
X_test=dataset.iloc[39:49,1:23].values
y_test=dataset.iloc[39:49,23:29].values
y1_test=y_test[:,0:1]
y2_test=y_test[:,1:2]
y3_test=y_test[:,2:3]

---

<!-- PDF page 843 -->

y4_test=y_test[:,3:4]
y5_test=y_test[:,4:5]
y6_test=y_test[:,5:6]
y_cv = cross_val_predict(model, X_test, y_test, cv=10)
y_cv1=y_cv[:,0:1]
y_cv2=y_cv[:,1:2]
y_cv3=y_cv[:,2:3]
y_cv4=y_cv[:,3:4]
y_cv5=y_cv[:,4:5]
y_cv6=y_cv[:,5:6]
score= r2_score(y_test, y_cv)
score1= r2_score(y1_test, y_cv1)
score2= r2_score(y2_test, y_cv2)
score3= r2_score(y3_test, y_cv3)
score4= r2_score(y4_test, y_cv4)
score5= r2_score(y5_test, y_cv5)
score6= r2_score(y6_test, y_cv6)
rmse = np.sqrt(mean_squared_error(y_test, y_cv))
rmse1 = np.sqrt(mean_squared_error(y1_test, y_cv1))
rmse2 = np.sqrt(mean_squared_error(y2_test, y_cv2))
rmse3 = np.sqrt(mean_squared_error(y3_test, y_cv3))
rmse4 = np.sqrt(mean_squared_error(y4_test, y_cv4))
rmse5 = np.sqrt(mean_squared_error(y5_test, y_cv5))
rmse6 = np.sqrt(mean_squared_error(y6_test, y_cv6))

### Code B.4 Random Forest Ensembled Learning

from sklearn.ensemble import RandomForestRegressor as rf
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
dataset=pd.read_excel ("Mastermerged.xlsx",encoding='unicode_escape')
traindataset=pd.read_excel ("TrainAll.xlsx",encoding='unicode_escape')
testdataset=pd.read_excel ("TestAll.xlsx",encoding='unicode_escape')
testA=pd.read_excel ("TestA.xlsx",encoding='unicode_escape')
testB=pd.read_excel ("TestB.xlsx",encoding='unicode_escape')
testC=pd.read_excel ("TestC.xlsx",encoding='unicode_escape')
testH=pd.read_excel ("TestH.xlsx",encoding='unicode_escape')
X1=dataset.iloc[:,0:12].values
y=dataset.iloc[:,13:14].values
from sklearn import preprocessing
X=preprocessing.scale(X1)
X_train1=traindataset.iloc[:,0:12].values
X_train=preprocessing.scale(X_train1)
y_train=traindataset.iloc[:,13:14].values
X_test1=testdataset.iloc[:,0:12].values
X_test=preprocessing.scale(X_test1)
y_test=testdataset.iloc[:,13:14].values
X_testA1=testA.iloc[:,0:12].values
X_testA=preprocessing.scale(X_testA1)
y_testA=testA.iloc[:,13:14].values
X_testB1=testB.iloc[:,0:12].values
X_testB=preprocessing.scale(X_testB1)
y_testB=testB.iloc[:,13:14].values
X_testC1=testC.iloc[:,0:12].values
X_testC=preprocessing.scale(X_testC1)
y_testC=testC.iloc[:,13:14].values
X_testH1=testH.iloc[:,0:12].values

---

<!-- PDF page 844 -->

X_testH=preprocessing.scale(X_testH1)
Y_testH=testH.iloc[:,13:14].values

rfr = rf(n_estimators = 1000, random_state = 423, min_samples_split = 2, min_samples_leaf = 4, max_features='sqrt', max_depth=50, bootstrap='True')
# Train the model on training data
rfr.fit(X_train, y_train);
predictions = rfr.predict(X_test)
# Calculate the absolute errors
errors = np.sqrt(mean_squared_error(predictions, y_test))

# Print out the mean absolute error (mae)
print('Root Mean Squared Error:', round(errors, 2), 'L.)
from pprint import pprint

# Look at parameters used by our current forest
print('Parameters currently in use:\n')
pprint(rf().get_params())
from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [200]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [5,10,20,50]
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth, 'min_samples_split': min_samples_split, 'min_samples_leaf': min_samples_leaf, 'bootstrap': bootstrap}

pprint(random_grid)
# Use the random grid to search for best hyperparameters
# First create the base model to tune
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf(), param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(X_train, y_train)
rf_random.best_params_
print(rf_random.best_params_)

### Code B.5 Partial Least Squares:

from sklearn.cross_decomposition import PLSRegression
import pandas as pd
import warnings
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
dataset=pd.read_excel("LDPE dataset_KevinMcgregor.xlsx",encoding='unicode_escape')

---

<!-- PDF page 845 -->

dataset=dataset.drop(36,axis=0)
X=dataset.iloc[0:39,1:23].values
y=dataset.iloc[0:39,23:29].values
# define model
model = PLSRegression(n_components=8)
model.fit(X, y)
X_test=dataset.iloc[39:49,1:23].values
y_test=dataset.iloc[39:49,23:29].values
y1_test=y_test[:,0:1]
y2_test=y_test[:,1:2]
y3_test=y_test[:,2:3]
y4_test=y_test[:,3:4]
y5_test=y_test[:,4:5]
y6_test=y_test[:,5:6]
y_cv = cross_val_predict(model, X_test, y_test, cv=10)
y_cv1=y_cv[:,0:1]
y_cv2=y_cv[:,1:2]
y_cv3=y_cv[:,2:3]
y_cv4=y_cv[:,3:4]
y_cv5=y_cv[:,4:5]
y_cv6=y_cv[:,5:6]
score=r2_score(y_test, y_cv)
score1=r2_score(y1_test, y_cv1)
score2=r2_score(y2_test, y_cv2)
score3=r2_score(y3_test, y_cv3)
score4=r2_score(y4_test, y_cv4)
score5=r2_score(y5_test, y_cv5)
score6=r2_score(y6_test, y_cv6)

### Code B.6 Neural Network

import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
dataset=pd.read_csv('Master batches.csv',encoding='unicode_escape')
X=dataset.iloc[:,0:11].values
Y=dataset.iloc[:,11:12].values
## define base model
#def baseline_model():
#    # create model
#    model = Sequential()
#    model.add(Dense(11, input_dim=11, kernel_initializer='normal', activation='relu'))
#    model.add(Dense(1, kernel_initializer='normal'))
#    # Compile model
#    model.compile(loss='mean_squared_error', optimizer='adam')
#    return model
## fix random seed for reproducibility
seed = 7
#np.random.seed(seed)
## evaluate model with standardized dataset
#estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)
#kfold = KFold(n_splits=10, random_state=seed)
#results = cross_val_score(estimator, X, Y, cv=kfold)

---

<!-- PDF page 846 -->

## Appendix B Introduction to Python for Chemical Engineers

#print("Results: %.2f (%.2f) MSE" & (results.mean(), results.std()))
#
#np.random.seed(seed)

#estimators = []

#estimators.append(('standardize', StandardScaler())
#estimators.append(('mlp', KerasRegressor(build_fn=baseline_model, epochs=50, batch_size=5, verbose=0)))
#pipeline = Pipeline(estimators)
#kfold = KFold(n_splits=10, random_state=seed)
#results = cross_val_score(pipeline, X, Y, cv=kfold)
#print("Standardized: %.2f (%.2f) MSE" & (results.mean(), results.std()))

# define the model
def larger_model():
    # create model
    model = Sequential()
    model.add(Dense(11, input_dim=11, kernel_initializer='normal', activation='relu'))
    model.add(Dense(5, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

np.random.seed(seed)

estimators = []
estimators.append(('standardize', StandardScaler())
estimators.append(('mlp', KerasRegressor(build_fn=larger_model, epochs=100, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Larger: %.2f (%.2f) MSE" & (results.mean(), results.std()))

#def wider_model():
#    # create model
#    model = Sequential()
#    model.add(Dense(20, input_dim=11, kernel_initializer='normal', activation='relu'))
#    model.add(Dense(1, kernel_initializer='normal'))
#    # Compile model
#    model.compile(loss='mean_squared_error', optimizer='adam')
#    return model

#np.random.seed(seed)

#estimators = []
#estimators.append(('standardize', StandardScaler())
#estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=100, batch_size=5, verbose=0)))
#pipeline = Pipeline(estimators)
#kfold = KFold(n_splits=10, random_state=seed)
#results = cross_val_score(pipeline, X, Y, cv=kfold)
#print("Wider: %.2f (%.2f) MSE" & (results.mean(), results.std()))

#fold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Larger: %.2f (%.2f) MSE" & (results.mean(), results.std()))

---

<!-- PDF page 847 -->

### Code B.7 Support Vector Machine

from sklearn.model_selection import train_test_split
import pandas as pd

dataset=pd.read_csv('Master batches.csv',encoding='unicode_escape')
X=dataset.iloc[:,0:11].values
Y=dataset.iloc[:,11:12].values

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.2,
                                  random_state=422)
from sklearn.model_selection import GridSearchCV
import math
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
model = SVR(kernel='rbf', C=1e3, gamma = 0.5, epsilon = 0.01)
print(model)
model.fit(X_train,y_train)
pred_y = model.predict(X_test)
mse = mean_squared_error(pred_y,y_test)
print("Mean Squared Error:",mse)
rmse = math.sqrt(mse)
print("Root Mean Squared Error: ",rmse)
# Tuning of parameters for regression by cross-validation
K = 10  # Number of cross validations

# Parameters for tuning
parameters = [{'kernel': ['rbf'], 'gamma': [0.1, 0.2, 0.5, 0.6, 0.9], 'C':
                              [10, 100, 1000, 10000]}]
print("Tuning hyper-parameters")
from sklearn.metrics import make_scorer
scorer = make_scorer(mean_squared_error, greater_is_better=False)
svr=GridSearchCV(SVR(epsilon=0.01), parameters, cv=K, scoring=scorer)
svr.fit(X,Y)
# Checking the score for all parameters
print("Grid scores on training set.")
means = svr.cv_results_['mean_test_score']
stds = svr.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, svr.cv_results_['params]):
    print("%0.3f (+/-%0.03f) for %r% (mean, std*2, params))

### Code B.8 Principal Component Analysis

from sklearn.decomposition import PCA
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
dataset=pd.read_excel("LDPE dataset_KevinMcGregor.xlsx",encoding='unicode_escape')
dataset=dataset.drop(36,axis=0)
X=dataset.iloc[0:39,1:23].values
model =PCA(n_components=2)
model.fit_transform(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_

---

<!-- PDF page 848 -->

## References

1 https://spectrum.ieee.org/top-programming-languages/

2 Caleb Bell (2023). Fluids: Fluid dynamics component of Chemical Engineering Design Library (ChEDL). https://github.com/CalebBell/fluids (accessed 25 March 2023).

3 Abadi, M., Barham, P., Chen, J. et al. TensorFlow: A system for large-scale machine learning. Proceedings of the 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI '16), Savannah, GA, USA, 2016.

4 Pedregosa, F., Varoquaux, G., Gramfort, A. et al. (2011). Scikit-learn: machine learning in Python. Journal of Machine Learning Research 12: 2825–2830.

5 Harris, C.R., Millman, K.J., van der Walt, S.J. et al. (2020). Array programming with numpy. Nature 585 (7825): 357–362.

McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, Austin, TX, June 28 to

7 Hunter, J. (2007). Matplotlib: a 2D graphics environment. Computing in Science & Engineering 9: 90. https://doi.org/10.1109/MCSE.2007.55.

---

<!-- PDF page 849 -->

## Index

## a

accumulated prediction error (ACPRER)

405

activation functions 587–589, 594, 679

segment-based vs. species-based mole fraction 43–44

vapor-liquid equilibrium

using gas-phase fugacity coefficient

43

Henry components for 46–50

for ideal vapor and nonideal liquid

phase 42–43

using liquid-phase activity coefficient

43

vs. equation of state models 38

Adam optimizer 590, 591, 630, 636, 637

adaptive boosting (AdaBoost) algorithm 534, 578

advanced process control (APC) 382 dependent variables 383 independent variables 382–383 integrating variable (ramp variable) 383–385 model-based predictions 387–389 multivariable dynamic step-response model 385–389 MV and CV target determination, steady-state economic optimization 389–392

online feedback correction 388 polyolefin manufacturing optimization 28–31

of polyolefin process 381–475

vs. traditional PID control 386–387

unit-step response curve 383



agent, defined 539

agglomerative hierarchical clustering (AHC) 572

AI-driven hybrid model 35, 657, 685

AlphaGo program 539

alternative basic network configuration,

using bias inputs 585–586

Anaconda 740, 741

Anaconda Navigator 740, 741

anionic copolymerization 268,

293–318

anionic polymerization systems 293

Archimedes number 748

Artificial Intelligence 31, 477, 533, 534, 656

reference books 540

Aspen AI Model Builder 685

model building 687

model validation results 687

variable interface 686

Aspen Apollo 29-31

Aspen Inferential Qualities 31

Aspen Maestro model workflow for

DMC3

data mining 472

input correlation detection 473

model creation 474