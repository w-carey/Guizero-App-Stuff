def justloggedinchanges():
	# This procedure runs oncce the user logs in and runs a bunch of functions/procedures required on menu startup
	try:
		updateusereventlog()
		accountdata = sqlExecutor(["SELECT user_email FROM tokafitnessDB_user WHERE user_ID == ?", (currentlyloggedinto, )])[0]
		email = accountdata[0]
		SETTINGS_currentemailtext.tk.config(text=email)
	except:
		# If loading the login changes fails it will be retried 
		print("ERROR! retrying.")
		justloggedinchanges()
	####
####
