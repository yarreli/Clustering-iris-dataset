
(affinity="euclidean", linkage='ward')   # accuracy = 0.8933

(affinity="euclidean", linkage='single')  # 0.68
(affinity="euclidean", linkage='average') # 0.9066
(affinity="euclidean", linkage='complete') #0.4933

(affinity="manhattan", linkage='single')  # 0.6733
(affinity="manhattan", linkage='average') # 0.9
(affinity="cosine", linkage='average')    # 0.66
 
### Método 1: Ward
La distancia para el último subgrupo es de 21 unidades aproximadamente (12 y 33), para el penúltimo fue
de 6 unidades, el anterior de 1, y las siguientes mucho menores. Por lo que en este caso tendría 
sentido elegir 2 o 3 clúster.

### Metodo 2: Complete
de 4 a 7 unidades en distancia antes del último grupo formado, 2.5 a 3, menos definidos que en el caso anterior.

### Método 3: Single
0.8 a 1.6  0.78 a 0.8
Es claro que un grupo sí está bien definido, pero los otros dos no claramente.

menos definidoooooo

Obtengo el puntaje de precisión más alto de 0.68 cuando se usa Euclidean y el pAverage como parámetros de enlace. 
Por lo tanto, es obvio que elegiré el tercero como modelo de agrupación jerárquica para el conjunto de datos de Iris.




---
por [yareli](https://github.com/yarreli)



# Cluster jerárquico flores de iris

_La idea general del clúster jerárquico se basa en la distancia entre los puntos del conjunto de datos. 
Hay dos formas de hacer clustering jerárquico: Agglomerative y Divisive. Para inferir el número de subgrupos 
en el conjunto se usa el dendograma.<br>
El conjunto de datos contiene 50 observaciones de cada una de las 3 variedades de iris: setosa, 
virginica y versicolor. Estamos interesados en aplicar 3 algoritmos de agrupamiento y comparar su 
desempeño, además de medir la "cophenetic correlation" entre cada resultado del agrupamiento, la cual
es una medida de cuán fielmente un dendrograma preserva las distancias por pares entre el conjunto de datos._

### Explorando los datos
Previo a la clusterización, se hace un análisis para familiarizarse con los datos por medio de estadísticos
descriptivos y técnicas de visualización. Además de  análizar la presencia de outliers.

## Clúster jerárquico 🖇️
La forma de agrupamiento fue con *Agglomerative*, en donde se forman grupos de abajo hacia arriba, y
hay 4 formas de linking (vincular) los datos: Ward, Complete, Single y Average. <br>
Primero se generó el dendograma en donde la distancia entre las barras representa la distancia al 
siguiente centro del grupo, esta técnica de visualización ayuda a determinar el número de subgrupos
a formar. <br>
A pesar de lo que sugieran los dendogramas, se eligieron 3 clúster en cada uno de los tres métodos, ya
que sabemos que hay tres variedades de flor, sin embargo, esto no siempre ocurre en la realidad.

## Pasos en el método de clustering jerárquico
1. Dibujar el dendograma
2. Generar el clúster: utilizando la función de python:
```
AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage="ward")
```
donde se pueden combinar affinity y linkage para conseguir métodos con precisiones diferentes y se 
elegiría el de la mejor precisión. A continuación se muestran 3 ejemplos de las posibles combinaciones.

```
Hclus = AgglomerativeClustering(n_clusters=3, affinity="manhattan", linkage='average')
Hclus.fit(flors)
sm.accuracy_score(vari.variety_num, Hclus.labels_)    # accuracy
# 0.9

Hclus = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage='ward')
Hclus.fit(flors)
sm.accuracy_score(vari.variety_num, Hclus.labels_)      # accuracy
# 0.8933

Hclus = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage='single')
Hclus.fit(flors)
sm.accuracy_score(vari.variety_num, Hclus.labels_)      # accuracy
# 0.68
```

