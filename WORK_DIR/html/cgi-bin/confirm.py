#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb
import pymysql

cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email  = form.getvalue('email')
confirm = form.getvalue('confirm')
print ("Content-type:text/html\r\n\r\n")    
if(confirm == 'yes'):

    # Open database connection
    db = pymysql.connect(host="localhost",user="root",password="root",db="cs531" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #first column value will be ignored by database
    #its auto increment value but we need to provide it
    #to avoid column count doesn't match error
    sql="INSERT INTO user_tbl(user_name, user_email, submission_date)VALUES('"+name+"','"+email+"',now())"
    
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database 
    db.commit()
    db.close()
    print ("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1>")
    print ("<TD>")
    print ("<pre>")
    print ("Registration successful")
    print ("Thanks!")
    print ("</TD>")
    print ("</TR>")
    print("</TABLE>")
    
else:
    print ("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1>")
    print ("<TD>")
    print ("<pre>")
    print ("<title>So, the information is correct</title>")

    print ("<a href='/cgi-bin/regist.py'>Please Registration Again</a>")

    print ("<a href='regist.html'>Back To Top</a>")

    print ("</pre>")
    print ("</TD>")
    print ("</TR>")
    print("</TABLE>")