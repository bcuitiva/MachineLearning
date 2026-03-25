# Machine Learning — Web Application

A web application built with Flask that helps understand machine learning concepts in a simple way and shows real-world examples of how they are used. It also includes a model that estimates body weight using real data.

---

## Description

This project was developed as part of the Machine Learning course at Universidad de Cundinamarca.

The goal is to combine theory with practice. It not only explains concepts, but also shows how they work within the application itself. It includes real examples from different fields and a functional model that can be used to make predictions.

The backend is built with Python and Flask, while the frontend uses HTML, CSS, and Bootstrap.

---

## Features

- Simple and easy-to-use main menu  
- 4 real-world machine learning use cases:
  - Fraud detection (PayPal)  
  - Route optimization (Waze)  
  - Heart disease prediction (Healthcare)  
  - Content recommendation (Instagram)  
- Linear regression module:
  - Basic concept explanations  
  - Practical exercise with a real model  
- Interactive form to enter data and get a weight estimation  
- Model results visualization  
- Graph comparing actual vs predicted values  

---

## Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- HTML and CSS  
- Bootstrap  
- Chart.js  

---

## Installation

### Requirements
- Python 3.8 or higher  
- pip  

### Steps

1. Clone the repository  
```bash
git clone https://github.com/bcuitiva/MachineLearnig.git
```

2. Go to the project folder  
```bash
cd MachineLearnig
```

3. Create and activate a virtual environment  

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac / Linux
python3 -m venv .venv
source .venv/bin/activate
```

4. Install dependencies  
```bash
pip install flask pandas scikit-learn numpy
```

5. Make sure the dataset is in the project root  

6. Run the application  
```bash
python app.py
```

---

## Usage

- Open the application in your browser  
- Navigate through the available sections  
- To test the model:
  1. Go to the linear regression module  
  2. Fill out the form  
  3. Run the prediction  
  4. View the result  

---

## Project Structure

```
machine-learning-app/
│
├── app.py
├── LinearRegression_Weight.py
├── ObesityDataSet_raw_and_data_sinthetic.csv
│
└── templates/
    ├── start.html
    ├── useCases.html
    ├── useCase_Almonacid.html
    ├── useCase_Mendez.html
    ├── useCase_Cuitiva.html
    ├── useCase_Group.html
    ├── linearRegressionMenu.html
    ├── linearRegressionConcepts.html
    └── linearRegression_Weighthtml
```

---

## Dataset

An obesity dataset was used, containing information from people in Mexico, Peru, and Colombia.

- More than 2000 records  
- Includes variables such as age, height, eating habits, and physical activity  
- The target variable is weight (in kg)  

---

## Model Performance

- R²: 0.579  
- Average error: ~13.8 kg  
- Mean squared error: ~17 kg  

This is not a perfect model, but it helps understand in a practical way how these techniques work.
