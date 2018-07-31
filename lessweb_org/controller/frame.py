from importlib import import_module, reload
from lessweb import Context
from lessweb_org.view import pydom, frames


def view_processor(ctx: Context):
    ret = ctx()
    view = ctx.view
    if not view:
        if isinstance(ret, (dict, list)):
            ctx.set_json_header()
        return ret

    if isinstance(view, str):  # enable auto-reload
        module_name, func_name = view.rsplit('.', 1)
        view_module = import_module('lessweb_org.view.' + module_name)
        reload(pydom)
        reload(frames)
        reload(view_module)
        view_obj = getattr(view_module, func_name)(ret)
    else:
        view_obj = view(ret)

    if isinstance(view_obj, str):
        return view_obj
    else:
        return view_obj.dumps()
