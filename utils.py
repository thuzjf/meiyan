# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 22:00
# @Author  : jf.zhang
# @File    : utils.py
# @Software: PyCharm


import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def detect_mopi(ori_array, mopi_array):
  """
  detect whether mopi has started, based on the fact that mopi will smooth the picture
   and it's gradients at sharp points will get turned down.
  :param ori_array:  the 2d nunpy array for original image
  :param mopi_array:  the 2d numpy array for processed image
  :return:
  """
  grad_ori_x, grad_ori_y = np.gradient(ori_array)
  grad_ori = np.sqrt(grad_ori_x**2 + grad_ori_y**2).flatten()
  grad_mopi_x, grad_mopi_y = np.gradient(mopi_array)
  grad_mopi = np.sqrt(grad_mopi_x**2 + grad_mopi_y**2).flatten()

  grad_ori_low = np.zeros_like(grad_ori)
  grad_ori_low[grad_ori<50] = 1
  grad_mopi_low = np.zeros_like(grad_mopi)
  grad_mopi_low[grad_mopi<50] = 1
  
  increment = 1 * grad_mopi_low.sum() / grad_ori_low.sum()
  if increment > 1.25:
    return True, increment
  else:
    return False, increment



if __name__ == "__main__":
  im_dir = "./resource"
  ori_path = os.path.join(im_dir, '0.png')
  shoulian_path = os.path.join(im_dir, 'shoulian_max.png')
  hongrun_path = os.path.join(im_dir, "hongrun_max.png")
  mopi_path = os.path.join(im_dir, "mopi_max.png")

  ori_im = Image.open(ori_path).convert('L')
  shoulian_im = Image.open(shoulian_path).convert('L')
  mopi_im = Image.open(mopi_path).convert('L')

  ori_array = np.array(ori_im)
  shoulian_array = np.array(shoulian_im)
  mopi_array = np.array(mopi_im)

  state_mp, increment = detect_mopi(ori_array, mopi_array)
  if state_mp:
    print "mopi has successfully started! detected low gradient increment is {}",format(increment)






