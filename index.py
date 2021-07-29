from flask import Flask,render_template,request,session,send_file
from flask_pymongo import PyMongo
from flask_mail import Mail,Message
import datetime
from random import randint

app=Flask(__name__)

app.secret_key="bgcw"

app.config['MONGO_DBNAME']="BGCW_DB"
app.config['MONGO_URI']="mongodb://127.0.0.1:27017/BGCW_DB"

pri=PyMongo(app)

# OTP For Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ocean143oa@gmail.com'
app.config['MAIL_PASSWORD'] = 'oa12345678'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main_page')
def main_page():
    return render_template('Main page.html')

#  python code for Alumni website
# ===============================

@app.route('/alumni_login')
def alumni_login():
    return render_template('Alumni website main page.html')

@app.route('/alumni_next')
def alumni_next():
    return render_template('Alumni next page.html')

@app.route('/alumni_insert')
def alumni_insert():
    return render_template('Admin insert alumni account.html')

@app.route('/alumni_post')
def alumni_post():
    return render_template('Admin post notification.html')

@app.route('/alumniotp')
def alumniotp():
    return render_template('Alumni OTP page.html')

# python code for execute student
# ---------------------------------

@app.route('/stueditprof')
def stueditprof():
    y = pri.db.student_reg
    return render_template('student edit profile.html',res=y.find({'email':session['email']}))

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
    return render_template('student post a query.html',y=request.args['x'])

@app.route('/sturegis')
def sturegis():
    y = pri.db.student_reg
    return render_template('student register page.html',res=y.find({'email':session['email']}))

@app.route('/stuviewnot')
def stuviewnot():
    y = pri.db.prin_upload
    return render_template('student view notification page.html', res=y.find(
        {"$or": [{"mode1": session['Mode']}, {"mode2": session['Mode']}, {'selection': 'both'}]}))

# python code for execute Faculty
# ---------------------------------

@app.route('/facueditprof')
def facugalup():
    y = pri.db.faculty_reg
    return render_template('faculty edit profile page.html',res=y.find({'email':session['email']}))

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
    y = pri.db.faculty_reg
    return render_template('faculty register page.html',res=y.find({'email':session['email']}))

@app.route('/facurepnot')
def facurepnot():
    return render_template('faculty reply notification page.html',y=request.args['x'])

@app.route('/facushare')
def facushare():
    y = pri.db.facul_notes
    return render_template('faculty share notes page.html',res=y.find())

@app.route('/facupnote')
def facupnote():
    return render_template('faculty upload notification.html')

@app.route('/facuviewnot')
def facuviewnot():
    y = pri.db.prin_upload

    return render_template('faculty view notification page.html', res=y.find(
        {"$or": [{"mode1": session['Mode']}, {"mode2": session['Mode']}, {'selection': 'both'}]}

    ))

   # y = pri.db.prin_upload
   # return render_template('faculty view notification page.html', res=y.find())

# python code for execute principal
# ---------------------------------

@app.route('/prineditprof')
def prineditprof():
    y = pri.db.prin_reg
    return render_template('principal edit profile page.html',res=y.find({'email':session['email']}))

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
    y = pri.db.prin_upload

    return render_template('principal view notification.html', res=y.find())

@app.route('/priupnot')
def priupnot():
    return render_template('principal upload notification.html')

@app.route('/prirepnot')
def prirepnot():
    return render_template('principal reply notification page.html',y=request.args['x'])

@app.route('/priregpg')
def priregpg():
    y = pri.db.prin_reg
    return render_template('principal register page.html',res=y.find({'email':session['email']}))

# python code for execute Admin
# ------------------------------

@app.route('/admfeed')
def admfeed():
    return render_template('Admin reply feedback notification.html',y=request.args['x'])

@app.route('/adinsacc')
def adinsacc():
    return render_template('Admin insert account page.html')

@app.route('/adinsfac')
def adinsfac():
    return render_template('Admin insert faculty page.html')

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
    y = pri.db.student_reg
    return render_template('Admin manage student details.html',res=y.find())

@app.route('/admanagefac')
def admanagefac():
    y = pri.db.faculty_reg
    return render_template('Admin manage faculty details.html',res=y.find())

@app.route('/admanageprin')
def admanageprin():
    y = pri.db.prin_reg
    return render_template('Admin manage principal details.html',res=y.find())

