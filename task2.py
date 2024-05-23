import re
import sys


#print (sys.argv[0])
file1 = open('log_task2.txt', encoding='utf-8')
Lines = file1.readlines()

file2=open('output_task2.txt',"w",encoding='utf-8')

def calculate_time(date):

    match= re.findall(r'^[0-9]*\/',date)
    for DD in match:
        DD = re.sub('\/','',DD)

    #print(DD)
    match1= re.findall(r'\/[A-Za-z][a-z][a-z]\/',date)
    for MM in match1:
        MM = re.sub('\/','',MM)

    #print(MM)

    match2= re.findall(r'\/[0-9]*\:',date)
    for YY in match2:
        YY = re.sub('\/','',YY)
        YY = re.sub('\:','',YY)
    #print(YY)

    match3= re.findall(r'\:[0-9]*\:[0-9]*\:',date)
    hh=""
    mm=""
    for time in match3:
        hh= re.sub(r'\:[0-9]*\:$','',time)
        mm = re.sub(r'\:[0-9]*\:','',time)
        hh = re.sub('\:','',hh)
        mm = re.sub('\:','',mm)
        
    #print(hh)
    #print(mm)

    match4= re.findall(r'\:[0-9]*$',date)
    for ss in match4:
        ss = re.sub('\:','',ss)
    #print(ss)
        
    Access_time =0

    #print(sys.argv[2])
    Access_time += int(DD)* 86400

    if(MM=='Jan'):
        Access_time += 1*2628288
    elif(MM=='Feb'):
        Access_time += 2*2628288
    elif(MM=='Mar'):
        Access_time += 3*2628288
    elif(MM=='Apr'):
        Access_time += 4*2628288
    elif(MM=='May'):
        Access_time += 5*2628288
    elif(MM=='Jun'):
        Access_time += 6*2628288
    elif(MM=='Jul'):
        Access_time += 7*2628288
    elif(MM=='Aug'):
        Access_time += 8*2628288
    elif(MM=='Sep'):
        Access_time += 9*2628288
    elif(MM=='Oct'):
        Access_time += 10*2628288
    elif(MM=='Nov'):
        Access_time += 11*2628288
    elif(MM=='Dec'):
        Access_time += 12*2628288
        
    Access_time += (int(YY)-1970) * 31536000
    Access_time += int(hh) * 3600
    Access_time += int(mm) * 60
    Access_time += int(ss)

    return Access_time
    

def task2():
    counts = dict()
    Start_Date = calculate_time(sys.argv[1])
    ip_addresses =""
    
    dates = dict()
    Stop_Date = Start_Date+ int(sys.argv[2])
    i=1
    SOURCE = sys.argv[3]
    #print(Start_Date)
    #print(Stop_Date)
                
    last_ip=""
    for line in Lines:
        
        matchOb1 = re.findall(rf'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]* - - \[[0-9]*\/[A-Z][a-z]*\/[0-9]*\:[0-9]*\:[0-9]*\:[0-9]* \+[0-9]*\] \"GET {SOURCE}',line)# (\w){SOURCE}\b(\w)',line)#[a-zA-Z\\0-9\^\<\>\%\.\:\,\;\_\+\&\^\#\'\\\*\{\}\/\-\|\[\]\-\"\=\?]*', line) 
        for newLine in matchOb1:#GETLERI IHTIYACIM OLAN YERE KADAR GETIRIYOR.
            #file2.write(str(i)+ " " + newLine+'\n');
            #print(newLine)
            matchOb2 = re.findall(r'\[[0-9]*\/[A-Z][a-z]*\/[0-9]*\:[0-9]*\:[0-9]*\:[0-9]* \+[0-9]*]',newLine)
            for date in matchOb2:
                #print(str(i)+ " " +date)
                date= re.sub('\[','',date)
                date = re.sub(r'\+[0-9]*','',date)
                date = re.sub('\]','',date)
                date = re.sub(' ', '', date)
                access_time=calculate_time(date)
                #print(access_time)
                #print(Start_Date)
                #print(Stop_Date)
                if(Start_Date <= access_time and access_time < Stop_Date):
                   
                    matchOb3 = re.findall(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*',newLine)
                    for ip in matchOb3:
                        last_ip=ip           
                        ip_addresses +=  ip + " "                    
                        if last_ip not in dates:
                            dates[last_ip]= access_time
                    
                    
    ips = ip_addresses.split()
    #print (ip_addresses)
    for ip in ips:
        if ip in counts:
            counts[ip] +=1
        else:
            counts[ip] =1
    
    #print(counts)           
    #print(dates)
    #print(counts['1.0.0.2'])
    #print(counts.__len__)
    #for ip in range(counts.__len__):
     #   print(counts[ip])
    
    
    counts =sorted(counts.items(), key=lambda x:x[1], reverse=True)
    for count in counts:
        file2.write(count[0]+ " "+ str(count[1])+ " " + str(dates[count[0]]) + "\n")
    
        
if __name__ == '__main__':
    task2()
    