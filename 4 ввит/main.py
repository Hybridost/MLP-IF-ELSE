from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
import pyjokes

app = FastAPI(title="Joke API", version="1.0.0")

class JokeInput(BaseModel):
    friend: str = Field(..., min_length=2, max_length=30)

    @field_validator('friend')
    def validate_friend(cls, v):
        if not v.strip():
            raise ValueError('Имя не может быть пустым')
        return v.strip()

class JokeOutput(BaseModel):
    friend: str
    joke: str

#Задание 1
@app.get("/", response_model=JokeOutput, status_code=status.HTTP_200_OK)
async def joke():
    return JokeOutput(friend="Anonymous", joke=pyjokes.get_joke())

@app.get("/{friend}", response_model=JokeOutput, status_code=status.HTTP_200_OK)
async def friends_joke(friend: str):
    # Валидация (Задание 2)
    if len(friend.strip()) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя друга должно содержать минимум 2 символа"
        )
    return JokeOutput(friend=friend.strip(), joke=pyjokes.get_joke())

@app.get("/multi/{friend}", status_code=status.HTTP_200_OK)
async def multi_friends_joke(friend: str, jokes_number: int):

    # Валидация имени
    if len(friend.strip()) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя друга должно содержать минимум 2 символа"
        )

    #Задание 3
    if jokes_number <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Количество шуток должно быть положительным числом"
        )
    if jokes_number > 20:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Слишком много шуток! Максимум 20 за раз"
        )

    result = []
    for i in range(jokes_number):
        result.append(f"{friend} tells joke #{i+1}: {pyjokes.get_joke()}")
    return {"jokes": result}

@app.post("/", 
response_model=JokeOutput, status_code=status.HTTP_201_CREATED)
async def create_joke(joke_input: JokeInput):
    """
    Создать шутку от имени друга (тело запроса в JSON)
    """
    return JokeOutput(friend=joke_input.friend, joke=pyjokes.get_joke())

#Задание 4

@app.get("/joke", response_model=JokeOutput, status_code=status.HTTP_200_OK)
async def joke_by_query(friend: str = "Anonymous"):
    if len(friend.strip()) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя друга должно содержать минимум 2 символа"
        )
    return JokeOutput(friend=friend.strip(), joke=pyjokes.get_joke())

if name == "main":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)