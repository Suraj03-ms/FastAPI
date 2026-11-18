import fastapi
from mockdata import details

f=fastapi.FastAPI()
@f.get("/")
def home():
    return "Hello welcome to fast api!"

@f.get("/about")
def about():
    return "This is a simple FastAPI application."

@f.get("/details")
def get_details():
    return details

@f.get("/detail/{item_id}")
def get_item_by_id(item_id: int):
    for i in details:
        if i.get("id")==item_id:
            return i
    return {"error": "Item not found"}

@f.get("/query")
def query_item(request: fastapi.Request):
    qp = request.query_params
    return f"Hello {qp.get('name')} whose {qp.get('age')} years old, welcome to FastAPI!"