#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os 

def get_all_folders(): 
    subfolders = [ f.path for f in os.scandir("./") if f.is_dir() ]
    print("Total Existing Folders: ")
    total_folders = 0
    for f in subfolders:
        print(f)
        total_folders += 1
    print("Total: {}".format(total_folders))

    return { 
            "subfolders": subfolders, 
            "total": total_folders
            }

def exec(video_path, ouput_path):
    cam = cv2.VideoCapture(video_path)
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except OSError as e:
        print("Error: Creating Directory: {}".format(e))

    current_frame = 0
    while(True):
        ret, frame = cam.read()
        if ret: 
            # if video is still creating images
            name = output_path + "/frame-" + str(current_frame) + ".jpg"
            print("Creating .... {}".format(name))

            cv2.imwrite(name, frame)

            current_frame += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    import os 
    try: 
        path = os.getcwd()
        video = sys.argv[1] 

        video_path = "{}/{}".format(path, video)
    except:
        path = "/Users/$USER/Repo/python-templates/media_files"
        video_path = "{}/file_name.mp4".format(path)

    current_folders = get_all_folders()
    output_path = "output_{}".format(current_folders['total'])

    exec(video_path, output_path)
