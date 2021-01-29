import csv
import json

# open the csv file.
def read_csv(csv_file):
    while True:
        try:
            with open(csv_file, newline='', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    print(row)
                input("\nTryck Enter för att forstätta.")
                break
        # If the CSV file is not found, will have to manually input the path for it.
        except FileNotFoundError:
            print("\nKunde inte hitta CSV filen. Vänligen mata in sökväg för CSV filen.")
            # User input the filepath for the CSV file.
            csv_file = input("CSV sökväg: ")


# save the csv file as dictionary in list then as JSON file.
def save_csv(csv_file, json_file):
    while True:
        try:
            with open(csv_file, newline='', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, delimiter=';')
                data = []
                for row in reader:
                    data.append(row)
            with open(json_file, 'w', encoding='utf-8-sig') as f:
                # saving the json file.
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("\nCSV fil sparat som %s" % (json_file))
            input("Tryck Enter för att forstätta.")
            break
        except FileNotFoundError:
            print("\nKunde inte hitta CSV filen. Vänligen mata in sökväg för CSV filen.")
            csv_file = input("CSV sökväg: ")


# adding a student to the json file.
def add_student(json_file):
    try:
        with open(json_file, newline='', encoding='utf-8-sig') as f:
            data = json.load(f)
            Användarnamn = ""
            Förnamn = ""
            Efternamn = ""
            epost = ""

            print("\nAnge information om studenten: \n")
            # check so that the user doesn't input an exmpty string. // credits to Mattias.
            while not Användarnamn:
                # strip to remove "SPACE"
                Användarnamn = input("Användarnamn: ").strip()
            while not Förnamn:
                Förnamn = input("Förnamn: ")
            while not Efternamn:
                Efternamn = input("Efternamn: ")
            while not epost:
                epost = input("epost: ")
            # Adding the student into a dictionary.
            student = {'Användarnamn': Användarnamn, 'Förnamn': Förnamn,
'Efternamn': Efternamn, 'epost': epost}
            data.append(student)  # add student to data List.

            while True:
                print("\nVill du lägga till %s till student listan?" % (Förnamn))
                inputed = input("Mata in 'ja' eller 'nej'.\n").lower()
                if inputed == 'ja':
                    with open(json_file, 'w', encoding='utf-8-sig') as f:
                        # saving the data of student to the json file.
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    print("Information om %s har blivit tillagd i %s!" %
                          (Förnamn, json_file))
                    input("Tryck Enter för att forstätta.")
                    break
                elif inputed == 'nej':
                    print("\nInformation om %s blev inte tillagd." %
                          (Användarnamn))
                    input("Tryck Enter för att forstätta.")
                    break
                else:
                    print(
                        "Mata in 'ja' eller 'nej' för att spara eller inte spara denna student till student listan.")
    except FileNotFoundError:
        print("Kunde inte hitta JSON filen. Vänligen konrollera JSON_FILE.")
        input("Tryck ENTER för att återgå till menyn.")


# remove a student from the student_data.json.
def remove_student(json_file):
    while True:
        try:
            with open(json_file, 'r', encoding='utf-8-sig') as f:
                reader = json.load(f)
                # so the first student number is started with 0. ( for the del reader(inputed) part)
                counter = -1
                for s in reader:
                    counter += 1
                    print("[%s] %s %s %s %s" % (counter, s['Användarnamn'],s['Förnamn'], s['Efternamn'], s['epost']))
                print("\nAnge nummer för vilken student som ska raderas från student listan.")
                while True:
                    try:
                        inputed = int(input("Student nummer: "))
                        del reader[inputed]
                        input("Tryck Enter för att forstätta.")
                        break
                    except ValueError:
                        print("Vänligen mata in ett student nummer.")
                    except IndexError:
                        print("Student nummer existerar inte!")
            with open(json_file, 'w', encoding='utf-8-sig') as f:
                # saving the json file.
                json.dump(reader, f, indent=4, ensure_ascii=False)
                break
        except FileNotFoundError:
            print(
                "\nKunde inte hitta JSON filen. Vänligen mata in sökväg för JSON filen.")
            json_file = input("Json sökväg: ")


# show a list of student from the studnet_data.json
def show_student(json_file):
    while True:
        try:
            with open(json_file, 'r', encoding='utf-8-sig') as f:
                reader = json.load(f)
                counter = 0 # to count how many students exist in the list.
                for s in reader:
                    counter += 1
                    print("[%s] %s %s %s %s" % (counter, s['Användarnamn'],s['Förnamn'], s['Efternamn'], s['epost']))
                input("\nTryck Enter för att forstätta.")
                break
        except FileNotFoundError:
            print(
                "\nKunde inte hitta JSON filen. Vänligen mata in sökväg för JSON filen.")
            json_file = input("Json sökväg: ")
