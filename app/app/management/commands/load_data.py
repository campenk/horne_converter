from django.core.management import BaseCommand

from app.models import Item, ItemCategory, MeasurementType


class Command(BaseCommand):
    help = 'Add animals to the Item class'

    def handle(self, *args, **options):
        animals = [
            {'itemName': 'African Elephant', 'itemMeasurement': 600},
            {'itemName': 'Anaconda', 'itemMeasurement': 550},
            {'itemName': 'Blue Whale', 'itemMeasurement': 2500},
            {'itemName': 'Cheetah', 'itemMeasurement': 160},
            {'itemName': 'Chimpanzee', 'itemMeasurement': 100},
            {'itemName': 'Cobra', 'itemMeasurement': 250},
            {'itemName': 'Crocodile', 'itemMeasurement': 450},
            {'itemName': 'Dolphin', 'itemMeasurement': 300},
            {'itemName': 'Eagle', 'itemMeasurement': 75},
            {'itemName': 'Elephant Seal', 'itemMeasurement': 500},
            {'itemName': 'Flamingo', 'itemMeasurement': 145},
            {'itemName': 'Giraffe', 'itemMeasurement': 550},
            {'itemName': 'Gorilla', 'itemMeasurement': 160},
            {'itemName': 'Great White Shark', 'itemMeasurement': 600},
            {'itemName': 'Grey Wolf', 'itemMeasurement': 130},
            {'itemName': 'Grizzly Bear', 'itemMeasurement': 220},
            {'itemName': 'Hippopotamus', 'itemMeasurement': 400},
            {'itemName': 'Jaguar', 'itemMeasurement': 180},
            {'itemName': 'Kangaroo', 'itemMeasurement': 100},
            {'itemName': 'King Cobra', 'itemMeasurement': 350},
            {'itemName': 'Lion', 'itemMeasurement': 190},
            {'itemName': 'Moose', 'itemMeasurement': 280},
            {'itemName': 'Orangutan', 'itemMeasurement': 140},
            {'itemName': 'Ostrich', 'itemMeasurement': 250},
            {'itemName': 'Penguin', 'itemMeasurement': 80},
            {'itemName': 'Polar Bear', 'itemMeasurement': 290},
            {'itemName': 'Python', 'itemMeasurement': 400},
            {'itemName': 'Rhinoceros', 'itemMeasurement': 350},
            {'itemName': 'Siberian Tiger', 'itemMeasurement': 280},
            {'itemName': 'Snow Leopard', 'itemMeasurement': 130},
            # Repeat entries for demonstration purposes
            {'itemName': 'Anaconda', 'itemMeasurement': 550},
            {'itemName': 'Blue Whale', 'itemMeasurement': 2500},
            {'itemName': 'Cheetah', 'itemMeasurement': 160},
            {'itemName': 'Chimpanzee', 'itemMeasurement': 100},
            {'itemName': 'Cobra', 'itemMeasurement': 250},
            {'itemName': 'Crocodile', 'itemMeasurement': 450},
            {'itemName': 'Dolphin', 'itemMeasurement': 300},
            {'itemName': 'Eagle', 'itemMeasurement': 75},
            {'itemName': 'Elephant Seal', 'itemMeasurement': 500},
            {'itemName': 'Flamingo', 'itemMeasurement': 145},
            {'itemName': 'Giraffe', 'itemMeasurement': 550},
            {'itemName': 'Gorilla', 'itemMeasurement': 160},

        ]

        for animal in animals:
            item = Item(
                itemName=animal['itemName'],
                itemCategory=ItemCategory.objects.get(itemCategory="animal"),
                itemMeasurement=animal['itemMeasurement'],
                measurementType=MeasurementType.objects.get(measurementType="length")
            )
            item.save()
            self.stdout.write(f'Successfully added {animal["itemName"]} to Item class.')

        self.stdout.write(self.style.SUCCESS('Successfully added all animals to Item class.'))


