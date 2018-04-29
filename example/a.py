 # -*- coding: UTF-8 -*-  
def A():
	print("aaaaaa")


def load(f, as_grey=False):
    """Load an image file located in the data directory.

    Parameters
    ----------
    f : string
        File name.
    as_grey : bool, optional
        Convert to greyscale.

    Returns
    -------
    img : ndarray
        Image loaded from ``skimage.data_dir``.
    """
    use_plugin('pil')
    return imread(_os.path.join(data_dir, f), as_grey=as_grey)


def erzhi(im,threshold):


         pixdata=im.load()
         #pixdata=np.array(Image.open("/Users/wangyunqi/Desktop/丽丽毕设/2.bmp").convert('L'))

         w,h=im.size

         for j in range(h):

                   for i in range(w):

                            if pixdata[i,j]<threshold:

                                     pixdata[i,j]=0

                            else:

                                     pixdata[i,j]=255

         return im



'''

def jietu(im,x,y,w,h):
	for i in range(2,6):
		box=(x,y,w,h)
		im=


'''


