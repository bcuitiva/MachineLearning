# Machine Learning — Web Application

A web application built with Flask that helps understand machine learning concepts in a simple way and shows real-world examples of how they are used. It includes supervised and unsupervised learning models that can be used to make real predictions and discover hidden patterns in data.

---

## Description

This project was developed as part of the Machine Learning course at Universidad de Cundinamarca.

The goal is to combine theory with practice. It not only explains concepts, but also shows how they work within the application itself. It includes real examples from different industries, concept explanations for each algorithm, and functional models that can be used to make predictions from real input data.

The backend is built with Python and Flask, while the frontend uses HTML, CSS, and Bootstrap — no external JavaScript frameworks required.

---

## Features

- Simple and easy-to-use main menu
- **4 real-world machine learning use cases:**
  - Fraud detection (PayPal)
  - Route optimization (Waze)
  - Heart disease risk prediction (Healthcare)
  - Content recommendation (Instagram)
- **Supervised Machine Learning module** with 3 algorithms:
  - **Linear Regression**
    - Basic concept explanations (variables, regression line, slope and intercept)
    - Practical exercise — body weight prediction using a real obesity dataset
    - Interactive form with results and Actual vs Predicted scatter plot
  - **Logistic Regression**
    - Basic concept explanations
    - Application — diabetes prediction using a real clinical dataset
    - Confusion matrix, ROC curve with real data, and full performance metrics
  - **Ridge Classifier** (assigned model)
    - Basic concept explanations (L2 regularization, decision boundary, advantages and limitations)
    - Application — student dropout prediction using a real academic dataset
    - Confusion matrix, ROC curve with real data, and full performance metrics
- **Unsupervised Machine Learning module** with K-Means clustering:
  - Basic concept explanations (clustering, centroids, distance metrics, convergence)
  - Manual K-Means exercise — step-by-step simulation with tables, distances and variance charts
  - **Clustering Application** — customer segmentation using a real marketing campaign dataset
    - Full data context and dataset explanation (2,216 records, 10 features)
    - Data preprocessing pipeline (null removal, feature selection, StandardScaler)
    - K-Means model training with scikit-learn
    - Cluster assignment table (first 100 records with cluster badges)
    - Cluster summary cards with per-feature averages
    - Centroids displayed in original scale
    - Scatter plot (Income vs Total Spend) with centroid markers
    - Normalised bar chart comparing feature averages across clusters
    - Business interpretation of each customer segment
- Consistent minimalist design across all pages
- Fully responsive layout

---

## Technologies Used

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Machine Learning | scikit-learn, pandas, NumPy |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Charts | Chart.js 4 |
| Typography | IBM Plex Mono, IBM Plex Sans |
| Datasets | ObesityDataSet_raw_and_data_sinthetic.csv · diabetes.csv · Predict_students_dropout.csv · marketing_campaign.csv |

---

## Installation

### Requirements

- Python 3.8 or higher
- pip

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/bcuitiva/MachineLearnig.git
```

**2. Go to the project folder**

```bash
cd MachineLearnig
```

**3. Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install flask pandas scikit-learn numpy
```

**5. Make sure all datasets are in the project root**

```
MachineLearnig/
├── ObesityDataSet_raw_and_data_sinthetic.csv
├── diabetes.csv
├── Predict_students_dropout.csv
└── marketing_campaign.csv
```

> **Note:** `marketing_campaign.csv` is a tab-separated file (TSV). Make sure it keeps the `.csv` extension and is placed at the project root alongside `app.py`.

**6. Run the application**

```bash
python app.py
```

**7. Open in your browser**

```
http://127.0.0.1:5000
```

---

## Usage

Open the application in your browser and navigate through the available sections.

**To test the Linear Regression model:**
1. Go to Supervised Machine Learning → Linear Regression → Practical Exercise
2. Fill out the form with personal and lifestyle data
3. Run the prediction
4. View the estimated weight and its position on the scatter plot

**To test the Logistic Regression model:**
1. Go to Supervised Machine Learning → Logistic Regression → Application
2. Enter the patient's clinical data
3. Run the prediction
4. View the diabetes risk result, probability, and model metrics

**To test the Ridge Classifier model:**
1. Go to Supervised Machine Learning → Ridge Classifier → Application
2. Enter the student's academic data (age, grades, units approved)
3. Run the prediction
4. View the result — Graduate or Dropout — along with the confusion matrix and ROC curve

**To explore the K-Means Clustering application:**
1. Go to Unsupervised Machine Learning → Clustering Application
2. The model runs automatically on page load — no form required
3. Browse the dataset stats, preprocessing steps, and model configuration
4. Explore the cluster assignment table, summary cards, and centroids
5. Interact with the scatter plot and bar chart to compare segments
6. Read the business interpretation of each customer cluster

---

## Project Structure

