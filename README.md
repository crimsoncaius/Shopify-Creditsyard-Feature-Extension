# Shopify Creditsyard Feature Extension

This project automates the process of rewarding store credit to customers through the CreditsYard API based on specific order criteria in a Shopify store.

## Overview

The script monitors Shopify orders and automatically awards store credit to customers when their order meets specific criteria. In this implementation, customers receive cashback (1.5% by default) when their total order quantity is a multiple of 6.

## Features

- Automatically checks new Shopify orders daily
- Awards store credit through CreditsYard API when order quantities are multiples of 6
- Tracks processed orders to prevent duplicate rewards
- Configurable cashback percentage and order quantity multiple

## Requirements

- Python 3.6+
- ShopifyAPI Python library
- Requests library

## Configuration

The application uses a `config.json` file for configuration:

```json
{
  "SHOPIFY_API_ACCESS_TOKEN": "your_shopify_access_token",
  "SHOPIFY_API_URL": "your_shopify_admin_url",
  "CREDITSYARD_API_URL": "creditsyard_api_endpoint",
  "CREDITSYARD_API_KEY": "your_creditsyard_api_key",
  "CASHBACK_AMOUNT": 0.015,
  "REASON": "Multiple Of 6 Discount",
  "MULTIPLE": 6,
  "ORDERIDSTORE_LOCATION": "orderIDstore.txt"
}
```

**Note:** The `config.json` file contains sensitive API keys and is excluded from version control via `.gitignore`.

## Usage

1. Clone the repository
2. Create and configure your `config.json` file with your API credentials
3. Install required dependencies:
   ```
   pip install shopify requests
   ```
4. Run the script:
   ```
   python script.py
   ```

For automated daily execution, consider setting up a cron job or scheduled task.

## Security Notes

- The `config.json` file contains sensitive API keys and should never be committed to version control
- The `orderIDstore.txt` file tracks processed orders and is also excluded from version control

## License

This project is proprietary and confidential.
