from fastapi import FastAPI, Response
from ttf_indicator.indicator import Indicator

app = FastAPI()

indicator = Indicator()

state = {
    "past": [
        {
            "state": 5.6
        },
        {
            "state": 15
        }
    ]
}


@app.get("/health")
def read_root():
    return "OK"

@app.post("/{username}")
def register_new_user(username: str):
    state[username] = []
    return "user created"


@app.get("/{username}/indicators/{sensor_no}")
def update_patricks_indicator_with_id_1(username: str, sensor_no: int):
    if username not in state:
        return Response(status_code=404, content="User not found")
    user_sensors = state[username]
    if sensor_no >= len(user_sensors):
        return Response(status_code=404, content="Sensor not found")
    return indicator.indicate(state[username][sensor_no]["state"])

@app.post("/{username}/indicators")
def add_new_indicator(username: str):
    if username not in state:
        return Response(status_code=404, content="User not found")
    state[username].append({"state": None})
    return len(state[username]) - 1
    

@app.put("/{username}/indicators/{sensor_no}")
def update_patricks_indicator_with_id_1(username: str, sensor_no: int, ttf: float):
    if username not in state:
        return Response(status_code=404, content="User not found")
    user_sensors = state[username]
    if sensor_no >= len(user_sensors):
        return Response(status_code=404, content="Sensor not found")
    state[username][sensor_no]["state"] = ttf
    return "updated"








