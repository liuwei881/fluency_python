#coding=utf-8


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    # print(tag('br'))
    # print(tag('p', 'hello'))
    # print(tag('p', 'hello', 'world'))
    # print(tag('p', 'hello', id=33))
    # print(tag('p',' hello', 'world', cls='sidebar'))
    # print(tag(content='testing', name='img'))
    # my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    # print(tag(**my_tag))
    # import inspect
    # sig = inspect.signature(tag)
    # my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
    #           'src': 'sunset.jpg', 'cls': 'framed'}
    # bound_args = sig.bind(**my_tag)
    # for name, value in bound_args.arguments.items():
    #     print(name, '=', value)
    # del my_tag['name']
    # bound_args = sig.bind(**my_tag)
    from functools import partial
    picture = partial(tag, 'img', cls='pic-frame')
    print(picture(src='wumpus.jpeg'))
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
