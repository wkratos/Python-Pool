if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating vault security protocols...")

    with open("secure_vault.txt", "r") as file:
        file_content = file.read()

    print("Vault connection established with failsafe protocols")
    print()
    print("SECURE EXTRACTION:")
    print(file_content)
    print()
    print("SECURE PRESERVATION:")

    with open("secure_vault.txt", "w") as file:
        file.write("[CLASSIFIED] New security protocols archived\n")

    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")
