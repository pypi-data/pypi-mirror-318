import os.path

from pyscreeps_arena.core import *
from pyscreeps_arena.localization import *

import re
import shutil
import chardet
import subprocess
import pyperclip
from colorama import Fore

WAIT = Fore.YELLOW + ">>>" + Fore.RESET
GREEN = Fore.GREEN + "{}" + Fore.RESET
version_info = sys.version_info
python_version_cn = f"Python版本: {version_info.major}.{version_info.minor}.{version_info.micro}"
python_version_en = f"Compiler py-version: {version_info.major}.{version_info.minor}.{version_info.micro}"

# def InsertPragmaBefore(content:str) -> str:
#     """
#     在content的开头插入__pragma__('noalias', 'undefined')等内容 |
#         Insert __pragma__('noalias', 'undefined') at the beginning of content
#     :param content: str
#     :return: str
#     """
#     return PYFILE_PRAGMA_INSERTS + "\n" + content
class Compiler_Const:
    PROTO_DEFINES_DIRS = ["builtin", "library"]
    FILE_STRONG_REPLACE = {
        "std": {
            "==": "===",
            "!=": "!==",
        }
    }
    PYFILE_IGNORE_CHECK_FNAMES = ['game/const.py', 'game/proto.py', 'game/utils.py']

    PYFILE_PRAGMA_INSERTS = """
    # __pragma__('noalias', 'undefined')
    # __pragma__('noalias', 'Infinity')
    # __pragma__('noalias', 'clear')
    # __pragma__('noalias', 'get')
    """

    TOTAL_INSERT_AT_HEAD = """
    import {arenaInfo} from "game";
    """

    TOTAL_INSERT_BEFORE_MAIN = """
    """

    TOTAL_SIMPLE_REPLACE_WITH = {
    }

    PYFILE_WORD_WARNING_CHECK = {
        r"\.\s*get\s*\(": LOC_PYFILE_WORD_WARNING_CHECK_GET,
        r"import\s+math\s*": LOC_PYFILE_WORD_WARNING_CHECK_MATH,
        r"\.\s*clear\s*\(": LOC_PYFILE_WORD_WARNING_CHECK_CLEAR,
        r"\[\s*-\s*1\s*\]": LOC_PYFILE_WORD_WARNING_INDEX_MINUS_ONE,
    }

    PYFILE_EXIST_WARNING_CHECK = {
        r"__pragma__\s*\(\s*['\"]noalias['\"]\s*,\s*['\"]undefined['\"]\s*\)": "Strongly suggest to add '__pragma__('noalias', 'undefined')'.",
        r"__pragma__\s*\(\s*['\"]noalias['\"]\s*,\s*['\"]Infinity['\"]\s*\)": "Strongly suggest to add '__pragma__('noalias', 'Infinity')'.",
        r"__pragma__\s*\(\s*['\"]noalias['\"]\s*,\s*['\"]clear['\"]\s*\)": "Strongly suggest to add '__pragma__('noalias', 'clear')'.",
        r"__pragma__\s*\(\s*['\"]noalias['\"]\s*,\s*['\"]get['\"]\s*\)": "Strongly suggest to add '__pragma__('noalias', 'get')'.",
    }

    JS_VM = "org.transcrypt.__runtime__.js"

    GAME_UTILS = './builtin.utils.js'
    GAME_PROTO = './builtin.proto.js'
    GAME_CONST = './builtin.const.js'
    BUILTIN_TRANS = ["engine.js"]
    OTHER_IGNORE_WITH = "./builtin"

    SYSTEM_MODULES_IGNORE = {
        GAME_UTILS: ['CircleVisualStyle', 'Color', 'CostMatrix', 'CreateConstructionSiteResult', 'Direction', 'DoesZapCodeSpaceFlag',
                     'FindPathOptions', 'Goal', 'HeapInfo',
                     'LineStyle', 'LineVisualStyle', 'PolyVisualStyle', 'RectVisualStyle', 'SearchPathOptions', 'SearchPathResult', 'Terrain',
                     'TextAlign', 'TextVisualStyle',
                     'Visual', 'getAt', 'searchPath'],
        GAME_PROTO: ['BodyPartType', 'CreepAttackResult', 'CreepBuildResult', 'CreepDropResult', 'CreepHarvestResult', 'CreepHealResult',
                     'CreepMoveResult', 'CreepPickupResult',
                     'CreepPullResult', 'CreepRangedAttackResult', 'CreepRangedHealResult', 'CreepRangedMassAttackResult',
                     'CreepTransferResult', 'CreepWithdrawResult',
                     'ResourceType', 'SpawnCreepResult', 'Store', 'TowerAttackResult', 'TowerHealResult', 'Spawning', 'ScoreController',
                     'Flag', 'Position'],
        GAME_CONST: ['RESOURCE_SCORE'],
    }
    SYSTEM_MODULES_TRANSNAME = {  # 对应的在js中的名字 | Corresponding name in js
        GAME_UTILS: "game/utils",
        GAME_PROTO: "game/prototypes",
        GAME_CONST: "game/constants",
    }
    GENERATE_IGNORE_PYFILES = ['config.py']  # Won't be compiled into the final js code, only for defines.

    JS_IMPORT_PAT = re.compile(r'from\s+[\'\"]([^\']+)[\'\"]')
    INSERT_PAT = re.compile(r'#\s*insert\s+([^\n]*)')  # 因为被判定的string为单line，所以不需要考虑多行的情况

    TRANSCRYPT_ERROR_REPLACE = {
        # 由于transcrypt的问题，导致编译后的js代码中存在一些错误，需要进行替换
        r"new\s+set\s*\(": r"set(",
    }

