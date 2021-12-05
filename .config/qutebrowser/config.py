#[dotfiles/config.py at master · koekeishiya/dotfiles · GitHub](https://github.com/koekeishiya/dotfiles/blob/master/qutebrowser/config.py)

# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'bottom': 5, 'left': 5, 'right': 5, 'top': 5}

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl

#c.url.default_page = 'https://koekeishiya.github.io/chunkwm/'

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl

#c.url.start_pages = 'https://koekeishiya.github.io/chunkwm/'

# Hide the window decoration.  This setting requires a restart on
# Wayland.
# Type: Bool
#c.window.hide_decoration = True

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#d5c4a1'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#333333'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#202020'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#8fee96'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#151515'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#151515'

# Foreground color of the matched text in the completion.
# Type: QssColor
c.colors.completion.match.fg = '#d75f5f'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#202020'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#d5c4a1'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#202020'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#d4c5a1'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#202020'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#d5c4a1'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#d75f5f'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#84edb9'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#8fee96'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#cd950c'

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = '#202020'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#707070'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#202020'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#707070'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#202020'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#d5c4a1'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#353535'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#d5c4a1'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#353535'

# Font used in the tab bar.
# Type: QtFont
# c.fonts.tabs = '10pt fantasque sans mono'

# Bindings for normal mode
#config.bind(';M', 'hint --rapid links spawn open -na /Applications/mpv.app {hint-url}')
#config.bind('<Meta+n>', 'open -p')
#config.bind('<Meta+w>', 'close')
config.bind(',M', 'hint links spawn mpv {hint-url}')
config.bind(',m', 'spawn mpv {url}')

#[qutebrowser の細かい設定 - Qiita](https://qiita.com/toyboot4e/items/c801050c0d53d3a1600a)

c.content.pdfjs = True # enable to see pdf
#####################################################################
# Save & restore session automatically
#####################################################################
#config.set('auto_save.session', True)
#c.auto_save.session = True

#c.url.default_page = 'https://google.com/'
#c.url.start_pages = 'https://qutebrowser.org/'
#c.scrolling.bar = "always"

####################################################################
# Behaviors
####################################################################
# Open new tab next to the current tab
c.tabs.new_position.unrelated = "next"
# Open new tab with `F` without focusing it
config.set('tabs.background', True)
# 
c.input.partial_timeout = 0

#c.url.searchengines = {
##    "DEFAULT": 'https://google.com/search?q={}',
#    "DEFAULT": 'https://https://duckduckgo.com/search?q={}',
##    "b": 'https://bandcamp.com/search?q={}',
#    "cr": 'https://crates.io/search?q={}',
#    "d": 'https://dictionary.cambridge.org/dictionary/english/{}',
#    'g': 'https://github.com/search?q={}',
#    "s": 'https://stackoverflow.com/search?q={}',
#    "y": 'https://www.youtube.com/results?search_query={}',
#}

# tab looking
#c.tabs.position = "right"
#c.tabs.width = 160
#c.tabs.padding = {'bottom': 4, 'left': 4, 'right': 4, 'top': 4}

# zoom
config.set('zoom.default', '90%')

# hide title bar
#c.window.hide_decoration = True

### QUICKMARK (it's much better than bookmarks for now) ###
#config.bind('sq', 'quickmark-save')
#config.bind('ab', 'bookmark-add')
#config.bind('aq', 'quickmark-add')
config.bind(';', 'set-cmd-text :')

config.unbind('d')
config.bind('db', 'bookmark-del')
config.bind('dd', 'tab-close')
config.bind('dq', 'quickmark-del')

#config.unbind('b',)
#config.bind('b',':bookmark-load ')
#config.unbind('B')
#config.bind('B', ':quickmark-load ')

### VIMIUM-LIKE ###
config.unbind('h')
config.unbind('l')
config.bind('h', ':tab-prev')
config.bind('l', ':tab-next')

config.unbind('<Shift+h>')
config.unbind('<Shift+l>')
config.bind('<Shift+h>', ':back')
config.bind('<Shift+l>', ':forward')

#config.unbind('<Control+i>')
#config.unbind('<Control+o>')
#config.bind('<Control+i>', ':back')
#config.bind('<Control+o>', ':forward')

#config.unbind('<Shift+h>')
#config.unbind(';')
#config.bind(';', ':')
#config.bind('<Shift+l>', ':forward')


config.unbind('j')
config.unbind('k')
config.bind('j', ':run-with-count 1 scroll down')
config.bind('k', ':run-with-count 1 scroll up')
config.bind('<Shift+j>', ':run-with-count 15 scroll down')
config.bind('<Shift+k>', ':run-with-count 15 scroll up')

config.bind(',c', ':spawn google-chrome-unstable {url}')
config.bind(',f', ':spawn firefox-nightly {url}')


#config.set('backend', 'webkit')
#config.bind('x', ':tab-close')
#config.bind('X', ':undo')

#config.bind('yf', ':hint links yank')

#config.bind('<Ctrl+e>', ':scroll down')
#config.bind('<Ctrl+y>', ':scroll up')

#c.content.user_stylesheets = "~/.config/qutebrowser/solarized-dark/solarized-dark-all-sites.css"

#[Yet another dark mode post : qutebrowser](https://www.reddit.com/r/qutebrowser/comments/jdnqbp/yet_another_dark_mode_post/)

import subprocess

def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props

#xresources = read_xresources('*')


ccw = c.colors.webpage
#ccw.bg = xresources['*.background']
ccw.bg = "black"
ccw.darkmode.enabled = True
ccw.darkmode.threshold.background = 100
ccw.darkmode.threshold.text = 256 - ccw.darkmode.threshold.background
ccw.darkmode.policy.images = 'smart'
ccw.darkmode.policy.page = 'smart'
#ccw.prefers_color_scheme_dark = True
ccw.preferred_color_scheme = 'dark'
#c.colors.statusbar.normal.bg = xresources['*.background']

