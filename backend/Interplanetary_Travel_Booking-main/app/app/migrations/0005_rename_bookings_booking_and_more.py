# Generated by Django 4.2.4 on 2023-08-18 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_paymentmethods_user_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookings',
            new_name='Booking',
        ),
        migrations.RenameModel(
            old_name='BookingStoppings',
            new_name='Bookingtoppings',
        ),
        migrations.RenameModel(
            old_name='FlightSchedules',
            new_name='FlightSchedule',
        ),
        migrations.RenameModel(
            old_name='PaymentMethods',
            new_name='PaymentMethod',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]