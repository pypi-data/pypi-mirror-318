.. SPDX-FileCopyrightText: Copyright © 2023 Idiap Research Institute <contact@idiap.ch>
..
.. SPDX-License-Identifier: GPL-3.0-or-later

.. _credible.install:

==============
 Installation
==============

Installation may follow one of two paths: deployment or development. Choose the
relevant tab for details on each of those installation paths.


.. tab:: Deployment (pip/uv)

   Install using pip_, or your preferred Python project management solution (e.g.
   uv_, rye_ or poetry_).

   **Stable** release, from PyPI:

   .. code:: sh

      pip install credible

   **Latest** development branch, from its git repository:

   .. code:: sh

      pip install git+https://gitlab.idiap.ch/medai/software/credible@main


.. tab:: Deployment (pixi)

   Use pixi_ to add this package as a dependence:

   .. code:: sh

      pixi add credible


.. tab:: Development

   Checkout the repository, and then use pixi_ to setup a full development
   environment:

   .. code:: sh

      git clone git@gitlab.idiap.ch:medai/software/credible
      pixi install --frozen

   .. tip::

      The ``--frozen`` flag will ensure that the latest lock-file available
      with sources is used.  If you'd like to update the lock-file to the
      latest set of compatible dependencies, remove that option.

      If you use `direnv to setup your pixi environment
      <https://pixi.sh/latest/features/environment/#using-pixi-with-direnv>`_
      when you enter the directory containing this package, you can use a
      ``.envrc`` file similar to this:

      .. code:: sh

         watch_file pixi.lock
         export PIXI_FROZEN="true"
         eval "$(pixi shell-hook)"


.. include:: links.rst
