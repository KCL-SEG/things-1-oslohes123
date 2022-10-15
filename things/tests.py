from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError
# Create your tests here.
class thingsTest(TestCase):
    def setUp(self):
        self.user = Thing.objects.create(
            name= 'Jane',
            description= 'fjsdfklsdjflsdjf',
            quantity=2,
        )

    def test_valid_input_data(self):
        try:
            self.user.full_clean()
        except ValidationError:
            self.fail("Test user not valid")



