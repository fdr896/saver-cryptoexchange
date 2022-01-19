import listener
import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_events(exchange: str, instrument: str, start_timestamp: int, finish_timestamp: int):
    ans = listener.get_all_msg_in_db(exchange, instrument, start_timestamp,
                                     finish_timestamp)
    print("все ок, но", ans, exchange, instrument, start_timestamp, finish_timestamp)# хочу понять, надо ли как-то изменять ответный джейсон, изменять поля или разделять по data_type
    res = []
    for i in ans:
        tmp = '[' + i[2] + ']'
        res += json.loads(tmp)
    print(res)
    return json.dumps(res)
