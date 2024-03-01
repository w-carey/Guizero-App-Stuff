sqlExecutor([sqltable])
# Function to fetch questions based on selected category
category_listbox = None
option_button = None
question_texts = None
question_boxes = None
correct = 0
def get_questions():
    selected_index = categories.index(category_listbox.value)
    response = requests.get("https://opentdb.com/api.php?amount=5&category={}&type=multiple".format(selected_index + 9))
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0:
            for i in range(5):
                question_texts[i].value = html.unescape(data["results"][i]["question"])
                answers = [data["results"][i]["correct_answer"]] + data["results"][i]["incorrect_answers"]
                random.shuffle(answers)
                for j in range(4):
                    option_buttons[i][j].enable()
                    option_buttons[i][j].text = answers[j]
                    if j==4:
                        option_buttons[i][j].update_command(lambda btn=option_buttons[i][j], correct_answer=data["results"][i]["correct_answer"]: check_answer(btn, correct_answer, option_buttons[i], True))
                    else:
                        option_buttons[i][j].update_command(lambda btn=option_buttons[i][j], correct_answer=data["results"][i]["correct_answer"]: check_answer(btn, correct_answer, option_buttons[i], False))
        else:
            app.error("error", "error getting data")
    else:
        app.error("error", "error getting data")
# Function to check the selected answer
def check_answer(button, correct_answer, buttons, finished):
    global correct
    if button.text == correct_answer:
        app.info("Correct!", "You got the answer right!")
        correct += 1
    else:
        app.error("Wrong!", "Sorry, that's not the correct answer.")
    if finished:
        app.info("done", "YOU GOT A SCORE OF {}".format(correct))
        correct = 0
