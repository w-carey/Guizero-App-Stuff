	
mainapp,mainbox,newbox = guizerostuff.createapp(712, 518, "app name here")   
LOGIN = guizerostuff.createappwindow()
SIGNUP = guizerostuff.createappwindow()
MENU = guizerostuff.createappwindow()

###createLOGINwindow###
LOGIN_backdrop, LOGIN_main = guizerostuff.setupmainbox(LOGIN)
LOGIN_topbar = guizerostuff.createtopbar(LOGIN_main, "LOGIN FORM")
guizerostuff.uselessbox(LOGIN_main, "fill", 100)
LOGIN_username = guizerostuff.createtextbox(LOGIN_main, "USERNAME...")
guizerostuff.uselessbox(LOGIN_main, "fill", 5)
LOGIN_password = guizerostuff.createtextbox(LOGIN_main, "PASSWORD...", True)
guizerostuff.uselessbox(LOGIN_main, "fill", 15)
LOGIN_LOGINbutton = guizerostuff.createbutton(LOGIN_main, 125, 25, "LOGIN", login)
guizerostuff.uselessbox(LOGIN_main, "fill", 5)
LOGIN_createaccount = guizerostuff.createbutton(LOGIN_main, 125, 25, "CREATE ACCOUNT", lambda:guizerostuff.changemenu(SIGNUP))
###
###createSIGNUPwindow###
SIGNUP_backdrop, SIGNUP_main = guizerostuff.setupmainbox(SIGNUP)
SIGNUP_topbar = guizerostuff.createtopbar(SIGNUP_main, "SIGNUP FORM")
guizerostuff.uselessbox(SIGNUP_main, "fill", 50)
SIGNUP_forename = guizerostuff.createtextbox(SIGNUP_main, "FORENAME...")
guizerostuff.uselessbox(SIGNUP_main, "fill", 5)
SIGNUP_surname = guizerostuff.createtextbox(SIGNUP_main, "SURNAME...")
guizerostuff.uselessbox(SIGNUP_main, "fill", 5)
SIGNUP_username = guizerostuff.createtextbox(SIGNUP_main, "USERNAME...")
guizerostuff.uselessbox(SIGNUP_main, "fill", 5)
SIGNUP_password = guizerostuff.createtextbox(SIGNUP_main, "PASSWORD...", True)
guizerostuff.uselessbox(SIGNUP_main, "fill", 5)
SIGNUP_confirmpassword = guizerostuff.createtextbox(SIGNUP_main, "CONFIRM PASSWORD...", True)
guizerostuff.uselessbox(SIGNUP_main, "fill", 15)
SIGNUP_cookies = guizerostuff.createcheckbox(SIGNUP_main, "ACCEPT COOKIES", None)
SIGNUP_cookies = guizerostuff.createcheckbox(SIGNUP_main, "ACCEPT TERMS & CONDITIONS", None)
guizerostuff.uselessbox(SIGNUP_main, "fill", 25)
SIGNUP_signupbutton = guizerostuff.createbutton(SIGNUP_main, 125, 25, "SIGNUP", None)
guizerostuff.uselessbox(SIGNUP_main, "fill", 5)
SIGNUP_loginbutton = guizerostuff.createbutton(SIGNUP_main, 125, 25, "BACK TO LOGIN", lambda:guizerostuff.changemenu(LOGIN))
###
###createMAINwindow###

###
guizerostuff.changemenu(LOGIN)
mainapp.display()
