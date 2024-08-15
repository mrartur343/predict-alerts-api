import datetime
from fastapi import FastAPI, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import predict


app = FastAPI()

@app.get("/")
def get_alerts_prediction(region_name: str):
	predict_results = predict.predict_function(region_name+".pkl", datetime.datetime.now().strftime("%m/%d/%Y"), alert_threshold=0).to_dict('records')
	print(predict_results)
	return list(predict_results)