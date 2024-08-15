import train

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

print('start_training...')
i=-1
for region_name in regions:
	i+=1
	print(f"{i}/{len(regions)} - {region_name}")
	train.train_function('08/15/2022', region_name,region_name+'.pkl')

print("Autotraining complete!")
