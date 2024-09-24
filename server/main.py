from fastapi import FastAPI
from .controllers import plr_controller, standard_2plr_controller 
from .models import database
import uvicorn

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(plr_controller.router)
app.include_router(standard_2plr_controller.router)

# Entry point for running the app
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)