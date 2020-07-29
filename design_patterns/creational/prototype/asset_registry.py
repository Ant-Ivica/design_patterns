from copy import deepcopy


class AssetRegistry(object):

    """
    Asset registry class that is responsible for storing and cloning asset blueprints. Class contains only a dictionary
    which can be updated by register and unregister asset methods. It also contains a clone method that will fetch the
    required asset from the dictionary, clone, update and return it as a new object with new values that have been
    provided.
    """

    def __init__(self):
        self.asset_types = {}

    def register_asset(self, asset_type: str, asset):
        self.asset_types.update({asset_type: asset})

    def unregister_asset(self, asset_type: str):
        del self.asset_types[asset_type]

    def clone(self, asset_type: str, id1: str, id2: str, id3: str):
        new_asset_details = {
            "id1": id1,
            "id2": id2,
            "id3": id3
        }

        object_to_clone = self.asset_types.get(asset_type)

        if object_to_clone is None:
            print("Asset of type {} is not in the registry!".format(asset_type))
        else:
            cloned_object = deepcopy(object_to_clone)
            cloned_object.__dict__.update(new_asset_details)
            return cloned_object
