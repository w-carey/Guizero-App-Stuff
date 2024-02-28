def placeholderfunc(textbox, event, password):
	# This procedure, creates the placeholder text for buttons, makes it easier to see what the textbox is meant to contain
	if event == "<FocusIn event>":
		# Textbox focus in (when a textbox has been clicked on)
		if textbox.value == placeholdertext.get(textbox.placeholder):
			textbox.value = ""
			textbox.text_color = "black"
			textbox.hide_text = password
		####
	elif event == "<FocusOut event>":
		# Textbox focus out (when a textbox is unselected)
		if textbox.value == "":
			textbox.value = placeholdertext.get(textbox.placeholder)
			textbox.text_color = "dark grey"
			textbox.hide_text = False
		####e
	elif event == "reset":
		# Resets a textbox to its placeholder text
		textbox.value = placeholdertext.get(textbox.placeholder)
		textbox.text_color = "dark grey"
		textbox.hide_text = False
	####
####
