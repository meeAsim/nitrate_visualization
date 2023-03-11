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
    main= pd.read_csv('./kleveArea.csv')
    sts = main.describe()

    json_data = sts.reset_index().to_json(orient ='records')
    myjson = json_data
    data = []
    data = json.loads(myjson)
    # print(data)
    context = {
        'list' : kleveCityList,
        'data' : data
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
    fig = plot.scatter_mapbox(
    data,  
    lat='lat',
    lon='long',
    center={"lat": 50.775555, "lon": 6.083611}, 
    width=1024,  
    height=720,  
    color='messergebnis_c',
    hover_data=["name"],  
        )

    fig.update_layout(mapbox_style="open-street-map")

    fig.show()
   
    map = {
        'map':fig
    }

    return render(request, 'dashboard/map.html',map)





def sts_data(request):
    main= pd.read_csv('./kleveArea.csv')
    sts = main.describe()

    json_data = sts.reset_index().to_json(orient ='records')
    myjson = json_data
    data = []
    data = json.loads(myjson)
    context = {'d': data}
    print('this is data fron d : ', data)

    return render(request, '')


 