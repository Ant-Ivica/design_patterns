from design_patterns.creational.builder.asset_builder import AssetBuilder


# instantiate AssetBuilder class
asset_builder = AssetBuilder()

# instantiate a list of unique identifiers
unique_ids = ["ID001", "ID002", "ID003"]

# for every id in the list create an asset and print it's contents.
for unique_id in unique_ids:
    asset = asset_builder.get_asset(unique_id)

    print(asset.__dict__, "\n")
