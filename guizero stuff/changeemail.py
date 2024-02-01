def changeemail():
	# This procedure updates the user database to their new email
	newemail, confirmemail = SETTINGS_newemail, SETTINGS_confirmemail
	if newemail.value == confirmemail.value:
		if ("@" in newemail.value) and ("." in newemail.value):
			# If the new email is accepted the database is updated
			sqlExecutor(["UPDATE tokafitnessDB_user SET user_email = ? WHERE user_ID == ?", (newemail.value, currentlyloggedinto)])
			placeholderfunc(newemail, "reset", False)
			placeholderfunc(confirmemail, "reset", False)
			justloggedinchanges()
			mainapp.info("SUCCESS!", "your email has successfully been changed")
		else:
			mainapp.error("ERROR!", "email not in a valid format")
		####
	else:
		mainapp.error("ERROR!", "emails do not match")
	####
####
