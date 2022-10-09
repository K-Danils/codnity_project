import requests
from bs4 import BeautifulSoup
import os
from markupsafe import escape

class ArticleReader():
    def __init__(self, DB):
        self.db = DB
        pass

    def __get_html_of(self, url):
        if len(url) == 0:
            raise Exception("Url must not be empty")
            
        # beautiful soup the request of an html page
        return BeautifulSoup(requests.get(url).content, "html.parser")
    
    def __get_article_points(self, id):
        if id < 0 or id is None or not isinstance(id, int):
            raise Exception("Id must be positive integer")

        # get points of the specified article
        # first get the extended page of the article
        articles = self.__get_html_of(
            "https://news.ycombinator.com/item?id="+str(id))

        # then find the points, not every article has points, it can be None
        found_points = articles.find("span", class_="score")

        return found_points.text if found_points is not None else None
    
    def __print_help(self):
        print(
            "get: Update db with new articles\n"
            "update_all: Update article points\n"
            "update_<id>: Update points for specific article by id (example - update_1234)\n"
        )

    def get_new_articles(self):
        articles = self.__get_html_of("https://news.ycombinator.com/")

        # extract the data
        ids = articles.find_all("tr", class_="athing")
        titles = articles.find_all("span", class_="titleline")

        # not every article has points, so extract it's parents and
        # check if it has points in the loop below
        points_dates = articles.find_all("td", class_="subtext")

        # delete existing articles and replace them with the new ones later
        try:
            self.db.execute('''
                DELETE FROM articles
            ''')
        except Exception as e: print(e)


        for id, container in enumerate(points_dates):
            # only get the first 10 articles
            if id == 10:
                break

            # parse the parent where points and dates are located
            point_date_soup = BeautifulSoup(str(container), "html.parser")

            # here we check if the article has any points, it can be None
            found_points = point_date_soup.find("span", class_="score")

            # make a query to add all the gathered info
            try:
                self.db.execute(f'''
                    INSERT INTO articles (id, title, link, points, date_created)
                    VALUES (
                        '{int(ids[id]["id"])}', 
                        '{escape(titles[id].a.text)}',
                        '{escape(titles[id].a["href"])}',
                        '{int(found_points.text.replace(" points", "")) if found_points is not None else None}',
                        '{escape(point_date_soup.find("span", class_="age")["title"])}'
                        );
            ''')
            except Exception as e: print(e)

        return True

    def get_articles(self):
        return self.db.get_data()

    def update_all_article_points(self):
        try:
            for i, article in enumerate(self.db.get_data()):
                self.update_article(article['id'])
                os.system("cls")
                print(f"{i+1}0%")
        except Exception as e: print(e)

        return True

    def update_article(self, id):
        if not isinstance(id, int) or id < 1 or id == None:
            raise Exception("Id must be a positive integer and bigger than 0")

        # check if article exists in the db
        if len(list(filter(lambda data: data["id"] == id, self.db.get_data()))) < 1:
            raise Exception("Article could not be found, make sure the id has been entered correctly")
        
        # update a single article by provided id
        try:
            self.db.execute(f'''
                    UPDATE articles
                    SET points='{self.__get_article_points(id)}'
                    WHERE id='{id}'
                ''')
        except Exception as e: print(e)

        return True

    def menu(self):
        # used to display errors or success messages
        message = ""

        # initial welcoming and input
        inpt = print(
            "Welcome to codnity web scraping homework!\n")

        while True:
            # clear the screen and print the options again
            os.system("cls")
            self.__print_help()
            print("\n" + message)

            inpt = input().lower()

            # handling of the input
            if inpt == "get":
                if self.get_new_articles():
                    message = "Articles succesfully updated"
                else:
                    message = "Failed to update articles"

            elif inpt == "update_all":
                if self.update_all_article_points():
                    message = "Article points succesfully updated"
                else:
                    message = "Failed to update article points"

            elif "update_" in inpt:
                id = inpt.replace("update_", "")

                if self.update_article(int(id)):
                    message = id+"- article points succesfully updated"
                else:
                    message = id+"- article points failed to update"
