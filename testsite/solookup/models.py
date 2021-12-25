# copied over from Scott Craig's work in testsite
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import datetime

# Boat Model
class Boat(models.Model):
    # Options that a boat can have as a model
    # This doesn't change often so can be static
    BOAT_MODEL_OPTIONS = [
        ('1910-Bay', '1910 Bay Max'),
        ('2110-Bay', '2110 Bay Max'),
        ('2110T-Bay', '2110 Bay Max Tunnel'),
        ('2410-Bay', '2410 Bay Max'),
        ('2210-CB', '2210 Carolina Bay'),
        ('2300-CB', '2300 Carolina Bay'),
        ('2500-CB', '2500 Carolina Bay'),
        ('2700-CB', '2700 Carolina Bay'),
        ('180-CC', '180 CC Adventure'),
        ('198-CC', '198 CC Adventure'),
        ('210-CC', '210 CC Adventure'),
        ('220-CC', '220 CC Adventure'),
        ('232-CC', '232 CC Adventure'),
        ('256-CC', '256 CC Adventure'),
        ('272-CC', '272 CC Adventure'),
        ('280-CC', '280 CC Adventure'),
        ('292-CC', '292 CC Adventure'),
        ('320-CC', '320 CC Adventure'),
        ('210-LXF', '210 LXF'),
        ('220-LXF', '220 LXF'),
        ('232-LXF', '232 LXF'),
        ('256-LXF', '256 LXF')
    ]
    # Options that a boat can have as a dealer
    # This doesn't change often so can be static
    DEALER_OPTIONS = [
        ('70-WEST', '70 WEST'),
        ('ADVENTURE','ADVENTURE'),
        ('ANCHORAGE','ANCHORAGE'),
        ('ATLANTIC','ATLANTIC'),
        ('ASHLEYS', 'ASHLEYS'),
        ('BEACH-BLVD','BEACH BLVD'),
        ('BENT','BENT'),
        ('BIG-BOYS','BIG BOYS'),
        ('BLUE-MARLIN', 'BLUE MARLIN'),
        ('BLUE-WATER','BLUE WATER'),
        ('BOAT-CITY','BOAT CITY'),
        ('BOAT-GUY','BOAT GUY'),
        ('BOATING-ATLANTA', 'BOATING ATLANTA'),
        ('BULLOCH','BULLOCH'),
        ('CAPE-ROMAIN','CAPE ROMAIN'),
        ('COASTA-LBOAT','COASTAL BOAT'),
        ('COASTLINE', 'COASTLINE'),
        ('CHALKS','CHALKS'),
        ('DUNCAN','DUNCAN'),
        ('EDS','EDS'),
        ('FOOTHILLS', 'FOOTHILLS'),
        ('FUNNSUN','FUN N SUN'),
        ('GEORGES','GEORGES'),
        ('GREENVILLE','GREENVILLE'),
        ('FAMILYT-BOATING', 'FAMILY BOATING'),
        ('HITCHCOCK','HITCHCOCK'),
        ('JETTS','JETTS'),
        ('JIMS','JIMS'),
        ('LEGACY', 'LEGACY'),
        ('LINCOLNTON','LINCOLNTON'),
        ('LIQUID-PLANET','LIQUID PLANET'),
        ('MARINE-OUTLET','MARINE OUTLET'),
        ('MARINE-SUPPLY','MARINE SUPPLY'),
        ('MARKER17', 'MARKER17'),
        ('MARSHALLS','MARSHALLS'),
        ('MATTHEWS','MATTHEWS'),
        ('MARITIME','MARITIME'),
        ('MIKES', 'MIKES'),
        ('MILLERS','MILLERS'),
        ('MONAHANS','MONAHANS'),
        ('MUSKOKA','MUSKOKA'),
        ('NAUTICAL-VENTURES', 'NAUTICAL VENTURES'),
        ('OCEAN-MARINE','OCEAN MARINE'),
        ('OLSON','OLSON'),
        ('ONEILLS','ONEILLS'),
        ('PELICAN', 'PELICAN'),
        ('PYH','PYH'),
        ('RACETRACK','RACETRACK'),
        ('RIVERFRONT','RIVERFRONT'),
        ('ROSE-MARINA-FL', 'ROSE MARINA FL'),
        ('ROSE-MARINE','ROSE MARINE'),
        ('ROYAL-PALM','ROYAL PALM'),
        ('SAN-CARLOS','SAN CARLOS'),
        ('SEA-HUNTER', 'SEA HUNTER'),
        ('TEXAS','TEXAS'),
        ('TYCOON','TYCOON'),
        ('WILSON','WILSON'),
        ('YANKEE', 'YANKEE'),
        ('OTHER', 'OTHER')
    ]

    # Options that a boat can have as a step
    # This doesn't change often so can be static
    BOAT_STEP_OPTIONS = [
        ('Gel', 'Gel'),
        ('Skin', 'Skin'),
        ('Bulk', 'Bulk'),
        ('Floor', 'Floor'),
        ('Box', 'Box'),
        ('Pull', 'Pull'),
        ('Grind', 'Grind'),
        ('Cut', 'Cut'),
        ('Patch', 'Patch'),
        ('Hardware', 'Hardware'),
        ('Cap', 'Cap'),
        ('Foam', 'Foam'),
        ('Con', 'Con'),
        ('Motor', 'Motor'),
        ('Rig', 'Rig'),
        ('Upholstery', 'Upholstery'),
        ('CC', 'CC'),
        ('Inspection', 'Inspection'),
        ('Shipped', 'Shipped')
    ]

    # Boat Attributes
    so_num = models.IntegerField(primary_key=True, default=211500)
    model = models.CharField(max_length =30, choices=BOAT_MODEL_OPTIONS, default='180-CC')
    color = models.CharField(max_length=10, null=True)
    serial_num = models.CharField(max_length=10, null=True)
    current_step = models.CharField(max_length=12, default="Not Started", choices=BOAT_STEP_OPTIONS)
    dealer_name = models.CharField(max_length =30,null=True, choices=DEALER_OPTIONS, blank=True, default='')
    anticipated_Start = models.DateField(null = True, blank = True)
    motor = models.CharField(max_length =30, null=True, default='')
    

    #boat production steps
    prep = models.DateField(null = True, blank = True)
    gel = models.DateField(null = True, blank = True)
    skin = models.DateField(null = True, blank = True)
    bulk = models.DateField(null = True, blank = True)
    floor = models.DateField(null = True, blank = True)
    box = models.DateField(null = True, blank = True)
    pull = models.DateField(null = True, blank = True)
    grind = models.DateField(null = True, blank = True)
    cut = models.DateField(null = True, blank = True)
    patch = models.DateField(null = True, blank = True)
    hw = models.DateField(null = True, blank = True)
    cap = models.DateField(null = True, blank = True)
    foam = models.DateField(null = True, blank = True)
    con = models.DateField(null = True, blank = True)
    mtr = models.DateField(null = True, blank = True)
    rig = models.DateField(null = True, blank = True)
    uph = models.DateField(null = True, blank = True)
    cc = models.DateField(null = True, blank = True)
    insp = models.DateField(null = True, blank = True)
    ship = models.DateField(null = True, blank = True)


    #current manager update
    #manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return u'/solookup/%d' % (self.so_num)

    # Save Boat Model, update steps
    def save(self, *args, **kwargs):
        self.auto_update_production()
        self.set_current_step()

        super().save(*args,**kwargs)

    #cascading auto update- if a later step has a date, and a previous date is empty, assign dates
    def auto_update_production(self):
        if self.ship != None and self.insp == None:
            self.insp = self.ship
        if self.insp != None and self.cc == None:
            self.cc = self.insp
        if self.cc != None and self.uph == None:
            self.uph = self.cc
        if self.uph != None and self.rig == None:
            self.rig = self.uph
        if self.rig != None and self.mtr == None:
            self.mtr = self.rig
        if self.mtr != None and self.con == None:
            self.con = self.mtr
        if self.con != None and self.foam == None:
            self.foam = self.con
        if self.foam != None and self.cap == None:
            self.cap = self.foam
        if self.cap != None and self.hw == None:
            self.hw = self.cap
        if self.hw != None and self.patch == None:
            self.patch = self.hw
        if self.patch != None and self.cut == None:
            self.cut = self.patch
        if self.cut != None and self.grind == None:
            self.grind = self.cut
        if self.grind != None and self.pull == None:
            self.pull= self.grind
        if self.pull != None and self.box == None:
            self.box = self.pull
        if self.box != None and self.floor == None:
            self.floor = self.box
        if self.floor != None and self.bulk == None:
            self.bulk = self.floor
        if self.bulk != None and self.skin == None:
            self.skin = self.bulk
        if self.skin != None and self.gel== None:
            self.gel = self.skin
        if self.gel != None and self.prep == None:
            self.prep = self.gel

    #working backwards for the setter since last step is current step
    def set_current_step(self):
        if self.ship != None:
            self.current_step = "Shipped"
        elif self.insp != None:
            self.current_step = "Inspection"
        elif self.cc != None:
            self.current_step = "CC"
        elif self.uph != None:
            self.current_step = "Upholstery"
        elif self.rig != None:
            self.current_step = "Rig"
        elif self.mtr != None:
            self.current_step = "Motor"
        elif self.con != None:
            self.current_step = "Con"
        elif self.foam != None:
            self.current_step = "Foam"
        elif self.cap != None:
            self.current_step = "Cap"
        elif self.hw != None:
            self.current_step = "Hardware"
        elif self.patch != None:
            self.current_step = "Patch"
        elif self.cut != None:
            self.current_step = "Cut"
        elif self.grind != None:
            self.current_step = "Grind"
        elif self.pull != None:
            self.current_step = "Pull"
        elif self.box != None:
            self.current_step = "Box"
        elif self.floor != None:
            self.current_step = "Floor"
        elif self.bulk != None:
            self.current_step = "Bulk"
        elif self.skin != None:
            self.current_step = "Skin"
        elif self.gel!= None:
            self.current_step = "Gel"


    # What gets printed when you print a boat model
    def __str__(self):
        return str(self.so_num)