class Compiler_Utils(Compiler_Const):
    last_output = False  # 一个小标志位，我只想输出一次此类告警信息

    @staticmethod
    def auto_read(fpath: str) -> str:
        """
        读取文件内容，自动应用编码
        :param fpath: str 文件路径
        """
        if not os.path.exists(fpath):
            if not Compiler_Utils.last_output:
                Compiler_Utils.last_output = True
                print()
            core.warn('Compiler_Utils.auto_read', core.lformat(LOC_FILE_NOT_EXISTS, [fpath]), end='', head='\n', ln=config.language)
            return ""

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(fpath, 'r', encoding='gbk') as f:
                    return f.read()
            except UnicodeDecodeError:
                # 如果使用检测到的编码读取失败，尝试使用chardet检测编码
                with open(fpath, 'rb') as f:  # 以二进制模式打开文件
                    raw_data = f.read()  # 读取文件的原始数据
                    result = chardet.detect(raw_data)  # 使用chardet检测编码
                    encoding = result['encoding']  # 获取检测到的编码
                with open(fpath, 'r', encoding=encoding) as f:  # 使用检测到的编码打开文件
                    return f.read()


    def copy_to(self) -> list:
        """
        复制src到build目录 | copy all files in src to build
        * 注意到src下的文件应当全部为py文件 |  all files in src should be py files
        """
        # copy to build dir
        # print(Fore.YELLOW + '>>> ' + Fore.RESET + ' copying to build dir: %s ...' % self.build_dir, end='')
        # LOC_COPYING_TO_BUILD_DIR

        core.lprint(WAIT, core.lformat(LOC_COPYING_TO_BUILD_DIR, [self.build_dir]), end="", ln=config.language)

        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)
        shutil.copytree(self.src_dir, self.build_dir)
        srcs = []  # src下所有python文件的路径 | paths of all python files under src
        for root, dirs, files in os.walk(self.build_dir):
            for file in files:
                if file.endswith('.py'):
                    srcs.append(os.path.join(root, file))
        # add libs
        for lib in self.PROTO_DEFINES_DIRS:
            shutil.copytree(lib, os.path.join(self.build_dir, lib))

        # overwrite last to [Done]
        # print(Fore.GREEN + '\r[1/6][Done]' + Fore.RESET + ' copying to build dir: %s' % self.build_dir)

        core.lprint(GREEN.format('[1/6]'), LOC_DONE, " ", core.lformat(LOC_COPYING_TO_BUILD_DIR_FINISH, [self.build_dir]), sep="", head="\r", ln=config.language)
        return srcs

    @staticmethod
    def potential_check(fpath:str, fname:str) -> bool:
        """
        检查某个py文件内是否有潜在问题 | check if there are potential problems in a py file

        如果有的话，输出[Warn][{file_name}/{line_io}]{detail} | if there are, output [Warn][{file_name}/{line_io}]{detail}

        Returns:
            bool: 是否有警告
        """
        # 文件路径检查
        if fpath.endswith('__init__.py') and fpath.find("builtin") == -1:
            core.error("potential_check", LOC_NOT_SUPPORT_PYFILE_INIT, ln=config.language, ecode=-1, head='\n')
        if fname in Compiler.PYFILE_IGNORE_CHECK_FNAMES:
            return False

        # # 文件内容检查
        content = Compiler.auto_read(fpath)
        warn_flag = False
        # # 内容关键字检查
        for pat, detail in Compiler.PYFILE_WORD_WARNING_CHECK.items():
            for i, line in enumerate(content.split('\n')):
                m = re.search(pat, line)
                if m:
                    # 检查m前面同一行内是否有#，如果有则忽略
                    comment = re.search(r'#', line[:m.start()])

                    # 检查m后面同一行内是否有#\s*ignore;，如果有则忽略
                    ignore = re.search(r'#\s*>\s*ignore', line[m.end():])

                    if not comment and not ignore:
                        warn_flag = True
                        core.warn('Compiler.potential_check', f'[{os.path.basename(os.path.dirname(fpath))}/{fname} line:{i + 1}]:', detail, end='', head='\n', ln=config.language)
        return warn_flag

    @staticmethod
    def preprocess_if_block(source_code: str, variables: dict[str, object]) -> str:
        """
        预处理if块，将 # > if, # > elif, # > else, # > endif 替换为实际的程序内容 |
        pre-process if blocks by replacing # > if, # > elif, # > else, # > endif with actual code.
        """
        lines = source_code.split('\n')  # 按行分割源代码 | split source code into lines
        stack = []  # 初始化一个栈，用于跟踪if条件 | initialize a stack to track if conditions
        result = []  # 初始化一个列表，用于存储处理后的代码行 | initialize a list to store processed code lines

        for i, line in enumerate(lines):  # 遍历源代码的每一行 | iterate over each line of source code
            striped = line.strip()  # 去掉行首尾的空格和换行符 | strip leading and trailing whitespace
            # 使用正则表达式匹配不同的条件语句 | use regex to match different conditional statements
            if_match = re.match(r'#\s*>\s*if\s+([^:.]*)$', striped)         # 匹配 '# > if' 语句 | match '# > if' statement
            elif_match = re.match(r'#\s*>\s*elif\s+([^:.]*)$', striped)     # 匹配 '# > elif' 语句 | match '# > elif' statement
            else_match = re.match(r'#\s*>\s*else$', striped)                # 匹配 '# > else' 语句 | match '# > else' statement
            endif_match = re.match(r'#\s*>\s*endif$', striped)              # 匹配 '# > endif' 语句 | match '# > endif' statement

            if if_match:  # 如果当前行是 '# > if' 语句 | if it's a '# > if' statement
                condition = if_match.group(1)  # 提取条件表达式 | extract the condition expression
                stack.append(eval(condition, variables))  # 评估条件表达式并将其结果压入栈中 | evaluate condition and push result onto stack
            elif elif_match and stack:  # 如果当前行是 '# > elif' 语句，并且栈不为空 | if it's a '# > elif' and stack isn't empty
                condition = elif_match.group(1)  # 提取条件表达式 | extract the condition expression
                stack[-1] = eval(condition, variables)  # 评估条件表达式并更新栈顶 | evaluate condition and update the top of the stack
            elif else_match and stack:  # 如果当前行是 '# > else' 语句，并且栈不为空 | if it's a '# > else' and stack isn't empty
                stack[-1] = not stack[-1]  # 将栈顶元素取反 | negate the top of the stack
            elif endif_match:  # 如果当前行是 '# > endif' 语句 | if it's a '# > endif' statement
                stack.pop()  # 弹出栈顶元素 | pop the top of the stack
            else:  # 如果当前行不是条件语句 | if it's not a conditional statement
                if not stack or all(stack):  # 如果栈为空，或者栈中所有元素均为真 | if stack is empty or all elements are True
                    result.append(line)  # 将当前行加入结果列表中 | add the current line to the result

        return '\n'.join(result)  # 将处理后的所有代码行连接成一个字符串，并返回最终结果 | join all processed lines into a string and return


