def main():
    user1 = UserAccount("roma_sinitsyn", "roma@example.com", "начальныйПароль123")
    print(user1.get_user_info())
    
    print("\nПроверка пароля:")
    test_password = "начальныйПароль123"
    if user1.check_password(test_password):
        print(f"Пароль '{test_password}' верный")
    else:
        print(f"Пароль '{test_password}' неверный")
    
    wrong_password = "неправильныйПароль"
    if user1.check_password(wrong_password):
        print(f"Пароль '{wrong_password}' верный")
    else:
        print(f"Пароль '{wrong_password}' неверный")
    
    print("\nИзменение пароля:")
    user1.set_password("новыйБезопасныйПароль2024")
    
    print("\nПроверка нового пароля:")
    if user1.check_password("новыйБезопасныйПароль2024"):
        print("Новый пароль установлен успешно")
    
#ЗАДАНИЕ 2


if __name__ == "__main__":
    main()