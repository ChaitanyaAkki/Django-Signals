import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal proving signals are synchronous
@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulating a delay
    print("Signal handler finished")

# Signal proving signals run in the same thread
@receiver(post_save, sender=User)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Signal proving signals run in the same transaction
@receiver(post_save, sender=User)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"Inside signal - User exists: {User.objects.filter(id=instance.id).exists()}")