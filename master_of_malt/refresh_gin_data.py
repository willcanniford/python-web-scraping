# Imports
import helpers as hp

# Set the master link
url = "https://www.masterofmalt.com/gin/"
testing_url = "https://www.masterofmalt.com/gin/failures"

# Test the url checker against status code 200
print(hp.check_url_status_code(testing_url, 200))
print(hp.check_url_status_code(url, 200))

print(hp.get_pagination_links("https://www.masterofmalt.com/gin/"))
