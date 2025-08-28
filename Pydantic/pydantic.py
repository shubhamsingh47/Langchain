from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List,Dict,Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str,Field(max_length=50,title='Name of the patient',description="Give name bro",examples=["Amit","Jack"])]
  email: EmailStr
  age: Annotated[int,Field(gt=18,lt=40,strict=True)]
  linkedin: AnyUrl
  weight: Annotated[float,Field(default=None,description="what is the weight")]
  height: Annotated[float,Field(default=None,description="what is the height")]
  allergies: Annotated[List[str],Field(default=None,max_length=5)]
  contact_details: Dict[str,str]

  @field_validator('email')
  @classmethod
  def validation_email(cls,value):

    valid_domain = ['hdfc.com','icici.com']
    domain_name = value.split('@')[-1]

    if domain_name not in valid_domain:
      raise ValueError("Not a valid domain")
    return value

  @field_validator('name')
  @classmethod
  def transform_name(cls,value):
    return value.upper()

  @model_validator(mode='after')
  def validate_emergency(cls,model):
    if model.age > 28 and 'emergency' not in model.contact_details:
      raise ValueError("Give emergency for this age")

    return model

  @computed_field
  @property
  def calculate_BMI(self)->float:
    bmi = round(self.weight/(self.height**2),2)
    return bmi

def update_patient(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.weight)
  print(patient.height)
  print(patient.age)
  print(patient.allergies)
  print(patient.contact_details)
  print('BMI',patient.calculate_BMI)
  print('Updated DONE')

patients_info = {'name':'shubham','age':29,'email':'shubham@icici.com','linkedin':'https://www.link.com',
                 'allergies':['dust','flowers'],'contact_details':{'phone':'955','tele':'052','emergency':'948'},
                 'weight':83,'height':1.83}

Patient1 = Patient(**patients_info)

update_patient(Patient1)
