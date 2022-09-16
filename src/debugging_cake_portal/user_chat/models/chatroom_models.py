from django.db import models

# I think I need to predefine rooms just like I did with user roles.


class ChatRoom(models.Model):
    PYTHON = 1
    JAVA = 2
    DRUPAL = 3
    ANGULAR = 4
    DOJ = 5
    JOS = 6
    ROOM_CHOICES = (
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
        (DRUPAL, 'Drupal'),
        (ANGULAR, 'Angular'),
        (DOJ, 'DOJ'),
        (JOS, 'JOS')
    )

    id = models.PositiveSmallIntegerField(choices=ROOM_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()
