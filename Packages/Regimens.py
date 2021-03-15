def regimen(bmi) :
    if bmi < 18.5 :
        r = {'Mon' : 'Chest', 'Tue' : 'Biceps', 'Wed' : 'Rest', 'Thu' : 'Back', 'Fri' : 'Triceps', 'Sat' : 'Rest', 'Sun' : 'Rest'}
    elif bmi >= 18.5 and bmi < 25 :
        r = {'Mon' : 'Chest', 'Tue' : 'Biceps', 'Wed' : 'Cardio/Abs', 'Thu' : 'Back', 'Fri' : 'Triceps', 'Sat' : 'Legs', 'Sun' : 'Rest'}
    elif bmi >= 25 and bmi < 30 :
        r = {'Mon' : 'Chest', 'Tue' : 'Biceps', 'Wed' : 'Cardio/Abs', 'Thu' : 'Back', 'Fri' : 'Triceps', 'Sat' : 'Legs', 'Sun' : 'Cardio'}
    else :
        r = {'Mon' : 'Chest', 'Tue' : 'Biceps', 'Wed' : 'Cardio', 'Thu' : 'Back', 'Fri' : 'Triceps', 'Sat' : 'Cardio', 'Sun' : 'Cardio'}
    return r