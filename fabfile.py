# pylint: disable-msg=W0401,W0614
"""
Deployment automation.
"""
from rdcore.deployment.automation import *

# Project description
env.project_name = 'debugging cake portal'
# env.svn_url_template = 'https://serv-sources.jouve-hdi.com/jouve/bpo_geodis/{project_name}'
env.git_url_template = 'https://git.jouve-hdi.com/luminess-dev-experiments/debugging_cake_portal.git'
env.project_dir_template = '/home/projet/{project_name}/{project_name}'
# Build variables
env.build_python_version = "3.8"
env.build_variant = "focal"
env.build_host = "localhost"
# to choose only one host, set 'build_variant' variable, eg. fab --set build_variant=centos6 snapshot
# uncomment the following lines to enable multiple plateform build
# env.build_variant = "centos7"
# env.build_variants = {'centos7': {'roles': {'build': ['ind-may1-drel03.dev.mayenne.l121'],}, 'extras': '' },
#                      'centos6': {'roles': {'build': ['ind-may1-drel02.dev.mayenne.l121'],}, 'extras': '' },
#                      'centos5': {'roles': {'build': ['ind-may1-drel01.dev.mayenne.l121'],}, 'extras': '' },}
compute_roledefs()
# Deploy variables
# use ind-may1-dint01 as staging environnement
env.roledefs['staging'] = ['0.0.0.0']
env.roledefs['prod'] = ['0.0.0.0']
env.upload_with_setuptools = True


def get_install_options():
    """Get install.py options.

    Set option --use-previous-answers if the Fabric env var
    all-install-questions is not set.
    """
    install_options = '--compare-process '
    if not env.get('all-install-questions'):
        install_options += '--use-previous-answers '
    return install_options


# Override the default install.get_install_options function
install.get_install_options = get_install_options