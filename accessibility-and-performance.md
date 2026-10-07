---
layout: default
title: Accessibility and performance
permalink: /accessibility-and-performance/
lede: Plinth is built so more people can shop your store, quickly, on any device. Here's what's built in and what's up to you.
description: Accessibility and performance features in Plinth, plus a checklist for merchants.
---
## Accessibility built in

Plinth is designed and tested against the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA, with automated checks and keyboard and screen reader testing on its main pages.

- **Keyboard support everywhere:** menus, dropdowns, the cart drawer, filters, search suggestions, the media gallery and hotspots all work without a mouse. A **Skip to content** link comes first on every page.
- **Clear focus outlines** show where keyboard users are.
- **Screen reader support:** form fields have visible labels; errors are announced and linked to their fields; the cart drawer and other panels behave as proper dialogs; and changes like "Added to cart" or search result counts are announced.
- **High-contrast default colors** that comfortably exceed the 4.5:1 contrast minimum for text.
- **Large tap targets** of at least 44 × 44 pixels for key buttons on touch screens.
- **Works without JavaScript:** buying, filtering, the gift card form and the country and language selectors still work if scripts fail to load.
- **Respects reduced motion** settings on the shopper's device.

## Your accessibility checklist

Some things depend on your content. Please check:

- **Alt text** on every product, collection and section image. Describe what's shown in a short phrase, such as "Black keyboard with lime coiled cable". Leave it out only for purely decorative images.
- **Color contrast** if you change theme colors. Body text needs at least 4.5:1 against its background. Use a free contrast checker to test your colors.
- **Link and button text** that makes sense on its own. "Shop the collection" is clearer than "Click here".
- **Video captions** for any video with speech.
- **Custom code and apps** from Custom Liquid sections or third-party apps. Plinth can't check these, so test them with a keyboard.

## Performance built in

- **Lightweight:** no large JavaScript libraries, and scripts load without blocking the page.
- **Critical styles are inlined**, so the page starts drawing right away.
- **Responsive images:** each visitor downloads an image sized for their screen. Below-the-fold images load only as shoppers scroll.
- **Heavy media waits:** videos and 3D models load only when a shopper presses play or view.
- **Recommendations load after the page**, so they never slow down the first view.

## Keep your store fast

- **Upload images at sensible sizes.** Around 2000 pixels wide is plenty for product images. Shopify serves smaller versions automatically.
- **Be selective with apps.** Each app can add its own scripts. Remove apps you no longer use, and check that their code was removed too.
- **Limit autoplaying media** and large videos near the top of the page.
- **Check your speed report** in **Online Store > Themes**, or test pages with a free tool such as PageSpeed Insights.
