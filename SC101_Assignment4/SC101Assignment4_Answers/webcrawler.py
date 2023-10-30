"""
File: webcrawler.py
Name: Rebecca
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        # extract all data under 'table' > 'class' > 't-stripe'
        tags = soup.find_all('table', {'class': 't-stripe'})
        # initialize the count
        boy_count = 0
        girl_count = 0

        for tag in tags:
            datas = tag.tbody.text.split('\n')  # extract data contains name and count
            for i in range(len(datas)-4):   # omit unrelated data in the list
                if len(datas[i]) > 4:   # omit rank
                    name_data = datas[i]
                    formatted_name_data = str(name_data).split(' ')    # formatted data into list
                    formatted_boy_count = int(formatted_name_data[1].replace(',', ''))
                    formatted_girl_count = int(formatted_name_data[3].replace(',', ''))
                    boy_count += formatted_boy_count
                    girl_count += formatted_girl_count

            print(boy_count)
            print(girl_count)


if __name__ == '__main__':
    main()
