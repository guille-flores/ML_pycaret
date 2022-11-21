#pip install fastapi
#pip install uvicorn

from fastapi import FastAPI
from pydantic import BaseModel #used to parse and validate data giving user friendly errors
from typing import Union

# Union: Type hinting is a formal solution to statically indicate the type of a value within your Python code.
# For example: 
# def greet(name: str) -> str: this function is stating that the parameter 'name' should be a string, and '->' indicates that the function should return a string
# Type hints help organize and debug the code. It also helps IDEs to recognize data type as the linter function (autocomplete) with bigger code, the more unclear variable data types get.
app = FastAPI()

@app.get("/items/{id}")
def read_item(id:int, q: Union[str, None] = None): 
    #Union help us define/accept multiple types of data for a single variable. In this case, q can be a string or None, andb y default is None if nothing is given.
    return {"item_id": id, "query":q}


#run in terminal line as 'uvicorn {python file name}:{app or however you called the FastAPI variable} --reload'


#--------------------------------------------------------------------------------
# By using one (or more) of these so-called "methods," you can communicate with each of the several paths supported by the HTTP protocol. Typically, you would use:
# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# We will modify our `main.py` file to include a new `PUT` request which will take multiple inputs of different data types.

# BaseModel is a class to inherit functionality such as:
# json() returns a JSON string representation dict(); cf. exporting models
# copy() returns a copy (by default, shallow copy) of the model; cf. exporting models
# parse_obj() a utility for loading any object into a model with error handling if the object is not a dictionary; cf. helper functions
# parse_raw() a utility for loading strings of numerous formats; cf. helper functions
# parse_file() like parse_raw() but for file paths; cf. helper functions
# schema()  returns a dictionary representing the model as JSON Schema; cf. schema
# schema_json() returns a JSON string representation of schema(); cf. schema
# construct() a class method for creating models without running validation; cf. Creating models without validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{id}")
def update_item(id:int, item: Item):
    return {"item id": id, "item name": item.name, "item price": item.price}