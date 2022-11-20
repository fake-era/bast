import subprocess

from django.core.management.base import BaseCommand

from apps.user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            bashCommand = "python manage.py createsuperuser --noinput"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output)
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
