from flask import Flask, render_template

app = Flask(__name__)

## 404 error handling

# app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
 #defining function
 return render_template("404.html")



@app.route('/')
def hello_world():
    return 'Hello world'

def goodbye_world():
    return 'But Why Me??!'