str_row = "   tExT TeXt tExT   "

print(str_row[0])

new_str = str_row.lower()
new_str = str_row.upper()

new_str = str_row.strip(" t")
new_str = str_row.split("ExT")
new_str = str_row.replace(" ","|")
str_row = "..."
print("isspace:", str_row.isspace())
print("isnumeric:", str_row.isnumeric())
print("isalnum:", str_row.isalnum())

