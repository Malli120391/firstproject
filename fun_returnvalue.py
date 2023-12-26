"""def add(a,b):
    c=a+b
    return c
result=add(5,4)
print(result)"""

def format_name(first_name, last_name):
    formatted_first_name=first_name.title()
    formatted_last_name=last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"
    #print(f"{formatted_first_name},{formatted_last_name}")
#print(format_name("Malleswararao", "CHENNU"))
#format_name("Malleswararao", "CHENNU")

formatted_name=format_name("Malleswararao", "CHENNU")
print(formatted_name)
