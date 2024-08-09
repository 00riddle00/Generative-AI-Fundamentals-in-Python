import re

email_list = [
    "test@example-com",
    "firstlast@examplecom",
    "test.one@@example.com",
    "secondtest@ex#ample.com",
    "john.doe@example.com",
    "third.testexample.com",
    "sample_email@examplecom",
    "user1234@example.com",
    "alice.bob@ex&ample.com",
    "last.first@example.com",
    "randomuserexample.com",
    "test_two@exam*ple.com",
    "demo.user@example.com",
    "testthreeexample.com",
    "example_user@examplecom",
    "sample.test@example.com",
    "user.test@examp$le.com",
    "test.four @example.com",
    "fifth.test@exa!mple.com",
    "anotheruser@example.com",
]

pattern = r"@example\.com"

verified_emails = []

for email in email_list:
    if re.search(pattern, email):
        verified_emails.append(email)

print(verified_emails)
