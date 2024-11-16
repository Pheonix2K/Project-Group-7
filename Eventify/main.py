from flask import *
from public import public
from admin import admins
from mod import mods


app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admins)
app.register_blueprint(mods)
    
app.secret_key="secretkey"



app.run(debug=True,port=5004)