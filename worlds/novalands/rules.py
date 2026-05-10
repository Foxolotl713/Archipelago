from __future__ import annotations

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld

def set_all_rules(world: NovaLandsWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: NovaLandsWorld) -> None:
    researches_to_Menu = world.get_entrance("Researches to Menu")
    menu_to_Islands = world.get_entrance("Menu to Islands")
    set_rule(researches_to_Menu, lambda state: state.has("Automation I", world.player))
    set_rule(menu_to_Islands, lambda state: state.has_all(["Explorer Needs I", "Iron Ingot", "Modular Brick", "Jetpack"], world.player))
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    #overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")
    #overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
    #right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")

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


def set_all_location_rules(world: NovaLandsWorld) -> None:
    set_rule(world.get_location("Research Mass Production I"), lambda state: state.has("Modular Brick", world.player))
    set_rule(world.get_location("Research Explorer Needs I"), lambda state: state.has("Iron Ingot", world.player))
    set_rule(world.get_location("Research Automation I"), lambda state: state.has("Iron Ingot", world.player))
    set_rule(world.get_location("Research Deposits I"), lambda state: state.has("Iron Ingot", world.player))
    set_rule(world.get_location("Research Jetpack"), lambda state: state.has("Iron Ingot", world.player))
    set_rule(world.get_location("Research Farming I"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Research Power I"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Research Automation II"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Research Energy Rifle"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Research Ranching I"), lambda state: state.has("Berry", world.player))
    set_rule(world.get_location("Research Power II"), lambda state: state.has("Glass", world.player))
    set_rule(world.get_location("Research Mass Production II"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Research Deposits II"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Research Suit Armor"), lambda state: state.has("Bone", world.player))
    set_rule(world.get_location("Research Farming II"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Research Explorer Needs III"), lambda state: state.has_all(["Steel", "Plastic"], world.player))
    set_rule(world.get_location("Research Advanced Production I"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Research Explorer Needs II"), lambda state: state.has("Glass", world.player))
    set_rule(world.get_location("Research Ranching II"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Research Overclocking I"), lambda state: state.has("Plastic", world.player))
    set_rule(world.get_location("Research Advanced Production II"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Research Modules I"), lambda state: state.has("Plastic", world.player))
    set_rule(world.get_location("Research Farming III"), lambda state: state.has("Plastic", world.player))
    set_rule(world.get_location("Research Advanced Production III"), lambda state: state.has("Plastic", world.player))
    set_rule(world.get_location("Research Explorer Needs IV"), lambda state: state.has("Plastic", world.player))
    set_rule(world.get_location("Research Ranching III"), lambda state: state.has_all(["Plastic", "Steel"], world.player))
    set_rule(world.get_location("Research Power III"), lambda state: state.has("Plasteel", world.player))
    set_rule(world.get_location("Research Complex Production I"), lambda state: state.has("Plasteel", world.player))
    set_rule(world.get_location("Research Liquids I"), lambda state: state.has_all(["Plastic", "Glass"], world.player))
    set_rule(world.get_location("Research Overclocking II"), lambda state: state.has("Electronic Parts", world.player))
    set_rule(world.get_location("Research Mass Transport"), lambda state: state.has("Electronic Parts", world.player))
    set_rule(world.get_location("Research Glass Works"), lambda state: state.has("Electronic Parts", world.player))
    set_rule(world.get_location("Research Complex Production II"), lambda state: state.has_all(["Titanium Ingot", "Computer Module"], world.player))
    set_rule(world.get_location("Research Superhard Minerals"), lambda state: state.has("Titanium Ore", world.player))
    set_rule(world.get_location("Research Supercomputer"), lambda state: state.has_all(["Advanced Electronic Parts", "Reinforced Super Metal"], world.player))
    set_rule(world.get_location("Research Nuclear Tech"), lambda state: state.has_all(["Behemittium", "Reinforced Super Metal"], world.player))
    set_rule(world.get_location("Research Hypercomputer"), lambda state: state.has_all(["Supercomputer", "Behemittium Battery"], world.player))

    set_rule(world.get_location("Modular Brick"), lambda state: state.has("Furnace", world.player))
    set_rule(world.get_location("Iron Ingot"), lambda state: state.has_all(["Mass Production I", "Furnace"], world.player))
    set_rule(world.get_location("Copper Ingot"), lambda state: state.has_all(["Mass Production I", "Furnace"], world.player) and state.has_any(["Grass Island", "Rock Island"], world.player))
    set_rule(world.get_location("Steel"), lambda state: state.has_all(["Mass Production II", "Iron Ingot", "Copper Ingot", "Electric Furnace"], world.player))
    set_rule(world.get_location("Glass"), lambda state: state.has_all(["Mass Production II", "Electric Furnace", "Desert Island"], world.player))
    set_rule(world.get_location("Plastic"), lambda state: state.has_all(["Advanced Production II", "Industrial Refinery", "Sea Island"], world.player))
    set_rule(world.get_location("Plasteel"), lambda state: state.has_all(["Advanced Production III", "Industrial Refinery", "Plastic", "Steel", "Desert Island", "Ranching III", "Grass Island"], world.player))
    set_rule(world.get_location("Electronic Parts"), lambda state: state.has_all(["Complex Production I", "Assembler", "Plasteel"], world.player) and state.has_any(["Rock Island", "Desert Island"], world.player))
    set_rule(world.get_location("Titanium Ingot"), lambda state: state.has_all(["Superhard Minerals", "Furnace", "Titanium Ore"], world.player))
    set_rule(world.get_location("Titanium Ore"), lambda state: state.has_all(["Metallic Island"], world.player) and state.has_any(["Energy Rifle", "Superhard Minerals", "Automation II"], world.player))
    set_rule(world.get_location("Computer Module"), lambda state: state.has_all(["Complex Production I", "Assembler", "Plasteel", "Electronic Parts"], world.player))
    set_rule(world.get_location("Advanced Electronic Parts"), lambda state: state.has_all(["Complex Production II", "Assembler", "Titanium Ingot", "Computer Module", "Electronic Parts", "Glass", "Iron Ingot", "Electric Furnace"], world.player))
    set_rule(world.get_location("Reinforced Super Metal"), lambda state: state.has_all(["Complex Production II", "Industrial Refinery", "Titanium Ore", "Plasteel", "Snow Island"], world.player))
    set_rule(world.get_location("Behemittium"), lambda state: state.has_all(["Superhard Minerals", "Behemittium Island"], world.player))
    set_rule(world.get_location("Supercomputer Module"), lambda state: state.has_all(["Supercomputer", "Assembler", "Advanced Electronic Parts", "Reinforced Super Metal", "Glass Works", "Industrial Refinery", "Glass", "Liquids I", "Snow Island"], world.player))
    set_rule(world.get_location("Behemittium Battery"), lambda state: state.has_all(["Nuclear Tech", "Industrial Refinery", "Reinforced Super Metal", "Glass Works", "Glass", "Liquids I", "Snow Island", "Behemittium", "Electric Furnace"], world.player))
    
    set_rule(world.get_location("Grass Island"), lambda state: state.has("Iron Ingot", world.player))
    set_rule(world.get_location("Rock Island"), lambda state: state.has_all(["Iron Ingot", "Copper Ingot"], world.player))
    set_rule(world.get_location("Desert Island"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Sea Island"), lambda state: state.has("Steel", world.player))
    set_rule(world.get_location("Forest Island"), lambda state: state.has_all(["Plastic", "Biome Scanner"], world.player))
    set_rule(world.get_location("Snow Island"), lambda state: state.has_all(["Plasteel", "Biome Scanner"], world.player))
    set_rule(world.get_location("Metallic Island"), lambda state: state.has("Snow Island", world.player))
    set_rule(world.get_location("Behemittium Island"), lambda state: state.has_all(["Reinforced Super Metal", "Biome Scanner"], world.player))

    set_rule(world.get_location("Electric Furnace"), lambda state: state.has_all(["Mass Production II", "Modular Brick", "Iron Ingot", "Copper Ingot", "Power"], world.player) or state.has_all(["Advanced Production III", "Modular Brick", "Steel", "Plastic", "Power"], world.player))
    set_rule(world.get_location("Industrial Refinery"), lambda state: state.has_all(["Advanced Production II", "Modular Brick", "Steel", "Power"], world.player))
    set_rule(world.get_location("Assembler"), lambda state: state.has_all(["Complex Production I", "Plasteel", "Modular Brick", "Steel", "Power"], world.player))
    set_rule(world.get_location("Biome Scanner"), lambda state: state.has_all(["Modular Brick", "Steel", "Explorer Needs III"], world.player))

    set_rule(world.get_location("Power",), lambda state: state.has_all(["Power I", "Iron Ingot", "Modular Brick"], world.player) or state.has_all(["Power II", "Glass", "Modular Brick", "Copper Ingot"], world.player) or state.has_all(["Power III", "Plasteel", "Steel", "Glass Works", "Glass", "Liquids I", "Snow Island", "Industrial Refinery", "Electric Furnace"], world.player))
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



def set_completion_condition(world: NovaLandsWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    #world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(["Supercomputer Module", "Behemittium Battery"], world.player)
