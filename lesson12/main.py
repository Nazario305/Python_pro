import abc
import random
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse

class GenerationService(abc.ABC):
    @abc.abstractmethod
    async def generate_random_article_idea(self):
        pass

    @abc.abstractmethod
    async def generate_technical_guide(self):
        pass

    @abc.abstractmethod
    async def generate_fiction(self):
        pass

class ArticleGenerationService(GenerationService):
    async def generate_random_article_idea(self):
        ideas = ["Как построить ракету", "Будущее искусственного интеллекта", "10 советов для лучшего сна"]
        await asyncio.sleep(1)  # Имитация асинхронной операции
        return random.choice(ideas)

    async def generate_technical_guide(self):
        guides = ["Как настроить Python-проект", "Понимание асинхронного программирования", "Основы Docker"]
        await asyncio.sleep(1)
        return random.choice(guides)

    async def generate_fiction(self):
        stories = ["Путешествие во времени", "Тайна заколдованного леса", "Приключения на Марсе"]
        await asyncio.sleep(1)
        return random.choice(stories)

app = FastAPI()
service = ArticleGenerationService()

@app.get("/generate-random-idea")
async def generate_random_idea():
    idea = await service.generate_random_article_idea()
    return JSONResponse(content={"idea": idea})

@app.get("/generate-technical-guide")
async def generate_technical_guide():
    guide = await service.generate_technical_guide()
    return JSONResponse(content={"guide": guide})

@app.get("/generate-fiction")
async def generate_fiction():
    fiction = await service.generate_fiction()
    return JSONResponse(content={"fiction": fiction})



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Article Generator API"}
