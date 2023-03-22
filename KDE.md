
# Understanding Probability Density Function (PDF) from Scratch: Parametric and Non-Parametric Approaches

**Probability Density Function (PDF)** is a fundamental concept in probability theory and statistics, which is used to describe the probability distribution of a continuous random variable. A PDF represents the likelihood of a random variable taking on a specific value or range of values. Understanding PDF is essential for a range of applications, including data analysis, modeling, and inference.

PDF can be represented using two main approaches: parametric and non-parametric. In this blog, we will delve into both approaches and understand how to create a PDF from scratch using each of them.

##  Parametric Approach:

The parametric approach involves assuming a specific functional form for the PDF and estimating its parameters. The most common parametric PDF is the Normal Distribution, also known as the Gaussian Distribution. The Normal Distribution is widely used in statistical modeling due to its simple shape and its ability to describe a wide range of natural phenomena.

The Normal Distribution PDF can be represented using the following formula:

![image](https://user-images.githubusercontent.com/55331192/227041089-74e21934-ed6d-4370-834e-40db557a1064.png)

where _μ_ represents the mean and _σ_ represents the standard deviation of the distribution.

The Normal Distribution PDF is a bell-shaped curve, with the peak at the mean value of the distribution. The standard deviation of the distribution determines the spread or width of the curve. The area under the curve represents the total probability of the distribution, which is always equal to one.

![image](https://user-images.githubusercontent.com/55331192/227042229-b65ca224-6336-436f-a6a7-e65abbbd548d.png)


##   Non-Parametric Approach:

The non-parametric approach does not assume any specific functional form for the PDF. Instead, it estimates the PDF directly from the data using a method called **Kernel Density Estimation (KDE).**

KDE involves placing a kernel function at each data point and then summing up the contributions of all kernels to estimate the PDF. The kernel function is usually a symmetric probability density function, such as the Gaussian kernel, which determines the shape of the PDF estimate.

To create a KDE from scratch, we follow the following steps:

* Choose a kernel function, such as the Gaussian kernel.
* For each data point, place a kernel function centered on that point.
* Scale each kernel function by a bandwidth parameter _h_.
* Sum up the contributions of all kernel functions to obtain the PDF estimate.

The bandwidth parameter _h_ determines the width of the kernel function and, therefore, the smoothness of the PDF estimate. A larger bandwidth parameter leads to a smoother estimate, while a smaller bandwidth parameter leads to a more variable estimate.

Here is the formula for KDE using the Gaussian kernel:

![image](https://user-images.githubusercontent.com/55331192/227041046-8449fc39-d405-4f2b-a411-77a2001cbd72.png)


where _K_ is the kernel function, _x_i_ represents the data point, _h_ is the bandwidth parameter, and _n_ is the number of data points.

![image](https://user-images.githubusercontent.com/55331192/227041769-f6cce9f4-c7f7-4790-b1de-3a4dea3b2340.png)

Follow this link to visualize kde estimation : https://samp-suman-normal-dist-visualize-app-lkntug.streamlit.app/

Conclusion:

In summary, understanding Probability Density Function is essential for a range of applications in data analysis, modeling, and inference. The PDF can be estimated using two main approaches: parametric and non-parametric. The parametric approach assumes a specific functional form for the PDF and estimates its parameters, while the non-parametric approach estimates the PDF directly from the data using Kernel Density Estimation.

In practice, both approaches have their advantages and disadvantages. The parametric approach is simple and efficient but assumes a specific functional form for the PDF. The non-parametric approach is more flexible but requires more data and is computationally intensive.

Overall, understanding both approaches is important for data analysts and statisticians to choose the most appropriate method for their specific application.
