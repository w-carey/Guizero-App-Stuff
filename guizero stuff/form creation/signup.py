####
_USELESSBOX_					= Box(SIGNUP, width="fill", height=25)
SIGNUP_backdrop					= Box(SIGNUP, width=mainbox.tk.winfo_width()-285, height=mainbox.tk.winfo_height()-100)
SIGNUP_backdrop.bg				= "#E6E1C1"
_USELESSBOX_					= Box(SIGNUP_backdrop, width="fill", height=15)
SIGNUP_main						= Box(SIGNUP_backdrop, width=SIGNUP_backdrop.width-30, height=SIGNUP_backdrop.height-30)
SIGNUP_main.bg					= "#FFFFFF"
_USELESSBOX_					= Box(SIGNUP_main, width=SIGNUP_main.width, height=5)
_SIGNUPTOPBAR_					= Box(SIGNUP_main, width=SIGNUP_main.width, height=25, border=True)
_SIGNUPTOPBAR_.bg				= "#BFBFBF"
_USELESSBOX_					= Text(_SIGNUPTOPBAR_, width="fill", height="fill", text="SIGNUP FORM")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=30)
SIGNUP_forename					= TextBox(SIGNUP_main, width=35, placeholder="FORENAME")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_surname					= TextBox(SIGNUP_main, width=35, placeholder="SURNAME")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_email					= TextBox(SIGNUP_main, width=35, placeholder="EMAIL")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_username					= TextBox(SIGNUP_main, width=35, placeholder="USERNAME")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_password					= TextBox(SIGNUP_main, width=35, placeholder="PASSWORD")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_confirmpassword			= TextBox(SIGNUP_main, width=35, placeholder="CONFIRMP")
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_errortext				= Text(SIGNUP_main, width="fill", height=1, text="ERROR TEXT HERE...", color="red", size=7)
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_cookies					= CheckBox(SIGNUP_main, text="ACCEPT COOKIES", command=commandsorter.get("DISPLAYcookies"))
SIGNUP_terms					= CheckBox(SIGNUP_main, text="ACCEPT TERMS & CONDITIONS", command=commandsorter.get("DISPLAYterms"))
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=10)
SIGNUP_signupbuttonbox			= Box(SIGNUP_main, width=125, height=25, border=True)
SIGNUP_signupbutton				= PushButton(SIGNUP_signupbuttonbox, width="fill", height="fill", text="CREATE ACCOUNT", command=commandsorter.get("signup"))
SIGNUP_signupbutton.bg			= "#BFBFBF"
_USELESSBOX_					= Box(SIGNUP_main, width="fill", height=5)
SIGNUP_loginbuttonbox			= Box(SIGNUP_main, width=125, height=25, border=True)
SIGNUP_loginbutton				= PushButton(SIGNUP_loginbuttonbox, width="fill", height="fill", text="BACK TO LOGIN", command=commandsorter.get("TOlogin"))
SIGNUP_loginbutton.bg			= "#BFBFBF"
SIGNUP_newlogoimage				= ImageTk.PhotoImage((Image.open("logo.png")).resize((117, 31), Image.Resampling.LANCZOS))
SIGNUP_bottomlogo				= Picture(SIGNUP_main, image=SIGNUP_newlogoimage, align="bottom")
SIGNUP_cookies.tk.config(font=("Calibri", 8), cursor="hand2")
SIGNUP_terms.tk.config(font=("Calibri", 8), cursor="hand2")
SIGNUP_forename.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_forename, str(type), False))
SIGNUP_forename.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_forename, str(type), False))
SIGNUP_surname.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_surname, str(type), False))
SIGNUP_surname.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_surname, str(type), False))
SIGNUP_email.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_email, str(type), False))
SIGNUP_email.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_email, str(type), False))
SIGNUP_username.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_username, str(type), False))
SIGNUP_username.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_username, str(type), False))
SIGNUP_password.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_password, str(type), True))
SIGNUP_password.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_password, str(type), True))
SIGNUP_confirmpassword.tk.bind("<FocusIn>", lambda type: placeholderfunc(SIGNUP_confirmpassword, str(type), True))
SIGNUP_confirmpassword.tk.bind("<FocusOut>", lambda type: placeholderfunc(SIGNUP_confirmpassword, str(type), True))
####