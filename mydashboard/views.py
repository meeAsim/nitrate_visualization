from django.shortcuts import render
import pandas as pd
from .models import CityData 
from .models import myData
from .models import kleveMain
from .models import kleveCityData
from datetime import datetime
import plotly.express as plot
import matplotlib.pyplot as mtp
import json
import utm

# Create your views here.
def index(request):
    mydata = CityData.Cname
    context = {
        'data': mydata,
    }
    return render(request,'dashboard/index.html', context)

def wesel(request):
    mydata = CityData.Cname
    context = {
        'wdata': mydata,
    }
    return render(request,'dashboard/wesel.html', context )

def kleve(request):
    kleveCityList = kleveMain.kleveCity
    context = {
        'list' : kleveCityList
    }
    return render(request,'dashboard/kleve.html', context)


## for the figure wesel

def visual(request):
    city = str(request.POST['city'])
    nnvalue= myData.mcvalue.loc[myData.cdata ['name'] == city]
    value = myData.mdate.loc[myData.cdata['name'] == city]
    datevalue = value.str.replace("00:00", " " )
    
    cityname = { 
        'city': city,
        'cdata':datevalue,
        'value': nnvalue
    }
    return render(request,'dashboard/visualize_wesel.html',cityname )


## for the figure kleve

def visualKleve(request):
    city2 = str(request.POST['city'])
    kleveValue = kleveCityData.mvalue.loc[kleveCityData.cdata['name'] == city2] 
    kleveDate = kleveCityData.mdate.loc[kleveCityData.cdata['name'] == city2]
    kleveDate = kleveDate.str.replace("00:00:00", " " )

   
    df = pd.read_csv('./kleveArea.csv')

    cleanTime_list = df['datum_pn'].str.replace("00:00:00", " " )
    

     
    
    

    main= pd.read_csv('./kleveArea.csv')
    mesDate = main['messergebnis_c'].loc[main['name']== city2]
    conClusion = main['messergebnis_cm'].loc[main['name']== city2]
   
   
    # for table data in json
    main_json = main.loc[main['name']== city2]
    json_data = main_json.reset_index().to_json(orient ='records')
    myjson = json_data
    data = []
    data = json.loads(myjson)



    kleveCityDataa = {
        'city' : city2,
        'cdata' : kleveDate,
        'value' : kleveValue,
        'newdata': mesDate,
        'conclu' : conClusion,
        'cdate' : cleanTime_list,
        'tab_data' : data

        
        
    } 
    return render(request, 'dashboard/visualize.html', kleveCityDataa )



def map(request):
   
    data = pd.read_csv('./Kleve_Wesel.csv')
    def getUTMs(row):
        tup = utm.to_latlon(row.iloc[0],row.iloc[1], 32, 'U')
        return pd.Series(tup[:2])

    data[['lat','long']] = data[['e32','n32']].apply(getUTMs , axis=1)
    # fig = plot.scatter_geo(data, lat='lat', lon='lng', hover_name='city')
    fig = plot.scatter_geo(data, lat = data['lat'], lon = data['long'], scope='europe', color = 'name')
    fig.show()

  
    map = {
        'map':fig
    }

    return render(request, 'dashboard/map.html',map)


#making table using jso data

def tabData(request):
    city2 = str(request.POST['city'])
    main= pd.read_csv('./kleveArea.csv')
    main_json = main.loc[main['name']== city2]
    mesDate = main['messergebnis_c'].loc[main['name']== city2]
    conClusion = main['messergebnis_cm'].loc[main['name']== city2]
    # maindata =[mesDate], conClusion]

  
    # json format ma data fatch.
    json_data = main_json.reset_index().to_json(orient ='records')
    myjson = json_data
    data = []
    data = json.loads(myjson)
    context = {'d': data}
    print('this is data fron d : ', data)
  
    return render(request, 'dashboard/visualize.html', context)

 