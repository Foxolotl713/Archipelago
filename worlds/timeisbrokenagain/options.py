from __future__ import annotations

from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import TimeIsBrokenAgainWorld
# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  TimeIsBrokenAgain doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/Menu/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.

# A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
class DogGoal(Toggle):
    """Whether the dog needs to be happy before you can escape."""
    display_name = "Goal requires happy dog"

class TimeCrystals(Range):
    """The number of Time Crystals that are available."""
    display_name = "Time Crystals available"
    range_start = 1
    range_end = 11
    default = 10

class TimeCrystalsRequiredForGoal(Range):
    """The number of Time Crystals required to meet the goal."""
    display_name = "Time Crystals Required For Goal"
    range_start = 1
    range_end = 11
    default = 8
# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.



# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class TimeIsBrokenAgainOptions(PerGameCommonOptions):
    dog_goal: DogGoal
    time_crystals: TimeCrystals
    time_crystals_required_for_goal: TimeCrystalsRequiredForGoal

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.


# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
options_presets = {
    "Default": {
        "dog_goal": True,
        "time_crystals": 10,
        "time_crystals_required_for_goal": 8,
    },
}