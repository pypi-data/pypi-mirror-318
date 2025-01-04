#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base


class EMBWay(base.EBase):

    phone = appier.field()

    @classmethod
    def validate(cls):
        return super(EMBWay, cls).validate() + [
            appier.not_null("phone"),
            appier.not_empty("phone"),
        ]

    @classmethod
    def payment_types(cls):
        return ("mbway",)
