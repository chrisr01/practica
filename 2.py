
def mayor(a,b,c):
    if ( ((a+b+c)/3) >=70 ):
        m = "Aprueba el curso"
    else:
        m = "Desaprueba el curso"
   
        
    return m
    
r= int(input("ingrese la primera calificacion:"))
s= int(input("ingrese la segunda calificacion:"))
t= int(input("ingrese la tercera calificacion:"))


print (" {}" .format(mayor(r,s,t)))
 
    
