from django.db import models
from django.conf import settings


class Category(models.Model):
    title= models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural= "Catogories"# when we see in admin pannel it shows every model with 's but when can declare by saying this 
        
class Product(models.Model):
    mainimage= models.ImageField(upload_to='Products')
    name=models.CharField(max_length=264)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    preview_text=models.TextField(max_length=200,verbose_name='Preview Text')
    detail_text=models.TextField(max_length=1000,verbose_name='Description')
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return  self.name
    class Meta:
        ordering=['-created_date']
