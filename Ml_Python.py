import subprocess
import re
import webbrowser

# Definir variables de Mercado Libre
APP_ID_TEST = "6495744218630885"
REDIRECT_URI_TEST = "http://localhost:8081/custom/mercadolibre/mercadolibreindex.php"
SERVER_GENERATED_AUTHORIZATION_CODE="TG-651d8bbed634ab00017909cf-187197360"
SECRET_KEY_TEST="AmOBuXOlfXAJOpFBpyisx2AflaPNcGB1"
ACCESS_TOKEN="APP_USR-6495744218630885-100411-345aa84e67b38757cfab68389cc6ddff-187197360"
REFRESH_TOKEN="TG-651d8b053f40a50001cc1aac-187197360"
USER_ID="187197360"


# Construir la URL de Mercado Libre para obtener el código de autorización
url = f'https://auth.mercadolibre.cl/authorization?response_type=code&client_id={APP_ID_TEST}&redirect_uri={REDIRECT_URI_TEST}'

# Hacer el curl para obtener el token
curl_command = f'curl "{url}"'

# Ejecutar el comando curl desde Python
def autentitication():
    try:
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # La solicitud fue exitosa, puedes imprimir la respuesta
            #obtener la url de la respuesta
            url = result.stdout
            match = re.search(r'Redirecting to (https://[^ ]+)', url)
            print(match.group(1))
            # abri la url en el navegador
            webbrowser.open(match.group(1))
        else:
            # Hubo un error en la ejecución del comando curl
            print("Error en la solicitud:")
            print(result.stderr)
    except Exception as e:
        print(f"Error en la ejecución del comando curl: {str(e)}")

def obtenerToken():
    try: 
        # definir curl 
        curl_command = f'curl -X POST \
        -H "accept: application/json" \
        -H "content-type: application/x-www-form-urlencoded" \
        "https://api.mercadolibre.com/oauth/token" \
        -d "grant_type=authorization_code" \
        -d "client_id={APP_ID_TEST}" \
        -d "client_secret={SECRET_KEY_TEST}" \
        -d "code={SERVER_GENERATED_AUTHORIZATION_CODE}" \
        -d "redirect_uri={REDIRECT_URI_TEST}"'
        print (curl_command)
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("Error en la solicitud:")
            print(result.stderr)
    except Exception as e:
        print(f"Error en la ejecución del comando curl: {str(e)}")
    
# Ejecutar la función
while True:
    print("1. Autenticar")
    print("2. Obtener Token")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        autentitication()
    elif opcion == "2":
        obtenerToken()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")