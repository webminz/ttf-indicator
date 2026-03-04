from fastapi import FastAPI, Response, status
from ttf_indicator.indicator import Indicator
from ttf_indicator.source import Source
from ttf_indicator.collector import Collector
from pathlib import Path
app = FastAPI()

indicator = Indicator()

state = {
    "users": {
        "past": [
            "bergen",
        ],
        "tosin": [
            "trondheim",
        ]
    },
    "sources": {
        "bergen": Source("bergen", Path("data/bergen.csv")),
        "trondheim": Source("trondheim", Path("data/trondheim.csv")),
        "oslo": Source("oslo", Path("data/oslo.csv")),
    }
}

collector = Collector()
indicator = Indicator()

@app.get("/health")
def read_root():
    return "OK"

@app.post("/{username}")
def register_new_user(username: str):
    state["users"][username] = []
    return "user created"

@app.get("/sources")
def get_sources():
    return list(state["sources"].keys())

@app.get("/{username}/indicators")
def get_user_indicators(username: str):
    if username not in state["users"]:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="User not found")
    return state["users"][username]

@app.get("/sources/{source_name}")
def get_source(source_name: str):
    print(state["sources"])
    print(source_name)
    if source_name not in state["sources"]:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="Source not found")
    return {
        "location": state["sources"][source_name].location,
        "last_updated": state["sources"][source_name].get_latest_update()
    }

@app.get("/{username}/indicators/{indicator_no}")
def update_user_indicator_with_id(username: str, indicator_no: int):
    if username not in state["users"]:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="User not found")
    user_indicators = state["users"][username]
    if indicator_no >= len(user_indicators):
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="Indicator not found")
    src = state["users"][username][indicator_no]
    src_obj = state["sources"][src]
    
    return collector.collect(src_obj, indicator)

@app.post("/{username}/indicators")
def add_new_indicator(username: str, src: str):
    if username not in state["users"]:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="User not found")
    if src not in state["sources"]:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="Source not found")
    state["users"][username].append(src)
    return len(state["users"][username]) - 1
    










