from fastapi import FastAPI
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
    return indicator.indicate(state[username][sensor_no]["state"])
    

@app.put("/{username}/indicators/{sensor_no}")
def update_patricks_indicator_with_id_1(username: str, senor_no: int, ttf: float):
    state[username][senor_no]["state"] = ttf
    return "updated"








