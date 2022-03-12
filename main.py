from flask import Flask, request
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
   
app.run(host='0.0.0.0', port=int(os.getenv('PORT')))
