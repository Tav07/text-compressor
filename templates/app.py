from flask import Flask 

from flask import render_template, request

app = Flask(__name__)

@app.route('/home')
def hello():
    return 'Hola Web'

@app.route('/encode')
def html():
    return render_template('encode.html')


@app.route('/decode')
def html():
    return render_template('decode.html')



if __name__=='__main__':
    app.run()