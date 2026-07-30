from __future__ import annotations

from BaseClasses import Item, ItemClassification

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAME_TO_ID = {
    "Mass Production I" : 1,
    "Explorer Needs I" : 2,
    "Automation I" : 3,
    "Deposits I" : 4,
    "Jetpack" : 5,
    "Farming I" : 6,
    "Power I" : 7,
    "Automation II" : 8,
    "Energy Rifle" : 9,
    "Ranching I" : 10,
    "Power II" : 11,
    "Mass Production II" : 12,
    "Deposits II" : 13,
    "Suit Armor" : 14,
    "Farming II" : 15,
    "Explorer Needs III" : 16,
    "Advanced Production" : 17,
    "Explorer Needs II" : 18,
    "Ranching II" : 19,
    "Overclocking I" : 20,
    "Advanced Production II" : 21,
    "Modules I" : 22,
    "Farming III" : 23,
    "Advanced Production III" : 24,
    "Explorer Needs IV" : 25,
    "Ranching III" : 26,
    "Power III" : 27,
    "Complex Production I" : 28,
    "Liquids I" : 29,
    "Overclocking II" : 30,
    "Mass Transport" : 31,
    "Glass Works" : 32,
    "Complex Production II" : 33,
    "Superhard Minerals" : 34,
    "Supercomputer" : 35,
    "Nuclear Tech" : 36,
    "Hypercomputer" : 37,
    "Air" : 38,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Mass Production I" : ItemClassification.progression,
    "Explorer Needs I" : ItemClassification.progression,
    "Automation I" : ItemClassification.progression,
    "Deposits I" : ItemClassification.progression,
    "Jetpack" : ItemClassification.progression,
    "Farming I" : ItemClassification.useful,
    "Power I" : ItemClassification.progression,
    "Automation II" : ItemClassification.progression,
    "Energy Rifle" : ItemClassification.useful,
    "Ranching I" : ItemClassification.useful,
    "Power II" : ItemClassification.progression,
    "Mass Production II" : ItemClassification.progression,
    "Deposits II" : ItemClassification.progression,
    "Suit Armor" : ItemClassification.useful,
    "Farming II" : ItemClassification.useful,
    "Explorer Needs III" : ItemClassification.progression,
    "Advanced Production" : ItemClassification.progression,
    "Explorer Needs II" : ItemClassification.useful,
    "Ranching II" : ItemClassification.progression,
    "Overclocking I" : ItemClassification.useful,
    "Advanced Production II" : ItemClassification.progression,
    "Modules I" : ItemClassification.progression,
    "Farming III" : ItemClassification.useful,
    "Advanced Production III" : ItemClassification.progression,
    "Explorer Needs IV" : ItemClassification.useful,
    "Ranching III" : ItemClassification.progression,
    "Power III" : ItemClassification.progression,
    "Complex Production I" : ItemClassification.progression,
    "Liquids I" : ItemClassification.progression,
    "Overclocking II" : ItemClassification.useful,
    "Mass Transport" : ItemClassification.useful,
    "Glass Works" : ItemClassification.progression,
    "Complex Production II" : ItemClassification.progression,
    "Superhard Minerals" : ItemClassification.progression,
    "Supercomputer" : ItemClassification.progression,
    "Nuclear Tech" : ItemClassification.progression,
    "Hypercomputer" : ItemClassification.progression,
    "Air" : ItemClassification.filler,
}
# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class NovaLandsItem(Item):
    game = "Nova Lands"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: NovaLandsWorld) -> str:
    # NovaLands has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    return "Air"


def create_item_with_correct_classification(world: NovaLandsWorld, name: str) -> NovaLandsItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.

    return NovaLandsItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: NovaLandsWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.
    itempool : list[NovaLandsItem] = [
        world.create_item("Deposits I"),
        world.create_item("Farming I"),
        world.create_item("Power I"),
        world.create_item("Automation II"),
        world.create_item("Energy Rifle"),
        world.create_item("Ranching I"),
        world.create_item("Power II"),
        world.create_item("Mass Production II"),
        world.create_item("Deposits II"),
        world.create_item("Suit Armor"),
        world.create_item("Farming II"),
        world.create_item("Explorer Needs III"),
        world.create_item("Advanced Production"),
        world.create_item("Explorer Needs II"),
        world.create_item("Ranching II"),
        world.create_item("Overclocking I"),
        world.create_item("Advanced Production II"),
        world.create_item("Modules I"),
        world.create_item("Farming III"),
        world.create_item("Advanced Production III"),
        world.create_item("Explorer Needs IV"),
        world.create_item("Ranching III"),
        world.create_item("Power III"),
        world.create_item("Complex Production I"),
        world.create_item("Liquids I"),
        world.create_item("Overclocking II"),
        world.create_item("Mass Transport"),
        world.create_item("Glass Works"),
        world.create_item("Complex Production II"),
        world.create_item("Superhard Minerals"),
        world.create_item("Supercomputer"),
        world.create_item("Nuclear Tech"),
        world.create_item("Hypercomputer"),
    ]
    if not world.options.quick_start:
        itempool.append(world.create_item("Mass Production I"))
        itempool.append(world.create_item("Explorer Needs I"))
        itempool.append(world.create_item("Automation I"))
        itempool.append(world.create_item("Jetpack"))
    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # NovaLands has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to NovaLands's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including NovaLands.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # NovaLands is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    if world.options.quick_start:
        starting_item = world.create_item("Mass Production I")
        world.push_precollected(starting_item)
        starting_item2 = world.create_item("Explorer Needs I")
        world.push_precollected(starting_item2)
        starting_item3 = world.create_item("Automation I")
        world.push_precollected(starting_item3)
        starting_item4 = world.create_item("Jetpack")
        world.push_precollected(starting_item4)