from django.shortcuts import render
from django.contrib import messages
import requests
import json

# Create your views here.

def exchanger(request):
    if request.method == "POST":
        base_cur = request.POST["option-1"]
        target_cur = request.POST["option-2"]
        quantity = request.POST["currency-value"]

        if base_cur and target_cur and quantity:
            api_key = "YOUR API KEY"
            url = "http://data.fixer.io/api/latest?access_key="
            r = requests.get(url + api_key)
            data = json.loads(r.content)
            first = data["rates"][base_cur]
            second = data["rates"][target_cur]
            result = (float(second) / float(first)) * float(quantity)
            return render(request, 'base.html', {"data":data, "result": result, "target_cur": target_cur })

        else:
            messages.warning(request, 'Please choose the currency and write down the quantity')
            return render(request, 'base.html')

    else:
        return render(request, 'base.html')
