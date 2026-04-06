tree = {
    'name': '/',
    'meta': {},
    'type': 'directory',
    'children': [
        {
            'name': 'eTc',
            'meta': {},
            'type': 'directory',
            'children': [
                {
                    'name': 'NgiNx',
                    'meta': {'size': 4000},
                    'type': 'directory',
                    'children': [],
                },
                {
                    'name': 'CONSUL',
                    'meta': {},
                    'type': 'directory',
                    'children': [
                        {
                            'name': 'config.json',
                            'type': 'file',
                        },
                    ],
                },
            ],
        },
        {'name': 'hosts', 'type': 'file', 'meta': {}},
    ],
}

# эта функция изменяет исходные данные так как в задании ничего не указано дополнительно
def renameFilesToUpper(initial_tree):
    def walk(current_node):
        if current_node['type'] == 'file':
            current_node['name'] = current_node['name'].upper()
        
        elif current_node['type'] == 'directory':
            for child in current_node.get('children', []):
                walk(child)

    walk(initial_tree)
    return initial_tree

new_tree = renameFilesToUpper(tree)
print(new_tree)