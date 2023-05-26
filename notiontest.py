import json
import logging
import os
import requests
from datetime import datetime,timedelta
import re


key = 'secret_juOVJ3rTPEfyHQlaAc4zGcyzIk7kvPcPLerGKLE3V6Q'
database = '08387bf6657145d3ad3afd604b3f678d'

class notion_client:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.key = os.getenv('NOTION_KEY')
        self.database_id = os.getenv('NOTION_DATABASE_ID')

        self.query_url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        self.page_url = "https://api.notion.com/v1/pages" 
        self.block_url = "https://api.notion.com/v1/blocks/"
        self.database_url = "https://api.notion.com/v1/databases"

        self.headers = {
            'Authorization': f'Bearer {self.key}',
            "Notion-Version": "2022-02-22",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }