from Packages import *
print('NOTE : "admin" is the password to access the Admin folder')

print(10*'*')
print('Welcome to Arnold GYM!')

def showOptions():
    print('**********\nSelect')
    print('1.Admin\n2.Member\n3.exit')
    n = int(input())
    return n
    
n = showOptions()
 
D = {}
R = {}
CR = {}
reg =  {'Mon' : 'Empty', 'Tue' : 'Empty', 'Wed' : 'Empty', 'Thu' : 'Empty', 'Fri' : 'Empty', 'Sat' : 'Empty', 'Sun' : 'Empty'}

A = Member.Members('Moulu',24,'Male',123456789,20,3)
D[A.phn] = A
R[A.phn] = Regimens.regimen(A.bmi)


while True : 
    if n == 1 :
        print('Enter The Password')
        p = input()
        if p == 'admin' :
            print('Hello Admin')
            while True :  
                print('**********\nSelect\n1.Create Member\n2.View Member\n3.Delete Member\n4.Update Member\n5.Create Regimen\n6.View Regimen\n7.Delete Regimen\n8.Update Regimen\n9.exit')
                c = int(input())
                if c == 1:
                    print('Create Member')
                    name = input('Enter the Name of  New Customer\n')
                    age = int(input('Enter the Age of New Customer\n'))
                    gender = input('Enter the Gender of New Customer\n')
                    phn = int(input('Enter the Contact Number of New Customer\n'))
                    bmi = int(input('Enter the BMI of New Customer\n'))
                    Dur = int(input('Enter the Membership Duration(in months) of New Customer\n'))
                    A = Member.Members(name,age,gender,phn,bmi,Dur)
                    D[phn] = A
                    while True :
                        print("1.Create Regimen By Customer's BMI\n2.Create Regimen from Customized Regimen Plans")
                        p = int(input())
                        if p == 1 :
                            R[phn] = Regimens.regimen(bmi)
                            print("Member's Regimen Updated Succefully")
                            break
                        elif p == 2 :
                            if len(CR) != 0 :
                                print('Select the Customized Regimen')
                                for i in range(len(CR.keys())) :
                                    print(i,'.',list(CR.keys())[i])
                                h = int(input())
                                R[phn] = CR[list(CR.keys())[i]]
                                print("Member's Regimen Updated Successfully")
                                break
                            else :
                                print('No Custom Plans Created')
                    print('Member Added Successfully!!')
                elif c == 2 :
                    print('View Member')
                    cntct = int(input('Enter the Contact Number of the Customer\n'))
                    if cntct in D.keys() :
                        D[cntct].viewDetails()
                    else :
                        print('Member Not Found')
                elif c == 3 :
                    print('Delete Member')
                    cntct = int(input('Enter the Contact Number of the Customer\n'))
                    if cntct in D.keys() and R.keys() :
                        D.pop(cntct)
                        R.pop(cntct)
                        print('Member Removed Successfully')
                    else :
                        print('Member Not Found')
                elif c == 4 :
                    print('Update Member')
                    cntct = int(input('Enter the Contact Number of the Customer\n'))
                    if cntct in D.keys() and R.keys():
                        print('Present Membership Duration is ',D[cntct].duration,' months')
                        k = int(input('Enter the New Membership Duration(in months) of the customer\n'))
                        if k == 0:
                            D.pop(cntct)
                            R.pop(cntct)
                            print('Membership Removed')
                        else :
                            D[cntct].duration = k
                            print('Membership Updated Successfully')
                    else :
                        print('Member Not Found')
                elif c == 5 :
                    print('Create Regimen')
                    b = {}
                    r = input('Enter the name of the Customized Regimen\n')
                    for i in reg :
                        print('Enter the Regimen plan for ',i)
                        j = input()
                        b[i] = j
                    CR[r] = b
                    print('Regimen Created Successfully')
                elif c == 6 :
                    print('View Regimen')
                    print('1.Regimen of a Member\n2.Your Customized Regimen Plans')
                    g = int(input())
                    if g == 1 :
                        cntct = int(input('Enter the Contact Number of the Customer\n'))
                        if cntct in list(R.keys()) :
                            for i in R[cntct] :
                                print(i ,' : ',R[cntct][i]) 
                        else :
                            print('Member Not Found')
                    elif g == 2 :
                        if len(CR) == 0 :
                            print('No Custom Regimen Created')
                        else :
                            for i in range(len(CR)) :
                                print(i,'.',list(CR.keys())[i])
                            f = int(input('Select the Regimen to View\n'))
                            for u in CR[list(CR.keys())[f]] :
                                print(u, ':', CR[list(CR.keys())[f]][u])
                    else :
                        print('Please Enter a Valid Option')
                elif c == 7 :
                    print('Delete Regimen')
                    if len(CR) == 0 :
                        print('No Custom Regimen Created')
                    else :
                        for i in range(len(CR)) :
                            print(i,'.',list(CR.keys())[i])
                        f = int(input('Select the Regimen to Delete\n'))
                        CR.pop(list(CR.keys())[f])
                        print('Regimen Deleted Successfully')
                elif c == 8 :
                    print('Update Regimen')
                    print('1.Update Regimen from Customized Regimen\n2.Update Regimen of a Member')
                    y = int(input())
                    if y == 1 :
                        if len(CR) == 0 :
                            print('No Custom Regimen Created')
                        else :
                            for i in range(len(CR)) :
                                print(i,'.',list(CR.keys())[i])
                            f = int(input('Select the Regimen to Update\n'))
                            for u in CR[list(CR.keys())[f]] :
                                print(u, ':', CR[list(CR.keys())[f]][u])
                            for t in range(len(reg)):
                                print('Enter ',t,' to update the Workout plan on', list(reg.keys())[t])
                            o = int(input())
                            CR[list(CR.keys())[f]][list(reg.keys())[o]] = input('Enter Your New Workout Plan of the Day\n')
                            print('Regimen Updated Successfully')
                    elif y == 2 :
                        cntct = int(input('Enter the contact number of the person\n'))
                        if cntct in list(R.keys()):
                            print("1.Update Regimen By Customer's BMI\n2.Update Regimen from Customized Regimen Plans")
                            p = int(input())
                            if p == 1 :
                                R[cntct] = Regimens.regimen(D[cntct].bmi)
                                print("Member's Regimen Updated Succefully")
                            elif p == 2 :
                                if len(CR) != 0 :
                                    print('Select the Customized Regimen')
                                    for i in range(len(CR.keys())) :
                                        print(i,'.',list(CR.keys())[i])
                                    h = int(input())
                                    R[cntct] = CR[list(CR.keys())[i]]
                                    print("Member's Regimen Updated Successfully")
                                else :
                                    print('No Customized plan Created')
                            else :
                                print('Enter a Valid Response')
                        else :
                            print('Member Not Found')
                    else :
                        print('Please Enter a Valid Response')        
                elif c == 9 :
                    break
                else :
                    print('Enter a valid Option')
        else :
            print('Wrong Password!!\nAccess Denied!!!')
    elif n == 2:
        print('Hello Member')
        cntct = int(input('Enter your contact number\n'))
        while True :
            if cntct not in D.keys() and R.keys():
                print('Number not found')
                break
            print('**********\nSelect\n1.My Regimen\n2.My Profile\n3.exit')
            m = int(input())
            if m == 1:
                print('Your Regimen')
                for i in R[cntct] :
                    print(i ,' : ',R[cntct][i])
            elif m == 2:
                print('Your Profile')
                print(D[cntct].viewDetails())
            elif m == 3:
                break
            else :
                print('Enter a valid Option')
    elif n == 3:
        break
    else :
        print('Select From Valid Options Only')
    n = showOptions()
    
print('Thank You!!')