```
MachineLearning/
│
├── app.py                                          # Flask routes
├── LinearRegression.py                             # Weight prediction model
├── LinearRegression_Weight.py                      # Weight prediction helpers
├── LogisticRegression.py                           # Diabetes prediction model
├── logisticRegressionDiabetes.py                   # Diabetes prediction helpers
├── RidgeClassifierStudents.py                      # Student dropout model
├── Clustering.py                                   # K-Means clustering model
│
├── ObesityDataSet_raw_and_data_sinthetic.csv       # Obesity dataset
├── diabetes.csv                                    # Diabetes dataset
├── Predict_students_dropout.csv                    # Student dropout dataset
├── marketing_campaign.csv                          # Marketing campaign dataset (TSV)
├── kmeans_dataset.csv                              # Manual K-Means exercise dataset
│
└── templates/
    ├── start.html                                  # Home menu
    │
    ├── useCases.html                               # Use cases menu
    ├── useCase_Almonacid.html                      # PayPal — fraud detection
    ├── useCase_Mendez.html                         # Waze — route optimization
    ├── useCase_Cuitiva.html                        # Healthcare — cardiac risk
    ├── useCase_Group.html                          # Instagram — recommendation
    │
    ├── supervisedML.html                           # Supervised ML menu
    │
    ├── linearRegressionMenu.html                   # Linear regression menu
    ├── linearRegressionConcepts.html               # Basic concepts
    ├── linearRegression_Weight.html                # Weight prediction form
    ├── linearRegressionGrades.html                 # Grade prediction form
    │
    ├── logisticRegressionMenu.html                 # Logistic regression menu
    ├── logisticRegressionConcepts.html             # Basic concepts
    ├── logisticRegressionApplication.html          # Diabetes prediction form
    │
    ├── RidgeClassifierMenu.html                    # Ridge Classifier menu
    ├── RidgeClassifierConcepts.html                # Basic concepts
    ├── RidgeClassifierApplication.html             # Dropout prediction form
    │
    ├── unsupervisedML.html                         # Unsupervised ML menu
    ├── unsupervisedConcepts.html                   # K-Means basic concepts
    ├── kmeansExercise.html                         # Manual K-Means exercise
    └── clusteringApp.html                          # K-Means clustering application
```

---

## Datasets

### Obesity Dataset
Used for the **Linear Regression** model.

- **Source:** Survey data from Mexico, Peru, and Colombia (partially synthetic via SMOTE)
- **Records:** 2,111
- **Target variable:** Weight in kg (range: 39 – 173 kg)
- **Features:** 15 variables including age, height, eating habits, and physical activity

### Diabetes Dataset
Used for the **Logistic Regression** model.

- **Source:** Pima Indians Diabetes Database (National Institute of Diabetes and Digestive and Kidney Diseases)
- **Records:** 768 patients (female, age ≥ 21)
- **Target variable:** Outcome — 0 = No diabetes · 1 = Diabetes
- **Class distribution:** 500 negative (65.1%) · 268 positive (34.9%)
- **Features:** 8 clinical variables including glucose, BMI, insulin, blood pressure, and age

### Student Dropout Dataset
Used for the **Ridge Classifier** model.

- **Source:** Academic records from a Portuguese higher education institution
- **Records:** 4,424 students
- **Original classes:** Dropout, Enrolled, Graduate (converted to binary)
- **Features:** 5 variables — age at enrollment, units approved and grades for semesters 1 and 2

### Marketing Campaign Dataset
Used for the **K-Means Clustering** model.

- **Source:** Customer purchase and demographic records from a retail company
- **Format:** Tab-separated (TSV), `.csv` extension
- **Records:** 2,240 raw · 2,216 after removing 24 rows with missing income
- **Target:** No label — unsupervised clustering into 3 customer segments
- **Features used for clustering (10):** Income, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumWebPurchases, NumStorePurchases, Recency
- **Total columns:** 29 (demographics, spending, campaign responses)

---

## Model Performance

### Linear Regression — Weight Prediction

| Metric | Value |
|---|---|
| R² Score | 0.579 |
| MAE | 13.82 kg |
| RMSE | 17.23 kg |
| Training set | 1,688 records (80%) |
| Test set | 423 records (20%) |

### Logistic Regression — Diabetes Prediction

| Metric | Value |
|---|---|
| Accuracy | 75.3% |
| Precision | 64.9% |
| Recall | 67.3% |
| F1-Score | 66.1% |
| AUC | 0.815 |
| Training set | 614 records (80%) |
| Test set | 154 records (20%) |

### Ridge Classifier — Student Dropout Prediction

| Metric | Value |
|---|---|
| Accuracy | 79.5% |
| Precision | 78.6% |
| Recall | 93.7% |
| F1-Score | 85.5% |
| AUC | 0.859 |
| Training set | 3,539 records (80%) |
| Test set | 885 records (20%) |

### K-Means Clustering — Customer Segmentation

| Metric | Value |
|---|---|
| Algorithm | K-Means (Lloyd's) |
| n_clusters | 3 |
| n_init | 10 |
| Inertia (SSE) | 11,991.85 |
| Records clustered | 2,216 |
| Features used | 10 (StandardScaler applied) |

**Discovered segments:**

| Cluster | Name | Size | Avg Income | Avg Wine Spend |
|---|---|---|---|---|
| Low-value | Budget Shoppers | ~1,084 (49%) | $35,573 | $49 |
| Mid-value | Mid-Range Buyers | ~648 (29%) | $62,052 | $533 |
| High-value | Premium Customers | ~484 (22%) | $76,464 | $574 |

---

## Authors

**Elkin Yamith Almonacid López**  
**Brayan David Cuitiva Umbarila**  
**Brayan Yair Mendez Rodriguez**

Universidad de Cundinamarca — Systems and Computer Engineering  
Machine Learning · 2026
