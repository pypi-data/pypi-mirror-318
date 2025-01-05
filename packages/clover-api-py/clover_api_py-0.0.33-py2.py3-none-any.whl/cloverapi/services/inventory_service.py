from cloverapi.helpers.http_helper import HttpServiceBase
from cloverapi.helpers.logging_helper import setup_logger
from cloverapi.helpers.date_helper import DateHelper
from typing import Union, Dict

# Setup logger for InventoryService
logger = setup_logger("InventoryService")

class InventoryService(HttpServiceBase):
    def __init__(self, headers, base_url, merchant_id, date_helper: DateHelper):
        """
        Initialize the InventoryService.

        :param headers: HTTP headers for the API requests.
        :param base_url: Base URL for the Clover API.
        :param merchant_id: Merchant ID for the Clover account.
        :param date_helper: An instance of DateHelper for date-related utilities.
        """
        super().__init__(headers, base_url, merchant_id)
        self.date_helper = date_helper

    def get_inventory(self, period=None, expand_details=False, offset=0, limit=100):
        """
        Retrieve all inventory items with optional filters and expansions.

        :param period: item modified period (e.g., 'day', 'week', 'month', etc.) or an integer for last n days.
        :param expand_details: If True, expand details like price and itemStock.
        :param offset: Pagination offset.
        :param limit: Number of items per request.
        :return: List of all inventory items.
        """
        filters = []
        params = {'offset': offset, 'limit': limit}

        # Apply the date range filter
        if period:
            start, end = self.date_helper.filters_period(period)  # Use the date_helper instance method
            filters.append(f"modifiedTime>={start}")
            filters.append(f"modifiedTime<={end}")

        # Add filters to params
        if filters:
            params['filter'] = filters

        # Add expand details if requested
        if expand_details:
            params['expand'] = "price,itemStock"

        logger.info(f"Fetching inventory with filters: {filters} and expand: {expand_details}")
        return self._get_data("items", params)

    def get_item_detail(self, item_id: str, expand: str = None) -> dict:
        """
        Fetch details for a specific inventory item by its ID.

        :param item_id: The ID of the inventory item.
        :param expand: Optional parameter to include additional details (e.g., itemStock).
        :return: Dictionary containing item details.
        """
        logger.info(f"Fetching details for item ID: {item_id} with expansion: {expand}")
        params = {"expand": expand} if expand else {}
        return self._get_data(f"items/{item_id}", params=params, paginated=False)

    def update_item_detail(self, item_id: str, item_data: dict) -> dict:
        """
        Update an existing inventory item.

        :param item_id: The ID of the inventory item to update.
        :param item_data: Dictionary containing the item details to update.
        :return: Updated item details or error message.
        """
        logger.info(f"Updating item ID: {item_id} with data: {item_data}")
        endpoint = f"items/{item_id}"
        return self._post_data(endpoint, item_data)

    def get_item_stock(self, item_id: str) -> Dict:
        """
        Fetch stock details for a specific inventory item by its ID.

        :param item_id: The ID of the inventory item.
        :return: Dictionary containing stock details (stockCount and quantity).
        """
        logger.info(f"Fetching stock details for item ID: {item_id}")
        stock_details = self._get_data(f"item_stocks/{item_id}", paginated=False)
        if stock_details:
            logger.debug(f"Stock details fetched: {stock_details}")
        else:
            logger.warning(f"No stock details found for item ID: {item_id}")
        return stock_details

    def update_item_stock(self, item_id: str, stock_count: int):
        """
        Update the stock count for a specific item.

        :param item_id: ID of the inventory item.
        :param stock_count: New stock count to set.
        :return: Response from the API.
        """
        logger.info(f"Updating stock for item ID {item_id} to {stock_count}")
        return self._post_data(f"item_stocks/{item_id}", {"quantity": stock_count})