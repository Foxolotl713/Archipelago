from __future__ import annotations

from BaseClasses import ItemClassification, Location

from . import items

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld
# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Research Mass Production I" : 1,
    "Research Explorer Needs I" : 2,
    "Research Automation I" : 3,
    "Research Deposits I" : 4,
    "Research Jetpack" : 5,
    "Research Farming I" : 6,
    "Research Power I" : 7,
    "Research Automation II" : 8,
    "Research Energy Rifle" : 9,
    "Research Ranching I" : 10,
    "Research Power II" : 11,
    "Research Mass Production II" : 12,
    "Research Deposits II" : 13,
    "Research Suit Armor" : 14,
    "Research Farming II" : 15,
    "Research Explorer Needs III" : 16,
    "Research Advanced Production I" : 17,
    "Research Explorer Needs II" : 18,
    "Research Ranching II" : 19,
    "Research Overclocking I" : 20,
    "Research Advanced Production II" : 21,
    "Research Modules I" : 22,
    "Research Farming III" : 23,
    "Research Advanced Production III" : 24,
    "Research Explorer Needs IV" : 25,
    "Research Ranching III" : 26,
    "Research Power III" : 27,
    "Research Complex Production I" : 28,
    "Research Liquids I" : 29,
    "Research Overclocking II" : 30,
    "Research Mass Transport" : 31,
    "Research Glass Works" : 32,
    "Research Complex Production II" : 33,
    "Research Superhard Minerals" : 34,
    "Research Supercomputer" : 35,
    "Research Nuclear Tech" : 36,
    "Research Hypercomputer" : 37,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class NovaLandsLocation(Location):
    game = "Nova Lands"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: NovaLandsWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: NovaLandsWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    Researches = world.get_region("Researches")
    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    Researches_locations = get_location_names_with_ids(
        [
            "Research Mass Production I",
            "Research Explorer Needs I",
            "Research Automation I",
            "Research Deposits I",
            "Research Jetpack",
            "Research Farming I",
            "Research Power I",
            "Research Automation II",
            "Research Energy Rifle",
            "Research Ranching I",
            "Research Power II",
            "Research Mass Production II",
            "Research Deposits II",
            "Research Suit Armor",
            "Research Farming II",
            "Research Explorer Needs III",
            "Research Advanced Production I",
            "Research Explorer Needs II",
            "Research Ranching II",
            "Research Overclocking I",
            "Research Advanced Production II",
            "Research Modules I",
            "Research Farming III",
            "Research Advanced Production III",
            "Research Explorer Needs IV",
            "Research Ranching III",
            "Research Power III",
            "Research Complex Production I",
            "Research Liquids I",
            "Research Overclocking II",
            "Research Mass Transport",
            "Research Glass Works",
            "Research Complex Production II",
            "Research Superhard Minerals",
            "Research Supercomputer",
            "Research Nuclear Tech",
            "Research Hypercomputer"
        ]
    )
    Researches.add_locations(Researches_locations, NovaLandsLocation)

def create_events(world: NovaLandsWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    Researches = world.get_region("Researches")
    Islands = world.get_region("Islands")
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


    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
    Researches.add_event("Iron Ingot", "Iron Ingot")
    Researches.add_event("Copper Ingot", "Copper Ingot")
    Researches.add_event("Steel", "Steel")
    Researches.add_event("Glass", "Glass")
    Researches.add_event("Power", "Power")
    Researches.add_event("Bone", "Bone")
    Researches.add_event("Plastic", "Plastic")
    Researches.add_event("Plasteel", "Plasteel")
    Researches.add_event("Electronic Parts", "Electronic Parts")
    Researches.add_event("Titanium Ore", "Titanium Ore")
    Researches.add_event("Titanium Ingot", "Titanium Ingot")
    Researches.add_event("Computer Module", "Computer Module")
    Researches.add_event("Advanced Electronic Parts", "Advanced Electronic Parts")
    Researches.add_event("Supercomputer Module", "Supercomputer Module")
    Researches.add_event("Reinforced Super Metal", "Reinforced Super Metal")
    Researches.add_event("Behemittium", "Behemittium")
    Researches.add_event("Behemittium Battery", "Behemittium Battery")
    Researches.add_event("Modular Brick", "Modular Brick")
    Researches.add_event("Berry", "Berry")
    Researches.add_event("Furnace", "Furnace")
    Researches.add_event("Electric Furnace", "Electric Furnace")
    Researches.add_event("Assembler", "Assembler")
    Researches.add_event("Industrial Refinery", "Industrial Refinery")
    Researches.add_event("Biome Scanner", "Biome Scanner")
    Islands.add_event("Grass Island", "Grass Island")
    Islands.add_event("Rock Island", "Rock Island")
    Islands.add_event("Desert Island", "Desert Island")
    Islands.add_event("Sea Island", "Sea Island")
    Islands.add_event("Forest Island", "Forest Island")
    Islands.add_event("Snow Island", "Snow Island")
    Islands.add_event("Metallic Island", "Metallic Island")
    Islands.add_event("Behemittium Island", "Behemittium Island")
    Islands.add_event("Mysterious Ruins Island", "Mysterious Ruins Island")
    Islands.add_event("Encampment Island", "Encampment Island")
    Islands.add_event("Mysterious Tower Island", "Mysterious Tower Island")
    Islands.add_event("Oasis Island", "Oasis Island")
    Islands.add_event("Space Station", "Space Station")
    Islands.add_event("Matriarch's Island", "Matriarch's Island")
    Islands.add_event("Behemittium Vein Island", "Behemittium Vein Island")
