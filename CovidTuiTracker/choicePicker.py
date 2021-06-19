from prompt_toolkit import print_formatted_text as pft
from prompt_toolkit import HTML
from prompt_toolkit.styles import Style
import inquirer
import awoc

class Picker:
    def chooseContinent(self):
        continents = [
            inquirer.List(
                'Continent',
                choices = sorted(["Asia", "North America", "South America", "Australia", "Europe", "Africa", "Antartica"]),
                carousel= True,
            ),
        ]
        style = Style.from_dict({
            'input': 'ansiwhite bold'
        })
        pft(HTML("<input>Enter which continent you are from</input>"), style=style)
        continent = inquirer.prompt(continents)
        return continent

    def chooseCountry(self, continent):
        countriesLister = awoc.AWOC()
        countries = [
            inquirer.List(
                'Country',
                choices=sorted(countriesLister.get_countries_list_of(continent)),
                carousel=True,
                )
        ]
        style = Style.from_dict({
            'input': 'ansiwhite bold'
        })
        pft(HTML("<input>Enter which country you are from</input>"), style=style)
        country = inquirer.prompt(countries)
        return country