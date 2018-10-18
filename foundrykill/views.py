from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import pandas

# Create your views here.
def index(request):
    with open('foundrykill/data.json', 'r') as csv_file:
        user_data = pandas.read_csv(csv_file, delimiter=',').T.to_dict().values()
        context = {
            'users': user_data
        }
    return render(request, 'foundrykill/index.html', context)
