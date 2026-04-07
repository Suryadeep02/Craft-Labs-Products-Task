from fastapi import FastAPI
from app.api.routes import products 

app = FastAPI(title ="Products API(Craft Labs)")
app.include_router(products.router, prefix='/api/v1')




"""
Add a Unit Test
Add a simple business method, such as getThirdProduct, or something similar (the focus is on properly building the unit test with the necessary mocks and assertions, rather than on complex business logic).
Add a unit test that validates that this method Works correctly.
"""