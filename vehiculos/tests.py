from django.test import TestCase
from django.contrib.auth.models import User
from .models import Vehiculo

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# 🔹 PRUEBAS UNITARIAS DEL MODELO
class VehiculoModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='usuario_test', password='clave123')
        self.vehiculo = Vehiculo.objects.create(
            user=self.user,
            placas='XYZ001',
            lat=19.43,
            lon=-99.13
        )

    def test_creacion_vehiculo(self):
        self.assertEqual(self.vehiculo.placas, 'XYZ001')
        self.assertEqual(self.vehiculo.lat, 19.43)
        self.assertEqual(self.vehiculo.lon, -99.13)
        self.assertEqual(self.vehiculo.user.username, 'usuario_test')

    def test_str_del_vehiculo(self):
        self.assertEqual(str(self.vehiculo), 'XYZ001 (19.43, -99.13)')


# 🔹 PRUEBAS DE LA API REST
class VehiculoAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')

    def test_crear_vehiculo(self):
        url = reverse('vehiculo-list')  # Usar nombre de la ruta desde el router DRF
        data = {
            'user': self.user.id,
            'placas': 'XYZ002',
            'lat': 19.50,
            'lon': -99.20
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['placas'], 'XYZ002')

    def test_listar_vehiculos(self):
        Vehiculo.objects.create(user=self.user, placas='ABC123', lat=1.1, lon=2.2)
        url = reverse('vehiculo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_actualizar_vehiculo(self):
        vehiculo = Vehiculo.objects.create(user=self.user, placas='EDIT001', lat=0, lon=0)
        url = reverse('vehiculo-detail', args=[vehiculo.id])
        data = {
            'user': self.user.id,
            'placas': 'EDIT999',
            'lat': 20.0,
            'lon': -100.0
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['placas'], 'EDIT999')

    def test_eliminar_vehiculo(self):
        vehiculo = Vehiculo.objects.create(user=self.user, placas='DEL123', lat=0, lon=0)
        url = reverse('vehiculo-detail', args=[vehiculo.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vehiculo.objects.count(), 0)