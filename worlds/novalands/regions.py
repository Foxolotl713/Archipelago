from __future__ import annotations

from BaseClasses import Entrance, Region

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: NovaLandsWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: NovaLandsWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    Menu = Region("Menu", world.player, world.multiworld)
    Researches = Region("Researches", world.player, world.multiworld)
    Islands = Region("Islands", world.player, world.multiworld)


    # Let's put all these regions in a list.
    regions = [Researches, Menu, Islands]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: NovaLandsWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    Researches = world.get_region("Researches")
    Menu = world.get_region("Menu")
    Islands = world.get_region("Islands")
    Researches.connect(Menu,"Researches to Menu")
    Menu.connect(Islands, "Menu to Islands")
    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.

    # You can then connect the Entrance to the target region.
 
    # An even easier way is to use the region.connect helper.

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.

