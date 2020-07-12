#!C:\Python35\python.exe
print("content-type: text/html; charset=utf-8\n")

import cgi, os

form = cgi.FieldStorage()

if 'String' in form:
    String= form["String"].value
else:
    String= 'NULL'


def individual_test(String):
    return ('smishing' in String)

result = individual_test(String)


print('''<!doctype html>
<html>
<head>
  <title>function</title>
  <meta charset="utf-8">
</head>
<body>

  <h1><a href="view.py">Back</a></h1>

<h2>{String}</h2>

<br><br>

Smishing Result  :  {result}

</body>
</html>
'''.format(String=String, result= result))
