from typing import Dict

from design_patterns.creational.abstract_factory.base_shoe_factory import BaseShoeFactory
from design_patterns.creational.abstract_factory.converse_factory import ConverseFactory
from design_patterns.creational.factory_method.nike_factory import NikeFactory


class ShoeFactory(BaseShoeFactory):

    def __init__(self):
        self.nike_factory = NikeFactory()
        self.converse_factory = ConverseFactory()

    def get_shoe(self, shoe_order: Dict[str, str]):
        shoe_maker = shoe_order.get("maker")
        shoe_model = shoe_order.get("model")

        if shoe_maker == "Nike":
            return self.nike_factory.get_shoe(shoe_model)
        elif shoe_maker == "Converse":
            return self.converse_factory.get_shoe(shoe_model)

        print("Shoe maker {} is not part of the Nike Company.".format(shoe_maker))
