import crawl_deface_id_strong_element

url = "https://defacer.id/archive/mirror/12418885"
html = crawl_deface_id_strong_element.url_html(url)
html.crawl_by_tag(tag = "strong")