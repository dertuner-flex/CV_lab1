import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def show_image(img):
    plt.figure()
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

def get_and_save_image(path_to_save_file):
	camera = cv.VideoCapture(0)
	ref, frame = camera.read()
	camera.release()

	if not ref:
		raise Exception("Problem with webcamera...")

	cv.imwrite(path_to_save_file, frame)
	show_image(frame)

def read_image(path_to_file):
	return cv.imread(path_to_file)

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

def proccess_and_show_image(image):
	gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	gray_image = cv.cvtColor(gray_image, cv.COLOR_GRAY2RGB)

	proccess_image = draw_random_rectangle(draw_random_line(gray_image))
	show_image(proccess_image)

def get_image_shape(image):
	return image.shape[:2]

filename = 'kek.png'
get_and_save_image(filename)
proccess_and_show_image(read_image(filename))
plt.show()