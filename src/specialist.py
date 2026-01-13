import numpy as np
import cv2

class SaltPepperSpecialist:
    """
    Encapsulates domain knowledge about Salt-and-Pepper noise.
    """
    def __init__(self):
        self.low_threshold = 10
        self.high_threshold = 245
        
    def perfect_detection(self, img):
        """
        Oracle-level detection based on extreme value assumption.
        Returns a binary mask where 1 indicates noise.
        """
        if img.dtype != np.uint8:
            img = img.astype(np.uint8)
            
        mask = (img <= self.low_threshold) | (img >= self.high_threshold)
        return mask.astype(np.uint8)
    
    def fast_median_repair(self, img, mask):
        """
        Sparse restoration: only process masked pixels using local median.
        Optimized with padding for boundary handling.
        """
        h, w = img.shape
        result = img.copy()
        coords = np.argwhere(mask == 1)
        
        # Padding to handle boundaries without checks inside loop
        pad = 2
        padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)
        
        for y, x in coords:
            # Map to padded coordinates
            py, px = y + pad, x + pad
            # 5x5 neighborhood
            neighborhood = padded[py-2:py+3, px-2:px+3]
            result[y, x] = np.median(neighborhood)
            
        return result

    def get_neighborhood(self, img, x, y, size):
        """
        Safe neighborhood extraction with boundary handling.
        """
        h, w = img.shape
        half = size // 2
        
        xs = max(0, x - half)
        xe = min(h, x + half + 1)
        ys = max(0, y - half)
        ye = min(w, y + half + 1)
        
        return img[xs:xe, ys:ye]
