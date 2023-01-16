class FactoryStateMethod:
    @staticmethod
    def factory_method(state_id):
        return lambda cls: cls.objects.get(pk=state_id)


def create_methods_from_attributes(cls):
    methods_to_create = []
    for cls_item in cls.__dict__:
        if 'STATE_' in cls_item:
            method_name = 'get_' + '_'.join(cls_item.lower().split('_')[1:])
            methods_to_create.append((method_name, cls.__dict__[cls_item]))

    for method_name, state_id in methods_to_create:
        method = FactoryStateMethod.factory_method(state_id)
        setattr(cls, method_name, classmethod(method))
    return cls