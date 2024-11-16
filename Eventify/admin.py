from flask import *
from database import *

admins=Blueprint('admin',__name__)

@admins.route("/admin")
def admin():
    return render_template("admin.html")

@admins.route("/modmanage",methods=['post','get'])
def modmanage():
    return render_template("modmanage.html")

@admins.route("/modreg",methods=['post','get']) 
def modreg():
    data={}
    a="select * from moderator"
    y=select(a)
    data['view']=y
    print("//////______________",y)

    if 'submit' in request.form:
        uname=request.form['uname']
        psw=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']

        x="insert into login values(null,'%s','%s','mod')"%(uname,psw)
        #res stores the dictionary inside the list at 0 index
        #and prints the dictionary with select query
        res=insert(x)
        query="insert into moderator values(null,'%s','%s','%s','%s','%s')"%(res,fname,lname,email,phone)
        insert(query)

    if 'action' in request.args:
        action=request.args['action']
        #since the session stores id of admin login,we need to set id of mod to access it
        #the condition is set in form submission action
        id=request.args['id']
    else:
        action=None

    if action=='update':
        a="select * from moderator where Moderator_id='%s'"%(id)
        data['up']=select(a)
        print(data['up'],"******************")
    #Also be aware of indentation for conditions and such, since it is causing invisible errors in the program
    if 'upd' in request.form:

        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
    
        #We need to use the column names of table here
        x="update moderator set First_name='%s',Last_name='%s',Email='%s',Phone='%s' where Moderator_id='%s'"%(fname,lname,email,phone,id)
        update(x)

        #for debugging. Alert box popup.
        return "<script>alert('updated');window.location='/modreg'</script>"
        
    if action=='delete':
        #we have to use the id to get the modid instead of using the session
        qry="delete from moderator where Moderator_id='%s'"%(id)
        delete(qry)
        return "<script>alert('Delete');window.location='/admin'</script>"


    return render_template("modreg.html",data=data)

@admins.route('/viewusers')
def viewusers():
    data={}
    qry="select * from user"
    y=select(qry)
    data['uview']=y
    
    qry2="SELECT * FROM login INNER JOIN USER USING(login_id) WHERE usertype='blocked'"
    x=select(qry2)
    data['bview']=x
    
    
    
    return render_template("viewusers.html",data=data)



@admins.route('/maneventcat')
def maneventcat():
    return render_template("maneventcat.html")

@admins.route('/viewevents')
def viewevents():
    return render_template("viewevents.html")

@admins.route('/postsshared')
def postsshared():
    return render_template("postsshared.html")

@admins.route('/particount')
def particount():
    return render_template("particount.html")

@admins.route('/complaints')
def complaints():
    return render_template("complaints.html")

@admins.route('/feedback')
def feedback():
    return render_template("feedback.html")