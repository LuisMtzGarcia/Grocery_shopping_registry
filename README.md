# Grocery_shopping_registry
WebApp to track and visualize grocery shopping expenses. Project focused on 
building a CRUD application.

(Create, Read, Update, Delete)

[Visit the site](https://registro-super.herokuapp.com/)

The site is hosted on Heroku, please be patient with the dyno's wake-up time.

## Introduction
This project aims to offer users a simple and effective way to register and track 
their shopping expenses.

Purchases have the following attributes:
* Name of the product
* Category
* Quantity bought
* Total price of the purchase
* Bulk purchase or not

Users have two options to visualize their purchases:
* By day, which displays the purchases made on a certain day.
* By month, which displays all the purchases made in the desired month.

This was a practice project aimend on building a CRUD application and deepening 
my handling of the back-end and the front-end of a website.

## Technologies
* Django  4.0
* Django-bootstrap5 21.3
* Python 4.0
* Bootstrap 5
* Plotly 5.4.0

## How to use

### First of all, I wanna show off the "Register a purchase" form.

It was the hardest part of the whole ordeal, I had to learn a lot of stuff really quickly just to style the damn thing.

Here it is, in all its glory:

<p align="center">
  <img src="https://i.imgur.com/9hgz4Xb.png">
</p>

*Chef's kiss* Truly the epitome of form building. A Mona Lisa of the front-end work, if you will.

Now, let me remove my self-contratulation cap and continue.

### Demo account

If you just want to see a demonstration of the site, I invite you to use the demo
 account.

Access the login page using the dropdown menu.

![Dropdown menu](https://i.imgur.com/zeWboN3.png "Dropdown menu")

And use the credentials provided. This account has some purchases registered so
 visitors can use them as examples.
It doesn't have permissions to modify or delete these purchases, nor permission to
 register new purchases.

![Login](https://i.imgur.com/imx2NwP.png "Login")

Then, using the dropdown menu, choose a visualization.
* Per day
* Per month

![Choosing visualization](https://i.imgur.com/8TiLZmA.png "Choosing visualization")

## Visualizations

### Per day

You can select a day that has a registered purchase and view related information of those purchases.

![Day select](https://i.imgur.com/SpejD4w.png "Day select")

Once selected, all information will be displayed.

![Day 1](https://i.imgur.com/s01IPE5.png "Day 1")

![Day 2](https://i.imgur.com/K8pvaGH.png "Day 2")

![Day 3](https://i.imgur.com/skQbkzD.png "Day 3")

![Day 4](https://i.imgur.com/cqtqbHa.png "Day 4")

### Per month

You can select a month with registered purchases and view related information of those purchases.

![Month 1](https://i.imgur.com/Z6XSPCV.png "Month 1")

![Month 2](https://i.imgur.com/WR1GdPH.png "Month 2")

![Month 3](https://i.imgur.com/6euXZzN.png "Month 3")

![Month 4](https://i.imgur.com/B3DVmkv.png "Month 4")

![Month 5](https://i.imgur.com/90I8gQf.png "Month 5")