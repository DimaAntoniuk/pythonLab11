from models.Exhibit import Exhibit
from models.InterestedPeople import InterestedPeople
from models.Date import Date
from models.Topic import Topic
from models.Style import Style

class Painting(Exhibit):

    def __init__(self, name="some_exhibit", portable=True,
            century_of_creation=0, country_of_creation="Italy",
            size=3, popularity=InterestedPeople.TWO,
            theme=Topic.ANCIENT_ROME, destroyed_in_persentage=20,
            start_date_in_current_exhibition = Date(3, 1, 2007),
            painting_style=Style.ABSTRACT_ART, frame=True):
        super().__init__(name, portable, century_of_creation,
            country_of_creation, size, popularity, theme,
            destroyed_in_persentage, start_date_in_current_exhibition)
        self.painting_style = painting_style
        self.frame = frame

    def __str__(self):
        return "Painting " + str(self.__dict__)
