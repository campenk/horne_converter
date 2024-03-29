from django.core.management import BaseCommand

from app.models import Item, ItemCategory


class Command(BaseCommand):
    help = 'Add animals to the Item class'

    def handle(self, *args, **options):
        #  standard unit is grams
        item_weights = [
            {'itemName': 'Salt grain', 'itemMeasurement': 0.0005, 'itemCategory': 'Food'},
            {'itemName': 'Feather', 'itemMeasurement': 0.0082, 'itemCategory': 'Nature'},
            {'itemName': 'Ant', 'itemMeasurement': 0.001, 'itemCategory': 'Insect'},
            {'itemName': 'Paperclip', 'itemMeasurement': 1, 'itemCategory': 'Stationery'},
            {'itemName': 'Pencil', 'itemMeasurement': 10, 'itemCategory': 'Stationery'},
            {'itemName': 'Apple', 'itemMeasurement': 150, 'itemCategory': 'Fruit'},
            {'itemName': 'Smartphone', 'itemMeasurement': 200, 'itemCategory': 'Electronics'},
            {'itemName': 'Soda can', 'itemMeasurement': 355, 'itemCategory': 'Food'},
            {'itemName': 'Laptop', 'itemMeasurement': 2000, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Dog', 'itemMeasurement': 5000, 'itemCategory': 'Household Items'},
            {'itemName': 'Watermelon', 'itemMeasurement': 8000, 'itemCategory': 'Fruit'},
            {'itemName': 'Car Tire', 'itemMeasurement': 10000, 'itemCategory': 'Automobile'},
            {'itemName': 'Elephant', 'itemMeasurement': 5000000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Aircraft', 'itemMeasurement': 5670000, 'itemCategory': 'Transportation'},
            {'itemName': 'Adult Human', 'itemMeasurement': 70000, 'itemCategory': 'Human'},
            {'itemName': 'Blue Whale', 'itemMeasurement': 108000000, 'itemCategory': 'Marine Life'},
            {'itemName': 'Small Car', 'itemMeasurement': 1500000, 'itemCategory': 'Automobile'},
            {'itemName': 'Motorcycle', 'itemMeasurement': 200000, 'itemCategory': 'Transportation'},
            {'itemName': 'Baseball', 'itemMeasurement': 145, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Basketball', 'itemMeasurement': 600, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Lion', 'itemMeasurement': 420000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Elephant', 'itemMeasurement': 2500000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Laptop Bag', 'itemMeasurement': 1000, 'itemCategory': 'Electronics'},
            {'itemName': 'Large Truck', 'itemMeasurement': 10000000, 'itemCategory': 'Automobile'},
            {'itemName': 'Adult Giraffe', 'itemMeasurement': 1200000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Human Brain', 'itemMeasurement': 1400, 'itemCategory': 'Human'},
            {'itemName': 'Backpack', 'itemMeasurement': 1000, 'itemCategory': 'Household Items'},
            {'itemName': 'Desktop Computer', 'itemMeasurement': 10000, 'itemCategory': 'Electronics'},
            {'itemName': 'Small TV', 'itemMeasurement': 5000, 'itemCategory': 'Electronics'},
            {'itemName': 'Soccer Ball', 'itemMeasurement': 410, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Tiger', 'itemMeasurement': 300000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Rhino', 'itemMeasurement': 2300000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Boat', 'itemMeasurement': 1500000, 'itemCategory': 'Transportation'},
            {'itemName': 'Empty Coffee Cup', 'itemMeasurement': 200, 'itemCategory': 'Household Items'},
            {'itemName': 'Car Battery', 'itemMeasurement': 15000, 'itemCategory': 'Automobile'},
            {'itemName': 'Adult Hippo', 'itemMeasurement': 1500000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Avocado', 'itemMeasurement': 150, 'itemCategory': 'Food'},
            {'itemName': 'Motorcycle Helmet', 'itemMeasurement': 1000, 'itemCategory': 'Accessories'},
            {'itemName': 'Large Pumpkin', 'itemMeasurement': 5000, 'itemCategory': 'Food'},
            {'itemName': 'Desktop Monitor', 'itemMeasurement': 5000, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Cat', 'itemMeasurement': 4000, 'itemCategory': 'Household Items'},
            {'itemName': 'Adult Kangaroo', 'itemMeasurement': 55000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Goldfish', 'itemMeasurement': 15, 'itemCategory': 'Pets'},
            {'itemName': 'Smartphone Charger', 'itemMeasurement': 100, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Backpack', 'itemMeasurement': 500, 'itemCategory': 'Household Items'},
            {'itemName': 'CD', 'itemMeasurement': 16, 'itemCategory': 'Electronics'},
            {'itemName': 'Lightbulb', 'itemMeasurement': 50, 'itemCategory': 'Electronics'},
            {'itemName': 'Standard Refrigerator', 'itemMeasurement': 150000, 'itemCategory': 'Household Items'},
            {'itemName': 'Baseball Cap', 'itemMeasurement': 100, 'itemCategory': 'Accessories'},
            {'itemName': 'Tennis Racket', 'itemMeasurement': 300, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Rabbit', 'itemMeasurement': 2000, 'itemCategory': 'Pets'},
            {'itemName': 'Chocolate Bar', 'itemMeasurement': 100, 'itemCategory': 'Food'},
            {'itemName': 'Adult Polar Bear', 'itemMeasurement': 450000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Water Bottle', 'itemMeasurement': 500, 'itemCategory': 'Household Items'},
            {'itemName': 'Average Car', 'itemMeasurement': 1500000, 'itemCategory': 'Automobile'},
            {'itemName': 'Fire Extinguisher', 'itemMeasurement': 5000, 'itemCategory': 'Safety Equipment'},
            {'itemName': 'Small Plant', 'itemMeasurement': 500, 'itemCategory': 'Nature'},
            {'itemName': 'Kitchen Blender', 'itemMeasurement': 5000, 'itemCategory': 'Household Items'},
            {'itemName': 'Adult Kangaroo', 'itemMeasurement': 55000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Notebook', 'itemMeasurement': 200, 'itemCategory': 'Stationery'},
            {'itemName': 'Tablet', 'itemMeasurement': 500, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Lemon', 'itemMeasurement': 100, 'itemCategory': 'Food'},
            {'itemName': 'Adult Gorilla', 'itemMeasurement': 160000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Ostrich', 'itemMeasurement': 145000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Chimpanzee', 'itemMeasurement': 40000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Chicken Egg', 'itemMeasurement': 50, 'itemCategory': 'Food'},
            {'itemName': 'Compact Mirror', 'itemMeasurement': 100, 'itemCategory': 'Accessories'},
            {'itemName': 'Straw Hat', 'itemMeasurement': 150, 'itemCategory': 'Clothing'},
            {'itemName': 'Small Pinecone', 'itemMeasurement': 5, 'itemCategory': 'Nature'},
            {'itemName': 'Adult Sperm Whale', 'itemMeasurement': 45000000, 'itemCategory': 'Wildlife'},
            {'itemName': 'Human Lung', 'itemMeasurement': 1300, 'itemCategory': 'Human'},

        ]

        for item in item_weights:
            item_category, _ = ItemCategory.objects.get_or_create(item_category=item['itemCategory'])
            item = Item(
                item_name=item['itemName'],
                item_measurement=item['itemMeasurement'],
                item_category=item_category,
                measurement_type="WE"
            )
            item.save()

        #  standard unit is metres
        items_lengths = [
            {'itemName': 'Salt Grain', 'itemMeasurement': 0.0005, 'itemCategory': 'Food'},
            {'itemName': 'Ant', 'itemMeasurement': 0.005, 'itemCategory': 'Insect'},
            {'itemName': 'Paperclip', 'itemMeasurement': 0.035, 'itemCategory': 'Stationery'},
            {'itemName': 'Pencil', 'itemMeasurement': 0.19, 'itemCategory': 'Stationery'},
            {'itemName': 'Apple', 'itemMeasurement': 0.08, 'itemCategory': 'Fruit'},
            {'itemName': 'Smartphone', 'itemMeasurement': 0.15, 'itemCategory': 'Electronics'},
            {'itemName': 'Soda Can', 'itemMeasurement': 0.13, 'itemCategory': 'Food'},
            {'itemName': 'Laptop', 'itemMeasurement': 0.35, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Dog', 'itemMeasurement': 0.40, 'itemCategory': 'Household Items'},
            {'itemName': 'Watermelon', 'itemMeasurement': 0.25, 'itemCategory': 'Fruit'},
            {'itemName': 'Car Tire', 'itemMeasurement': 0.63, 'itemCategory': 'Automobile'},
            {'itemName': 'Elephant', 'itemMeasurement': 80.00, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Human', 'itemMeasurement': 1.70, 'itemCategory': 'Human'},
            {'itemName': 'Blue Whale', 'itemMeasurement': 30.00, 'itemCategory': 'Marine Life'},
            {'itemName': 'Small Car', 'itemMeasurement': 4.00, 'itemCategory': 'Automobile'},
            {'itemName': 'Motorcycle', 'itemMeasurement': 2.00, 'itemCategory': 'Transportation'},
            {'itemName': 'Baseball', 'itemMeasurement': 0.075, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Basketball', 'itemMeasurement': 0.24, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Lion', 'itemMeasurement': 2.43, 'itemCategory': 'Wildlife'},
            {'itemName': 'Baby Elephant', 'itemMeasurement': 0.96, 'itemCategory': 'Wildlife'},
            {'itemName': 'Laptop Bag', 'itemMeasurement': 0.50, 'itemCategory': 'Electronics'},
            {'itemName': 'Adult Giraffe', 'itemMeasurement': 5.20, 'itemCategory': 'Wildlife'},
            {'itemName': 'Human Brain', 'itemMeasurement': 0.15, 'itemCategory': 'Human'},
            {'itemName': 'Backpack', 'itemMeasurement': 0.50, 'itemCategory': 'Household Items'},
            {'itemName': 'Desktop Computer', 'itemMeasurement': 0.45, 'itemCategory': 'Electronics'},
            {'itemName': 'Small TV', 'itemMeasurement': 0.25, 'itemCategory': 'Electronics'},
            {'itemName': 'Soccer Ball', 'itemMeasurement': 0.22, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Tiger', 'itemMeasurement': 2.50, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Rhino', 'itemMeasurement': 3.5, 'itemCategory': 'Wildlife'},
            {'itemName': 'Coffee Cup', 'itemMeasurement': 0.12, 'itemCategory': 'Household Items'},
            {'itemName': 'Canoe', 'itemMeasurement': 4.60, 'itemCategory': 'Transportation'},
            {'itemName': 'Car Battery', 'itemMeasurement': 0.50, 'itemCategory': 'Automobile'},
            {'itemName': 'Adult Hippo', 'itemMeasurement': 4.70, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Avocado', 'itemMeasurement': 0.12, 'itemCategory': 'Food'},
            {'itemName': 'Large Pumpkin', 'itemMeasurement': 0.50, 'itemCategory': 'Food'},
            {'itemName': 'Desktop Monitor', 'itemMeasurement': 0.40, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Cat', 'itemMeasurement': 0.40, 'itemCategory': 'Household Items'},
            {'itemName': 'Goldfish', 'itemMeasurement': 0.10, 'itemCategory': 'Pets'},
            {'itemName': 'Smartphone Charger', 'itemMeasurement': 0.06, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Backpack', 'itemMeasurement': 0.30, 'itemCategory': 'Household Items'},
            {'itemName': 'CD', 'itemMeasurement': 0.12, 'itemCategory': 'Electronics'},
            {'itemName': 'Lightbulb', 'itemMeasurement': 0.12, 'itemCategory': 'Electronics'},
            {'itemName': 'Fridge', 'itemMeasurement': 1.80, 'itemCategory': 'Household Items'},
            {'itemName': 'Baseball Cap', 'itemMeasurement': 0.20, 'itemCategory': 'Accessories'},
            {'itemName': 'Tennis Racket', 'itemMeasurement': 0.70, 'itemCategory': 'Sports Equipment'},
            {'itemName': 'Adult Rabbit', 'itemMeasurement': 0.40, 'itemCategory': 'Pets'},
            {'itemName': 'Chocolate Bar', 'itemMeasurement': 0.18, 'itemCategory': 'Food'},
            {'itemName': 'Adult Polar Bear', 'itemMeasurement': 3.00, 'itemCategory': 'Wildlife'},
            {'itemName': 'Water Bottle', 'itemMeasurement': 0.18, 'itemCategory': 'Household Items'},
            {'itemName': 'Average Car', 'itemMeasurement': 4.00, 'itemCategory': 'Automobile'},
            {'itemName': 'Fire Extinguisher', 'itemMeasurement': 0.40, 'itemCategory': 'Safety Equipment'},
            {'itemName': 'Small Plant', 'itemMeasurement': 0.20, 'itemCategory': 'Nature'},
            {'itemName': 'Kitchen Blender', 'itemMeasurement': 0.40, 'itemCategory': 'Household Items'},
            {'itemName': 'Adult Kangaroo', 'itemMeasurement': 2.00, 'itemCategory': 'Wildlife'},
            {'itemName': 'Small Notebook', 'itemMeasurement': 0.15, 'itemCategory': 'Stationery'},
            {'itemName': 'Tablet', 'itemMeasurement': 0.20, 'itemCategory': 'Electronics'},
            {'itemName': 'Small Lemon', 'itemMeasurement': 0.10, 'itemCategory': 'Food'},
            {'itemName': 'Adult Gorilla', 'itemMeasurement': 1.70, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Ostrich', 'itemMeasurement': 2.10, 'itemCategory': 'Wildlife'},
            {'itemName': 'Adult Chimpanzee', 'itemMeasurement': 1.50, 'itemCategory': 'Wildlife'},
            {'itemName': 'Chicken Egg', 'itemMeasurement': 0.05, 'itemCategory': 'Food'},
            {'itemName': 'Compact Mirror', 'itemMeasurement': 0.10, 'itemCategory': 'Accessories'},
            {'itemName': 'Straw Hat', 'itemMeasurement': 0.30, 'itemCategory': 'Clothing'},
            {'itemName': 'Small Pinecone', 'itemMeasurement': 0.05, 'itemCategory': 'Nature'},
            {'itemName': 'Adult Sperm Whale', 'itemMeasurement': 18.00, 'itemCategory': 'Wildlife'},
            {'itemName': 'Human Lung', 'itemMeasurement': 0.20, 'itemCategory': 'Human'},
        ]

        for item in items_lengths:
            item_category, _ = ItemCategory.objects.get_or_create(item_category=item['itemCategory'])
            item = Item(
                item_name=item['itemName'],
                item_measurement=item['itemMeasurement'],
                item_category=item_category,
                measurement_type= "LE"
            )
            item.save()

        self.stdout.write(self.style.SUCCESS('Successfully added all items to Item class.'))


