# Laboratorio 4

### Joan Sebastian Arcila Cardozo
### Gustavo Adolfo Ropero Bastidas

## Universiad Nacional de Colombia

En este laboratorio, trabajamos con el robot Phantom X Pincher para llevar a cabo diversas tareas de medición y análisis cinemático. El objetivo principal fue determinar las longitudes de los eslabones del robot, derivar los parámetros Denavit-Hartenberg (DH), implementar el control de las articulaciones utilizando ROS y Dynamixel, y finalmente, crear una interfaz de usuario que facilite la interacción con el robot. Se utilizaron herramientas avanzadas como el Toolbox de Peter Corke para MATLAB para modelar y simular el comportamiento del robot.

## Mediciones de Longitudes de Eslabón
### Diagrama de Longitudes del Robot

El diagrama de longitudes del robot Phantom X Pincher es fundamental para entender su estructura y funcionamiento. Este diagrama representa las distancias entre las articulaciones del robot y es crucial para la configuración correcta de sus movimientos.

![Screenshot 2024-05-24 002613](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/f308cdd9-d2d7-463c-b420-0c59949b4733)

El diagrama de longitudes del robot junto con las direciones en las articulaciones, es una representación visual de los eslabones y articulaciones del Phantom X Pincher. A continuación, se presenta un esquema

![Screenshot 2024-05-24 002613](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/a6843383-f5b2-4300-8678-d9908d4a4507)

Con las dimensiones medidas, se obtuvieron los parámetros de Denavit-Hartenberg (DH) del robot. Estos parámetros son esenciales para la descripción matemática de la cinemática del robot y se utilizan para calcular las transformaciones entre las diferentes articulaciones.

### Tabla de Parámetros DH

La tabla con los parámetros DH calculados a partir de las longitudes medidas.

![image](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/23ad94b5-1554-4520-b4fa-d4e99901f895)

# Simulación del Robot Phantom X Pincher

Este proyecto contiene la simulación del robot Phantom X Pincher utilizando MATLAB. A continuación se presenta el código utilizado para definir y simular el robot.

## Código de Simulación en MATLAB

Gracias al codigo que nos proporciono el profesor Pedro Cardenas, se logro mejorar y optimizar para proporcionar una buena simulación.

### Configuración del Espacio de Trabajo y Opciones de Ploteo

Se estableció el espacio de trabajo (workspace) del robot para asegurar que todas las posibles posiciones y configuraciones del robot sean visualizadas correctamente:

```matlab
ws = [-300 300 -300 300 0 350];
```
Las opciones de ploteo (plot_options) incluyen parámetros como el tamaño del robot, la vista de la cámara, la posición de la luz, y la presencia de una base y un suelo:

```matlab
plot_options = {'workspace', ws, 'scale', 0.6, 'noa', 'view', [125 25], 'tilesize', 2, ...
                'ortho', 'lightpos', [2 2 10], ...
                'floorlevel', 0, 'base'};
```
### Definición de los Parámetros DH

Los parámetros DH del robot Phantom X Pincher se definieron utilizando el objeto Link del toolbox de Peter Corke. Cada articulación se configuró como un eslabón revoluto con sus respectivos parámetros DH:

```matlab
L(1) = Link('revolute', 'alpha', pi/2, 'a', 0, 'd', L1, 'offset', 0, 'qlim', [-pi pi]);
L(2) = Link('revolute', 'alpha', 0, 'a', L2, 'd', 0, 'offset', pi/2, 'qlim', [-2*pi/3 2*pi/3]);
L(3) = Link('revolute', 'alpha', 0, 'a', L3, 'd', 0, 'offset', pi/2, 'qlim', [-2*pi/3 2*pi/3]);
L(4) = Link('revolute', 'alpha', pi/2, 'a', 0, 'd', 0, 'offset', pi/2, 'qlim', [-pi/2 pi/2]);
L(5) = Link('revolute', 'alpha', 0, 'a', 0, 'd', L4, 'offset', 0, 'qlim', [0 0]);
```
La configuración incluye los desplazamientos (offsets) y los límites articulares (qlim) para cada articulación.

### Creación del Modelo del Robot

El objeto SerialLink se utiliza para agrupar los eslabones en un modelo de robot y establecer sus opciones de ploteo:

