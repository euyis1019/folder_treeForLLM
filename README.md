# folder_tree

A Python package for printing folder directory trees.

## Features

- Supports ignoring hidden files and folders.
- Supports wildcard pattern exclusion of files or folders.
- Supports different output formats: string, JSON, XML.
- Optionally display file sizes.
- Customizable maximum recursion depth.

## Installation

```bash
git clone https://github.com/yourusername/folder_tree.git
cd folder_tree
pip install .
```

```python
# 设置排除列表和通配符模式
exclude = ['node_modules']
exclude_patterns = ['*.pyc', '__pycache__']

# 测试字符串输出
output_str = folder_tree.print_tree(
    path='.',
    max_depth=2,
    exclude=exclude,
    exclude_patterns=exclude_patterns,
    show_hidden=False,
    include_file_sizes=True,
    output_format='string'
)
print(output_str)

# 测试 JSON 输出
output_json = folder_tree.print_tree(
    path='',
    max_depth=1,
    exclude=exclude,
    exclude_patterns=exclude_patterns,
    show_hidden=False,
    include_file_sizes=True,
    output_format='json'
)
print(json.dumps(output_json, indent=4, ensure_ascii=False))

# 测试 XML 输出
output_xml = folder_tree.print_tree(
    path='',
    max_depth=1,
    exclude=exclude,
    exclude_patterns=exclude_patterns,
    show_hidden=False,
    include_file_sizes=True,
    output_format='xml'
)
root = ET.Element('root')
for elem in output_xml:
    root.append(elem)
tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
print('XML 输出已写入 output.xml 文件')
```
