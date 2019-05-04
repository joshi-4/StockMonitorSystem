from django.shortcuts import render
from .models import Stocks
import requests, json

# API_KEY : IK1FO6GDTJWUAB62
# Create your views here.

API_KEY = 'IK1FO6GDTJWUAB62'



def stocks(request):
	if request.method == 'GET':
		stocks = Stocks.objects.all()
			

		for stock in stocks:
			r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ stock.code+'&apikey=' + API_KEY)
			if (r.status_code == 200):
				json_data = json.loads(r.text)
				#print(json_data)
				d = json_data["Global Quote"]
				
				print(d['02. open'])
				#open_price = json_data.get('Global Quote').get('02. open')
				stock.open_price = d['02. open']
				stock.high_price = d['03. high']
				stock.low_price  = d['04. low']
			
			stock.save()	

				
		context = { 'stocks' : stocks }
	return render(request,'Stocks/stock.html',context)
