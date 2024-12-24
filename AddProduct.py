
page_name = "index.html"
page_content =""
starting_message ="<h3>EU Products with The best Price & Quality</h3>"

print("Enter the HTML block you want to insert (Type 'END' when finished):")
home_view = ""
while True:
    line = input()
    if line == "END":
        break
    home_view += line + "\n"

#home_view = input("Insert The Home View Code: ")
#product_view = input("Insert The Product View Code: ")

with open(page_name, "r") as file:
    page_content = file.readlines()

insert_position = None

for i, line in enumerate(page_content):
    if'<h3>EU Products with The best Price & Quality</h3>' in line:
        insert_position = i+1
        break

print("\n\n\n",home_view)

if insert_position is not None:
    page_content.insert(insert_position, home_view)
    
    with open(page_name, 'w') as file:
        file.writelines(page_content)
    print("HTML Successfully Updated")
else:
    print("inserting went wrong")
