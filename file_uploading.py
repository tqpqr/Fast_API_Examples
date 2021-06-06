import uvicorn
from typing import List
import shutil
from fastapi import FastAPI, UploadFile, File

api2 = FastAPI()
host = "YOUR_HOST"

#single_file:
@api2.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'file_name': file.filename}

#multiple_files:
@api2.post("/multiple")
async def upload_files(files: List[UploadFile] = File(...)):
    for f in files:
        with open(f'{f.filename}', "wb") as buffer:
            shutil.copyfileobj(f.file, buffer)
    return {'file_name': "Done"}




if __name__ == "__main__":
    uvicorn.run(api2, host=host, port=8000)
