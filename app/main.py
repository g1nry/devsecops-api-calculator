from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="DevSecOps API Calculator",
    version="v0.1"
)


class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def root():
    return {
        "name": "DevSecOps API Calculator",
        "version": "v0.1"
    }



@app.post("/calculate")
def calculate(request: CalculationRequest):
    if request.operation == "add":
        result = request.a + request.b

    elif request.operation == "subtract":
        result = request.a - request.b

    elif request.operation == "multiply":
        result = request.a * request.b

    elif request.operation == "divide":
        if request.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = request.a / request.b

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown operation: {request.operation}"
        )

    return {"result": result}