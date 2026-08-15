# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print('Please type a number larger than 0 next time.')
#         quit()
# else:
#     print('Please type a number next time.')
#     quit()

# random_number = random.randint(0, top_of_range)
# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print('Please type a number next time.')
#         continue

#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You were above the number!")
#     else:
#         print("You were below the number!")

# print("You got it in", guesses, "guesses")

import random
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"game_state": "setup"}
    )


@app.post("/start", response_class=HTMLResponse)
async def start_game(request: Request, top_of_range: str = Form(...)):
    if not top_of_range.isdigit() or int(top_of_range) <= 0:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "game_state": "setup",
                "error": "Please enter a number larger than 0 next time.",
            },
        )

    max_num = int(top_of_range)
    target = random.randint(0, max_num)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "game_state": "guessing",
            "target": target,
            "max_num": max_num,
            "guesses": 0,
            "message": None,
        },
    )


@app.post("/guess", response_class=HTMLResponse)
async def make_guess(
    request: Request,
    user_guess: str = Form(...),
    target: int = Form(...),
    max_num: int = Form(...),
    guesses: int = Form(...),
):
    if not user_guess.isdigit():
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "game_state": "guessing",
                "target": target,
                "max_num": max_num,
                "guesses": guesses,
                "error": "Please type a valid number.",
            },
        )

    guess_val = int(user_guess)
    guesses += 1

    # Win Condition
    if guess_val == target:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "game_state": "won",
                "target": target,
                "guesses": guesses,
            },
        )

    # Hint Condition
    message = (
        "You were above the number!"
        if guess_val > target
        else "You were below the number!"
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "game_state": "guessing",
            "target": target,
            "max_num": max_num,
            "guesses": guesses,
            "message": message,
        },
    )