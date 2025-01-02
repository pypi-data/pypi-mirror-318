import jinja2

from .loaders import load_any, load_filters
from .exceptions import GaelinaRenderingException

MAX_ITERATIONS = 200


def gaelina(path):
    source = Source(
        load_any(path),
        load_filters(path, {})
    )
    if isinstance(source.data, dict):
        return GaelinaDict(source.data, source)
    return source.data


def gaelina_value(value, data):
    if isinstance(value, dict):
        return GaelinaDict(value, data)
    if isinstance(value, list):
        return GaelinaList(value, data)
    if isinstance(value, str) and '{{' in value:
        return g_render(value, data)
    return value


def g_render(str_, source):
    render = str_
    env = jinja2.Environment(autoescape=True)
    for _ in range(MAX_ITERATIONS):
        template = env.from_string(render)
        new_render = template.render(source.data, filters=source.filters)
        if new_render == render:
            return render
        render = new_render
    raise GaelinaRenderingException(f'Failed to render template: {str_}')


class Source: # pylint: disable=too-few-public-methods
    def __init__(self, data, filters):
        self.data = data
        self.filters = filters


class GaelinaDict(dict):
    def __init__(self, value, source):
        super().__init__(value)
        self.source = source

    def __getitem__(self, key):
        value = super().__getitem__(key)
        return gaelina_value(value, self.source)

    def get(self, key, default_value):
        value = super().get(key, default_value)
        return gaelina_value(value, self.source)


class GaelinaList(list):
    def __init__(self, value, source):
        super().__init__(value)
        self.source = source

    def __getitem__(self, index):
        value = super().__getitem__(index)
        if isinstance(index, slice):
            return GaelinaList(value, self.source)
        return gaelina_value(value, self.source)
