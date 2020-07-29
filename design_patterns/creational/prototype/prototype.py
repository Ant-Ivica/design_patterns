from design_patterns.creational.prototype.asset_registry import AssetRegistry
from design_patterns.creational.prototype.private_asset import PrivateAsset
from design_patterns.creational.prototype.public_asset import PublicAsset

# initialize asset prototypes to be registered
public_asset = PublicAsset()
private_asset = PrivateAsset()

# initialize AssetRegistry object and register created assets
asset_registry = AssetRegistry()
asset_registry.register_asset("public", public_asset)
asset_registry.register_asset("private", private_asset)

# print out current asset details to see the default values in place
print(public_asset.__dict__)
print(private_asset.__dict__)

# create new asset clones with provided values
new_public_asset = asset_registry.clone("public", "ID001", "ID002", "ID003")
new_private_asset = asset_registry.clone("private", "ID004", "ID005", "ID006")

# prints to see that cloning was completed successfully
print(new_public_asset.__dict__)
print(new_private_asset.__dict__)

# run mock processing methods to see that these are actually the right class instances.
new_public_asset.get_financial_details()
new_private_asset.get_financial_details()
