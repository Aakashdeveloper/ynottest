#Developed By Aakash Handa

'''sys module provides information about constants, functions 
and methods of the Python interpreter.
re module use for regex and pattern matching'''
import sys
import re


def extract_babyname(htmlfile):
  
  # Open html file and read content.
  f = open(htmlfile, 'r')
  text = f.read()

  data = []
  # Search data in html tag with regex
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  #print(tuples)

  # Read Data from tuple as current output of tuple is
  # (1, 'abc', 'def')
  names_count =  {}
  for final_tuple in tuples:
    (count, name1, name2) = final_tuple 
    if name1 not in names_count:
      names_count[name1] = count
    if name2 not in names_count:
      names_count[name2] = count

  sorted_names = sorted(names_count.keys())

  for name in sorted_names:
    data.append(name + " " + names_count[name])

  return data

# extract_babyname('baby1990.html')
def main():
  args = sys.argv[1:]

  if not args:
    print 'Add paramter with filename: [--summaryfile] file [filename]'
    sys.exit(1)

  # default summary is true, update variable if user send flag.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for htmlfilename in args:
    print(">>>>>",htmlfilename)
    names = extract_babyname(htmlfilename)
    text = '\n'.join(names)
    #Open the file and insert value in the text file
    if summary:
      outf = open(htmlfilename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print names

if __name__ == '__main__':
  main()