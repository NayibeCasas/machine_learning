from sklearn.feature_selection import SelectKBest
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, redirect, url_for
# librerias de procesamiento
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd
import seaborn as sb
plt.rcParams['figure.figsize'] = (10, 9)
plt.style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
import dataframe_image as dfi

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resultado')
def resultado():
    return render_template('resultado.html')


@app.route('/enviarDatos', methods=['POST'])
def enviarDatos():
    chest = int(request.form['chest'])
    front = int(request.form['front'])
    across = int(request.form['across'])
    print(chest, front, across)
    data = procesamiento(chest,front,across)
    return render_template('resultado.html', talla=data)


def procesamiento(chest, front, across):
	dataframe = pd.read_csv("./talla.csv")
	X= dataframe.drop(['Size', 'BrandName', 'Type', 'BrandSize'], axis=1)
	y= dataframe['Size']
	best = SelectKBest(k=3)
	X_new = best.fit_transform(X, y)
	X_new.shape
	selected = best.get_support(indices=True)
	print(X.columns[selected])
	used_features = X.columns[selected]
	X_train, X_test = train_test_split(dataframe, test_size=0.2, random_state=6)
	y_train =X_train['Size']
	y_test = X_test['Size']
	# Instantiate the classifier
	gnb = GaussianNB()
	# Train classifier
	gnb.fit(X_train[used_features].values,y_train)
	y_pred = gnb.predict(X_test[used_features])
	prediccion=gnb.predict([[chest,front,across] ])
	dataframeFinal=dataframe.drop(['Chest(cm)', 'FrontLength(cm)','AcrossShoulder(cm)'], axis=1)
	resultante=dataframeFinal.loc[dataframeFinal['Size']==prediccion[0]]
	rango={36:'XS',38:'XS-S',39:'S-M',40:'M-L',42:'L-XL',44:'XL-XXL',46:'XXL-EL-TXL',48:'TXL-3XL-EL-KL'}
	dato=[prediccion[0],rango[prediccion[0]]]
	dfi.export(resultante,'./src/static/Images/resultado.png')
	return dato

if __name__ == '__main__':
    app.run(debug=True, port=5000)
