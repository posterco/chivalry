from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    xp = models.IntegerField(null=True)
    level = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="categories" , null=True)
    slug = models.SlugField(unique=True , null=True , blank=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category , self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.category_name
    
class Goals(BaseModel):
    goal_name = models.CharField(max_length=300)
    goal_category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products_category")
    slug = models.SlugField(unique=True , null=True , blank=True)
    time = models.CharField(max_length=100, null=True,blank=True)
    start_date = models.DateField(blank=True , null=True)
    completed = models.BooleanField(default=False)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.goal_name)
        super(Goals , self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.goal_name
    
class UserGoals(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user')
    goals = models.ManyToManyField(Goals , related_name='user_goals')