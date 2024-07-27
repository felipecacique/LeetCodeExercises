class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # https://leetcode.com/problems/unique-email-addresses/
        unique = set()
        for email in emails:
            email = email.split("@")
            local, domain = email[0], email[1]
            newLocal = ""
            for c in local:
                if c == ".": continue
                elif c == "+": break
                newLocal += c
            newEmail = newLocal + "@" + domain
            unique.add(newEmail)
        return len(unique)
            