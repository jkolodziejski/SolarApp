import pandas as pd
import requests
import matplotlib.pyplot as plt


def CashPurchaseSavings(aCashPurchaseSavings):
    paybackYears = []
    panelConfigIndex = []
    for i in aCashPurchaseSavings:
        if (i['panelConfigIndex'] != -1):
            panelConfigIndex.append(i["panelConfigIndex"])
            paybackYears.append(i['cashPurchaseSavings']['paybackYears'])
    plt.xticks(rotation=90)
    plt.plot(panelConfigIndex, paybackYears)
    plt.xlabel('Amount of panels')
    plt.ylabel('Payback Years')
    plt.title('Number of years until payback occurs')
    plt.show()

def SolarPanelConfig(aPotencial):
    panelsCount = []
    yearlyEnergyDcKwh = []
    for i in aPotencial:
        panelsCount.append(i["panelsCount"])
        yearlyEnergyDcKwh.append(i["yearlyEnergyDcKwh"])
    plt.bar(panelsCount, yearlyEnergyDcKwh)
    plt.xlabel('Number of panels')
    plt.ylabel('DC kWh')
    plt.title('How much sunlight energy this layout captures over the course of a year')
    plt.show()

def BillsOver(aCashPurchaseSavings):
    monthlyBill = []
    panelConfigIndex = []
    for i in aCashPurchaseSavings:
        if (i['panelConfigIndex'] != -1):
            monthlyBill.append(i["monthlyBill"]["units"])
            panelConfigIndex.append(i["panelConfigIndex"])
    plt.xticks(rotation=90)
    plt.scatter(monthlyBill, panelConfigIndex)
    plt.xlabel('monthly electric bill $')
    plt.ylabel('Solar layout')
    plt.title('Optimum solar layout for this bill size')
    plt.show()

def getStatistics(inputLatitude, intputLongitude, inputQuality):
    urlSolarAPI = 'https://solar.googleapis.com/v1/'

    bulidingInsights = 'buildingInsights:findClosest?'

    latitude = 'location.latitude'
    longitude = 'location.longitude'
    quality = 'requiredQuality'
    key = 'key'

    inputKey = 'AIzaSyCl_NCBB-wSld15_v7vEIebc0K1cZ98eY4'

    PARAMS = {latitude:inputLatitude,longitude:intputLongitude, quality: inputQuality, key : inputKey }

    r= requests.get( url = urlSolarAPI+bulidingInsights, params = PARAMS)

    data = r.json()

    print(data["imageryDate"]["year"])
    print(data["imageryDate"]["month"])
    SolarPanelConfig(data["solarPotential"]["solarPanelConfigs"])
    BillsOver(data["solarPotential"]["financialAnalyses"])
    CashPurchaseSavings(data["solarPotential"]["financialAnalyses"])












