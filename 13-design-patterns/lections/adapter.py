class Client:
    """
    Целевой класс объявляет интерфейс, с которым может работать код пользователей.
    """

    def request(self):
        return "Client: The default client's behavior."


class Service:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим пользовательским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем пользовательский код сможет его использовать.
    """

    def specific_request(self):
        return ".ecivreS eht fo roivaheb laicepS"


class Adapter(Client):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом.
    """

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def user_code(client):
    """
    Пользовательский код поддерживает все классы, использующие интерфейс Client.
    """

    print(client.request())


if __name__ == "__main__":
    print("User: I can work just fine with the Client objects:")
    client = Client()
    user_code(client)
    print('-' * 50)

    service = Service()
    print("User: The Service class has a weird interface. See, I don't understand it:")
    print(f"Service: {service.specific_request()}")
    print('-' * 50)

    print("User: But I can work with it via the Adapter:")
    adapter = Adapter(service)
    user_code(adapter)
