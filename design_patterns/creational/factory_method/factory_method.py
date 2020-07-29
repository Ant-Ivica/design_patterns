"""
Imagine that we are to refactor the NikeID page and for some reason they decide to use Python and one of its web
frameworks. Let's see how the oversimplified version of that system would look like.
"""
from design_patterns.creational.factory_method.nike_factory import NikeFactory


# initialize NikeFactory instance
shoe_factory = NikeFactory()

# initialize lists that contain shoe orders and completed shoes
shoe_requests = ["90", "95", "97", "720"]
shoes = []


# for every shoe request try to create shoes and add them to the second list
for shoe_request in shoe_requests:

    shoe = shoe_factory.get_shoe(shoe_request)

    if shoe is not None:
        shoes.append(shoe)

# print created shoes details
for shoe in shoes:
    shoe_details = shoe.get_shoe_details()
    shoe_model = shoe_details.get("model")
    shoe_colour_scheme = shoe_details.get("colour_scheme")

    print("{} - Model: {} - Colour Scheme: {}".format(shoe.__class__, shoe_model, shoe_colour_scheme))
