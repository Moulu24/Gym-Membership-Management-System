class Members :
    def __init__(self,name,age,gender,phn,bmi,duration):
        self.name = name
        self.age = age
        self.gender = gender
        self.phn = phn
        self.bmi = bmi
        self.duration = duration
        
    def viewDetails(self) :
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Gender : ', self.gender)
        print('Phone Number : ', self.phn)
        print('BMI : ', self.bmi)
        print('Membership Duration : ', self.duration,' Months')
        
        