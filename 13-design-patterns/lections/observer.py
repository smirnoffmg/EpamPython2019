"""
Observer (Наблюдатель)

Определяет зависимость типа один ко многим между объектами таким образом, что при изменении состояния одного объекта
  все зависящие от него оповещаются об этом событии.

При реализации шаблона «наблюдатель» обычно используются следующие классы:
  Observable — интерфейс, определяющий методы для добавления, удаления и оповещения наблюдателей;
  Observer — интерфейс, с помощью которого наблюдатель получает оповещение;
  ConcreteObservable — конкретный класс, который реализует интерфейс Observable;
  ConcreteObserver — конкретный класс, который реализует интерфейс Observer.

Шаблон «наблюдатель» применяется в тех случаях, когда система обладает следующими свойствами:
  * существует, как минимум, один объект, рассылающий сообщения;
  * имеется не менее одного получателя сообщений, причём их количество и состав могут изменяться
    во время работы приложения;
  * нет надобности очень сильно связывать взаимодействующие объекты, что полезно для повторного использования.

Данный шаблон часто применяют в ситуациях, в которых отправителя сообщений не интересует,
  что делают получатели с предоставленной им информацией.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Абстрактный наблюдатель
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Получение нового сообщения
        """
        pass


class Observable(ABC):
    """
    Абстрактный наблюдаемый
    """

    def __init__(self) -> None:
        self.observers = list()  # инициализация списка наблюдателей

    def subscribe(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message: str) -> None:
        """
        Передача сообщения всем наблюдателям, подписанным на события
        данного объекта наблюдаемого класса
        """
        for observer in self.observers:
            observer.update(message)


class Newspaper(Observable):
    """
    Газета, за новостями которой следят тысячи людей
    """

    def add_news(self, news: str) -> None:
        """
        Выпуск очередной новости
        """
        self.notify_observers(news)


class Citizen(Observer):
    """
    Гражданин, который любит читать газету
    """

    def __init__(self, name: str) -> None:
        """
        Constructor.

        :param name: имя гражданина, чтобы не спутать его с кем-то другим
        """
        self.name = name

    def update(self, message: str) -> None:
        """
        Получение очередной новости
        """
        print(f'{self.name} узнал следующее: {message}')


if __name__ == '__main__':
    newspaper = Newspaper()  # Создаем газету

    # Добавляем двух человек
    ivan = Citizen('Иван')
    maria = Citizen('Мария')

    # Оформим подписку на газету
    newspaper.subscribe(ivan)
    newspaper.subscribe(maria)

    # Вбрасываем газетную утку
    newspaper.add_news('Пришельцы прилетели на Землю и посеяли пшеницу')

    # Один гражданин решил отписаться от таких новостей
    newspaper.unsubscribe(maria)

    # Выпустим опровержение
    newspaper.add_news('Опровержение! Пришельцев не было, пшеница сама выросла')
