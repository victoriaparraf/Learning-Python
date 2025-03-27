#comprehesion list

lista_normal= [1,2,3,4,5,6,7,8,9,10]
lista_comprenhension = [i for i in lista_normal if i%2==0]
print(lista_comprenhension)

#lambdas
lambda x: x+1
lambda x,y: x+y
lambda x,y,z: x+y+z
lambda x,y,z: x+y-z

my_lambda = lambda x: x+1
print(my_lambda(5))