from fryweb.element import Element, component_id_attr_name, component_name_attr_name, children_attr_name, type_attr_name
from fryweb.utils import static_url
from fryweb.config import fryconfig
from importlib import import_module
from html import escape
import json

class Page(object):
    def __init__(self):
        # 记录当前已经处理的组件script元素列表，列表长度是当前正在处理的组件的ID
        self.components = {}
        # 组件实例ID到子组件引用/引用列表的映射关系, cid -> (refname -> childcid | list of childcid)
        self.cid2childrefs = {}
        self.hasjs = False

    def add_component(self, component):
        cid = len(self.components) + 1
        self.components[cid] = component
        component['cid'] = cid
        self.cid2childrefs[cid] = {} 
        return cid

    def add_ref(self, cid, refname, childcid):
        childrefs = self.cid2childrefs[cid]
        if refname in childrefs:
            refs = childrefs[refname]
        else:
            refs = set()
            childrefs[refname] = refs
        refs.add(childcid)

    def child_refs(self, cid):
        origin = self.cid2childrefs.get(cid, {})
        refs = {}
        for name, ids in origin.items():
            if name.endswith(':a'):
                refs[name[:-2]] = sorted(ids)
            else:
                if len(ids) != 1:
                    raise RuntimeError(f"More than ONE ref value for '{name}'.")
                refs[name] = ids.pop()
        return refs


def render(element, **kwargs):
    page = Page()
    if isinstance(element, Element):
        element = element.render(page)
    elif callable(element) and getattr(element, '__name__', 'anonym')[0].isupper():
        element = Element(element, kwargs).render(page)
    elif isinstance(element, str):
        if '.' in element:
            module, _, comp = element.rpartition('.')
            module = import_module(module)
            component = getattr(module, comp)
            if callable(component) and comp[0].isupper():
                element = Element(component, kwargs).render(page)
        elif element and element[0].islower():
            element = Element(element, kwargs).render(page)
    return element


def html(content='div',
         args={},
         title='',
         lang='en',
         rootclass='',
         charset='utf-8',
         viewport="width=device-width, initial-scale=1.0",
         metas={},
         properties={},
         equivs={},
         autoreload=True,
        ):
    sep = '\n    '
    main_content = render(content, **args)
    page = main_content.page
    if main_content.name == 'body':
        body = main_content
    else:
        body = Element('body', dict(children=[main_content]), True)
    components = []
    for c in page.components.values():
        scriptprops = {
            type_attr_name: 'text/x-frydata',
            component_id_attr_name: c['cid'],
            component_name_attr_name: c['name'],
        }
        content = {}
        if 'setup' in c:
            content['setup'] = c['setup']
            content['refs'] = c['refs']
            content['args'] = c['args']
        scriptprops[children_attr_name] = [escape(json.dumps(content))]
        comp = Element('script', scriptprops, True)
        components.append(comp)
    if components:
        components = Element('div', dict(style=dict(display='none'), children=components), True)
        body.props[children_attr_name].append(components)
    if page.hasjs:
        # 此时必定存在js_url
        script = f"""
      const {{ hydrate }} = await import("{static_url(fryconfig.js_url)}");
      await hydrate(document.documentElement);
"""
        hydrate_script = Element('script', dict(type='module', children=[script]), True)
        body.props[children_attr_name].append(hydrate_script)

    if fryconfig.debug and autoreload:
        script = f"""
      let serverId = null;
      let eventSource = null;
      let timeoutId = null;
      function checkAutoReload() {{
          if (timeoutId !== null) clearTimeout(timeoutId);
          timeoutId = setTimeout(checkAutoReload, 1000);
          if (eventSource !== null) eventSource.close();
          eventSource = new EventSource("{fryconfig.check_reload_url}");
          eventSource.addEventListener('open', () => {{
              console.log(new Date(), "Auto reload connected.");
              if (timeoutId !== null) clearTimeout(timeoutId);
              timeoutId = setTimeout(checkAutoReload, 1000);
          }});
          eventSource.addEventListener('message', (event) => {{
              const data = JSON.parse(event.data);
              if (serverId === null) {{
                  serverId = data.serverId;
              }} else if (serverId !== data.serverId) {{
                  if (eventSource !== null) eventSource.close();
                  if (timeoutId !== null) clearTimeout(timeoutId);
                  location.reload();
                  return;
              }}
              if (timeoutId !== null) clearTimeout(timeoutId);
              timeoutId = setTimeout(checkAutoReload, 1000);
          }});
      }}
      checkAutoReload();
"""
        autoreload = Element('script', dict(type='module', children=[script]), True)
        body.props[children_attr_name].append(autoreload)

    metas = sep.join(f'<meta name="{name}" content="{value}">'
                       for name, value in metas.items())
    properties = sep.join(f'<meta property="{property}" content="{value}">'
                            for property, value in properties.items())
    equivs = sep.join(f'<meta http-equiv="{equiv}" content="{value}">'
                            for equiv, value in equivs.items())
    # no need to use importmap
    #importmap = f'''
    #<script type="importmap">
    #  {{
    #    "imports": {{
    #      "fryweb": "{static_url('js/fryweb.js')}"
    #    }}
    #  }}
    #</script>
    #'''

    if rootclass:
        rootclass = f' class="{rootclass}"'
    else:
        rootclass = ''

    return f'''\
<!DOCTYPE html>
<html lang={lang}{rootclass}>
  <head>
    <meta charset="{charset}">
    <title>{title}</title>
    <meta name="viewport" content="{viewport}">
    {metas}
    {properties}
    {equivs}
    <link rel="stylesheet" href="{static_url(fryconfig.css_url)}">
  </head>
  {body}
</html>
'''
