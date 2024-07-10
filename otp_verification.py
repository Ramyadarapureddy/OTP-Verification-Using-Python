import random
import smtplib # used to send emails (Simple Mail Transfer Protocol)

OTP = random.randint(100000,999999)

#setting up the SMTP Server

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#User Inputs
name = input("Enter Your Name : ")
global receiver_email
receiver_email = input("Enter Your Email ID : ")

#Email Verification Function

def email_verification(receiver_email):
    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]
    count = 0

    #Checking the Domain
    for domain in email_check1:
        if domain in receiver_email:
            count += 1

    #Checking the Site
    for site in email_check2:
        if site in receiver_email:
            count += 1
        
    if '@' not in receiver_email and count != 2:
        print("Invalid Email Id")
        new_receiver_email = input("Enter Correct Email ID : ")
        email_verification(new_receiver_email)
        return new_receiver_email
    return receiver_email


#Validating Email
valid_receiver_email = email_verification(receiver_email)

#Logging into SMTP Server
password = "pirs gedp hiyj qndy"
server.login("otpverifica@gmail.com", password)

#Sending the Initial OTP
body = "Dear " + name + ",\n \n" + "Your OTP is " + str(OTP) + " ."
subject = "OTP Verification Using Python"
message = f'Subject : {subject}\n\n {body}'

server.sendmail("otpverifica@gmail.com", valid_receiver_email, message)

#OTP Verification Fundtion
def sending_otp(receiver_email):
    new_otp = random.randint(100000,999999)

    body = "Dear " + name + ",\n\n" + "Your OTP is " + str(new_otp) + " ."
    subject = "OTP Verification Using Python"
    message = f'Subject : {subject}\n\n{body}'
    server.sendmail('otpverifica@gmail.com',receiver_email,message)
    print("OTP has been sent to " +receiver_email)
    
    while True:
        try:
            receiver_OTP = int(input("Enter OTP : "))

            if receiver_OTP == new_otp:
                print("OTP Verified")
                break
            else:
                print("Invalid OTP")
                print("Resending OTP........")
                sending_otp(receiver_email)
                break
        except ValueError:
            print("Invalid Input. Please Enter a Numeric OTP")

#intial OTP Verification
print("OTP has been sent to " +valid_receiver_email)

while True:
    try:
        receiver_OTP = int(input("Enter OTP : "))

        if receiver_OTP == OTP :
            print("OTP Verified")
            break

        else:
            print("Invalid OTP")
            answer =input("Enter YES to resend OTP on same Email and NO to enter a New Email Id : ")
            YES = ["yes", "YES", "Yes"]
            NO = ["no", "NO", "No"]
            if answer in YES:
                sending_otp(valid_receiver_email)
                break

            elif answer in NO:
                new_receiver_email = input("Enter New Email ID : ")
                email_verification(new_receiver_email)
                sending_otp(new_receiver_email)
                break
            else:
                print("Invalid Input")
    except ValueError:
        print("Invalid Input.Please Enter a Numeric OTP.")

#Quitting The Server
server.quit()