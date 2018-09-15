import requests

from .base import logger


class Momo:

    def __init__(self):
        self.url = "https://web.immomo.com/sendCode"
        logger.debug("")
        logger.debug("")
        logger.debug("-" * 60)
        logger.info("正在对陌陌平台进行测试")

    def run(self, phone):
        """
        用户没有注册:{"ec":409,"em":"用户名不存在"}
        用户注册过:{"ec":200,"em":"OK","result":true}
        """
        logger.info("你测试的手机号为:{}".format(phone))
        data = {
            "momoid": phone,
            "password": "54a77e1a25e7da1a77f63ac5a9f43829",
            "imgv": "",
            "symbol": "/?rf=",
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
        logger.debug("reponse data:{}".format(z.json()))
        if z.json()["em"] == "用户名不存在":
            logger.info("恭喜你!该手机号 {} 没有注册陌陌平台".format(phone))
        else:
            logger.info("在陌陌平台发现你了呢:{}".format(phone))


def main():
    m = Momo()
    m.run("")


if __name__ == "__main__":
    main()
