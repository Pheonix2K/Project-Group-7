from flask import *
from database import *

mods=Blueprint('mods',__name__)

@mods.route('/moderator')
def moderator():
    return render_template("moderator.html")

@mods.route('/viewusers')
def viewusers():
    return render_template("viewusers.html")

@mods.route('/vieweventcat')
def vieweventcat():
    return render_template("vieweventcat.html")

@mods.route('/modviewevents')
def modviewevents():
    return render_template("modviewevents.html")

@mods.route('/postsshared')
def postsshared():
    return render_template("postsshared.html")

@mods.route('/postuser')
def postuser():
    return render_template("postuser.html")

@mods.route('/complaints')
def complaints():
    return render_template("complaints.html")












