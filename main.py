from models import Contact, ContactBook
from storage import save_contacts, load_contacts

def main()-> None:
    contact_book = ContactBook()
    loaded_data = load_contacts('data.json')

    for item in loaded_data:
        contact = Contact(item['name'], item['phone_number'], item['email'], item['category'])
        contact_book.add_contact(contact)

    while True:

        print('1. Add Contact')
        print('2. View all Contacts')
        print('3. Search Contacts')
        print('4. Delete Contacts')
        print('5. Quit')

        try:
            user_choice = int(input('please enter a number between 1-5.'))
            if user_choice > 5 or user_choice == 0:
                print('please pick a number between 1-5 only.')
                continue
        except ValueError:
            print('You can only choose numbers between 1-5.')
            continue
        
        # where the user choices start⬇️

        if user_choice == 1:
            print('please enter the contact details:')

            contact_name = (input('Please enter a name: '))

            phone_number = (input('please enter a phone number: '))
            
            if len(phone_number) >= 14:
                print('invalid')

            email = (input('please enter an email address: '))

            category = (input('please enter a category(friends, family, work): '))

            contact = Contact(contact_name, phone_number, email, category)
            contact_book.add_contact(contact)
            save_contacts('data.json', contact_book.to_list())
        
        
        elif user_choice == 2:
            contact_book.show_all()
        
        elif user_choice == 3:

            search_term = input('please enter a search term (such as a name): ')

            contact_book.search(search_term)
        
        elif user_choice == 4:
            
            delete_term = input('please enter a delete term (such as a name): ')

            contact_book.delete_contact(delete_term)

            save_contacts('data.json', contact_book.to_list())

        
        elif user_choice == 5:
            print('goodbye!')
            break



if __name__ == '__main__':
    main()


