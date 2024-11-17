from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_image = models.ImageField(upload_to='faq_images/', null=True, blank=True)
    answer_image = models.ImageField(upload_to='faq_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Warning(models.Model):
    warning = models.TextField()
    solution = models.TextField()
    warning_image = models.ImageField(upload_to='warning_images/', null=True, blank=True)
    solution_image = models.ImageField(upload_to='warning_images/', null=True, blank=True)

    def __str__(self):
        return self.warning

class Error(models.Model):
    error_description = models.TextField()
    solution = models.TextField()
    error_image = models.ImageField(upload_to='error_images/', null=True, blank=True)
    solution_image = models.ImageField(upload_to='error_images/', null=True, blank=True)

    def __str__(self):
        return self.error_description