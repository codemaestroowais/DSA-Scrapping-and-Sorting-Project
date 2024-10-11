from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def extract_seller_name(text):
    pattern = r'([^()]+)\s+\(\d+\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return "N/A"

def extract_items_sold(text):
    pattern = r'\((\d+)\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  
    return "0"

def extract_reliability(text):
    pattern = r'(\d+\.\d+%)$'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  
    return "0"
