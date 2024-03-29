from core.models import BaseModel, models
from django.contrib.auth.models import User
from organization.models import Organization
from django.contrib.auth.models import AbstractUser


class Employee(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="employee")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="employee")
    POSITION_TYPE = (
        ('M', "Manager"),
        ('EO', "Employee Organization"),
        ('E', "Employee"),
    )
    position = models.CharField(
        max_length=15, choices=POSITION_TYPE, default="E")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.user.username

#    def get_absolute_url(self):
#        return reverse("employee_detail", kwargs={"pk": self.pk})