@app.route('/admanagefed')
def admanagefed():
    y=pri.db.admin_feed
    return render_template('Admin manage feedback details.html',res=y.find())

@app.route('/admanagenxt')
def admanagenxt():
    return render_template('Admin manage all account details.html')

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

@app.route('/principal_db',methods=['POST'])
def principal_db():
    y=pri.db.prin_reg
    prin = request.form['prin']
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gender']
    dob = request.form['dob']
    age = request.form['age']
    phn1 = request.form['phn1']
    phn2 = request.form['phn2']
    email = request.form['email1']
    pas = request.form['pass']
    address = request.form['address']

    for i in y.find({"principal_id":prin,"Phone No":phn1,"email":email}):
        return render_template('Admin insert principal page.html',msg='email-Id or Phone Number is already exist')

    y.insert({"principal_id":prin,"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"phone":phn1,"alt_phone":phn2,"email":email,"password":pas,"address":address})

    return render_template('Admin insert account page.html',msg='Registration is Successful')

# principal login database
# ------------------------

@app.route('/prilogdb',methods=['POST'])
def prilogdb():
    y=pri.db.prin_reg
    email = request.form['email']
    pas = request.form['pass']
    session['email'] = email
    for i in y.find({"email":email,"password":pas}):
        session['email'] = i['email']
        session['name']='Principal'
        session['dept']=''
        t = Message('OTP DETAILS', sender='ocean143oa@gmail.com', recipients=[session['email']])
        x = str(randint(1000, 9999))
        session['otp'] = x
        t.body = "Your otp is :" + x
        mail.send(t)
        return render_template('principal OTP page.html',msg='Login is Successful')
        break
    else:
        return render_template('principal login page.html',msg='Login is not correct please fill out correct format')

# principal OTP session
# ------------------------

@app.route('/adotp3_db',methods=['POST'])
def adotp3_db():
    d=str(request.form['otp'])
    if d==session['otp']:
        return render_template('principal next page.html',msg='valid OTP')
    else:
        return render_template('principal OTP page.html',msg='Invalid')

# principal DELETE database
# ---------------------------
@app.route('/principaldel_db')
def principaldel_db():
   y=pri.db.prin_reg
   y.delete_one({"principal_id":request.args['prin']})
   return render_template('Admin manage principal details.html',msg='Principal account was deleted')

# principal reply database
# ------------------------
@app.route('/princirep_db', methods=['POST'])
def princirep_db():
   subject = request.form['descrip']
   email = request.form['email']

   s = pri.db.prin_upload
   t = Message('principal post reply Message here...', sender='ocean143oa@gmail.com', recipients=[email])
   x = str(subject)
   # session['subject'] = x
   t.body = "Your subject is : " + x
   mail.send(t)
   return render_template('principal next page.html', msg='reply message is send Successful')

# principal update database
# --------------------------------
@app.route('/principalup_db',methods=['POST'])
def principalup_db():
   y=pri.db.prin_reg
  # phn1 = request.form['phn1']
  # phn2 = request.form['phn2']
    # email = request.form['email1']
  # pas = request.form['pass']
  # address = request.form['address']

   y.update({"email": session['email']},
            {"$set": {"phone": request.form['phn1'], "alt_phone": request.form['phn2'], "email": request.form['email1'], "password": request.form['pass'], "address": request.form['address']}})

   return render_template('principal next page.html',msg='Update is Successful')

# text Local code(sending message high priority)
# ==============================================
import urllib.request
import urllib.parse

def sendSMS(apikey,numbers,sender,message):
    data=urllib.parse.urlencode({'apikey':apikey,'numbers':numbers,'message':message,'sender':sender})
    data=data.encode('utf-8')
    request=urllib.request.Request("https://api.textlocal.in/send/?")
    f=urllib.request.urlopen(request,data)
    fr=f.read()
    return (fr)

# principal upload file database
# =============================

@app.route('/prinup_db',methods=['POST'])
def prinup_db():
   y=pri.db.prin_upload
   priority=request.form['pri']
   description = request.form['descrip']
   myfile=request.files['myfile']
   myfile.save(myfile.filename)
   select = request.form['radio']

   xx={'name':session['name'],'dept':session['dept'],"date_time":datetime.datetime.now(),'email':session['email'],'priority':priority,'description':description,'my_file':myfile.filename,'selection':select}

   if (priority == 'High'):
       # if request.method == "POST":
       kd = request.form['radio']

       if kd == 'both':
           x = pri.db.faculty_reg
           xx['mode1']='arts'
           xx['mode2']='science'
           for i in x.find():
               ph = i['phone']
               res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph),'TXTLCL', (description))

           xh = pri.db.student_reg
           for i in xh.find():
                   ph = i['phone']
                   res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph), 'TXTLCL', (description))

       # for staffs
       elif kd == 'staff':
            x = pri.db.faculty_reg

            if request.form.get('check1'):
                xx['mode1']='arts'

                #request.form.getlist('check')
                for i in x.find({"Mode":'arts'}):
                    ph = i['phone']
                    res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph),
                                  'TXTLCL', (description))

            if request.form.get('check2'):
                xx['mode2'] = 'science'
                # return xx['mode1']
                for i in x.find({"Mode":'science'}):
                    ph = i['phone']
                    res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph),
                                  'TXTLCL', (description))

       # for student
       elif kd == 'student':
           xh = pri.db.student_reg

           if request.form.get('check3'):
               xx['mode1'] = 'arts'
               for i in xh.find({"Mode":'arts'}):
                   ph = i['phone']
                   res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph),
                                 'TXTLCL', (description))

           if request.form.get('check4'):
               xx['mode2'] = 'science'
               for i in xh.find({"Mode":'science'}):
                   ph = i['phone']
                   res = sendSMS('87SpQ7Fhieo-0v40DLkR5LKi2RqRSfe4AZl226vx5k', "91" + str(ph),
                                 'TXTLCL', (description))

       y.insert(xx)

       return render_template("principal next page.html", msg='(high priority)message uploaded successfully')

   # for low priority
   elif (priority == 'Low'):

       # for both
       kd = request.form['radio']

       if kd == 'both':
           xx['mode2'] = 'science'
           xx['mode1'] = 'arts'
           x = pri.db.faculty_reg
          # y = x.find({"email":'email'})
           for i in x.find():
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (both faculty and student)" + x
               mail.send(t)

           xh = pri.db.student_reg
           # yh = xh.find({"email":'email'})
           for i in xh.find():
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (both student and faculty)" + x
               mail.send(t)

       # for staffs
       elif kd == 'staff':

           x = pri.db.faculty_reg
           if request.form.get('check1'):
               xx['mode1'] = 'arts'
               # request.form.get('check')
               for i in x.find({"Mode": 'arts'}):
                   subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
                   t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
                   x = str(subject)
                   # session['subject'] = x
                   t.body = "Your Message is : (faculty from arts)" + x
                   mail.send(t)

           if request.form.get('check2'):
               x = pri.db.faculty_reg
               xx['mode2'] = 'science'
               for i in x.find({"Mode": 'science'}):
                   subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
                   t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
                   x = str(subject)
                   # session['subject'] = x
                   t.body = "Your Message is : (faculty from science)" + x
                   mail.send(t)

       # for student
       elif kd == 'student':
           xh = pri.db.student_reg
           if request.form.get('check3'):
               xx['mode1'] = 'arts'
               for i in xh.find({"Mode": 'arts'}):
                   subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
                   t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
                   x = str(subject)
                   # session['subject'] = x
                   t.body = "Your Message is : (student from arts)" + x
                   mail.send(t)

           if request.form.get('check4'):
               xx['mode2'] = 'science'
               for i in xh.find({"Mode": 'science'}):
                   subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
                   t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
                   x = str(subject)
                   # session['subject'] = x
                   t.body = "Your Message is : (student from science)" + x
                   mail.send(t)
       y.insert(xx)

       return render_template("principal next page.html", msg='(Low priority)message uploaded successfully')

   else:
       return render_template('principal upload notification.html',msg='message not uploaded')

