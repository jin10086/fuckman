import requests

from .base import logger
import re

class LaiZuWoBa:

    def __init__(self):
        self.url = "http://www.hiremeplz.com/index.php/Home/Account/login.html"
        logger.debug("")
        logger.debug("")
        logger.debug("-" * 60)
        logger.info("正在对来租我吧平台进行测试")

    def run(self, phone):
        """
        
        """
        logger.info("你测试的手机号为:{}".format(phone))
        data = {
            "phone": phone,
            "code": "8888",
        }

        logger.debug("req url:{}".format(self.url))
        logger.debug("req data:{}".format(data))
        z = requests.post(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
            },
            data=data,
        )

        logger.debug("reponse data:{}".format(z.text))
        if re.search( r'<p class="error">该用户不存在</p>', z.text) is not None:
            logger.info("恭喜你!该手机号 {} 没有注册来租我吧平台".format(phone))
        else:
            logger.info("在来租我吧平台发现你了呢:{}".format(phone))


def main():
    m = LaiZuWoBa()
    m.run("")


if __name__ == "__main__":
    main()
