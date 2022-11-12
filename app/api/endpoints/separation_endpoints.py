import time

from fastapi import APIRouter, File, UploadFile
from app.api.schemas.seperation_schemas import TrackArgs
from pygame import mixer

router = APIRouter()


@router.post(path="/SeparateToChannels", operation_id='separate to channels')
async def separate_to_channels(file: UploadFile = File(...)):
    mixer.init()
    mixer.music.load(file.file)
    mixer.music.play()
    time.sleep(32)
    return {"msg:": "success"}
