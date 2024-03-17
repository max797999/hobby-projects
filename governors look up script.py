governors = {
    'Alabama': 'Kay Ivey',
    'Alaska': 'Mike Dunleavy',
    'Arizona': 'Doug Ducey',
    'Arkansas': 'Asa Hutchinson',
    'California': 'Gavin Newsom',
    'Colorado': 'Jared Polis',
    'Connecticut': 'Ned Lamont',
    'Delaware': 'John Carney',
    'Florida': 'Ron DeSantis',
    'Georgia': 'Brian Kemp',
    'Hawaii': 'David Ige',
    'Idaho': 'Brad Little',
    'Illinois': 'J.B. Pritzker',
    'Indiana': 'Eric Holcomb',
    'Iowa': 'Kim Reynolds',
    'Kansas': 'Laura Kelly',
    'Kentucky': 'Andy Beshear',
    'Louisiana': 'John Bel Edwards',
    'Maine': 'Janet Mills',
    'Maryland': 'Larry Hogan',
    'Massachusetts': 'Charlie Baker',
    'Michigan': 'Gretchen Whitmer',
    'Minnesota': 'Tim Walz',
    'Mississippi': 'Tate Reeves',
    'Missouri': 'Mike Parson',
    'Montana': 'Greg Gianforte',
    'Nebraska': 'Pete Ricketts',
    'Nevada': 'Steve Sisolak',
    'New Hampshire': 'Chris Sununu',
    'New Jersey': 'Phil Murphy',
    'New Mexico': 'Michelle Lujan Grisham',
    'New York': 'Kathy Hochul',
    'North Carolina': 'Roy Cooper',
    'North Dakota': 'Doug Burgum',
    'Ohio': 'Mike DeWine',
    'Oklahoma': 'Kevin Stitt',
    'Oregon': 'Kate Brown',
    'Pennsylvania': 'Tom Wolf',
    'Rhode Island': 'Dan McKee',
    'South Carolina': 'Henry McMaster',
    'South Dakota': 'Kristi Noem',
    'Tennessee': 'Bill Lee',
    'Texas': 'Greg Abbott',
    'Utah': 'Spencer Cox',
    'Vermont': 'Phil Scott',
    'Virginia': 'Glenn Youngkin',
    'Washington': 'Jay Inslee',
    'West Virginia': 'Jim Justice',
    'Wisconsin': 'Tony Evers',
    'Wyoming': 'Mark Gordon',
}

while True:
    print ('welcome to State Governor look up')
    userinput = input(' Please enter look up or quit')
    
    def Look_up_Program():
     userinput = input('Please enter State name')
     print(governors.get(userinput))
    
    if userinput ==("look up"):
     Look_up_Program()
    

    if userinput == ("quit"):
     break