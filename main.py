from pyscript import document, display

def check_student(e):
    document.getElementById("output1").innerHTML = ""  # Clear previous output
        fname = document.getElementById("fname").value = ""  # Gets Value of fname
        lname = document.getElementById("lname").value = ""  # Gets Value of lname

        applicant_name = str(fname + lname) # Concatenates fname and lname
        true_applicant_name = ["Lucas Ladion", "Francis Fernandez", "Maria Bamba", "Orange Mendoza", "Rafael De Castro", "Rayne Maniago", "Rohan Tabasan", "Tyler Sales", "Yanis Concepcion", "Zander Mira", "Georgina Gamponia", "Hannah Galapon", "Jarvis Joven", "Jibril Abdul", "Julienne Musni", "Kadhija Lucman", "Kian Ang", "Krishna Pascua", "Lorissa Paragas", "Cheree Mendoza", "Anya Basuil", "Edrian Correa", "Francesca Daquigan","Emmanual Correa", "Gabrielle De Jesus"]
        x = 
        verified = applicant_name.intersection(true_applicant_name) # Checks if the applicant_name is in the true_applicant_name list
        display(result, target ="outpu")  

