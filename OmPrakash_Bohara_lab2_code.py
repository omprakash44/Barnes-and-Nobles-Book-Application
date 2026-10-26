"""
Author: Om Prakash Bohara
Program Title: Barnes and Nobles Book Application
File Description: The purpose of this program is to help students calculate the total number of books and book amount they purchased this month and determines the reward points. It uses loop and function.
"""

def get_total(number_of_books):
    total = 0
    for book in range(1, number_of_books + 1):
      price = float(input(f"Enter price for Book {book}: $"))
      total = total + price
    return total

def count_points(subtotal):
    if subtotal >= 100:
        return 100
    elif subtotal >= 80:
        return 80
    elif subtotal >= 60:
        return 60
    elif subtotal >= 40:
        return 40
    elif subtotal >= 20:
        return 20
    else:
        return 0

def show_receipt(subtotal, tax, final_price, points):
    print("*" *40)
    print("Receipt".center(40))
    print("*" *40)
    print(f"{'Sub Total:':>20} ${subtotal:>7.2f}")
    print(f"{'Taxes Owed:':>20} ${tax:>7.2f}")
    print("*" *40)
    print(f"{'Total:':>20} ${final_price:>7.2f}")
    print(f"{'Points Earned:':>20}  {points:>7.2f}")
    print("*" *40)

def main():
    number_of_books = int(input("How many books did you purchase this month? "))
    subtotal = get_total(number_of_books)
    tax = subtotal * 0.07
    final_price = subtotal + tax
    points = count_points(subtotal)
    show_receipt(subtotal, tax, final_price, points)

main()