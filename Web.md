I. Instrucciones:
Leer detalladamente los reactivos y responder de manera correcta lo solicitado en los
reactivos


1. Dibuje un árbol con la estructura básica de un proyecto y una aplicación de Django

Estructura básica de un proyecto

                django
                ├───manage.py
                └───miproyecto
                        settings.py
                        urls.py
                        wsgi.py
                        __init__.py`

Estructura básica de una aplicación de Django

                django
                ├── miproyecto
                |       __init__.py
                |       settings.py
                |       urls.py
                |       wsgi.py
                ├── manage.py
                └── app
                    ├── migrations
                    |       __init__.py
                    ├── admin.py
                    ├── models.py
                    ├── tests.py
                    └── views.py    
                    ├── __init__.py


2. Mencione tres argumentos que gestiona el comando manage.py
python manage.py runserver
python manage.py startapp nombreapp
python manage.py createsuperuser

3. Explique la diferencia de utilizar urls global y urls local
global son todas las del proyecto
local se generar dentro de la aplicacion

4. Escriba un patrón de url para una vista basada en función
def list(request):
        return render(request, 'Luis/list_view.html', {})

5. Escriba un patrón de url para una vista basada en clase
class DetailView(ListView):
    model = modelo
    template_name = 'Luis/list_view.html'

6. Escriba el comando para hacer un proyecto en Django
django-admin startproject nombreproyecto

7. Escriba el comando para hacer una aplicación en Django
python manage.py startapp nombreapp

8. Mencione para que sirve el archivo Settings.py
Sirve para la configuración del proyecto, contiene toda la configuración que usa Django en el proyecto, nos nuestra las aplicaciones, variables de configuración, base de datos.

9. Escriba el comando para registrar las migraciones de los modelos
python manage.py makemigrations nombreapp

10. Escriba el comando para sincronizar el modelo con el motor de base de datos
python manage.py migrate nombreapp
