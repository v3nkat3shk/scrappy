import scrape
import csv

url_list = [
    'https://www.etsy.com/listing/949580183/baby-riding-a-cow-earrings-7-colours?external=1&ref=hp_top_in_taxo-1-1&bes=1',
    'https://www.etsy.com/listing/683116487/raw-kokum-butter-100-pure-organic-great',
    'https://www.etsy.com/listing/789745301/forget-me-not-necklace-seed-of-loss-seed',
    'https://www.etsy.com/listing/835396469/transparent-tiktok-bright-neon-dinosaur?ref=hp_ifq',
    'https://www.etsy.com/in-en/listing/1025559267/handwriting-wallet-leather-wallet-for',
    'https://www.etsy.com/in-en/listing/990762977/personalized-name-necklace-by',
    'https://www.etsy.com/in-en/listing/667282692/valentines-day-gift-for-himpersonalized',
    'https://www.etsy.com/in-en/listing/1015120148/romantic-personalized-record-birthday',
    'https://www.etsy.com/in-en/listing/951172360/heart-keychain-set-made-with-authentic',
    'https://www.etsy.com/in-en/listing/1138724248/solar-outdoor-hanging-lanterns-pack-of-4',
    'https://www.etsy.com/in-en/listing/1166244960/live-cactus-plant-wholesale-54-plants-in',
    'https://www.etsy.com/in-en/listing/171184437/handmade-pottery-gnome-garden-stake',
    'https://www.etsy.com/in-en/listing/522138659/illustrated-floral-removable-wallpaper',
]

headers = [
    'Product Link', 'In Stock', 'Options', 'Title & Author', 'Shipping Time', 'Price', 'Description', 'Store', 'Categories', 'Created', 'Country Of Origin', 'Image Link'
]


def main():

    results = scrape.go_scrape(urls=url_list)
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in results:
            writer.writerow(row)


if __name__ == '__main__':
    main()
