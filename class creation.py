alltextboxes = []
allboxesWH   = []
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
	def __init__(self, master, *arguments, **keywords):
		gz.TextBox.__init__(self, master, *arguments, **keywords)
		allboxesWH.append(self)
	####
####
