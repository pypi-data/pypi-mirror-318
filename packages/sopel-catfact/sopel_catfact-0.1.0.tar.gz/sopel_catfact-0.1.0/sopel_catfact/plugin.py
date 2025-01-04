"""sopel-catfact

Sopel cat facts plugin

Copyright 2018-2024 dgw
Licensed under the Eiffel Forum License 2
"""
from __future__ import annotations

import requests

from sopel import plugin


@plugin.commands('catfact')
@plugin.example('.catfact')
def cat_fact(bot, trigger):
    """Fetch a random cat fact."""
    try:
        r = requests.get(url='https://catfact.ninja/fact', timeout=(10.0, 4.0))
    except requests.exceptions.ConnectTimeout:
        bot.say("Connection timed out.")
        return
    except requests.exceptions.ConnectionError:
        bot.say("Couldn't connect to server.")
        return
    except requests.exceptions.ReadTimeout:
        bot.say("Server took too long to send data.")
        return
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        bot.say("HTTP error: " + str(e))
        return
    try:
        data = r.json()
    except ValueError:
        bot.say("Couldn't decode API response: " + r.content)
        return
    bot.say(data['fact'])