class CompilerBase(Compiler_Utils):

    def __init__(self, src_dir, build_dir):
        # check
        if not os.path.exists(src_dir):
            core.error('Compiler.__init__', core.lformat(LOC_FILE_NOT_EXISTS, ['src', src_dir]), head='\n', ln=config.language)

        src_dir = os.path.abspath(src_dir)
        build_dir = os.path.abspath(build_dir)
        base_dir = os.path.dirname(src_dir)
        lib_dir = os.path.join(base_dir, 'library')
        built_dir = os.path.join(base_dir, 'builtin')

        # 在builtin文件下搜索需要跳过的文件，计入到PYFILE_IGNORE_CHECK_FNAMES中
        for fname in os.listdir(os.path.join(base_dir, "builtin")):
            if fname.endswith('.py') and fname not in ['const.py', 'proto.py', 'utils.py']:
                self.PYFILE_IGNORE_CHECK_FNAMES.append(f'builtin/{fname}')

        self.src_dir = os.path.abspath(src_dir)
        self.lib_dir = os.path.abspath(lib_dir)
        self.build_dir = os.path.abspath(build_dir)
        self.built_dir = os.path.abspath(built_dir)
        self.target_dir = os.path.join(self.build_dir, '__target__')
        self.build_name = os.path.basename(self.build_dir)


    @property
    def builtin_py(self) -> str:
        """
        返回builtin目录下的__init__.py的路径 | return the path of __init__.py in builtin
        """
        return os.path.join(self.built_dir, '__init__.py')

    @property
    def target_py(self) -> str:
        """
        返回build下的main.py的路径 | return the path of main.py in build
        """
        return os.path.join(self.build_dir, 'main.py')

    @property
    def target_js(self):
        """
        返回build下的main.js的路径 | return the path of main.js in build
        """
        return os.path.join(self.target_dir, 'main.js')



