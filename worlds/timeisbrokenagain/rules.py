from __future__ import annotations

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import TimeIsBrokenAgainWorld

def set_all_rules(world: TimeIsBrokenAgainWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: TimeIsBrokenAgainWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    #overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")
    #overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
    #right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")
    set_rule(world.get_entrance("House 1 to House 2"), lambda state: state.has("TimeUp", world.player, count=1))
    set_rule(world.get_entrance("House 2 to House 3"), lambda state: state.has("TimeUp", world.player, count=3))
    set_rule(world.get_entrance("House 3 to House 4"), lambda state: state.has("TimeUp", world.player, count=2))
    set_rule(world.get_entrance("House 3 to Dog Area"), lambda state: state.has_all(["Dog Scrub cut down", "Dog Food"], world.player))
    set_rule(world.get_entrance("House 1 to Dog Area"), lambda state: state.has("Dog Scrub cut down", world.player) and state.has("TimeUp", world.player, count=2))
    set_rule(world.get_entrance("House 2 to House 5"), lambda state: state.has("TimeUp", world.player, count=1))
    set_rule(world.get_entrance("House 5 to House 4"), lambda state: state.has("TimeUp", world.player, count=2))
    set_rule(world.get_entrance("House 5 to Dog 2 Area"), lambda state: state.has("Dog2 Scrub cut down", world.player))
    # An access rule is a function. We can define this function like any other function.
    # This function must accept exactly one parameter: A "CollectionState".
    # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
    # which regions they've reached, etc.
    # In an access rule, we can ask whether the player has a collected a certain item.
    # We can do this via the state.has(...) function.
    # This function takes an item name, a player number, and an optional count parameter (more on that below)
    # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
    # our function needs to be locally defined so that it has access to the player number from the outer scope.
    # In our case, we are inside a function that has access to the "world" parameter, so we can use world.player.
    #def can_destroy_bush(state: CollectionState) -> bool:
    #    return state.has("Sword", world.player)

    # Now we can set our "can_destroy_bush" rule to our entrance which requires slashing a bush to clear the path.
    # One way to set rules is via the set_rule() function, which works on both Entrances and Locations.
    #set_rule(overworld_to_bottom_right_room, can_destroy_bush)

    # Because the function has to be defined locally, most worlds prefer the lambda syntax.
    #set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))

    # Conditions can depend on event items.
    #set_rule(right_room_to_final_boss_room, lambda state: state.has("Top Left Room Button Pressed", world.player))

    # Some entrance rules may only apply if the player enabled certain options.
    # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # Overworld to the Top Middle Room.
    #if world.options.hammer:
    #    overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
    #    set_rule(overworld_to_top_middle_room, lambda state: state.has("Hammer", world.player))
    pass


def set_all_location_rules(world: TimeIsBrokenAgainWorld) -> None:
    set_rule(world.get_location("Dog Scrub cut down"), lambda state: state.has("Machete", world.player) and state.has("TimeUp", world.player))
    set_rule(world.get_location("Dog2 Scrub cut down"), lambda state: state.has("Machete", world.player))
    set_rule(world.get_location("Dog 1 - 2"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Dog 1 - 3"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Dog Happy"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Dog 2 - 3"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Dog 2 - 4"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Dog2 Happy"), lambda state: state.has("Dog Food", world.player))
    set_rule(world.get_location("Victory"), lambda state: state.has("TimeCrystal", world.player, count=world.options.time_crystals_required_for_goal) and state.has_all(["Dog Happy", "Dog2 Happy"], world.player))
    #if world.options.dog_goal==True:
    #    set_rule(world.get_location("Victory"), lambda state: state.has("TimeCrystal", world.player, count=world.options.time_crystals_required_for_goal) and state.has_all(["Dog Food", "Dog Scrub cut down"], world.player))
    # Location rules work no differently from Entrance rules.
    # Most of our locations are chests that can simply be opened by walking up to them.
    # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # reach the region that the chest sits in.
    # However, our two enemies work differently.
    # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # So, we need to set requirements on the Locations themselves.
    # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.
    # DON'T DO THIS!!!!

    # Now, what's actually wrong with this? It works perfectly fine, right?
    # If hard mode disabled, Sword is enough. If hard mode is enabled, we also need a Shield or a Health Upgrade.
    # The access rule we just wrote does this correctly, so what's the problem?
    # The problem is performance.
    # Most of your world code doesn't need to be perfectly performant, since it just runs once per slot.
    # However, access rules in particular are by far the hottest code path in Archipelago.
    # An access rule will potentially be called thousands or even millions of times over the course of one generation.
    # As a result, access rules are the one place where it's really worth putting in some effort to optimize.
    # What's the performance problem here?
    # Every time our access rule is called, it has to evaluate whether world.options.hard_mode is True or False.
    # Wouldn't it be better if in easy mode, the access rule only checked for Sword to begin with?
    # Wouldn't it also be better if in hard mode, it already knew it had to check Shield and Health Upgrade as well?
    # Well, we can achieve this by doing the "if world.options.hard_mode" check outside the set_rule call,
    # and instead having two *different* set_rule calls depending on which case we're in.

    # Another way to chain multiple conditions is via the add_rule function.
    # This makes the access rules a bit slower though, so it should only be used if your structure justifies it.
    # In our case, it's pretty useful because hard mode and easy mode have different requirements.

    # For the "known" requirements, it's still better to chain them using a normal "and" condition.

        # You can check for multiple copies of an item by using the optional count parameter of state.has().

def set_completion_condition(world: TimeIsBrokenAgainWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)