# for download code
# -----------------
@app.route('/sendimage/<name>')
def sendimage(name):
 path = name
 return send_file(path, as_attachment=True)
# return render_template('principal view notification.html')

# principal file upload(code)
# ==========================

# @app.route('/',methods=['POST'])
# def home():
#    if 'name' in request.files:
#        f=request.files['name']
#        mongo.save_file(f.filename.f)
#        s=f.filename.split(".") [-1]
#        mongo.db.data.insert({'type':s,'file':f.filename})
#        return render_template('index.html')

# @app.route("/download")
# def download():
#    return mongo.send_file(filename='shapes.jpg')

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
    mode = request.form['mode']
    dept = request.form['dept']
    phn1 = request.form['phn']
    phn2 = request.form['phn1']
    email = request.form['email']
    pas = request.form['pass']
    address = request.form['address']

    #for i in y.find({"faculty_id": facul}):
    #    return render_template('Admin insert faculty page.html', msg='FACULTY_ID is already exist')

    #for i in y.find({"Phone No":phn1}):
    #    return render_template('Admin insert faculty page.html',msg='Phone Number is already exist')

    #for i in y.find({"email":email}):
    #    return render_template('Admin insert faculty page.html',msg='email-Id is already exist')

    y.insert({"faculty_id":facul,"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"Mode":mode,"department":dept,"phone":phn1,"alt_phone":phn2,"email":email,"password":pas,"address":address})

    return render_template('Admin insert account page.html',msg='Registration is Successful')

# Faculty login database
# ------------------------

@app.route('/faculog_db', methods=['POST'])
def faculog_db():
    y = pri.db.faculty_reg
    email = request.form['email']
    pas = request.form['pass']
    session['email'] = email
    for i in y.find({"email": email, "password": pas}):
        session['Mode']=i['Mode']
        session['email'] = i['email']
        session['name']=i['name']
        session['dept']=i['department']
        t = Message('OTP DETAILS', sender='ocean143oa@gmail.com', recipients=[session['email']])
        x = str(randint(1000, 9999))
        session['otp'] = x
        t.body = "Your otp is :" + x
        mail.send(t)
        return render_template('faculty OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('faculty login page.html',msg='Login is not correct please fill out correct format')

# faculty OTP session
# ------------------------

@app.route('/adotp2_db',methods=['POST'])
def adotp2_db():
    c=str(request.form['otp'])
    if c==session['otp']:
        return render_template('faculty next page.html',msg='valid OTP')
    else:
        return render_template('faculty OTP page.html',msg='Invalid')

# faculty DELETE database
# --------------------------------
@app.route('/faculdel_db')
def faculdel_db():
   y=pri.db.faculty_reg
   y.delete_one({"faculty_id":request.args['facul']})
   return render_template('Admin manage faculty details.html',msg='This Faculty account was deleted')

# faculty profile update database
# --------------------------------
@app.route('/faculup_db',methods=['POST'])
def faculup_db():
   y=pri.db.faculty_reg
   phn1 = request.form['phn1']
   phn2 = request.form['phn2']
   email = request.form['email']
   pas = request.form['pass']
   address = request.form['address']

   for i in y.find({"Phone No":phn1,"email":email}):
       session['email'] = i['email']
       return render_template('faculty next page.html',msg='email-Id or Phone Number is already exist')

   y.update({"email":session['email'],'name':session['name']},{"$set":{"phone":phn1,"alt_phone":phn2,"email":email,"password":pas,"address":address}})

   return render_template('faculty next page.html',msg='Update is Successful')

# faculty upload file database
# =============================

@app.route('/facultyup_db',methods=['POST'])
def facultyup_db():
   y=pri.db.prin_upload
   description = request.form['descrip']
   myfile = request.files['myfile']
   myfile.save(myfile.filename)
   select = request.form['radio']

   xx = {'name':session['name'],'dept':session['dept'],"date_time":datetime.datetime.now(),'email':session['email'],'description': description, 'my_file': myfile.filename,'selection': select}

   # for both
   kd = request.form['radio']

   if kd == 'principal':
       x = pri.db.prin_reg
       # y = x.find({"email":'email'})
       for i in x.find():
           subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
           t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
           x = str(subject)
           # session['subject'] = x
           t.body = "Your Message is : (principal only)" + x
           mail.send(t)

   elif kd == 'both':
       xx['mode2'] = 'science'
       xx['mode1'] = 'arts'
       x = pri.db.faculty_reg
       # y = x.find({"email":'email'})
       for i in x.find():
           subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
           t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
           x = str(subject)
           # session['subject'] = x
           t.body = "Your Message is : (both faculty and student)" + x
           mail.send(t)

       xh = pri.db.student_reg
       # yh = xh.find({"email":'email'})
       for i in xh.find():
           subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
           t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
           x = str(subject)
           # session['subject'] = x
           t.body = "Your Message is : (both student and faculty)" + x
           mail.send(t)

   # for staffs
   elif kd == 'staff':

       x = pri.db.faculty_reg
       if request.form.get('check1'):
           xx['mode1'] = 'arts'
           # request.form.get('check')
           for i in x.find({"Mode": 'arts'}):
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (faculty from arts)" + x
               mail.send(t)

       if request.form.get('check2'):
           x = pri.db.faculty_reg
           xx['mode2'] = 'science'
           for i in x.find({"Mode": 'science'}):
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (faculty from science)" + x
               mail.send(t)

   # for student
   elif kd == 'student':
       xh = pri.db.student_reg
       if request.form.get('check3'):
           xx['mode1'] = 'arts'
           for i in xh.find({"Mode": 'arts'}):
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (student from arts)" + x
               mail.send(t)

       if request.form.get('check4'):
           xx['mode2'] = 'science'
           for i in xh.find({"Mode": 'science'}):
               subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
               t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
               x = str(subject)
               # session['subject'] = x
               t.body = "Your Message is : (student from science)" + x
               mail.send(t)
   y.insert(xx)

   return render_template("faculty next page.html", msg='Notification Message uploaded successfully')

# for download code faculty
# --------------------------
@app.route('/sendimage1/<name>')
def sendimage1(name):
    path = name
    return send_file(path, as_attachment=True)

# faculty upload notes database
# =============================

@app.route('/faculnotes_db',methods=['POST'])
def faculnotes_db():
   y = pri.db.facul_notes
   email = request.form['email']
   a = request.form['dept']
   b = request.form['year']
   c = request.form['about']
   file1=request.files['notesfile']
   file1.save(file1.filename)
   y.insert({'department':a,'year':b,'about_notes':c,'myfile1':file1.filename,'email': session['email']})

   s = pri.db.student_reg
   # session['email']=email
   for i in s.find({'department':a,'year':b}):
       session['mode1'] = 'arts'
       session['mode2'] = 'science'
       t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
       x = str(c)
       t.body = "Your subject is :" + x
       with app.open_resource(file1.filename) as fp:
           t.attach(file1.filename, "doc/docx", fp.read())
       mail.send(t)
       return render_template('faculty next page.html',msg='Notes uploaded successfully')
   else:
       return render_template('faculty share notes page.html',msg='Notes not uploaded')

# faculty reply database
# ======================
@app.route('/facurep_db', methods=['POST'])
def facurep_db():
   subject = request.form['descrip']
   email = request.form['email']

   s = pri.db.prin_upload
   t = Message('faculty post reply Message here...', sender='ocean143oa@gmail.com', recipients=[email])
   x = str(subject)
   # session['subject'] = x
   t.body = "Your subject is :  " + x + "\n"
   mail.send(t)
   return render_template('faculty next page.html', msg='reply message is send Successful')

# Student database
# ================

# student Registrations database
# ------------------------------

@app.route('/stureg_db',methods=['POST'])
def stureg_db():
    y=pri.db.student_reg
    reg = request.form['reg']
    name1 = request.form['name1']
    name2 = request.form['name2']
    gen = request.form['gen']
    dob = request.form['dob']
    age = request.form['age']
    mode = request.form['mode']
    dept = request.form['dept']
    year = request.form['year']
    phn1 = request.form['phn']
    phn2 = request.form['phn1']
    email = request.form['email']
    pas = request.form['pass']
    address = request.form['address']

    #for i in y.find({"student_reg": reg}):
   #     return render_template('Admin insert student page.html', msg='Registration Number is already exist')

    #for i in y.find({"phone":phn1}):
     #   return render_template('Admin insert student page.html',msg='Phone Number is already exist')

   # for i in y.find({"email":email}):
    #    return render_template('Admin insert student page.html',msg='email-Id is already exist')

    y.insert({"student_reg":reg,"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"Mode":mode,"department":dept,"year":year,"phone":phn1,"alt_phone":phn2,"email":email,"password":pas,"address":address})

    return render_template('Admin insert account page.html',msg='Registration is Successful')

# Student login database
# ------------------------

@app.route('/stulog_db', methods=['POST'])
def stulog_db():
    y = pri.db.student_reg
    email = request.form['email']
    pas = request.form['pass']
    session['email']=email
    for i in y.find({"email": email, "password": pas}):
        session['Mode'] = i['Mode']
        session['email'] = i['email']
        session['name'] = i['name']
        session['dept'] = i['department']
        t = Message('OTP DETAILS', sender='ocean143oa@gmail.com', recipients=[session['email']])
        x = str(randint(1000, 9999))
        session['otp'] = x
        t.body = "Your otp is :" + x
        mail.send(t)
        return render_template('student OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('student login.html',msg='Login is not correct, please fill out correct format')

# student OTP session
# ------------------------

@app.route('/adotp_db',methods=['POST'])
def adotp_db():
    a=str(request.form['otp'])
    if a==session['otp']:
        return render_template('student next page.html',msg='valid OTP')
    else:
        return render_template('student OTP page.html',msg='Invalid')

# student DELETE database
# -------------------------
@app.route('/studentdel_db')
def studentdel_db():
   y=pri.db.student_reg
   y.delete_one({"student_reg":request.args['reg']})
   return render_template('Admin manage student details.html',msg='This Student account was deleted')

# download code for student
# --------------------------
@app.route('/sendimage2/<name>')
def sendimage2(name):
    path = name
    return send_file(path, as_attachment=True)

# student update database
# --------------------------------
@app.route('/studentup_db',methods=['POST'])
def studentup_db():
   y=pri.db.student_reg
   dept = request.form['dept']
   year = request.form['year']
   phn1 = request.form['phn1']
   phn2 = request.form['phn2']
   email = request.form['email']
   pas1 = request.form['pass']
   address = request.form['address']

   for i in y.find({"Phone No":phn1,"email":email}):
       session['email'] = i['email']
       return render_template('student register page.html',msg='email-Id or Phone Number is already exist')

   y.update({"email":session['email']},{"$set":{"department":dept,"year":year,"phone":phn1,"alt_phone":phn2,"email":email,"password":pas1,"address":address}})

   return render_template('student next page.html',msg='Update is Successful')

# student reply database
# ------------------------
@app.route('/studrep_db', methods=['POST'])
def studrep_db():
   dept = request.form['dept']
   year = request.form['year']
   subject = request.form['descrip']
   email = request.form['email']

   s = pri.db.prin_upload
   t = Message('student Query Message here...', sender='ocean143oa@gmail.com', recipients=[email])
   x = str(subject)
   xy = str(dept)
   xz = str(year)
   # session['subject'] = x
   t.body = "Your subject is : " + x + "\n From : " + xy + " , " + xz
   mail.send(t)
   return render_template('student next page.html', msg='reply message is send Successful')

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
    address = request.form['address']

    y.insert({"name":name1,"initial":name2,"Gender":gen,"DOB":dob,"Age":age,"department":dept,"phone":phn1,"altphone":phn2,"email":email,"password":pas,"address":address})

    return render_template('Admin login page.html',msg='Registration is Successful')

# Admin login database
# ------------------------

@app.route('/adminlog_db', methods=['POST'])
def adminlog_db():
    y = pri.db.admin_reg
    email = request.form['email1']
    pas = request.form['pass']
    for i in y.find({"email": email, "password": pas}):
        session['email'] = i['email']
        t = Message('OTP DETAILS', sender='ocean143oa@gmail.com', recipients=[session['email']])
        x = str(randint(1000, 9999))
        session['otp'] = x
        t.body = "Your otp is :" + x
        mail.send(t)
        return render_template('Admin OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('Admin login page.html',msg='Login is not correct please fill out correct format')

# admin OTP session
# --------------------

@app.route('/adotp1_db',methods=['POST'])
def adotp1_db():
    b=str(request.form['otp'])
    if b==session['otp']:
        return render_template('Admin next page.html',msg='valid OTP')
    else:
        return render_template('Admin OTP page.html',msg='Invalid')

# Admin feedback database
# ------------------------

@app.route('/adminfeed_db', methods=['POST'])
def adminfeed_db():
    y = pri.db.admin_feed
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    session['email']=email
    y.insert({"name": name,"email": email,"subject":subject,"message":message})

    return render_template('index.html', msg='Feedback Uploaded Successful')

# Admin Reply feedback database
# -----------------------------

@app.route('/admfeedrep_db', methods=['POST'])
def admfeedrep_db():
    # y = pri.db.admin_feedrep
    subject = request.form['descrip']
    file = request.files['myfile']
    email=request.form['email']
    file.save(file.filename)
    # y.insert({'subject':subject,'admin_reply_gal': file.filename})

    s = pri.db.admin_feed

    t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[email])
    x = str(subject)
    # session['subject'] = x
    t.body = "Your subject is :" + x
    # with app.open_resource(file.filename) as fp:
    #    t.attach(file.filename, "doc/docx", fp.read())
    mail.send(t)
    return render_template('Admin reply feedback notification.html', msg='reply is send Successful')


    # return render_template('Admin reply feedback notification.html', msg='Reply Feedback Uploaded Successful')

# Admin feedback DELETE database
# ------------------------------
@app.route('/adfeeddel_db')
def adfeeddel_db():
    y = pri.db.admin_feed
    y.delete_one({"name": request.args['name']})
    return render_template('Admin manage feedback details.html', msg='Feedback Deleted Successful')

# for alumni website
# ------------------

# Alumni login database
# ------------------------

@app.route('/alumni_log', methods=['POST'])
def alumni_log():
    y = pri.db.admin_reg
    y = pri.db.faculty_reg
    y = pri.db.prin_reg
    email = request.form['email']
    pas = request.form['pass']
    for i in y.find({"email": email, "password": pas}):
        session['email'] = i['email']
        session['name'] = i['name']
        t = Message('OTP DETAILS', sender='ocean143oa@gmail.com', recipients=[session['email']])
        x = str(randint(1000, 9999))
        session['otp'] = x
        t.body = "Your otp is :" + x
        mail.send(t)
        return render_template('Alumni OTP page.html', msg='Login is Successful')
        break
    else:
        return render_template('Alumni website main page.html',msg='Login is not correct please fill out correct format')

# alumni OTP session
# --------------------

@app.route('/alumni_otp',methods=['POST'])
def alumni_otp():
    b=str(request.form['otp'])
    if b==session['otp']:
        return render_template('Alumni next page.html',msg='valid OTP')
    else:
        return render_template('Alumni OTP page.html',msg='Invalid')

# alumni register page
# --------------------
@app.route('/alumnireg_db',methods=['POST'])
def alumnireg_db():
    y=pri.db.alumni_reg
    name1 = request.form['name1']
    name2 = request.form['name2']
    mode = request.form['mode']
    dept = request.form['dept']
    academy_year = request.form['year']
    phone = request.form['phone']
    email = request.form['email']

    y.insert({"name":name1,"initial":name2,"Mode":mode,"department":dept,"Academic_year":academy_year,"phone":phone,"email":email})

    return render_template('Alumni next page.html',msg='Alumni Registration is Successful')

# alumni find(search) page
# --------------------
@app.route('/alumni_find',methods=['POST'])
def alumni_find():
    mode = request.form['mode']
    dept = request.form['dept']
    academy_year = request.form['year']

    y = pri.db.alumni_reg

# alumni faculty & principal send message page
# ---------------------------------------------
@app.route('/alumnimsg_db',methods=['POST'])
def alumnimsg_db():
    y = pri.db.alumni_info
    Mode = request.form['mode']
    dept = request.form['dept']
    year = request.form['year']
    descrip = request.form['descrip']
    myfile = request.files['myfile']
    myfile.save(myfile.filename)
    y.insert({"Mode": Mode, "department": dept,"Academic_year":year,"description":descrip,"my_file":myfile.filename})

    y = pri.db.alumni_reg
    for i in y.find({"Mode":Mode.lower(),"department":dept,"Academic_year":year}):
        #session['Mode']=i['Mode']
        #session['department'] = i['dept']
        #session['Academic_year'] = i['year']
        subject = "You have Received Some message from BGCW.... \n please check the message to BGCW official Website \n bgcwinfo.com"
        t = Message('BGCW Reply Message', sender='ocean143oa@gmail.com', recipients=[i['email']])
        x = str(subject)
        t.body = "Your Message is : (Alumni)" + x
        mail.send(t)
        return render_template('Alumni next page.html', msg='message send Successful')
        break
    else:
        return render_template('Alumni next page.html', msg='Specifying details are not correct')

app.run(debug=True)

