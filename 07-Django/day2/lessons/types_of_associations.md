class Dining_Set(models.Model):
    name = models. CharField(max_length=200, default="6 PIECE SET")
    color = models. CharField(max_length=100, default="medium charcoal gray")

class Stool(models.Model) :
    length= models. PositiveIntegerField(default=2)
    width = models.PositiveIntegerField(default=1)
    dining_set = models. OneToOneField(Dining_Set, related_name="stool", on_delete=models. CASCADE) <!-- one to one  -->
    
class Chairs(models.Model) :
    height = models. PositiveIntegerField(default=3)
    escription = models. TextField(default="None")
    dining_set = models. ForeignKey(Dining_Set, on_delete=models. CASCADE, related_name="chair") <!-- many to one  -->

class Kitchen(models.Model):
    name = models. CharField(max_length="255", default="my kitchen")
    dining_sets = models.ManyToManyField(Dining_Set) | <!-- many to many -->