import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Cargar el conjunto de datos de diabetes
diabetes = load_diabetes()
a = diabetes.data
b = diabetes.target


# Definir los modelos
linear_model = LinearRegression()
#valores por defecto de la funcion alpha
ridge_model = Ridge(alpha=1.0)
lasso_model = Lasso(alpha=0.1)

# Entrena los modelos con los datos cargados
linear_model.fit(a, b)
ridge_model.fit(a, b)
lasso_model.fit(a, b)

# Obtener los coeficientes
linear_coefficients = linear_model.coef_
ridge_coefficients = ridge_model.coef_
lasso_coefficients = lasso_model.coef_

#obtiene los nombre de las caracteristicas del conjunto de datos
feature_names = diabetes.feature_names
#llamamos a p que creara una matriz que contenga el tamaño de los nombres de las caracteristicas
x = np.arange(len(feature_names))
# Graficar los coeficientes
#crea la figura de tamaño 10 pulgadas de ancho y 6 de ancho
plt.figure(figsize=(10, 6))
#crea una comparacion que utiliza las variables en x sus coeficientes(el marker sirve para cambiar la forma de los puntos escogidos)
plt.plot(x, linear_coefficients, marker='o')
plt.plot(x, ridge_coefficients, marker='s')
plt.plot(x, lasso_coefficients,  marker='^')
#define las posiciones en donde se encontraran las etiquetas
#los nombres de las etiquetas seran llamadas en labels
plt.xticks(ticks=x, labels=feature_names)
#crea los subtitulios del eje x e y
plt.xlabel('caracteristicas')
plt.ylabel('coeficientes')
#titulo
plt.title('comparacion de subtitulos')
#muestra grafica para denotar a que sistema de regrecion pertenece
plt.legend(["linear regression","ridge regression","lasso regression"])
#añade las cuadriculas en la grafica para que se vea de mejor manera
plt.grid(True)
#muestra todo el proyecto
plt.show()