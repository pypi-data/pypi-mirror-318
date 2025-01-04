#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Easypay API
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Easypay API.
#
# Hive Easypay API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Easypay API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Easypay API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import unittest

import easypay


class BaseTest(unittest.TestCase):

    def test_shelve(self):
        api = easypay.ShelveAPI(username="username", cin="1111", entity="11111")

        data = dict(
            ep_cin="1111",
            ep_user="username",
            ep_entity="11111",
            ep_reference="111111111",
            ep_value="10.00",
            t_key="key",
        )

        reference = api.gen_reference(data)

        self.assertEqual(reference["status"], "pending")
        self.assertEqual(reference["username"], "username")
        self.assertEqual(reference["entity"], "11111")
        self.assertEqual(reference["reference"], "111111111")
        self.assertEqual(reference["value"], "10.00")
        self.assertEqual(reference["identifier"], "key")
        self.assertEqual(reference["warning"], None)
        self.assertEqual(reference["cancel"], None)

        reference = api.get_reference("key")

        self.assertEqual(reference["status"], "pending")
        self.assertEqual(reference["username"], "username")
        self.assertEqual(reference["entity"], "11111")
        self.assertEqual(reference["reference"], "111111111")
        self.assertEqual(reference["value"], "10.00")
        self.assertEqual(reference["identifier"], "key")
        self.assertEqual(reference["warning"], None)
        self.assertEqual(reference["cancel"], None)

        api.del_reference("key")
        reference = api.get_reference("key")

        self.assertEqual(reference, None)

        reference = api.gen_reference(data)
        doc = api.gen_doc("doc", "key")

        self.assertEqual(doc["identifier"], "doc")
        self.assertEqual(doc["key"], "key")
        self.assertEqual(doc["username"], "username")
        self.assertEqual(doc["cin"], "1111")

        doc = api.get_doc("doc")

        self.assertEqual(doc["identifier"], "doc")
        self.assertEqual(doc["key"], "key")
        self.assertEqual(doc["username"], "username")
        self.assertEqual(doc["cin"], "1111")

        api.del_doc("doc")
        doc = api.get_doc("doc")

        self.assertEqual(doc, None)

    def test_shelve_v2(self):
        api = easypay.ShelveAPIv2(account_id="account_id", account_key="account_key")

        data = dict(
            method="mb",
            identifier="identifier",
            key="key",
            amount="10.00",
            currency="EUR",
            warning=True,
            cancel=True,
        )

        api.set_payment(data)

        payment = api.get_payment("identifier")

        self.assertEqual(payment["identifier"], "identifier")
        self.assertEqual(payment["key"], "key")
        self.assertEqual(payment["amount"], "10.00")
        self.assertEqual(payment["currency"], "EUR")
        self.assertEqual(payment["warning"], True)
        self.assertEqual(payment["cancel"], True)

        api.del_payment("identifier")
        payment = api.get_payment("identifier")

        self.assertEqual(payment, None)
