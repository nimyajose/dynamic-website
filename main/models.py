from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/',default='static/images/b.jpg')
    title = models.CharField(max_length=255, default="Welcome to Pulari Australia")
    subtitle = models.CharField(max_length=255, default="Building a Stronger Community Together")

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="About Pulari")
    description = models.TextField(default="Pulari is a registered Non-Profit Organization under the Consumer Affairs of Victoria, Australia.")
    image = models.ImageField(upload_to='about_us/', default='static/images/about.jpg')
    points = models.TextField(help_text="Enter bullet points separated by '|' (pipe symbol)", default="Discover and nurture community talents.|Promote Indian values, culture, and arts to future generations.|Organize events with local and international talents.|Raise funds for charitable causes.")
    extra_text = models.TextField(blank=True, null=True)

    def get_points(self):
        return self.points.split("|")

    def __str__(self):
        return self.title
# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    date=models.DateTimeField()
    image=models.ImageField(upload_to='events/',blank=True, null=True)

    def __str__(self):
        return self.title