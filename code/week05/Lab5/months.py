#primes.py
#A program that creates a tuple of months and seasons
#Shane Austin

months = ("November",
            "December",
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October"            
            
)

season = ("Spring", "Summer", "Autumn", "Winter")

winter = months[0:3]
spring = months[3:6]
summer = months[6:9]
autumn = months[9:12]

for month in autumn:
    print(month)