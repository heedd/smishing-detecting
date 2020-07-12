# view.py running server
from flask import Flask, render_template, request

app=Flask(__name__)
import cgi, os

@app.route("/")
def main():
  #!C:\Users\clari\AppData\Local\Programs\Python\Python36\python.exe
  #-*- coding: utf-8 -*-
  print("content-type: text/html; charset=utf-8\n")

  form = cgi.FieldStorage()
  return render_template('view.html')
app.add_url_rule('/view.py', 'main')


@app.route("/function.py", methods=['GET', 'POST'])
def function():
    #!C:\Users\clari\AppData\Local\Programs\Python\Python36\python.exe
    #-*- coding: utf-8 -*-
    print("content-type: text/html; charset=utf-8\n")
    form = cgi.FieldStorage()
    name=request.form['String']
    import individual_test
    ans=individual_test.function(name)
    return render_template('function.html',String=name,ans=ans)


app.run(port=5000, host="0.0.0.0")
# app.run(port=5000, host="localhost"

