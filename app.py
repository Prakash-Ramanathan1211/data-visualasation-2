from io import BytesIO
from flask import Flask, render_template, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import jinja2

plt.style.use('ggplot')

app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('/Users/yehhsuan-yu/something'),
])
app.jinja_loader = my_loader


@app.route('/oilprice_visualisation_1/')
def oilprice_visualization_1():
    fig, ax = plt.subplots()
    df = pd.ExcelFile('/Users/yehhsuan-yu/Download/PET_PRI_SPI_S1_M.xis')
    df_crudeoil = pd.read_excel(df, 'Data 1', skiprows=2)
    time = df_crudeoil['Date']
    price1 = df_crudeoil.iloc[:, 1]
    price2 = df_crudeoil.iloc[:, 2]
    plt.plot(time, price1, color='blue')
    plt.plot(time, price2, color='orange')
    plt.xlabel('Time (Year')
    plt.ylabel('Crude Oil Price')
    plt.title('Time Series of Crude Oil Prices')
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savwefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/')
def index():
    return render_template("sample.html")


if __name__ == '__main__':
    app.run(debug=True)
