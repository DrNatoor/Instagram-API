import json
from collections import OrderedDict

def changePassword(self, oldPassword, newPassword):
        """
        Change Password.

        :type oldPassword: str
        :param oldPassword: Old Password
        :type newPassword: str
        :param newPassword: New Password
        :rtype: object
        :return: Change Password Data
        """

        data = json.dumps(
            OrderedDict([
                ('_uuid', self.uuid),
                ('_uid', self.username_id),
                ('_csrftoken', self.token),
                ('old_password', oldPassword),
                ('new_password1', newPassword),
                ('new_password2', newPassword)
            ])
        )
        return self.http.request('accounts/change_password/', SignatureUtils.generateSignature(data))[1]
