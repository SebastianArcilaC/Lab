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

```matlab
clear ;clf;clc;
L1 = 40.6; L2 = 107; L3 = 107; L4 = 69.5;
ws = [-300 300 -300 300 0 350];

plot_options = {'workspace', ws, 'scale', 0.6, 'noa', 'view', [125 25], 'tilesize', 2, ...
                'ortho', 'lightpos', [2 2 10], ...
                'floorlevel', 0, 'base'};

L(1) = Link('revolute', 'alpha', pi/2, 'a', 0, 'd', L1, 'offset', 0, 'qlim', [-pi pi]);
L(2) = Link('revolute', 'alpha', 0, 'a', L2, 'd', 0, 'offset', pi/2, 'qlim', [-2*pi/3 2*pi/3]);
L(3) = Link('revolute', 'alpha', 0, 'a', L3, 'd', 0, 'offset', pi/2, 'qlim', [-2*pi/3 2*pi/3]);
L(4) = Link('revolute', 'alpha', pi/2, 'a', 0, 'd', 0, 'offset', pi/2, 'qlim', [-pi/2 pi/2]);
L(5) = Link('revolute', 'alpha', 0, 'a', 0, 'd', L4, 'offset', 0, 'qlim', [0 0]);

Robot = SerialLink(L, 'name', 'Robot', 'plotopt', plot_options);

Robot.tool = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1];

q = [0 0 0 0 0];
Robot.teach(q);
hold on;
trplot(eye(4), 'length', 24);

M = Robot.base;
for i = 1:Robot.n
    M = M * L(i).A(q(i));
    trplot(M, 'rgb', 'frame', num2str(i), 'length', 50);
end

TCP = Robot.fkine(q);
trplot(TCP, 'length', 2);
tr2rpy(TCP, 'zyx', 'deg');

MTH = Robot.fkine(q);
disp('La matriz de transformación homogénea (MTH) es:');
disp(MTH);
