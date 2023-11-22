#BAPB
import smtplib

correo_escritor = ''
correo_receptor = ''
mensaje = 'Subject: Prueba de Envio (Script python)-Envio de Correos \n\nBAPB\n\n'

# Estableciendo conexiión
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()


# Sacando la contraseña de un archivo password.txt
try:
    with open('password.txt', 'r') as archivo:
        # Lee todas las líneas del archivo en una lista
        lineas = archivo.readlines()
        
        # Verifica si hay al menos dos líneas en el archivo
        if len(lineas) >= 2:
            # Extrae la segunda línea y elimina los espacios en blanco al principio y al final
            password = lineas[1].strip()
        else:
            print("El archivo no tiene la constraseña")
except FileNotFoundError:
    print("El archivo 'password.txt' no fue encontrado.")
except Exception as e:
    print("Ocurrió un error:", e)



# Iniciando sesión y enviando el mensaje

try:
    conn.login(correo_escritor, password)
    conn.sendmail(correo_escritor, correo_receptor, mensaje)
    print("Correo enviado exitosamente.")

except smtplib.SMTPAuthenticationError:
    print("Error de autenticación: La contraseña es incorrecta.")
except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrando la conexión
    conn.quit()