```matlab
Robot = SerialLink(L, 'name', 'Robot', 'plotopt', plot_options);
```
### Visualización y Configuración Inicial
El robot se visualiza en una posición inicial (home) con todas las articulaciones en cero grados:

```matlab
q = [0 0 0 0 0];
Robot.teach(q);
hold on;
trplot(eye(4), 'length', 24);
```
### Resultados de las poses con sus respectivos angulos

El código proporciona una simulación completa del robot Phantom X Pincher, desde la definición de los parámetros DH hasta la visualización y cálculo de la cinemática directa. La configuración visualizada coincide con la configuración teórica establecida por los parámetros DH.

### Pose Home

![Screenshot 2024-04-29 104330](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/e90507af-fc76-4d97-abd0-c7070fa102f6)


### Pose 1

![Screenshot 2024-04-29 103641](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/fc0fe44e-fcb4-402a-81e6-00987bbe76a6)


### Pose 2

![Screenshot 2024-04-29 103918](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/b75e0a5e-a945-4300-abc7-c213cd9f471d)


### Pose 3

![Screenshot 2024-04-29 104150](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/9cea936e-2a59-4fa3-9128-1ad571152f46)


### Pose 4

![Screenshot 2024-04-29 104251](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/fa121adb-461a-4c80-8c53-64e1924a78bd)

## Interfaz de Usuario (HMI)

Los servomotores utilizados en robots como el Phantom X Pincher generalmente emplean un rango de valores de 0 a 1023 debido a la resolución de su sistema de control de posición. Esta resolución está basada en la conversión analógica-digital y en la capacidad del controlador del servomotor para manejar y ajustar posiciones angulares precisas. El rango de 0 a 1023 se asigna a la capacidad del servomotor para moverse dentro de su ángulo total permitido. Según Dymanixel Wizard 2.0, los servomotores tienen un rango de 0 a 300 grados. Esto significa que cada incremento en el valor de control representa un cambio muy pequeño y preciso en el ángulo del servomotor. Para el debido funcionamiento del codigo Python se hizo la relación de los grados entre la resolución de los servomotores para obtener los valores esperados.

### Descripción de la Interfaz

Para facilitar la interacción con el robot Phantom X Pincher, se ha desarrollado una interfaz de usuario (Basado en el controller de Felipe Gonzalez, se menciona para darle los respectivos reconocimientos) que permite a los usuarios controlar y monitorear el robot de manera intuitiva y eficiente. Esta interfaz está diseñada para permitir el envío de comandos a las distintas articulaciones, la interfaz fue modificada para que permita el manejo de los 5 servomotores.

### Conexión con Python

Para integrar el control del robot con la interfaz de usuario, se han desarrollado scripts en Python que permiten la comunicación con los motores Dynamixel del robot a través de ROS. A continuación, se describen los scripts utilizados para la publicación y suscripción en los tópicos de ROS.

```python
# Función para enviar comandos a los motores Dynamixel
def send_motor_command(command, id_num, addr_name, value, time):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command, id_num, addr_name, value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))
```

El código incluye un panel de control que permite a los usuarios seleccionar entre cinco poses predefinidas. Estas poses representan configuraciones específicas del robot que han sido programadas para demostrar sus capacidades de movimiento. Al seleccionar una de estas poses, el usuario puede enviar la configuración correspondiente al robot con solo un clic, facilitando la demostración de las distintas posiciones del manipulador.

Se ha creado un script en Python que permite publicar en cada tópico de controlador de articulación. Este script se asegura de que los comandos enviados a las articulaciones respeten los límites articulares predefinidos, evitando movimientos que puedan dañar el robot o exceder sus capacidades mecánicas.

También se ha implementado un script en Python para suscribirse a los tópicos de controlador de articulación. Este script escucha los mensajes publicados en los tópicos de las articulaciones y retorna la configuración de cinco ángulos en grados. Esto permite monitorear continuamente la posición del robot y actualizar la interfaz de usuario con los valores articulares actuales.

# Resultados

Estos scripts permiten una integración completa entre MATLAB, Python y ROS, facilitando simulación, control y monitoreo del robot Phantom X Pincher a través de una interfaz de usuario intuitiva y funcional. La combinación de estas herramientas proporciona una plataforma poderosa para la investigación y desarrollo en robótica, permitiendo a los usuarios interactuar de manera efectiva con el robot y analizar su comportamiento en tiempo real.

## Video de demostración

