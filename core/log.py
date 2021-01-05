import os
import re
import time
import fcntl
import shutil
import logging.config

from configs import LOGGING_PATH

from stat import ST_MTIME
from logging import FileHandler, StreamHandler
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler


class StreamHandler_MP(StreamHandler):
    """
    一个处理程序类，它将日志记录适当地格式化，写入流。用于多进程
    """
    def emit(self, record):
        """
        发出一个记录。首先seek(写文件流时控制光标的)到文件的最后，以便多进程登录到同一个文件。
        """
        try:
            if hasattr(self.stream, "seek"):
                self.stream.seek(0, 2)
        except IOError as e:
            pass
        StreamHandler.emit(self, record)


class FileHandler_MP(FileHandler,StreamHandler_MP):
    """
    为多进程写入格式化日志记录到磁盘文件的处理程序类。
    """
    def emit(self, record):
        """
        发出一条记录。
        如果因为在构造函数中指定了延迟而未打开流，则在调用超类发出之前打开它。
        """
        if self.stream is None:
            self.stream = self._open()
        StreamHandler_MP.emit(self,record)


class RotatingFileHandler_MP(RotatingFileHandler,FileHandler_MP):
    """
    处理程序，用于记录一组文件，当当前文件达到一定大小时，该文件从一个文件切换到下一个文件。
    基于logging.RotatingFileHandler文件处理程序，用于多进程的修正
    """
    _lock_dir = '.lock'
    if os.path.exists(_lock_dir):
        pass
    else:
        os.mkdir(_lock_dir)

    def doRollover(self):
        """
        做一个翻转，如__init__()中所描述的，对于多进程，我们使用深拷贝（shutil.copy）而不是重命名。
        """

        self.stream.close()
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d" % (self.baseFilename, i)
                dfn = "%s.%d" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    shutil.copy(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.remove(dfn)
            if os.path.exists(self.baseFilename):
                shutil.copy(self.baseFilename, dfn)
        self.mode = "w"
        self.stream = self._open()

    def emit(self, record):
        """
        发送一条记录，
        将记录输出到文件中，如doRollover().对于多进程，我们使用文件锁。还有更好的方法吗？
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            FileLock = self._lock_dir + '/' + os.path.basename(self.baseFilename) + '.' + record.levelName
            f = open(FileLock, "w+")
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            FileHandler_MP.emit(self, record)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            f.close()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

class TimedRoeatingFileHandler_MP(TimedRotatingFileHandler, FileHandler_MP):
    """
    处理程序，用于logging文件，以一定的时间间隔旋转日志文件。
    如果 backupCount > 0，则在进行翻转时，保持不超过backupCount个数的文件。
    最老的被删除。
    """
    _lock_dir = '.lock'
    if os.path.exists(_lock_dir):
        pass
    else:
        os.mkdir(_lock_dir)

    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=0, utc=0):
        FileHandler_MP.__init__(self, filename, 'a', encoding, delay)
        self.encoding = encoding
        self.when = when
        self.backupCount = backupCount
        self.utc = utc

        # 计算实际更新间隔，这只是更新之间的秒数。还设置在更新发生时使用的文件名后缀。
        # 当前的'when'为什么是时得到支持：
        # S - Seconds 秒
        # M - Minutes 分钟
        # H - Hours   小时
        # D - Days    天
        # 在夜里进行文件更新
        # W{0－6} -在某一天更新；0代表星期一 6代表星期日
        # “when” 的的情况并不重要；小写或大写字母都会起作用。

        if self.when == 'S':
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == "M":
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == "H":
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == "D" or self.when == "MIDNIGHT":
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        elif self.when.startswith('W'):
            if len(self.when) != 2:
                raise ValueError("你必须指定每周更新日志的时间从0到6（0是星期一）: %s" % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError("每周更新时间是无效日期: %s" % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}"
        else:
            raise ValueError("指定的更新间隔无效: %s" % self.when)

        self.extMatch = re.compile(self.extMatch)

        if interval != 1:
            raise ValueError("无效翻滚间隔，必须为1。")

    def shouldRollover(self, record):
        """
        确定是否发生翻滚。记录不被使用，因为我们只是比较时间，但它需要方法签名是相同的。
        """
        if not os.path.exists(self.baseFilename):
            # print(“文件不存在”)
            return 0

        cTime = time.localtime(time.time())
        mTime = time.localtime(os.stat(self.baseFilename)[ST_MTIME])
        if self.when == "S" and cTime[5] != mTime[5]:
            # print("cTime:",cTime[5],"mTime:",mTime[5])
            return 1
        elif self.when == "M" and cTime[4] != mTime[4]:
            # print("cTime:",cTime[4],"mTime:",mTime[4])
            return 1
        elif self.when == "H" and cTime[3] != mTime[3]:
            # print("cTime:",cTime[3],"mTime:",mTime[3])
            return 1
        elif (self.when == "MIDNIGHT" or self.when == 'D') and cTime[2] != mTime[2]:
            # print("cTime:",cTime[2],"mTime:",mTime[2])
            return 1
        elif self.when == "W" and cTime[1] != mTime[1]:
            # print("cTime:",cTime[1],"mTime:",mTime[1])
            return 1
        else:
            return 0

    def doRollover(self):
        """
        更新日志文件；
        在这种情况下，当发生翻滚时，日期/时间戳被附加到文件名。但是，您希望文件被命名为间隔开始，而不是当前时间。
        如果有一个备份计数，那么我们必须得到一个匹配的文件名列表，对它们进行排序，并删除具有最长后缀的列表。
        对于多进程，我们使用深拷贝(shutil.copy)而不是重命名。
        """
        if self.stream:
            self.stream.close()
        # 获得这个序列开始的时间，并使它成为一个时间表.
        # t = self.rolloverAT - self.interval
        t = int(time.time())
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        dfn = self.baseFilename + '.' + time.strftime(self.suffix, timeTuple)
        if os.path.exists(dfn):
            os.remove(dfn)
        if os.path.exists(self.baseFilename):
            shutil.copy(self.baseFilename,dfn)
            # print("%s -> %s" %(self.baseFilename, dfn))
            # os.rename(self.baseFilename,dfn)
        if self.backupCount > 0:
            # 查找最旧的日志文件并删除它
            # s = glob.glob(self.baseFilename + ".20*")
            # if len(s) > self.backupCount:
            #     s.sort()
            #     os.remove(s[0])
            for s in self.getFilesToDelete():
                os.remove(s)
        self.mode = 'w'
        self.stream = self._open()

    def emit(self, record):
        """
        发送一条记录
        将记录输出到文件中，如SE所述。对于多进程，我们使用文件锁。还有更好的方法吗？
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            FileLock = self._lock_dir + '/' + os.path.basename(self.baseFilename) + '.' + record.levelname
            f = open(FileLock,"w+")
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            FileHandler_MP.emit(self,record)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            f.close()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

logging.config.fileConfig(LOGGING_PATH) # 这个路径是log日志，的配置文件的路径
logger = logging.getLogger()