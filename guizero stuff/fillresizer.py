def fillresizer():
	# Guizero has a "fill" option when setting the width/height of an object (This changes the width/height to a number e.g. mainapp.width returns 150 instead of "fill")
	for self, master in allboxesWH:
		try:self.tk.pack();self.tk.update()
		except:pass
		if self.width == "fill" and self.tk.winfo_width()!=1:
			self.width = self.tk.winfo_width()
		if self.height == "fill" and master.tk.winfo_height()!=1:
			self.height = self.tk.winfo_height()
		####
	####
	#print(weighttracker_toprightbox.height, weighttracker_bottomrightbox.height)
####
