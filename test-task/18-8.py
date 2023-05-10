fake = Faker()
# fake.add_provider(internet)

# fake.add_provider(RuAddress)
# fake.add_provider(RuPerson)
with open('fake.csv, 'w') as f wr = csv.writer(f, delimiter=';')
[wr.writerow(['id', 'name', 'address', 'ip'])
for number in range(5):
wr. writerow([number,fake.name(),fake.address().replace('\n', ''),

fake.ipv4 public()
