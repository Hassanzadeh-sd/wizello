from core.models import BaseModel, models


class Organization(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ['-created']

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse("organization_detail", kwargs={"pk": self.pk})
