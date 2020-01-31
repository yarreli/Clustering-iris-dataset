


---
por [yareli](https://github.com/yarreli)



# Cluster jerárquico flores de iris

_La idea general del clúster jerárquico se basa en la distancia entre los puntos del conjunto de datos. 
Hay dos formas de hacer clustering jerárquico: Agglomerative y Divisive. Para inferir el número de subgrupos 
en el conjunto se usa el dendograma.<br>
El conjunto de datos flor de iris contiene 50 observaciones de cada una de las 3 variedades de iris: setosa, 
virginica y versicolor. Estamos interesados en aplicar 3 algoritmos de agrupamiento y comparar su 
desempeño, además de medir la "cophenetic correlation" entre cada resultado del agrupamiento, la cual
es una medida de cuán fielmente un dendrograma preserva las distancias por pares entre el conjunto de datos._

### Explorando los datos
Previo a la clusterización, se hace un análisis para familiarizarse con los datos por medio de estadísticos
descriptivos y técnicas de visualización. Además de  analizar la presencia de outliers.

## Clúster jerárquico 🖇️
El grupamiento empleado fue *Agglomerative*, en donde se forman grupos de abajo hacia arriba, y
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
### Determinar los métodos a comparar
La función anterior se aplicó a todas las posibles combinaciones de los métodos, en donde se pueden combinar affinity y linkage para conseguir métodos con precisiones diferentes y se 
elegiría el de la mejor precisión. A continuación se muestran algunos ejemplos de las posibles combinaciones.
```
#for affin in ['euclidean','manhattan', 'cosine']:     
for affin in ['euclidean','manhattan']:
    for link in ['complete', 'single', 'average']:
        Hclus = AgglomerativeClustering(n_clusters=3, affinity=affin, linkage=link)
        Hclus.fit(xx)
        print ("Accuracy for a model with affinity=", affin, "and linkage=", link, ":")      
        print ("%.2f" % sm.accuracy_score(vari.variety_num, Hclus.labels_) )  # accuracy
        
Accuracy for a model with affinity=euclidean and linkage= ward: 0.89
Accuracy for a model with affinity= euclidean and linkage= complete: 0.49
Accuracy for a model with affinity= euclidean and linkage= single: 0.68
Accuracy for a model with affinity= euclidean and linkage= average: 0.91
Accuracy for a model with affinity= manhattan and linkage= complete: 0.33
Accuracy for a model with affinity= manhattan and linkage= single: 0.67
Accuracy for a model with affinity= manhattan and linkage= average: 0.90
Accuracy for a model with affinity= cosine and linkage= average: 0.66
```



 
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


