#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import bd_common
from . import bd_address

from .. import store


class BDStore(store.EStore, bd_common.BDCommon):

    @classmethod
    def wrap(cls, models, build=True, handler=None, **kwargs):
        def handler(model):
            address = model.get("address", {})
            model.update(
                address=bd_address.BDAddress.wrap(address) if address else None
            )

        return super(BDStore, cls).wrap(models, build=build, handler=handler, **kwargs)
