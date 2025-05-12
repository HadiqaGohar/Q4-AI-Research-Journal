from pydantic import BaseModel, ValidationError
from typing import Optional  # Import Optional for Python <3.10

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None  # Use Optional for optional fields

# Valid data
user_data = {"id": 1, "name": "Hadiqa Gohar", "email": "hg@example.com", "age": 19}
user = User(**user_data)
print(user)  # id=1 name='Hadiqa Gohar' email='hg@example.com' age=19
print(user.model_dump())  # {'id': 1, 'name': 'Hadiqa Gohar', 'email': 'hg@example.com', 'age': 19}

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
