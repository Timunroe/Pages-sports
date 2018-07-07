config = {
    "project_name": "pages_sports",
    "db_name": "db.json",
    "db_fields_dflt": {
        'desc': '',
        'draft': 0,  # int 0:published, 1-2: draft
        'rank': 0, # int
        'rank_time': 0, # int
        'label': '',
        'title': '',
        'categories': [], # list of strings
        'sections': [], # list of strings
        'tags': [], # list of strings
    },
    "apis": {
        "filter": ["searchResultView"],
        "feed" : [
            'http://api.zuza.com/search/article/default?&category=sports&pageIndex=1&location=hamilton&sort=datedesc&pageSize=30&startindex=1&endindex=30',
            # 'http://api.zuza.com/search/article/default?guid=346a9bb4-5f2b-4838-b632-4abcc516eeca&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            # 'http://api.zuza.com/search/article/default?guid=ad33da77-38f2-42fc-ba36-392490bee98b&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            # 'http://api.zuza.com/search/article/default?guid=49255a54-3476-496a-8a42-abfd94a67feb&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            # 'http://api.zuza.com/search/article/default?guid=ab2cef44-1fd3-4380-a6ee-f695f4e0d4e5&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
        ],
        "football": [
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=football&pageIndex=1&location=hamilton&sort=datedesc&pageSize=20&startindex=1&endindex=20',
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=ticats&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
            'http://api.zuza.com/search/article/default?guid=346a9bb4-5f2b-4838-b632-4abcc516eeca&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            'http://api.zuza.com/search/article/default?guid=ad33da77-38f2-42fc-ba36-392490bee98b&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
        ],
        "hockey": ['http://api.zuza.com/search/article/default?&category=sports&subcategory=hockey&pageIndex=1&location=hamilton&sort=datedesc&pageSize=20&startindex=1&endindex=20'],
        "baseball": ['http://api.zuza.com/search/article/default?&category=sports&subcategory=baseball&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10'],
        "soccer": [
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=soccer&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=world-cup&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10'
        ],
        "basketball": ['http://api.zuza.com/search/article/default?&category=sports&subcategory=soccer&pageIndex=1&location=hamilton&sort=datedesc&pageSize=20&startindex=1&endindex=20'],
        "golf": ['http://api.zuza.com/search/article/default?&category=sports&subcategory=golf&pageIndex=1&location=hamilton&sort=datedesc&pageSize=20&startindex=1&endindex=20'],
    },
    

}