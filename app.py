from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/',methods=['GET'])
def home():
    temp = int(request.args['temp'])
    ox = int(request.args['ox'])
    humid = int(request.args['humid'])
    int_features= temp, ox, humid
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if temp+ox+humid>(0):
        x=output
        x=str(x)
        return x
        print(x)

    
if __name__ == '__main__':
    app.run(debug=True)
