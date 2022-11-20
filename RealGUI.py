from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np

def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.bilateralFilter(gray, d=7, sigmaColor=200,sigmaSpace=200)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges

def edge_enhancement(img, nIteration):
  for i in range(nIteration) :
    size = (3, 3)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    img = cv2.erode(img, kernel)
    if(i == nIteration - 1) :
      return img

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.001)
  attempts = 20

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

line_size = 7
blur_value = 5
total_color = 15

def select_image():
    global panelA, panelB
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)
        edges = edge_mask(blurred, line_size, blur_value)
        quanti = color_quantization(blurred, total_color)
        cartooned = cv2.bitwise_and(quanti, quanti, mask=edges)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cartooned = cv2.cvtColor(cartooned, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        cartooned = Image.fromarray(cartooned)
        image = ImageTk.PhotoImage(image)
        cartooned = ImageTk.PhotoImage(cartooned)
        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            panelB = Label(image=cartooned)
            panelB.image = cartooned
            panelB.pack(side="right", padx=10, pady=10)
        else:
            panelA.configure(image=image)
            panelB.configure(image=cartooned)
            panelA.image = image
            panelB.image = cartooned

root = Tk()
panelA = None
panelB = None
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
root.mainloop()

