from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")
