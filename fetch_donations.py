import requests
from bs4 import BeautifulSoup


# Function to login and fetch donation data
def fetch_donation_data():
    # Your login credentials
    username = 'your_username'
    password = 'your_password'

    # Login URL
    login_url = 'https://danamojo.org/login'

    # Donation page URL
    donation_url = 'https://danamojo.org/dm/admin/dashboard'

    # Session object to persist the login session
    session = requests.Session()

    # Login payload
    login_data = {
        'username': AAKCM6856B,
        'password': u7dFcv
    }

    # Perform login
    login_response = session.post(login_url, data=login_data)

    # Check if login was successful
    if login_response.status_code == 200:
        print("Login successful")
        # Fetch donation page after login
        donation_response = session.get(donation_url)
        if donation_response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(donation_response.content, 'html.parser')
            # Find the donation amount element
            donation_amount_element = soup.find('div', class_='col-lg-3').find('h3')
            if donation_amount_element:
                # Extract donation amount text
                donation_amount = donation_amount_element.text.strip()
                print("Total donation amount this month:", donation_amount)
                return donation_amount
            else:
                print("Donation amount element not found")
        else:
            print("Failed to fetch donation page:", donation_response.status_code)
    else:
        print("Login failed:", login_response.status_code)

    return None

# Run the function
donation_amount = fetch_donation_data()

# Write donation amount to a JSON file
if donation_amount:
    with open('donation_amount.json', 'w') as json_file:
        json.dump({'donation_amount': donation_amount}, json_file)
