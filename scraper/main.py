import requests
import utils
from bs4 import BeautifulSoup, _typing

URL: str = "https://books.toscrape.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
} 

def main():
    response: requests.models.Response = requests.get(URL,headers=headers)

    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

        booksList: list = soup.find_all("article", class_="product_pod")

        print(f"Find {len(booksList)} books in this page:")

        for book in booksList:
            title: str = book.h3.a["title"]
            price: str = book.find("p",class_="price_color").text
            stars: str = book.find("p",class_="star-rating")["class"][1]
            stock: str = book.find("p",class_="instock")["class"][1]

            result: list[str] = [title,price,stars[1],stock]

            print(utils.list_processing(result))

    else:
        print(response.status_code)

if __name__ == "__main__":
    main()
