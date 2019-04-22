from models.Exhibit import Exhibit
from models.Armor import Armor
from models.Vase import Vase
from models.Crown import Crown
from models.Painting import Painting
from models.Topic import Topic
from managers.ExhibitManager import ExhibitManager


Armor = Armor()
Vase = Vase()
Crown = Crown()
Painting = Painting()

list_of_exhibits = [Painting, Vase, Crown, Armor]
manager = ExhibitManager(list_of_exhibits)

manager.find_by_theme(Topic.ANCIENT_ROME)
manager.print_exhibit_list_info()
manager.sort_by_age(list_of_exhibits)
manager.print_exhibit_list_info()
manager.sort_by_date_in_current_exhibition(list_of_exhibits)
manager.print_exhibit_list_info()
