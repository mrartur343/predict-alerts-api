import datetime
from typing import Annotated

from fastapi import FastAPI, Query
import predict


regions = [
	"Cherkaska oblast",
	"Chernihivska oblast",
	"Chernivetska oblast",
	"Dnipropetrovska oblast",
	"Donetska oblast",
	"Ivano-Frankivska oblast",
	"Kharkivska oblast",
	"Khersonska oblast",
	"Khmelnytska oblast",
	"Kirovohradska oblast",
	"Kyiv City",
	"Kyivska oblast",
	"Lvivska oblast",
	"Mykolaivska oblast",
	"Odeska oblast",
	"Poltavska oblast",
	"Rivnenska oblast",
	"Sumska oblast",
	"Ternopilska oblast",
	"Vinnytska oblast",
	"Volynska oblast",
	"Zakarpatska oblast",
	"Zaporizka oblast",
	"Zhytomyrska oblast"
]
app = FastAPI()

@app.get("/")
def get_alerts_prediction(region_name: Annotated[str, Query(enum=regions)], days: int):
	predict_results = predict.predict_function(region_name+".pkl", datetime.datetime.now().strftime("%m/%d/%Y"), alert_threshold=0,days_to_predict=int(days)).to_dict('records')
	return list(predict_results)