sqlExecutor(["INSERT INTO tokafitnessDB_user(user_ID, user_forename, user_surname, user_email, user_name, user_password, user_darkmode, user_font, user_premium, user_eventlog) VALUES(?,?,?,?,?,?,?,?,?,?)",
(None, forenameTB.value, surnameTB.value, emailTB.value, usernameTB.value, passwordTB.value, False, "Calibri", 0, "account created on '"+str(datetime.datetime.now())+"'")])
