import datetime
import json, requests
from AI.BASE import Gen
from AI import prompts
import bs4


class AIparser:
    def __init__(self, link, element=None, language="en", log=False, important=None, timer=False):
        self.link = link
        self.element = element
        self.log = log
        self.language = language
        self.important = important
        self.timer = timer

    @staticmethod
    def json2dict(json_string: str) -> dict:
        return json.loads(json_string)

    def parse(self, element=None):
        t1 = None
        if self.timer:
            t1 = datetime.datetime.now()

        if element:
            self.element = element

        if self.log:
            print("[AIparse]   >>>   " + self.link)
            print("[Element]   >>>   " + self.element)
            print("[Status]    >>>   link parse", end="")

        ai = Gen()
        if self.language in ["ru", "en"]:
            ai.system_instructions = [{"text": eval(f"prompts.Instructions.{self.language}_instruction")}]
            if self.important:
                ai.system_instructions.append(
                    {"text": eval(f"prompts.Instructions.{self.language}_important") + self.important}
                )

        bs = bs4.BeautifulSoup(requests.get(self.link).text, "html.parser")

        if self.log:
            print("\r[status]    >>>   Element ai search", end="")

        ai.history_add("user", str({
            "source_code": str(bs),
            "parse_element": self.element
        }))

        result = ai.generate().strip()

        if self.log:
            print("\r[result]    >>>   " + result, end="\n\n")
        result = self.json2dict(result)
        result["value"] = str(result["value"])

        if self.timer and t1:
            t = datetime.datetime.now() - t1
            print("[+] Time: " + str(t.total_seconds()) + " seconds")
        return result

