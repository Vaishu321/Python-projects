import random
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

OPTIONS = ["rock", "paper", "scissors"]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_wins": 0,
            "computer_wins": 0,
            "user_pick": None,
            "computer_pick": None,
            "result": None,
            "result_type": None,
        },
    )


@app.post("/play", response_class=HTMLResponse)
async def play(
    request: Request,
    user_pick: str = Form(...),
    user_wins: int = Form(...),
    computer_wins: int = Form(...),
):
    user_pick = user_pick.lower()
    computer_pick = random.choice(OPTIONS)

    # Determine outcome
    if user_pick == computer_pick:
        result = "It's a tie!"
        result_type = "tie"
    elif (
        (user_pick == "rock" and computer_pick == "scissors")
        or (user_pick == "paper" and computer_pick == "rock")
        or (user_pick == "scissors" and computer_pick == "paper")
    ):
        result = "You won!"
        result_type = "win"
        user_wins += 1
    else:
        result = "You lost!"
        result_type = "loss"
        computer_wins += 1

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_wins": user_wins,
            "computer_wins": computer_wins,
            "user_pick": user_pick,
            "computer_pick": computer_pick,
            "result": result,
            "result_type": result_type,
        },
    )


# import random

# user_wins = 0
# computer_wins = 0

# options = ["rock", "paper", "scissors"]

# while True:
#     user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
#     if user_input == "q":
#         break

#     if user_input not in options:
#         continue

#     random_number = random.randint(0, 2)
#     # rock: 0, paper: 1, scissors: 2
#     computer_pick = options[random_number]
#     print("Computer picked", computer_pick + ".")

#     if user_input == "rock" and computer_pick == "scissors":
#         print("You won!")
#         user_wins += 1

#     elif user_input == "paper" and computer_pick == "rock":
#         print("You won!")
#         user_wins += 1

#     elif user_input == "scissors" and computer_pick == "paper":
#         print("You won!")
#         user_wins += 1

#     else:
#         print("You lost!")
#         computer_wins += 1

# print("You won", user_wins, "times.")
# print("The computer won", computer_wins, "times.")
# print("Goodbye!")