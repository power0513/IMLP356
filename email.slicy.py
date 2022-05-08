email = input('what is your email address?').strip()
#SLICE OUT THE USER NAME
user_name = email[:email.index('@')]
#SLICE OUT THE DOMAIN NAME
domian_name = email[email.index('@')+1:len(email)]

#format message
output = "your user name is '()' and your domain name is '()'".format(user_name,domian_name)
print(output)
