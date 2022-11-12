import uvicorn
import requests

from fastapi import FastAPI
from api.api import api_router

app = FastAPI(title='Final Project Host')
app.include_router(api_router)


# instead using Postman
# def send_file_to_host(path_to_file):
#     requests.post(url='localhost:8000/SeparateToChannels', files={'file': open(path_to_file, 'rb')})

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    main()
