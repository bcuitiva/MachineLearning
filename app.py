from flask import Flask, render_template, request
from LinearRegression_Weight import (predecir_peso, actual_values, predicted_values)
import LinearRegression_Weight

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('start.html')

@app.route('/FirstPage')
def firstPage():
    return render_template('index.html')

@app.route('/useCases')
def useCases():
    return render_template('useCases.html')

@app.route('/Almonacid')
def UseCase1():
    return render_template('useCase_Almonacid.html')

@app.route('/Mendez')
def UseCase2():
    return render_template('useCase_Mendez.html')

@app.route('/Cuitiva')
def UseCase3():
    return render_template('useCase_Cuitiva.html')

@app.route('/Group')
def UseCase4():
    return render_template('useCase_Group.html')

@app.route('/Group')
def UseCase4():
    return render_template('useCase_Group.html')

@app.route('/lRMenu')
def linearRM():
    return render_template('linearRegressionMenu.html')

@app.route('/lRConcepts')
def linearRC():
    return render_template('linearRegressionConcepts.html')

@app.route('/LinearRegressionWeight', methods=["GET", "POST"])
def linearRW():
    calculateResult = None
    user_point = None

    if request.method == "POST":
        datos = {
            'Age': float(request.form['Age']),
            'Height': float(request.form['Height']),
            'Gender': request.form['Gender'],
            'family_history_with_overweight': request.form['family_history_with_overweight'],
            'FAVC': request.form['FAVC'],
            'FCVC': float(request.form['FCVC']),
            'NCP': float(request.form['NCP']),
            'CAEC': request.form['CAEC'],
            'CALC': request.form['CALC'],
            'SMOKE': request.form['SMOKE'],
            'CH2O': float(request.form['CH2O']),
            'SCC': request.form['SCC'],
            'FAF': float(request.form['FAF']),
            'TUE': float(request.form['TUE']),
            'MTRANS': request.form['MTRANS'],
        }

        calculateResult = predecir_peso(datos)

    return render_template(
        'linearRegression_Weight.html',
        resultado=calculateResult,
        actual=actual_values,
        predicted=predicted_values,
        user_point=user_point
    )
if __name__ == '__main__':
    app.run(debug=True)