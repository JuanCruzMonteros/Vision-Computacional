
from utils import read_video, save_video

def main():
    PATH_INPUT_VIDEO = 'input_videos/partido_corto.avi'
    PATH_OUTPUT_VIDEO = 'output_videos/partido.avi'
    video_frames = read_video(PATH_INPUT_VIDEO)

    save_video(video_frames, PATH_OUTPUT_VIDEO)

main()
# yolo_inference.py
# pip install ultralytics opencv-python

""" from ultralytics import YOLO
import cv2

# Cargar modelo preentrenado YOLOv8
model = YOLO('yolo11n.pt')  # Modelo pequeño y rápido

# Ruta del video de entrada
video_path = 'partido.mp4'  # Cambia por tu video
cap = cv2.VideoCapture(video_path)

# Configuración del video de salida
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height)) """
