def rule_no_harm(prompt):
    return "kill" not in prompt.lower()

def rule_no_abuse(prompt):
    return "abuse" not in prompt.lower()

GLOBAL_ETHICS = [
    rule_no_harm,
    rule_no_abuse
]
