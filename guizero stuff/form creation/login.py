_USELESSBOX_					= Box(LOGIN, width="fill", height=25)
LOGIN_backdrop					= Box(LOGIN, width=mainbox.tk.winfo_width()-285, height=mainbox.tk.winfo_height()-100)
LOGIN_backdrop.bg				= "#E6E1C1"
_USELESSBOX_					= Box(LOGIN_backdrop, width="fill", height=15)
LOGIN_main						= Box(LOGIN_backdrop, width=LOGIN_backdrop.width-30, height=LOGIN_backdrop.height-30)
LOGIN_main.bg					= "#FFFFFF"
_USELESSBOX_					= Box(LOGIN_main, width=LOGIN_main.width, height=5)
_LOGINTOPBAR_					= Box(LOGIN_main, width=LOGIN_main.width, height=25, border=True)
_LOGINTOPBAR_.bg				= "#BFBFBF"
_USELESSBOX_					= Text(_LOGINTOPBAR_, width="fill", height="fill", text="LOGIN FORM")
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=100)
LOGIN_username					= TextBox(LOGIN_main, width=35, placeholder="USERNAME")
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=10)
LOGIN_password					= TextBox(LOGIN_main, width=35, placeholder="PASSWORD")
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=5)
LOGIN_errortext					= Text(LOGIN_main, width="fill", height=1, text="", color="red", size=7)
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=10)
LOGIN_loginbuttonbox			= Box(LOGIN_main, width=125, height=25, border=True)
LOGIN_loginbutton				= PushButton(LOGIN_loginbuttonbox, width="fill", height="fill", text="LOGIN", command=commandsorter.get("login"))
LOGIN_loginbutton.bg			= "#BFBFBF"
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=5)
LOGIN_createaccountbox			= Box(LOGIN_main, width=125, height=25, border=True)
LOGIN_createaccount				= PushButton(LOGIN_createaccountbox, width="fill", height="fill", text="CREATE ACCOUNT", command=commandsorter.get("TOcreateaccount"))
LOGIN_createaccount.bg			= "#BFBFBF"
_USELESSBOX_					= Box(LOGIN_main, width="fill", height=5)
LOGIN_forgotpasswordbox			= Box(LOGIN_main, width=125, height=25, border=True)
LOGIN_forgotpassword			= PushButton(LOGIN_forgotpasswordbox, width="fill", height="fill", text="FORGOT PASSWORD", command=commandsorter.get("TOforgotpassword"))
LOGIN_forgotpassword.bg			= "#BFBFBF"
LOGIN_newlogoimage				= ImageTk.PhotoImage((Image.open("logo.png")).resize((117, 31), Image.Resampling.LANCZOS))
LOGIN_bottomlogo				= Picture(LOGIN_main, image=LOGIN_newlogoimage, align="bottom")
LOGIN_username.tk.bind("<FocusIn>", lambda type: placeholderfunc(LOGIN_username, str(type), False))
LOGIN_username.tk.bind("<FocusOut>", lambda type: placeholderfunc(LOGIN_username, str(type), False))
LOGIN_password.tk.bind("<FocusIn>", lambda type: placeholderfunc(LOGIN_password, str(type), True))
LOGIN_password.tk.bind("<FocusOut>", lambda type: placeholderfunc(LOGIN_password, str(type), True))
