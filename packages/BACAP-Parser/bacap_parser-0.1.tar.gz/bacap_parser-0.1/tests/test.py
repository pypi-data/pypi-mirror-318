from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.BACAP_Parser import AdvType, Color, constants, AdvTypeManager, Datapack, Parser

task = AdvType(name="task", frames="task", colors=Color("green"))
goal = AdvType(name="goal", frames="goal", colors=Color("#75E1FF"))
challenge = AdvType(name="challenge", frames="challenge", colors=Color("dark_purple"), hidden_color=constants.DEFAULT_BACAP_HIDDEN_COLOR)
super_challenge = AdvType(name="super_challenge", frames="challenge", colors=Color("#FF2A2A"))
root = AdvType(name="root", frames=("task", "challenge"), colors=Color("#CCCCCC"))
milestone = AdvType(name="milestone", frames="goal", colors=Color("yellow"), tabs="bacap")
advancement_legend = AdvType(name="advancement_legend", frames="challenge", colors=Color("gold"), tabs="bacap")
manager = AdvTypeManager([task, goal, challenge, super_challenge, root, milestone, advancement_legend])
bacap = Datapack(name="bacap", path=Path("test_datapacks/bacap"), adv_type_manager=manager, reward_namespace="bacap_rewards", technical_tabs="technical")
bacaped = Datapack(name="bacaped", path=Path("test_datapacks/bacaped"), adv_type_manager=manager, reward_namespace="bacaped_rewards", technical_tabs="technical")
bacaped_hardcore = Datapack(name="bacaped_hardcore", path=Path("test_datapacks/bacaped_hardcore"), adv_type_manager=manager, reward_namespace="bacaped_rewards", technical_tabs="technical")

parser = Parser(bacap, bacaped, bacaped_hardcore)
print(parser.info)
manager = parser.get_datapack("bacap").advancement_manager
adv_with_trophies_data = [adv for adv in manager.deep_find(
    {"trophy": lambda trophy: bool(trophy)})]
print(adv_with_trophies_data)