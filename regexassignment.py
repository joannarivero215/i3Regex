''' For this assignment you should create your own regex program that 
takes input from your twitter text file and finds the patter that will
allow you to extract string in "text":"Supreme Court Declares Bans on 
Same-Sex Marriage Unconstitutional http:\/\/t.co\/HQbVO988L0  #SCOTUS 
#Lovewins". 
'''



# below this line import the regular expression moduel

# below this line open your .txt file using "with" so the file will automatically be closed
with open(filename, "r") as somename :
# below this line read the file using .read and assign it a new var name

# below this line implement a finallsearch calling module re (i.e., re.findall)
# the expression should search for text and print everything between " "
            
# Join the matches together. I did this step for you. Instead of printing 
#all on one line, escape using new line
out_twt = ",".join(output)
print out_twt
# Write the output to a new file, again using "with", you might need to 
# change a parameter in the syntax https://docs.python.org/2/tutorial/inputoutput.html

# below this line you need to write the output to the file above
