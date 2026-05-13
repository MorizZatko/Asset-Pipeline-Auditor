"""Module with classes for assets, meshes and textures."""

import pandas as pd
import numpy as np

class Asset:
    """Basic class for all assets.

    Args:
        name (str): name of asset.
        asset_type (str): type of asset.
        version (float): version number.
        size (float): size of asset in MB.
    """

    def __init__(self, name, asset_type, version, size):
        self.name = name
        self.asset_type = asset_type
        self.version = version
        self.size = size
        self.status = "ok"

    def describe_asset(self):
        """Provide a short description of the asset."""
        print(f"{self.name} ({self.asset_type}) V{self.version} {self.size} | {self.status}")

class MeshAsset(Asset):
    """Specialized class for 3D-Object data.

    Args:
        name (str): name of asset.
        asset_type (str): type of asset.
        version (float): version number.
        size (float): size of asset in MB.
        polycount (float): polygon count of asset.
    """

    def __init__(self, name, asset_type, version, size, polycount):
        super().__init__ (name, asset_type, version, size)
        self.polycount = polycount

class TextureAsset(Asset):
    """Specialized class for texture data.

    Args:
        name (str): name of asset.
        asset_type (str): type of asset.
        version (float): version number.
        size (float): size of asset in MB.
        resolution (float): pixel resolution of asset.
    """

    def __init__(self, name, asset_type, version, size, resolution):
        super().__init__ (name, asset_type, version, size)
        self.resolution = resolution

class AssetLibrary:
    """Global class to manage all validated assets."""

    def __init__(self):
        self.assets = []

    def add_asset(self, asset_obj):
        """Add asset objects to asset list."""
        self.assets.append(asset_obj)

    def list_all_assets(self):
        """Start describe_asset methode for every asset."""
        for a in self.assets:
            print(a.describe_asset())

    def run_health_check(self):
        """Scann all assets for outliers and adjust the status."""
        for a in self.assets:
            if a.version < 2.0:
                a.status = "Outdated"
            if a.size > 500:
                a.status = "Too heavy"