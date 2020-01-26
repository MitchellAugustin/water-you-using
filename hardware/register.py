import urllib2
username = raw_input("Username: ")
password = raw_input("Password: ")
urllib2.urlopen('http://localhost:5000/register/' + username + '/' + password)
