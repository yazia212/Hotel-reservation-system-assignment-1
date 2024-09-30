# Class for Customer
class Customer:
    def __init__(self, name, email, phone, credit_card):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__credit_card = credit_card

    # Getters
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_credit_card(self):
        return self.__credit_card

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        if "@" in email:  # basic validation
            self.__email = email
        else:
            print(f"Invalid email format for {self.__name}. Please re-enter a valid email.")

    def set_phone(self, phone):
        self.__phone = phone

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card

    # Placeholder function with pass
    def update_customer_info(self):
        # This function should handle customer info updates in the future
        pass


# Class for Room
class Room:
    def __init__(self, room_number, room_type, price, availability):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price = price
        self.__availability = availability

    # Getters
    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_price(self):
        return self.__price

    def is_available(self):
        return self.__availability

    # Setters
    def set_room_number(self, room_number):
        self.__room_number = room_number

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def set_price(self, price):
        self.__price = price

    def set_availability(self, availability):
        self.__availability = availability

    # Placeholder function with pass
    def reserve_room(self):
        # This function should handle room reservation logic in the future
        pass


# Class for Reservation
class Reservation:
    def __init__(self, dates, room_type, confirmation_number, price, nights, number_of_rooms):
        self.__dates = dates
        self.__room_type = room_type
        self.__confirmation_number = confirmation_number
        self.__price = price
        self.__nights = nights
        self.__number_of_rooms = number_of_rooms

    # Getters
    def get_dates(self):
        return self.__dates

    def get_room_type(self):
        return self.__room_type

    def get_confirmation_number(self):
        return self.__confirmation_number

    def get_price(self):
        return self.__price

    def get_nights(self):
        return self.__nights

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    # Setters
    def set_dates(self, dates):
        self.__dates = dates

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def set_confirmation_number(self, confirmation_number):
        self.__confirmation_number = confirmation_number

    def set_price(self, price):
        self.__price = price

    def set_nights(self, nights):
        self.__nights = nights

    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    # Placeholder function with pass
    def cancel_reservation(self):
        # This function should handle reservation cancellation in the future
        pass


# Class for Payment
class Payment:
    def __init__(self, method, total_amount, status, taxes_fees):
        self.__method = method
        self.__total_amount = total_amount
        self.__status = status
        self.__taxes_fees = taxes_fees

    # Getters
    def get_method(self):
        return self.__method

    def get_total_amount(self):
        return self.__total_amount

    def get_status(self):
        return self.__status

    def get_taxes_fees(self):
        return self.__taxes_fees

    # Setters
    def set_method(self, method):
        self.__method = method

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def set_status(self, status):
        self.__status = status

    def set_taxes_fees(self, taxes_fees):
        self.__taxes_fees = taxes_fees

    # Method to process payment
    def process_payment(self):
        if self.__status == "pending":
            self.__status = "completed"
            print("Payment successful.")
        else:
            print("Payment already processed.")

    # Placeholder function with pass
    def process_refund(self):
        # This function should handle refund process in the future
        pass


# Updated Test Case - Filling in Reservation Details
customer1 = Customer("Sara Ahmed", "sara@gmail.com", "1234567890", "Mastercard 9904")
room1 = Room(101, "Queen Bed", 329.95, True)  # Price in AED
reservation1 = Reservation("2024-09-30", "Queen Bed", 52523687, 329.95, 2, 1)
payment1 = Payment("Mastercard", 659.90, "pending", 21.58)

# Printing out reservation details similar to the example image
print("\nYour Reservation Is Confirmed")
print(f"Your Name: {customer1.get_name()}")
print(f"Your Email: {customer1.get_email()}")
print(f"Hotel Confirmation Number: {reservation1.get_confirmation_number()}")

print("\nHotel in Abu Dhabi")
print("Sheikh Zayed Road, Abu Dhabi, UAE")
print("Phone: 02-555-5555")
print(f"Check-In: {reservation1.get_dates()}")
print(f"Room Type: {reservation1.get_room_type()}")
print(f"Room Number: {room1.get_room_number()}")
print(f"Nights: {reservation1.get_nights()}")
print(f"Number of Rooms: {reservation1.get_number_of_rooms()}")

print("\nSummary of Charges")
print(f"Billing Name: {customer1.get_name()}")
print(f"Credit Card: {customer1.get_credit_card()}")
print(f"Room Cost (per night): AED {room1.get_price()}")
print(f"Room Subtotal: AED {reservation1.get_price() * reservation1.get_nights()}")
print(f"Taxes and Fees: AED {payment1.get_taxes_fees()}")
print(f"Total Charges: AED {reservation1.get_price() * reservation1.get_nights() + payment1.get_taxes_fees()}")
payment1.process_payment()



