Anonymized credit card transactions labeled as fraudulent or genuine->
This dataset is downloaded from Kaggle.
This is a classification problem.
This dataset is huge, of 284809 lines. There are 29 independent variables
and one dependent variable (Class-> 1 for fraudulent transactions, 0 otherwise).
Since this .csv file is huge, I am not uploading it into GitHub repository.
But, one can easily download it from kaggle.

Context:
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not 
charged for items that they did not purchase.

-------------------------------------------------------------

Results:

Kernel SVM:

Accuracy of predictions for the training set = 99.97761636200049 %
Accuracy of predictions for the test set = 99.84375548611355 %


Random Forest:

Accuracy of predictions for the training set = 100 %
Accuracy of predictions for the test set =  99.95259997893332 %


--------------------------------------------------------------------
Details of Dataset:
Various columns of the dataset->
TimeNumber of seconds elapsed between this transaction and the first transaction in the dataset
V1may be result of a PCA Dimensionality reduction to protect user identities and sensitive features(v1-v28)
V2
V3
V4
V5
V6
V7
V8
V9
V10
V11
V12
V13
V14
V15
V16
V17
V18
V19
V20
V21
V22
V23
V24
V25
V26
V27
V28abc
AmountTransaction amount
Class->     1 for fraudulent transactions, 0 otherwise
