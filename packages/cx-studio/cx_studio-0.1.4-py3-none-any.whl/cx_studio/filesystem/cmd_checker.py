import itertools
import os
from pathlib import Path
from cx_studio.core import MemberCaches
from .path_utils import ensure_paths, is_executable


class CommandChecker:
    """
    CommandChecker 类用于查找并验证可执行文件的存在。

    原则上 CommandChecker 用于检查*用于命令行输入的可执行文件*是否可用，所以不会触发错误，如果查找失败则会尽量按照原样返回。

    注意：
        此类不会触发错误，因此无法保证可执行文件的可用性。

    Attributes:
        _source (str): 要查找的可执行文件的名称或路径。
        _include_pwd (bool): 是否包含当前工作目录。
        _extra_paths (list[Path]): 额外的搜索路径列表。
        _extra_suffixes (list[str]): 可执行文件的额外后缀列表。

    Methods:
        _possible_sources(): 生成可能的可执行文件源列表。
        os_paths(): 生成系统路径列表。
        additional_paths(): 生成额外的搜索路径列表。
        search_paths(): 生成所有搜索路径列表。
        executable(): 查找并返回可执行文件的路径。
    """

    def __init__(
        self,
        executable: str,
        include_pwd=True,
        extra_paths: list[Path] = None,
        extra_suffixes: list[str] = None,
    ):
        """
        初始化 CommandChecker 实例。

        Args:
            executable (str): 要查找的可执行文件的名称或路径。
            include_pwd (bool, optional): 是否包含当前工作目录。默认为 True。
            extra_paths (list[Path], optional): 额外的搜索路径列表。默认为 None。
            extra_suffixes (list[str], optional): 可执行文件的额外后缀列表。默认为 None。
        """
        self._source = str(executable)
        self._include_pwd = include_pwd
        self._extra_paths = [x for x in ensure_paths(extra_paths)]
        self._extra_suffixes = extra_suffixes if extra_suffixes else []

    def _possible_sources(self):
        """
        生成可能的可执行文件源列表。

        Yields:
            str: 可能的可执行文件源。
        """
        possible_suffixes = [".exe", ".com"]
        yield self._source
        for suffix in possible_suffixes:
            yield self._source + suffix
        for x in self._extra_suffixes:
            suffix = str(x)
            if not suffix.startswith("."):
                suffix = "." + suffix
            yield self._source + suffix

    @staticmethod
    def os_paths():
        """
        生成系统路径列表。

        Yields:
            Path: 系统路径。
        """
        for p in os.environ["PATH"].split(os.pathsep):
            yield Path(p)

    def additional_paths(self):
        """
        生成额外的搜索路径列表。

        Yields:
            Path: 额外的搜索路径。
        """
        for p in self._extra_paths:
            if p.is_dir():
                yield p
        if self._include_pwd:
            yield Path.cwd()

    def search_paths(self):
        """
        生成所有搜索路径列表。

        Yields:
            Path: 所有搜索路径。
        """
        yield from self.os_paths()
        yield from self.additional_paths()

    def executable(self) -> str:
        """
        查找并返回可执行文件的路径。

        Returns:
            str: 可执行文件的路径，如果未找到则返回空字符串。
        """
        if os.path.isabs(self._source) and is_executable(Path(self._source)):
            return self._source

        for folder, file in itertools.product(
            self.os_paths(), self._possible_sources()
        ):
            cmd = Path(folder) / file
            if is_executable(cmd):
                return self._source

        for folder, file in itertools.product(
            self.additional_paths(), self._possible_sources()
        ):
            cmd = Path(folder) / file
            if is_executable(cmd):
                return cmd.resolve()

        return ""

    def absolute(self) -> str:
        result = self.executable()
        if result:
            return str(Path(result).resolve())
        return ""
