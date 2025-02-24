from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class FileUploaderTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')  


    def test_valid_file_upload(self):
        # Archivo válido
        file_content = b"12345,test@example.com,CC,750000,valor5\n67890,user@domain.com,TI,1000000,valor5"
        uploaded_file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")

        # solicitud POST con el archivo
        response = self.client.post(self.url, {'file': uploaded_file})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "✅El archivo cumple con todas las validaciones.")


    def test_invalid_file_upload(self):
        # Archivo inválido 
        file_content = b"12,invalid-email,XX,2000000,valor5"
        uploaded_file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")

        # solicitud POST con el archivo
        response = self.client.post(self.url, {'file': uploaded_file})
       
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Columna 1: Debe ser un número entero de 3 a 10 caracteres.")
        #self.assertContains(response, "Columna 3: Solo se permiten los valores 'CC' o 'TI'.")
        self.assertContains(response, "Columna 4: El valor debe estar entre 500000 y 1500000.")


def test_empty_file_upload(self):
    # Archivo vacío
    file_content = b""
    uploaded_file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")

    # Hacer una solicitud POST con el archivo
    response = self.client.post(self.url, {'file': uploaded_file})

    # Verificar que la respuesta contiene errores
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "El archivo debe tener 5 columnas")


    def test_no_file_upload(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "✅El archivo cumple con todas las validaciones.")


