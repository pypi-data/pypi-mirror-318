from dataclasses import dataclass
from random import random
from enum import Enum
import openfoodfacts
from requests import ConnectionError


class AbstractSDK:
    @property
    def product(self):
        raise NotImplementedError()


@dataclass(frozen=True)
class Product:
    name: str
    energy: str
    protein: str
    fiber: str
    fat: str
    nutriscore: str


class SDKVersion(Enum):
    v1 = "v1"


class SDKBuilder:
    def build(version: SDKVersion) -> AbstractSDK:
        return SDKV1()


class ProductOperationV1:
    def get(barcode: str) -> Product:
        api = openfoodfacts.API(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            version=openfoodfacts.APIVersion.v3,
            timeout=100,
        )
        # raise Exception(api.product.text_search("nutella"))
        json_info = api.product.get("3017620422003")

        name = json_info["abbreviated_product_name"]
        energy = str(json_info["nutriments"]["energy-kcal_100g"] * 0.001)
        protein = str(json_info["nutriments"]["proteins_100g"] * 0.001)
        fiber = str(json_info["nutriments"].get("fiber_100g", "-") * 0.001)
        fat = str(json_info["nutriments"]["fat_100g"] * 0.001)
        nutriscore = json_info["nutriments"]["nutriscore"]["2023"]["grade"]
        return Product(name, energy, protein, fiber, fat, nutriscore)


class SDKV1:
    @property
    def product(self):
        return ProductOperationV1()


class ProductOperationV2:
    def get(barcode: str) -> Product:
        api = openfoodfacts.API(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            version=openfoodfacts.APIVersion.v3,
            timeout=100,
        )
        # raise Exception(api.product.text_search("nutella"))
        json_info = api.product.get("3017620422003")

        name = json_info["abbreviated_product_name"]
        energy = json_info["nutriments"]["energy-kcal_100g"] * 0.001
        protein = json_info["nutriments"]["proteins_100g"] * 0.001
        fiber = json_info["nutriments"].get("fiber_100g", "-") * 0.001
        fat = json_info["nutriments"]["fat_100g"] * 0.001
        nutriscore = json_info["nutriments"]["nutriscore"]["2023"]["grade"]
        return Product(name, energy, protein, fiber, fat, nutriscore)


class SDKV2:
    @property
    def product(self):
        return ProductOperationV2()


class ProductOperationV3:
    def get(barcode: str) -> Product:
        api = openfoodfacts.API(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            version=openfoodfacts.APIVersion.v3,
            timeout=100,
        )
        json_info = api.product.get("3017620422003")

        name = json_info["abbreviated_product_name"]
        energy = json_info["nutriments"]["energy-kcal_100g"]
        protein = json_info["nutriments"]["proteins_100g"]
        fiber = json_info["nutriments"].get("fiber_100g", "-")
        fat = json_info["nutriments"]["fat_100g"]
        nutriscore = json_info["nutriments"]["nutriscore"]["2023"]["grade"]
        return Product(name, energy, protein, fiber, fat, nutriscore)


class SDKV3:
    @property
    def product(self):
        return ProductOperationV3()


class ProductOperationV5:
    def get(barcode: str, timeout: int = 5) -> Product:
        api = openfoodfacts.API(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            version=openfoodfacts.APIVersion.v3,
            timeout=timeout,
        )
        # raise Exception(api.product.text_search("nutella"))
        json_info = api.product.get("3017620422003")

        name = json_info["abbreviated_product_name"]
        energy = json_info["nutriments"]["energy-kcal_100g"]
        protein = json_info["nutriments"]["proteins_100g"]
        fiber = json_info["nutriments"].get("fiber_100g", "-")
        fat = json_info["nutriments"]["fat_100g"]
        nutriscore = json_info["nutriments"]["nutriscore"]["2023"]["grade"]
        return Product(name, energy, protein, fiber, fat, nutriscore)


class SDKV5:
    @property
    def product(self):
        return ProductOperationV5()


class ProductOperationV6:
    def get(barcode: str, timeout: int = 5) -> Product:
        if random() < 0.2:
            raise ConnectionError("Error when trying to reach hose")

        api = openfoodfacts.API(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            version=openfoodfacts.APIVersion.v3,
            timeout=timeout,
        )
        # raise Exception(api.product.text_search("nutella"))
        json_info = api.product.get("3017620422003")

        name = json_info["abbreviated_product_name"]
        energy = json_info["nutriments"]["energy-kcal_100g"]
        protein = json_info["nutriments"]["proteins_100g"]
        fiber = json_info["nutriments"].get("fiber_100g", "-")
        fat = json_info["nutriments"]["fat_100g"]
        nutriscore = json_info["nutriments"]["nutriscore"]["2023"]["grade"]
        return Product(name, energy, protein, fiber, fat, nutriscore)


class SDKV6:
    @property
    def product(self):
        return ProductOperationV6()
