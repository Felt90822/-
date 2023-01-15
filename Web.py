from flask import Flask, render_template, request

app = Flask(__name__)

'''
@app.route("/<name>")
def home(name):
    #傳送到index.html的介面, content變數為 name
    return render_template("index.html", content=name)
'''

@app.route("/")
def home():
    return render_template("My_Web.html")

@app.route("/home")
def Homee():
    return render_template("My_Web.html")

@app.route("/TF")
def TrnansForm():
    return render_template("TransForm.html")

@app.route("/Page3")
def page3():
    return render_template("calculate.html")

@app.route("/IF")
def weather():
    return render_template("weather.html")

@app.route("/calculate_return", methods=['POST'])
def calaulate_return():
    CH = request.form['CH']
    EN = request.form['EN']
    M = request.form['M']
    C = request.form['C']
    PY = request.form['PY']
    S = request.form['S']
    H = request.form['H']
    G = request.form['G']
    L = request.form['L']

    return render_template("calculate_return.html", CH=CH, EN=EN, M=M, PY=PY, C=C, S=S, H=H, G=G, L=L)

@app.route("/TransForm_return", methods=["POST"])
def TransForm_return():
    N = int(request.form['num'])
    
    i = 0
    sum = 0
    m = 0
    if N>=0:
        while N!=0:
            m = N % 10
            N = N // 10
            
            sum += m*pow(2, i)
            i = i+1
    
    return render_template("TransForm_return.html", num=sum)

@app.route("/weather_return", methods=['POST'])
def weather_return():
    weather = int(request.form['weather'])
    feeling = int(request.form['feeling'])
    ans = feeling + weather
    return render_template("weather_return.html", A=ans)

if __name__ == "__main__":
    app.run(debug=True)

