from flask import Flask
import os
import msmcauth

app = Flask(__name__)

@app.route('/api')
def api():
   try:
      em = request.args.get('email')
      ps = request.args.get('password')
      resp = msmcauth.login(em, ps)
      return {
        "msg": "success",
        "data": resp
    }
   except Exception as e:
      return {
        "msg": "error",
        "data": str(e)
    }
   
app.run(port=os.getenv('PORT'))