import csv

def parse_csv(file_name):
	list_of_views = []

	with open(file_name, newline='') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in csvreader:
			list_of_views.append(row)

	return list_of_views

def find_page_paths_by_user(list_of_views):
	page_paths_by_user = {}

	for view in list_of_views:
		customer = view[1]
		page = view[2]
		if three_page_paths_by_user.has_key(customer):
			page_paths_by_user[customer].append(page)
		else:
			page_paths_by_user[customer] = [page]

	return page_paths_by_user


def find_three_page_paths(customer_page_paths):
	three_page_paths = {}

	for customer in customer_page_paths:
		page_path = customer_page_paths[customer]

		for i in range(len(page_path) - 2):
			three_page_path = page_path[i] + page_path[i + 1] + page_path[i + 2]
			three_page_path = ','.join(three_page_path)
			if three_page_paths.has_key(three_page_path):
				three_page_paths[three_page_path]+= 1
			else:
				three_page_paths[three_page_path] = 1

	return three_page_paths

def find_max_three_page_path(three_page_paths_dict):
	return max(three_page_paths_dict.keys(), key=(lambda path: three_page_paths_dict[path]))

if __name__ = "__main__":
	csv_file_name = input("Input csv file name: ")
	views = parse_csv(csv_file_name)
	user_page_paths = find_page_paths_by_user(views)
	triple_page_paths = find_three_page_paths(user_page_paths)
	max_three_page_path = find_max_three_page_path(triple_page_paths)

	print(max_occurring_three_page_path + " (" + triple_page_paths[max_three_page_path] + ")")


