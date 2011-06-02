# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = 'defying the conventional'

##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    [T('Home'), True,
     URL(request.application,'default','home'), []],
    [T('Services'), False,
     URL(request.application,'default','services'), []],
    [T('Careers'), False,
     URL(request.application, 'default', 'careers'), []],
    [T('Contact us'), False,
      URL(request.application, 'default', 'contact'), []],
]


def createMenu(menu):
    """
    Creates menu in a format understandable by front-end styles.
    """
    for label, selected, link, subMenu in menu:
        cls = (selected and 'here') or ''
        response.write('<li><a href="%s" class="%s i18n"><span><span>%s</span></span></a>' %
                (link, cls, label), escape=False)
        # Submenus are rendered as nested <ul>.
        if subMenu:
            response.write('<ul>', escape=False)
            createMenu(subMenu)
            response.write('</ul>', escape=False)
        response.write('</li>', escape=False)