class Compiler(CompilerBase):
    def pre_compile(self):
        """
        预编译 | Precompile
        """
        src_paths = self.copy_to()

        core.lprint(WAIT, LOC_PREPROCESSING, end="", ln=config.language)
        py_fpath, py_names, warn_flag = [], [], False
        for root, dirs, files in os.walk(self.build_dir):
            for file in files:
                if file.endswith('.py'):
                    fpath: str = str(os.path.join(root, file))

                    # 将PYFILE_PRAGMA_INSERTS.replace("\t", "").replace("    ", "")插入到文件开头
                    content = self.auto_read(fpath)
                    content = self.PYFILE_PRAGMA_INSERTS.replace("\t", "").replace("    ", "") + content
                    # 如果是main.py，则将self.built_dir下的__init__.py文件内容插入到main.py文件开头
                    if fpath == self.target_py:
                        content = self.auto_read(self.builtin_py) + content
                    with open(fpath, 'w', encoding='utf-8') as f:  # 注意，这里修改的是build目录下的文件，不是源文件 | Note that the file under the build directory is modified here, not the source file
                        f.write(content)

                    # 得到src目录后面的内容
                    rel_name = os.path.relpath(fpath, self.build_dir).replace('\\', '/')
                    py_names.append(rel_name.replace('/', '.'))
                    py_fpath.append(fpath)
                    warn_flag |= self.potential_check(fpath, rel_name)
        if warn_flag:
            print()  # 换行

        _usubs_ = []  # update_subclass
        _pre_import_, _pre_imp_detail_ = [], {}  # > import
        _pre_sort_ = {}  # > sort
        _pre_define_ = {}  # > define
        _js_replace_, _insert_id_ = {}, 0  # > insert


        # ---------------------------------- UPDATABLE ---------------------------------- #
        # 获取在src目录内定义的所有继承了Updatable或CreepLogic的类 |
        # get all classes that inherit from Updatable or CreepLogic defined in the src directory
        for i, fpath in enumerate(py_fpath):
            if fpath in src_paths:
                content = self.auto_read(fpath)
                for line in content.split('\n'):
                    m = re.search(r'class\s+([^\s(]+)\s*\((Updatable|CreepLogic)', line)
                    if m:
                        _usubs_.append(m.group(1))

        # change REPALCE: '/// $UPDATABLE.UPDATES$ ///'
        _rp_key = "/// $UPDATABLE.UPDATES$ ///"
        _rp_txt = ""
        for usub in _usubs_:
            _rp_txt += "try{" + f"if ({usub} && !Updatable.UPDATES.includes({usub}))Updatable.UPDATES.append({usub});"  + "}catch(e){ if (!(e instanceof ReferenceError)) throw e; }\n"
        self.TOTAL_SIMPLE_REPLACE_WITH[_rp_key] = _rp_txt


        # ----------------------------------- IMPORT ----------------------------------- #
        # 获取所有.py文件中的所有import的内容，并记录下来fname:[imp1, imp2, ...]
        # | get all import in .py files, and record them fname:[imp1, imp2, ...]
        for i, fpath in enumerate(py_fpath):
            fname = py_names[i][:-3] + '.js'
            content = self.auto_read(fpath)
            for i, line in enumerate(content.split('\n')):
                m = re.search(r'#\s*>\s*import\s+([^\n]+)', line)
                if m:
                    _pre_import_.append('./' + re.sub(r'\s', '', m.group(1)) + '.js')
                    # 记录文件/lineio信息
                    _pre_imp_detail_[_pre_import_[-1]] = f'{fname}/line:{i + 1}'

        # ----------------------------------- REMOVE ----------------------------------- #
        # 移除所有# > remove所在行的内容
        # | remove all # > remove in .py files
        for fpath in py_fpath:
            content = self.auto_read(fpath)
            new_content = ""
            for line in content.split('\n'):
                if not re.search(r'#\s*>\s*remove', line):
                    new_content += line + '\n'

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        # ------------------------------------ SORT ------------------------------------ #
        # 获取所有.py文件中的所有# > sort的内容，并记录下来(不存在则默认为65535)
        # | get all # > sort in .py files, and record them (default 65535 if not exists)
        for i, fpath in enumerate(py_fpath):
            fname = py_names[i][:-3] + '.js'
            content = self.auto_read(fpath)
            m = re.search(r'#\s*>\s*sort\s+(\d+)', content)
            if m:
                try:
                    sort_num = int(m.group(1))
                except ValueError:
                    core.warn('Compiler.pre_compile', core.lformat(LOC_SORT_NUMBER_ERROR, [m.group(1)]), end='', head='\n', ln=config.language)
                    sort_num = 65535
                _pre_sort_[fname] = sort_num
            else:
                _pre_sort_[fname] = 65535

        # ------------------------------------ DEFINE ------------------------------------ #
        # 扫描所有# > define的内容，然后在.py中移除这些行，并记录下来
        # | get all # > define in .py files, and record them
        for fpath in py_fpath:
            content = self.auto_read(fpath)
            new_content = ""
            for line in content.split('\n'):
                # re.compile(r'#\s*define\s+([^\s]+)\s+([^\n]*)')
                m = re.search(r'#\s*>\s*define\s+([^\s]+)\s+([^\n]*)', line)
                if m:
                    _pre_define_[m.group(1)] = m.group(2)
                    new_content += '\n'
                else:
                    new_content += line + '\n'

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        # 按照keys的顺序，先用前面的key对应的内容去依次替换后面的key对应的value中
        # | replace the value of the key with the content of the previous key in order
        _def_keys = list(_pre_define_.keys())
        _keys_len = len(_def_keys)
        for i in range(_keys_len - 1):
            for j in range(i + 1, _keys_len):
                _pre_define_[_def_keys[j]] = _pre_define_[_def_keys[j]].replace(_def_keys[i], _pre_define_[_def_keys[i]])

        # ------------------------------------ DEFINE:REPLACE ------------------------------------ #
        # 将刚才记录的define替换到.py中(注意优先替换更长的串)(因此先排序)
        # | replace the defined content to .py files (replace the longer string first)
        _def_keys.sort(key=lambda x: len(x), reverse=True)
        for fpath in py_fpath:
            content = self.auto_read(fpath)

            # std.py PYSCREEPS_ARENA_PYTHON_VERSION replace
            if os.path.basename(fpath).lower() == 'std.py':
                content = content.replace('PYSCREEPS_ARENA_PYTHON_VERSION_EN', f'\"{python_version_en}\"')
                content = content.replace('PYSCREEPS_ARENA_PYTHON_VERSION_CN', f'\"{python_version_cn}\"')

            for key in _def_keys:
                content = re.sub(r'[^_A-Za-z0-9]' + key, self._kfc_wrapper(_pre_define_[key]), content)

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)

        # ------------------------------------ IF BLOCK ------------------------------------ #
        # 预处理if块，将 # > if, # > elif, # > else, # > endif 替换为实际的程序内容
        # | preprocess if block, replace # > if, # > elif, # > else, # > endif to actual code
        for fpath in py_fpath:
            content = self.auto_read(fpath)

            content = self.preprocess_if_block(content, _pre_define_)

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)

        # ------------------------------------ INSERT ------------------------------------ #
        # 扫描所有# > insert的内容，然后在.py中将整行替换为# __pragma__("js", __JS_INSERT_{id})
        # | get all # > insert in .py files, and replace the whole line with # __pragma__("js", __JS_INSERT_{id})
        for fpath in py_fpath:
            content = self.auto_read(fpath)
            new_content = ""
            for line in content.split('\n'):
                # re.compile(r'#\s*insert\s*([^\n]*)')
                # '# > insert if(obj && obj.body) for(var p of obj.body) if (p.type == MOVE) return true;'
                m = re.search(r'#\s*>\s*insert\s+([^\n]*)', line)
                if m:
                    _sign_index_ = line.find('#')  # 必然存在
                    _js_key_ = f"__JS_INSERT_{_insert_id_:08d}"
                    _js_replace_[_js_key_] = m.group(1)

                    new_content += line[:_sign_index_] + f'# __pragma__("js", "{_js_key_}")\n'
                    _insert_id_ += 1
                else:
                    new_content += line + '\n'

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        core.lprint(GREEN.format('[2/6]'), LOC_DONE, " ", LOC_PREPROCESSING_FINISH, sep="", head="\r", ln=config.language)
        return _pre_import_, _pre_imp_detail_, _pre_sort_, _pre_define_, _js_replace_

    def clear_not_generate_pyfile(self):
        """
        清空不需要编译的py文件 | clear not generate py file
        :return:
        """
        for root, dirs, files in os.walk(self.build_dir):
            for file in files:
                if file.endswith('.py') and file in self.GENERATE_IGNORE_PYFILES:
                    with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                        f.write('')

    def transcrypt_cmd(self):
        # 执行cmd命令: transcrypt -b -m -n -s -e 6 target | execute cmd: transcrypt -b -m -n -s -e 6 target
        # 并获取cmd得到的输出 | and get the output of the cmd
        cmd = 'transcrypt -b -m -n -s -e 6 %s' % self.target_py
        core.lprint(WAIT, core.lformat(LOC_TRANSCRYPTING, [cmd]), end="", ln=config.language)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if 'Error while compiling' in stdout.decode():
            print('\r' + stdout.decode())
            core.error('Compiler.transcrypt_cmd', LOC_TRANSCRYPTING_ERROR, indent=1, head='\n', ln=config.language)
        core.lprint(GREEN.format('[3/6]'), LOC_DONE, " ", LOC_TRANSCRYPTING_FINISH, sep="", head="\r", ln=config.language)

    @staticmethod
    def _keep_lbracket(matched) -> str:
        """
        如果第一个字符是{, 则返回'{'，否则返回'' | if the first char is {, return '{', else return ''
        :param matched:
        :return:
        """
        return '{' if matched.group(0)[0] == '{' else ''

    @staticmethod
    def _keep_first_char(matched:re.Match) -> str:
        """
        保留第一个字符 | keep the first char
        :param matched: re.match object | re.match对象
        :return:
        """
        return matched.group(0)[0]

    @staticmethod
    def _kfc_wrapper(replace:str) -> callable:
        """
        获取一个保留第一个字符的函数 | get a function to keep the first char
        :param replace: str
        :return: function
        """

        def _kfc(matched) -> str:
            return matched.group(0)[0] + replace

        return _kfc

    def analyze_rebuild_main_js(self, defs:dict[str, object]) -> tuple[str, list[str]]:
        """
        分析main.js中导入的模块名称和先后顺序, 并重新生成main.js | analyze the module names and order imported in main.js, and rebuild main.js
        * 主要移除非SYSTEM_MODULES_IGNORE中的模块导入语句 | mainly remove the module import statements that are not in SYSTEM_MODULES_IGNORE
        :param defs: dict{define: value} 定义的变量 | defined variables
        :return: imports : str, modules (names: str)
                imports是一段用于放在js主体开头的import语句 | imports is a string of import statements to be placed at the beginning of the js body
                modules是一个list，包含了所有的模块名称 | modules is a list containing all module names
                                    其中的内容可能是这样的: ['./game.utils.js', './game.proto.js', './game.const.js', ...]
        """

        # create undefined
        imports = ""

        if defs.get('USE_TUTORIAL_FLAG', '0') == '0' and defs.get('USE_ARENA_FLAG', '0') == '0':
            imports += 'var Flag = undefined;\n'
        if defs.get('USE_SCORE_COLLECTOR', '0') == '0':
            imports += 'var ScoreController = undefined;\nvar RESOURCE_SCORE = undefined;\n'
        imports += '\n'

        core.lprint(WAIT, LOC_ANALYZING_AND_REBUILDING_MAIN_JS, end="", ln=config.language)

        content = self.auto_read(self.target_js)
        modules, new_content = [], ""
        for line in content.split('\n'):
            m = re.search(self.JS_IMPORT_PAT, line)
            if not m:
                new_content += line + '\n'
                continue
            # remove ignore if in SYSTEM_MODULES_IGNORE
            module = m.group(1)
            for ignore in self.SYSTEM_MODULES_IGNORE.get(module, []):
                line = re.sub(r'[\s{]' + ignore + ',?', self._keep_lbracket, line)

            # do not add in modules if in system_modules_ignores
            if module in self.SYSTEM_MODULES_IGNORE:
                if module in self.SYSTEM_MODULES_TRANSNAME:
                    line = line.replace(module, self.SYSTEM_MODULES_TRANSNAME[module])  # 调整为js中的名称
                imports += line + '\n'
                continue

            _ignore = False
            if module in modules: _ignore = True
            if not _ignore and module.startswith(self.OTHER_IGNORE_WITH): _ignore = True
            for keeps in self.BUILTIN_TRANS:
                if module.endswith(keeps): _ignore = False
            if not _ignore: modules.append(module)

        # save raw main.js
        with open(self.target_js[:-3] + ".raw.js", 'w', encoding='utf-8') as f:
            f.write(content)

        # write rebuild main.js
        with open(self.target_js, 'w', encoding='utf-8') as f:
            f.write(new_content)

        core.lprint(GREEN.format('[4/6]'), LOC_DONE, " ", LOC_ANALYZING_AND_REBUILDING_MAIN_JS_FINISH, sep="", head="\r", ln=config.language)

        return imports, modules

    @staticmethod
    def remove_js_import(raw) -> str:
        """
        移除js中的import行
        :param raw:
        :return:
        """
        return re.sub(r'import[^\n]*\n', '', raw)

    def generate_total_js(self, usr_modules, t_imps: dict, f_sorts, f_replaces, g_replaces) -> str:
        """
        生成总的main.js
        按照如下顺序组合:
            ./org.transcrypt.__runtime__.js
            ./game.const.js  # IGNORE
            ./game.proto.js  # IGNORE
            ./game.utils.js  # IGNORE
            {usr_modules}
        :param usr_modules: list[str]  # js vm + 用户自定义模块
        :param t_imps: dict{module_name: detail}
        :param f_sorts: dict{module_name: sort_priority}
        :param f_replaces: dict{module_name: dict{old: new}}
        :param g_replaces: dict{old: new}
        :return: str
        """
        total_js = "" + self.TOTAL_INSERT_AT_HEAD

        core.lprint(WAIT, LOC_GENERATING_TOTAL_MAIN_JS, end="", ln=config.language)

        # resort modules
        f_sorts[self.JS_VM] = -1

        err_flag = False
        for module in usr_modules:
            if module[2:] not in f_sorts:
                print(Fore.RED + '\n[Error] ' + Fore.RESET + f'"{module[2:-3]}.py" is not a user module.')
                imp_detail = t_imps.get(module, None)
                if imp_detail:
                    print("\t\t-- May be imported by user in: %s" % imp_detail)
                else:
                    print("\t\t-- Please move this file into the 'src' directory.")
                err_flag = True
        if err_flag:
            sys.exit(1)
        for i in range(len(usr_modules)):
            for j in range(i + 1, len(usr_modules)):
                if f_sorts[usr_modules[i][2:]] > f_sorts[usr_modules[j][2:]]:
                    usr_modules[i], usr_modules[j] = usr_modules[j], usr_modules[i]

        # write modules
        for module in usr_modules:
            content = self.auto_read(os.path.join(self.target_dir, module))
            content = self.remove_js_import(content)
            for old, new in f_replaces.get(module, {}).items():
                content = re.sub(old, new, content)
            for old, new in self.TRANSCRYPT_ERROR_REPLACE.items():
                content = re.sub(old, new, content)
            total_js += f"\n// ---------------------------------------- Module:{module} "
            total_js += "----------------------------------------\n\n"
            total_js += content + '\n'


        total_js += self.TOTAL_INSERT_BEFORE_MAIN

        # write main.js
        content = self.auto_read(self.target_js)
        for old, new in self.TRANSCRYPT_ERROR_REPLACE.items():
            content = re.sub(old, new, content)
        total_js += content

        # global replace
        for old, new in g_replaces.items():
            total_js = re.sub(old, new, total_js)

        core.lprint(GREEN.format('[5/6]'), LOC_DONE, " ", LOC_GENERATING_TOTAL_MAIN_JS_FINISH, sep="", head="\r", ln=config.language)

        # REPACE
        for old, new in self.TOTAL_SIMPLE_REPLACE_WITH.items():
            total_js = total_js.replace(old, new)

        return total_js

    def __parse_js_file_sort(self, fpath):
        """
        解析js文件中的sort
        :param fpath:
        :return:
        """
        content = self.auto_read(fpath)
        m = re.search(r'//\s*>\s*sort\s+(\d+)', content)
        if m:
            return int(m.group(1))
        return 65535


    def find_add_pure_js_files(self, sorts, modules):
        """
        找到所有的纯js文件，并添加到modules中
        :param sorts:
        :param modules:
        :return:
        """
        for root, dirs, files in os.walk(self.lib_dir):
            for file in files:
                if file.endswith('.js') and file not in modules:
                    fpath = str(os.path.join(root, file))
                    fname = file.replace('\\', '/')
                    # copy file to target
                    shutil.copy(fpath, os.path.join(self.target_dir, fname))
                    sorts[fname] = self.__parse_js_file_sort(fpath)
                    modules.append("./" + fname)

    def compile(self, export_to=None, paste=False):
        """
        编译
        :param export_to: 指定main.mjs的输出路径(/main.mjs)
        :param paste: 是否复制到剪贴板
        :return:
        """
        imps, imp_ts, sorts, defs, reps = self.pre_compile()
        self.clear_not_generate_pyfile()  # 清空不需要编译的py文件(请确保在pre_compile之后)
        self.transcrypt_cmd()
        imports, modules = self.analyze_rebuild_main_js(defs)
        self.find_add_pure_js_files(sorts, modules)
        total_js = imports + "\n" + self.generate_total_js(list(set(modules + imps)), imp_ts, sorts, self.FILE_STRONG_REPLACE, reps)

        core.lprint(WAIT, LOC_EXPORTING_TOTAL_MAIN_JS, end="", ln=config.language)

        # ensure exported main.mjs path
        build_main_mjs = os.path.join(self.build_dir, 'main.mjs')

        if not export_to:
            # 尝试读取defs
            mjs_path = defs.get('MAIN_JS_PATH', build_main_mjs)
        else:
            mjs_path = export_to

        if not mjs_path.endswith('js'):
            mjs_path = os.path.join(mjs_path, 'main.mjs')

        # write main.mjs
        with open(build_main_mjs, 'w', encoding='utf-8') as f:
            f.write(total_js)

        # export main.mjs
        dir_path = os.path.dirname(mjs_path)
        if not os.path.exists(dir_path):
            core.error('Compiler.compile', core.lformat(LOC_EXPORT_DIR_PATH_NOT_EXISTS, [dir_path]), head='\n', ln=config.language)
        with open(mjs_path, 'w', encoding='utf-8') as f:
            f.write(total_js)

        core.lprint(GREEN.format('[6/6]'), LOC_DONE, " ", LOC_EXPORTING_TOTAL_MAIN_JS_FINISH, sep="", head="\r", ln=config.language)

        if mjs_path != build_main_mjs:
            core.lprint(Fore.LIGHTBLUE_EX + '[Info] ' + Fore.RESET, core.lformat(LOC_USR_EXPORT_INFO, [mjs_path]), ln=config.language)

        # copy to clipboard
        if paste:
            pyperclip.copy(total_js)
            core.lprint(LOC_DONE, " ", LOC_COPY_TO_CLIPBOARD, ln=config.language)

    def clean(self):
        """
        清除build目录下除了main.mjs之外的所有文件和目录
        * 先复制main.mjs到src目录下，然后删除build目录，再将main.mjs剪切回build目录
        :return:
        """
        core.lprint(WAIT, LOC_CLEAN_BUILD_DIR, end="", ln=config.language)
        if not os.path.exists(self.build_dir):
            core.error('Compiler.clean', LOC_BUILD_DIR_NOT_EXISTS, indent=1, head='\n', ln=config.language)

        if not os.path.exists(os.path.join(self.build_dir, 'main.mjs')):
            core.error('Compiler.clean', LOC_MAIN_MJS_NOT_EXISTS, indent=1, head='\n', ln=config.language)

        # copy main.mjs to src
        shutil.copy(os.path.join(self.build_dir, 'main.mjs'), os.path.join(self.src_dir, 'main.mjs'))

        # remove build dir
        shutil.rmtree(self.build_dir)

        # create build dir
        os.makedirs(self.build_dir)

        # move main.mjs to build dir
        shutil.move(os.path.join(self.src_dir, 'main.mjs'), os.path.join(self.build_dir, 'main.mjs'))

        core.lprint(GREEN.format('[Done]'), LOC_CLEAN_BUILD_DIR_FINISH, head="\r", ln=config.language)

    def clear(self):
        """
        清除build目录下所有文件和目录
        :return:
        """
        core.lprint(WAIT, LOC_CLEAN_BUILD_DIR, end="", ln=config.language)
        if not os.path.exists(self.build_dir):
            core.lprint(LOC_BUILD_DIR_NOT_EXISTS, ln=config.language)

        shutil.rmtree(self.build_dir)
        os.makedirs(self.build_dir)

        core.lprint(GREEN.format('[Done]'), LOC_CLEAN_BUILD_DIR_FINISH, head="\r", ln=config.language)


if __name__ == '__main__':
    compiler = Compiler('src', 'library', 'build')
    compiler.compile()
    compiler.clean()
