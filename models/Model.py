class Model:
    # model title (can be same as table name)
    title = "Hotel"  # model title
    data = []  # loaded data from storage

    # sample
    # data = [
    #     {
    #         "id": 1,
    #         "title": "hotel Sabouri"
    #     },
    #     {
    #         "id": 1,
    #         "title": "hotel Sabouri"
    #     }
    # ]  # loaded data from storage

    pattern = {
        "main": [
            "id",
            "title"
        ],
        "properties": [
        ]
    }  # data structure

    def __init__(self, title):
        self.title = title
