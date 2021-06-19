from pprint import pprint
import requests
import plotext as plt
import json

class Tracker:
    def World(self):
        apiURL = "https://corona.lmao.ninja/v2/continents?yesterday=true&sort"
        getRequest = requests.get(apiURL)
        listOfCases = getRequest.json() 
        n = 0
        sumOfCases = 0
        sumOfRecovered = 0
        sumOfDeaths = 0
        while n < len(listOfCases):
            sumOfCases = sumOfCases + listOfCases[n]['active']
            sumOfRecovered = sumOfRecovered + listOfCases[n]['recovered']
            sumOfDeaths = sumOfDeaths + listOfCases[n]['deaths']
            n = n + 1
        data = [sumOfCases, sumOfRecovered, sumOfDeaths]
        dataText = ["Acitve", "Recovered", "Deaths"]
        plt.bar(dataText, data, color="blue")
        plt.plotsize(100, 30)
        plt.colorless()
        plt.title("World's Current Cases")
        plt.xlabel("Data Text")
        plt.ylabel("Values")
        print("Number of Cases: " + str(sumOfCases))
        print("Number of Recovered Cases: " + str(sumOfRecovered))
        print("Number of Deaths: " + str(sumOfDeaths))
        plt.show()

    def Country(self):
        f = open("settings.json", "r")
        dictionary = json.load(f)
        f.close()
        countryName = dictionary["Country"]
        apiURL = "https://corona.lmao.ninja/v2/countries/" + countryName + "?yesterday=true&sort"
        getRequest = requests.get(apiURL)
        listOfCases = getRequest.json()
        sumOfCases = listOfCases['active']
        sumOfRecovered = listOfCases['recovered']
        sumOfDeaths = listOfCases['deaths']
        data = [sumOfCases, sumOfRecovered, sumOfDeaths]
        dataText = ["Acitve", "Recovered", "Deaths"]
        plt.bar(dataText, data, color="blue")
        plt.plotsize(100, 30)
        plt.colorless()
        plt.title("World's Current Cases")
        plt.xlabel("Data Text")
        plt.ylabel("Values")
        print("Number of Cases: " + str(sumOfCases))
        print("Number of Recovered Cases: " + str(sumOfRecovered))
        print("Number of Deaths: " + str(sumOfDeaths))
        plt.show()

    def Continent(self):
        f = open("settings.json", "r")
        dictionary = json.load(f)
        f.close()
        countryName = dictionary["Continent"]
        apiURL = "https://corona.lmao.ninja/v2/continents/" + countryName + "?yesterday=true&sort"
        getRequest = requests.get(apiURL)
        listOfCases = getRequest.json()
        sumOfCases = listOfCases['active']
        sumOfRecovered = listOfCases['recovered']
        sumOfDeaths = listOfCases['deaths']
        data = [sumOfCases, sumOfRecovered, sumOfDeaths]
        dataText = ["Acitve", "Recovered", "Deaths"]
        plt.bar(dataText, data, color="blue")
        plt.plotsize(100, 30)
        plt.colorless()
        plt.title("World's Current Cases")
        plt.xlabel("Data Text")
        plt.ylabel("Values")
        print("Number of Cases: " + str(sumOfCases))
        print("Number of Recovered Cases: " + str(sumOfRecovered))
        print("Number of Deaths: " + str(sumOfDeaths))
        plt.show()