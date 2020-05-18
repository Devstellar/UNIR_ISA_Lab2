# -*- coding: utf-8 -*-

# Realiza la suma de los argumentos a y b
def suma(a, b):
  return(a + b)

# Realiza la resta sobre el argumento a de b
def resta(a, b):
  return(a - b)

# Realiza la multiplicación de a y b
def multiplicacion(a, b):
  return(a*b)

# Realiza la división de a por b
def division(a, b):
  return(a / b)

# Realiza la raíz cuadrada de x, por aproximación
def raiz_cuadrada(x, error=0.00001):
  # si el número es 1 se puede producir una división por 0
  if (x == 1):
    return(1)

  # chequeo de seguridad
  max_iteraciones = 20
  
  # Encontrar el valor más cercano a solución, iterando
  p = 1
  while ((multiplicacion(p, p) < x)):
    p = suma(p, 1)
  if (resta(multiplicacion(p, p), x) < (resta(p, 1) * resta(resta(p, 1), x))):
    n = p
  else:
    n = resta(p, 1)

  anterior = 0  
  # controla el número máximo de iteraciones
  for i in range(0, max_iteraciones):
    # aplicar formula Bakhshali
#    n = (n*n*n*n + 6*n*n*x + x*x)/(4*n*n*n + 4*n*x)
    n = division(suma(suma(multiplicacion(multiplicacion(multiplicacion(n, n), n), n),
                           multiplicacion(multiplicacion(multiplicacion(6, n), n), x)),
                      multiplicacion(x, x)),
                 suma(multiplicacion(multiplicacion(multiplicacion(4, n), n), n),
                      multiplicacion(multiplicacion(4, n), x))
      )
 
    # estima si el error está en rango (libro Análisis Matemático)
    if ((abs(resta(multiplicacion(n, n), x)) < error) and
        (abs(resta(n, anterior)) < error)):
      break
    anterior = n

  return(n)
