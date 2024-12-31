from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)  # ISO 3166-1 alpha-2 or alpha-3 codes

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=165)
    code = models.CharField(max_length=8, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    class Meta:
        unique_together = ("name", "country")
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.name}, {self.country}"


class Locality(models.Model):
    name = models.CharField(max_length=165)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="localities")

    class Meta:
        unique_together = ("name", "postal_code", "state")
        verbose_name_plural = "Localities"

    def __str__(self):
        return f"{self.name}, {self.state}"


class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)  # e.g., "123 Main Street"
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)  # e.g., "Apt 4B"
    locality = models.ForeignKey(
        Locality,
        on_delete=models.SET_NULL,
        related_name="addresses",
        blank=True,
        null=True,
    )
    raw = models.TextField(blank=True, null=True)  # Unprocessed input
    formatted = models.TextField(blank=True, null=True)  # Parsed address output
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.formatted or self.raw or "Unnamed Address"
