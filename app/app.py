from fastapi import FastAPI, HTTPException
from app import DB, object_to_datetime, cheak_user_session

from app.router import authorization
import datetime

app = FastAPI()

app.include_router(authorization.router, prefix="/authorization")
DB.add(BigTask(user_id=user_session.user_id, name=_app.name, icon=_app.icon))

@app.post("/get/tikers/{tiker}", response_model=SessionOutModel)
def registed(tiker: str):
    data = DB.get_first_filter(Tiker, search=(Tiker.id_tiker == 'tiker'))

    print(data)

    return SessionOutModel(session=user_session)