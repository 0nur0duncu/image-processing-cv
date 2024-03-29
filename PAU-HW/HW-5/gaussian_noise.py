######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import numpy as np

def gaussianGürültü(image, ortalama=0, varyans=0.05, db=0):
    """Sıfır ortalamalı ve σ^2 varyanslı Gauss gürültüsü – ki buna beyaz Gauss gürültüsü adı da verilir; Gauss olasılık yoğunluk fonksiyonundan elde edilen normal dağılıma sahip rasgele bir gürültü sürecidir, hem Gauss gürültüsü hem de belirli bir dB seviyesine sahip gürültüyü birleştirir.

    Args:
        image (numpy.array): Gürültü eklenmek istenen görüntü.
        ortalama (int, optional): Gaussian dağılımın ortalama değeri. Varsayılan değer 0'dır.
        varyans (float, optional): Gaussian dağılımın varyansı. Varsayılan değer 0.05'tir.
        db (int, optional): Gürültünün desibel (dB) seviyesi. Varsayılan değer 0'dır.

    Returns:
        numpy.array: Gürültü eklenmiş görüntü.
    """

    gauss_noise = np.random.normal(ortalama, varyans, image.shape)

    height, width, channel = image.shape
    signal_power = np.sum(image ** 2) / (height * width)
    noise_power = signal_power / (10 ** (db / 10))
    db_noise = np.random.normal(0, np.sqrt(noise_power), (height, width, channel))

    noise = image / 255 + gauss_noise + db_noise

    return noise

