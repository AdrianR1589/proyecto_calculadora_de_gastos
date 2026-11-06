# Proyecto_Calculadora_de_Gastos
Proyecto de una calculadora de gastos que te ayude a clasificar y obtener los gastos que tienes

https://proyectocalculadoradegastos-bof5nvsqw9sarrrea7nsql.streamlit.app/

Lucero de María Zúñiga Andrade

Francisco Nery Sánchez Hernández

Adrian Roberto Zarate Sánchez

Usualmente la gente, gasta, compra, presta su dinero sin conocer si cuenta con el presupuesto suficiente para pagar sus responsabilidades y tener el dinero a gastar. Mucha gente no termina por hacer un registro y conteo de sus gastos debido a que no tienen tiempo para hacerlo, no terminan tener el interés o piensan que es muy complicado andar llevando un control de gastos.

El objetivo con la que fue hecha este proyecto es que tengan una herramienta que les facilite llevar un registro de sus gastos, sabiendo que tanto gastan y a que categorías es en donde "se les escapa el dinero". Una herramienta que ayude a registrar sus gastos, clasificarlos, calcular el total por clasificación y visualizarlo de manera más sencilla en graficas.

Esta calculadora lo que busca es darte una visualización de cómo vas utilizando tu dinero, para que al final si la persona le interesa pueda descargar su registro de los gastos que obtuvo en formato CSV. Que consideramos que es la mejor manera que pueda ocupar debido a que la manera más ordenada para el registro es por medio de tablas para los datos obtenidos, al igual, si la persona gusta puede seguir el registro de los gastos ya por medio del CSV ya establecido.

# DIVISION DE TRABAJO

Entre los integrantes del equipo se dividió el código para la ejecución del programa, cada uno formó un archivo propio de Python que después se subió a este repositorio que terminó finalizando en otro archivo que conectaba todos los archivos hechos de cada integrante, que era el final y ejecutaba por completo el programa. 

*Adrian* se encargó del código para hacer el registro de los datos de los gastos y el código para unir y ejecutar los archivos.

*Nery* se encargó del código para hacer los cálculos de los registros obtenidos para obtener suma, suma por categorías, promedio de los gastos registrados.

*Lucero* se encargó del código para ilustrar los registros en tablas de los gastos, la ilustración de los gastos por categorías por medio de grafica circular y el guardado para descargar el registro por CSV.

Se ocupa la versión de Python 3.14.7 para la creación de la aplicación.

# INSTRUCCIONES DE INSTALACION Y EJECUCION

Si quieres conocer la aplicación ya establecida, solamente ingresa al enlace al inicio y puedes empezar a registrar tus gastos.

Si quieres instalarlo de manera local.
Previamente necesitas tener instalado las aplicaciones de Python, Visual Studio Code (u otro programa similar).

Una vez instalado esto, se ingresa al repositorio de GitHub y presionas el botón de "Code" para seleccionar la descarga "Download ZIP" y este descomprimirlo en una carpeta de la computadora.

Después, abres la aplicación de Visual Studio Code, abres la carpeta donde tengas guardado los archivos descomprimidos y comprueba la versión de Python instalada y que sea la misma a la mencionada anteriormente. Usando el comando "Python --versión", para escribir los códigos busca la opción para abrir una nueva terminal y en ese espacio escribe los códigos.

Ya una vez verificado, instalas primero las dependencias requeridas, por medio de la función "Python -m pip install -r requirements.txt".

Para finalizar y ejecutar el programa solamente en la misma terminal, escribe la función "Python -m streamlit run app.py"

# COMO USARLO
Para hacer el registro dentro de la aplicación.
Fecha: Primero se escoge la fecha la cual tendrá el registro, aquí puedes escribirla manualmente empezando por el año, mes y día; tambien puedes escogerla por medio del calendario y escoger la fecha exacta.

Concepto: Se escribe el concepto por el cual quieres reconocer el gasto.

Categoría: Escoges de una lista desplegable la categoría a la que es acorde el gasto a registrar (Alimentación, Transporte, Entretenimiento, Salud, Servicios, Otros)

Descripción del gasto: Este es de manera opcional, que redacta si necesitas una descripción más precisa del gasto a tu consideración.

Al finalizar, decides en la tabla de tus gastos ya registrados la opción de descargar los datos que tengas en formato CSV.

# LIMITACIONES

Como tal es una aplicación que, aunque funcione es limitada en las aplicaciones que tiene.

Debes tener cuidado al registrar los gastos debido a que no se puede editar, ni borrar los datos ya registrados. Solamente dentro del CSV ya guardado.
Permite la exportación de los registros solamente en el CSV, sin embargo, intenta guardar todos los registros necesarios antes de cerrar la pestaña, debido a que el programa no termina por conservar los gastos al cerrar y volver a abrir la página.

# CONCLUSIONES

Consideramos que la aplicación funciona para cumplir con la necesidad básica con la que fue basada, pero aun es una aplicación que se puede mejorar a una mejor de registro, mejores formas de dar y visualizar el resultado.
Sin embargo, creemos que nuestra calculadora puede funcionar a toda esta gente debido a que es sencilla de utilizar, permite registrar y clasificar sus gastos, muestra visualmente sus gastos. Es una herramienta que puede funcionar para control básico de sus gastos personales, como un servicio para pequeños negocios y cuidar esos gastos cotidianos que no se terminan por contabilizar y principalmente como un apoyo para los estudiantes y personas interesadas a identificar sus hábitos de consumo y cuidar mejor su presupuesto.
