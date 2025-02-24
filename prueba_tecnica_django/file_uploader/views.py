from django.shortcuts import render

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
import re

def index(request):
    if request.method == 'POST':

        if 'file' not in request.FILES:  
            return render(request, 'file_uploader/index.html', {'errors': ["No se ha subido ningún archivo."]})
         
        # Procesar el archivo
        file = request.FILES['file']
        file_name = default_storage.save(file.name, ContentFile(file.read()))
        file_path = default_storage.path(file_name)


        with open(file_path, 'r') as f:
            content = f.read()
            rows = content.split('\n')  
            data = [row.split(',') for row in rows if row]  

        
        for row in data:
            print(row)


        errors = []

        for i, row in enumerate(data, start=1):           

            # Validación:  El archivo solo debe permitir 5 columnas
            if len(row) != 5:
                errors.append(f"El archivo debe tener 5 columnas")
                continue

            # Validación: Columna 1 solo números enteros entre 3 y 10 caracteres
            col1 = row[0].strip()
            if not col1.isdigit() or len(col1) < 3 or len(col1) > 10:
                errors.append(f"Columna 1: Debe ser un número entero de 3 a 10 caracteres.")

            # Validación: Columna 2 solo correos electrónicos válidos
            col2 = row[1].strip()
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', col2):
                errors.append(f"Columna 2: Debe ser un correo electrónico válido.")
            
            # Validación: Columna 3 solo permite los valores "CC" o "TI"
            col3 = row[2].strip()
            if col3 not in ["CC", "TI"]:
                errors.append(f"Columna 3: Solo se permiten los valores 'CC' o 'TI'.")


            # Validación: Columna 4 solo permite valores entre 500000 y 1500000
            col4 = row[3].strip()
            try:
                col4_value = int(col4)  
                if col4_value < 500000 or col4_value > 1500000:                  
                    errors.append(f"Columna 4: El valor debe estar entre 500000 y 1500000.")
            except ValueError:
                errors.append(f"Columna 4: El valor debe ser un número.")
        

            # Validación: Columna 5 permite cualquier valor (al permitir cualquier valor, no lo valide)
                


        default_storage.delete(file_name)

        if errors:
            return render(request, 'file_uploader/index.html', {'errors': errors})
        else:
            return render(request, 'file_uploader/index.html', {'success': "✅El archivo cumple con todas las validaciones."})

    return render(request, 'file_uploader/index.html')
