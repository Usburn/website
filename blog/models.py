from django.db import models

# Create your models here.

class Reader(models.Model):
    Last_name = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Comment = models.TextField( null=True , blank=True)
    
    def __str__(self):
        return f"{self.Last_name} {self.First_name} {self.Email}" 
    
    
class Author(models.Model):
    Last_name = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.Last_name} {self.First_name}"
    
    
    
    

class Project(models.Model):
    title= models.CharField(max_length=100)
    excerpt = models.CharField(max_length=400)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null= True, related_name="projects")
    
    
    def __str__(self):
        return f"{self.title} {self.date}"
    
    
  
  
class Comment(models.Model):
    Last_name = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Email = models.EmailField()
    comment = models.TextField(max_length=400)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.Last_name} {self.First_name}"
    
    
    
    


    
    
  