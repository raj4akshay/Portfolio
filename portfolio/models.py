from django.db import models


# Create your models here.
class Cards(models.Model):
    card_title = models.CharField(max_length=20)
    card_description = models.TextField()
    card_image = models.ImageField(upload_to='card_pics', default='')

    def __str__(self):
        return self.card_title


class Image(models.Model):
    logo_image = models.ImageField(upload_to='home_pic', default='')
    aki_pic = models.ImageField(upload_to='home_pic', default='')
    aki_pic_title = models.CharField(max_length=20, default='my_pics')
    aki_background = models.ImageField(upload_to='home_pic', default='')

    def __str__(self):
        return self.aki_pic_title


class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='gallery_pic', default='')
    gallery_img_title = models.CharField(max_length=20)
    gallery_img_about = models.TextField()

    def __str__(self):
        return self.gallery_img_title


class Project(models.Model):
    project_image = models.ImageField(upload_to='project_pic', default='')
    project_title = models.CharField(max_length=15)
    project_description = models.TextField()
    project_link = models.TextField()

    def __str__(self):
        return self.project_title


class Certificate(models.Model):
    certificate_image = models.ImageField(upload_to='certificate_pic', default='')
    certificate_title = models.CharField(max_length=20)
    certificate_description = models.TextField()

    def __str__(self):
        return self.certificate_title


class About(models.Model):
    about_title = models.CharField(max_length=20)
    about_image = models.ImageField(upload_to='home_pic')
    about_description = models.TextField()

    def __str__(self):
        return self.about_title
