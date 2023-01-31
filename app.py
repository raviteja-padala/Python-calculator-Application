from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'] )
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(operation == 'add'):  
            r= num1+num2
            result = 'Sum of two numbers  '+ str(num1) +' + '+ str(num2) + '  =  ' + str(r)
        
        if(operation == 'subtract'):
            r= num1-num2
            result = 'Difference of  '+ str(num1) +' - '+ str(num2) + '   =   ' + str(r)

        if(operation == 'multiply'):
            r= num1*num2
            result = 'Multiplication  of two numbers  '+ str(num1) +' x '+ str(num2) + '   =   ' + str(r)

        if(operation == 'divide'):
            r= num1/num2
            result = 'Division of two numbers  '+ str(num1) +' / '+ str(num2) + '  =   ' + str(r)


        return render_template('results.html', result = result)



    if __name__ == '__main__':
        app.run()