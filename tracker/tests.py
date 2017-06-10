from django.test import TestCase
from django.test import Client
from tracker.models import Garden, Location, Plant, Planting, Status, Exposure, Soil
from datetime import date

class PlantTestCase(TestCase):
    def setUp(self):
        g = Garden.objects.create(name="Front Yard", description="My front yard")
        st = Status.objects.create(status="live")
        st.save()
        e = Exposure.objects.create(exposure_type="sun")
        e.save()
        s = Soil.objects.create(soil_type="clay")
        s.save()
        l = Location.objects.create(name="south end",
                               description="flower bed", garden=g)
        l.save()
        l.exposure.add(e)
        p = Plant.objects.create(name="Lemon Verbena",
                                sci_name="lem ver",
                                height=26,
                                width=24,
                                color="vibrant green",
                                moisture="even moisture",
                                bloom_season="N/A",
                                food="balanced",
                                notes="Smells awesome")
        p.save()
        p.exposure.add(e)
        p.soil.add(s)
        planting = Planting.objects.create(date=date.today(),
                                          plant=p,
                                          location=l,
                                          status=st,
                                          description="Needs regular pruning")
        planting.save()

    def test_plant_view(self):
        c = Client()
        response = c.get('/tracker/plants/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lemon Verbena", response.content)
