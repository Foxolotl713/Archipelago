from __future__ import annotations

from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import NovaLandsWorld
# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  NovaLands doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/Menu/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.

# A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
class QuickStart(Toggle):
    """Whether to start with the Explorer Needs I, Jetpack and Automation I"""
    display_name = "Quick Start"

class AutomationLogic(Toggle):
    """Whether to require Automation I and II for most of the game"""
    display_name = "Automation Logic"

# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
class Goal(Choice):
    """The goal of the game"""
    option_museum = 1
    option_moschillar = 2
    option_drameleon = 3
    option_tunasa = 4
    default = 2
    display_name = "Goal"

class MuseumDioramaCount(Range):
    """The number of Dioramas required to complete the Museum goal. This option is only relevant if the Goal is set to Museum."""
    range_start = 1
    range_end = 40
    default = 20
    display_name = "Museum Diorama Count"

class BossChecks(Toggle):
    """Adds Locations for defeating and befriending bosses"""
    display_name = "Boss Checks"

class MuseumChecks(Choice):
    """Adds Locations for completing Museum Dioramas or Rooms"""
    option_off = 0
    option_room = 1
    option_diorama = 2
    default = 1
    display_name = "Museum Checks"

class TrapPercentage(Range):
    """The percentage of traps that will be placed in the world. This option is only relevant if the Goal is set to Moschillar, Drameleon or Tunasa."""
    range_start = 0
    range_end = 100
    default = 80
    display_name = "Trap Percentage"

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class NovaLandsOptions(PerGameCommonOptions):
    quick_start: QuickStart
    goal: Goal
    museum_diorama_count: MuseumDioramaCount
    boss_checks: BossChecks
    automation_logic: AutomationLogic
    museum_checks: MuseumChecks
    trap_percentage: TrapPercentage

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.


# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
options_presets = {
    "Default": {
        "quick_start": True,
        "automation_logic": True,
        "goal": 2,
        "museum_diorama_count": 20,
        "boss_checks": True,
        "museum_checks": 1,
        "trap_percentage": 80
    },
}