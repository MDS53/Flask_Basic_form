from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to this Page</h1>"

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
        
@app.route('/submit_form.php',methods=['POST'])
def submit():
    fname=request.form['fname']
    lname=request.form['lname']
    age=request.form['age']
    email=request.form['email']
    message=request.form['message']
    return render_template('output.html',fname=fname,lname=lname,age=age,email=email,message=message)    
if __name__=='__main__':
    app.run(debug=True)