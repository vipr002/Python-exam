# question 3
class Message:

    def __init__(mail, recipient, sender, text):
        mail.recipient = recipient
        mail.sender = sender
        mail.text = text

    def get_sender(mail):
        return mail.sender

    def get_recipient(mail):
        return mail.sender

    def append(mail, new_message):
        mail.text += new_message
        return mail.text

    def toString(mail):
        longString = f"From: {mail.sender} \nTo: {mail.recipient} \n{mail.text} "
        return longString


def main():
    running = True
    has_message = False
    new_message = None
    print("Welcome to Pythonmail")
    while running:
        nav = input(
            "Would you like to send a new mail? \ny. Yes \nn. No/Exit \nv. View current "
            "mail \n")
        try:
            if nav == "y":
                sender = input("Who is sending this mail?: \n")
                recipient = input("Who is this mail to?: \n")
                text = input("Write your message: \n")

                new_message = Message(recipient, sender, text)

                sending = input("Would you like to send this message? \ny. Yes \nanything. No/Exit \n")
                if sending == "y":
                    print("Message is sent")
                else:
                    print("Message is not sent")
                    has_message = True

            elif nav == "v":
                if has_message:
                    print(new_message.toString())

                    editing = True
                    while editing:
                        nav2 = input("do you want to add anything? \ny. Yes \nn. No\ns. Send \n")
                        try:
                            if nav2 == "y":
                                addToString = input("type what you want to add to the message: \n")
                                new_message.append(" ")
                                new_message.append(addToString)
                                print(f"your new mail is: \n{new_message.toString()}")
                            elif nav2 == "n":
                                print("nothing added")
                                editing = False
                            elif nav2 == "s":
                                print("Message sent!")
                                has_message = False
                                editing = False
                            else:
                                raise ValueError(f"Invalid input: {nav2}")
                        except ValueError as e:
                            print(e)
                else:
                    print("there is no current mail")
            elif nav == "n":
                running = False
            else:
                raise ValueError(f"Invalid input: {nav}")
        except ValueError as e:
            print(e)


main()
