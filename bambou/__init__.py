# -*- coding: utf-8 -*-
"""
Copyright (c) 2011-2012 Alcatel, Alcatel-Lucent, Inc. All Rights Reserved.

This source code contains confidential information which is proprietary to Alcatel.
No part of its contents may be used, copied, disclosed or conveyed to any party
in any manner whatsoever without prior written permission from Alcatel.

Alcatel-Lucent is a trademark of Alcatel-Lucent, Inc.
"""

import logging

bambou_logger = logging.getLogger('bambou')

try:
    # NullHandler is only available for python >= 2.7
    bambou_logger.addHandler(logging.NullHandler())
except:
    pass

__all__ = ['NURESTBasicUser', 'NURESTConnection', 'NURESTModelController', 'NURESTFetcher', 'NURESTLoginController', 'NURESTObject', 'NURESTPushCenter', 'NURESTRequest', 'NURESTResponse']

from bambou.nurest_user import NURESTBasicUser
from bambou.nurest_connection import NURESTConnection
from bambou.nurest_fetcher import NURESTFetcher
from bambou.nurest_login_controller import NURESTLoginController
from bambou.nurest_object import NURESTObject
from bambou.nurest_push_center import NURESTPushCenter
from bambou.nurest_request import NURESTRequest
from bambou.nurest_response import NURESTResponse
from bambou.nurest_modelcontroller import NURESTModelController