Instalacion ultralytics
pip install ultralytics
pip install supervision


Decisiones elegidas:
Ultralytics es la empresa/organización que desarrolla y mantiene las implementaciones modernas de YOLO (You Only Look Once), una familia de modelos de deep learning especializados en detección de objetos en tiempo real. Ultralytics tomó un papel central a partir de YOLOv5, desarrollando un repositorio muy popular en PyTorch, fácil de usar y con herramientas listas para entrenamiento, validación e inferencia.Hoy, Ultralytics mantiene modelos más avanzados como YOLOv8, que no solo hace detección de objetos, sino también clasificación de imágenes, segmentación y seguimiento de objetos (tracking).

Además, Ultralytics ofrece:
Una librería en Python (ultralytics) que facilita usar YOLO con pocas líneas de código.
Una plataforma web para entrenar, desplegar y gestionar modelos en la nube.

En Yolo se puede tener las cordenadas mediante:
* el punto del centro, ancho y alto. Osea x, y , with, height
* Las esquinas izquierda arriba y derecha abajo. x1, y1, x2, y2
* otros.

Ejemplo de results[0]
xywh: tensor([[431.7008, 868.9752,  76.4810, 202.6715]], device='cuda:0')
xywhn: tensor([[0.3997, 0.4526, 0.0708, 0.1056]], device='cuda:0')
xyxy: tensor([[393.4603, 767.6394, 469.9413, 970.3109]], device='cuda:0')
xyxyn: tensor([[0.3643, 0.3998, 0.4351, 0.5054]], device='cuda:0')


Se detecta mediante la red convolucional, la clase, el id y la posicion


Inconvenientes:
* La pelota la mayoria del tiempo no la localiza ya que se mueve muy rapido
* Detecta personas fuera de la cancha. Debería ignorarlas
* El referi debería detectarlo?

Para resolver estos inconvenientes podemos bajar un dataset de roboflow
https://universe.roboflow.com/roboflow-jvuqo/   -3zvbc/dataset/19#