import xml.etree.ElementTree as ET 
import json

tree = ET.parse("TP3_mouslim_beneddeb\BOOK.xml")
root = tree.getroot()
print("the getroot function :",root.tag)

print("\n------------------------------------\n")

#Task 1: Extract and print:

for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    print(f"Title : {title} | Author : {author}")
    
print("\n------------------------------------\n")

for magazine in root.findall("magazine"):
    editor = magazine.find("editor").text
    print(f"editor : {editor}")
    
print("\n------------------------------------\n")

#Task 2: Add a new book.

new_book = ET.Element("book") # create a new element book 
new_book.set("id","105") # give it the attribute ID 
title = ET.SubElement(new_book , "title") # create the a child named title (name of the tag is title )
title.text = "Data Science Fundamentals"  # set a text 
author = ET.SubElement(new_book , "author")
author.text = "Landa Green"
genre = ET.SubElement(new_book , "genre")
genre.text = "Data Science"
price = ET.SubElement(new_book , "price")
price.text = "40.99"
price.set("currency","USD")
published = ET.SubElement(new_book , "published")
published.text = "2023-11-20"
rating = ET.SubElement(new_book , "rating")
rating.text = "4.9"
root.append(new_book) # add the element new_book to the root

output = "TP3_mouslim_beneddeb\BOOK.xml"
tree.write(output) # write the new tree in the output file 
print("the book is added successfully")

print("\n------------------------------------\n")

#Task 3: Filter and print books published after 2022.

print("the books published after 2022 are : \n")
for book in root.findall("book"): # Loop through all elements named 'book' 
    date = book.find("published").text # to extract the date  
    date = date.split("-") # to split the list into the format YYYY-MM-DD 
    if int(date[0]) >= 2022: # Check if the year is greater than or equal to 2022
        print("-",book.find("title").text)
        
print("\n------------------------------------\n")

#Task 4: Convert the XML file to JSON with a separate list for books and magazines.

print("converting an XML file to JSON file .\n")
def xml_to_json(parent : ET.Element):
    d={} # Initialize the main dictionary
    for child in parent:  # Iterate over the child elements of the parent
        if child.tag not in d:  # Ensure each tag has its own list in the dictionary
            d[child.tag]=[]
        dic={} # Initialize a sub-dictionary for the current child element
        for child2 in child: # Iterate over the nested elements 
            if child2.tag not in dic: # Add the tag and its text content
                dic[child2.tag]=child2.text
        d[child.tag].append(dic) # Append the sub-dictionary to the corresponding list
    return d

print(xml_to_json(root))
data = xml_to_json(root)

# Write the dictionary to a JSON file
with open("TP3_mouslim_beneddeb\\data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)   # Save the dictionary to a file in JSON format with pretty formatting
    