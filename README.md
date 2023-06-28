
# SDV

<b> Imagen de la caja </b> 
 

# INTEGRANTES
<p>Santiago Quevedo Lopez</p>
<p>Juan Nicolas Torres Escobar</p>
<p>Juan Carlos Oliveros Garzón</p>

# DESCRIPCION DEL PROYECTO

<p>SDV es un dispositivo con el objetivo de defender objetos de valor que contenga dentro al detectar a alguien dentro de un rango disparando en este caso balas Nerf</p>

<h3>PROBLEMATICA</h3>
<p>SDV nace como la respuesta a la problematica de defender objetos de valor como por ejemplo en cajas de seguridad donde la unica barrera que progetee a los obetos de valor es una barrera que muchas veces puede ser trasnpasada con facilidad</p>

<h3>ALCANCES</h3>
<p>Se esperea obtener una caja autodefendible cuando detecte aglo dentro de su rango de alcance</p>

<h3>OBJETIVOS</h3>
<ul>
<li>Hacer una caja que pueda disparar cuando detecte algo dentro de un rango propuesto dispare</li>
<li>Poder cambiar el rango de que tiene la caja para poder detectar una amenaza</li>
<li>Lanzar un sonido de advertencia cuando haya un objetivo en el rango propuesto</li>
<li>Prender leds parpadeantes cuando haya un objetivo dentro del rango propuesto</li>
</ul>

# DIAGRAMAS

<p>En este apartado de diagramas encontraremos el rpoceso grafico por el cual llevaremos a cabo nuestro objetivos propuesto</p>

<h3>DIAGRAMA DE FLUJO</h3>
<p>En este apartado encontraremos el proceso por el cual se lleva a cabo una accion, los procesos a los cuales llevara cabo esa accion y los resultados finales de esa accion</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/874d6cea-2944-442f-9cdf-c7139dc15ca6) 

<h3>DIAGRAMA DE CAJA NEGRA SIN TECNOLOGIA DEFINIDA</h3>
<p>En este apartado encontraremos encontraremos los pprocesos de entrada ysalida con tecnologia ya aplicadpero sin especificar claramente cual es la que vamos a utilizar ya que se tiene que evaluar la caracteristica de cada componente para poder llevar a cabo los objetivos propuestos</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/b9d4f565-b937-4c56-abac-af00bf8cc043)

<h4>LISTA DE MATERIALES</h4>

<p>En este apartado encontraremos los materiales que usaremos parar completar el diagrama de caja negra y como se conectaran los diferentes componentes</p>

<p>Motores DC x2</p>
<p>Servomotor x1</p>
<p>Sensor ultrasonico x1</p>
<p>ESP 32 CAM x1</p>
<p>Leds x6</p>
<p>Buzzer x1</p>

<h3>DIAGRAMA DE CAJA NEGRA CON TECNOLOGIA DEFINIDA</h3>
<p>En este apartado encontraremos los procesos integrados en el diagrama anterior con los materiales seleccionados y como estos se llevarian a cabo</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/e45863e3-b1d2-4eab-8515-a7d002a74404)

# DISEÑOS


<p>1)En este primer diseño podremos apreciar como cada componente consume energia y asi poder calcular cuanta potencia requiere en total el circuito para poder funcionar</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/009ad30d-5c0c-4a15-a059-9555bed91aea)

<p>2)En este segundo diseño encontraremos la cantidad de pines que requeria cada componente para poder funcionar, esto con la finalidad de evaluar si teniamos la placa de programacion que necesitabamos</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/4530e9ac-82c7-4213-983d-6a4c6d52a958)

# IMPLEMENTACION

<p>En esta seccion veremos como implementamos los componenetes para que cumplan la funcion designada</p>

<h3>ESQUEMATICO DEL CIRCUITO</h3>

<p>Este es el esquema circuital del  proyecto</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/bbc27289-119c-4422-b20b-e6f50a4d8289)

<h3>RUTEO PCB</h3>
<p>En esta parte podremos apreciar como se ruteo la PCB y como se dispusieron los diferentes elementos</p>

![image](https://github.com/JOUNAL/SDV/assets/136606554/4b200ebf-eabd-4a9d-8f48-2fbcdb5d15aa)

<p>Podremos apreciar ue se decidio rutear por la parte de atras las conexiones principales y por delante se dispuso lo que seria el GND</p>

<h3>PCB 3D</h3>

![image](https://github.com/JOUNAL/SDV/assets/136606554/b99c30ea-63fb-4a57-ab40-c2e111876a7e)

# PRUEBAS

<p>1)En este caso de puso a prueba el SDV en un entorno controlado para comprobar su funcionalidad</p>
https://youtu.be/dbPjX9YF6rE

<p>2)En este caso de puso a prueba el SDV en una simlacion de lo que se encontraria cumpliendo a cabalidad su funcion, aumentado con este mismo fin la distancia que detectara el objetivo</p>
https://youtu.be/GnnjFE5JcX4
