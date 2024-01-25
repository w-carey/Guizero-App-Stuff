def login():
	usernameTB		= LOGIN_username				# textbox that stores the users username
	passwordTB		= LOGIN_password				# textbox that stores the users password
	userplaceholder = placeholdertext.get("USERNAME")	# placeholder text for the username textbox
	error			= "Incorrect username and /or password..."		# a list to hold all of the errors with the users details
	username, password = usernameTB.value, passwordTB.value # Extracts the username and password from the textboxes
	# Lambda function to reset a textbox (username and password textboxes... )
	resetbox = lambda textbox:[
		textbox.tk.delete(0, tk.END),
		textbox.tk.focus_set(),
		mainapp.tk.focus_set()
	]
	# Lambda function to display the error
	displayerror = lambda:[
		LOGIN_errortext.tk.config(text=error, fg="red")
	]
	if username == userplaceholder or not 3<=len(username)<=20 or (" " in username)==True:
		resetbox(passwordTB)
		displayerror()
		return
	####
	loginvalid = sqlExecutor(["SELECT user_ID FROM tokafitnessDB_user WHERE user_name == ? AND user_password == ?", (username, password)])
	if loginvalid:
		# If the username and password are correct
		global currentlyloggedinto
		currentlyloggedinto = loginvalid[0][0]
		updateeventlog("logged in on '{}'".format(str(datetime.datetime.now()))) # Adds event to the users personal event log
		resetbox(passwordTB)
		print("logged in")
		commandsorter.get("SHOWMENU")()
		commandsorter.get("TOhomemenu")()
		justloggedinchanges()
	else:
		# If the username and password are incorrect
		displayerror()
		print("login failed")
	####
####
