from flask import Flask,render_template,request
from flask_pymongo import PyMongo

app=Flask(__name__)

app.config['MONGO_DBNAME']="BGCW_DB1"
app.config['MONGO_URI']="mongodb://127.0.0.1:27017/BGCW_DB1"

pri=PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main_page')
def main_page():
    return render_template('Main page.html')

# python code for execute student
# ---------------------------------

@app.route('/stueditprof')
def stueditprof():
    return render_template('student edit profile.html')

@app.route('/stugalup')
def stugalup():
    return render_template('student gallery upload.html')

@app.route('/stulogin')
def stulogin():
    return render_template('student login.html')

@app.route('/stunext')
def stunext():
    return render_template('student next page.html')

@app.route('/stuotp')
def stuotp():
    return render_template('student OTP page.html')

@app.route('/stuquery')
def stuquery():
    return render_template('student post a query.html')

@app.route('/sturegis')
def sturegis():
    return render_template('student register page.html')

@app.route('/stuviewnot')
def stuviewnot():
    return render_template('student view notification page.html')

# python code for execute Faculty
# ---------------------------------

@app.route('/facugalup')
def facugalup():
    return render_template('faculty gallery upload.html')

@app.route('/faculogin')
def faculogin():
    return render_template('faculty login page.html')

@app.route('/facunxtpg')
def facunxtpg():
    return render_template('faculty next page.html')

@app.route('/facuotp')
def facuotp():
    return render_template('faculty OTP page.html')

@app.route('/facuregpg')
def facuregpg():
    return render_template('faculty register page.html')

@app.route('/facurepnot')
def facurepnot():
    return render_template('faculty reply notification page.html')

@app.route('/facushare')
def facushare():
    return render_template('faculty share notes page.html')

@app.route('/facupnote')
def facupnote():
    return render_template('faculty upload notification.html')

@app.route('/facuviewnot')
def facuviewnot():
    return render_template('faculty view notification page.html')

# python code for execute principal
# ---------------------------------

@app.route('/prinlog')
def prinlog():
    return render_template('principal login page.html')

@app.route('/priotppg')
def priotppg():
    return render_template('principal OTP page.html')

@app.route('/prinextpg')
def prinextpg():
    return render_template('principal next page.html')

@app.route('/priview')
def priview():
    return render_template('principal view notification page.html')

@app.route('/priupnot')
def priupnot():
    return render_template('principal upload notification.html')

@app.route('/priupgal')
def priupgal():
    return render_template('principal upload gallery page.html')

@app.route('/prirepnot')
def prirepnot():
    return render_template('principal reply notification page.html')

@app.route('/priregpg')
def priregpg():
    return render_template('principal register page.html')

# python code for execute Admin
# ------------------------------

@app.route('/addelacc')
def addelacc():
    return render_template('Admin delete account page.html')

@app.route('/addelfac')
def addelfac():
    return render_template('Admin delete faculty account.html')

@app.route('/addelprin')
def addelprin():
    return render_template('Admin delete principal account.html')

@app.route('/addelstu')
def addelstu():
    return render_template('Admin delete student account.html')

@app.route('/adinsacc')
def addelinsacc():
    return render_template('Admin insert account page.html')

@app.route('/adinsfac')
def adinsfac():
    return render_template('Admin insert faculty page.html')

@app.route('/adinsnofac')
def adinsnofac():
    return render_template('Admin insert no.of faculty.html')

@app.route('/adinsnostu')
def adinsnostu():
    return render_template('Admin insert no.of student.html')

@app.route('/adinsprin')
def adinsprin():
    return render_template('Admin insert principal page.html')

@app.route('/adinsstu')
def adinsstu():
    return render_template('Admin insert student page.html')

@app.route('/adlogin')
def adlogin():
    return render_template('Admin login page.html')

@app.route('/admanage')
def admanage():
    return render_template('Admin manage all account details.html')

@app.route('/admanagestu')
def admanagestu():
    return render_template('Admin manage student details.html')

@app.route('/admanagefac')
def admanagefac():
    return render_template('Admin manage faculty details.html')

@app.route('/admanageprin')
def admanageprin():
    return render_template('Admin manage principal details.html')

@app.route('/admanagefed')
def admanagefed():
    return render_template('Admin manage feedback details.html')

@app.route('/admanagenxt')
def admanagenxt():
    return render_template('Admin manage next page.html')

@app.route('/adsignlog')
def adsignlog():
    return render_template('Admin sign or log page.html')

@app.route('/adnextpg')
def adnextpg():
    return render_template('Admin next page.html')

@app.route('/adotppg')
def adotppg():
    return render_template('Admin OTP page.html')

