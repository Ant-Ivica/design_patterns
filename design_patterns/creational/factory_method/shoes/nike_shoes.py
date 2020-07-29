from design_patterns.creational.factory_method.shoes.shoe import Shoe

"""
This module contains three classes (AirMax90, AirMax95, AirMax97) with default values set in __init__ method, and one
additional method that returns a dictionary with default values. The basis of this approach is to create an interface
that will be the superclass to all classes that will be produced by factory method.
"""


class AirMax90(Shoe):

    def __init__(self):
        self.model = "Air Max 90"
        self.body_colour = "grey"
        self.midsection_colour = "highlighter-yellow"
        self.logo_colour = "grey"
        self.sole_colour = "white"
        self.tongue_colour = "white"

    def get_shoe_details(self):

        return {
            "model": self.model,
            "colour_scheme": {
                "body": self.body_colour,
                "midsection": self.midsection_colour,
                "logo": self.logo_colour,
                "sole": self.sole_colour,
                "tongue": self.tongue_colour
            }
        }


class AirMax95(Shoe):

    def __init__(self):
        self.model = "Air Max 95"
        self.body_colour = "hyper-jade"
        self.midsection_colour = "indigo-burst"
        self.logo_colour = "black"
        self.sole_colour = "black"
        self.tongue_colour = "grey"

    def get_shoe_details(self):
        return {
            "model": self.model,
            "colour_scheme": {
                "body": self.body_colour,
                "midsection": self.midsection_colour,
                "logo": self.logo_colour,
                "sole": self.sole_colour,
                "tongue": self.tongue_colour
            }
        }


class AirMax97(Shoe):

    def __init__(self):
        self.model = "Air Max 97"
        self.body_colour = "anthracite"
        self.midsection_colour = "silver"
        self.logo_colour = "white"
        self.sole_colour = "white"
        self.tongue_colour = "black"

    def get_shoe_details(self):
        return {
            "model": self.model,
            "colour_scheme": {
                "body": self.body_colour,
                "midsection": self.midsection_colour,
                "logo": self.logo_colour,
                "sole": self.sole_colour,
                "tongue": self.tongue_colour
            }
        }
