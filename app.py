#import a library
from flask import Flask, render_template,request
from flask.wrappers import Request
import joblib

load_model=joblib.load('dib_79.pkl')

#instance of an app
app=Flask(__name__)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/blog', methods=['POST'])
def blog_page():
    a=request.form.get('preg')
    b=request.form.get('plas')
    c=request.form.get('pres')
    d=request.form.get('skin')
    e=request.form.get('test')
    f=request.form.get('mass')
    g=request.form.get('pedi')
    h=request.form.get('age')
    
    #print(exp,mail,contact,addr)

    pred=load_model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])
    print(pred)

    if pred[0]==1:
        output='diabetic'

    else:
        output='not diabetic'



    return render_template('blog.html', predicted_text=f'person is {output}')

@app.route('/contact')
def contact():
    return 'contacts page'

#run the app
if __name__=='__main__':
    app.run(debug=True) # debug=True will reload server automatically and any change in function name or content will be reflecting immediately without the need to restart the server manually



