from dataclasses import dataclass 

@dataclass
class Contact:
    name: str
    phone_number: str
    email: str
    category: str

    def __str__(self)-> str:
        return f'{self.name}: {self.phone_number}: {self.email}: {self.category}'
    
    def to_dict(self) -> dict:
        contact_detail = {
            'name': self.name, 
            'phone_number': self.phone_number, 
            'email': self.email,
            'category': self.category
        }
        return contact_detail
    
