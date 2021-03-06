# Generated by Django 3.1.3 on 2021-03-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solookup', '0017_auto_20210313_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='dealer_name',
            field=models.CharField(blank=True, choices=[('70-WEST', '70 WEST'), ('ADVENTURE', 'ADVENTURE'), ('ANCHORAGE', 'ANCHORAGE'), ('ATLANTIC', 'ATLANTIC'), ('ASHLEYS', 'ASHLEYS'), ('BEACH-BLVD', 'BEACH BLVD'), ('BENT', 'BENT'), ('BIG-BOYS', 'BIG BOYS'), ('BLUE-MARLIN', 'BLUE MARLIN'), ('BLUE-WATER', 'BLUE WATER'), ('BOATC-ITY', 'BOAT CITY'), ('BOAT-GUY', 'BOAT GUY'), ('BOATING-ATLANTA', 'BOATING ATLANTA'), ('BULLOCH', 'BULLOCH'), ('CAPE-ROMAIN', 'CAPE ROMAIN'), ('COASTA-LBOAT', 'COASTAL BOAT'), ('COASTLINE', 'COASTLINE'), ('CHALKS', 'CHALKS'), ('DUNCAN', 'DUNCAN'), ('EDS', 'EDS'), ('FOOTHILLS', 'FOOTHILLS'), ('FUNNSUN', 'FUN N SUN'), ('GEORGES', 'GEORGES'), ('GREENVILLE', 'GREENVILLE'), ('FAMILYT-BOATING', 'FAMILY BOATING'), ('HITCHCOCK', 'HITCHCOCK'), ('JETTS', 'JETTS'), ('JIMS', 'JIMS'), ('LEGACY', 'LEGACY'), ('LINCOLNTON', 'LINCOLNTON'), ('LIQUID-PLANET', 'LIQUID PLANET'), ('MARINE-OUTLET', 'MARINE OUTLET'), ('MARINE-SUPPLY', 'MARINE SUPPLY'), ('MARKER17', 'MARKER17'), ('MARSHALLS', 'MARSHALLS'), ('MATTHEWS', 'MATTHEWS'), ('MARITIME', 'MARITIME'), ('MIKES', 'MIKES'), ('MILLERS', 'MILLERS'), ('MONAHANS', 'MONAHANS'), ('MUSKOKA', 'MUSKOKA'), ('NAUTICAL-VENTURES', 'NAUTICAL VENTURES'), ('OCEAN-MARINE', 'OCEAN MARINE'), ('OLSON', 'OLSON'), ('ONEILLS', 'ONEILLS'), ('PELICAN', 'PELICAN'), ('PYH', 'PYH'), ('RACETRACK', 'RACETRACK'), ('RIVERFRONT', 'RIVERFRONT'), ('ROSE-MARINA-FL', 'ROSE MARINA FL'), ('ROSE-MARINE', 'ROSE MARINE'), ('ROYAL-PALM', 'ROYAL PALM'), ('SAN-CARLOS', 'SAN CARLOS'), ('SEA-HUNTER', 'SEA HUNTER'), ('TEXAS', 'TEXAS'), ('TYCOON', 'TYCOON'), ('WILSON', 'WILSON'), ('YANKEE', 'YANKEE')], default='', max_length=30, null=True),
        ),
    ]
