# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

from remotesystem import RemoteSystem

from common.environment import Environment


class Git:
    def __init__(self, connection=RemoteSystem()):
        self.connection = connection

    def get_stable_branch_name(self) -> str:
        """Returns the stable branch name that the given branch name is branches of from.

        Returns
        -------
        # Returns git branch used within Jenkins
        """

        jenkins_git_branch = ""
        if Environment(self.connection).get_remote_environment_variable("GIT_BRANCH"):
            jenkins_git_branch = Environment(self.connection).get_remote_environment_variable("GIT_BRANCH").lower()
        if jenkins_git_branch.startswith(r"maint/"):
            return r"maint/stable"
        elif jenkins_git_branch.startswith(r"feat/"):
            return r"feat/stable"
        return "Unknown"
