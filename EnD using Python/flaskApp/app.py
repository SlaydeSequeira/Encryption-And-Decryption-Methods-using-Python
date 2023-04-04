from flask import Flask,render_template,request 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result" , methods = ['POST' , 'GET'])
def result():
    output = request.form.to_dict()
    string = str(output["input-text"])
    x = int(output["x-num"])
    y = int(output["y-num"])

    # conversion function
    binary = ''.join(format(ord(c), '08b') for c in string)                   #convert to binary
    num1 = int(binary, 2)                                                     #make it decimal
    num1=num1*x+num1*y+num1*(x+y)+num1*(x-y)                                  #Secret formula will make stronger later
    strr= str(num1)
    output_dec = strr.ljust(64, '0')                                          #Fill end with 0 to make 64 bit
    num2=int(output_dec)
    num=num1+num2
    name = hex(num)[2:]



    return render_template("index.html",name = name)

if __name__ == '__main__':
    app.run(debug=True , port=5001)