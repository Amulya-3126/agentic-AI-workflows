def observe():
    temperature = int(input("Enter temperature: "))
    return temperature


def decide(temperature):
    if temperature > 100:
        return "COOL"
    else:
        return "NORMAL"


def act(action):
    if action == "COOL":
        print("Action: Turning ON the cooling system.")
    else:
        print("Action: Temperature is normal. No action needed.")


# Agentic Loop
while True:
    # 1. Observe
    temperature = observe()

    # 2. Decide
    action = decide(temperature)

    # 3. Act
    act(action)

    # Repeat or stop
    choice = input("Continue? (yes/no): ")

    if choice.lower() == "no":
        print("Agent stopped.")
        break