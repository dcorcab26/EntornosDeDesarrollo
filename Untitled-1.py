
from sympy import isprime
try
	numero=int(input(“me das un numero?”))
 except ValueError:
	print(“debe introducir un numero entero”)
	   
try:
	if isprime(numero):
		print(f”el numero {numero} es primo”)
	else:
		print(f“el numero {numero} no es primo”)
except Exception as e:
	print(f“error inesperado, aparece {e}”)

