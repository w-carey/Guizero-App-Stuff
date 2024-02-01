def changepassword():
	# This procedure updates the user database to their new password
	currentpassword, newpassword, confirmpassword = SETTINGS_currentpass, SETTINGS_newpass, SETTINGS_confirmpass
	oldpassword = sqlExecutor(["SELECT user_password FROM tokafitnessDB_user WHERE user_ID == ?", (currentlyloggedinto, )])[0][0]
	if oldpassword == currentpassword.value:
		if newpassword.value == confirmpassword.value:
			if len(newpassword.value)>5:
				# If the new password meets all requirements and is accepted the database will be updated
				sqlExecutor(["UPDATE tokafitnessDB_user SET user_password = ? WHERE user_ID == ?", (newpassword.value, currentlyloggedinto)])
				placeholderfunc(currentpassword, "reset", False)
				placeholderfunc(newpassword, "reset", False)
				placeholderfunc(confirmpassword, "reset", False)
				mainapp.info("SUCCESS!", "your password has successfully been changed")
			else:
				mainapp.error("ERROR!", "your new password must be more than 5 characters long")
			####
		else:
			mainapp.error("ERROR!", "new passwords do not match")
		####
	else:
		mainapp.error("ERROR!", "old password does not match")
	####
####
