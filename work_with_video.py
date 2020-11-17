import cv2 as cv
import numpy as np

def draw_random_line(image):
    shape = image.shape[1], image.shape[0]

    x_first, y_first = np.random.randint((0, 0), shape, size=2)
    x_second = x_first + np.random.randint(1, shape[0] - x_first, size=1)
    y_second = y_first + np.random.randint(1, shape[1] - y_first, size=1)

    RED_COLOR = np.random.randint((0, 0, 0), (255, 255, 255), size=3)
    RED_COLOR = tuple([int(x) for x in RED_COLOR])
    thickness = np.random.randint(1, 10)

    image_with_line = cv.line(image, (x_first, y_first), (x_second, y_second), RED_COLOR, thickness)
    return image_with_line

def draw_random_rectangle(image):
    shape = image.shape[1], image.shape[0]

    x_first, y_first = np.random.randint((0, 0), shape, size=2)
    x_second = x_first + np.random.randint(1, shape[0] - x_first, size=1)
    y_second = y_first + np.random.randint(1, shape[1] - y_first, size=1)

    RED_COLOR = np.random.randint((0, 0, 0), (255, 255, 255), size=3)
    RED_COLOR = tuple([int(x) for x in RED_COLOR])
    thickness = np.random.randint(1, 10)

    image_with_rectangle = cv.rectangle(image, (x_first, y_first), (x_second, y_second), RED_COLOR, thickness)
    return image_with_rectangle

def proccess_image(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_image = cv.cvtColor(gray_image, cv.COLOR_GRAY2RGB)

    return draw_random_rectangle(draw_random_line(gray_image))
    
def get_and_save_video(output_filename_without_video_type_suffix, videocamera_shape, fps):
    output_filename = output_filename_without_video_type_suffix
    cap = cv.VideoCapture(0)
    out = cv.VideoWriter(output_filename + '.avi', cv.VideoWriter_fourcc(*'XVID'), fps, (videocamera_shape[1], videocamera_shape[0]), True)
    while True:
        ret, frame = cap.read()
        if ret == True:
            cv.imshow('frame',frame)
            out.write(frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
		
    out.release()
    cap.release()
    cv.destroyAllWindows()

def proccess_and_save_video(videoname, output_videoname_without_video_type_suffix, videocamera_shape, fps):
    output_videoname = output_videoname_without_video_type_suffix
    cap = cv.VideoCapture(videoname)
    out = cv.VideoWriter(output_videoname + '.avi', cv.VideoWriter_fourcc(*'XVID'), fps, (videocamera_shape[1], videocamera_shape[0]), True)
    while True:
        ret, frame = cap.read()
        if ret == True:
            proccess_frame = proccess_image(frame)
            cv.imshow('frame', proccess_frame)
            out.write(proccess_frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    cap.release()
    out.release()
    cv.destroyAllWindows()

videocamera_shape = (480, 640)
fps = 20
get_and_save_video('kek_video', videocamera_shape, fps)
proccess_and_save_video('kek_video.avi', 'kek_video_proccess', videocamera_shape, fps)

