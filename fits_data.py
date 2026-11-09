import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import AsinhStretch, ImageNormalize, PercentileInterval

'''
url = "https://data.astropy.org/tutorials/FITS-images/HorseHead.fits"
filename = download_file(url, cache=True, timeout=120)
# image = fits.getdata(filename)
'''

with fits.open("./HorseHead.fits") as hdul:
    image = hdul[0].data

norm = ImageNormalize(image, interval=PercentileInterval(99.5), stretch=AsinhStretch())
plt.imshow(image, origin="lower", cmap="gray", norm=norm)
plt.colorbar(label="Pixel value")
plt.show()
