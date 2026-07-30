from __future__ import annotations

from BaseClasses import Entrance, Region

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import TimeIsBrokenAgainWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: TimeIsBrokenAgainWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: TimeIsBrokenAgainWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    House1_Area = Region("House 1 Area", world.player, world.multiworld)
    House2_Area = Region("House 2 Area", world.player, world.multiworld)
    House3_Area = Region("House 3 Area", world.player, world.multiworld)
    House4_Area = Region("House 4 Area", world.player, world.multiworld)
    House5_Area = Region("House 5 Area", world.player, world.multiworld)
    Dog_Area = Region("Dog Area", world.player, world.multiworld)
    Dog2_Area = Region("Dog 2 Area", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [House1_Area, House2_Area, House3_Area, House4_Area, House5_Area, Dog_Area, Dog2_Area]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: TimeIsBrokenAgainWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    House1_Area = world.get_region("House 1 Area")
    House2_Area = world.get_region("House 2 Area")
    House3_Area = world.get_region("House 3 Area")
    House4_Area = world.get_region("House 4 Area")
    House5_Area = world.get_region("House 5 Area")
    Dog_Area = world.get_region("Dog Area")
    Dog2_Area = world.get_region("Dog 2 Area")

    House1_Area.connect(House2_Area, "House 1 to House 2")
    House2_Area.connect(House3_Area, "House 2 to House 3")
    House2_Area.connect(House5_Area, "House 2 to House 5")
    House3_Area.connect(House4_Area, "House 3 to House 4")
    House3_Area.connect(Dog_Area, "House 3 to Dog Area")
    House1_Area.connect(Dog_Area, "House 1 to Dog Area")
    House5_Area.connect(House4_Area, "House 5 to House 4")
    House5_Area.connect(Dog2_Area, "House 5 to Dog 2 Area")
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

