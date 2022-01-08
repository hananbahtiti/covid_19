from django.db import models
from django.conf import settings

def get_test_img(instance, filename):
	ID = instance.user.email.replace('@', 'ss')
	return 'pic_folder/{0}/tests/{1}'.format(ID, filename)

class Imag(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='image_user')
	Image = models.ImageField(upload_to = get_test_img)

