from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import Expenses,Investments,Investment_tracking
from .utils.utils import format_decimal

def index(request):
    return HttpResponseRedirect(redirect_to="https://phatpham.work")

def redirect(request):
    pass

def get_expenses(request):
    pass

def get_investment_tracking(request):
    # from = request.GET.get('from',None)
    inv_track = Investment_tracking.objects.all().values()
    print("inv_track",list(inv_track))
    # data = {
    #         "data": {
    #             "id": inv_track['id'],
    #             "date": inv_track['date'],
    #             "acbs": format_decimal(str(inv_track['acbs'])),
    #             "mio": format_decimal(str(inv_track['mio'])),
    #             "ssi": format_decimal(str(inv_track['ssi'])),
    #             "dragon": format_decimal(str(inv_track['dragon'])),
    #             "cash": format_decimal(str(inv_track['cash'])),
    #             "total_investment": format_decimal(str(inv_track['total_investment']))
    #         }
    #     }
    data = {
        "data": list(inv_track)
    }
    return JsonResponse(data,safe=False)
