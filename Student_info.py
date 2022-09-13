import json
ans={
    "Student":{
        "Personal_info":{
            "first_name":"Zholdoshbek",
            "last_name":"Tashiev",
            "birth_d":"20-07-2001",
        },
        "University":
            {
        "Course":3,
        "Club":"Neobis",
        "student_id":1904,
        "scholarship_$":100
            
        }
        
    }

}
x=json.dumps(ans)
print(x)