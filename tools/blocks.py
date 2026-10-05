"""Tiny helpers that serialize WordPress core blocks exactly the way the
block editor saves them, so generated patterns open without "unexpected
content" warnings. Used by build_patterns.py."""

import json

NAV = "#roadmap"  # replaced with the Navigator URL at render (inc/setup.php)


def _attrs(d):
    d = {k: v for k, v in d.items() if v not in (None, "", {})}
    return (" " + json.dumps(d, separators=(",", ":"), ensure_ascii=False)) if d else ""


def _cls(*names):
    return " ".join(n for n in names if n)


def img_url(file):
    return f"<?php echo thln_img( '{file}' ); ?>"


def group(children, cls=None, tag="div", anchor=None, align=None):
    a = {"anchor": anchor}
    if tag != "div":
        a["tagName"] = tag
    a["align"] = align
    a["className"] = cls
    if align:
        cls = _cls(f"align{align}", cls)
    a["layout"] = {"type": "default"}
    idattr = f' id="{anchor}"' if anchor else ""
    inner = "".join(children)
    return (f"<!-- wp:group{_attrs(a)} -->\n"
            f'<{tag}{idattr} class="{_cls("wp-block-group", cls)}">{inner}</{tag}>\n'
            f"<!-- /wp:group -->\n")


def p(html, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f"<!-- wp:paragraph{_attrs({'className': cls})} -->\n<p{c}>{html}</p>\n<!-- /wp:paragraph -->\n"


def h(html, level=2, cls=None, anchor=None):
    a = {"level": level if level != 2 else None, "className": cls}
    idattr = f' id="{anchor}"' if anchor else ""
    if anchor:
        a = {"anchor": anchor, **a}
    return (f"<!-- wp:heading{_attrs(a)} -->\n"
            f'<h{level}{idattr} class="{_cls("wp-block-heading", cls)}">{html}</h{level}>\n'
            f"<!-- /wp:heading -->\n")


def img(file, alt="", cls=None):
    a = {"sizeSlug": "full", "linkDestination": "none", "className": cls}
    return (f"<!-- wp:image{_attrs(a)} -->\n"
            f'<figure class="{_cls("wp-block-image size-full", cls)}"><img src="{img_url(file)}" alt="{alt}"/></figure>\n'
            f"<!-- /wp:image -->\n")


def button(text, href=NAV, style=None):
    cls = f"is-style-{style}" if style else None
    return (f"<!-- wp:button{_attrs({'className': cls})} -->\n"
            f'<div class="{_cls("wp-block-button", cls)}"><a class="wp-block-button__link wp-element-button" href="{href}">{text}</a></div>\n'
            f"<!-- /wp:button -->\n")


def buttons(*btns):
    return f'<!-- wp:buttons -->\n<div class="wp-block-buttons">{"".join(btns)}</div>\n<!-- /wp:buttons -->\n'


def lst(items, cls=None, ordered=False):
    a = {"ordered": True if ordered else None, "className": cls}
    tag = "ol" if ordered else "ul"
    lis = "".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->\n" for i in items)
    return (f"<!-- wp:list{_attrs(a)} -->\n"
            f'<{tag} class="{_cls("wp-block-list", cls)}">{lis}</{tag}>\n'
            f"<!-- /wp:list -->\n")


def quote(paras, cls=None):
    inner = "".join(p(x) for x in paras)
    return (f"<!-- wp:quote{_attrs({'className': cls})} -->\n"
            f'<blockquote class="{_cls("wp-block-quote", cls)}">{inner}</blockquote>\n'
            f"<!-- /wp:quote -->\n")


def shortcode(code):
    return f"<!-- wp:shortcode -->\n{code}\n<!-- /wp:shortcode -->\n"


def section(children, cls, anchor=None):
    """A full-width page section. 'thln-section' turns on the canvas layout."""
    return group(children, cls=_cls("thln-section", cls), tag="section", anchor=anchor, align="full")


def container(children, cls=None):
    return group(children, cls=_cls("container", cls))
