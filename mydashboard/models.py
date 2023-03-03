from django.db import models

import pandas as pd
import pandasql as ps

# Create your models here.

class CityData(models.Model):
    # City = models.CharField(max_length=200)
    # Nvalue= models.FloatField()
    data = pd.read_csv('./weselArea.csv')

    Cname = data['name'].drop_duplicates()
    print((Cname))

    # print(data)

    def __str__(self):
        return f'{self.Cname}'


class myData(models.Model):
    
  
    cdata = pd.read_csv('./weselArea.csv', error_bad_lines=False)
    cmdata = pd.read_csv('./weselArea.csv')
    cmdata_sort = cmdata.sort_values(by='datum_pn', ascending = True, inplace=True)
    mcvalue = cdata['messergebnis_c']
    mdate = cmdata['datum_pn']

class kleveMain(models.Model):

    kleveData = pd.read_csv('./kleveArea.csv')
    kleveCity = kleveData['name'].drop_duplicates()

    def __str__(self):
        return f'{self.kleveCity}'

class kleveCityData(models.Model):
    cdata = pd.read_csv('./kleveArea.csv', error_bad_lines=False)
    cmdata = pd.read_csv('./kleveArea.csv')
    cmdata_sort = cmdata.sort_values(by='datum_pn', ascending = True, inplace=True)
    mvalue = cdata['messergebnis_c']
    mdate = cmdata['datum_pn']

    print('this is mvalue: ', mvalue)


    
