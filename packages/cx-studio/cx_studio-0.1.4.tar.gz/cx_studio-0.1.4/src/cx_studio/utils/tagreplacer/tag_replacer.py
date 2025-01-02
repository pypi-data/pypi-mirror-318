import re


class TagReplacer:
    """
    TagReplacer 类用于替换字符串中的标签。

    标签的格式为 `${tag_name}` 或 `${tag_name:param}`，其中 `tag_name` 是数据源的名称，`param` 是可选的参数。
    TagReplacer 类支持安装多个数据源，并根据这些数据源来替换字符串中的标签。

    Attributes:
        TAG_PATTERN (re.Pattern): 用于匹配标签的正则表达式模式。
        _data_sources (dict): 存储数据源的字典，键为标签名称，值为数据源。
        _keep_unknown_tags (bool): 如果为 True，则保留未知的标签；否则替换为默认数据。
        _default_data (str): 用于替换未知标签的默认数据。
    """

    TAG_PATTERN = re.compile(r"\${([^:{}]+)(?::([^:{}]+))?}")

    def __init__(self, keep_unknown_tags=True, default_data=""):
        """
        初始化 TagReplacer 实例。

        Args:
            keep_unknown_tags (bool, optional): 如果为 True，则保留未知的标签；否则替换为默认数据。默认为 True。
            default_data (str, optional): 用于替换未知标签的默认数据。默认为空字符串。
        """
        self._data_sources = {}
        self._keep_unknown_tags = keep_unknown_tags
        self._default_data = str(default_data)  # 确保默认数据是字符串

    def install_data_source(self, tag: str, source):
        """
        安装一个数据源。

        数据源可以是一个可调用对象或一个字符串。如果是可调用对象，它将被调用以获取替换数据。

        Args:
            tag (str): 数据源的标签名称。
            source (callable or str): 数据源，可以是一个可调用对象或一个字符串。

        Raises:
            TypeError: 如果 `tag` 不是字符串，或者 `source` 既不是可调用对象也不是字符串。

        Returns:
            TagReplacer: 返回当前实例，以便链式调用。
        """
        if not isinstance(tag, str):
            raise TypeError("Tag must be a string")
        if callable(source):
            self._data_sources[tag] = source
        elif isinstance(source, str):
            self._data_sources[tag] = source
        else:
            raise TypeError("Source must be a callable or a string")
        return self

    def tags(self):
        """
        获取所有已安装的数据源的标签。

        Returns:
            dict_keys: 数据源标签的键视图。
        """
        return self._data_sources.keys()

    def __lookup_match(self, match: re.Match):
        """
        根据匹配的标签查找替换数据。

        Args:
            match (re.Match): 正则表达式匹配对象。

        Returns:
            str: 替换数据，如果标签未找到且 `_keep_unknown_tags` 为 True，则返回原始标签；否则返回默认数据。
        """
        tag = match.group(1)
        param = match.group(2) or None
        if tag in self._data_sources:
            source = self._data_sources[tag]
            if callable(source):
                return (
                    source(param) if param is not None else source()
                )  # 检查参数是否为 None
            elif isinstance(source, str):
                return source
            else:
                return tag

        if self._keep_unknown_tags:
            return match.group(0)
        return self._default_data

    def lookup(self, tag: str):
        """
        查找并返回给定标签的替换数据。

        Args:
            tag (str): 要查找的标签。

        Returns:
            str: 替换数据，如果标签未找到且 `_keep_unknown_tags` 为 True，则返回原始标签；否则返回默认数据。
        """
        match = self.TAG_PATTERN.match(tag)
        if match:
            return self.__lookup_match(match)
        elif self._keep_unknown_tags:
            return tag
        else:
            return self._default_data

    def replace_tags(self, text: str):
        """
        替换字符串中的所有标签。

        Args:
            text (str): 包含标签的字符串。

        Returns:
            str: 替换后的字符串。
        """
        return self.TAG_PATTERN.sub(self.__lookup_match, text)

    def __call__(self, text: str):
        """
        使实例可调用，用于替换字符串中的所有标签。

        Args:
            text (str): 包含标签的字符串。

        Returns:
            str: 替换后的字符串。
        """
        t = str(text or "")
        result = self.replace_tags(t)
        return result
