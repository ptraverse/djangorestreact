from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import struct
import PIL.Image
import scipy
import scipy.misc
import scipy.cluster
import wget

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=512)
    primary_color = models.CharField(max_length=6)
    secondary_color = models.CharField(max_length=6)

# Download file, determine colors
@receiver(pre_save, sender=Image)
def my_callback(sender, instance, *args, **kwargs):
    # save file
    image = wget.download(instance.url, 'backend/backend/images/')
    # taken from http://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
    NUM_CLUSTERS = 5
    im = PIL.Image.open(image)
    im = im.resize((150, 150))  # optional, to reduce time
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])
    codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)
    vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences
    index_max = scipy.argmax(counts)  # find most frequent
    peak = codes[index_max]
    primary_color = ''.join(chr(c.astype(int)) for c in peak).encode('hex')
    instance.primary_color = primary_color
