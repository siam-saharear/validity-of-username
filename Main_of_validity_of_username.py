current_users=["user_1","user_2","user_3","user_4","user_5","user_6"]
new_users=["person_1","person_2","user_1","user_5","person_3","person_4","person_5","person_6"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"sorry this user_name ('{new_user}') cant be resistered.")
    elif new_user.lower not in current_users:
        print(f"This user name ('{new_user}') is valid to be resistered.")
