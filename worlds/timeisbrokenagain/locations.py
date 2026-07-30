from __future__ import annotations

from BaseClasses import ItemClassification, Location

from . import items

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import TimeIsBrokenAgainWorld
# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
	"Old Man 1": 11,
	"Old Man 2": 12,
	"Old Man 3": 13,
	"Old Man 4": 14,
	"House 1": 21,
	"House 2": 22,
	"House 3": 23,
	"House 4": 24,
	"House 5": 25,
	"Dog 1 - 1": 31,
	"Dog 1 - 2": 32,
	"Dog 1 - 3": 33,
	"Dog 2 - 1": 34,
	"Dog 2 - 2": 35,
	"Dog 2 - 3": 36,
	"Dog 2 - 4": 37
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class TimeIsBrokenAgainLocation(Location):
    game = "Time is broken again"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: TimeIsBrokenAgainWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: TimeIsBrokenAgainWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    House_1_Area = world.get_region("House 1 Area")
    House_2_Area = world.get_region("House 2 Area")
    House_3_Area = world.get_region("House 3 Area")
    House_4_Area = world.get_region("House 4 Area")
    House_5_Area = world.get_region("House 5 Area")
    Dog_Area = world.get_region("Dog Area")
    Dog2_Area = world.get_region("Dog 2 Area")
    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    House_1_Area_Locations = get_location_names_with_ids(
        [
            "House 1",
            "Old Man 1",
            "Old Man 2",
            "Old Man 3",
            "Old Man 4",
        ]
    )
    House_2_Area_Locations = get_location_names_with_ids(
        [
            "House 2",
        ]
    )
    House_3_Area_Locations = get_location_names_with_ids(
        [
            "House 3",
        ]
    )
    House_4_Area_Locations = get_location_names_with_ids(
        [
            "House 4",
        ]
    )
    House_5_Area_Locations = get_location_names_with_ids(
        [
            "House 5",
        ]
    )
    Dog_Area_Locations = get_location_names_with_ids(
        [
            "Dog 1 - 1",
            "Dog 1 - 2",
            "Dog 1 - 3",
        ]
    )
    Dog2_Area_Locations = get_location_names_with_ids(
        [
            "Dog 2 - 1",
            "Dog 2 - 2",
            "Dog 2 - 3",
            "Dog 2 - 4",
        ]
    )
    House_1_Area.add_locations(House_1_Area_Locations, TimeIsBrokenAgainLocation)
    House_2_Area.add_locations(House_2_Area_Locations, TimeIsBrokenAgainLocation)
    House_3_Area.add_locations(House_3_Area_Locations, TimeIsBrokenAgainLocation)
    House_4_Area.add_locations(House_4_Area_Locations, TimeIsBrokenAgainLocation)
    House_5_Area.add_locations(House_5_Area_Locations, TimeIsBrokenAgainLocation)
    Dog_Area.add_locations(Dog_Area_Locations, TimeIsBrokenAgainLocation)
    Dog2_Area.add_locations(Dog2_Area_Locations, TimeIsBrokenAgainLocation)
def create_events(world: TimeIsBrokenAgainWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    House_4_Area = world.get_region("House 4 Area")
    House_1_Area = world.get_region("House 1 Area")
    House5_Area = world.get_region("House 5 Area")
    Dog_Area = world.get_region("Dog Area")
    Dog2_Area = world.get_region("Dog 2 Area")
    # One way to create an event is simply to use one of the normal methods of creating a location.
    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    House_1_Area.add_event("Dog Scrub cut down", "Dog Scrub cut down")
    House_4_Area.add_event("Victory", "Victory")
    House5_Area.add_event("Dog2 Scrub cut down", "Dog2 Scrub cut down")
    Dog_Area.add_event("Dog Happy", "Dog Happy")
    Dog2_Area.add_event("Dog2 Happy", "Dog2 Happy")
    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)