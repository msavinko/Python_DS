import sys

def marketing():
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', \
		'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', \
		'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

	clients_set = set(clients)
	participants_set = set(participants)
	recipients_set = set(recipients)

	if sys.argv[1] == 'call_center':
		didnt_see_promo_sed = clients_set - recipients_set
		didnt_see_promo = list(didnt_see_promo_sed)
		# didnt_see_promo.append('jessica@gmail.com')
		return didnt_see_promo
	if sys.argv[1] == 'potential_clients':
		participants_not_clients_sed = participants_set - clients_set
		participants_not_clients = list(participants_not_clients_sed)
		# participants_not_clients.append('pinkman@yo.org')
		return participants_not_clients
	if sys.argv[1] == 'loyalty_program':
		did_not_partic_sed = set.union(clients_set, recipients_set) - participants_set
		did_not_partic = list(did_not_partic_sed)
		return did_not_partic

if __name__ == '__main__':
	if len(sys.argv) != 2 or (sys.argv[1] != 'call_center' \
		and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
		raise Exception('Wrong arguments')
	print(marketing())
