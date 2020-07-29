from design_patterns.creational.abstract_factory.shoe_factory import ShoeFactory


shoe_factory = ShoeFactory()

shoe_requests = [
    {
        "maker": "Nike",
        "model": "90"
    },
    {
        "maker": "Converse",
        "model": "CT"
    },
    {
        "maker": "Adidas",
        "model": "Forum"
    }
]

shoes = []

for shoe_request in shoe_requests:

    shoe = shoe_factory.get_shoe(shoe_request)

    if shoe is not None:
        shoes.append(shoe)

for shoe in shoes:
    shoe_details = shoe.get_shoe_details()
    shoe_model = shoe_details.get("model")
    shoe_colour_scheme = shoe_details.get("colour_scheme")

    print("{} - Model: {} - Colour Scheme: {}".format(shoe.__class__, shoe_model, shoe_colour_scheme))
