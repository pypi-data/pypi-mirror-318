from reactpy import component, html

@component
def Title(title):
    return html.script(f'() => {{document.title = "{title}";}}')

@component
def Favicon(src):
    return html.script(f"""
        const existingLinks = document.querySelectorAll("link[rel='icon']");
        existingLinks.forEach(link => link.remove());

        const newLink = document.createElement("link");
        newLink.rel = 'icon';
        newLink.type = 'image/x-icon';
        newLink.href = "{src}";
        document.head.appendChild(newLink);
    """)


@component
def Meta(meta_tags):
    return html.script(f"""
        const metaTags = {meta_tags};
        metaTags.forEach(meta => {{
            const metaElement = document.createElement("meta");
            Object.keys(meta).forEach(key => {{
                metaElement.setAttribute(key, meta[key]);
            }});
            document.head.appendChild(metaElement);
        }});
    """)