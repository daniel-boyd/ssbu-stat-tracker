from fastapi import FastAPI
from .controllers import standard_2plr_controller
from .models import database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(standard_2plr_controller.router)