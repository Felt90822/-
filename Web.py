from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def stu(): #用來回應首頁連線函式
    return render_template("index.html")

@app.route("/index_return", methods=['POST'])#建立 接收表單 回應方式
def index_return(): #用來回應絕對值表單連線函式
    N = int(request.form['num'])
    
    i = 0
    sum = 0
    if N>0:
        while N!=0:
            m = N % 10
            N /= 10
            
            sum += m*pow(2, i)
            i += 1
    
    return render_template("index_return.html", num=sum)
#啟動網站伺服器
app.run(debug=True)
