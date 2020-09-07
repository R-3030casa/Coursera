#Forma um quadrado
'''from turtle import *  # importa a biblioteca
color('blue', 'green')  # escolhe a cor do traco e do preenchimento
begin_fill()  # inicia o desenho na posicao (0,0)
forward(200)  # move 200 passos a frente
left(90)  # vira a esquerda 90 graus
forward(200)  # move 200 passos a frente
left(90)  # vira a esquerda 90 graus
forward(200)  # move 200 passos a frente
left(90)  # vira a esquerda 90 graus
forward(200)  # move 200 passos a frente
end_fill()  # preenche o desenho
done()  # encerra o processo'''

import turtle

tim = turtle.Turtle()
tim.color('red')
tim.pensize(5)
tim.shape('turtle')

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('green')
tim.forward(100)

dave = turtle.Turtle()
dave.color('blue')
dave.pensize(20)

dave.backward(100)
dave.speed(1)
