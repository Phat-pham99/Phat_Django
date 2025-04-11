
from datetime import datetime, date

def format_decimal(string:str) -> str:
    result = ""
    if isinstance(string,str) and "," in string:
        result = string
    else:
        result = "{:,.0f}".format(float(string))
    return result

def compare_date_today(date_str:str) -> str:
    """
    Compare the provided date to today()
    yyyy/mm/dd
    """
    date_str = date_str.split(" ")[0]
    if datetime.strptime(date_str, "%Y-%m-%d").date() <  date.today():
        return f"{datetime.strptime(date_str, '%Y-%m-%d').date()}"
    elif datetime.strptime(date_str, "%Y-%m-%d").date() ==  date.today():
        return f"[yellow]{datetime.strptime(date_str, '%Y-%m-%d').date()}[/yellow]"
    elif datetime.strptime(date_str, "%Y-%m-%d").date() >  date.today():
        return f"[cyan]{datetime.strptime(date_str, '%Y-%m-%d').date()}[/cyan]"

def prep_content(content_list:list,number:int=3,apply_function=None) -> str:
    """
    Input a list of content data, return a single string
    that consists of number of data
    """
    result = ""
    if apply_function == None:
        for item in content_list[0:number]:
            result += str(item) + "\n"
    else:
        for item in content_list[0:number]:
            result += str(apply_function(item)) + "\n"
    return result

def convert_value(value:str) ->str:
    dict = {
        'HASTC': 'HNX',
        'VMPF': "VMEEF",
        "100": "HOSE",
        "200": "HNX",
        "300": "UPCOM",
        "1": "cash",
        "0": "stock"
    }
    if value in dict:
        return dict[value]
    else:
        return value

def format_date(value:str) ->str:
    return f"{value[0:4]}-{value[4:6]}-{value[6:8]}"

def assign_color(ticker:str,color_dict:dict) ->str:
    color = color_dict[ticker]
    return "["+color+"]"+str(ticker)+"[/"+color+"]"

def format_gold(price:str) ->str:
    if "$" in price:
        return price.replace(",","").replace(" $","")
    if "N" in price:
        return price.replace(",","").replace(" N","")+"000"