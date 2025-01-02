import os
import time

from ultralytics import YOLO

from src.Utilities import flexMenu
from src.Utilities import log


def m_train():
    start_time = time.time()
    m=""
    try:
        # Code that might raise an exception
        f = ['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt']
        model_path = os.getcwd() + "OUTPUT//yolov8DefaultModels/"
        model_name = flexMenu.display_options(f)
        model_path = model_path + model_name
        data_path = "OUTPUT/datasets"
        f = os.listdir(data_path)
        y = os.getcwd()
        print("\n\t DATASETS :")
        x = flexMenu.display_options(f)
        data_path = y + "/" + data_path + "/" + x + "/data.yaml"
        print("\n\tConfigure Training Parameters : ")
        epochs = int(input("\n\t  ======> Insert Epochs Value   : "))
        imgsz = int(input("\n\t  ======> Insert imgsz Value    : "))
        device_input = input("\n\t  ======> Insert device Value (cpu or GPU ID): ")
        device = device_input if device_input.lower() == "cpu" else int(device_input)
        print
        lr = float(input("\n\t  ======> Insert learning Rate Value  : "))
        project = "OUTPUT//Train"
        if model_name == "yolov8n.pt":
            m = "n"
        elif model_name == "yolov8s.pt":
            m = "s"
        elif model_name == "yolov8m.pt":
            m = "m"
        elif model_name == "yolov8l.pt":
            m = "l"
        elif model_name == "yolov8x.pt":
            m = "x"

        name = "train-e" + str(epochs) + "-i" + str(imgsz) + "-lr" + str(lr) + "-" + "v8" + m
        start_time = time.time()
        model = YOLO(model_path)
        log.logger.info("\nTraining START")
        print("\n")
        model.train(data=data_path, epochs=epochs, imgsz=imgsz, device=device,
                     project=project, name=name, show_labels=True,
                    lr0=lr)

    except Exception as e:
        # Code to handle other exceptions
        end_time = time.time()
        log.logger.error(f"\nAn error occurred: {e}\nExecution time: %.2f seconds", end_time - start_time)
    else:
        # Code to run if no exception occurred
        end_time = time.time()
        log.logger.info("\nNo errors occurred DONE SUCESS\nExecution time: %.2f seconds", end_time - start_time)

    finally:
        # Code that will run regardless of whether an exception occurred
        log.logger.critical("\nTrainning EXIT")
        print("\n")
