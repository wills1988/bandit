import jinja2
from jinja2 import Environment
templateLoader = jinja2.FileSystemLoader( searchpath="/" )
something = ''

Environment(loader=templateLoader, load=templateLoader, autoescape=True)
templateEnv = jinja2.Environment(autoescape=True,
        loader=templateLoader )
Environment(loader=templateLoader, load=templateLoader, autoescape=something)
templateEnv = jinja2.Environment(autoescape=False, loader=templateLoader )
Environment(loader=templateLoader,
            load=templateLoader,
            autoescape=False)

Environment(loader=templateLoader,
            load=templateLoader)
