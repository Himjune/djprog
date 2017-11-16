from django.test import TestCase
from django.test import Client

from django.test import TestCase

class Test(TestCase):
    def test_sum1(self):
        c = Client()
        response = c.get('/sum/?a=1&b=2')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.content, b'sum=3')
        self.assertEqual(response.status_code, 200)


    def test_sum2(self):
        c = Client()
        response = c.get('/sum/?a=1&b=2&a=3&c=5')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.content, b'sum=11')
        self.assertEqual(response.status_code, 200)

    def test_sum_error(self):
        c = Client()
        response = c.get('/sum/?a=2&b=rgreg')
        self.assertEqual(response.content, b'error, b = rgreg is not a number')
        self.assertEqual(response.status_code, 400)
        print(response.content)
        print(response.status_code)

    def test_mul1(self):
        c = Client()
        response = c.get('/mul/?a=1&b=2')
        self.assertEqual(response.content, b'mult=2')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        print(response.status_code)

    def test_mul2(self):
        c = Client()
        response = c.get('/mul/?a=1&b=2&a=3&c=5')
        self.assertEqual(response.content, b'mult=30')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        print(response.status_code)

    def test_mul_error(self):
        c = Client()
        response = c.get('/mul/?a=2&b=rgreg')
        self.assertEqual(response.content, b'error, b = rgreg is not a number')
        self.assertEqual(response.status_code, 400)
        print(response.content)
        print(response.status_code)

    def test_pow1(self):
        c = Client()
        response = c.get('/pow/?a=4&b=2')
        self.assertEqual(response.content, b'pow=16')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        print(response.status_code)

    def test_pow1_error(self):
        c = Client()
        response = c.get('/pow/?a=1&b=2&a=3&c=5')
        self.assertEqual(response.content, b'error, power accept 2 parameters')
        self.assertEqual(response.status_code, 400)
        print(response.content)
        print(response.status_code)

    def test_pow2_error(self):
        c = Client()
        response = c.get('/pow/?a=2&b=rgreg')
        self.assertEqual(response.content, b'error, one parameter is nan')
        self.assertEqual(response.status_code, 400)
        print(response.content)
        print(response.status_code)




# Create your tests here.
