from wine_collect import wineInfo

def scraping_enoteca_wine_list():
    print("Here we run scrapipng Enoteca HP")
    wine1 = wineInfo.WineInfo("Clarendlle")
    wine2 = wineInfo.WineInfo("Château Latour")
    result = [wine1, wine2]
    return result

# Handler
def lambda_handler(event, context):
    wine_list = scraping_enoteca_wine_list()

    print("Printng all the Wine List: ")
    for wine in wine_list:
        print(wine)

    print("")
    print("Hello for WineCollector!!")