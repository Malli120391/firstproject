"""student_info={
    "Ram":{"roll_no":10,"age":20,"course":"python"},
    "Mohan":{"roll_no":20,"age":22,"course":"Java"}
}"""
student_info=[
    {
        "Name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"python"
    },
    {
        "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java",
        "phone_no":[9999955555,7777755]
    }
]
print(student_info[1]["phone_no"])
#print(student_info["Mohan"])
#print(student_info["Mohan"]["roll_no"])
#student_info["Mohan"]["phone_no"]=9999955555
#print(student_info["Mohan"])
#del student_info["Mohan"]["phone_no"]
#print(student_info["Mohan"].pop("phone_no"))
#print(student_info["Mohan"])

travel_info={
    "Hyderabad":["Hitech-City","jubblihills", "Ameerper-University"],
    "Vijayawada":["Prakasham barrage", "Durga Temple"]
}
print(travel_info)