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
    "Research Mass Production I" : 101,
    "Research Explorer Needs I" : 102,
    "Research Automation I" : 103,
    "Research Deposits I" : 104,
    "Research Jetpack" : 105,
    "Research Farming I" : 106,
    "Research Power I" : 107,
    "Research Automation II" : 108,
    "Research Energy Rifle" : 109,
    "Research Ranching I" : 110,
    "Research Power II" : 111,
    "Research Mass Production II" : 112,
    "Research Deposits II" : 113,
    "Research Suit Armor" : 114,
    "Research Farming II" : 115,
    "Research Explorer Needs III" : 116,
    "Research Advanced Production I" : 117,
    "Research Explorer Needs II" : 118,
    "Research Ranching II" : 119,
    "Research Overclocking I" : 120,
    "Research Advanced Production II" : 121,
    "Research Modules I" : 122,
    "Research Farming III" : 123,
    "Research Advanced Production III" : 124,
    "Research Explorer Needs IV" : 125,
    "Research Ranching III" : 126,
    "Research Power III" : 127,
    "Research Complex Production I" : 128,
    "Research Liquids I" : 129,
    "Research Overclocking II" : 130,
    "Research Mass Transport" : 131,
    "Research Glass Works" : 132,
    "Research Complex Production II" : 133,
    "Research Superhard Minerals" : 134,
    "Research Supercomputer" : 135,
    "Research Nuclear Tech" : 136,
    "Research Hypercomputer" : 137,
    "Moschillar" : 201,
    "Drameleon" : 202,
    "Tunasa" : 203,
    "Museum: 1 Grass Diorama" : 311,
    "Museum: 2 Grass Dioramas" : 312,
    "Museum: 3 Grass Dioramas" : 313,
    "Museum: 4 Grass Dioramas" : 314,
    "Museum: 5 Grass Dioramas" : 315,
    "Museum: 1 Rock Diorama" : 321,
    "Museum: 2 Rock Dioramas" : 322,
    "Museum: 3 Rock Dioramas" : 323,
    "Museum: 4 Rock Dioramas" : 324,
    "Museum: 5 Rock Dioramas" : 325,
    "Museum: 1 Desert Diorama" : 331,
    "Museum: 2 Desert Dioramas" : 332,
    "Museum: 3 Desert Dioramas" : 333,
    "Museum: 4 Desert Dioramas" : 334,
    "Museum: 5 Desert Dioramas" : 335,
    "Museum: 1 Sea Diorama" : 341,
    "Museum: 2 Sea Dioramas" : 342,
    "Museum: 3 Sea Dioramas" : 343,
    "Museum: 4 Sea Dioramas" : 344,
    "Museum: 5 Sea Dioramas" : 345,
    "Museum: 1 Forest Diorama" : 351,
    "Museum: 2 Forest Dioramas" : 352,
    "Museum: 3 Forest Dioramas" : 353,
    "Museum: 4 Forest Dioramas" : 354,
    "Museum: 5 Forest Dioramas" : 355,
    "Museum: 1 Snow Diorama" : 361,
    "Museum: 2 Snow Dioramas" : 362,
    "Museum: 3 Snow Dioramas" : 363,
    "Museum: 4 Snow Dioramas" : 364,
    "Museum: 5 Snow Dioramas" : 365,
    "Museum: 1 Metallic Diorama" : 371,
    "Museum: 2 Metallic Dioramas" : 372,
    "Museum: 3 Metallic Dioramas" : 373,
    "Museum: 4 Metallic Dioramas" : 374,
    "Museum: 5 Metallic Dioramas" : 375,
    "Museum: 1 Behemittium Diorama" : 381,
    "Museum: 2 Behemittium Dioramas" : 382,
    "Museum: 3 Behemittium Dioramas" : 383,
    "Museum: 4 Behemittium Dioramas" : 384,
    "Museum: 5 Behemittium Dioramas" : 385,
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
    Islands = world.get_region("Islands")
    Museum = world.get_region("Museum")
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
    Islands_locations = get_location_names_with_ids(
        [
            "Moschillar",
            "Drameleon",
            "Tunasa"
        ]
    )
    Islands.add_locations(Islands_locations, NovaLandsLocation)
    if world.options.museum_checks == 2:
        Museum_locations = get_location_names_with_ids(
            [
                "Museum: 1 Grass Diorama",
                "Museum: 2 Grass Dioramas",
                "Museum: 3 Grass Dioramas",
                "Museum: 4 Grass Dioramas",
                "Museum: 5 Grass Dioramas",
                "Museum: 1 Rock Diorama",
                "Museum: 2 Rock Dioramas",
                "Museum: 3 Rock Dioramas",
                "Museum: 4 Rock Dioramas",
                "Museum: 5 Rock Dioramas",
                "Museum: 1 Desert Diorama",
                "Museum: 2 Desert Dioramas",
                "Museum: 3 Desert Dioramas",
                "Museum: 4 Desert Dioramas",
                "Museum: 5 Desert Dioramas",
                "Museum: 1 Sea Diorama",
                "Museum: 2 Sea Dioramas",
                "Museum: 3 Sea Dioramas",
                "Museum: 4 Sea Dioramas",
                "Museum: 5 Sea Dioramas",
                "Museum: 1 Forest Diorama",
                "Museum: 2 Forest Dioramas",
                "Museum: 3 Forest Dioramas",
                "Museum: 4 Forest Dioramas",
                "Museum: 5 Forest Dioramas",
                "Museum: 1 Snow Diorama",
                "Museum: 2 Snow Dioramas",
                "Museum: 3 Snow Dioramas",
                "Museum: 4 Snow Dioramas",
                "Museum: 5 Snow Dioramas",
                "Museum: 1 Metallic Diorama",
                "Museum: 2 Metallic Dioramas",
                "Museum: 3 Metallic Dioramas",
                "Museum: 4 Metallic Dioramas",
                "Museum: 5 Metallic Dioramas",
                "Museum: 1 Behemittium Diorama",
                "Museum: 2 Behemittium Dioramas",
                "Museum: 3 Behemittium Dioramas",
                "Museum: 4 Behemittium Dioramas",
                "Museum: 5 Behemittium Dioramas"
            ]
        )
        Museum.add_locations(Museum_locations, NovaLandsLocation)
    elif world.options.museum_checks == 1:
        Museum_locations = get_location_names_with_ids(
            [
                "Museum: 5 Grass Dioramas",
                "Museum: 5 Rock Dioramas",
                "Museum: 5 Desert Dioramas",
                "Museum: 5 Sea Dioramas",
                "Museum: 5 Forest Dioramas",
                "Museum: 5 Snow Dioramas",
                "Museum: 5 Metallic Dioramas",
                "Museum: 5 Behemittium Dioramas"
            ]
        )
        Museum.add_locations(Museum_locations, NovaLandsLocation)
