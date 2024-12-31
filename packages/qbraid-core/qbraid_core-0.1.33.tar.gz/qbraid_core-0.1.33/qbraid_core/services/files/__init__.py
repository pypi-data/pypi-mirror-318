# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module providing client for interacting with the qBraid file management service.

.. currentmodule:: qbraid_core.services.files

Classes
--------

.. autosummary::
   :toctree: ../stubs/

   FileManagerClient

Exceptions
------------

.. autosummary::
   :toctree: ../stubs/

   FileManagementServiceRequestError

"""
from .client import FileManagerClient
from .exceptions import FileManagementServiceRequestError

__all__ = ["FileManagerClient", "FileManagementServiceRequestError"]
