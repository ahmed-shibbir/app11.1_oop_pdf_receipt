import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv")


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == article_id, "price"].squeeze()

    def available(self):
        quantity = df.loc[df["id"] == self.id, "in stock"].squeeze()
        return quantity


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name.title()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


# Programme main loop:-
print(df)

item_id = int(input("Choose an articles to buy: "))

article = Article(article_id=item_id)

if article.available():
    receipt = Receipt(article=article)
    receipt.generate()
else:
    print("No available stock at the moment. Please try later")








######################################################################
## THIS WORKS:-
# class Receipt:
#     def __init__(self, article_id):
#         self.article_id = article_id
#         self.article_name = df.loc[df["id"] == self.article_id, "name"].squeeze()
#         self.article_price = df.loc[df["id"] == self.article_id, "price"].squeeze()
#
#     def generate(self):
#         pdf = FPDF(orientation="P", unit="mm", format="A4")
#         pdf.add_page()
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article_id}", ln=1)
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Article: {self.article_name.title()}", ln=1)
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)
#
#         pdf.output("receipt.pdf")
#
#
# # Programme main loop:-
# print(df)
#
# item_id = int(input("Choose an articles to buy: "))
# receipt_instance = Receipt(item_id)
# receipt_instance.generate()

########################################################################





## EXPERIMENTS:-
# class Articles:
#     def __init__(self, article_id):
#         self.article_id = article_id
#
#     def get_article_name(self):
#         article_name = df.loc[df["id"] == article_id, "name"].squeeze()
#         return article_name
#
#     def get_article_price(self):
#         article_price = df.loc[df["id"] == article_id, "price"].squeeze()
#         return article_price
#
#
# class Pdf:
#     def __init__(self, article_id):
#         self.article_id = article_id
#         self.article_name = Articles.get_article_name
#         self.article_price = Articles.get_article_price
#
#     def receipt(self):
#         pdf = FPDF(orientation="P", unit="mm", format="A4")
#         pdf.add_page()
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article_id}", ln=1)
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Article: {self.article_name.title()}", ln=1)
#
#         pdf.set_font(family="Times", size=16, style="B")
#         pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)
#
#         pdf.output("receipt.pdf")
#
# #Programme main loop:-
# print(df)
#
# article_id = int(input("Choose an articles to buy: "))
# articles = Articles(article_id)
#
# article_name = articles.get_article_name()
#
# article_price = articles.get_article_price()
#
# receipt = Pdf(article_id)
# print(Pdf.receipt)