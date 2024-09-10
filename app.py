#Integrating HTML with Flask - aka Jinja2 technique, HTTP verb-GET and POST

from flask import Flask, redirect, url_for, render_template, request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score<33:
        res="Failed With Score: "+str(score)
    else:
        res="Passed With Score: "+str(score)
    return render_template('results.html',result=res)

#Result Checker HTML Page
@app.route('/submit',methods=['GET','POST'])
def submit():
    t_score=0
    if request.method=='POST':
        sci=float(request.form['science'])
        math=float(request.form['maths'])
        eng=float(request.form['english'])
        hin=float(request.form['hindi'])
        t_score=sci+math+eng+hin
        percent=t_score/4
    '''if percent<33:
        result="failed"
    else:
        result="passed"'''
    return redirect(url_for('success',score=percent))

if __name__=='__main__':
    app.run(debug=True)