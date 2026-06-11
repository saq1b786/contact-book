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
    
class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact: Contact):

        self.contacts.append(contact)
        print('the contact info has been added!')

    def delete_contact(self, name: str):

        for item in self.contacts:
            if name == item.name:
                self.contacts.remove(item)
                print('contact has been removed from contacts list')
                return
        else:
            print('there was no name that matched in the contacts list')
            return
        
    def search(self, search_term: str)-> list:

        searched_list = []

        for item in self.contacts:
            if search_term.lower() in item.name.lower() or search_term.lower() in item.email.lower() or search_term.lower() in item.category.lower():
                searched_list.append(item)
        
        if not searched_list:
            print('no matches were found')

        return searched_list
    
    def show_all(self) -> None:

        if not self.contacts:
            print('the list is empty')
            return

        for item in self.contacts:
            print(item)
    
    def to_list(self) -> list:
        saved_list = []

        for item in self.contacts:
            saved_list.append(item.to_dict())
        return saved_list
        
            
            



            





        


