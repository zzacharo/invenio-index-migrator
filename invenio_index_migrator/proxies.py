# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Index sync proxies."""

from flask import current_app
from werkzeug.local import LocalProxy

current_index_migrator = LocalProxy(
    lambda: current_app.extensions['invenio-index-migrator'])
