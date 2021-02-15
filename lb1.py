#ІВ-93 Кочерга Андрій Варіант 11
#Змінна GLOVA мала використовуватися для гарного вигляду виводу("X1",'X2',"X3"...),але я забув про неї и додав теж саме в 46 рядку в insert,тобто данна змінна - непотрібна 
import random
a0=3
a1=4
a2=7
a3=3
x1=random.sample(range(1, 20), 8)
x2=random.sample(range(1, 20), 8)
x3=random.sample(range(1, 20), 8)
X0x1=(min(x1)+max(x1))/2
X0x2=(min(x2)+max(x2))/2
X0x3=(min(x3)+max(x3))/2
DXx1=X0x1-min(x1)
DXx2=X0x3-min(x2)
DXx3=X0x2-min(x3)
Xn1=[]
Xn2=[]
Xn3=[]
for i in range(len(x1)):
 Xn1.append(round((x1[i]-X0x1)/DXx1,4))

for i in range(len(x2)):
 Xn2.append(round((x2[i]-X0x2)/DXx2,4))

for i in range(len(x3)):
 Xn3.append(round((x3[i]-X0x3)/DXx3,4))

Y=[]
for i in range(len(x1)):
 Y.append(a0+(a1*x1[i])+(a2*x2[i])+(a3*x3[i]))


Vuvod=[]
for i in range(8):
 Vuvod.append([])
 Vuvod[i].append(i+1)
 Vuvod[i].append(x1[i])
 Vuvod[i].append(x2[i])
 Vuvod[i].append(x3[i])
 Vuvod[i].append(Y[i])
 Vuvod[i].append(Xn1[i])
 Vuvod[i].append(Xn2[i])
 Vuvod[i].append(Xn3[i])
GLOVA=["№","X1",'X2',"X3",'Y',"Xn1","Xn2","Xn3"]
Vuvod.insert(0,["№","X1",'X2',"X3",'Y',"Xn1","Xn2","Xn3"])
Vuvod.append([])
Vuvod.append([])
Vuvod[-1].append("X0")
Vuvod[-1].append(X0x1)
Vuvod[-1].append(X0x2)
Vuvod[-1].append(X0x3)
Vuvod.append([])
Vuvod[-1].append("dx")
Vuvod[-1].append(DXx1)
Vuvod[-1].append(DXx2)
Vuvod[-1].append(DXx3)
for row in Vuvod:
    print(' | '.join([str(elem) for elem in row]))
print("max(Y)=",max(Y))
print('a0={},a1={},a2={},a3={}'.format(a0,a1,a2,a3))
