# -*- coding: utf-8 -*- 

#########################################################################
## This is the main controller. 
## - index is the default action of any application
#########################################################################  


# Global configuration.
cache_expiry =  (request.env.web2py_runtime_gae and 300) or 2
config = {'cache_expire': cache_expiry}


def _ajaxCheck(func):
    """
    Checks for ajax call. Redirects to index with target variable set.
    Used as decorator.
    """
    def new(*args, **kwargs):
        if not request.vars.ajax:
            redirect(URL(r=request, f='index', vars={'target': request.env.path_info}))
        return func(*args, **kwargs)
    return new


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
def index():
    """
    Renders the main template.
    """
    d = dict()
    return response.render(d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
@_ajaxCheck
def home():
    """
    Gets the content to be displayed on the home page. 
    """
    rows=db(db.content.ident=='home-main').select(db.content.ALL, orderby=db.content.seq)
    d = dict(rows=rows)
    return response.render(d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
@_ajaxCheck
def contact():
    """
    Serializes the contact form for the view; validates and accepts the input.
    """
    d = dict()
    return response.render(d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
@_ajaxCheck
def careers():
    """
    Gets the zen of defiance from the data store.
    """
    rows = db(db.content.ident=='careers-zen').select(db.content.ALL, orderby=db.content.seq)
    d = dict(rows=rows)
    return response.render(d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
@_ajaxCheck
def services():
    """
    Gets the list of services from the data store.
    """
    rows = db().select(db.services.ALL)
    d = dict(rows=rows)
    return response.render(d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
def ieError():
    """
    Displays error if the user is using IE6. IE6 breaks a lot of things. No point fixing them.
    """
    summary = "We don't support IE6."
    description = """ IE7 or higher or any other modern browser should work fine. We advice you upgrade even if you
    don't plan to come back. Apart from incomplete/incompatible implementation of web standards, older browsers have
    some serious secuirty vulnerabilities making them susceptible to cyber attacks.
    """
    d = dict(summary=summary, description=description)
    return response.render("default/error.html", d)


@cache(request.env.path_info, time_expire=config['cache_expire'], cache_model=cache.ram)
def cantFind():
    """
    Displays error if a non-existent page is accessed.
    """
    summary = "The page you are looking for can't be found"
    description = """ The page you are looking for does not exist. It might have moved or deleted. Please head over to
    the <a href="/">home</a> page to continue browsing this site.
    """
    d = dict(summary=summary, description=description)
    return response.render("default/error.html", d)


