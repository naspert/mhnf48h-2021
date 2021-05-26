import csv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    """manage.py import_users --csv='/Users/user/accounts.csv' --encoding='iso-8859-1'"""
    help = 'Imports users based on a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv',
            action='store',
            dest='file',
            help='File path of CSV containing users list'
        )

        parser.add_argument(
            '--encoding',
            action='store',
            dest='encoding',
            help='encoding of file'
        )

    def handle(self, *args, **options):
        User = get_user_model()

        if options['file']:
            with open(options['file'], encoding=options.get('encoding', 'utf-8')) as csvfile:
                reader = csv.DictReader(csvfile)
                created_users = existing_users = errors = 0
                users_with_errors = []
                for row in reader:
                    if row['username'] and row['email']:
                        try:
                            user, created = User.objects.get_or_create(
                                username=row['username'], email=row['email'])
                            if created:
                                user.first_name = row.get('first_name')
                                user.last_name = row.get('last_name')
                                user.set_password(row['password'])
                                user.is_active = True
                                user.save()
                                created_users += 1
                            else:
                                existing_users += 1
                            print('{0} - {1}'.format(row['username'], 'Created' if created else 'Exist'))
                        except Exception as e:
                            errors += 1
                            users_with_errors.append(row['username'])
                            self.stdout.write(self.style.ERROR(e))
                self.stdout.write(self.style.SUCCESS(
                    'Successfully imported {0} users, '
                    '{1} already exist, {2} users with errors'.format(
                        created_users,
                        existing_users,
                        errors
                    ))
                )
                if users_with_errors:
                    print('Users with errors: {0}'.format(','.join(users_with_errors)))
        else:
            self.stdout.write(self.style.ERROR('No file provided'))