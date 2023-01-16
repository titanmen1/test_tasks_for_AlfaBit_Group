class Foo:
    @classmethod
    def buy(cls, user, item_id):
        # Строчки 5, 6, 7 можно упросить
        product_qs = Product.objects.filter(item_id=item_id)
        if product_qs.exists():  # Если здесь будет False, то на строчке 10 будет ошибка, что нет переменной product
            product = product_qs[0]
        # Проверку продукта на доступность можно сделать в запросе. Глядя только на этот метод у нас нет ни какой доп
        # логики работы когда продукт не доступен. Его вовсе можно не получать из запроса
        if product.available:
            # Все что происходит ниже не обернуто в транзакции. На любой строчке может появится ошибка и часть данных
            # уже будет обновлена, а часть нет.
            # списание средств со счета пользователя
            user.withdraw(product.price)
            # Не знаю точно как эта функция реализована, но она должна быть фоновой задачей, например селери таск.
            # И запускать ее нужно в фоне
            # информация о купленном товаре
            send_email_to_user_of_buy_product(user)
            product.available = False
            product.buyer = user
            product.save()
            return True
        else:
            return False

class Bar:
    @classmethod
    def buy(cls, user: User, item_id: int) -> bool:
        # Сразу делаем запрос с нужным фильтром
        product = Product.objects.filter(item_id=item_id, available=True).first()
        if not product:
            return False
        # Если продукт есть, то все дальнейшие действия мы должны делать в транзакции. Если что то пойдет не так, то
        # все данные вернутся в исходное состояние. А также мы получил уведомление об ошибке в транзакции
        try:
            with transaction.atomic():
                # списание средств со счета пользователя
                user.withdraw(product.price)
                # Эту задачу запускаем в фоне
                # информация о купленном товаре
                send_email_to_user_of_buy_product.apply_async(user_id=user.pk)
                product.available = False
                product.buyer = user
                product.save()
                return True
        except IntegrityError:
            # Эта функция вернет эсепшен об ошибке интеграции
            handle_exception()
