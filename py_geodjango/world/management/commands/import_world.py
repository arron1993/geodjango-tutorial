
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource

from django.contrib.gis.utils import LayerMapping

from world.models import WorldBorder


class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        world_shp = Path(__file__).resolve().parent.parent.parent / "data" / "TM_WORLD_BORDERS-0.3.shp"
        world_mapping = {
            "fips": "FIPS",
            "iso2": "ISO2",
            "iso3": "ISO3",
            "un": "UN",
            "name": "NAME",
            "area": "AREA",
            "pop2005": "POP2005",
            "region": "REGION",
            "subregion": "SUBREGION",
            "lon": "LON",
            "lat": "LAT",
            "mpoly": "MULTIPOLYGON",
        }
        lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
        lm.save(strict=True, verbose=True)

