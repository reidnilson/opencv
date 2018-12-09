import argparse
import cv2
parser = argparse.ArgumentParser()

parser.add_argument('--path', default='./image.jpg', help='Image path.')

params = parser.parse_args()

img = cv2.imread(params.path)

assert img is not None 

print('read {}'.format(params.path))
print('shape:',img.shape)
print('dtype:',img.dtype)
