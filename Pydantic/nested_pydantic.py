from pydantic import BaseModel
from typing import List,Dict,Optional, Annotated

class Address(BaseModel):
  city: str
  pincode: int
  sector: str

class Patient(BaseModel):
  name: str
  age: int
  address: Address

address_dict = {'city':'Mumbai','pincode':400037,'sector':'C3'}

address1 = Address(**address_dict)

Patient_dict = {'name':'shubham','age':24,'address':address1}

final_patient = Patient(**Patient_dict)

print(final_patient.name)
print(final_patient.age)
print(final_patient.address.city)
print(final_patient.address.pincode)
