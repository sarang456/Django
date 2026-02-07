from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=128)
    user_phone = models.IntegerField()
    created_at = models.DateField()

    class Meta:
        db_table = "user"

class item(models.Model):

    status = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('recovered', 'Recovered')
    ]

    item_title = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    item_description = models.TextField()
    # item_image = models.ImageField(upload_to='items/')
    item_status = models.CharField(choices=status, default='Lost')

    class Meta:
        db_table = "items"


class lost_report(models.Model):

    status_lost = [
        ('open', 'Open'),
        ('recovered', 'Recovered')
    ]

    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    lost_date = models.DateField()
    lost_time = models.TimeField()
    status_lost = models.CharField(choices=status_lost, default="Open")

    class Meta:
        db_table = "lost_reports"


class found_report(models.Model):

    status_found = [
        ('available', 'Available'),
        ('claim', 'Claim')
    ]

    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    found_date = models.DateField()
    status_found = models.CharField(choices=status_found, default="Available", max_length=20)

    class Meta:
        db_table = "found_reports"


class message(models.Model):
    sender_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name="sender")
    receiver_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name="receiver")
    content = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "messages"


class notification(models.Model):

    notification_type = [
        ('match', 'Match'),
        ('message', 'Message'),
        ('status', 'Status')
    ]

    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(choices=notification_type, max_length=20)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField()


    class Meta:
        db_table = "notifications"


class rating(models.Model):
    from_user_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name="Rating_given")
    to_user_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name="Rating_receive")
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField()


    class Meta:
        db_table = "ratings"