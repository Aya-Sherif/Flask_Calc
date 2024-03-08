# import flast module
from flask import Flask,render_template,request,redirect,url_for

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/",methods=['POST','GET'])

def Calculate():
    number1=float(request.form.get('number_1'))
    number2=float(request.form.get('number_2'))
    operation=request.form.get('operation')
    result = do_Calc(number1,number2,operation)
    return render_template('index.html',result=result)

def do_Calc(number1,number2,operation):
    if(operation=="+"):
        return number1+number2
    elif (operation=="-"):
        return number1-number2
    elif (operation=="*"):
        return number1*number2
    elif (operation=="/"):
        if(number2==0):
            return "We can not divide by zero"
        else:
            return number1/number2
        


if __name__ == '__main__': 
    app.run()
