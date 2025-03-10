import shopify
import requests
import json

from datetime import timedelta, date

config = json.load(open("config.json"))

url = config["CREDITSYARD_API_URL"]

headers = {
    "X-Shop-Api-Key": config["CREDITSYARD_API_KEY"],
    "Content-Type": "application/json",
    "User-Agent": "PostmanRuntime/7.32.2",
}

cashbackAmount = config["CASHBACK_AMOUNT"]
reason = config["REASON"]
multiple = config["MULTIPLE"]


# function to call CreditsYard API
def AdjustValue(email, amount, id):
    # check if order is already in
    with open(config["ORDERIDSTORE_LOCATION"], "r") as f:
        ordersIn = f.read().split()

    payload = {
        "customer_email": email,
        "amount": float(amount) * cashbackAmount,
        "reason": reason,
    }

    if str(id) not in ordersIn:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            # Successful response
            f = open(config["ORDERIDSTORE_LOCATION"], "a")
            f.write(" " + str(id))
        else:
            # Error response
            print(f"Request failed with status code {response.status_code}")
    else:
        print(id, "already given Store Credit")


session = shopify.Session(
    config["SHOPIFY_API_URL"],
    "2023-04",
    config["SHOPIFY_API_ACCESS_TOKEN"],
)

shopify.ShopifyResource.activate_session(session)

today = date.today()
yesterday = date.today() - timedelta(days=1)

# getting order
orders = shopify.Order.find(created_at_min=yesterday, create_at_max=today)

# looping through orders
for order in orders:
    totalQuantity = 0

    # getting total quantity
    for line_item in order.line_items:
        totalQuantity += line_item.quantity

    # check if multiple
    if totalQuantity % multiple == 0:
        AdjustValue(order.email, order.total_price, order.id)
