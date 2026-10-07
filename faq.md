---
layout: default
title: FAQ and troubleshooting
permalink: /faq/
lede: Quick answers to the questions merchants ask most.
description: Answers to common Plinth questions and fixes for common setup issues.
---
## Setup

### The hero and flagship sections show the wrong product
They use **Theme settings > Brand > Flagship product**. If that's empty, they use the first product in the **Flagship collection**. Pick your hero product there. You can also set a custom image in the Hero section.

### How do I give my main product the long, detailed page?
Open the product in **Products**, set **Theme template** to **flagship** and save. Then edit that template in the theme editor (**Products > flagship** in the page selector). See [Getting started]({{ '/getting-started/' | relative_url }}#use-the-productflagship-template).

### My menu has no dropdowns
Dropdowns come from nested menu items. In **Content > Menus**, open your main menu and drag items under a parent item. Also check **Theme settings > Header > Menu** is set to that menu.

### My logo is too big or too small
Change **Desktop logo width** and **Mobile logo width** in **Theme settings > Logo**.

### The header shows my store name instead of my brand
Enter your brand in **Theme settings > Brand > Brand name**, or upload a logo in **Theme settings > Logo**.

## Product page

### There's no Buy it now button on my gift card
That's on purpose. Shopify's express checkout buttons can't carry gift card recipient details, so Plinth hides them on gift card products while the recipient form is on. To bring them back, turn off **Theme settings > Cart > Show recipient information form for gift card products**. That also removes the option to send the card to someone else.

### Complementary products don't show
They're chosen in the **Shopify Search & Discovery** app under **Product recommendations**. The section stays hidden until a product has some. Check that the section's **Type** is *Complementary products*.

### Related products don't show
Shopify needs some product and order data to generate them, so new stores may see none at first. The section hides itself when there's nothing to show.

### Pickup availability doesn't appear
Turn on local pickup for at least one location in **Settings > Shipping and delivery**, and make sure the variant has stock at that location.

### The subscription options don't appear
The product needs to be added to a selling plan (subscription) in your subscriptions app.

### Shop Pay Installments don't appear
Your store has to be eligible, with installments turned on in your Shop Pay settings. Availability depends on your country and the product price.

### The trust points under Add to cart are missing
They're blank by default, so you only show policies you really offer. Fill in each point in the **Trust strip** block of Product information.

### The reviews section is empty
Install a reviews app and add its block to the **Product reviews** section. Until then, the section doesn't show on your store.

## Cart, filters and selectors

### The cart drawer shows no suggestions
Set an **Add-ons collection** in **Theme settings > Brand**. Suggestions skip products already in the cart, so they disappear once everything's added.

### Where do shoppers enter a discount code?
At checkout. Automatic discounts and shared discount links apply in the cart. See [Cart > Discounts]({{ '/cart/' | relative_url }}#discounts).

### Filters don't appear on my collection
Install **Search & Discovery** and add filters there. Then check **Enable filtering** is on in the **Collection products** section. A filter only shows when the collection has products with values for it.

### The country or language selector doesn't appear
It needs more than one country in **Settings > Markets** (or more than one published language in **Settings > Languages**), and the matching setting turned on in the Header or Footer section.

### Social icons don't appear
Add your profile links in **Theme settings > Social media**, and check **Show social media icons** is on in the Footer section.

### Follow on Shop doesn't appear
It needs Shop Pay turned on for your store, and **Show Follow on Shop** on in the Footer section.

## General

### My changes don't show on my store
Check you're editing the published theme, then select **Save** in the theme editor. If you're editing a copy, use **Preview** or publish it. Browser caches can take a moment, so refresh the page.

### Can I edit the theme code?
Yes, through **⋯ > Edit code** in your theme library. Duplicate the theme first so you have a backup. Custom code changes aren't covered by theme support, and theme updates won't include them.

### How do I update Plinth?
When a new version is available, Shopify shows it in your theme library. Updating adds a new copy of the theme with your settings and content carried over. Review it, then publish. See the [Changelog]({{ '/changelog/' | relative_url }}) for what's new.

Still stuck? [Contact support]({{ '/support/' | relative_url }}).
