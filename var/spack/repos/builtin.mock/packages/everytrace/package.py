##############################################################################
# Copyright (c) 2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

def check(condition, msg):
    """Raise an install error if condition is False."""
    if not condition:
        raise InstallError(msg)

class Everytrace(CMakePackage):
    """Get stack trace EVERY time a program exits."""

    homepage = "https://github.com/citibeth/everytrace"
    url = "https://github.com/citibeth/everytrace/tarball/0.2.0"

    version('0.2.0', '2af0e5b6255064d5191accebaa70d222')
    version('develop',
            git='https://github.com/citibeth/everytrace.git', branch='develop')

    variant('mpi', default=False, description='Enables MPI parallelism')
    variant('fortran', default=False,
            description='Enable use with Fortran programs')

    depends_on('mpi', when='+mpi')

    def cmake_args(self):
        spec = self.spec
        return [
            '-DUSE_MPI=%s' % ('YES' if '+mpi' in spec else 'NO'),
            '-DUSE_FORTRAN=%s' % ('YES' if '+fortran' in spec else 'NO')]

    def setup_environment(self, spack_env, env):
        env.prepend_path('PATH', join_path(self.prefix, 'bin'))
