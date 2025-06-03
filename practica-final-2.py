# Paso 1: Soliticar al usuario las medidas de la pieza del mueble en centimetros
  
medida_en_cms = float(input("Por favor ingresar las medidas de la pieza del mueble (en centimetros): "))  #castea el input q es STR a FLOAT

# Paso 2: Convertir las medidas de centimetros a pulgadas

medida_en_in = medida_en_cms / 2.54

   
# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario.
    
print("Las medidas en pulgadas de la pieza ingresada son: ", medida_en_in)
