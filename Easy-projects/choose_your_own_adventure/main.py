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
        request=request, name="index.html", context={"step": "start"}
    )


@app.post("/play", response_class=HTMLResponse)
async def play(
    request: Request,
    step: str = Form(...),
    name: str = Form("Traveler"),
    choice: str = Form(None),
):
    ctx = {"name": name}

    # STEP 0: Enter Name -> Start Adventure
    if step == "start":
        ctx.update(
            {
                "step": "dirt_road",
                "story": f"Welcome, {name}! You are on a dirt road that has come to an end. You can go left or right.",
            }
        )

    # STEP 1: Dirt Road Choices
    elif step == "dirt_road":
        if choice == "left":
            ctx.update(
                {
                    "step": "river",
                    "story": "You come to a river. You can walk around it or swim across.",
                }
            )
        elif choice == "right":
            ctx.update(
                {
                    "step": "bridge",
                    "story": "You come to a bridge—it looks wobbly! Do you want to cross it or head back?",
                }
            )

    # STEP 2A: River Choices
    elif step == "river":
        if choice == "swim":
            ctx.update(
                {
                    "step": "game_over",
                    "is_win": False,
                    "story": "You swam across and were eaten by an alligator! 🐊",
                }
            )
        elif choice == "walk":
            ctx.update(
                {
                    "step": "game_over",
                    "is_win": False,
                    "story": "You walked for many miles, ran out of water, and lost the game. 🏜️",
                }
            )

    # STEP 2B: Bridge Choices
    elif step == "bridge":
        if choice == "back":
            ctx.update(
                {
                    "step": "game_over",
                    "is_win": False,
                    "story": "You turned back and gave up. Game Over. 🚪",
                }
            )
        elif choice == "cross":
            ctx.update(
                {
                    "step": "stranger",
                    "story": "You cross the bridge safely and meet a stranger. Do you talk to them?",
                }
            )

    # STEP 3: Stranger Choices
    elif step == "stranger":
        if choice == "yes":
            ctx.update(
                {
                    "step": "game_over",
                    "is_win": True,
                    "story": "You talked to the stranger and they gave you a bag of gold! YOU WIN! 💰✨",
                }
            )
        elif choice == "no":
            ctx.update(
                {
                    "step": "game_over",
                    "is_win": False,
                    "story": "You ignored the stranger. They were offended and cursed your journey. You lose. 😤",
                }
            )

    return templates.TemplateResponse(
        request=request, name="index.html", context=ctx
    )



# name = input("Type your name: ")
# print("Welcome", name, "to this adventure!")

# answer = input(
#     "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

# if answer == "left":
#     answer = input(
#         "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

#     if answer == "swim":
#         print("You swam acrross and were eaten by an alligator.")
#     elif answer == "walk":
#         print("You walked for many miles, ran out of water and you lost the game.")
#     else:
#         print('Not a valid option. You lose.')

# elif answer == "right":
#     answer = input(
#         "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

#     if answer == "back":
#         print("You go back and lose.")
#     elif answer == "cross":
#         answer = input(
#             "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

#         if answer == "yes":
#             print("You talk to the stanger and they give you gold. You WIN!")
#         elif answer == "no":
#             print("You ignore the stranger and they are offended and you lose.")
#         else:
#             print('Not a valid option. You lose.')
#     else:
#         print('Not a valid option. You lose.')

# else:
#     print('Not a valid option. You lose.')

# print("Thank you for trying", name)