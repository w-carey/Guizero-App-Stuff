def login():
	usernameTB		= LOGIN_username				# textbox that stores the users username
	passwordTB		= LOGIN_password				# textbox that stores the users password
	userplaceholder = placeholdertext.get("USERNAME")	# placeholder text for the username textbox
	username, password = usernameTB.value, passwordTB.value # Extracts the username and password from the textboxes
	# Lambda function to reset a textbox (username and password textboxes... )
	# Lambda function to display the error
	displayerror = lambda:guizerostuff.errormessage("Incorrect username and /or password...")
	if username == userplaceholder or not 3<=len(username)<=20 or (" " in username)==True:
		passwordTB.value = ""
		displayerror()
		return
	####
	loginvalid = sqlExecutor(["SELECT user_id FROM bnb_user WHERE user_name == ? AND user_password == ?", (username, password)])
	if loginvalid:
		# If the username and password are correct
		global currentlyloggedinto
		currentlyloggedinto = loginvalid[0][0]
		passwordTB.value = ""
		print("logged in")
		#loginupdaterstuff()
		guizerostuff.changemenu(MENU)
	else:
		# If the username and password are incorrect
		displayerror()
		print("login failed")
	####
####
