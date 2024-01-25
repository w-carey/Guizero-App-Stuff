windowX, windowY = 712, 518
mainapp = App(title="TOKA FITNESS APP", width=windowX, height=windowY)
mainbox = Box(mainapp, width=windowX-2, height=windowY-10)
mainapp.bg = "#000000"
mainbox.bg = "#3F3F3F"
mainapp.tk.resizable(False, False) # PREVENTS WINDOW RESIZE
mainapp.tk.bind_all("<Button-1>", lambda event: event.widget.focus_set()) # NEEDED FOR PLACEHOLDER STUFF
topbar = Picture(mainbox, image="topbar.png")
mainbox.tk.pack();mainbox.tk.update()
