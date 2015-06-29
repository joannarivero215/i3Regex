'''
Some identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  a search for a specific character except new line
\b the white space around words 
\. a period

Some modifiers (...a type):
{1,3} expecting 1-3 of something 
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ match the beginning 
| either or
[] range or variance 
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

'''
# imports the regular expression moduel
import re 
text = ''' @obama did you see @scotus passed your laws'''                                         
output = re.findall(r'@([A-Za-z0-9_]+)', text) #(r'@([A-Za-z0-9_]+)') ## prints twitter names
# Join the matches together
out_twt = ",".join(output)
print out_twt
