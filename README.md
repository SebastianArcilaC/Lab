# Laboratorio 4

### Joan Sebastian Arcila Cardozo
### Gustavo Adolfo Ropero Bastidas

## Universiad Nacional de Colombia

En este laboratorio, trabajamos con el robot Phantom X Pincher para llevar a cabo diversas tareas de medición y análisis cinemático. El objetivo principal fue determinar las longitudes de los eslabones del robot, derivar los parámetros Denavit-Hartenberg (DH), implementar el control de las articulaciones utilizando ROS y Dynamixel, y finalmente, crear una interfaz de usuario que facilite la interacción con el robot. Se utilizaron herramientas avanzadas como el Toolbox de Peter Corke para MATLAB para modelar y simular el comportamiento del robot.

## Mediciones de Longitudes de Eslabón
### Diagrama de Longitudes del Robot

![Screenshot 2024-05-24 002613](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/f308cdd9-d2d7-463c-b420-0c59949b4733)
![Screenshot 2024-05-24 002613](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/a6843383-f5b2-4300-8678-d9908d4a4507)



### Tabla de Parámetros DH
La tabla con los parámetros DH calculados a partir de las longitudes medidas.

![image](https://github.com/SebastianArcilaC/lab4robotics/assets/115434124/23ad94b5-1554-4520-b4fa-d4e99901f895)

## Simulación en Matlab
# Proyecto de Simulación del Robot Phantom X Pincher

Este proyecto contiene la simulación del robot Phantom X Pincher utilizando MATLAB. A continuación se presenta el código utilizado para definir y simular el robot.

## Código de Simulación en MATLAB

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
