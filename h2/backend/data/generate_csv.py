import os
import random
import csv

phishing_templates = [
    "Your account has been suspended verify immediately",
    "Click here to update your payment details",
    "You have won a free gift card claim now",
    "URGENT: Your password expires in 24 hours",
    "Action required: verify your banking information",
    "Your invoice is attached please pay immediately",
    "You have a new secure message from IT",
    "Security Alert: unusual sign-in detected",
    "Update your billing details to avoid service interruption",
    "Claim your exclusive reward today"
]

legit_templates = [
    "Meeting scheduled tomorrow with the team",
    "Please review the attached project document",
    "Reminder for today's appointment",
    "Here are the notes from last week's sync",
    "Can you double check these numbers?",
    "Lunch at noon?",
    "Your recent order has shipped",
    "Code review requested for the new feature",
    "Happy birthday! Wishing you the best.",
    "Don't forget to submit your timesheet"
]

def generate():
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    with open('emails.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["email_text", "label"])
        
        for _ in range(500):
            writer.writerow([random.choice(phishing_templates), 1])
            writer.writerow([random.choice(legit_templates), 0])
            
    print("emails.csv generated successfully with 1000 rows.")

if __name__ == "__main__":
    generate()
