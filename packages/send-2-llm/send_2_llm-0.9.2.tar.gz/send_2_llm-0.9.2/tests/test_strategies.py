from send_2_llm.trading.strategies.base import BaseStrategy
from send_2_llm.trading.strategies.strategy_one import StrategyOne
import pytest

def test_base_strategy():
    """Тестирование базового класса стратегии"""
    strategy = BaseStrategy()
    
    # Проверяем наличие необходимых методов
    assert hasattr(strategy, 'analyze')
    assert hasattr(strategy, 'execute')
    assert hasattr(strategy, 'validate')

def test_strategy_one():
    """Тестирование первой торговой стратегии"""
    strategy = StrategyOne()
    
    # Тестовые данные
    test_data = {
        'price': 100,
        'volume': 1000,
        'timestamp': '2024-03-20 10:00:00'
    }
    
    # Проверяем анализ данных
    result = strategy.analyze(test_data)
    assert isinstance(result, dict)
    assert 'signal' in result 