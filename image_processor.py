import cv2

def load_image(image_path, unchanged=False):

    flag = cv2.IMREAD_UNCHANGED if unchanged else cv2.IMREAD_COLOR
    return cv2.imread(image_path, flag)

def blend_images(image1, image2, alpha=0.5):
    beta = 1 - alpha
    gamma = 0
    return cv2.addWeighted(image1, alpha, image2, beta, gamma)