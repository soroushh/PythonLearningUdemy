my_dict = {"soroush":"khosravi", "farnaz":"khosravi"}

for name,family in my_dict.items() :
    print(name +" "+ family)

universities = [
{"name":"MIT",
"location": "USA"},
{
"name":"Sharif",
"location": "Iran"
}
]

for uni in universities:
    print("The" + uni["name"] + "is located in " + uni["location"])
