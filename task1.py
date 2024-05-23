import re
def task1():
    file1 = open('log_task1.txt', encoding='utf-8')
    Lines = file1.readlines()
    # Strips the newline character
    file2=open('output_task1.txt',"w",encoding='utf-8')
    
    lineoutput=''
    i=1
    for line in Lines:
        
        matchOb1 = re.findall(r'^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]* - - \[[0-9]*\/[A-za-z]*\/[0-9][0-9][0-9][0-9]', line)
        
        for newLine in matchOb1:
            #print(newLine+ " "+ str(i))
            newLine= re.sub('-','',newLine)
            newLine = re.sub(' ','x', newLine)
            newLine = re.sub('xxx',' ', newLine)
            newLine = re.sub('\[','',newLine)
            newLine = re.sub('\]','',newLine)
            newLine = re.sub('\/','-',newLine)
            #print(newLine +" " + str(i))
            file2.write(newLine+'\n');
        
        i=i+1         

if __name__ == '__main__':
    task1()
    