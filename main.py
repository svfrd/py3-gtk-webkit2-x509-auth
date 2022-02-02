#!/usr/bin/python3

try:
    import gi
    gi.require_version('Gtk', '3.0')
    gi.require_version('WebKit2', '4.0')
    from gi.repository import Gtk, WebKit2, GLib, Gio
except ImportError:
    try:
        import pgi as gi
        gi.require_version('Gtk', '3.0')
        gi.require_version('WebKit2', '4.0')
        from pgi.repository import Gtk, WebKit2, GLib, Gio
    except ImportError:
        gi = None
if gi is None:
    raise ImportError("Either gi (PyGObject) or pgi module is required.")

import urllib3
urllib3.disable_warnings()

import requests
from urllib.parse import urlparse, urlencode

def foo_load_changed(webview, event):
    print('XXX: foo_load_changed()')

def foo_res_load_started(webview, resource, request):
    print('XXX: foo_res_load_started()')

def foo_authenticate(webview, request):
    print('XXX: foo_authenticate()')

def close(window, event):
    Gtk.main_quit()

Gtk.init()
window = Gtk.Window()

ctx = WebKit2.WebContext.get_default()
ctx.set_tls_errors_policy(WebKit2.TLSErrorsPolicy.IGNORE)

#mgr = WebKit2.WebContext.get_website_data_manager(ctx)
#mgr.set_persistent_credential_storage_enabled(True)

cookies = ctx.get_cookie_manager()
cookies.set_accept_policy(WebKit2.CookieAcceptPolicy.ALWAYS)
#cookies.set_persistent_storage(cookies, WebKit2.CookiePersistentStorage.TEXT)

#context = WebKit2.WebContext.new()

# WebView
#wview = WebKit2.WebView.new_with_context(context)
wview = WebKit2.WebView()

window.resize(500, 500)
window.add(wview)
window.set_title("SAML Login")
window.connect('delete-event', close)

#ctx.allow_tls_certificate_for_host(certificate=Gio.TlsCertificate.new_from_file('bob.pem'), host='x.dingsbums.de')

#ctx.WebKit2.Credential.new(
#cert_gio = Gio.TlsCertificate.new_from_file('bob.pem')
cert_gio = Gio.TlsCertificate.new_from_files('bob.pem','bob.key')
cred = WebKit2.Credential.new_for_certificate(cert_gio,WebKit2.CredentialPersistence.FOR_SESSION)
#ctx.allow_tls_certificate_for_host(cert_gio, host='x.dingsbums.de')
ctx.allow_tls_certificate_for_host(cert_gio,host='x.dingsbums.de')

#wview.open('https://x.dingsbums.de/')
wview.connect('load-changed', foo_load_changed)
wview.connect('resource-load-started', foo_res_load_started)
wview.connect('authenticate', foo_authenticate)

settings = wview.get_settings()
settings.set_enable_developer_extras(True)

wview.get_main_resource()
#wview.load_html('index.html','https://x.dingsbums.de/')
#wview.open('https://x.dingsbums.de/')
wview.load_uri('https://x.dingsbums.de/x509')
#wview.load_uri('https://x.dingsbums.de/auth')

window.show_all()
Gtk.main()

Gtk.main_quit()
