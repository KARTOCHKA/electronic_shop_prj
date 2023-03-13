class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        """Исключение, если отсутствует одна из колонок данных"""
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message
