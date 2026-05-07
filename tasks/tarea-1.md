# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica



   1. El Entorno Virtual (.venv)Problema que resuelve: El conflicto de versiones. Evita que las librerías de un proyecto interfieran con las de otro (Aislamiento).Diferencia de instalación: Al instalar dentro de .venv, las librerías son locales al proyecto. Si se hace de forma global, se ensucia el sistema operativo y se pierde el control sobre qué versión necesita cada aplicación.
   2. Gestión de Dependencias (requirements.txt)Propósito: Es el "manual de instrucciones" del entorno. No pertenece a la máquina personal porque su función es la portabilidad: permite que cualquier desarrollador o servidor recree el entorno exacto usando el comando pip install -r requirements.txt.
   3. El Flujo de Ejecución en FlaskPunto de Entrada (app.py): Es el archivo principal que inicializa el servidor. Al ejecutar python app.py, el programa mapea las URLs a funciones específicas.Mecánica de la Ruta:Ruta (/): La dirección que el usuario escribe en el navegador.Función (inicio()): La lógica de Python que se dispara cuando se accede a esa ruta.Plantilla (templates/index.html): El archivo visual que la función decide enviar como respuesta.
   4. Verificación y DiagnósticoEvidencia de éxito: La terminal debe mostrar la dirección local http://127.0.0.1:5000. Esto indica que el servidor está en modo "escucha".Relación Backend-Frontend: Si al modificar el HTML el navegador cambia, se confirma que el Backend (Flask) está entregando correctamente los recursos actualizados al Frontend (Cliente/Navegador).
   5. Buenas Prácticas y Errores ComunesError 404: Ocurre cuando se solicita una ruta que no ha sido definida en el código Python.Error "Address already in use": Significa que el puerto 5000 está bloqueado por otra ejecución; se debe cerrar el proceso anterior antes de reiniciar.Carpeta .venv: Nunca se comparte ni se sube a repositorios (se incluye en .gitignore), ya que es específica de la arquitectura de cada computadora.


## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
2. Las dependencias se instalaron desde `requirements.txt`.
3. La aplicacion corre en tu maquina y responde en el navegador.
4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
