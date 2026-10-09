---
layout: default
title: Changelog
permalink: /changelog/
lede: What's new in each version of Plinth.
description: Plinth release notes.
---
## 1.1.5

*October 2026*

### Changed

- **Lighter blog and content pages.** The product form script now loads only on pages that show a product form (product pages and the Featured product section), so pages, blog posts and the blog index load less JavaScript. Blog post and blog index images are requested at sizes closer to how they're displayed, and the first blog index image loads with high priority. Product gallery images now use the same set of image sizes as the hero, Featured product and Product hotspots sections, so when one image appears in more than one section the browser downloads it only once.

### Fixed

- **Spacing above sections that follow page content.** When a page has another section below its content, such as the accordion on the FAQ page, the gap between them is now half as large.

## 1.1.4

*October 2026*

### Changed

- **More readable pages and blog posts.** Pages, blog posts and the blog index now keep text to a comfortable line length (about 70 characters), with more space between paragraphs, headings, lists, quotes, images and tables. Blog posts show the blog name, a larger title and the date and author more clearly, and featured images load at the right size for each screen. The blog index shows each post as a card with its image, title, date and excerpt. Product descriptions use a more compact version of the same text styles.

### New

- **Content width setting.** The Page, Blog post and Blog sections each have a "Content width" setting (Narrow or Normal) to control how wide the text column is.

## 1.1.3

*October 2026*

### Fixed

- **Buy it now on sold-out products.** The "Buy it now" button no longer shows when the selected variant is sold out or unavailable. It reappears as soon as you choose an available variant.

## 1.1.2

*October 2026*

### Changed

- **Demo content renamed.** The demo brand in the preset templates is now Halvard, and the featured demo product is the Halvard Fell. Only the sample text changed. Settings and sections work as before, and none of your own content is affected.

## 1.1.1

*October 2026*

### New

- **Brand tagline in the header and footer.** The Brand tagline setting (Theme settings > Brand) now shows next to your logo on screens 990px and wider, and with your logo or brand name at the top of the footer. Each section has a "Show brand tagline" setting, and nothing shows while the tagline is blank. The tagline is now blank by default.

## 1.1.0

*October 2026*

### New

- **Collection filters and sorting** powered by Shopify Search & Discovery, with counts, a price range, color swatches and removable filter tags. Filters open in a drawer on mobile.
- **Search suggestions** in the header, covering products, collections, pages and blog posts.
- **Dropdown menus** with up to three levels, and a mobile menu drawer.
- **Country/region and language selectors** in the footer and, optionally, the header.
- **Email signup** section and footer block.
- **Social media icons** for 10 networks, plus **Follow on Shop**.
- **Product recommendations** section for related or complementary products.
- **Featured product** section that's fully shoppable from any page.
- **Color swatches and button-style variant picker.**
- **Rich product media:** video, YouTube, Vimeo and 3D models with augmented reality.
- **Store pickup availability** on product pages.
- **Subscriptions:** a purchase options picker for selling plans.
- **Gift cards:** a recipient form (email, name, message and send date), plus a redesigned gift card page with a QR code, Apple Wallet link, copy button and print styles.
- **Logo and favicon** settings with separate desktop and mobile logo widths.
- **Collection banner** with the collection image and description.
- **Order notes**, discounts on cart lines and totals, unit prices and Shop Pay Installments messaging.
- **A lean default product template** for add-ons and accessories, alongside the detailed flagship template.

### Improved

- **Faster first load:** critical styles inlined, fonts preloaded and fewer render-blocking requests.
- **Accessibility:** larger tap targets, clearer focus outlines, an accessible cart drawer and inline form errors.
- **Honest defaults:** demo customer quotes and policy claims replaced with clearly marked placeholders that stay hidden until you add real content.
- **Brand name** falls back to your store name when left blank.

### Fixed

- Dropdown menus closing unexpectedly after a click.
- Unreadable dropdown menus (select boxes) on iPhone and Safari with the dark color scheme.
- Product cards on mobile collection pages overflowing the screen.
