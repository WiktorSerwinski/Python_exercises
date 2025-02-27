from functools import reduce


#Initial only one "@" in email address

def divide_domain_from_email(email):
    name = ""
    domain = ""
    for i in range(0,len(email)):        
        if(email[i]) == "@":
            div = i
            for j in range(div,len(email)):
                domain+=email[j]
            break
        else:
            name+=email[i]
    
    print(name)
    print(domain)
    
def divide_domain_from_email(email):
    name = ""
    domain = ""
    for i in range(0,len(email)):        
        if(email[i]) == "@":
            div = i
            for j in range(div,len(email)):
                domain+=email[j]
            break
        else:
            name+=email[i]
    
    print(name)
    print(domain)

divide_domain_from_email("wiktor.serwinski8@gmail.com")


def divide_domain_from_email_pro(email):
    name = ""
    domain = ""
    n = email.find("@")
    name = email[0:n]
    domain = email[n:len(email)]
    print(name)
    print(domain)
    new_email = name + domain.replace("@gmail.com","@onet.pl")
    print(new_email)

# divide_domain_from_email_pro("wiktor.serwinski8@gmail.com")


def print_reverse_name(name):
    rev_name=""
    for n in range(1,len(name)+1):
        rev_name+=name[-n]
    print(rev_name)


        
#print_reverse_name("Wikor")
