from django.test import Client


c = Client()
response = c.get('/admin/')
response.status_code