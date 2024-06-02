from django.db import migrations

def set_default_bookshelf(apps, schema_editor):
    Profile = apps.get_model('app_book', 'Profile')
    Bookshelf = apps.get_model('app_book', 'Bookshelf')

    for profile in Profile.objects.all():
        if not profile.bookshelf:
            bookshelf = Bookshelf.objects.create(profile=profile)
            profile.bookshelf = bookshelf
            profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0011_alter_profile_bookshelf'),
    ]

    operations = [
        migrations.RunPython(set_default_bookshelf),
    ]