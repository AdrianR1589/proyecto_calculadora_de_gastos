# Proyecto_Calculadora_de_Gastos
Proyecto de una calculadora de gastos que te ayude a clasificar y obtener los gastos que tienes

https://proyectocalculadoradegastos-bof5nvsqw9sarrrea7nsql.streamlit.app/

Lucero de María Zúñiga Andrade

Francisco Nery Sánchez Hernández

Adrian Roberto Zarate Sánchez

Usualmente la gente, gasta, compra, presta su dinero sin conocer si cuenta con el presupuesto suficiente para pagar sus responsabilidades y tener el dinero a gastar. Mucha gente no termina por hacer un registro y conteo de sus gastos debbido a que no tienen tiempo para hacerlo, no terminan tener el interes o piensan que es muy complicado andar llevando un control de gastos.

El objetivo con la que fue hecha este proyecto es que tengan una herramienta que les facilite llevar un registro de sus gastos, sabiendo que tanto gastan y a que categorias es en donde "se les escapa el dinero". Una herramienta que ayude a registrar sus gastos, clasificarlos, calcular el total por clasificacion y visualizarlo de manera mas sencilla en graficas.

Esta calculadora lo que busca es darte una visualizacion de como vas utilizando tu dinero, para que al final si la persona le interesa pueda descargar su registro de los gastos que obtuvo en formato CSV. Que consideramos que es la mejor manera que pueda ocupar debido a que la manera mas ordenada para el registro es por medio de tablas para los datos obtenidos, al igual, si la persona gusta puede seguir el registro de los gastos ya por medio del CSV ya establecido.

# DIVISION DE TRABAJO

Entre los integrantes del equipo se dividio el codigo para la ejecucion del programa, cada uno formó un archivo propio de python que despues se subio a este repositorio que terminó finalizando en otro archivo que conectaba todos los archivos hechos de cada integrante, que era el final y ejecutaba por completo el programa. 

*Adrian* se encargo del codigo para hacer el registro de los datos de los gastos y el codigo para unir y ejecutar los archivos.

*Nery* se encargo del codigo para hacer los calculos de los registros obtenidos para obtener suma, suma por categorias, promedio de los gastos registrados.

*Lucero* se encargo del codigo para ilustrar los registros en tablas de los gastos, la ilustración de los gastos por categorias por medio de grafica circular y el guardado para descargar el registro por CSV.

Se ocupa la version de Python 3.14.7 para la creación de la app.

# INSTRUCCIONES DE INSTALACION Y EJECUCION

Si quieres conocer la aplicacion ya establecida, solamente ingresa al link al inicio y puedes empezar a registrar tus gastos.

Si quieres instalarlo de manera local.
Previamente necesitas tener instalado las aplicaciones de python, Visual Studio Code (u otro programa similar).

Una vez instalado esto, se ingresa al repositorio de GitHub y presionas el boton de "Code" para seleccionar la descarga "Download ZIP" y este descomprimirlo en una carpate de la computadora.

Despues, abres la aplicacion de Visual Studio Code, abres la carpeta donde tengas guardado los archivos descomprimidos y comprueba la version de python instalada y que sea la misma a la mencionada anteriormente. Usando el comando "python --version", para escribir los codigos busca la opcion para abrir una nueva terminal y en ese espacio escribe los codigos.

Ya una vez verificado, instalas primeros los programas requeridos, por medio de la función "python -m pip install -r requirements.txt".

Para finalizar y ejecutar el programa solamente en la misma terminal, escribe la función "python -m streamlit run app.py"

# COMO USARLO
Para hacer el registro dentro de la aplicación.
Fecha: Primero se escoge la fecha la cual tendra el registro,aqui puedes escribirla manualmente empezando por el año, mes y dia; tambien puedes escogerla por medio del calendario y escoger la fecha exacta.

Concepto: Se escribe el concepto por el cual quieres reconocer el gasto.

Categoria: Escoges de una lista desplegable la categoria a la que es acorde el gasto a registrar (Alimentación, Transporte, Entretenimiento, Salud, Servicios, Otros)

Descripción del gasto: Este es de manera opcional, que redacta si necesitas una descripción mas precisa del gasto a tu consideración.

Al finalizar, decides en la tabla de tus gastos ya registrados la opcion de descargar los datos que tengas en formato CSV.

# LIMITACIONES

Como tal es una aplicación que aunque funcione es limitada en las aplicaciones que tiene.

Debes tener cuidado al registrar los gastos debido a que  no se puede editar, ni borrar los datos ya registrados. Solamente dentro del CSV ya guardado.
Permite la exportación de los registros solamente en el CSV, sin embargo, intenta guardar todos los registros necesarios antes de cerrar la pestaña, debido a que el programa no termina por conservar los gastos al cerrar y volver a abrir la pagina.
