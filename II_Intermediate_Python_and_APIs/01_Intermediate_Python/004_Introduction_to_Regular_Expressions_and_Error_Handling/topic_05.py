import re

email_list = [
    "test@example-com",
    "firstlast@examplecom",
    "test.one@@example.com",
    "secondtest@ex#ample.com",
    "john.doe@example.org",
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
    "sample.test@example.org",
    "user.test@examp$le.org",
    "test.four @example.com",
    "fifth.test@exa!mple.com",
    "anotheruser@example.net",
]

verified_email_count = 0

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"

for email in email_list:
    if re.search(pattern, email):
        verified_email_count += 1
        print(email)

print(verified_email_count)
