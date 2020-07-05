import pypizza
import requirements.txt
import requests

json = requests.get(http://localhost:5000/order)

customer = Customer(json.getVar(Name), json.getVar(Phone), json.getVar(Address))

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

menu = my_local_dominos.get_menu()

order = Order.begin_customer_order(customer, my_local_dominos)

order.add_item(json.getVar(Order))

payment = Payment("CASH")

order.place(payment)
my_local_dominos.place_order(order, payment)
