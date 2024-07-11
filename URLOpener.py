import webbrowser

str = """Library genesis
Libgen
b-ok.org
e library
gen.lib.rus.ec
sciencedirect
manybooks.net
libgen.io
bookfi.com
1lib.us
openstax
bigwords.com
Zlibrary
Slug books
gettextbooks.com
thriftbooks.com"""

arr = str.split("\n")

for url in arr:
  print(url)

# webbrowser.get("chromium").open_new_tab(arr[0])

# for url in arr:
#   webbrowser.get('brave').open(url)

# import webbrowser

# # Register the browser
# webbrowser.register('brave', None, webbrowser.BackgroundBrowser(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"))

# # Open the browser
# webbrowser.get("brave").open_new_tab(arr[0])