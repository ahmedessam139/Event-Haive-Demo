from fastapi import FastAPI, Request, Header
from starlette.responses import FileResponse
from dp.db_functions import *
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse('templates/home.html')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/static/{file_path:path}")
def read_file(file_path: str):
    return FileResponse(f'static/{file_path}')


@app.get("/administration")
def login():
    return FileResponse('templates/administration.html')



@app.get("/generateticket")
def read_tracking():
    print("full data page requested")
    return FileResponse('templates/generateticket.html')
@app.get("/generateticketbyid")
def read_tracking():
    print("id page requested")
    return FileResponse('templates/generateticketbyid.html')
##########################


@app.post("/add_user")
async def add_user(request: Request):
    user_info = await request.json()
    print(user_info)
    # print(user_info)
    # add_user(user_info)
    try:
        print(type(user_info.get("name")),user_info.get("mobile"))
        result = add_visitor(user_info.get("name"), user_info.get("mobile"), user_info.get(
            "email"), user_info.get("nationalId"))
        
    except Exception as e:
        response_data = {"status": "Error in sheet(May be open)"+",Try again"}
        print(e)
        return response_data
        #make result string

    # str_result = str(result)
    response_data = {"status": "ok",
                     "ticket": result}
    
    return response_data

@app.post("/add_user_by_number")
async def add_user_by_number(request: Request):
    user_info = await request.json()
    print(user_info)
    # print(user_info)
    # add_user(user_info)
    try:
        # print(type(user_info.get("name")),user_info.get("mobile"), user_info.get("email") ,user_info.get("nationalId"))
        result = add_visitor_by_number(user_info.get("mobile"), user_info.get("Id"))
        
    except Exception as e:
        response_data = {"status": "Error in sheet(May be open)"+",Try again"}
        print(e)
        return response_data
        #make result string

    # str_result = str(result)
    response_data = {"status": "ok",
                     "ticket": result}
    
    return response_data

