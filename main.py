from pyscript import document, display

def check_student(e):
    document.getElementById("output1").innerHTML = ""  # Clear previous output
    fname = document.getElementById("fname").value   # Gets Value of fname
    lname = document.getElementById("lname").value   # Gets Value of lname

    applicant_name = str(fname + " " + lname) # Concatenates fname and lname
    true_applicant_name = ["Lucas Ladion", "Francis Fernandez", "Cassiopeia Rigodon", "Maria Bamba", "Orange Mendoza", "Rafael De Castro", "Rayne Maniago", "Rohan Tabasan", "Tyler Sales", "Yanis Concepcion", "Zander Mira", "Georgina Gamponia", "Hannah Galapon", "Jarvis Joven", "Jibril Abdul", "Julienne Musni", "Kadhija Lucman", "Kian Ang", "Krishna Pascua", "Lorissa Paragas", "Cheree Mendoza", "Anya Basuil", "Edrian Correa", "Francesca Daquigan","Emmanual Correa", "Gabrielle De Jesus"] #Name of all registered applicants
    
    check = applicant_name in true_applicant_name # Checks if the applicant_name is in the true_applicant_name list
    verified = "Congratulations" + " " + applicant_name + "!" + " " + "you are a member of Math Guild" # Concatenates the applicant_name and the result of the check
    not_verified = "Sorry" + " " + applicant_name + " " + "you are not a member of Math Guild" # Concatenates the applicant_name and the result of the check
    display({
        True: verified,     # Displays the result in the output1 div when the applicant_name is in the true_applicant_name list
        False: not_verified # Displays the result in the output1 div when the applicant_name is not in the true_applicant_name list
    } [check], target="output1") # Displays the result in the output1 div

