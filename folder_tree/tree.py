# folder_tree/tree.py

import os
import fnmatch
import json
import xml.etree.ElementTree as ET

def print_tree(
    path='.',
    depth=0,
    max_depth=2,
    exclude=None,
    exclude_patterns=None,
    show_hidden=False,
    include_file_sizes=False,
    indent='    ',
    prefix='|-- ',
    output_format='string',
):
    """
    打印文件夹目录树。

    参数：
    - path (str): 起始路径。
    - depth (int): 当前递归深度。
    - max_depth (int): 最大递归深度。
    - exclude (list): 需要排除的文件或文件夹名称列表。
    - exclude_patterns (list): 需要排除的文件或文件夹的通配符模式列表。
    - show_hidden (bool): 是否显示隐藏文件和文件夹。
    - include_file_sizes (bool): 是否显示文件大小。
    - indent (str): 缩进符号。
    - prefix (str): 前缀符号。
    - output_format (str): 输出格式，'string'、'json' 或 'xml'。

    返回：
    - str 或 list 或 xml.etree.ElementTree.Element: 文件夹树的表示。
    """
    if exclude is None:
        exclude = []
    if exclude_patterns is None:
        exclude_patterns = []

    if depth > max_depth:
        if output_format == 'string':
            return ''
        elif output_format == 'json':
            return []
        elif output_format == 'xml':
            return []

    tree_str = ''
    tree_json = []
    tree_xml = []

    try:
        items = os.listdir(path)
    except PermissionError:
        error_msg = indent * depth + prefix + '[权限不足]\n'
        if output_format == 'string':
            return error_msg
        elif output_format == 'json':
            return [{'name': '[权限不足]', 'type': 'error', 'children': []}]
        elif output_format == 'xml':
            error_element = ET.Element('error', name='[权限不足]')
            return [error_element]

    # 排序，先文件夹后文件
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x.lower()))

    for item in items:
        item_path = os.path.join(path, item)
        is_dir = os.path.isdir(item_path)

        # 处理隐藏文件和文件夹
        if not show_hidden and item.startswith('.'):
            continue

        # 处理名称排除列表
        if item in exclude:
            continue

        # 处理通配符模式排除
        if any(fnmatch.fnmatch(item, pattern) for pattern in exclude_patterns):
            continue

        display_item = item

        # 添加文件大小信息
        if include_file_sizes and os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            display_item += f' ({size} bytes)'

        # 构建树结构
        if output_format == 'string':
            tree_str += indent * depth + prefix + display_item + '\n'
        elif output_format == 'json':
            node = {
                'name': display_item,
                'type': 'directory' if is_dir else 'file',
                'children': []
            }
        elif output_format == 'xml':
            node = ET.Element('directory' if is_dir else 'file', name=display_item)

        # 递归处理子目录
        if is_dir:
            child = print_tree(
                path=item_path,
                depth=depth + 1,
                max_depth=max_depth,
                exclude=exclude,
                exclude_patterns=exclude_patterns,
                show_hidden=show_hidden,
                include_file_sizes=include_file_sizes,
                indent=indent,
                prefix=prefix,
                output_format=output_format
            )

            if output_format == 'string':
                tree_str += child
            elif output_format == 'json':
                node['children'] = child
            elif output_format == 'xml':
                node.extend(child)

        if output_format == 'json':
            tree_json.append(node)
        elif output_format == 'xml':
            tree_xml.append(node)

    if output_format == 'string':
        return tree_str
    elif output_format == 'json':
        return tree_json
    elif output_format == 'xml':
        return tree_xml
