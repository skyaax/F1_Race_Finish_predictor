from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

app = FastAPI(title="F1 ML API")
model = load("model_f1.joblib")
#grid_position", "q2_seconds", "q3_seconds","circuit_avg_finish","circuit_avg_points"
class FormulaInput(BaseModel):
    grid_position: int
    q2_seconds: float
    q3_seconds: float
    circuit_avg_finish: float
    circuit_avg_points: float
@app.get("/")
def health_check():
    return {"status": "API is running"}
@app.post("/predict")
def predict(data: FormulaInput):
    features = [[
        data.grid_position,
        data.q2_seconds,
        data.q3_seconds,
        data.circuit_avg_finish,
        data.circuit_avg_points
    ]]
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}