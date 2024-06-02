import unittest
from unittest.mock import MagicMock, patch
import numpy as np
import sys
from io import StringIO
from models import CustomerClassifier  # Asegúrate de importar la clase correctamente

class TestCustomerClassifier(unittest.TestCase):
    @patch('models.load_model')
    def setUp(self, mock_load_model):
        # Crear un mock para el modelo de Keras
        self.mock_model = MagicMock()
        mock_load_model.return_value = self.mock_model

        # Crear una instancia de CustomerClassifier con el modelo simulado
        self.classifier = CustomerClassifier('fake_model_path')

    def test_predict_class(self):
        # Configurar el mock para el método predict
        self.mock_model.predict.return_value = np.array([[0.25, 0.5, 0.25]])

        # Simular un cliente de prueba
        test_client = [0.4, 0.4, 0.2]

        # Redirigir la salida estándar
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llamar al método predict_class
        self.classifier.predict_class(test_client)
        
        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__
        
        print('')
        print(captured_output.getvalue())

        # Verificar que la salida sea la esperada
        self.assertIn('El cliente pertenece a la clase: medium', captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
