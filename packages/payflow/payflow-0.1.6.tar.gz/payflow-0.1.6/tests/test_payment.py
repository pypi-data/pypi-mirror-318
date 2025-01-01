# -#- coding: utf-8 -#-
from payflow.client import Client
import unittest
import os


class TestPayment(unittest.TestCase):
    """
    Test Hacer Pago a entorno Pruebas
    """
    def test_make_payment(self):
        api_key = os.getenv('FLOW_API_KEY')
        api_secret = os.getenv('FLOW_API_SECRET')

        # Verificar que las variables de entorno existan
        self.assertIsNotNone(api_key, "FLOW_API_KEY no está configurada en las variables de entorno")
        self.assertIsNotNone(api_secret, "FLOW_API_SECRET no está configurada en las variables de entorno")

        client = Client(
            api_key,
            api_secret,
            'https://sandbox.flow.cl/api',
            True,
        )
        payment = {
            'commerceOrder': 'SO1',
            'subject': 'Orden SO1',
            'email': 'dansanti@gmail.com',
            'paymentMethod': "1",
            'urlConfirmation': 'https://gitlab-test.cl/payment/flow/notify',
            'urlReturn': 'https://gitlab-test.cl/payment/flow/return',
            'currency': "CLP",
            'amount': "1000",
            }
        res = client.payments.post(payment)
        print (res)
        self.assertIsNotNone(res, "La respuesta del pago es None")


if __name__ == '__main__':
    unittest.main()
