#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base


class EStore(base.EBase):

    name = appier.field()

    address = appier.field(type=appier.reference("EAddress", name="id"))
