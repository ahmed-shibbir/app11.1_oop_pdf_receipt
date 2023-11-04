import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv")

print(df)
print(df.info())
article_id = int(input("Choose an articles to buy: "))

article_name = df.loc[df["id"]==article_id, "name"].squeeze()

print(article_name)

article_price = df.loc[df["id"]==article_id, "price"].squeeze()
print(article_price)

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Receipt nr.{article_id}", ln=1)

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Article: {article_name.title()}", ln=1)

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Price: {article_price}", ln=1)

pdf.output("receipt.pdf")



# Programme main loop:-
# print(df)
# article_id = input("Choose an articles to buy: ")
