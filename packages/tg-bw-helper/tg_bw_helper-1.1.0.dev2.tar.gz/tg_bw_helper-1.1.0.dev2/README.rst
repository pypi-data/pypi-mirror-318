==============================
Ansible Vault Bitwarden Helper
==============================

    CLI command that connects two awesome tools together - Ansible Vault & Bitwarden Password Manager

.. image:: https://gitlab.com/thorgate-public/tg-bw-helper/badges/master/pipeline.svg
   :height: 20px

.. image:: https://gitlab.com/thorgate-public/tg-bw-helper/badges/master/coverage.svg
   :height: 20px

----

.. image:: https://asciinema.org/a/d8zWlTHhrtXYi8KhAvresaHK8.svg
   :target: https://asciinema.org/a/d8zWlTHhrtXYi8KhAvresaHK8
   :align: center

----

.. contents:: Table of Contents
   :depth: 2

####
Why?
####

At Thorgate, we deploy project using Ansible. Ansible comes with awesome encrypted storage, and every storage needs it's own password to access it contents.

We also using Bitwarden to store company-wide passwords and sensitive information. And if we already are storing passwords to Ansible Vault's in Bitwarden, we thought why not use Bitwarden CLI tool to pass these passwords directly to Ansible Vault?

And that's how this project was born 😎

###############
Getting Started
###############

*************
Prerequisites
*************

We need these tools to be installed:

* Python 3.9+ & Pip
* `Ansible <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW#installing-ansible>`_
* Ansible project that uses `Ansible Vault <https://docs.ansible.com/ansible/latest/cli/ansible-vault.html>`_
* `Bitwarden Account <https://bitwarden.com>`_
* `Bitwarden CLI <https://bitwarden.com/help/article/cli/#download-and-install>`_

We strongly recommend installing Python packages in dedicated and isolated virtual environments. There are several tools that helps manage virtual environments:

* `Virtualenv <https://docs.python.org/3/library/venv.html#module-venv>`_
* `Pipenv <https://pipenv.pypa.io/en/latest/#install-pipenv-today>`_
* `Poetry <https://python-poetry.org/docs/#installation>`_ (We will be using this one)

************
Installation
************

We assume several things:

* That you have existing or starting new Ansible project
* That your Ansible installation lives in virtual environment

Based on these assumptions, for installation you need to add this package into your virtual environment. For example you might run ``$ poetry add tg-bw-helper``

***********************
Setting Up With Ansible
***********************

1. Create if not yet existing shell script with this example content (it can be named ``ask-vault-pass.sh``) - note that you do not need to add ``poetry run`` before invoking ``bw_helper`` here, or activate virtualenv etc., since your ansible will be already running in correct environment

   .. code-block:: bash

      #!/bin/sh
      bw_helper --vault-item "Ansible Vault" --vault-item-field "Password"

2. Make sure that this script is executable! If not, run ``$ sudo chmod +x ask-vault-pass.sh``
3. Edit ``ansible.cfg`` to specify script that Ansible will be using to get Vault password

   .. code-block:: ini

      [defaults]
      vault_password_file=./ask-vault-pass.sh

#####
Usage
#####

Now when all these steps completed:

* ``tg-bw-helper`` is installed into virtual environment where Ansible is installed
* Ansible project is configured to use special script

We are ready to use the tool:

1. Run ``$ bw login`` (Needs to be run once per user session)
2. Run your usual Ansible playbook that previously asked for Vault password
3. Enter Bitwarden master password

###########
CLI Options
###########

--bw-executable      Optional, should point to bw executable, defaults to /usr/bin/bw, can also be set with ``TG_BW_AP_EXECUTABLE_PATH`` env variable
--fallback-prompt    optional, prompt to display if bw fails, defaults to "Vault password: ", can also be set with ``TG_BW_AP_FALLBACK_PROMPT`` env variable
--vault-item      vault item ID or name, should be specific since tool will fail if multiple items are found

      * **Item name** is what you see as it's name in bitwarden UI
      * **Item ID** is useful if you have two items with same name, you can learn it by using bitwarden CLI (use ``bw login`` to login, follow the instructions for how to pass the session information over to the next command, and then use ``bw list items --search <item name>``. You will get json array of matching objects, each object will have ID that you can use.)
--vault-item-field      optional, field to use on the item. If not specified, password is used. Examples:

      * You have an item "Awesome project ansible vault" with password "123", and you want to use "123". You do not specify ``--valut-item-field`` in this case.
      * You have an item "Ansible secrets" with password set to "abc", that has additional fields "Test server ansible" set to "123" and "Live server ansible" set to "456", and you want to use "123". You specify ``--valut-item-field="Test server ansible"`` in this case.

############
Environment
############
If **BW_SESSION** is set in environment, it will be used instead of asking bitwarden master password
to unlock bitwarden.

If using linux, you can opt to save the bitwarden session in linux kernel secret storage by
setting **TG_BW_SESSION_SECRET_NAME** environment variable to to some string (preferably random)
that will be used to store the secret on user's session keyring.

############
Contributing
############

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

**********
Developing
**********

For local development project repository contains ``pyproject.toml`` and ``poetry.lock``. When using them with `Poetry <https://python-poetry.org/docs/#installation>`_ you will be able to recreate ready to use environment.

We also added ``Makefile`` that contains lots of useful commands to help setup the project, run tests and lint code. Do check it out by running ``make``

**********
Opening MR
**********

1. Clone the Project
2. Create your Feature Branch (``git checkout -b feature/AmazingFeature``)
3. Commit your Changes (``git commit -m 'Add some AmazingFeature'``)
4. Push to the Branch (``git push origin feature/AmazingFeature``)
5. Open a Merge Request

#######
License
#######

Distributed under the MIT License. See LICENSE for more information.
