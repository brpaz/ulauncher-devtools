""" Main Module """

import json
import logging

# pylint: disable=import-error
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

LOGGING = logging.getLogger(__name__)

CATEGORIES = [{
    'name': 'Linters',
    'code': 'linters',
    'icon': 'images/icon.png'
}, {
    'name': 'Editors',
    'code': 'editors',
    'icon': 'images/icon.png'
}, {
    'name': 'Markdown Tools',
    'code': 'mdtools',
    'icon': 'images/icon.png'
},
    {
    'name': 'Text manipulation',
    'code': 'text',
    'icon': 'images/icon.png'
},
    {
    'name': 'Presentations Tools',
    'code': 'presentations',
    'icon': 'images/icon.png'
},
    {
    'name': 'Design Tools',
    'code': 'design',
    'icon': 'images/icon.png'
},
    {
    'name': 'Date & Time',
    'code': 'datetime',
    'icon': 'images/icon.png'
},
    {
    'name': 'Security',
    'code': 'security',
    'icon': 'images/icon.png'
},
    {
    'name': 'Other',
    'code': 'other',
    'icon': 'images/icon.png'
}]

MENU = {
    'linters': [
        {
            'name': 'JSLint',
            'description': 'Online Javascript linter',
            'url': 'http://www.jslint.com/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'YAML Lint',
            'description': 'Online YAML Linter',
            'url': 'http://www.yamllint.com/',
            'icon': 'images/icon.png'
        }
    ],
    'mdtools': [
        {
            'name': 'Markdown Tables Generator',
            'description': 'Online Markdown tables generator',
            'url': 'http://www.tablesgenerator.com/markdown_tables',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Markdown TOC Generator',
            'description': 'Online Markdown TOC generator',
            'url': 'https://ecotrust-canada.github.io/markdown-toc/',
            'icon': 'images/icon.png'
        }
    ],
    'text': [
        {
            'name': 'Base64 Encode / Decode',
            'description': 'Encodes text as base64',
            'url': 'https://www.base64encode.org',
            'icon': 'images/icon.png'
        },
        {
            'name': 'URL Encode / Deocde',
            'description': '',
            'url': 'https://www.urlencoder.org/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'LoremIpsum Generator',
            'description': 'Generates lorem ipsum text',
            'url': 'https://loremipsum.io/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Unicode chatacter table',
            'description': '',
            'url': 'https://unicode-table.com/en/#control-character',
            'icon': 'images/icon.png'
        }
    ],
    'editors': [
        {
            'name': 'JSON Editor',
            'description': 'Simple JSON Editor',
            'url': 'https://jsonformatter.org/json-editor',
            'icon': 'images/icon.png'
        },
        {
            'name': 'StackEdit',
            'description': 'In-browser Markdown editor',
            'url': 'https://stackedit.io/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Repl',
            'description': 'Repl.it gives you an instant IDE to learn, build, collaborate, and host all in one place.',
            'url': 'https://repl.it/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'CodeSandbox',
            'description': 'The online code editor for Web',
            'url': 'https://codesandbox.io/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'JSON Schema Converter',
            'description': 'Converts a JSON object into a JSON schema specification',
            'url': 'https://www.jsonschema.net/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Regex101',
            'description': 'Regular expressions editor',
            'url': 'https://regex101.com/',
            'icon': 'images/icon.png'
        }
    ],
    'presentations': [
        {
            'name': 'Carbon',
            'description': 'Create and share beautiful images of your source code.',
            'url': 'https://carbon.now.sh',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Slides.com',
            'description': 'Slides is a place for creating, presenting and sharing slide decks.',
            'url': 'https://slides.com/',
            'icon': 'images/icon.png'
        }
    ],
    'design': [
        {
            'name': 'Draw.io',
            'description': 'Create diagrams',
            'url': 'https://www.draw.io/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Figma',
            'description': 'Design tool',
            'url': 'https://www.figma.com/',
            'icon': 'images/icon.png'
        }
    ],
    'datetime': [
        {
            'name': 'Time.is',
            'description': 'What is the current time',
            'url': 'https://time.is/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Timezone converter',
            'description': 'Converts dates between timezones',
            'url': 'http://www.thetimezoneconverter.com/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Epoch Converter',
            'description': 'Epoch converter',
            'url': 'https://www.epochconverter.com/',
            'icon': 'images/icon.png'
        }
    ],
    'security': [
        {
            'name': 'Pwdgen',
            'description': 'Strong password generator',
            'url': 'https://www.pwdgen.org/',
            'icon': 'images/icon.png'
        }
    ],
    'other': [
        {
            'name': 'Placeholder.com',
            'description': 'Generate placeholder images',
            'icon': 'images/icon.png',
            'url': 'https://placeholder.com/'
        },
        {
            'name': 'Fake Identity generator',
            'description': 'Fake Identity generator',
            'url': 'https://www.fakenamegenerator.com/',
            'icon': 'images/icon.png'
        },
        {
            'name': 'Crontab generator',
            'description': 'Crontab generator',
            'url': 'https://crontab-generator.org/',
            'icon': 'images/icon.png'
        }
    ]
}


class DevToolsExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(DevToolsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def show_categories_menu(self, kw, filter_q):
        """ Shows the Tools category menu """
        items = []

        for category in CATEGORIES:

            if filter_q and filter_q.lower() not in category['name'].lower():
                continue

            items.append(ExtensionSmallResultItem(icon=category['icon'],
                                                  name=category['name'],
                                                  on_enter=SetUserQueryAction('%s %s > ' % (kw, category['code']))))
        return RenderResultListAction(items)

    def show_tools_by_category(self, category, query):
        """ Show tools by the selected category """

        tools = MENU[category]

        if query:
            tools = [p for p in tools if query.strip().lower()
                     in p['name'].lower()]

        if not tools:
            return RenderResultListAction([ExtensionSmallResultItem(icon='images/icon.png',
                                                                    name='No tool found for the specified filter',
                                                                    highlightable=False,
                                                                    on_enter=HideWindowAction())])
        items = []
        for tool in tools:
            items.append(ExtensionSmallResultItem(icon=tool['icon'],
                                                  name=tool['name'],
                                                  on_enter=OpenUrlAction(tool['url'])))

        return RenderResultListAction(items)


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument() or ""
        query_parts = query.split('>')

        if not query or len(query_parts) < 2:
            return extension.show_categories_menu(event.get_keyword(), query)

        selected_category = query_parts[0].strip()
        search_term = query_parts[1] or ""

        return extension.show_tools_by_category(selected_category, search_term)


if __name__ == '__main__':
    DevToolsExtension().run()
