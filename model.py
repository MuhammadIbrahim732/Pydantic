from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    computed_field,
    field_validator,
    model_validator,
)


class Category(BaseModel):
    name: Literal["starter", "beverages", "Electronics", "Stationary"]

class Model(BaseModel):
    model_config = ConfigDict(
        extra = "ignore",
        strict = True,
        frozen = True,
        validate_assignment = True
    )


    # Field       : ValyeType
    id            : int
    name          : str = Field(..., alias="userName") # Required Field
    price         : float
    category      : Category
    is_available  : bool = Field(default=True) # Default Value
    description   : str | None = None # optional Field
    email         : EmailStr

    # FieldValidator
    @field_validator("name")
    @classmethod
    def title_name(cls, value):
        return value.title()

    # ModelValidator
    @model_validator(mode = "after")
    def check_available(self):
        if self.is_available and self.price <= 0:
            raise ValueError("Available Item must have price greator than zero")
        else:
            return self

    #ComputedField
    @computed_field
    @property
    def price_with_tax(self) -> float:
        return round(self.price * 1.5, 2)
      
item = Model(
    id = 1,
    userName = "Sample ITEM",
    price = 20.98,
    category = Category(name = "Electronics"),
    is_available = True,
    description = "This is a sample item for demonstration purposes.",
    email= "ali@gmail.com"
)

print(item.model_dump()) # Serialization
print(item.model_dump_json()) # JSON Serialization