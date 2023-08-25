**Report (Machine Learning Intern Assessment Assignment)**

Date: 24/08/2023

Author: Animesh Singh

Project: Customer Churn Prediction

**Introduction:**

This report presents the development and evaluation of a customer churn prediction model. The goal of the model is to predict whether a customer is likely to churn (cancel their subscription or service) based on historical data and relevant features.

Repository: <https://github.com/animeshdebug7/Customer-Churn-Prediction>

**Dataset:**

Dataset used for the project was the one assigned as part of the task.

**Data Preprocessing:**

- First thing was to remove the ‘CustomerID’ and ‘CustomerName’ from the data as they are not useful in predicting the outcome. 
- Checking the correlation between the independent variables (Input) and the output variable.

We get the plots below that indicate that there are no direct correlations between any of the input variables with the output variable.

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.001.png "download")![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.002.png "download (1)")

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.003.png "download (2)")![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.004.png "download (3)")

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.005.png "download (4)")![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.006.png "download (5)")

![C:\Users\anime\AppData\Local\Microsoft\Windows\INetCache\Content.Word\download (6).png](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.007.png)

- Doing suitable encodings for the categorical data (Gender – LabelEncoding, 

Location – OneHotEncoding).

- Used MinMaxScaler for scaling the numeric data that have big range ('Age',  'Subscription\_Length\_Months',  'Monthly\_Bill',  'Total\_Usage\_GB').
- Added a new column Data\_Cost to estimate the difference in cost per GB data in different locations and if that affected the churn rate. 
- Did PCA to overcome the very low accuracy.

**Performance Metrics:**

Tried multiple ML algorithms and ANN (trained at max 100 epochs) for the above classification problem and the results are bad because of the data not being correlated at all.

![curly bracket Icon - Free PNG & SVG 870096 - Noun Project](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.008.png)**ANN**

**All of them gave an accuracy of ~50%**

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.009.png)**XGBoost**                           

**CatBoost**

**SVM**

**ANN (PCA)**


**Results:**

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.010.jpeg "Screenshot 2023-08-25 053625")

**Deployment:** 

- Used Flask server to deploy the model on a development level.
- Relevantly styled web-app with Input for the top 4 most import fields (reduced to 4 for the ease of use, the features aren’t correlated anyways).

![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.011.png "Screenshot (519)")    ![](Aspose.Words.290ec3bf-1ac1-4ec9-94f4-c1bbdd0dbc53.012.png "Screenshot (518)")




**Business Impact:**

The parameters that are in the data set is insufficient for predicting the churn rate for consumers. It is better to have more parameters for a business standpoint.

**Limitations:**

The limitation in this project is that the input variable of the data set is not correlated with the output variable and hence are not the right parameters for predicting churn rate.

**Future Enhancements:**

- Different parameters can be used for churn prediction.
- More data can be added so that we achieve some curve that fits the data.




