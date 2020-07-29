import names
from faker import Faker
from random import randint

from design_patterns.creational.builder.asset import Asset

faker = Faker()


class AssetBuilder(object):

    """
    Class AssetBuilder that is responsible for building new instances of Asset class with all proper members set. It
    contains get_asset method, which, based on the unique identifier provided creates and fills Asset class instance
    with proper values. It also contains 4 protected supporting methods to provide logs and mocked data to be set as
    asset member values.
    """

    def get_asset(self, unique_identifier):
        asset = Asset()

        asset_name = self._get_asset_name(unique_identifier)
        asset.set_name(asset_name)

        asset_country = self._get_asset_country(unique_identifier)
        asset.set_country(asset_country)

        asset_revenue = self._get_asset_revenue(unique_identifier)
        asset.set_revenue(asset_revenue)

        asset_cogs = self._get_asset_cogs(unique_identifier)
        asset.set_cogs(asset_cogs)

        return asset

    def _get_asset_name(self, unique_identifier):
        print("Querying asset's proper name by unique identifier {}".format(unique_identifier))
        return names.get_full_name()

    def _get_asset_country(self, unique_identifier):
        print("Querying asset's country of origin by unique identifier {}".format(unique_identifier))
        return faker.country()

    def _get_asset_revenue(self, unique_identifier):
        print("Querying asset's revenue by unique identifier {}.".format(unique_identifier))
        print("Converting asset's revenue to USD.")
        return round(randint(12000, 34000) / 17, 2)

    def _get_asset_cogs(self, unique_identifier):
        print("Querying asset's cost of goods sold by unique identifier {}.".format(unique_identifier))
        print("Converting asset's revenue to USD.")
        return round(randint(12000, 34000) / 13, 2)
