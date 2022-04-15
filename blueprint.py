import numpy as np
import matplotlib.pyplot as plt
import time


# First
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

im = plt.imread("D:\\mobile\\New folder\\Private\\new\\sugam\\IMG-20210308-WA0026.jpg")


fig, ax = plt.subplots()
ax.set_facecolor("black")
im = ax.imshow(im, extent=[-3, 58, 4, 50])

x = np.array(range(58))






x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show(block=False)
plt.pause(3) # 3 seconds, I use 1 usually

plt.close("all")

# Second
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True



im_1 = plt.imread("D:\\mobile\\New folder\\Private\\new\\sugam\\IMG_20210329_121011_187.jpg")
fig, ax = plt.subplots()
ax.set_facecolor("black")
im = ax.imshow(im_1, extent=[-3, 58, 4, 50])

x = np.array(range(58))

x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show(block=False)
plt.pause(3)
plt.close("all")

#Third
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

im_2 = plt.imread("D:\\mobile\\New folder\\Private\\new\\sugam\\IMG-20210815-WA0010.jpg")


fig, ax = plt.subplots()
ax.set_facecolor("black")
im = ax.imshow(im_2, extent=[-3, 58, 4, 50])

x = np.array(range(58))






x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show(block=False)
plt.pause(3) # 3 seconds, I use 1 usually

plt.close("all")

# Fourth
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

im_3 = plt.imread("D:\\mobile\\New folder\\Private\\new\\sugam\\Sugam CU 20210210_151438.jpg")


fig, ax = plt.subplots()
ax.set_facecolor("black")
im = ax.imshow(im_3, extent=[-3, 58, 4, 50])

x = np.array(range(58))






x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show(block=False)
plt.pause(3) # 3 seconds, I use 1 usually

plt.close("all")

# Fifth
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

im_4 = plt.imread("D:\\mobile\\New folder\\Private\\new\\sugam\\IMG_20210629_103134_397.jpg")


fig, ax = plt.subplots()
ax.set_facecolor("black")
im = ax.imshow(im_4, extent=[-3, 58, 4, 50])

x = np.array(range(58))






x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show(block=False)
plt.pause(2) # 3 seconds, I use 1 usually

plt.close("all")


fig, ax = plt.subplots()
ax.set_facecolor("black")
x1=[2,2,2,2,4,6,6,6]
y1=[2,0,-2,0,0,0,2,-2]

x2=[8,8,8,10,12,12,12,12,8]
y2=[-2,0,2,2,2,0,-2,0,0]

x3=[14,14,14,18,18,14]
y3=[-2,0,2,2,0,0]

x4=[20,20,20,24,24,20]
y4=[-2,0,2,2,0,0]

x5=[26,28,30,28,28]
y5=[2,0,2,0,-2]

x6=[2,2,2,6,6,6,2,2,6]
y6=[-8,-6,-4,-4,-6,-8,-8,-6,-6]

x7=[8,10,12,10,10,8,12]
y7=[-4,-4,-4,-4,-8,-8,-8]

x8=[14,14,18,18,14,18]
y8=[-8,-4,-4,-6,-6,-8]

x9=[20,24,22,22]
y9=[-4,-4,-4,-8]

x10=[26,26,26,30,30,30]
y10=[-8,-4,-6,-6,-8,-4]

x11=[32,32,36,36,32]
y11=[-8,-4,-4,-8,-8]

x12=[38,38,42,42,42,38]
y12=[-8,-4,-4,-8,-6,-6]

x13=[44,46,48,46,46]
y13=[-4,-6,-4,-6,-8]

l1=[5,0,0,5,5,0]
p1=[-10,-10,-12,-12,-14,-14]

l2=[10,10,15,15]
p2=[-10,-14,-14,-10]

l3=[30,20,20,25,25,30,30]
p3=[-10,-10,-14,-14,-12,-12,-14]

l4=[45,35,35,40,40,45,45]
p4=[-10,-10,-14,-14,-12,-12,-14]

l5=[50,50,55,55]
p5=[-10,-14,-14,-10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)


plt.plot(l1,p1)
plt.plot(l2,p2)
plt.plot(l3,p3)
plt.plot(l4,p4)
plt.plot(l5,p5)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
