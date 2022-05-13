import time
user_input = None
while True:
    if not user_input:
        while True:
            user_input = input('Enter your ID: ')
            try:
                int(user_input)
                if len(user_input) !=11:
                    raise UserWarning
            except ValueError:
                print('Code is not numeric')
            except UserWarning:
                if len(user_input) > 11:
                    print('Code is too long')
                else:
                    print('Code is too short')
            else:
                print(user_input)
                time.sleep(1.5)
                break
        # THIS ZONE IS IN TEST(TO MAKE USER_INPUT 6 WORKING)
    if user_input:
        if int(user_input[0]) in range (1,9):
            if int(user_input[0]) % 2 == 0:
                gender = 'female'
            else:
                gender = 'male'
        else:
            gender = 'Error. Can not determine gender.'

        if user_input[0] in ['1', '2']:
            bcent = '18'
        elif user_input[0] in ['3', '4']:
            bcent = '19'
        elif user_input[0] in ['5', '6']:
            bcent = '20'
        elif user_input[0] in ['7', '8']:
            bcent = '21'
        else:
            bcent = None
        birth = (f'You were born in {user_input[5:7]}.{user_input[3:5]}.{bcent}{user_input[1:3]}')
        if int(user_input[7:10]) in range(100, 151):
            region = 'You were born in East Tallinn Central Hospital or Pelgulinna Maternity Hospital (Tallinn)'
        elif int(user_input[7:10]) in range(151, 161):
            region = 'You were born in Keila Hospital'
        elif int(user_input[7:10]) in range(161, 221):
            region = 'You were born in Rapla-, Loksa- or Hiiumaa Hospital'
        elif int(user_input[7:10]) in range(221, 271):
            region = 'You were born in Ida-Viru Central Hospital (Kohtla Järve)'
        elif int(user_input[7:10]) in range(271, 371):
            region = 'You were born in Maarjamõisa Clinic (Tartu) or Jõgeva Hospital'
        elif int(user_input[7:10]) in range(371, 421):
            region = 'You were born in Narva Hospital'
        elif int(user_input[7:10]) in range(421, 471):
            region = 'You were born in Pärnu Hospital'
        elif int(user_input[7:10]) in range(471, 491):
            region = 'You were born in Haapsalu Hospital'
        elif int(user_input[7:10]) in range(491, 521):
            region = 'You were born in Järva County Hospital'
        elif int(user_input[7:10]) in range(521, 571):
            region = 'You were born in Rakvere Hospital or Tapa Hospital'
        elif int(user_input[7:10]) in range(571, 601):
            region = 'You were born in Valga Hospital'
        elif int(user_input[7:10]) in range(601, 651):
            region = 'You were born in Viljandi Hospital'
        elif int(user_input[7:10]) in range(651, 701):
            region = 'You were born in South Estonian Hospital (Võru) or Põlva Hospital'
        elif int(user_input[7:10]) in range(701, 1000):
            region = 'You were not born in Estonia'
        elif int(user_input[8:10]) in range(11, 20):
            region = "You were born in University of Tartu Women's Clinic"
        elif int(user_input[8:10]) in range(21, 100):
            region = 'You were born in East Tallinn Central Hospital or Pelgulinna Maternity Hospital (Tallinn)'
        elif int(user_input[9:10]) in range(1, 10) or int(user_input[8:10]) == 10:
            region = 'You were born in Kuressaare Hospital'
        else:
            region = 'The region of your birth has not been identified'





    user_choice = input('Please choose:\n'
                        '1.Get gender\n'
                        '2.Get date of birth\n'
                        '3.Get region of birth\n'
                        '4.Validate ID\n'
                        '5.Change ID\n'
                        '6.General information\n'
                        '0.Exit\n'
                        '--->')
    if user_choice == '1':
        try:
            print('You are', gender)
            time.sleep(1.5)
        except(NameError):
            print('Your gender has not been determined, try again.')
            time.sleep(1.5)
            user_input = ''
            continue
    elif user_choice == '2':
        try:
            print(birth)
            time.sleep(1.5)
        except(NameError):
            print('Your birthday has not been determined, try again.')
            time.sleep(1.5)
            user_input = ''
            continue

    elif user_choice == '3':
        try:
            print(region)
            time.sleep(1.5)
        except(NameError):
            print('Your region has not been determined, try again.')
            time.sleep(1.5)
            user_input = ''
            continue
    elif user_choice == '4':
        x = [int(num) for num in str(user_input)]
        sum1 = (str(x[0] + x[1]*2 + x[2]*3 + x[3]*4 + x[4]*5 + x[5]*6 + x[6]*7 + x[7]*8 + x[8]*9 + x[9]))
        sum2 = (str(x[0]*3 + x[1]*4 + x[2]*5 + x[3]*6 + x[4]*7 + x[5]*8 + x[6]*9 + x[7]*1 + x[8]*2 + x[9]*3))
        if int(sum1) % 11 == int(user_input[10]):
            print('Valid code')
            time.sleep(1.5)

        elif int(sum2) % 11 == int(user_input[10]):
            print('Valid code')
            time.sleep(1.5)
        else:
            print('Code is not valid. Returning to the main menu.')
            time.sleep(1.5)

    if user_choice == '0':
        break
    elif user_choice == '6':
        try:
            print('You are', gender + '.', birth + '.', 'And', region[0:21].lower() + region[21::].capitalize())
            time.sleep(1.5)
        except (NameError):
            print('Check your gender, date and region at first, please')
            time.sleep(1.5)


    elif user_choice == '5':
        user_input = ''
        continue


