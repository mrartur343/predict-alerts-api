import datetime
from fastapi import FastAPI, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import predict


app = FastAPI()

@app.get("/")
def get_alerts_prediction(region_name: str):
	predict_results = predict.predict_function(region_name+".pkl", datetime.datetime.now().strftime("%m/%d/%Y")).to_dict('records')
	return JSONResponse(predict_results)