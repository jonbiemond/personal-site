Title: Making This Site
Date: 2025-04-08 21:48
Tags: Meta
Slug: this-site
Author: Jonathan Biemond
Summary: How I made this website.

This static site is made with [Pelican](https://getpelican.com/) and hosted on [CloudFlare Pages](https://pages.cloudflare.com/).
There are many great technical blogs I enjoy reading. I hope that by sharing some posts myself, I may
write something someone finds useful and along the way improve my writing skills. For this project I shamelessly copied [Duarte O.Carmo's site](https://duarteocarmo.com/),
you should check it out, it's great. More than just engaging writing, Duarte's site caught my eye for its clean design,
and since it is powered by Pelican, which I knew I wanted to use, it was a natural starting point.
Finally, it introduced me to CloudFlare Pages, which I must say has been an absolute pleasure to use.

## Pelican
This site is rendered from some Markdown files and HTML templates using [Pelican](https://getpelican.com/). We're not wanting for choice
when it comes to static-site generators, Pelican stands out because of it's ease-of-use, good reputation, and, for me,
it is built using Python. So far it's been a joy to work with, notably due to the ample, high quality documentation.

## Deployment
I deployed the site to [CloudFlare Pages](...). This was really quite simple, I chose my GitHub repo, accepted the
default settings, and it started to build. I didn't get it right on the first try though, because I was missing a
`requirements.txt`. Frustratingly, this wasn't documented anywhere that I could find. Hopefully CloudFlare will support `pylock.toml` files in the future. Once the dependencies were installed
everything was smooth sailing. No GitHub Action to set up, any new commits to the `main` branch are live a minute later.
Since I also purchased my domain from CloudFlare, DNS record registration was just a simple click.

You can find the source on GitHub: [https://github.com/jonbiemond/personal-site](https://github.com/jonbiemond/personal-site)
