from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

QUESTIONS = [
    {"id": "q1", "prompt": "What does CPU stand for?", "answer": "central processing unit"},
    {"id": "q2", "prompt": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"id": "q3", "prompt": "What does RAM stand for?", "answer": "random access memory"},
    {"id": "q4", "prompt": "What does PSU stand for?", "answer": "power supply"},
]

@app.get("/", response_class=HTMLResponse)
async def show_quiz(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"questions": QUESTIONS, "results": None}
    )

@app.post("/submit", response_class=HTMLResponse)
async def submit_quiz(request: Request):
    form_data = await request.form()
    score = 0
    results = []

    for q in QUESTIONS:
        user_ans = form_data.get(q["id"], "").strip()
        is_correct = user_ans.lower() == q["answer"]
        if is_correct:
            score += 1
        results.append({
            "prompt": q["prompt"],
            "user_ans": user_ans,
            "correct_ans": q["answer"],
            "is_correct": is_correct
        })

    percentage = (score / len(QUESTIONS)) * 100

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "questions": QUESTIONS,
            "score": score,
            "total": len(QUESTIONS),
            "percentage": percentage,
            "results": results
        }
    )


# print("Welcome to my computer quiz!")

# playing = input("Do you want to play? (Y/N) ")

# if playing.lower() != "y":
#     quit()

# print("Okay! Let's play :)")
# score = 0

# answer = input("What does CPU stand for? ")
# if answer.lower() == "central processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does GPU stand for? ")
# if answer.lower() == "graphics processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does RAM stand for? ")
# if answer.lower() == "random access memory":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does PSU stand for? ")
# if answer.lower() == "power supply":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# print("You got " + str(score) + " questions correct!")
# print("You got " + str((score / 4) * 100) + "%.") 
