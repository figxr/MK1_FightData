from bs4 import BeautifulSoup
import requests

characters = ['Ashrah', 'Baraka', 'General_Shao', 'Geras', 'Havik', 'Johnny_Cage', 'Kenshi', 'Kitana', 'Kung_Lao',
              'Li_Mei', 'Liu_Kang', 'Mileena', 'Nitara', 'Raiden', 'Rain', 'Reiko', 'Reptile', 'Scorpion',
              'Shang_Tsung', 'Sindel', 'Smoke', 'Sub-Zero', 'Tanya']

base_url = 'https://wiki.supercombo.gg/w/Mortal_Kombat_1/'

for character in characters:
    url = base_url + character
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        move_data_sections = soup.find_all(class_='movedata-flex-framedata-name')
        tables = soup.find_all('table', class_='wikitable citizen-table-nowrap')

        print(f"{character} Data:\n")

        for section, table in zip(move_data_sections, tables):
            move_name = section.get_text(strip=True)
            headers = [th.get_text(strip=True) for th in table.find('tr').find_all('th')]


            print(move_name)


            print('\t'.join(headers))


            for row in table.find_all('tr')[1:]:
                row_data = [td.get_text(strip=True) for td in row.find_all('td')]
                print('\t'.join(row_data))
            print("\n\n")

    else:
        print(f"{character} Data: Failed to retrieve the webpage\n\n\n")

