#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
from multiprocessing import process
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email  = form.getvalue('email')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Registration Form</title>")
print ("</head>")
print ("<body>")
print ("<form action= '/cgi-bin/process.py' method=POST>")
print("Name: <input type=text name=name value='' size=23>")
print("<br>")
print("Email: <input type=text name=email value='' size=23>")
print("<input type=submit value=Submit name=B1>")
print("<input type=reset value=Reset name=B2>")
print("</form>")
#print ("<h2> %s %s</h2>" % (name, email))
print ("</body>")
print ("</html>")