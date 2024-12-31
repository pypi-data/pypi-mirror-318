# Lotion

Lotion is a wrapper of `notion-client`.

refs: [ramnes/notion-sdk-py: The official Notion API client library, but rewritten in Python! (sync + async)](https://github.com/ramnes/notion-sdk-py)

You can use Notion API easily using Lotion.

## Example

### By notion-client

```python
from notion_client import Client

client = Client(auth='NOTION_SECRET')
client.pages.create(
    parent={
      'type': 'database_id',
      'database_id': 'abcd1234-4e63-4a46-9ffe-36adeb59ab30'
    },
    properties={
      'Name': {
        'title': [
          {
            'type': 'text',
            'text': {
              'content': 'テスト'
            }
          }
        ]
      }
    },
)
```

### By lotion

```python
from lotion import Lotion

lotion = Lotion.get_instance()
created_page = lotion.create_page_in_database(
    database_id='abcd1234-4e63-4a46-9ffe-36adeb59ab30',
    properties=[
      Title.from_plain_text(name='Name', text='テスト')
    ]
)
```

## Use Original Prop and Database page.

### Available Class

- Checkbox
- Date
- Email
- MultiSelect
- Number
- PhoneNumber
- Relation
- Select
- Status
- Text
- Title
- Url
