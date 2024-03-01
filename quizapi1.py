categories = [
    "General Knowledge",
    "Entertainment: Books",
    "Entertainment: Film",
    "Entertainment: Music",
    "Entertainment: Musicals & Theatres",
    "Entertainment: Television",
    "Entertainment: Video Games",
    "Entertainment: Board Games",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Sports",
    "Geography",
    "History",
    "Politics",
    "Art",
    "Celebrities",
    "Animals",
    "Vehicles",
    "Entertainment: Comics",
    "Science: Gadgets",
    "Entertainment: Japanese Anime & Manga",
    "Entertainment: Cartoon & Animations"
]
def runapp():
    global app
    app.hide()
    global question_boxes
    global question_texts
    global category_listbox
    global option_buttons
    # Create the application
    app = Window(app, title="Trivia Quiz", width=800, height=400)
    app.tk.resizable(False, False)
    # Create listbox for category selection
    outerbox = Box(app, width="300", height="fill", align="left")
    category_listbox = ListBox(outerbox, items=categories, width="fill", height="fill", align="left", selected=categories[0])

    # Create button to fetch questions
    outerbox2 = Box(app, align="right", width="fill")
    fetch_button = PushButton(outerbox2, text="Fetch Questions", command=get_questions, align="top")

    # Create boxes to hold question and answer widgets
    question_boxes = []
    for _ in range(5):
        question_boxes.append(Box(outerbox2, width="fill", height="fill", border=True, align="top"))

    # Create text widgets to display questions
    question_texts = []
    for i in range(5):
        question_texts.append(Text(question_boxes[i], text="", size=9, width="fill", height="fill"))

    # Create buttons for options
    option_buttons = []
    for i in range(5):
        option_buttons.append([])
        for j in range(4):
            option_buttons[i].append(PushButton(question_boxes[i], text="", align="left", width="fill", height="fill"))
    get_questions()
    # Display the application
####
