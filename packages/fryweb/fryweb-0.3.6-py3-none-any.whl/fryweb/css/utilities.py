import re
from random import randint
from .color import tailwind_colors, radix_colors, semantic_colors

def is_digit(value):
    return value.isdigit()

def is_digit_range(value, minv, maxv):
    return value.isdigit() and minv <= int(value) <= maxv

def is_float(value):
    vs = value.split('.')
    return len(vs) == 2 and all((v=='' or v.isdigit()) for v in vs)

def is_fraction(value):
    vs = value.split('/')
    return len(vs) == 2 and all(v.isdigit() for v in vs)

def is_percent(value):
    return (len(value) > 1 and
            value[-1] == '%' and
            value[:-1].isdigit() and
            0 <= int(value[:-1]) <= 100)

def is_calc(value):
    return (len(value) > 6 and
            value[3] == ',' and
            value[:3] in ('add', 'sub','mul', 'div'))

def is_hex(value):
    return all('0'<=x<='9' or 'a'<=x<='f' or 'A'<=x<='F'
               for x in value)

def random_color(r=(0,255), g=(0,255), b=(0,255), a=255):
    def check(x):
        if (isinstance(r, (list, tuple)) and
            len(r) == 2 and
            0 <= r[0] <= r[1]):
            min = r[0]
            max = r[1] if r[1] <= 255 else 255
            return (min, max)
        elif isinstance(r, int):
            min = r if r >= 0 else 0
            min = min if min <= 255 else 255
            max = 255
            return (min, max)
        raise RuntimeError(f"Invalid argument '{x}'")
    r = randint(*check(r))
    g = randint(*check(g))
    b = randint(*check(b))
    a = randint(*check(a))
    return f'#{r:02x}{g:02x}{b:02x}{a:02x}'
    

def convert_size(value, negative=False):
    values = {
        '0':    '0px',
        'px':   '1px',
        'auto': 'auto',
        'full': '100%',
        'min':  'min-content',
        'max':  'max-content',
        'fit':  'fit-content',
        '3xs':  '16rem',       # 256px
        '2xs':  '18rem',       # 288px
        'xs':   '20rem',       # 320px
        'sm':   '24rem',       # 384px
        'md':   '28rem',       # 448px
        'lg':   '32rem',       # 512px
        'xl':   '36rem',       # 576px
        '2xl':  '42rem',       # 672px
        '3xl':  '48rem',       # 768px
        '4xl':  '56rem',       # 896px
        '5xl':  '64rem',       # 1024px
        '6xl':  '72rem',       # 1152px
        '7xl':  '80rem',       # 1280px
    }
    v = values.get(value)
    if v:
        size = v
    elif is_digit(value):
        size = f'{int(value)/4}rem'
    elif is_float(value):
        size = f'{float(value)/4}rem'
    elif is_fraction(value):
        a, b = value.split('/')
        a, b = int(a), int(b)
        size = f'{a*100/b}%'
    elif is_calc(value):
        items = value.split(',')
        if len(items) != 3:
            size = value
        else:
            ops = {'add':'+','sub':'-','mul':'*', 'div':'/'}
            size = f'calc({items[1]} {ops[items[0]]} {items[2]})'
    else:
        size = value
    if negative and size and size[0] != '-':
        size = '-' + size
    return size

def convert_color(args):
    if len(args) == 0:
        return None

    # 16进制格式的颜色，支持带有透明度
    if (len(args) == 2 and
        args[0] == 'hex' and
        is_hex(args[1]) and
        len(args[1]) in (3, 4, 6, 8)):
        return '#' + args[1]
    if (len(args) == 1 and
        args[0][0] == '#' and
        is_hex(args[0][1:]) and
        len(args[0]) in (4, 5, 7, 9)):
        return args[0]
    if (len(args) == 1 and
        is_hex(args[0]) and
        len(args[0]) in (3, 4, 6, 8)):
        return '#' + args[0]

    # tailwind风格的颜色，支持后跟'/75'这样添加透明度
    values = {
        'none':        'none',
        'inherit':     'inherit',
        'current':     'correntColor',
        'transparent': 'transparent',
        'black':       'rgb(0 0 0)',
        'white':       'rgb(255 255 255)',
    }
    value = '-'.join(args)
    color_opacity = value.split('/')
    if len(color_opacity) == 1:
        # 属性名中不能出现'/'符号，所以如果用无值属性时，应该用pink-900@25
        # 这样的方法，不能用pink-900/25这种方式，后者只能用于class值或属性值中
        # 2023-10-19: 当前fry语法中，属性名可以包含'/'，所以可以使用pink-900/25
        #             以下逻辑暂时保留
        color_opacity = value.split('@')
        if len(color_opacity) == 1:
            color = color_opacity[0]
            opacity = None
        else:
            color, opacity = color_opacity
    elif len(color_opacity) == 2:
        color, opacity = color_opacity
    else:
        return None
    c = (values.get(color) or
         tailwind_colors.get(color) or
         radix_colors.get(color) or
         semantic_colors.get(color))
    if not c:
        from fryweb.css.plugin import plugin_color
        color = plugin_color(color)
        if not color:
            return None
        type = 'plugin'
    else:
        color = c
    if not opacity:
        return color
    if opacity.isdigit() and 0<=int(opacity)<=100:
        return re.sub(r'\)$', f' / {int(opacity)/100})', color)
    return None
        
def opacity_to(color, opacity):
    r = 255
    g = 255
    b = 255
    m = re.fullmatch(r'rgb\(([0-9]+) ([0-9]+) ([0-9]+)[^)]*\)', color)
    if color[0] == '#' and is_hex(color[1:]):
        if len(color) in (4, 5):
            r = int(int(color[1], 16)/15*255)
            g = int(int(color[2], 16)/15*255)
            b = int(int(color[3], 16)/15*255)
        elif len(color) in (7, 9):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
    elif m:
        r,g,b = m.groups()
    return f'rgb({r} {g} {b} / {opacity/100})'
        

def merge_value(args, negative=False):
    value = '-'.join(args)
    if negative and value and value[0] != '-':
        value = '-' + value
    return value.replace('_', ' ')