@app.route('/adregpg')
def adregpg():
    return render_template('Admin register page.html')

# principal database
# ==================
# principal Registrations database
# --------------------------------

@app.route('/priregdb',methods=['POST'])
def priregdb():
    y=pri.db.prinreg
    prin = request.form['prin']
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gender']
    dob = request.form['dob']
    age = request.form['age']
    phn1 = request.form['phn1']
    phn2 = request.form['phn2']
    email = request.form['email']
    pas1 = request.form['pass']
    pas2 = request.form['pass1']
    address = request.form['address']

    y.insert({"principal id":prin,"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"phone":phn1,"altphone":phn2,"email":email,"password":pas1,"alt password":pas2,"Address":address})
    return render_template('principal login page.html',msg='Registration is Successful')

# principal login database
# ------------------------

@app.route('/prilogdb',methods=['POST'])
def prilogdb():
    y=pri.db.prinreg
    email = request.form['email1']
    pas = request.form['pass']
    for i in y.find({"email":email,"password":pas}):
        return render_template('principal next page.html',msg='Login is Successful')
        break
    else:
        return render_template('principal login page.html',msg='Login is not correct please fill out correct format')

# Faculty database
# ==============

# Faculty Registrations database
# --------------------------------

@app.route('/facreglog_db',methods=['POST'])
def facreglog_db():
    y=pri.db.faculty_reg
    facul = request.form['facul']
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gender']
    dob = request.form['dob']
    age = request.form['age']
    dept = request.form['dept']
    phn1 = request.form['phn1']
    phn2 = request.form['phn2']
    email = request.form['email']
    pas = request.form['pass']
    pas1 = request.form['pass1']
    address = request.form['address']

    y.insert({"faculty id":facul,"name":name1,"initial":name2,"Gender":gen,"D.O.B":dob,"Age":age,"department":dept,"phone":phn1,"altphone":phn2,"email":email,"password":pas,"alt password":pas1,"address":address})

    return render_template('faculty next page.html',msg='Registration is Successful')

# Faculty login database
# ------------------------

@app.route('/faculog_db', methods=['POST'])
def faculog_db():
    y = pri.db.faculty_reg
    email = request.form['email']
    pas = request.form['pass']
    for i in y.find({"email": email, "password": pas}):
        return render_template('faculty OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('faculty login page.html',msg='Login is not correct please fill out correct format')

# Student database
# ================

# student Registrations database
# -------------------------------

@app.route('/stureg_db',methods=['POST'])
def stureg_db():
    y=pri.db.student_reg
    reg = request.form['reg']
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gen']
    dob = request.form['dob']
    age = request.form['age']
    dept = request.form['dept']
    year = request.form['year']
    phn1 = request.form['phn1']
    phn2 = request.form['phn2']
    email = request.form['email']
    pas = request.form['pass']
    pas1 = request.form['pass1']
    address = request.form['address']

    y.insert({"student reg":reg,"name":name1,"initial":name2,"Gender":gen,"D.O.B":dob,"Age":age,"department":dept,"year":year,"phone":phn1,"alt phone":phn2,"email":email,"password":pas,"alt password":pas1,"address":address})

    return render_template('student next page.html',msg='Registration is Successful')

# Student login database
# ------------------------

@app.route('/stulog_db', methods=['POST'])
def stulog_db():
    y = pri.db.student_reg
    email = request.form['email']
    pas = request.form['pass']
    for i in y.find({"email": email, "password": pas}):
        return render_template('student OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('student login.html',msg='Login is not correct, please fill out correct format')


# Admin database
# ==============

# Admin Registrations database
# -----------------------------

@app.route('/adminreg_db',methods=['POST'])
def adminreg_db():
    y=pri.db.admin_reg
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gender']
    dob = request.form['dob']
    age = request.form['age']
    dept = request.form['dept']
    phn1 = request.form['phn1']
    phn2 = request.form['phn2']
    email = request.form['email1']
    pas = request.form['pass']
    pas1 = request.form['pass1']
    address = request.form['address']

    y.insert({"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"department":dept,"phone":phn1,"altphone":phn2,"email":email,"password":pas,"alt password":pas1,"address":address})

    return render_template('Admin login page.html',msg='Registration is Successful')

# Admin login database
# ------------------------

@app.route('/adminlog_db', methods=['POST'])
def adminlog_db():
    y = pri.db.admin_reg
    email = request.form['email1']
    pas = request.form['pass']
    for i in y.find({"email": email, "password": pas}):
        return render_template('Admin next page.html', msg='Login is Successful')
        break
    else:
        return render_template('Admin login page.html',msg='Login is not correct please fill out correct format')

app.run(debug=True)

