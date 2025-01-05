class BaseStrategy:
    """Базовый класс для всех торговых стратегий"""
    
    def analyze(self, data):
        """
        Анализ входных данных
        :param data: dict с данными для анализа
        :return: dict с результатами анализа
        """
        raise NotImplementedError
    
    def execute(self, signal):
        """
        Выполнение торговой операции
        :param signal: сигнал для выполнения
        :return: результат выполнения
        """
        raise NotImplementedError
    
    def validate(self, params):
        """
        Валидация параметров стратегии
        :param params: параметры для проверки
        :return: bool
        """
        raise NotImplementedError 