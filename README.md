# PDF Generator

The main idea is:
Create Document DSL with simple api to generate PDF report with simple customization.

For example:
```
d = Document()
    .addComponent(Table().addRow(...).addRow(...))
    .addComponent(List().addItem(...).addItem(...))
    .addComponent(<a href="https://github.com/yazabara">yazabara repo</a>)
    ....

PdfGenerator.generate(doc)
```

For now there are 3 base components:
- Table: ```html <table>```
- List: ```html <ul>```
- Custom: ```any html code```

There is possibility to customize pdf reports using css (weasyprint).

## Installing

**_weasyprint:_**
https://weasyprint.readthedocs.io/en/stable/install.html#step-2-update-pip-and-setuptools-packages

## Useful links
Example : http://pbpython.com/pdf-reports.html
Jinja2 template engine: http://jinja.pocoo.org/docs/2.10/templates/

