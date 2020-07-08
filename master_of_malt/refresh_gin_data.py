# Imports
import helpers as hp

url = "https://www.masterofmalt.com/gin/"
cookies = {"MaOMa": "VisitorID=797957185&CountryCodeShort=GB&IsVATableCountry=1&CountryID=464&CurrencyID=-1"
                    "&DeliveryCountrySavedToDB=1"}
headers = {"Accept-Language": "en-GB",
           "User-Agent": "APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)"}

page_cursor = 100
increment = 5
found_max = -1
last_status = 'NA'
final_page_found = False

while not final_page_found:
    url_to_check = "https://www.masterofmalt.com/gin/{}/".format(page_cursor)
    response = hp.check_page_exists(url=url_to_check, cookies=cookies, headers=headers)
    print(url_to_check, response)

    if response:
        if not last_status:
            final_page_found = True
        else:
            page_cursor = page_cursor + 5
    else:
        page_cursor = page_cursor - 1

    last_status = response

print("Maximum page found: {}".format(page_cursor))
