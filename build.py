#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.flake8")
# On utilise pytest pour l'exécution des tests
use_plugin("pypi:pybuilder_pytest")
# Pour l'installation de nouvelles dépendances
use_plugin('python.install_dependencies')


name = "banque-portail-functests"
version = "1.0.0"
description = "Tests fonctionnels Selenium pour la portail bancaire"

default_task = [ "install_dependencies", "run_unit_tests" ]


@init
def set_properties(project):
    project.set_property('dir_source_pytest_python', 'src/functest/python')
    # Ajout de dépendances de projet nécessite le plugin 'python.install_dependencies'
    project.depends_on('selenium')
    project.depends_on('webdrivermanager')
