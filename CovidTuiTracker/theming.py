from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

class styling:
    style = Style.from_dict({
        'continent': 'ansired bold underline',
        'country': 'ansigreen bold underline',
        'state': 'ansicyan blue underline'
    })