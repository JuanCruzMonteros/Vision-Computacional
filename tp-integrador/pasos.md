Referencias
https://docs.ultralytics.com/es/tasks/detect/


hasta minuto 3:
solo explica que es object detection y descarga el video


minuto 4:
La red convolucional elegida es Yolo de Ultralitics
pip install ultralytics

minuto 10:
explica como funciona el output mediante corrdenadas de los objetos encontrados por el modelo.


11:30 explica como se pueden organizar las coordenadas.

17:35


19: Por los inconvenientes encontrados recomendó buscar un dataset en roboflow


Desde minuto 23 y 26 se explica como funciona roboflow y la data de entrenamiento
34 ya tengo los pesos de la carpeta de entrenamiento por lo que los paso al proyecto principal para utilizarlos.

39:00
La idea es crear un archivo de utilidades para leer video mediante OpenCV. Así obtenemos la lista de frames del video y devolverlos como un array.

51: VAmos a usar un tracker para trackear los jugadores en los frames. Para ello necesitamos que cada box tenga un ID

Partido encontrado con bordes bien marcados:
https://www.youtube.com/watch?v=t10423Ay3qM&t=1239s&ab_channel=Chepsi007

48 Pasa a explicar por que vamos a usar un tracker
51:30  empezamos a crear un tracker. Nos permite estimar la posición y trayectoria del objeto a lo largo del tiempo por ejemplo de la pelota.