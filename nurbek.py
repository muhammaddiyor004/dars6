# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TD0Ok33eyFxbWjjipiq05shAaK4-Q3ji
"""

pip install opencv-python


from google.colab.patches import cv2_imshow
import cv2
picture1=cv2.imread("rasm.jpeg")
picture2=cv2.imread("rasm1.jpeg")
picture3=cv2.imread("rasm2.jpeg")
picture4=cv2.imread("rasm3.jpeg")
picture5=cv2.imread("rasm4.jpeg")
cv2_imshow(picture1)
cv2_imshow(picture2)
cv2_imshow(picture3)
cv2_imshow(picture4)
cv2_imshow(picture5)

color1=cv2.cvtColor(picture1,cv2.COLOR_BGR2GRAY)
cv2_imshow(color1)
color2=cv2.cvtColor(picture2,cv2.COLOR_BGR2GRAY)
cv2_imshow(color2)
color3=cv2.cvtColor(picture3,cv2.COLOR_BGR2GRAY)
cv2_imshow(color3)
color4=cv2.cvtColor(picture4,cv2.COLOR_BGR2GRAY)
cv2_imshow(color4)
color5=cv2.cvtColor(picture5,cv2.COLOR_BGR2GRAY)
cv2_imshow(color5)