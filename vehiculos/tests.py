from django.test import TestCase
from django.contrib.auth.models import User
from .models import Vehiculo

class VehiculoTest(TestCase):
    def test_creacion_vehiculo(self):
        user = User.objects.create_user('testuser', 'test@example.com', '12345')
        v = Vehiculo.objects.create(user=user, placas='ABC123', lat=19.4, lon=-99.1)
        self.assertEqual(str(v), 'ABC123 (19.4, -99.1)')
