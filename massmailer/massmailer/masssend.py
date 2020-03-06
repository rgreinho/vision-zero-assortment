import csv
import pathlib
import os

import yagmail

from massmailer import renderer

DEBUG = True


def send_email(subject, receiver, message, preview_only=False):
    if preview_only:
        yag = yagmail.SMTP("mygmailusername", "mygmailpassword")
        recipients, msg_string = yag.prepare_send(
            to=receiver, subject=subject, contents=message
        )
        print(f"recipients={recipients}")
        print(f"msg_string={msg_string}")
        return

    gmail_user = os.environ.get("gmail_user")
    gmail_oauth2 = os.environ.get("gmail_oauth2", "~/.config/oca/oauth2_creds.json")
    yag = yagmail.SMTP(gmail_user, oauth2_file=gmail_oauth2)
    yag.send(to=receiver, subject=subject, contents=message, preview_only=preview_only)


def main():
    # Read the CSV file.
    input_file = pathlib.Path("amplify.csv")
    with input_file.open(newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        # Render the template for each row.
        for row in reader:
            content = renderer.file_to_string("massmailer/our_congress_avenue.txt", row)
            if row.get("email"):
                # print(content)
                send_email(
                    "Our Congress Avenue", row.get("email"), content, preview_only=DEBUG
                )
            break


if __name__ == "__main__":
    main()
