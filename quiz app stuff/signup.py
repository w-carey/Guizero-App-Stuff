def signup():
	# This is the signup procedure
	forenameTB		= SIGNUP_forename # reassigning the variable name for the Textboxes, these names are much shorter so the code doesnt look messy
	surnameTB		= SIGNUP_surname
	usernameTB		= SIGNUP_username
	passwordTB		= SIGNUP_password
	confirmpTB		= SIGNUP_confirmpassword
	cookiesTB, termsTB, usertypeTB  = SIGNUP_cookies, SIGNUP_terms, SIGNUP_usertype
	forename, surname, email, username, password, confirmpassword, cookies, terms, usernametaken = " ", " ", " ", " ", " ", " ", " ", " ", " "
	hasplaceholder	= lambda textbox:textbox.value==placeholdertext.get(textbox.placeholder) # lambda function to check wether a textbox has its placeholder text in it (EMPTY)
	try:
		# Validation to check wether the forename textbox is empty
		if len(forenameTB.value)==0 or " " in forenameTB.value or hasplaceholder(forenameTB):forename="please fill in forename box"
		# Validation to check wether the surname textbox is empty
		if len(surnameTB.value)==0 or hasplaceholder(surnameTB):surname="please fill in surname box"
		# Validation to check wether the email is written in the correct format ( contains '@' and '.' )
		if 3>len(usernameTB.value) or " " in usernameTB.value  or len(usernameTB.value)>20 or hasplaceholder(usernameTB):username="username must be between 3 and 20 characters"
		# Validation to check wether the password has some level of strength (contains 5 or more characters)
		if len(passwordTB.value)<=5 or hasplaceholder(passwordTB):password="password must be above 5 characters"
		# Validation to check wether the confirmpassword textbox matches the new password box
		if confirmpTB.value != passwordTB.value:confirmpassword="passwords do not match"
		# Validation to check wether the user has accepted cookies
		if cookiesTB.value==0:cookies="please accept cookies"
		# Validation to check wether the user has accepted the terms and conditions
		if termsTB.value==0:terms="please accept terms and conditions"
		# Validation to check wether the username has already been taken (already in use)
		if sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_name == ?", (usernameTB.value,)]):usernametaken="username already taken"
		# Compiles all of the errors from each textbox and the validation above
		errorlist = [x for x in [forename, surname, email, username, password, confirmpassword, cookies, terms, usernametaken] if x != " "]
		errors = "\n - ".join(errorlist)
		if len(errorlist)==0:
			# If the errorlist contains nothing then the user has valid details and their account will be created
			sqlExecutor(["INSERT INTO gibjohn_user(user_id, user_forename, user_surname, user_name, user_password, user_type, user_points, user_classroomid) VALUES(?,?,?,?,?,?,?,?)",
(None, forenameTB.value, surnameTB.value, usernameTB.value, passwordTB.value, usertypeTB.value, 0, None)])
			mainapp.info("SIGNUP", "Account created '{}'".format(usernameTB.value))
			cookiesTB.value = 0;termsTB.value = 0
			####
			if usertypeTB.value==1:
				usertypeTB.value = 0
				sqlExecutor(["INSERT INTO gibjohn_classroom(classroom_id, classroom_joinrequests) VALUES(?,?)", (None, "NEW")])
				classroomid = sqlExecutor(["SELECT classroom_id FROM gibjohn_classroom WHERE classroom_joinrequests == 'NEW'"])[0][0]
				sqlExecutor(["UPDATE gibjohn_classroom SET classroom_joinrequests='[]' WHERE classroom_id == ?", (classroomid,)])
				userid = sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_name == ?", (usernameTB.value,)])[0][0]
				sqlExecutor(["UPDATE gibjohn_user SET user_classroomid = ? WHERE user_id = ?", (classroomid, userid)])
			else:
				userid = sqlExecutor(["SELECT user_id FROM gibjohn_user WHERE user_name == ?", (usernameTB.value,)])[0][0]
				sqlExecutor(["UPDATE gibjohn_user SET user_classroomid = ? WHERE user_id = ?", ("SENDREQUEST", userid)])
			####
			for textbox in [forenameTB, surnameTB, usernameTB, passwordTB, confirmpTB]:
				placeholderfunc(textbox, "reset", False)
			####
			changewindow(LOGIN)
			print("created account")
		else:
			# Exports the errorlist to the user so they can retry and see where they went wrong
			mainapp.error("ERROR!", errors)
			print("signup failed")
	except Exception as error:
		# Extra level of error handling, most likely will not be used but e.g. incase the database does not exist then this will print out the errors
		print("failed checks :=:", error)
	####
####
