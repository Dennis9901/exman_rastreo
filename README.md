# Examen Rastreo

Instrucciones para correr localmente:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Pruebas CURL:
```bash
# Login, insertar, actualizar, borrar usando cookies o token
curl.exe -c cookies.txt -s http://localhost:8000/accounts/login/ > login.html
Select-String -Path login.html -Pattern 'csrfmiddlewaretoken' | ForEach-Object {
  $_ -match 'value="(.+?)"' | Out-Null
  $GLOBALS:csrfToken = $matches[1]
}
```
```bash
#Login
curl.exe -b cookies.txt -c cookies.txt -X POST http://localhost:8000/accounts/login/ `
  -H "Content-Type: application/x-www-form-urlencoded" `
  -H "Referer: http://localhost:8000/accounts/login/" `
  -d "username=admin&password=admin123&csrfmiddlewaretoken=$csrfToken"
```
```bash


# Crear objetos
@'
{ "placas": "XYZ001", "lat": 19.43, "lon": -99.13 }
'@ | Out-File -Encoding ASCII data1.json

@'
{ "placas": "XYZ002", "lat": 19.44, "lon": -99.14 }
'@ | Out-File -Encoding ASCII data2.json

@'
{ "placas": "XYZ003", "lat": 19.45, "lon": -99.15 }
'@ | Out-File -Encoding ASCII data3.json
```
```bash

#Ejecutar Curls
curl.exe -b cookies.txt -X POST http://localhost:8000/api/vehiculos/ `
  -H "Content-Type: application/json" `
  -H "X-CSRFToken: $csrfToken" `
  -H "Referer: http://localhost:8000/api/vehiculos/" `
  --data "@data1.json"

curl.exe -b cookies.txt -X POST http://localhost:8000/api/vehiculos/ `
  -H "Content-Type: application/json" `
  -H "X-CSRFToken: $csrfToken" `
  -H "Referer: http://localhost:8000/api/vehiculos/" `
  --data "@data2.json"

curl.exe -b cookies.txt -X POST http://localhost:8000/api/vehiculos/ `
  -H "Content-Type: application/json" `
  -H "X-CSRFToken: $csrfToken" `
  -H "Referer: http://localhost:8000/api/vehiculos/" `
  --data "@data3.json"


```

Pruebas Editado:
```bash
#Actualizar segun el id y los datos a cambiar
@'
{ "placas": "XYZ999", "lat": 20.00, "lon": -100.00 }
'@ | Out-File -Encoding ASCII update.json

curl.exe -b cookies.txt -X PUT http://localhost:8000/api/vehiculos/id/ `
    -H "Content-Type: application/json" `
    -H "X-CSRFToken: $csrfToken" `
    -H "Referer: http://localhost:8000/api/vehiculos/id/" `
    --data "@update.json"


```


Pruebas Editado:
```bash

curl.exe -b cookies.txt -X DELETE http://localhost:8000/api/vehiculos/id/ `
    -H "X-CSRFToken: $csrfToken" `
    -H "Referer: http://localhost:8000/api/vehiculos/id/"

```