IGNORES = set(['css', 'args', 'argc', 'neg', 'from_plugin', 'utility_method', 'is_utility', 'add_style'])
class Utility():
    def __init__(self, css):
        args = css.utility_args
        self.css = css
        self.args = args
        self.argc = len(args)
        self.neg = len(args) > 0 and len(args[0]) > 0 and args[0][0] == '-'

    def from_plugin(self, pu):
        css = self.css
        css.plugin_order = pu.plugin_order
        css.level_order = pu.level_order
        css.selector_template = css.selector_template.format(selector=pu.selector_template)
        css.wrappers += pu.wrappers
        css.addons += pu.addons
        css.styles += pu.styles
        return True

    def utility_method(self):
        if self.argc == 0 or self.args[0] == '':
            return None

        from fryweb.css.plugin import plugin_utility
        pu = plugin_utility(self.args)
        if pu:
            return lambda: self.from_plugin(pu)

        names = {
            'break': 'break_method',
            'not':   'not_method',
            'from':  'from_method',
        }
        name = self.args[0]

        if name in IGNORES:
            return None

        # 去掉负值的情况
        name = name[1:] if name[0] == '-' else name 

        # 处理python关键字
        name = names.get(name, name)

        return getattr(self, name, None)

    def is_utility(self):
        return True if self.utility_method() else False

    def __call__(self):
        method = self.utility_method()
        if not callable(method):
            return False
        return method()

    def add_style(self, key, value):
        self.css.add_style(key, value)

    def dummy(self):
        return True

    def aspect(self):
        if self.argc != 2:
            return False
        arg = self.args[1]
        values = {
            'auto':   'auto',
            'square': '1 / 1',
            'video':  '16 / 9'
        }
        value = values.get(arg, arg.replace('/', ' / '))
        self.add_style('aspect-ratio', str(value))
        return True

    def container(self):
        if self.argc != 1:
            return False
        self.add_style('width', '100%')
        for size in (640, 768, 1024, 1280, 1536):
            addon = self.css.new_addon()
            addon.wrappers.append(f'@media (min-width: {size}px)')
            addon.styles.append(('max-width', f'{size}px'))
        return True

    def columns(self):
        if self.argc != 2:
            return False
        arg = self.args[1]
        values = {
            '3xs': '16rem', # 256px
            '2xs': '18rem', # 288px
            'xs':  '20rem', # 320px
            'sm':  '24rem', # 384px
            'md':  '28rem', # 448px
            'lg':  '32rem', # 512px
            'xl':  '36rem', # 576px
            '2xl': '42rem', # 672px
            '3xl': '48rem', # 768px
            '4xl': '56rem', # 896px
            '5xl': '64rem', # 1024px
            '6xl': '72rem', # 1152px
            '7xl': '80rem', # 1280px
        }
        value = values.get(arg, arg)
        self.add_style('columns', str(value))
        return True

    def joined_args(self, values):
        arg = '-'.join(self.args)
        value = values.get(arg)
        if isinstance(value, list):
            for v in value:
                self.add_style(*v)
            return True
        elif isinstance(value, tuple):
            self.add_style(*value)
            return True
        return False

    def break_method(self):
        # how a column or page should break
        values = {
            'break-after-auto':          ('break-after', 'auto'),
            'break-after-avoid':         ('break-after', 'avoid'),
            'break-after-all':           ('break-after', 'all'),
            'break-after-avoid-page':    ('break-after', 'avoid-page'),
            'break-after-page':          ('break-after', 'page'),
            'break-after-left':          ('break-after', 'left'),
            'break-after-right':         ('break-after', 'right'),
            'break-after-column':        ('break-after', 'column'),
            'break-before-auto':         ('break-before', 'auto'),
            'break-before-avoid':        ('break-before', 'avoid'),
            'break-before-all':          ('break-before', 'all'),
            'break-before-avoid-page':   ('break-before', 'avoid-page'),
            'break-before-page':         ('break-before', 'page'),
            'break-before-left':         ('break-before', 'left'),
            'break-before-right':        ('break-before', 'right'),
            'break-before-column':       ('break-before', 'column'),
            'break-inside-auto':         ('break-inside', 'auto'),
            'break-inside-avoid':        ('break-inside', 'avoid'),
            'break-inside-avoid-page':   ('break-inside', 'avoid-page'),
            'break-inside-avoid-column': ('break-inside', 'avoid-column'),
        }
        if self.joined_args(values):
            return True

        values = {
            'break-normal': [('overflow-wrap', 'normal'), ('word-break', 'normal')],
            'break-words':  ('overflow-wrap', 'break-word'),
            'break-all':    ('word-break', 'break-all'),
            'break-keep':   ('word-break', 'keep-all'),
        }
        return self.joined_args(values)

    def box(self):
        values = {
            'box-decoration-clone': ('box-decoration-break', 'clone'),
            'box-decoration-slice': ('box-decoration-break', 'slice'),
            'box-border':           ('box-sizing', 'border-box'),
            'box-content':          ('box-sizing', 'content-box'),
        }
        return self.joined_args(values)

    def block(self):
        return self.joined_args({'block': ('display', 'block')})

    def inline(self):
        values = {
            'inline':       ('display', 'inline'),
            'inline-block': ('display', 'inline-block'),
            'inline-flex':  ('display', 'inline-flex'),
            'inline-table': ('display', 'inline-table'),
        }
        return self.joined_args(values)

    def flex(self):
        values = {
            'flex':              ('display', 'flex'),
            'flex-row':          ('flex-direction', 'row'),
            'flex-row-reverse':  ('flex-direction', 'row-reverse'),
            'flex-col':          ('flex-direction', 'column'),
            'flex-col-reverse':  ('flex-direction', 'column-reverse'),
            'flex-wrap':         ('flex-wrap', 'wrap'),
            'flex-wrap-reverse': ('flex-wrap', 'wrap-reverse'),
            'flex-nowrap':       ('flex-wrap', 'nowrap'),
            'flex-1':            ('flex', '1 1 0%'),
            'flex-auto':         ('flex', '1 1 auto'),
            'flex-initial':      ('flex', '0 1 auto'),
            'flex-none':         ('flex', 'none'),
        }
        if self.joined_args(values):
            return True
        if self.argc != 4:
            return False
        if self.args[1].isdigit() and self.args[2].isdigit():
            self.add_style('flex', f'{self.args[1]} {self.args[2]} {self.args[3]}')
            return True
        return False

    def table(self):
        # set table-related display
        values = {
            'table':              ('display', 'table'),
            'table-caption':      ('display', 'table-caption'),
            'table-cell':         ('display', 'table-cell'),
            'table-column':       ('display', 'table-column'),
            'table-column-group': ('display', 'table-column-group'),
            'table-footer-group': ('display', 'table-footer-group'),
            'table-header-group': ('display', 'table-header-group'),
            'table-row-group':    ('display', 'table-row-group'),
            'table-row':          ('display', 'table-row'),
        }
        if self.joined_args(values):
            return True

        # set table layout
        values = {
            'table-auto':  ('table-layout', 'auto'),
            'table-fixed': ('table-layout', 'fixed'),
        }
        return self.joined_args(values)

    def flow(self):
        return self.joined_args({'flow-root': ('display', 'flow-root')})

    def grid(self):
        values = {
            'grid':                ('display', 'grid'),
            'grid-cols-none':      ('grid-template-columns', 'none'),
            'grid-rows-none':      ('grid-template-rows', 'none'),
            'grid-flow-row':       ('grid-auto-flow', 'row'),
            'grid-flow-col':       ('grid-auto-flow', 'column'),
            'grid-flow-dense':     ('grid-auto-flow', 'dense'),
            'grid-flow-row-dense': ('grid-auto-flow', 'row dense'),
            'grid-flow-col-dense': ('grid-auto-flow', 'column dense'),
        }

        if self.joined_args(values):
            return True

        if self.argc >= 3 and self.args[1] == 'cols':
            if self.argc == 3 and self.args[2].isdigit():
                value = f'repeat({self.args[2]}, minmax(0, 1fr))'
            else:
                value = merge_value(self.args[2:])
            self.add_style('grid-template-columns',  value)
            return True
        elif self.argc >= 3 and self.args[1] == 'rows':
            if self.argc == 3 and self.args[2].isdigit():
                value = f'repeat({self.args[2]}, minmax(0, 1fr))'
            else:
                value = merge_value(self.args[2:])
            self.add_style('grid-template-rows', value)
            return True


    def contents(self):
        return self.joined_args({'contents': ('display', 'contents')})

    def list(self):
        if self.argc == 1:
            return False
        values = {
            'list-item':       ('display', 'list-item'),
            'list-image-none': ('list-style-image', 'none'),
            'list-inside':     ('list-style-position', 'inside'),
            'list-outside':    ('list-style-position', 'outside'),
            'list-none':       ('list-style-type', 'none'),
            'list-disc':       ('list-style-type', 'disc'),
            'list-decimal':    ('list-style-type', 'decimal'),
        }
        if self.joined_args(values):
            return True
        if self.args[1] == 'image':
            value = merge_value(self.args[2:])
            self.add_style('list-style-image', value)
        else:
            value = merge_value(self.args[1:])
            self.add_style('list-style-type', value)
        return True

    def hidden(self):
        return self.joined_args({'hidden': ('display', 'none')})

    def float(self):
        values = {
            'float-right': ('float', 'right'),
            'float-left':  ('float', 'left'),
            'float-none':  ('float', 'none'),
        }
        return self.joined_args(values)

    def clear(self):
        values = {
            'clear-left':  ('clear', 'left'),
            'clear-right': ('clear', 'right'),
            'clear-both':  ('clear', 'both'),
            'clear-none':  ('clear', 'none'),
        }
        return self.joined_args(values)

    def isolate(self):
        return self.joined_args({'isolate': ('isolation', 'isolate')})

    def isolation(self):
        return self.joined_args({'isolation-auto': ('isolation', 'auto')})

    def object(self):
        values = {
            'object-contain':      ('object-fit', 'contain'),
            'object-cover':        ('object-fit', 'cover'),
            'object-fill':         ('object-fit', 'fill'),
            'object-none':         ('object-fit', 'none'),
            'object-scale-down':   ('object-fit', 'scale-down'),
            'object-bottom':       ('object-position', 'bottom'),
            'object-center':       ('object-position', 'center'),
            'object-left':         ('object-position', 'left'),
            'object-left-bottom':  ('object-position', 'left bottom'),
            'object-left-top':     ('object-position', 'left top'),
            'object-right':        ('object-position', 'right'),
            'object-right-bottom': ('object-position', 'right bottom'),
            'object-right-top':    ('object-position', 'right top'),
            'object-top':          ('object-position', 'top'),
        }
        return self.joined_args(values)

    def overflow(self):
        values = {
            'overflow-auto':      ('overflow', 'auto'),
            'overflow-hidden':    ('overflow', 'hidden'),
            'overflow-clip':      ('overflow', 'clip'),
            'overflow-visible':   ('overflow', 'visible'),
            'overflow-scroll':    ('overflow', 'scroll'),
            'overflow-x-auto':    ('overflow-x', 'auto'),
            'overflow-x-hidden':  ('overflow-x', 'hidden'),
            'overflow-x-clip':    ('overflow-x', 'clip'),
            'overflow-x-visible': ('overflow-x', 'visible'),
            'overflow-x-scroll':  ('overflow-x', 'scroll'),
            'overflow-y-auto':    ('overflow-y', 'auto'),
            'overflow-y-hidden':  ('overflow-y', 'hidden'),
            'overflow-y-clip':    ('overflow-y', 'clip'),
            'overflow-y-visible': ('overflow-y', 'visible'),
            'overflow-y-scroll':  ('overflow-y', 'scroll'),
        }
        return self.joined_args(values)

    def overscroll(self):
        values = {
            'overscroll-auto':      ('overscroll-behavior', 'auto'),
            'overscroll-contain':   ('overscroll-behavior', 'contain'),
            'overscroll-none':      ('overscroll-behavior', 'none'),
            'overscroll-x-auto':    ('overscroll-behavior-x', 'auto'),
            'overscroll-x-contain': ('overscroll-behavior-x', 'contain'),
            'overscroll-x-none':    ('overscroll-behavior-x', 'none'),
            'overscroll-y-auto':    ('overscroll-behavior-y', 'auto'),
            'overscroll-y-contain': ('overscroll-behavior-y', 'contain'),
            'overscroll-y-none':    ('overscroll-behavior-y', 'none'),
        }
        return self.joined_args(values)

    def static(self):
        return self.joined_args({'static': ('position', 'static')})

    def fixed(self):
        return self.joined_args({'fixed': ('position', 'fixed')})

    def absolute(self):
        return self.joined_args({'absolute': ('position', 'absolute')})

    def relative(self):
        return self.joined_args({'relative': ('position', 'relative')})

    def sticky(self):
        return self.joined_args({'sticky': ('position', 'sticky')})

    def inset(self):
        if self.argc == 2:
            direction = None
            value = self.args[1]
        elif self.argc == 3:
            direction = self.args[1]
            value = self.args[2]
            if direction != 'x' or direction != 'y':
                return False
        else:
            return False
        value = convert_size(value, self.neg)
        if not direction:
            self.add_style('inset', value)
        elif direction == 'x':
            self.add_style('left', value)
            self.add_style('right', value)
        else:
            self.add_style('top', value)
            self.add_style('bottom', value)
        return True

    def start(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('inset-inline-start', value)
        return True

    def end(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('inset-inline-end', value)
        return True

    def top(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('top', value)
        return True
    
    def right(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('right', value)
        return True

    def bottom(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('bottom', value)
        return True

    def left(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1], self.neg)
        self.add_style('left', value)
        return True

    def visible(self):
        return self.joined_args({'visible': ('visibility', 'visible')})

    def invisible(self):
        return self.joined_args({'invisible': ('visibility', 'hidden')})

    def collapse(self):
        return self.joined_args({'collapse': ('visibility', 'collapse')})

    def z(self):
        if self.argc != 2:
            return False
        if self.args[0][0] == '-':
            value = '-' + self.args[1]
        else:
            value = self.args[1]
        self.add_style('z-index', value)
        return True

    def basis(self):
        if self.argc != 2:
            return False
        value = convert_size(self.args[1])
        self.add_style('flex-basis', value)
        return True

    def grow(self):
        if self.argc == 1:
            value = 1
        elif self.argc != 2:
            return False
        elif not self.args[1].isdigit():
            return False
        else:
            value = self.args[1]
        self.add_style('flex-grow', value)
        return True

    def shrink(self):
        if self.argc == 1:
            value = 1
        elif self.argc != 2:
            return False
        elif not self.args[1].isdigit():
            return False
        else:
            value = self.args[1]
        self.add_style('flex-shrink', value)
        return True

    def order(self):
        if self.argc != 2:
            return False
        elif self.args[1] == 'first':
            value = '-9999'
        elif self.args[1] == 'last':
            value = '9999'
        elif self.args[1] == 'none':
            value = '0'
        elif not self.args[1].isdigit():
            return False
        else:
            value = self.args[1]
            if self.args[0][0] == '-':
                value = '-' + value
        self.add_style('order', value)
        return True

    def col(self):
        values = {
            'col-auto':       ('grid-column', 'auto'),
            'col-span-full':  ('grid-column', '1 / -1'),
            'col-start-auto': ('grid-column-start', 'auto'),
            'col-end-auto':   ('grid-column-end', 'auto'),
        }

        if self.joined_args(values):
            return True
        if self.argc == 3 and self.args[1] == 'span' and self.args[2].isdigit():
            name, value = 'grid-column', f'span {self.args[2]} / span {self.args[2]}'
        elif self.argc == 3 and self.args[1] in ('start', 'end') and self.args[2].isdigit():
            name, value = f'grid-column-{self.args[1]}', self.args[2]
        else:
            name, value = 'grid-column', merge_value(self.args[1:])
        self.add_style(name, value)
        return True

    def row(self):
        values = {
            'row-auto':       ('grid-row', 'auto'),
            'row-span-full':  ('grid-row', '1 / -1'),
            'row-start-auto': ('grid-row-start', 'auto'),
            'row-end-auto':   ('grid-row-end', 'auto'),
        }

        if self.joined_args(values):
            return True
        if self.argc == 3 and self.args[1] == 'span' and self.args[2].isdigit():
            name, value = 'grid-row', f'span {self.args[2]} / span {self.args[2]}'
        elif self.argc == 3 and self.args[1] in ('start', 'end') and self.args[2].isdigit():
            name, value = f'grid-row-{self.args[1]}', self.args[2]
        else:
            name, value = 'grid-row', merge_value(self.args[1:])
        self.add_style(name, value)
        return True

    def auto(self):
        values = {
            'auto-cols-auto': ('grid-auto-columns', 'auto'),
            'auto-cols-min':  ('grid-auto-columns', 'min-content'),
            'auto-cols-max':  ('grid-auto-columns', 'max-content'),
            'auto-cols-fr':   ('grid-auto-columns', 'minmax(0, 1fr)'),
            'auto-rows-auto': ('grid-auto-rows', 'auto'),
            'auto-rows-min':  ('grid-auto-rows', 'min-content'),
            'auto-rows-max':  ('grid-auto-rows', 'max-content'),
            'auto-rows-fr':   ('grid-auto-rows', 'minmax(0, 1fr)'),
        }
        if self.joined_args(values):
            return True
        if self.argc >= 3 and self.args[1] in ('cols', 'rows'):
            arg = self.args[1]
            args = self.args[2:]
            name, value = f"grid-auto-{'columns' if arg == 'cols' else arg}", merge_value(args)
            self.add_style(name, value)
            return True
        return False

    def gap(self):
        if self.argc == 2:
            direction = None
            value = self.args[1]
        elif self.argc == 3:
            if self.args[1] not in ('x', 'y'):
                return False
            direction = self.args[1]
            value = self.args[2]
        else:
            return False
        # tailwind不支持负的gap
        value = convert_size(value)
        if not direction:
            self.add_style('gap', value)
        elif direction == 'x':
            self.add_style('column-gap', value)
        else:
            self.add_style('row-gap', value)
        return True

    def justify(self):
        values = {
            'justify-normal':        ('justify-content', 'normal'),
            'justify-start':         ('justify-content', 'flex-start'),
            'justify-end':           ('justify-content', 'flex-end'),
            'justify-center':        ('justify-content', 'center'),
            'justify-between':       ('justify-content', 'space-between'),
            'justify-around':        ('justify-content', 'space-around'),
            'justify-evenly':        ('justify-content', 'space-evenly'),
            'justify-stretch':       ('justify-content', 'stretch'),
            'justify-items-start':   ('justify-items', 'start'),
            'justify-items-end':     ('justify-items', 'end'),
            'justify-items-center':  ('justify-items', 'center'),
            'justify-items-stretch': ('justify-items', 'stretch'),
            'justify-self-auto':     ('justify-self', 'auto'),
            'justify-self-start':    ('justify-self', 'start'),
            'justify-self-end':      ('justify-self', 'end'),
            'justify-self-center':   ('justify-self', 'center'),
            'justify-self-stretch':  ('justify-self', 'stretch'),
        }
        return self.joined_args(values)

    def content(self):
        # align content
        values = {
            'content-normal':   ('align-content', 'normal'),
            'content-center':   ('align-content', 'center'),
            'content-start':    ('align-content', 'flex-start'),
            'content-end':      ('align-content', 'flex-end'),
            'content-between':  ('align-content', 'space-between'),
            'content-around':   ('align-content', 'space-around'),
            'content-evenly':   ('align-content', 'space-evenly'),
            'content-baseline': ('align-content', 'baseline'),
            'content-stretch':  ('align-content', 'stretch'),
        }
        if self.joined_args(values):
            return True

        # content of the before or after pseudo-elements
        values = {
            'content-none': ('content', 'none'),
        }
        if self.joined_args(values):
            return True

        # arbitrary content
        if self.argc > 1:
            value = merge_value(self.args[1:])
            self.add_style('content', value)
            return True

        return False

    def items(self):
        values = {
            'items-start':    ('align-items', 'flex-start'),
            'items-end':      ('align-items', 'flex-end'),
            'items-center':   ('align-items', 'center'),
            'items-baseline': ('align-items', 'baseline'),
            'items-stretch':  ('align-items', 'stretch'),
        }
        return self.joined_args(values)

    def self(me):
        values = {
            'self-auto':     ('align-self', 'auto'),
            'self-start':    ('align-self', 'flex-start'),
            'self-end':      ('align-self', 'flex-end'),
            'self-center':   ('align-self', 'center'),
            'self-baseline': ('align-self', 'baseline'),
            'self-stretch':  ('align-self', 'stretch'),
        }
        return me.joined_args(values)

    def place(self):
        values = {
            'place-content-center':   ('place-content', 'center'),
            'place-content-start':    ('place-content', 'start'),
            'place-content-end':      ('place-content', 'end'),
            'place-content-between':  ('place-content', 'space-between'),
            'place-content-around':   ('place-content', 'space-around'),
            'place-content-evenly':   ('place-content', 'space-evenly'),
            'place-content-baseline': ('place-content', 'baseline'),
            'place-content-stretch':  ('place-content', 'stretch'),
            'place-items-start':      ('place-items', 'start'),
            'place-items-end':        ('place-items', 'end'),
            'place-items-center':     ('place-items', 'center'),
            'place-items-baseline':   ('place-items', 'baseline'),
            'place-items-stretch':    ('place-items', 'stretch'),
            'place-self-auto':        ('place-self', 'auto'),
            'place-self-start':       ('place-self', 'start'),
            'place-self-end':         ('place-self', 'end'),
            'place-self-center':      ('place-self', 'center'),
            'place-self-stretch':     ('place-self', 'stretch'),
        }
        return self.joined_args(values)

    def p(self):
        if self.argc == 2:
            size = convert_size(self.args[1])
            self.add_style('padding', size)
            return True
        elif self.argc == 3 and self.args[1] in 'xysetrbl':
            self.args = [self.args[0]+self.args[1], self.args[2]]
            self.argc = 2
            return self()
        return False

    def px(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-left', size)
        self.add_style('padding-right', size)
        return True

    def py(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-top', size)
        self.add_style('padding-bottom', size)
        return True

    def ps(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-inline-start', size)
        return True

    def pe(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-inline-end', size)
        return True

    def pt(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-top', size)
        return True

    def pr(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-right', size)
        return True

    def pb(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-bottom', size)
        return True

    def pl(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1])
        self.add_style('padding-left', size)
        return True

    def m(self):
        if self.argc == 2:
            size = convert_size(self.args[1], self.neg)
            self.add_style('margin', size)
            return True
        elif self.argc == 3 and self.args[1] in 'xysetrbl':
            self.args = [self.args[0]+self.args[1], self.args[2]]
            self.argc = 2
            return self()
        return False

    def mx(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-left', size)
        self.add_style('margin-right', size)
        return True

    def my(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-top', size)
        self.add_style('margin-bottom', size)
        return True

    def ms(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-inline-start', size)
        return True

    def me(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-inline-end', size)
        return True

    def mt(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-top', size)
        return True

    def mr(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-right', size)
        return True

    def mb(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-bottom', size)
        return True

    def ml(self):
        if self.argc != 2:
            return False
        size = convert_size(self.args[1], self.neg)
        self.add_style('margin-left', size)
        return True

    def space(self):
        if self.argc != 3 or self.args[1] not in 'xy':
            return False
        self.css.selector_template += ' > :not([hidden]) ~ :not([hidden])'

        dir = self.args[1]
        if self.args[2] == 'reverse':
            self.add_style(f'--fry-space-{dir}-reverse', '1')
        else:
            size = convert_size(self.args[2], self.neg)
            if dir == 'x':
                self.add_style('--fry-space-x-reverse',  '0')
                self.add_style('margin-right', f'calc({size} * var(--fry-space-x-reverse))')
                self.add_style('margin-left', f'calc({size} * calc(1 - var(--fry-space-x-reverse)))')
            else:
                self.add_style('--fry-space-y-reverse', '0')
                self.add_style('margin-bottom', f'calc({size} * var(--fry-space-y-reverse))')
                self.add_style('margin-top', f'calc({size} * calc(1 - var(--fry-space-y-reverse)))')
        return True

    def w(self):
        if self.argc != 2:
            return False
        if self.joined_args({'w-screen': ('width', '100vw')}):
            return True
        size = convert_size(self.args[1])
        self.add_style('width', size)
        return True

    def h(self):
        if self.argc != 2:
            return False
        if self.joined_args({'h-screen': ('height', '100vh')}):
            return True
        size = convert_size(self.args[1])
        self.add_style('height', size)
        return True

    def min(self):
        if self.joined_args({'min-h-screen': ('min-height', '100vh')}):
            return True

        if self.argc != 3 or self.args[1] not in 'hw':
            return False

        type = 'height' if self.args[1] == 'h' else 'width'
        size = convert_size(self.args[2])
        self.add_style(f'min-{type}', size)
        return True
        
    def max(self):
        values = {
            'max-w-none':       ('max-width', 'none'),
            'max-w-prose':      ('max-width', '65ch'),
            'max-w-screen-sm':  ('max-width', '640px'),
            'max-w-screen-md':  ('max-width', '768px'),
            'max-w-screen-lg':  ('max-width', '1024px'),
            'max-w-screen-xl':  ('max-width', '1280px'),
            'max-w-screen-2xl': ('max-width', '1536px'),
            'max-h-none':       ('max-height', 'none'),
            'max-h-screen':     ('max-height', '100vh'),
        }
        if self.joined_args(values):
            return True

        if self.argc != 3 or self.args[1] not in 'hw':
            return False

        type = 'height' if self.args[1] == 'h' else 'width'
        size = convert_size(self.args[2])
        self.add_style(f'max-{type}', size)
        return True

    def font(self):
        # font family, font weight
        values = {
            'font-sans':       ('font-family', 'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"'),
            'font-serif':      ('font-family', 'ui-serif, Georgia, Cambria, "Times New Roman", Times, serif'),
            'font-mono':       ('font-family', 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,"Liberation Mono", "Courier New", monospace'),
            'font-thin':       ('font-weight', '100'),
            'font-extralight': ('font-weight', '200'),
            'font-light':      ('font-weight', '300'),
            'font-normal':     ('font-weight', '400'),
            'font-medium':     ('font-weight', '500'),
            'font-semibold':   ('font-weight', '600'),
            'font-bold':       ('font-weight', '700'),
            'font-extrabold':  ('font-weight', '800'),
            'font-black':      ('font-weight', '900'),
        }
        if self.joined_args(values):
            return True
        value = merge_value(self.args[1:])
        if value.isdigit():
            self.add_style('font-weight', value)
        else:
            self.add_style('font-family', value)
        return True

    def text(self):
        # text overflow
        values = {
            'text-ellipsis': ('text-overflow', 'ellipsis'),
            'text-clip':     ('text-overflow', 'clip'),
        }

        if self.joined_args(values):
            return True

        # text align
        values = {
            'text-left':        ('text-align', 'left'),
            'text-center':      ('text-align', 'center'),
            'text-right':       ('text-align', 'right'),
            'text-justify':     ('text-align', 'justify'),
            'text-start':       ('text-align', 'start'),
            'text-end':         ('text-align', 'end'),
        }

        if self.joined_args(values):
            return True

        if self.argc < 2:
            return False

        # text color
        color = convert_color(self.args[1:])

        if color:
            self.add_style('color', color)
            return True

        # font size
        font_sizes = {
            'xs': ('0.75rem', '1rem'),
            'sm': ('0.875rem', '1.25rem'),
            'base': ('1rem', '1.5rem'),
            'lg': ('1.125rem', '1.75rem'),
            'xl': ('1.25rem', '1.75rem'),
            '2xl': ('1.5rem', '2rem'),
            '3xl': ('1.875rem', '2.25rem'),
            '4xl': ('2.25rem', '2.5rem'),
            '5xl': ('3rem', '1'),
            '6xl': ('3.75rem', '1'),
            '7xl': ('4.5rem', '1'),
            '8xl': ('6rem', '1'),
            '9xl': ('8rem', '1'),
        }

        if self.argc == 2 and self.args[1] in font_sizes:
            fs, lh = font_sizes[self.args[1]]
            self.add_style('font-size', fs)
            self.add_style('line-height', lh)
            return True

        # arbitrary font size
        # e.g. text-14px
        size = merge_value(self.args[1:])
        self.add_style('font-size', size)
        return True

    def antialiased(self):
        if self.argc != 1:
            return False
        self.add_style('-webkit-font-smoothing', 'antialiased')
        self.add_style('-moz-osx-font-smoothing', 'grayscale')
        return True

    def subpixel(self):
        if self.argc == 2 and self.args[1] == 'antialiased':
            self.add_style('-webkit-font-smoothing', 'auto')
            self.add_style('-moz-osx-font-smoothing', 'auto')
            return True
        return False

    def italic(self):
        if self.argc != 1:
            return False
        self.add_style('font-style', 'italic')
        return True

    def not_method(self):
        values = {
            'not-italic':   ('font-style', 'normal'),
            'not-sr-only':  [('position', 'static'),
                             ('width', 'auto'),
                             ('height', 'auto'),
                             ('padding', '0'),
                             ('margin', '0'),
                             ('overflow', 'visible'),
                             ('clip', 'auto'),
                             ('white-space', 'normal')],
        }
        return self.joined_args(values)

    def normal(self):
        # font-variant-numeric and text-transform
        values = {
            'normal-nums': ('font-variant-numeric', 'normal'),
            'normal-case': ('text-transform', 'none'),
        }
        return self.joined_args(values)

    def ordinal(self):
        values = {
            'ordinal': ('font-variant-numeric', 'ordinal'),
        }
        return self.joined_args(values)

    def slashed(self):
        values = {
            'slashed-zero': ('font-variant-numeric', 'slashed-zero'),
        }
        return self.joined_args(values)

    def lining(self):
        values = {
            'lining-nums': ('font-variant-numeric', 'lining-nums'),
        }
        return self.joined_args(values)

    def oldstyle(self):
        values = {
            'oldstyle-nums': ('font-variant-numeric', 'oldstyle-nums'),
        }
        return self.joined_args(values)

    def proportional(self):
        values = {
            'proportional-nums': ('font-variant-numeric', 'proportional-nums'),
        }
        return self.joined_args(values)

    def tabular(self):
        values = {
            'tabular-nums': ('font-variant-numeric', 'tabular-nums'),
        }
        return self.joined_args(values)

    def diagonal(self):
        values = {
            'diagonal-fractions': ('font-variant-numeric', 'diagonal-fractions'),
        }
        return self.joined_args(values)

    def stacked(self):
        values = {
            'stacked-fractions': ('font-variant-numeric', 'stacked-fractions'),
        }
        return self.joined_args(values)

    def tracking(self):
        if self.argc != 2:
            return False

        letter_spacings = {
            'tighter': '-0.05em',
            'tight':   '-0.025em',
            'normal':  '0em',
            'wide':    '0.025em',
            'wider':   '0.05em',
            'widest':  '0.1em',
        }

        ls = letter_spacings.get(self.args[1], self.args[1])
        if self.neg and ls and ls[0] != '-':
            ls = '-' + ls
        self.add_style('letter-spacing', ls)
        return True

    def line(self):
        # text decoration: line-through
        values = {
            'line-through': ('text-decoration-line', 'line-through'),
        }
        if self.joined_args(values):
            return True

        # line clamp
        if self.argc != 3 or self.args[1] != 'clamp':
            return False
        if self.args[2] == 'none':
            self.add_style('overflow', 'visible')
            self.add_style('display', 'block')
            self.add_style('-webkit-box-orient', 'horizontal')
            self.add_style('-webkit-line-clamp', 'none')
            return True
        if self.args[2].isdigit():
            self.add_style('overflow', 'hidden')
            self.add_style('display', '-webkit-box')
            self.add_style('-webkit-box-orient', 'vertical')
            self.add_style('-webkit-line-clamp', self.args[2])
            return True
        return False

    def leading(self):
        if self.argc != 2:
            return False
        line_heights = {
            'none': '1',
            'tight': '1.25',
            'snug': '1.375',
            'normal': '1.5',
            'relaxed': '1.625',
            'loose': '2',
        }
        height = line_heights.get(self.args[1], convert_size(self.args[1]))
        self.add_style('line-height', height)
        return True

    def underline(self):
        # text-decoration-line: underline
        if self.argc == 1:
            self.add_style('text-decoration-line', 'underline')
            return True

        # text-underline-offset
        values = {
            'underline-offset-auto': ('text-underline-offset', 'auto'),
            'underline-offset-0':    ('text-underline-offset', '0px'),
            'underline-offset-1':    ('text-underline-offset', '1px'),
            'underline-offset-2':    ('text-underline-offset', '2px'),
            'underline-offset-4':    ('text-underline-offset', '4px'),
            'underline-offset-8':    ('text-underline-offset', '8px'),
        }
        if self.joined_args(values):
            return True

        if self.argc > 2 and self.args[1] == 'offset':
            value = merge_value(self.args[2:])
            self.add_style('text-underline-offset', value)
            return True

    def overline(self):
        if self.argc != 1:
            return False
        self.add_style('text-decoration-line', 'overline')
        return True

    def no(self):
        values = {
            'no-underline': ('text-decoration-line', 'none'),
        }
        return self.joined_args(values)

    def decoration(self):
        if self.argc < 2:
            return False
        # text decoration style
        values = {
            'decoration-solid':  ('text-decoration-style', 'solid'),
            'decoration-double': ('text-decoration-style', 'double'),
            'decoration-dotted': ('text-decoration-style', 'dotted'),
            'decoration-dashed': ('text-decoration-style', 'dashed'),
            'decoration-wavy':   ('text-decoration-style', 'wavy'),
        }
        if self.joined_args(values):
            return True

        # text decoration color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('text-decoration-color', color)
            return True

        # text decoration thickness
        values = {
            'decoration-auto':      ('text-decoration-thickness', 'auto'),
            'decoration-from-font': ('text-decoration-thickness', 'from-font'),
            'decoration-0':         ('text-decoration-thickness', '0px'),
            'decoration-1':         ('text-decoration-thickness', '1px'),
            'decoration-2':         ('text-decoration-thickness', '2px'),
            'decoration-4':         ('text-decoration-thickness', '4px'),
            'decoration-8':         ('text-decoration-thickness', '8px'),
        }
        if self.joined_args(values):
            return True

        value = merge_value(self.args[1:])
        self.add_style('text-decoration-thickness', value)
        return True

    def uppercase(self):
        if self.argc == 1:
            self.add_style('text-transform', 'uppercase')
            return True
        return False

    def lowercase(self):
        if self.argc == 1:
            self.add_style('text-transform', 'lowercase')
            return True
        return False

    def capitalize(self):
        if self.argc == 1:
            self.add_style('text-transform', 'capitalize')
            return True
        return False

    def truncate(self):
        if self.argc == 1:
            self.add_style('overflow', 'hidden')
            self.add_style('text-overflow', 'ellipsis')
            self.add_style('white-space', 'nowrap')
            return True
        return False

    def indent(self):
        if self.argc == 1:
            return False
        elif self.argc == 2:
            size = convert_size(self.args[1], self.neg)
        else:
            size = merge_value(self.args[1:], self.neg)
        self.add_style('text-indent', size)
        return True

    def align(self):
        values = {
            'align-baseline':    ('vertical-align', 'baseline'),
            'align-top':         ('vertical-align', 'top'),
            'align-middle':      ('vertical-align', 'middle'),
            'align-bottom':      ('vertical-align', 'bottom'),
            'align-text-top':    ('vertical-align', 'text-top'),
            'align-text-bottom': ('vertical-align', 'text-bottom'),
            'align-sub':         ('vertical-align', 'sub'),
            'align-super':       ('vertical-align', 'super'),
        }

        if self.joined_args(values):
            return True
        value = merge_value(self.args[1:])
        self.add_style('vertical-align', value)
        return True

    def whitespace(self):
        values = {
            'whitespace-normal':       ('white-space','normal'),
            'whitespace-nowrap':       ('white-space','nowrap'),
            'whitespace-pre':          ('white-space','pre'),
            'whitespace-pre-line':     ('white-space','pre-line'),
            'whitespace-pre-wrap':     ('white-space','pre-wrap'),
            'whitespace-break-spaces': ('white-space','break-spaces'),
        }
        return self.joined_args(values)

    def hyphens(self):
        values = {
            'hyphens-none':   ('hyphens','none'),
            'hyphens-manual': ('hyphens','manual'),
            'hyphens-auto':   ('hyphens','auto'),
        }
        return self.joined_args(values)

    def bg(self):
        # background blend mode
        values = {
            'bg-blend-normal': ('background-blend-mode','normal'),
            'bg-blend-multiply': ('background-blend-mode','multiply'),
            'bg-blend-screen': ('background-blend-mode','screen'),
            'bg-blend-overlay': ('background-blend-mode','overlay'),
            'bg-blend-darken': ('background-blend-mode','darken'),
            'bg-blend-lighten': ('background-blend-mode','lighten'),
            'bg-blend-color-dodge': ('background-blend-mode','color-dodge'),
            'bg-blend-color-burn': ('background-blend-mode','color-burn'),
            'bg-blend-hard-light': ('background-blend-mode','hard-light'),
            'bg-blend-soft-light': ('background-blend-mode','soft-light'),
            'bg-blend-difference': ('background-blend-mode','difference'),
            'bg-blend-exclusion': ('background-blend-mode','exclusion'),
            'bg-blend-hue': ('background-blend-mode','hue'),
            'bg-blend-saturation': ('background-blend-mode','saturation'),
            'bg-blend-color': ('background-blend-mode','color'),
            'bg-blend-luminosity': ('background-blend-mode','luminosity'),
        }
        if self.joined_args(values):
            return True

        # background attachment: how a background image hehaves when scrolling
        values = {
            'bg-fixed':  ('background-attachment','fixed'),
            'bg-local':  ('background-attachment','local'),
            'bg-scroll': ('background-attachment','scroll'),
        }
        if self.joined_args(values):
            return True

        # background clip
        values = {
            'bg-clip-border':  ('background-clip','border-box'),
            'bg-clip-padding': ('background-clip','padding-box'),
            'bg-clip-content': ('background-clip','content-box'),
            'bg-clip-text':    ('background-clip','text'),
        }
        if self.joined_args(values):
            return True

        # background color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('background-color', color)
            return True

        # background origin
        values = {
            'bg-origin-border':  ('background-origin','border-box'),
            'bg-origin-padding': ('background-origin','padding-box'),
            'bg-origin-content': ('background-origin','content-box'),
        }
        if self.joined_args(values):
            return True

        # background position
        values = {
            'bg-bottom':       ('background-position','bottom'),
            'bg-center':       ('background-position','center'),
            'bg-left':         ('background-position','left'),
            'bg-left-bottom':  ('background-position','left bottom'),
            'bg-left-top':     ('background-position','left top'),
            'bg-right':        ('background-position','right'),
            'bg-right-bottom': ('background-position','right bottom'),
            'bg-right-top':    ('background-position','right top'),
            'bg-top':          ('background-position','top'),
        }
        if self.joined_args(values):
            return True
        if self.argc > 2 and self.args[1] == 'pos':
            value = merge_value(self.args[2:])
            self.add_style('background-position', value)
            return True

        # background repeat
        values = {
            'bg-repeat':       ('background-repeat','repeat'),
            'bg-no-repeat':    ('background-repeat','no-repeat'),
            'bg-repeat-x':     ('background-repeat','repeat-x'),
            'bg-repeat-y':     ('background-repeat','repeat-y'),
            'bg-repeat-round': ('background-repeat','round'),
            'bg-repeat-space': ('background-repeat','space'),
        }
        if self.joined_args(values):
            return True
            
        # background size
        values = {
            'bg-auto':    ('background-size','auto'),
            'bg-cover':   ('background-size','cover'),
            'bg-contain': ('background-size','contain'),
        }
        if self.joined_args(values):
            return True
        if self.argc > 2 and self.args[1] == 'size':
            value = merge_value(self.args[2:])
            self.add_style('background-size', value)
            return True

        # background image
        values = {
            'bg-none':           ('background-image','none'),
            'bg-gradient-to-t':  ('background-image','linear-gradient(to top, var(--fry-gradient-stops))'),
            'bg-gradient-to-tr': ('background-image','linear-gradient(to top right, var(--fry-gradient-stops))'),
            'bg-gradient-to-r':  ('background-image','linear-gradient(to right, var(--fry-gradient-stops))'),
            'bg-gradient-to-br': ('background-image','linear-gradient(to bottom right, var(--fry-gradient-stops))'),
            'bg-gradient-to-b':  ('background-image','linear-gradient(to bottom, var(--fry-gradient-stops))'),
            'bg-gradient-to-bl': ('background-image','linear-gradient(to bottom left, var(--fry-gradient-stops))'),
            'bg-gradient-to-l':  ('background-image','linear-gradient(to left, var(--fry-gradient-stops))'),
            'bg-gradient-to-tl': ('background-image','linear-gradient(to top left, var(--fry-gradient-stops))'),
            'bg-radial':         ('background-image','radial-gradient(var(--fry-gradient-stops))'),
        }
        if self.joined_args(values):
            return True
        if self.argc > 2 and self.args[1] == 'img':
            value = merge_value(self.args[2:])
            self.add_style('background-image', value)
            return True

    def from_method(self):
        if self.argc == 1:
            return False

        # from position
        if self.argc == 2 and is_digit_range(self.args[1], 0, 100):
            self.add_style('--fry-gradient-from-position', f'{self.args[1]}%')
            return True
        if self.argc == 2 and is_percent(self.args[1]):
            self.add_style('--fry-gradient-from-position', self.args[1])
            return True


        # from color
        color = convert_color(self.args[1:])
        if not color:
            return False
        opacity0 = opacity_to(color, 0)
        self.add_style('--fry-gradient-from', f'{color} var(--fry-gradient-from-position)')
        self.add_style('--fry-gradient-to', f'{opacity0} var(--fry-gradient-to-position)')
        self.add_style('--fry-gradient-stops', 'var(--fry-gradient-from), var(--fry-gradient-to)')
        return True


    def via(self):
        if self.argc == 1:
            return False

        # via position
        if self.argc == 2 and is_digit_range(self.args[1], 0, 100):
            self.add_style('--fry-gradient-via-position', f'{self.args[1]}%')
            return True
        if self.argc == 2 and is_percent(self.args[1]):
            self.add_style('--fry-gradient-via-position', self.args[1])
            return True

        # via color
        color = convert_color(self.args[1:])
        if not color:
            return False
        opacity0 = opacity_to(color, 0)
        self.add_style('--fry-gradient-to', f'{opacity0} var(--fry-gradient-to-position)')
        self.add_style('--fry-gradient-stops', f'var(--fry-gradient-from), {color} var(--fry-gradient-via-position), var(--fry-gradient-to)')
        return True

    def to(self):
        if self.argc == 1:
            return False

        # to position
        if self.argc == 2 and is_digit_range(self.args[1], 0, 100):
            self.add_style('--fry-gradient-to-position', f'{self.args[1]}%')
            return True
        if self.argc == 2 and is_percent(self.args[1]):
            self.add_style('--fry-gradient-to-position', self.args[1])
            return True

        # to color
        color = convert_color(self.args[1:])
        if not color:
            return False
        self.add_style('--fry-gradient-to', f'{color} var(--fry-gradient-to-position)')
        return True

    def rounded(self):
        default_size = '0.25rem'
        sizes = {
            'none': '0px',
            'sm':   '0.125rem',
            'md':   '0.375rem',
            'lg':   '0.5rem',
            'xl':   '0.75rem',
            '2xl':  '1rem',
            '3xl':  '1.5rem',
            'full': '9999px',
        }
        positions = {
            's':  ('start-start', 'end-start'),
            'e':  ('start-end', 'end-end'),
            't':  ('top-left', 'top-right'),
            'r':  ('top-right', 'bottom-right'),
            'b':  ('bottom-right', 'bottom-left'),
            'l':  ('top-left', 'bottom-left'),
            'ss': ('start-start',),
            'se': ('start-end',),
            'ee': ('end-end',),
            'es': ('end-start',),
            'tl': ('top-left',),
            'tr': ('top-right',),
            'bl': ('bottom-left',),
            'br': ('bottom-right',),
        }
        if self.argc == 1:
            self.add_style('border-radius', default_size)
            return True
        if self.argc == 2:
            if self.args[1] in sizes:
                self.add_style('border-radius', sizes[self.args[1]])
                return True
            if self.args[1] in positions:
                for pos in positions[self.args[1]]:
                    self.add_style(f'border-{pos}-radius', default_size)
                return True
            value = merge_value(self.args[1:])
            self.add_style('border-radius', value)
            return True
        if self.args[1] not in positions:
            return False
        if self.argc == 3 and self.args[2] in sizes:
            size = sizes[self.args[2]]
        else:
            size = merge_value(self.args[2:])
        for pos in positions[self.args[1]]:
            self.add_style(f'border-{pos}-radius', size)
        return True

    def border(self):
        # set table border collapse
        values = {
            'border-collapse': ('border-collapse','collapse'),
            'border-separate': ('border-collapse','separate'),
        }

        if self.joined_args(values):
            return True

        # set border style
        values = {
            'border-solid':  ('border-style','solid'),
            'border-dashed': ('border-style','dashed'),
            'border-dotted': ('border-style','dotted'),
            'border-double': ('border-style','double'),
            'border-hidden': ('border-style','hidden'),
            'border-none':   ('border-style','none'),
        }

        if self.joined_args(values):
            return True

        # set table border spacing
        if self.argc > 2 and self.args[1] == 'spacing':
            if self.args[2] in 'xy' and self.argc == 4:
                size = convert_size(self.args[3])
                self.add_style(f'--fry-border-spacing-{self.args[2]}', size)
            elif self.argc == 3:
                size = convert_size(self.args[2])
                self.add_style('--fry-border-spacing-x', size)
                self.add_style('--fry-border-spacing-y', size)
            else:
                return False
            self.add_style('border-spacing', 'var(--fry-border-spacing-x) var(--fry-border-spacing-y)')
            return True

        # set border width and border color
        positions = {
            'x': ('left', 'right'),
            'y': ('top', 'bottom'),
            's': ('inline-start',),
            'e': ('inline-end',),
            't': ('top',),
            'r': ('right',),
            'b': ('bottom',),
            'l': ('left',),
        }
        default_size = 1

        # border设置宽度为1px
        if self.argc == 1:
            self.add_style('border-width', f'{default_size}px')
            return True
        color = convert_color(self.args[1:])
        if color:
            self.add_style('border-color', color)
            return True

        if self.argc == 2:
            if self.args[1] in positions:
                for pos in positions[self.args[1]]:
                    self.add_style(f'border-{pos}-width', f'{default_size}px')
                return True
            if self.args[1].isdigit():
                self.add_style('border-width', f'{self.args[1]}px')
                return True
            value = merge_value(self.args[1:])
            self.add_style('border-width', value)
            return True
        if self.args[1] not in positions:
            return False

        color = convert_color(self.args[2:])
        if color:
            for pos in positions[self.args[1]]:
                self.add_style(f'border-{pos}-color', color)
            return True

        if self.argc == 3 and self.args[2].isdigit():
            size = f'{self.args[2]}px'
        else:
            size = merge_value(self.args[2:])
        for pos in positions[self.args[1]]:
            self.add_style(f'border-{pos}-width', size)
        return True

    def divide(self):
        # divide作用于其直接子元素
        self.css.selector_template += ' > :not([hidden]) ~ :not([hidden])'

        # divide styles
        values = {
            'divide-solid':  ('border-style','solid'),
            'divide-dashed': ('border-style','dashed'),
            'divide-dotted': ('border-style','dotted'),
            'divide-double': ('border-style','double'),
            'divide-none':   ('border-style','none'),
        }

        if self.joined_args(values):
            return True

        if self.argc == 1:
            return False

        # divide color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('border-color', color)
            return True

        # divide width
        if self.args[1] not in 'xy':
            return False
        if self.argc == 2:
            width = '1px'
        elif self.args[2].isdigit():
            width = f'{self.args[2]}px'
        elif self.args[2] == 'reverse':
            self.add_style(f'--fry-divide-{self.args[1]}-reverse', '1')
            return True
        else:
            width = merge_value(self.args[2:])
        if self.args[1] == 'x':
            self.add_style('--fry-divide-x-reverse', '0')
            self.add_style('border-left-width', f'calc({width} * calc(1 - var(--fry-divide-x-reverse)))')
            self.add_style('border-right-width', f'calc({width} * var(--fry-divide-x-reverse))')
        else:
            self.add_style('--fry-divide-y-reverse', '0')
            self.add_style('border-top-width', f'calc({width} * calc(1 - var(--fry-divide-y-reverse)))')
            self.add_style('border-bottom-width', f'calc({width} * var(--fry-divide-y-reverse))')
        return True

    def outline(self):
        # outline style
        values = {
            'outline-none':   [('outline', '2px solid transparent'), ('outline-offset', '2px')],
            'outline':        ('outline-style', 'solid'),
            'outline-dashed': ('outline-style', 'dashed'),
            'outline-dotted': ('outline-style', 'dotted'),
            'outline-double': ('outline-style', 'double'),
        }
        if self.joined_args(values):
            return True

        # outline color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('outline-color', color)
            return True
        
        # outline offset
        if self.args[1] == 'offset' and self.argc > 2:
            if self.argc == 3 and self.args[2].isdigit():
                offset = f'{self.args[2]}px'
            else:
                offset = merge_value(self.args[2:])
            self.add_style('outline-offset', offset)
            return True

        # outline width
        if self.argc == 2 and self.args[1].isdigit():
            width = f'{self.args[1]}px'
        else:
            width = merge_value(self.args[1:])
        self.add_style('outline-width', width)
        return True

    def ring(self):
        # ring inset
        values = {
            'ring-inset': ('--fry-ring-inset','inset'),
        }

        if self.joined_args(values):
            return True

        # ring color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('--fry-ring-color', color)
            return True

        # ring offset width and ring offset color
        if self.argc > 2 and self.args[1] == 'offset':
            color = convert_color(self.args[2:])
            if color:
                self.add_style('--fry-ring-offset-color', color)
                return True
            if self.args[2].isdigit():
                width = f'{self.args[2]}px'
            else:
                width = merge_value(self.args[2:])
            self.add_style('--fry-ring-offset-width', width)
            return True

        # ring width
        if self.argc == 1:
            width = '3px'
        elif self.argc == 2 and self.args[1].isdigit():
            width = f'{self.args[1]}px'
        else:
            width = merge_value(self.args[1:])
        self.add_style('--fry-ring-offset-shadow', 'var(--fry-ring-inset) 0 0 0 var(--fry-ring-offset-width) var(--fry-ring-offset-color)')
        self.add_style('--fry-ring-shadow', f'var(--fry-ring-inset) 0 0 0 calc({width} + var(--fry-ring-offset-width)) var(--fry-ring-color)')
        self.add_style('box-shadow', 'var(--fry-ring-offset-shadow), var(--fry-ring-shadow), var(--fry-shadow, 0 0 #0000)')
        return True

    def shadow(self):
        values = {
            'sm':     ('0 1px 2px 0 rgb(0 0 0 / 0.05)',
                       '0 1px 2px 0 var(--fry-shadow-color)'),
            'nm':     ('0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
                       '0 1px 3px 0 var(--fry-shadow-color), 0 1px 2px -1px var(--fry-shadow-color)'),
            'md':     ('0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
                       '0 4px 6px -1px var(--fry-shadow-color), 0 2px 4px -2px var(--fry-shadow-color)'),
            'lg':     ('0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
                       '0 10px 15px -3px var(--fry-shadow-color), 0 4px 6px -4px var(--fry-shadow-color)'),
            'xl':     ('0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
                       '0 20px 25px -5px var(--fry-shadow-color), 0 8px 10px -6px var(--fry-shadow-color)'),
            '2xl':    ('0 25px 50px -12px rgb(0 0 0 / 0.25)',
                       '0 25px 50px -12px var(--fry-shadow-color)'),
            'inner':  ('inset 0 2px 4px 0 rgb(0 0 0 / 0.05)',
                       'inset 0 2px 4px 0 var(--fry-shadow-color)'),
            'none':   ('0 0 #0000',
                       '0 0 #0000'),
        }

        # box shadow color
        color = convert_color(self.args[1:])
        if color:
            self.add_style('--fry-shadow-color', color)
            self.add_style('--fry-shadow', 'var(--fry-shadow-colored)')
            return True

        if self.argc == 1:
            size = 'nm'
        elif self.argc == 2 and self.args[1] in values:
            size = self.args[1]
        else:
            value = merge_value(self.args[1:])
            self.add_style('box-shadow', value)
            return True
        shadow1, shadow2 = values[size]
        self.add_style('--fry-shadow', shadow1)
        self.add_style('--fry-shadow-colored', shadow2)
        self.add_style('box-shadow', 'var(--fry-ring-offset-shadow, 0 0 #0000), var(--fry-ring-shadow, 0 0 #0000), var(--fry-shadow)')
        return True

    def filter_opacity(self, argc, args):
        if argc != 2:
            return None
        if not args[1].isdigit():
            return None
        value = int(self.args[1])
        if value < 0 or value > 100:
            return None
        return value/100

    def opacity(self):
        value = self.filter_opacity(self.argc, self.args)
        if value is None:
            return False
        self.add_style('opacity', str(value))
        return True

    def mix(self):
        values = {
            'mix-blend-normal':       ('mix-blend-mode','normal'),
            'mix-blend-multiply':     ('mix-blend-mode','multiply'),
            'mix-blend-screen':       ('mix-blend-mode','screen'),
            'mix-blend-overlay':      ('mix-blend-mode','overlay'),
            'mix-blend-darken':       ('mix-blend-mode','darken'),
            'mix-blend-lighten':      ('mix-blend-mode','lighten'),
            'mix-blend-color-dodge':  ('mix-blend-mode','color-dodge'),
            'mix-blend-color-burn':   ('mix-blend-mode','color-burn'),
            'mix-blend-hard-light':   ('mix-blend-mode','hard-light'),
            'mix-blend-soft-light':   ('mix-blend-mode','soft-light'),
            'mix-blend-difference':   ('mix-blend-mode','difference'),
            'mix-blend-exclusion':    ('mix-blend-mode','exclusion'),
            'mix-blend-hue':          ('mix-blend-mode','hue'),
            'mix-blend-saturation':   ('mix-blend-mode','saturation'),
            'mix-blend-color':        ('mix-blend-mode','color'),
            'mix-blend-luminosity':   ('mix-blend-mode','luminosity'),
            'mix-blend-plus-lighter': ('mix-blend-mode','plus-lighter'),
        }

        return self.joined_args(values)

    filter_vars = 'var(--fry-blur) var(--fry-brightness) var(--fry-contrast) var(--fry-grayscale) var(--fry-hue-rotate) var(--fry-invert) var(--fry-saturate) var(--fry-sepia) var(--fry-drop-shadow)'

    backdrop_filter_vars = 'var(--fry-backdrop-blur) var(--fry-backdrop-brightness) var(--fry-backdrop-contrast) var(--fry-backdrop-grayscale) var(--fry-backdrop-hue-rotate) var(--fry-backdrop-invert) var(--fry-backdrop-opacity) var(--fry-backdrop-saturate) var(--fry-backdrop-sepia)'

    def filter_blur(self, argc, args):
        sizes = {
            'none': '0',
            'sm':   '4px',
            'nm':   '8px',
            'md':   '12px',
            'lg':   '16px',
            'xl':   '24px',
            '2xl':  '40px',
            '3xl':  '64px',
        }

        if argc == 1:
            size = sizes['nm']
        elif argc == 2 and args[1] in sizes:
            size = sizes[args[1]]
        else:
            size = merge_value(args[1:])
        return size

    def blur(self):
        size = self.filter_blur(self.argc, self.args)
        self.add_style('--fry-blur', f'blur({size})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_brightness(self, argc, args):
        if argc != 2 or not args[1].isdigit():
            return None
        value = int(args[1])
        if value < 0 or value > 200:
            return None
        return value/100

    def brightness(self):
        value = self.filter_brightness(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-brightness', f'brightness({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_contrast(self, argc, args):
        if argc != 2 or not args[1].isdigit():
            return None
        value = int(args[1])
        if value < 0 or value > 200:
            return None
        return value/100

    def contrast(self):
        value = self.filter_contrast(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-contrast', f'contrast({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def drop(self):
        if self.argc < 2 or self.args[1] != 'shadow':
            return False

        values = {
            'sm':   ('0 1px 1px rgb(0 0 0 / 0.05)',),
            'nm':   ('0 1px 2px rgb(0 0 0 / 0.1))', '0 1px 1px rgb(0 0 0 / 0.06)'),
            'md':   ('0 4px 3px rgb(0 0 0 / 0.07)', '0 2px 2px rgb(0 0 0 / 0.06)'),
            'lg':   ('0 10px 8px rgb(0 0 0 / 0.04)', '0 4px 3px rgb(0 0 0 / 0.1)'),
            'xl':   ('0 20px 13px rgb(0 0 0 / 0.03)', '0 8px 5px rgb(0 0 0 / 0.08)'),
            '2xl':  ('0 25px 25px rgb(0 0 0 / 0.15)',),
            'none': ('0 0 #0000',),
        }
        if self.argc == 2:
            value = values['nm']
        elif self.argc == 3 and self.args[2] in values:
            value = values[self.args[2]]
        elif self.argc == 3:
            value = (merge_value(self.args[2:]),)
        elif self.argc == 4:
            value = (merge_value([self.args[2]]), merge_value([self.args[3]]))
        else:
            return False
        self.add_style('--fry-drop-shadow', ' '.join(f'drop-shadow({v})' for v in value))
        self.add_style('filter', self.filter_vars)
        return True

    def filter_grayscale(self, argc, args):
        if argc == 1:
            value = 100
        elif argc == 2 and args[1].isdigit():
            value = int(args[1])
            if value < 0 or value > 100:
                return None
        else:
            return None
        return f'{value}%'

    def grayscale(self):
        value = self.filter_grayscale(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-grayscale', f'grayscale({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_hue(self, argc, args, neg):
        if argc != 3 and args[1] != 'rotate' and not args[2].isdigit():
            return None
        value = int(args[2])
        if value < 0 or value > 360:
            return None
        if neg:
            value = f'-{value}deg'
        else:
            value = f'{value}deg'
        return value

    def hue(self):
        value = self.filter_hue(self.argc, self.args, self.neg)
        if value is None:
            return False
        self.add_style('--fry-hue-rotate', f'hue-rotate({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_invert(self, argc, args):
        if argc == 1:
            value = 100
        elif argc == 2 and args[1].isdigit():
            value = int(args[1])
            if value < 0 or value > 100:
                return None
        else:
            return None
        return f'{value}%'

    def invert(self):
        value = self.filter_invert(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-invert', f'invert({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_saturate(self, argc, args):
        if argc != 2 or not args[1].isdigit():
            return None
        value = int(args[1])
        if value < 0 or value > 200:
            return None
        return value/100

    def saturate(self):
        value = self.filter_saturate(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-saturate', f'saturate({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter_sepia(self, argc, args):
        if argc == 1:
            value = 100
        elif argc == 2 and args[1].isdigit():
            value = int(args[1])
            if value < 0 or value > 100:
                return None
        else:
            return None
        return f'{value}%'

    def sepia(self):
        value = self.filter_sepia(self.argc, self.args)
        if value is None:
            return False
        self.add_style('--fry-sepia', f'sepia({value})')
        self.add_style('filter', self.filter_vars)
        return True

    def filter(self):
        values = {
            'filter-none': ('filter','none'),
        }
        return self.joined_args(values)

    def backdrop(self):
        values = {
            'backdrop-filter-none': [('-webkit-backdrop-filter', 'none'),
                                             ('backdrop-filter', 'none')],
        }
        if self.joined_args(values):
            return True

        if self.argc == 1:
            return False
        
        argc = self.argc - 1
        args = self.args[1:]
        neg  = self.neg

        if self.args[1] == 'blur':
            size = self.filter_blur(argc, args)
            self.add_style('--fry-backfrop-blur', f'blur({size})')
        elif self.args[1] == 'brightness':
            value = self.filter_brightness(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-brightness', f'brightness({value})')
        elif self.args[1] == 'contrast':
            value = self.filter_contrast(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-contrast', f'contrast({value})')
        elif self.args[1] == 'grayscale':
            value = self.filter_grayscale(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-grayscale', f'grayscale({value})')
        elif self.args[1] == 'hue':
            value = self.filter_hue(argc, args, neg)
            if value is None:
                return False
            self.add_style('--fry-backdrop-hue-rotate', f'hue-rotate({value})')
        elif self.args[1] == 'invert':
            value = self.filter_invert(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-invert', f'invert({value})')
        elif self.args[1] == 'opacity':
            value = self.filter_opacity(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-opacity', f'opacity({value})')
        elif self.args[1] == 'saturate':
            value = self.filter_saturate(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-saturate', f'saturate({value})')
        elif self.args[1] == 'sepia':
            value = self.filter_sepia(argc, args)
            if value is None:
                return False
            self.add_style('--fry-backdrop-sepia', f'sepia({value})')
        else:
            return False

        self.add_style('-webkit-backdrop-filter', self.backdrop_filter_vars)
        self.add_style('backdrop-filter', self.backdrop_filter_vars)
        return True

    def caption(self):
        # set table caption side
        values = {
            'caption-top':    ('caption-side','top'),
            'caption-bottom': ('caption-side','bottom'),
        }
        return self.joined_args(values)

    def transition(self):
        # transition none
        values = {
            'transition-none': ('transition-property','none'),
        }

        if self.joined_args(values):
            return True

        # transition properties
        values = {
            'transation-all': ('transition-property','all'),
            'transition':     ('transition-property','color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter'),
            'transition-colors': ('transition-property','color, background-color, border-color, text-decoration-color, fill, stroke'),
            'transition-opacity': ('transition-property','opacity'),
            'transition-shadow': ('transition-property','box-shadow'),
            'transition-transform': ('transition-property','transform'),
        }

        if not self.joined_args(values):
            prop = merge_value(self.args[1:])
            self.add_style('transition-property', prop)
        self.add_style('transition-timing-function', 'cubic-bezier(0.4, 0, 0.2, 1)')
        self.add_style('transition-duration', '150ms')
        return True
    
    def duration(self):
        if self.argc != 2 and not self.args[1].isdigit():
            return False
        self.add_style('transition-duration', f'{self.args[1]}ms')
        return True
    
    def ease(self):
        if self.argc == 1:
            return False
        values = {
            'ease-linear': ('transition-timing-function','linear'),
            'ease-in':     ('transition-timing-function','cubic-bezier(0.4, 0, 1, 1)'),
            'ease-out':    ('transition-timing-function','cubic-bezier(0, 0, 0.2, 1)'),
            'ease-in-out': ('transition-timing-function','cubic-bezier(0.4, 0, 0.2, 1)'),
        }
        if not self.joined_args(values):
            timing = merge_value(self.args[1])
            self.add_style('transition-timing-function', timing)
        return True

    def delay(self):
        if self.argc != 2 and not self.args[1].isdigit():
            return False
        self.add_style('transition-delay', f'{self.args[1]}ms')
        return True
        
    def animate(self):
        if self.argc == 1:
            return False
        values = {
            'animate-none':              ('animation','none'),
            'animate-spin':              ('animation','spin 1s linear infinite'),
            'animate-ping':              ('animation','ping 1s cubic-bezier(0, 0, 0.2, 1) infinite'),
            'animate-pulse':             ('animation','pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite'),
            'animate-bounce':            ('animation','bounce 1s infinite'),
            'animate-normal':            ('animation-direction', 'normal'),
            'animate-reverse':           ('animation-direction', 'reverse'),
            'animate-alternate':         ('animation-direction', 'alternate'),
            'animate-alternate-reverse': ('animation-direction', 'alternate-reverse'),
            'animate-forwards':          ('animation-fill-mode', 'forwards'),
            'animate-backwards':         ('animation-fill-mode', 'backwards'),
            'animate-infinite':          ('animation-iteration-count', 'infinite'),
            'animate-paused':            ('animation-play-state', 'paused'),
            'animate-running':           ('animation-play-state', 'running'),
            'animate-ease':              ('animation-timing-function', 'ease'),
            'animate-ease-in':           ('animation-timing-function', 'ease-in'),
            'animate-ease-out':          ('animation-timing-function', 'ease-out'),
            'animate-ease-in-out':       ('animation-timing-function', 'ease-in-out'),
            'animate-linear':            ('animation-timing-function', 'linear'),
        }

        if self.joined_args(values):
            return True

        if self.argc > 2:
            # 支持多个animation的情况，需要逗号隔开
            sub = self.args[1]
            if sub == 'name':
                key = 'animation-name'
            elif sub == 'duration':
                key = 'animation-duration'
            elif sub == 'delay':
                key = 'animation-delay'
            elif sub == 'dir':
                key = 'animation-direction'
            elif sub == 'fill':
                key = 'animation-fill-mode'
            elif sub == 'count':
                key = 'animation-iteration-count'
            elif sub == 'state':
                key = 'animation-play-state'
            elif sub == 'ease':
                key = 'animation-timing-function'
                if self.argc == 6 and all(is_digit(v) or is_float(v) for v in self.args[2:]):
                    args = self.args[2:]
                    self.add_style(key, f'cubic-bezier({args[0]}, {args[1]}, {args[2]}, {args[3]})')
                    return True
            else:
                animation = merge_value(self.args[1:])
                self.add_style('animation', animation)
                return True
            value = merge_value(self.args[2:], self.neg)
            self.add_style(key, value)
        else:
            animation = merge_value(self.args[1:])
            self.add_style('animation', animation)
        return True
    
    transform_vars = 'translate(var(--fry-translate-x), var(--fry-translate-y)) rotate(var(--fry-rotate)) skewX(var(--fry-skew-x)) skewY(var(--fry-skew-y)) scaleX(var(--fry-scale-x)) scaleY(var(--fry-scale-y))'

    gpu_transform_vars = 'translate3d(var(--fry-translate-x), var(--fry-translate-y), 0) rotate(var(--fry-rotate)) skewX(var(--fry-skew-x)) skewY(var(--fry-skew-y)) scaleX(var(--fry-scale-x)) scaleY(var(--fry-scale-y))'

    def scale(self):
        if self.argc == 2 and self.args[1].isdigit():
            scale = self.args[1]
            dir = 'xy'
        elif self.argc == 3 and self.args[1] in 'xy' and self.args[2].isdigit():
            scale = self.args[2]
            dir = self.args[1]
        else:
            return False
        scale = int(self.args[1])/100
        scale = -scale if self.neg else scale
        if 'x' in dir:
            self.add_style('--fry-scale-x', str(scale))
        if 'y' in dir:
            self.add_style('--fry-scale-y', str(scale))
        self.add_style('transform', self.transform_vars)
        return True

    def rotate(self):
        if self.argc == 2 and self.args[1].isdigit():
            deg = ('-' if self.neg else '') + self.args[1]
            self.add_style('--fry-rotate', f'{deg}deg')
            self.add_style('transform', self.transform_vars)
            return True
        return False

    def translate(self):
        if self.argc == 3 and self.args[1] in 'xy':
            size = convert_size(self.args[2], self.neg)
            self.add_style(f'--fry-translate-{self.args[1]}', size)
            self.add_style('transform', self.transform_vars)
            return True
        return False

    def skew(self):
        if self.argc == 3 and self.args[1] in 'xy' and self.args[2].isdigit():
            deg = ('-' if self.neg else '') + self.args[2]
            self.add_style(f'--fry-skew-{self.args[1]}', f'{deg}deg')
            self.add_style('transform', self.transform_vars)
            return True
        return False

    def origin(self):
        if self.argc == 1:
            return False
        values = {
            'origin-center':       ('transform-origin','center'),
            'origin-top':          ('transform-origin','top'),
            'origin-top-right':    ('transform-origin','top right'),
            'origin-right':        ('transform-origin','right'),
            'origin-bottom-right': ('transform-origin','bottom right'),
            'origin-bottom':       ('transform-origin','bottom'),
            'origin-bottom-left':  ('transform-origin','bottom left'),
            'origin-left':         ('transform-origin','left'),
            'origin-top-left':     ('transform-origin','top left'),
        }
        if not self.joined_args(values):
            value = merge_value(self.args[1:])
            self.add_style('transform-origin', value)
        return True

    def transform(self):
        values = {
            'transform-none': ('transform','none'),
            'transform-gpu':  ('transform', self.gpu_transform_vars),
        }
        if self.joined_args(values):
            return True

    def accent(self):
        color = convert_color(self.args[1:])
        if color:
            self.add_style('accent-color', color)
            return True
        return False

    def appearance(self):
        values = {
            'appearance-none': ('appearance','none'),
        }
        return self.joined_args(values)

    def cursor(self):
        if self.argc == 1:
            return False
        value = merge_value(self.args[1:])
        self.add_style('cursor', value)
        return True

    def caret(self):
        color = convert_color(self.args[1:])
        if color:
            self.add_style('caret-color', color)
            return True
        return False

    def pointer(self):
        values = {
            'pointer-events-none': ('pointer-events','none'),
            'pointer-events-auto': ('pointer-events','auto'),
        }
        return self.joined_args(values)

    def resize(self):
        values = {
            'resize-none': ('resize','none'),
            'resize-y':    ('resize','vertical'),
            'resize-x':    ('resize','horizontal'),
            'resize':      ('resize','both'),
        }
        return self.joined_args(values)

    def scroll(self):
        values = {
            'scroll-auto':   ('scroll-behavior','auto'),
            'scroll-smooth': ('scroll-behavior','smooth'),
        }
        if self.joined_args(values):
            return True
        if self.argc == 3 and self.args[1][0] in 'mp':
            self.args = self.args[1:]
            self.argc = 2
            if self():
                styles = self.css.styles
                self.css.styles = [(f'scroll-{k}', v) for k, v in styles]
                return True
        return False

    def snap(self):
        values = {
            'snap-start':      ('scroll-snap-align','start'),
            'snap-end':        ('scroll-snap-align','end'),
            'snap-center':     ('scroll-snap-align','center'),
            'snap-align-none': ('scroll-snap-align','none'),
            'snap-normal':     ('scroll-snap-stop','normal'),
            'snap-always':     ('scroll-snap-stop','always'),
            'snap-none':       ('scroll-snap-type','none'),
            'snap-x':          ('scroll-snap-type','x var(--fry-scroll-snap-strictness)'),
            'snap-y':          ('scroll-snap-type','y var(--fry-scroll-snap-strictness)'),
            'snap-both':       ('scroll-snap-type','both var(--fry-scroll-snap-strictness)'),
            'snap-mandatory':  ('--fry-scroll-snap-strictness','mandatory'),
            'snap-proximity':  ('--fry-scroll-snap-strictness','proximity'),
        }
        return self.joined_args(values)

    def touch(self):
        values = {
            'touch-auto':         ('touch-action','auto'),
            'touch-none':         ('touch-action','none'),
            'touch-pan-x':        ('touch-action','pan-x'),
            'touch-pan-left':     ('touch-action','pan-left'),
            'touch-pan-right':    ('touch-action','pan-right'),
            'touch-pan-y':        ('touch-action','pan-y'),
            'touch-pan-up':       ('touch-action','pan-up'),
            'touch-pan-down':     ('touch-action','pan-down'),
            'touch-pinch-zoom':   ('touch-action','pinch-zoom'),
            'touch-manipulation': ('touch-action','manipulation'),
        }
        return self.joined_args(values)

    def select(self):
        values = {
            'select-none': ('user-select','none'),
            'select-text': ('user-select','text'),
            'select-all':  ('user-select','all'),
            'select-auto': ('user-select','auto'),
        }
        return self.joined_args(values)

    def will(self):
        values = {
            'will-change-auto':      ('will-change','auto'),
            'will-change-scroll':    ('will-change','scroll-position'),
            'will-change-contents':  ('will-change','contents'),
            'will-change-transform': ('will-change','transform'),
        }
        return self.joined_args(values)

    def fill(self):
        if self.argc == 1:
            return False
        color = convert_color(self.args[1:])
        if color:
            self.add_style('fill', color)
            return True
        return False

    def stroke(self):
        if self.argc == 1:
            return False
        color = convert_color(self.args[1:])
        if color:
            self.add_style('stroke', color)
        else:
            width = merge_value(self.args[1:])
            self.add_style('stroke-width', width)
        return True

    def sr(self):
        values = {
            'sr-only': [('position', 'absolute'),
                        ('width', '1px'),
                        ('height', '1px'),
                        ('padding', '0'),
                        ('margin', '-1px'),
                        ('overflow', 'hidden'),
                        ('clip', 'rect(0, 0, 0, 0)'),
                        ('white-space', 'nowrap'),
                        ('border-width', '0')],
        }
        return self.joined_args(values)

