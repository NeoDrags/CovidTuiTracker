from CovidTuiTracker.choicePicker import Picker
import prompt_toolkit as prompt
import inquirer
import os
import json
from CovidTuiTracker.tracker import Tracker

class runner:
    pathJson = os.path.abspath("settings.json")
    def __init__(self) -> None:
        pass
    def runner(self):
        if os.path.exists(path = self.pathJson) == False:
            with open(str(self.pathJson), "w") as file:
                data = {}
                os.system('cls' if os.name == 'nt' else 'clear')
                picker = Picker()
                continent = picker.chooseContinent()
                data.update(continent)
                os.system('cls' if os.name == 'nt' else 'clear')
                country = picker.chooseCountry(continent["Continent"])
                data.update(country)
                json.dump(data, file)
        else:
            prompt.print_formatted_text("Enter what you want to do: ")
            options = [
                inquirer.List(
                    'Choices',
                    choices= ["Reset Options", "Display Data"],
                    carousel=True
                )
            ]
            choice = inquirer.prompt(options)
            choice = choice["Choices"]
            if choice.lower() == "reset options":
                with open(str(self.pathJson), "w") as file:
                    data = {}
                    os.system('cls' if os.name == 'nt' else 'clear')
                    picker = Picker()
                    continent = picker.chooseContinent()
                    data.update(continent)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    country = picker.chooseCountry(continent["Continent"])
                    data.update(country)
                    json.dump(data, file)
            else:
                print("Enter which data you want to display: ")
                optionChoose = [
                    inquirer.List(
                        'Choice',
                        choices= ["World", "Continent", "Country"],
                        carousel= True
                    )
                ]
                theChoice = inquirer.prompt(optionChoose)['Choice']
                tracker = Tracker()
                if theChoice == "World":
                    tracker.World()
                elif theChoice == "Country":
                    tracker.Country()
                else:
                    tracker.Continent()
