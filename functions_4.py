def greet_family(name='John', surname='Doe', family_list=[]):
    print(f'Hello {name} {surname}')
    for member in family_list:
        print(f'Hello {member[0]} {member[1]}')

family_members = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
greet_family(family_list=family_members)