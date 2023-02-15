
from contact import user, text, owl

def send_mass_messages(message, user_list):
    """Envoi des messages en masse.

    Utilise la méthode de message de chaque utilisateur."""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)

# Our main program.
alice = user.User("Alice", text.TextContactSystem("0102030405"))
bob = user.User("Bob", owl.OwlContactSystem("4 Privet Drive"))

user_list = [alice, bob]
send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
send_mass_messages(
    "Salut {name}. Tes informations de contact sont-elles corrects?"
    " Nous avons celles-ci: {contact_info}.",
    user_list,
)
