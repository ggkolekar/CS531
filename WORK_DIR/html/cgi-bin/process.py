#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email = form.getvalue('email')

print ("Content-type:text/html\r\n\r\n")
print ("<HTML>")
print("<body>")
print ("<p>Registration Form</p>")
print("<table align=center datasrc='#xmlRegData' border=2>")
print("<tr>")
print("<td> Name:</td>")
print("<td><span datafld='name'>"+name+"</td>")
print("</tr>")
print("<td>E-mail:</td>")
print("<td><span datafld='email'>"+email+"</td>")
print("</tr>")
print("</table>")
print ("<p>Is this information correct ?</p>")

print("<form method=POST action=/cgi-bin/confirm.py>")
print("<input type=hidden name=name value="+name+">")
print("<input type=hidden name=email value="+email+">")
print ("<input type=radio name='confirm' value='yes'> YES")
print("<input type=radio name='confirm' value='no' checked>NO")
print("<br/>")
print("<br/>")
print ("<input type=submit value=Submit>")
print ("<input type=reset value=Reset>")

print ("</form>")
print("</body>")
print ("</HTML>")

