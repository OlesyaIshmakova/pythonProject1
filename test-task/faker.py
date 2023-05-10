import csv

from faker import Faker
# from faker.providers import internet
# from faker.providers.address.ru_RU import Provider as RuAddress
# from faker.providers.person.ru_RU import Provider as RuPerson

fake = Faker()
# fake.add_provider(internet)
# fake.add_provider(RuAddress)
# fake.add_provider(RuPerson)

# with open('fake.csv', 'w') as f:
#     wr = csv.writer(f, delimiter=';')
#
#     wr.writerow(['id', 'name', 'address', 'ip'])
#     for number in range(5):
#         wr.writerow([
#             number,
#             fake.name(),
#             fake.address().replace('\n', ' '),
#             fake.ipv4_public()
#         ])

with open('fake-dict-writer.csv', 'w') as f:
    fieldnames = ['id', 'name', 'address', 'ip']
    wr = csv.DictWriter(f, fieldnames=fieldnames)

    wr.writeheader()
    for number in range(5):
        wr.writerow(dict(zip(fieldnames, [
            number,
            fake.name(),
            fake.address().replace('\n', ' '),
            fake.ipv4_public()
        ]
    )))
