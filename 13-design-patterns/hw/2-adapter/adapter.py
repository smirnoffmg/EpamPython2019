"""
Класс StoreService - очень упрощенный арихв XML-документов, который умеет сохранять документ и возвращать его.
    (и в котором могло бы быть реализовано больше функций, например, поиск документов по тексту, проверка на попытку
    загрузить один и тот же файл дважды и т.д.)
Сервис предоставляет определенный интерфейс, который мы знаем, но не можем изменить.
Класс StoreService нельзя изменять.

Класс DocumentsHandler - выполняющая роль выгрузки и загрузки документов часть нашего гипотетически огромного
    приложения App. Другими словами, это клиент, который содержит существующую бизнес-логику программы.
Класс DocumentsHandler нельзя изменять.

Далее идет клиентский код, в котором реализована логика загрузки документов в сервис-архив и выгрузка этих же
    документов из сервиса. Клиентский код изменять нельзя.

Ранее сервис работал с документами в формате XML, но недавно он изменился и стал работать с JSON-документами,
    что вызвало ряд неполадок в нашем приложении. Необходимо написать класс-адаптер, который перед отработкой
    текущей бизнес-логики (загрузка документов) сконвертирует XML-документы в JSON-документы.

Примечание: Действительно конвертировать XML в JSON не нужно. Будет достаточно изменить расширение документа.
"""

import uuid
import os


class StoreService:
    stored_documents = {}

    def store_document(self, document):
        if document.endswith('.json'):
            document_id = uuid.uuid4()
            self.stored_documents[document_id] = document
            return {
                'status': 'success',
                'document_id': document_id
            }
        else:
            return {
                'status': 'error',
                'msg': 'Now we store only JSON documents. Sorry :(',
            }

    def get_document(self, document_id):
        if document_id in self.stored_documents:
            return {
                'status': 'success',
                'document': self.stored_documents[document_id]
            }
        return {
            'status': 'error',
            'msg': f'Document with {document_id} ID is not found.',
        }


class DocumentsHandler:
    _service = None
    _document_ids = []

    def __init__(self, service):
        self._service = service

    def upload_documents(self, documents):
        """
            Метод принимающий на вход 1 или более документов для отгрузки в сервис-архив.
            Возвращает список идентификаторов загруженных документов.
        """
        if not isinstance(documents, list):
            documents = [documents]

        stored_documents = []

        for document in documents:
            result = self._service.store_document(document)
            if result['status'] == 'success':
                stored_documents.append(result['document_id'])
            if result['status'] == 'error':
                print("Couldn't upload document {}: {}".format(document, result['msg']))

        self._document_ids.extend(stored_documents)

        return stored_documents

    def get_documents(self, document_ids):
        """
             Метод принимающий на вход 1 или более идентификаторов документа для их загрузки из сервиса-архива.
             Возвращает список выгруженных документов.
        """
        if not isinstance(document_ids, list):
            document_ids = [document_ids]

        loaded_documents = []

        for doc_id in document_ids:
            result = self._service.get_document(doc_id)
            if result['status'] == 'success':
                loaded_documents.append(result['document'])
            if result['status'] == 'error':
                print("Couldn't load document with {} ID: {}".format(doc_id, result['msg']))

        return loaded_documents


def client_code(documents_handler):
    xml_files_to_upload = os.listdir(os.path.dirname(__file__) + '/documents')

    document_ids = documents_handler.upload_documents(xml_files_to_upload)
    print(document_ids)
    print(documents_handler.get_documents(document_ids[1]))


if __name__ == "__main__":
    class App:
        pass  # Упрощенная реализация сложного приложения

    app = App()
    app.documents_handler = DocumentsHandler(StoreService())
    # Реализуйте класс Adapter и раскомментируйте строку ниже
    # app.documents_handler = Adapter(app.documents_handler)
    client_code(app.documents_handler)
