
with open('Sample.txt','w') as f:
    f.write('My name is Shivam kumar soni\
                I am 20 Year Old.\
                Currently , I am pursing my B.tech From Marwadi University ,Rajkot\
                Thankyou all of you!!!')
with open('Sample.txt','r') as f:
    #print(f.readlines(60))
    f.seek(40)
    print(f.read(5))
    print(f.tell())