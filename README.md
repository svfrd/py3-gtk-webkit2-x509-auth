# py3-gtk-webkit2-x509-auth

**PyGObject API Reference**

* https://lazka.github.io/pgi-docs/ (outdated)
* https://lazka.github.io/pgi-docs/WebKit2-4.0/ (outdated version 2.32.2. upstream: 2.34.4)
* https://lazka.github.io/pgi-docs/#Gio-2.0 (outdated version 2.66.2. upstream: 2.72)

**GTK+ WebKit2/GIO Reference**

* https://webkitgtk.org/reference/webkit2gtk/stable/index.html \
* https://docs.gtk.org/gio/
* https://docs.gtk.org/gio/class.TlsCertificate.html

## x509 client certificate auth

A simple test page with ssl client certification verification.

https://x.dingsbums.de/x509/

* bob.pfx (blank passphrase)
* bob.pem 
* bob.key

\
_apache2 config:_
```
<Location "/x509">
        SSLVerifyClient require
        SSLVerifyDepth 2
        SSLRequire %{SSL_CLIENT_S_DN_CN} eq "bob"
</Location>
```

## http basic auth

A simple test page without stored credentials.

The authentication method "basic auth" triggers the signal "authenticate" in the class "WebKit2.WebView".

https://x.dingsbums.de/auth/


_apache config:_
```
<Location "/auth">
        AuthType Basic
        AuthName "Restricted Content"
        AuthUserFile /dev/null
        Require valid-user
</Location>
```
