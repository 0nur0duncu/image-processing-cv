######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import numpy as np

def tuzBiberGurultusu(image, s_vs_p=0.5, amount=0.04):
    """Darbe gürültüsü, görüntü içerisindeki bazı piksellerin değerini rasgele değiştirir. Darbe gürültüsüne aynı zamanda tuz-biber gürültüsü adı da verilir.

    Args:
        image (numpy.array): Gürültü eklenmek istenen görüntü.
        s_vs_p (float, optional): Tuz ve biber miktarı arasındaki oran. Varsayılan değer 0.5'tir.
        amount (float, optional): Gürültü miktarı. Varsayılan değer 0.04'tür.

    Returns:
        numpy.array: Gürültü eklenmiş görüntü.
    """
    image = image / 255
    gurultulu = np.copy(image)

    num_tuz = int(np.ceil(amount * image.size * s_vs_p))
    tuz_konumlar = [np.random.randint(0, i-1, num_tuz) for i in image.shape]
    gurultulu[tuz_konumlar] = 1

    num_biber = int(np.ceil(amount * image.size * s_vs_p))
    biber_konumlar = [np.random.randint(0, i-1, num_biber) for i in image.shape]
    gurultulu[biber_konumlar] = 0

    return gurultulu
