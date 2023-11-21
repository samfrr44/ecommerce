from services.customerservice import CustomerService
from sqlalchemy.orm.exc import UnmappedInstanceError
from exceptions.validationexceptions import ValidationException

service = CustomerService()
# dict = {
#     "name": "",
#     "address": "",
#     "city": "metrocity",
#     "zipcode": 12345,
#     "country": "narnia",
#     "phone": "1234567890",
# }
# try:
#     uuid = service.save(dict)
# except ValidationException as e:
#     print(e.errors)
# else:
#     print("success!!")
dict = service.findById("566fb480-778e-11ee-8bbe-000000000000")
print(dict)
# try:
#     service.delete("719696e2-43bb-4b98-9ce3-93902953d34d")
# except UnmappedInstanceError as e:
#     print(e)
# dict = service.findAll()
# print(dict)
