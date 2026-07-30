from __future__ import annotations

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld
# For our game to display correctly on the website, we need to define a WebWorld subclass.
class NovaLandsWebWorld(WebWorld):
    # We need to override the "game" field of the WebWorld superclass.
    # This must be the same string as the regular World class.
    game = "Nova Lands"

    # Your game pages will have a visual theme (affecting e.g. the background image).
    # You can choose between dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "dirt"

    # A WebWorld can have any number of tutorials, but should always have at least an English setup guide.
    # Many WebWorlds just have one setup guide, but some have multiple, e.g. for different languages.
    # We need to create a Tutorial object for every setup guide.
    # In order, we need to provide a title, a description, a language, a filepath, a link, and authors.
    # The filepath is relative to a "/docs/" directory in the root folder of your apworld.
    # The "link" parameter is unused, but we still need to provide it.
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Nova Lands for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Gott"],
    )

    # We add these tutorials to our WebWorld by overriding the "tutorials" field.
    tutorials = [setup_en]

