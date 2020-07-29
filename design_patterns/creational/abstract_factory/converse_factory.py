from design_patterns.creational.factory_method.shoes.shoe import Shoe


class Chuck70(Shoe):

    def __init__(self):
        self.model = "Chuck 70 Classic"
        self.body_colour = "white"
        self.midsection_colour = "white"
        self.logo_colour = "blue"
        self.sole_colour = "tan"
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


class ChuckTaylor(Shoe):

    def __init__(self):
        self.model = "Chuck Taylor All Star Classic"
        self.body_colour = "white"
        self.midsection_colour = "white"
        self.logo_colour = "blue"
        self.sole_colour = "tan"
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


class ConverseFactory(object):

    @staticmethod
    def get_shoe(shoe_type: str):
        if shoe_type == "C70":
            return Chuck70()
        elif shoe_type == "CT":
            return ChuckTaylor()

        print("Requested shoe type '{}' is not available yet!".format(shoe_type))
