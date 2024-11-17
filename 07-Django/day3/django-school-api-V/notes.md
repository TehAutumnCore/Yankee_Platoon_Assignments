all_students = Student.objects.all()
all_students

gary = all_students[1]
gary

gary.subjects
gary.subjects.all()

all_subjects = Subject.object.all()
all_subjects

django_subject = Subject.objects.get(subject_name='Django')
django_subject

django_subject.students
django_subject.students.all()

gary.subjects.all()
all_subjects

javascript = Subject.object.get(subject_name=Javascript)
javascript
javascript.id

gary.add_subject(3)
gary.subjects
gary.subjects.all()

html = Subject(subject_name="Html", professor="Professor Roger")
html.fullclean()
html.save()
css = Subject(subject_name="Css", professor="Professor Roger")
html.fullclean()
html.save()
react = Subject(subject_name="React", professor="Professor Roger")
html.fullclean()
html.save()

gary.add_subject(2)
gary.add_subject.remove(2)
gary.add_subject(6)
gary.add_subject.remove(6)
gary.add_subject(7)
gary.add_subject.remove(7)
gary.add_subject(8)
gary.add_subject.remove(8)


models.OneToOneField #One to one relationship
models.ForeignKey #Many to One Relationship
models.ManyToManyField #Many to One Relation