def create_events(world: NovaLandsWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    Researches = world.get_region("Researches")
    Researches2 = world.get_region("Researches2")
    Islands = world.get_region("Islands")
    Captures = world.get_region("Captures")
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
    Researches.add_event("Biome Scanner", "Biome Scanner")
    Researches.add_event("Furnace", "Furnace")
    Researches.add_event("Electric Furnace", "Electric Furnace")
    Researches.add_event("Berry", "Berry")
    Researches.add_event("Modular Brick", "Modular Brick")
    Researches.add_event("Stone", "Stone")
    Researches.add_event("Twig", "Twig")
    Captures.add_event("Antork Capsule", "Antork Capsule")
    Researches.add_event("Iron Ore", "Iron Ore")
    Researches.add_event("Copper Ore", "Copper Ore")
    Captures.add_event("Carancrab Capsule", "Carancrab Capsule")
    Researches.add_event("Sand", "Sand")
    Researches.add_event("Cactus Flower", "Cactus Flower")
    Researches.add_event("Lens", "Lens")
    Captures.add_event("Scortixa Capsule", "Scortixa Capsule")
    Researches.add_event("Stretshroom", "Stretshroom")
    Captures.add_event("Jellyblue Capsule", "Jellyblue Capsule")
    Researches2.add_event("Sweetcane", "Sweetcane")
    Researches2.add_event("Cornillia Flower", "Cornillia Flower")
    Researches2.add_event("Biofuel Bottle", "Biofuel Bottle")
    Researches2.add_event("Lubricant Oil", "Lubricant Oil")
    Captures.add_event("Birbee Capsule", "Birbee Capsule")
    Researches2.add_event("Juice Ball", "Juice Ball")
    Researches2.add_event("Jelly", "Jelly")
    Researches2.add_event("Super Cooler Fluid", "Super Cooler Fluid")
    Captures.add_event("Jellypink Capsule", "Jellypink Capsule")
    Captures.add_event("Arabeetle Capsule", "Arabeetle Capsule")
    Researches2.add_event("Blood Flower", "Blood Flower")
    Researches2.add_event("Super Control Unit", "Super Control Unit")
    Captures.add_event("Moschy Capsule", "Moschy Capsule")
    Researches2.add_event("Plastic", "Plastic")
    Researches2.add_event("Plasteel", "Plasteel")
    Researches2.add_event("Electronic Parts", "Electronic Parts")
    Researches2.add_event("Titanium Ore", "Titanium Ore")
    Researches2.add_event("Titanium Ingot", "Titanium Ingot")
    Researches2.add_event("Computer Module", "Computer Module")
    Researches2.add_event("Advanced Electronic Parts", "Advanced Electronic Parts")
    Researches2.add_event("Supercomputer Module", "Supercomputer Module")
    Researches2.add_event("Reinforced Super Metal", "Reinforced Super Metal")
    Researches2.add_event("Behemittium", "Behemittium")
    Researches2.add_event("Behemittium Battery", "Behemittium Battery")
    Researches2.add_event("Hypercomputer Module", "Hypercomputer Module")
    Researches2.add_event("Assembler", "Assembler")
    Researches2.add_event("Industrial Refinery", "Industrial Refinery")
    Researches2.add_event("Fighter Bot", "Fighter Bot")
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

    if not world.options.automation_logic:
        Researches.add_event("Hand Logic", "Hand Logic")