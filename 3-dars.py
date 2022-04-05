# -*- coding: utf-8 -*-
"""
03-dars. PRINT() by Anvar Narzullayev

Created on Tue Apr  5 14:26:20 2022

@author: Urozboev Shavkat

"""
# Quyidagi kod Hello World jumlasini konsolga chiqaradi
print("Assalomu alaykum")
print('Hello World!')
# consol tozalash uchun --- clear --- bosiladi
print('Men "Dell" Markasidagi noutbook sotib oldim.')
print("""Odami ersang, demagil odami,
oniki, yo'q xalq g'amidin g'ami """)
print('''Odami ersang, demagil odami,
oniki, yo'q xalq g'amidin g'ami ''')

#  \n qatorga bo'lish belgisi
 
# o', g', ishlatganimizda \(backshlash)ishlatish kerek

print('Odami ersang, demagil odami, oniki, yo\'q xalq g\'amidin g\'ami')

print(" Odami ersang,\n demagil odami,\n oniki, yo'q xalq g'amidin g'ami")

#              RAQAMLAR bilan ishlash

print(2+4*2)
# pythonda arifmetik amallar ham bir xil ketma ketlikda bajariladi
print(19/5)
# " / " bo'lish bunda butun yani o'nli qismi ham ko'rinadi. example 2.43
print(200//5)
# " // " bo'lish bunda butun qismi ham ko'rinadi. example 2.0; 4.0
print(166//2)
print(2**64)
# " ** " kvadratga oshirish belgisi: 2**4=16
print("To'qizning kvadrati", 9**2, "ga teng")
print('3x3=',3*3)

# Amaliy mashg'ulot

#2-Misol if and else
print("2-example")
print("""Oxiri 7 raqami bilan tugaydigan son besh xonali sondan
kichik va 9987 dan katta ekani ma'lum. Shu sonni toping.""")
print("9987<a<10000 a ni toping?")
print("Answer:",9997)

# 3-Misol 
print("3-example")
print("""To'g'ri to'rtburchakning eni bo'yidan 8 m qisqa, 
perimetri esa 64 m. Shu to'g'ri to'rtbuchakning yuzini toping.""")
print("""b=a-8
p=2*(a+b)=64
s=a*b=?""")
p=64

a=((p/2)+8)/2
b=a-8
s=a*b
print(s)


# 4- Misol
print("4-example")
print("""Men bir son o'yladim. 
Agar u son 12 ga BO'LINSA  va
bo'linmaga 350 qo'shilsa, 
yig'indi 410 hosil bo'ldi. 
O'ylasgan sonimni toping.""")

print(" O'ylagan sonim x bo'lsin. x/12+350=410")
x= (410-350)*12
print("Answer: x= (410-350)*12 =",x)
































