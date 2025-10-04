# 代码生成时间: 2025-10-04 22:42:53
import pandas as pd
import requests
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(filename='price_monitor.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class PriceMonitor:
    """
    A class to monitor prices of a list of products.
    """"

    def __init__(self, product_list, url):
        self.product_list = product_list  # List of products to monitor
        self.url = url  # URL to fetch prices from
        self.previous_prices = {}  # Dictionary to store previous prices

    def fetch_price(self, product_id):
        """
        Fetch the current price of a product from the given URL.
        """"
        try:
            response = requests.get(f"{self.url}/{product_id}")
            response.raise_for_status()
            data = response.json()
            return data.get('price')
        except requests.RequestException as e:
            logging.error(f'Failed to fetch price for product {product_id}: {e}')
            return None

    def monitor(self):
        """
        Monitor the prices of all products and log any significant changes.
        """
        current_prices = {}
        for product_id in self.product_list:
            current_price = self.fetch_price(product_id)
            if current_price is not None:
                current_prices[product_id] = current_price
                if product_id in self.previous_prices:
                    if abs(current_price - self.previous_prices[product_id]) > 0.01:  # 1% change threshold
                        logging.info(f'Price change detected for product {product_id}: {self.previous_prices[product_id]} -> {current_price}')
                self.previous_prices[product_id] = current_price
            else:
                logging.warning(f'Price not found for product {product_id}')

        return current_prices

    def report(self):
        """
        Generate a report of the current prices.
        """
        current_prices = self.monitor()
        report = pd.DataFrame(list(current_prices.items()), columns=['Product ID', 'Current Price'])
        report.to_csv('price_report.csv', index=False)
        logging.info('Price report generated successfully.')

# Example usage
if __name__ == '__main__':
    products = ['product1', 'product2', 'product3']  # Replace with actual product IDs
    url = 'http://example.com/api/price'  # Replace with the actual API URL
    monitor = PriceMonitor(products, url)
    monitor.report()