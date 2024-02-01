App			= gz.App
Picture		= gz.Picture
Text		= gz.Text
PushButton	= gz.PushButton
CheckBox	= gz.CheckBox
ListBox     = gz.ListBox
Combo		= gz.Combo
class TextBox(gz.TextBox):
	def __init__(self, master, placeholder=None, *arguments, **keywords):
		gz.TextBox.__init__(self, master, *arguments, **keywords)
		self.placeholder = placeholder
		if placeholder:
			placeholderfunc(self, "reset", False)
		####
		alltextboxes.append(self)
	####
####
class Box(gz.Box):
	def __init__(self, master, premium=False, addtomainlist=True, *arguments, **keywords):
		gz.Box.__init__(self, master, *arguments, **keywords)
		self.premium = premium
		if addtomainlist and premium!="REMOVEWHENSIGNOUT":
			allboxesWH.append([self, master])
		####
		self.tk.config(highlightthickness=0, bd=0)
		if premium and premium!="REMOVEWHENSIGNOUT":
			allpremiumboxes.append([self, premium])
		####
	####
####
