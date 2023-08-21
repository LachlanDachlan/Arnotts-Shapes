import pandas


def currency(x):
  return "${:.2f}".format(x)

all_names = ["a", "b", "c", "d", "e"]

mini_movie_dict = {"Name": all_names,
                  "Ticket Price": all_ticket_costs,
                  "Surcharge": surcharge}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()
print(mini_movie_frame)

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
  mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f} ".format(profit))
