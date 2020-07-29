from design_patterns.creational.factory_method.shoes.nike_shoes import AirMax90, AirMax95, AirMax97


class NikeFactory(object):

    """
    Class NikeFactory contains only one method which is responsible for creating shoes based on shoe type (or model)
    provided.
    """

    @staticmethod
    def get_shoe(shoe_type: str):
        if shoe_type == "90":
            return AirMax90()
        elif shoe_type == "95":
            return AirMax95()
        elif shoe_type == "97":
            return AirMax97()

        print("Requested shoe type '{}' is not available yet!".format(shoe_type))
