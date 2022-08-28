from flask import Flask, render_template, jsonify
import json
import requests
from flask import request
from types import SimpleNamespace

app = Flask(__name__)

base_url = 'http://351c-34-91-253-60.ngrok.io/result'



@app.route('/result', methods=['GET'])
def data_1():
    url = base_url
    req = requests.get(url)
    req = json.loads(req.content)
    x = req['response_1']
    
    y = json.loads(x, object_hook=lambda d: SimpleNamespace(**d))
    data = []
    data.append({
        "antecedents": y.antecedents,
        "consequents": y.consequents,
        "antecedent_support": y.antecedent_support,
        "consequent_support": y.consequent_support,
        "support": y.support,
        "confidence": y.confidence,
        "lift": y.lift,
        "leverage": y.leverage,
        "conviction": y.conviction
    })
  

    # print(data)

    return render_template('result.html', data=data)


@app.route('/data', methods=['GET'])
def data_2():
    url = base_url
    req = requests.get(url)
    req = json.loads(req.content)
    x = req['response_2']
    
    y = json.loads(x, object_hook=lambda d: SimpleNamespace(**d))
    data = []
    data.append({
        "antecedents": y.antecedents,
        "consequents": y.consequents,
        "antecedent_support": y.antecedent_support,
        "consequent_support": y.consequent_support,
        "support": y.support,
        "confidence": y.confidence,
        "lift": y.lift,
        "leverage": y.leverage,
        "conviction": y.conviction
    })
    return render_template('data.html', data=data)


@app.route('/drink-data', methods=['GET'])
def data_3():
    url = base_url
    req = requests.get(url)
    req = json.loads(req.content)
    x = req['response_3']
    
    y = json.loads(x, object_hook=lambda d: SimpleNamespace(**d))
    data_raw = []
    data_raw.append(
        y.mean
    )

    for i in data_raw:
        data = {
            "Coffe Based": i.COFFEE_BASED,
            "Flavor Latte": i.Flavor_Latte,
            "Konversa Signature": i.KONVERSA_SIGNATURE,
            "Other Drink": i.OTHER_DRINK,
            "Special Blend": i.SPECIAL_BLEND,

        }

        data_value = {
            i.COFFEE_BASED,
            i.Flavor_Latte,
            i.KONVERSA_SIGNATURE,
            i.OTHER_DRINK,
            i.SPECIAL_BLEND,

        }

    min_value = min(data_value, key=lambda ev: ev)
    max_value = max(data_value, key=lambda ev: ev)
    
    # List Label  
    a = 'Coffe Based'
    b = 'Flavor Latte'
    c = 'Konversa Signature'
    d = 'Other Drink'
    e = 'Special Blend'

    # Find min value label
    if data['Coffe Based'] == min_value:
        min_label = a
    elif data['Flavor Latte'] == min_value:
        min_label = b
    elif data['Konversa Signature'] == min_value:
        min_label = c
    elif data['Other Drink'] == min_value:
        min_label = d
    elif data['Special Blend'] == min_value:
        min_label = e

   
    # Find min value label
    if data['Coffe Based'] == max_value:
        max_label = a
    elif data['Flavor Latte'] == max_value:
        max_label = b
    elif data['Konversa Signature'] == max_value:
        max_label = c
    elif data['Other Drink'] == max_value:
        max_label = d
    elif data['Special Blend'] == max_value:
        max_label = e
      
    
    value = {
        "min_label": min_label,
        "max_label": max_label
    }

    
    labels = []
    values = []
    for k, v in data.items():
        labels.append((k))
        values.append((v))
   
    return render_template('drink-data.html', nama=labels, values=values, min_max = value)

@app.route('/meal-data', methods=['GET'])
def data_4():
    url = base_url
    req = requests.get(url)
    req = json.loads(req.content)
    x = req['response_4']
    
    y = json.loads(x, object_hook=lambda d: SimpleNamespace(**d))
    data_raw = []
    data_raw.append(
        y.mean
    )

    for i in data_raw:
        data = {
            "Dessert": i.DESSERT,
            "Food": i.FOOD,
            "Light Meals": i.LIGHT_MEALS,
            "Manual Brew": i.MANUAL_BREW,
            "Promo Morfin": i.Promo_MORFIN,

        }

        data_value = {
            i.DESSERT,
            i.FOOD,
            i.LIGHT_MEALS,
            i.MANUAL_BREW,
            i.Promo_MORFIN,

        }
    
    min_value = min(data_value, key=lambda ev: ev)
    max_value = max(data_value, key=lambda ev: ev)

    # List Label  
    a = 'Dessert'
    b = 'Food'
    c = 'Light Meals'
    d = 'Manual Brew'
    e = 'Promo Morfin'

    # Find min value label
    if data['Dessert'] == min_value:
        min_label = a
    elif data['Food'] == min_value:
        min_label = b
    elif data['Light Meals'] == min_value:
        min_label = c
    elif data['Manual Brew'] == min_value:
        min_label = d
    elif data['Promo Morfin'] == min_value:
        min_label = e

   
    # Find min value label
    if data['Dessert'] == max_value:
        max_label = a
    elif data['Food'] == max_value:
        max_label = b
    elif data['Light Meals'] == max_value:
        max_label = c
    elif data['Manual Brew'] == max_value:
        max_label = d
    elif data['Promo Morfin'] == max_value:
        max_label = e
      
    
    value = {
        "min_label": min_label,
        "max_label": max_label
    }

    
    labels = []
    values = []
    for k, v in data.items():
        labels.append((k))
        values.append((v))
   
    return render_template('meal-data.html', nama=labels, values=values, min_max = value)



@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')






if __name__ == "__main__":
    app.run(debug=True, port=5001)