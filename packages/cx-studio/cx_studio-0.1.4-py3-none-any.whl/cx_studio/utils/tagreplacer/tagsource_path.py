import re
from functools import lru_cache
from pathlib import Path

from cx_studio.utils.textutils import contains_invisible_char, is_quoted, quote_text


class TagSourcePath:
    """
    TagSourcePath 类用于处理文件路径，并提供了一些方法来获取路径的不同部分。

    Attributes:
        SPACE_MODES (list): 定义了处理空格的模式，包括 'quote', 'escape', 'ignore'。
    """

    SPACE_MODES = ["quote", "escape", "ignore"]

    def __init__(self, path: Path, space_mode=None):
        """
        初始化 TagSourcePath 实例。

        Args:
            path (Path): 文件路径。
            space_mode (str, optional): 处理空格的模式，可选值为 'quote', 'escape', 'ignore'。默认为 None。

        Raises:
            TypeError: 如果 path 不是 Path 对象。
        """
        if not isinstance(path, Path):
            raise TypeError("path must be a Path object")
        self._source = path
        self._space_mode = space_mode

    @property
    @lru_cache(maxsize=128)
    def _neat_source(self):
        """
        返回解析后的路径。

        Returns:
            Path: 解析后的路径。
        """
        return self._source.resolve()

    @lru_cache(maxsize=128)
    def _handle(self, argument):
        """
        根据参数返回路径的不同部分。

        Args:
            argument (str): 参数，用于指定返回路径的哪一部分。

        Returns:
            str: 路径的相应部分。
        """
        match argument:
            case "absolute":
                return self._neat_source.absolute()
            case "name":
                return self._source.name
            case "basename":
                name = self._source.name
                index = name.find(".")
                if index != -1:
                    return name[:index]
                else:
                    return name
            case "suffix":
                return self._source.suffix
            case "complete_suffix":
                return "".join(self._source.suffixes)
            case "suffix_no_dot":
                suffix = self._source.suffix
                if suffix.startswith("."):
                    return suffix[1:]
                return suffix
            case "complete_suffix_no_dot":
                suffix = "".join(self._source.suffixes)
                if suffix.startswith("."):
                    return suffix[1:]
                return suffix
            case "complete_basename":
                return self._source.stem
            case "parent":
                return self._source.parent
            case "parent_absolute":
                return self._neat_source.parent.absolute()
            case "parent_name":
                return self._source.parent.name
            case _:
                return self._source

    def _handle_spaces(self, result):
        """
        根据空格处理模式处理结果字符串中的空格。

        Args:
            result (str): 包含空格的字符串。

        Returns:
            str: 处理后的字符串。
        """
        if is_quoted(result) and contains_invisible_char(result):
            if self._space_mode == "quote":
                result = quote_text(result)
            elif self._space_mode == "escape":
                result = re.sub(r"\s+", "\\ ", result)
        return result

    def __call__(self, argument):
        """
        根据参数返回路径的不同部分，并根据空格处理模式处理结果。

        Args:
            argument (str): 参数，用于指定返回路径的哪一部分。

        Returns:
            str: 路径的相应部分，根据空格处理模式处理后的结果。
        """
        result = str(self._handle(argument))
        return self._handle_spaces(result)
