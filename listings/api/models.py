from django.db import models
from datetime import datetime

class House(models.Model):
    area_unit = models.CharField(max_length=50)
    bedrooms = models.FloatField(null=True)
    bathrooms = models.FloatField(null=True)
    home_size = models.FloatField(null=True)
    home_type = models.CharField(max_length=50)
    last_sold = models.DateField(null=True)
    last_sold_price = models.FloatField(null=True)
    link = models.URLField()
    price = models.FloatField()
    property_size = models.FloatField(null=True)
    rent_price = models.FloatField(null=True)
    rent_zestimate = models.FloatField(null=True)
    rent_zestimate_last_updated = models.DateField(null=True)
    tax_value = models.FloatField()
    tax_year = models.IntegerField()
    year_built = models.IntegerField(null=True)
    zestimate = models.FloatField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address} - ${self.price}"

    def string_price_to_float(self, price_str):
        """
        Convert a string price to a float.
        This function removes any commas and dollar signs from the string.
        Supports formats:
        $715K
        $1.93M
        """
        price_str = price_str.replace('$', '').replace(',', '')
        if 'K' in price_str:
            return float(price_str.replace('K', '')) * 1000
        elif 'M' in price_str:
            return float(price_str.replace('M', '')) * 1000000
        else:
            return float(price_str)

    @staticmethod
    def from_csv_line(line):
        date_format = '%m/%d/%Y'
        house = House()
        house.area_unit = line[0]
        house.bathrooms = None if line[1] == '' else float(line[1])
        house.bedrooms = None if line[2] == '' else float(line[2])
        house.home_size = None if line[3] == '' else float(line[3])
        house.home_type = line[4]
        house.last_sold = None if line[5] == '' else datetime.strptime(line[5], date_format).date()
        house.last_sold_price = None if line[6] == '' else float(line[6])
        house.link = line[7]
        house.price = House.string_price_to_float(house, line[8])
        house.property_size = None if line[9] == '' else float(line[9])
        house.rent_price = None if line[10] == '' else float(line[10])
        house.rent_zestimate = None if line[11] == '' else float(line[11])
        house.rent_zestimate_last_updated = None if line[12] == '' else datetime.strptime(line[12], date_format).date()
        house.tax_value = float(line[13])
        house.tax_year = int(line[14])
        house.year_built = None if line[15] == '' else int(line[15])
        house.zestimate = None if line[16] == '' else float(line[16])
        house.zestimate_last_updated = None if line[17] == '' else datetime.strptime(line[17], date_format).date()
        house.zillow_id = line[18]
        house.address = line[19]
        house.city = line[20]
        house.state = line[21]
        house.zip_code = line[22]
        return house
