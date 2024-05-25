#!/usr/bin/env python

import rospy
import numpy as np
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand

# Autores
# Joan Sebastian Arcila Cardozo
# Gustavo Adolfo Ropero Bastidas

posicion = [0, 0, 0, 0, 0]
Limite = [400, 400, 400, 400, 400]
Caso1 = [25, 25, 20, -20, 0]
Caso2 = [-35, 35, -30, 30, 0]
Caso3 = [85, -20, 55, 25, 0]
Caso4 = [80, -35, 55, -45, 0]
Home = [512, 512, 819, 512, 512]
p1 = [598, 598, 887, 443, 512]
p2 = [392, 631, 716, 614, 512]
p3 = [802, 443, 1006, 597, 512]
p4 = [785, 392, 1006, 358, 512]
Angulos = [p1, p2, p3, p4]
Resolucion = [Caso1, Caso2, Caso3, Caso4]

# Función para imprimir las posiciones de los eslabones
def print_positions(pos):
    print('Posiciones de los eslabones:\n')
    for i in range(len(pos)):
        print(f'{i+1}: {pos[i]:.2f}°\t', end=' ')
    print('\n')

caso = int(input())

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

# Actualizar las posiciones
def update_positions(data):
    global posicion
    posicion = np.multiply(data.position, 180/np.pi)
    posicion[2] = posicion[2] - 90

def print_actual_positions(real, teorico):
    for i in range(len(real)):
        print(f'{i+1}: {real[i]:.2f}°\t', end=' ')

def subscribe_to_joint_states():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, update_positions)

def move_joint_sequentially(joint, goal, actual):
    N = 5
    delta = ((goal - actual) / N)
    for i in range(N):
        send_motor_command('', (joint + 1), 'Goal_Position', int(actual + delta * (i + 1)), 0.5)
        time.sleep(0.1)

MetaAngulos = Angulos[caso - 1]
MetaCasos = Resolucion[caso - 1]

if __name__ == '__main__':
    try:
        subscribe_to_joint_states()

        for i in range(5):
            send_motor_command('', (i + 1), 'Torque_Limit', Limite[i], 0)

        for i in range(5):
            send_motor_command('', (i + 1), 'Goal_Position', Home[i], 1)
            time.sleep(0.5)

        for i in range(5):
            move_joint_sequentially(i, MetaAngulos[i], Home[i])

        print_actual_positions(posicion, MetaCasos)
    except rospy.ROSInterruptException:
        pass
