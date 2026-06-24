def Student(**kwargs):
    for key,value in kwargs.items():
        print(key,'=',value)

Student(Name='Shivam Kumar Soni',Age=20,Gender='Male',City='Rajkot')
