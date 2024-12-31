from django.db import models
from django.db.models import ForeignKey
from django.db.models.signals import pre_save
from geopy.geocoders import ArcGIS
from scourgify import normalize_address_record
from .models import Address, Locality, State, Country


class AutoParsedAddressField(ForeignKey):
    """
    A custom AddressField that parses raw addresses and populates fields.
    """

    def __init__(self, geocoder_provider=None, **kwargs):
        """
        Initialize the field with optional custom geocoder provider.
        """
        self.geocoder_provider = geocoder_provider or self.default_geocoder_provider
        kwargs["to"] = "autoparsed_address_field.Address"
        kwargs["on_delete"] = kwargs.get("on_delete", models.CASCADE)
        super().__init__(**kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        """
        Connects the parsing logic to the model class.
        """
        super().contribute_to_class(cls, name, **kwargs)
        pre_save.connect(self.parse_address, sender=cls)

    def parse_address(self, instance, **kwargs):
        """
        Parses the address field of the model instance before saving.
        """
        address_instance = getattr(instance, self.name)
        if isinstance(address_instance, Address) and address_instance.raw:
            try:
                geocoder = self.geocoder_provider()
                geocoder.parse(address_instance)
            except Exception as e:
                print(f"Error parsing address: {e}")

    @staticmethod
    def default_geocoder_provider():
        """
        Returns the default geocoder provider based on settings.
        """
        from django.conf import settings

        provider = getattr(settings, "ADDRESS_GEOCODER_PROVIDER", "scourgify")
        if provider == "arcgis":
            return ArcGISGeocoder
        elif provider == "scourgify":
            return ScourgifyGeocoder
        else:
            raise ValueError(f"Unsupported geocoding provider: {provider}")


class ArcGISGeocoder:
    """
    Handles address parsing with ArcGIS.
    """

    def __init__(self):
        self.geolocator = ArcGIS()

    def parse(self, address_instance):
        result = self.geolocator.geocode(address_instance.raw, exactly_one=True)
        if result:
            address_instance.formatted = result.address
            address_instance.latitude = result.latitude
            address_instance.longitude = result.longitude
            address_instance.save()


class ScourgifyGeocoder:
    """
    Handles address parsing with Scourgify.
    """

    def parse(self, address_instance):
        parsed = normalize_address_record(address_instance.raw)
        if parsed:
            address_instance.street_number = parsed.get("address_line_1", "")
            address_instance.route = parsed.get("address_line_2", "")
            address_instance.locality, _ = Locality.objects.get_or_create(
                name=parsed.get("city", ""),
                postal_code=parsed.get("postal_code", ""),
                state=State.objects.get_or_create(
                    name=parsed.get("state", ""),
                    country=Country.objects.get_or_create(name="USA")[0],
                )[0],
            )
            address_instance.save()
