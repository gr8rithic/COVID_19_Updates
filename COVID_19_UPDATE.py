import requests

url = "https://api.covid19api.com/summary"

response=requests.get(url)
read_data=response.json()
#print(read_data)
for i in read_data.keys():
    if i=="Global":
        g=input("To know about currrent details")
        if g=="NewConfirmed":
            print(read_data["Global"][g])
        elif g=="TotalConfirmed":
            print(read_data["Global"][g])
        elif g=="TotalDeaths":
            print(read_data["Global"][g])
    elif i=="Countries":
        j=0
        q = input("Enter the country's Data you want to know")
        while(j<=300):
            #q=input("Enter the country's Data you want to know")
            if read_data[i][j]["Country"]==q:
                f=input("Get {}'s data".format(q))
                if f=="NewConfirmed":
                    print(read_data[i][j][f])
                elif f=="TotalConfirmed":
                    print(read_data[i][j][f])
                elif f=="NewDeaths":
                    print(read_data[i][j][f])
                elif f=="TotalDeaths":
                    print(read_data[i][j][f])
                break
            j+=1

