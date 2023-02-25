customer_records = [{"id": "34", "name": "Huxley", "age": "5"}, {"id": "12", "name": "Brock", "age": "1"}]
# customer = [c for c in customer_records if c['id'] == 7]
# print(customer_records.index(customer[0]))

# max_id = 0
# for c in customer_records:
#     if int(c['id']) > max_id:
#         max_id = int(c['id'])


customer_records[0].update(name="hello")
print(customer_records)