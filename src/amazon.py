from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import pandas as ps

driver = webdriver.Chrome('/home/v9/dev/scrappy/env/bin/chromedriver')

amazons_products = [
    "https://www.amazon.ca/Pampers-Diapers-Size-Disposable-Waistband/dp/B08PX1JKYQ?th=1",
    "https://www.amazon.ca/Peel-Stick-LEGO%C2%AE-Compatible-Baseplates/dp/B075LP8G7K?th=1",
    "https://www.amazon.ca/Sillbird-Science-Engineering-Educational-Building/dp/B082B72NYY",
    "https://www.amazon.ca/STEM-Educational-Tank-Building-Blocks/dp/B07HKGX4V6",
    "https://www.amazon.ca/Kid-Friendly-Plastic-Building-Toddlers-Dimple/dp/B079MDLGT8",
    "https://www.amazon.ca/Spike-the-Fine-Motor-Hedgehog/dp/B078WM314M",
    "https://www.amazon.ca/Melissa-Doug-Primary-Lacing-Beads/dp/B00272N8L2",
    "https://www.amazon.ca/Learning-Resources-Jumbo-Animals-Forest/dp/B001SH1RM4",
    "https://www.amazon.ca/ACTION-AIR-Inflatable-Backyard-Material/dp/B07G3S6VL1",
    "https://www.amazon.ca/KIDCHEER-Activity-Building-Compatible-Activities/dp/B08BRDPPTY",
    "https://www.etsy.com/listing/949580183/baby-riding-a-cow-earrings-7-colours?external=1&ref=hp_top_in_taxo-1-1&bes=1",
    "https://www.etsy.com/listing/683116487/raw-kokum-butter-100-pure-organic-great",
    "https://www.etsy.com/listing/859099243/loch-ness-monster-necklace-baby-nessie?ref=hp_ifq",
    "https://www.etsy.com/listing/789745301/forget-me-not-necklace-seed-of-loss-seed",
    "https://www.etsy.com/listing/835396469/transparent-tiktok-bright-neon-dinosaur?ref=hp_ifq",
    "https://www.etsy.com/in-en/listing/1025559267/handwriting-wallet-leather-wallet-for",
    "https://www.etsy.com/in-en/listing/990762977/personalized-name-necklace-by",
    "https://www.etsy.com/in-en/listing/667282692/valentines-day-gift-for-himpersonalized",
    "https://www.etsy.com/in-en/listing/1015120148/romantic-personalized-record-birthday",
    "https://www.etsy.com/in-en/listing/951172360/heart-keychain-set-made-with-authentic",
    "https://www.etsy.com/in-en/listing/1138724248/solar-outdoor-hanging-lanterns-pack-of-4",
    "https://www.etsy.com/in-en/listing/1166244960/live-cactus-plant-wholesale-54-plants-in",
    "https://www.etsy.com/in-en/listing/702456259/mini-greenhouse-with-grow-lights-sezam",
    "https://www.etsy.com/in-en/listing/171184437/handmade-pottery-gnome-garden-stake",
    "https://www.etsy.com/in-en/listing/522138659/illustrated-floral-removable-wallpaper",
]


def go_scrape(urls: list, driver) -> list:
    for url in urls:
        scrape(url, driver)


def scrape(url, driver):
    driver.get(url)
    print(get_stock_information)
    print(get_title)
    print(get_shipping_details)
    print(get_price)
    print(get_discription)
    print(get_store)


def get_stock_information(driver):
    """
    Gets if the product is in stock or not
    """
    div = driver.find_element(By.ID, 'availability')
    stock_info = div.find_element(
        By.TAG_NAME, 'span').get_attribute("textContent")
    if "out of stock" in stock_info:
        return 'X'
    else:
        return ''


def get_shipping_details(driver):
    """
    Get delivery information for the product
    """
    stock = get_stock_information(driver=driver)
    if stock != 'X':
        div = driver.find_element(
            By.ID, 'mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE')
        delivery_price = div.find_element(
            By.TAG_NAME, 'a').get_attribute("textContent").strip()
        delivery_date = div.find_element(
            By.CLASS_NAME, 'a-text-bold').get_attribute("textContent").strip()
        return f"{delivery_price}\n{delivery_date}"
    else:
        return ''


def get_discription(driver):
    """
    Gets the product discription
    """
    disc = driver.find_element(By.ID, 'feature-bullets')
    list_item = disc.find_elements(By.CLASS_NAME, 'a-list-item')
    discription = ""
    for el in range(len(list_item)):
        discription += f"{list_item[el].text}\n"
    return discription.strip()


def get_price(driver):
    """
    Gets the price of the product
    """
    return driver.find_element(By.XPATH, '//span[@class="a-offscreen"]').get_attribute("textContent").strip()


def get_title(driver):
    """
    Gets the title of the product
    """
    return driver.find_element(By.ID, "productTitle").text


def get_store(driver):
    """
    Get store link
    """
    div = driver.find_element(By.ID, "bylineInfo_feature_div")
    return div.find_element(By.TAG_NAME, 'a').get_attribute("href").strip()


scrape("https://www.amazon.ca/ACTION-AIR-Inflatable-Backyard-Material/dp/B07G3S6VL1",
       driver=driver)
