import yfinance as yf
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
import asyncio

async def get_stock_data(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol', '')
        
        # Calculate the start date as 3 months ago from the current date
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
        
        ticker = yf.Ticker(symbol)
        
        # Fetch historical stock data for the last 3 months
        data = await asyncio.to_thread(ticker.history, start=start_date, end=end_date)
        
        response_data = {
            'date': data.index.strftime('%Y-%m-%d').tolist(),
            'close': data['Close'].tolist(),
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})


def index(request):
    return render(request, 'stocks/index.html')
