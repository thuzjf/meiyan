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


def detect_mopi(ori_array, im_array):
  """
  detect whether mopi has started, based on the fact that mopi will smooth the picture
   and it's gradients at sharp points will get turned down.
  :param ori_array:  the 2d nunpy array for original image
  :param mopi_array:  the 2d numpy array for processed image
  :return:
  """
  grad_ori_x, grad_ori_y = np.gradient(ori_array)
  grad_ori = np.sqrt(grad_ori_x**2 + grad_ori_y**2).flatten()
  grad_mopi_x, grad_mopi_y = np.gradient(im_array)
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


def detect_dayan(ori_array, im_array):
  pass
  
  
  

if __name__ == "__main__":
  im_dir = "./resource"
  filelist =[f for f in os.listdir(im_dir) if 'png' in f]
  ori_img_name = "ori.png"
  ori_path = os.path.join(im_dir, ori_img_name)
  ori_im = Image.open(ori_path).convert('L')
  ori_array = np.array(ori_im)

  #begin test
  filelist.remove(ori_img_name)
  for item in filelist:
    im_path = os.path.join(im_dir, item)
    im = Image.open(im_path).convert('L')
    im_array = np.array(im)
    # test mopi
    if "mopi" in item:
      state_mp, increment = detect_mopi(ori_array, im_array)
      if state_mp:
        print "successfully detected mopi! detected low gradient increment is {:.3f}".format(increment)
      else:
        print "failed to detect mopi! detected low gradient increment is {:.3f}".format(increment)

    if "dayan" in item:
      detect_dayan(ori_img_name, im_array)
      pass
    
    if "hongrun" in item:
      pass
    
    if "meibai" in item:
      pass
    
    if "saihong" in item:
      pass
    
    if "shoulian" in item:
      pass

  print "all tests finished!"

