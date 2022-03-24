import os
from tkinter import BOTTOM, S

import cv2
import numpy as np
import pandas as pd
import pytesseract

import environment as env
from tools import fix_image, fix_strings, fix_anomalies, fix_int

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Isa Sadiqli\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def process(src_vid):

    env.process_progress_bar.pack(pady=10, side=BOTTOM, anchor=S)

    video_len = int(src_vid.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = src_vid.get(cv2.CAP_PROP_FPS)
    frame_range = int(fps / env.fps_variable.get())

    index = 1
    if env.fps_variable.get() <= int(fps):
        env.is_high_FPS = False
        while src_vid.isOpened():

            prog = int(100 * index / video_len)
            env.process_progress_bar['value'] = prog
            env.window.update_idletasks()

            ret, frame = src_vid.read()
            if not ret:
                break

            # name each frame and save as png
            if index < 1000:
                name = './image_frames/frame0' + str(index) + '.png'
            else:
                name = './image_frames/frame' + str(index) + '.png'


            if index % frame_range == 0:
                print('Extracting frames ...' + name)

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower = np.array([39, 50, 125])
                upper = np.array([178, 255, 255])
                mask = cv2.inRange(hsv, lower, upper)

                mask = fix_image(mask)

                cv2.imwrite(name, mask)

            index = index + 1

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        env.label_information.configure(text='Video frames are extracted')
        src_vid.release()
        # cv2.destroyAllWindows()
    else:
        env.label_information.configure(text="The FPS value you selected is higher than the FPS value of the video.\n"
                                             "FPS of video is:" + str(fps))
        env.is_high_FPS = True


def get_text():

    env.read_progress_bar.pack(pady=10, side=BOTTOM, anchor=S)

    sourceFile = open('files/output.txt', 'w')

    try:
        os.remove("cropped_images")
    except OSError:
        pass

    if not os.path.exists("cropped_images"):
        os.makedirs("cropped_images")

    # progress['value'] = 0

    data = {
        'day': [],
        'month': [],
        'year': [],
        'hour': [],
        'min': [],
        'sec': [],
        'degree_lat': [],
        'minute_lat': [],
        'second_lat': [],
        'direction_lat': [],
        'degree_lon': [],
        'minute_lon': [],
        'second_lon': [],
        'direction_lon': [],
    }

    df = pd.DataFrame(data)
    j = 0
    for i in os.listdir(env.image_frames):
        print(str(i))
        frame = cv2.imread(env.image_frames + "/" + i)

        crop = {'day': frame[25:60, 24:74],
                'month': frame[25:60, 71:144],
                'year': frame[25:60, 144:240],
                'hour': frame[55:94, 20:74],
                'min': frame[58:94, 96:149],
                'sec': frame[58:94, 166:218],
                'degree_lat': frame[1010:1044, 48:119],
                'minute_lat': frame[1010:1044, 140:193],
                'second_lat': frame[1010:1044, 217:264],
                'direction_lat': frame[1010:1044, 264:291],
                'degree_lon': frame[1041:1077, 46:119],
                'minute_lon': frame[1041:1077, 140:193],
                'second_lon': frame[1041:1077, 217:264],
                'direction_lon': frame[1041:1077, 264:291],
                }

        print(i, file=sourceFile)
        k = 0
        text = {'frame': i}
        for c in crop.keys():
            if c == 'month':
                text[c] = pytesseract.image_to_string(crop[c], lang='eng',
                                                      config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPRSTUVWXYZ  --psm 6')
            elif c == 'direction_lat':
                text[c] = pytesseract.image_to_string(crop[c], lang='eng',
                                                      config='-c tessedit_char_whitelist=SN  --psm 6')
            elif c == 'direction_lon':
                text[c] = pytesseract.image_to_string(crop[c], lang='eng',
                                                      config='-c tessedit_char_whitelist=EW  --psm 6')
            else:
                text[c] = pytesseract.image_to_string(crop[c], lang='eng',
                                                      config='-c tessedit_char_whitelist=0123456789  --psm 6')

            text[c] = text[c].replace("\u000C", "")
            text[c] = text[c].replace("\n", "")

            k += 1
            cv2.imwrite("cropped_images/" + i + "_" + str(k) + '.' + c + ".png", crop[c])

            print(text[c], file=sourceFile)

            j += 1
            prog = int(100 * j / (os.listdir(env.image_frames).__len__() * crop.__len__()))
            env.read_progress_bar['value'] = prog
            env.window.update_idletasks()

        df = df.append(text, ignore_index=True)


    #df['minute_lat'] = fix_int(df['minute_lat'])
    #df['second_lat'] = fix_int(df['second_lat'])
#
    #df['minute_lon'] = fix_int(df['minute_lon'])
    #df['second_lon'] = fix_int(df['second_lon'])

    df['month'] = fix_strings(df['month'])
    df['direction_lat'] = fix_strings(df['direction_lat'])
    df['direction_lon'] = fix_strings(df['direction_lon'])
    df['day'] = fix_anomalies(df['day'], 1)
    df['year'] = fix_strings(df['year'])
    df['hour'] = fix_anomalies(df['hour'], 3)
    df['min'] = fix_anomalies(df['min'], 3)
    df['sec'] = fix_anomalies(df['sec'], 1)
    df['degree_lat'] = fix_anomalies(df['degree_lat'], 3)
    df['minute_lat'] = fix_anomalies(df['minute_lat'], 3)
    df['second_lat'] = fix_anomalies(df['second_lat'], 3)
    df['degree_lon'] = fix_anomalies(df['degree_lon'], 3)
    df['minute_lon'] = fix_anomalies(df['minute_lon'], 2)
    df['second_lon'] = fix_anomalies(df['second_lon'], 3)
    df.to_csv('files/output.csv', index=False)

    env.label_information.configure(text='CSV file is complete')

    sourceFile.close()
    env.read_progress_bar['value'] = 100
    env.window.update_idletasks()
