# Phishing-Domain-Detection-using-Machine-Learning-Technique

### Problem Statement

Phishing is a type of cyberattack where attackers attempt to trick individuals into divulging sensitive information, such as passwords or credit card details, by posing as a trustworthy entity or source. Phishing attacks can take many forms, including emails, text messages, phone calls, or even fake websites.

Phishing detection refers to the process of identifying and preventing these types of attacks. It involves using various methods, such as machine learning algorithms or rule-based systems, to analyze the characteristics of a message or website and determine whether it is legitimate or fraudulent.

Phishing detection is critical for protecting individuals and organizations from cyber threats. In recent years, there has been an increase in the frequency and sophistication of phishing attacks, making it even more important to implement effective detection methods.

### Goal:

This is a Classification problem, in which selected features [Using Feature Engineering methods]are given as inputs to the model and the respective model classify whether the URL is Legitimate website [0] or Phishing website [1].

### Dataset Source: ['dataset_full.csv' used]

https://data.mendeley.com/datasets/72ptz43s9v/1


### Proposed Solution Approach:

First of all, Exploratory Data Analysis (EDA), Feature Engineering (FE) and Feature Selection (FS) [if required] using various python based libraries [pandas, numpy etc.] on downloaded data set from the above mentioned link will be performed. Visualization tools [matplotlib, seaborn etc.] will aid to get a better understanding of the data that we are working with. Afterwards, distinct regression models wiil be created. Finally, We will evaluate these models using distinct perfomance metrics plus will try to get best Hyper prameters using Grid Search CV apporach and will select the best performing(most suitable) model for this specific dataset for classification whether URL is Phishing or Non-phishing.

### Tech Stack Used

1. Python 
2. Pycharm as IDE & Jupyter Notebook for Analysis
3. Machine learning algorithms 
4. MongoDB
5. FastAPI [Back End]
6. Streamlit [UI Interface/Front End]
7. Docker [Docker Desctop and Docker hub]

### Most Suitable Machine Learning Model [As per given Dataset] 

Random Forest Classifier [Testing Accuracy: 97.8%]

### Infrastructure Required for Deployment.

1. Docker hub
2. AWS Elastic Beanstalk (EB)

## How to run?

Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, Elastic Beanstalk (EB).

## Data Collections
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)


## Project Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)


## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)


### Step 1 - Clone the repository
```bash
git clone https://github.com/ansariparvej/Phishing-Domain-Detection.git
```

### Step 2 - Create a conda environment after opening the repository

```bash
conda create -n Phishing_Domain_Detection python=3.8.16 -y
```

```bash
conda activate Phishing_Domain_Detection
```

### Step 3 - Install the requirements
```bash
pip3 install -r requirements.txt
```

### Step 4 - Run the application server [Using Fast API]
```bash
python main.py
```

### Step 5 - Train application 
```bash
http://localhost:8080/train

```

### Step 6 - Run the application server [Using Fast API]
```bash
streamlit run app.py
```

### Step 7 - Prediction application [Using Streamlit/UI]
```bash
http://localhost:8501

```

## For Application Deployment, REFER: >> Deployment_Steps.pdf file.


