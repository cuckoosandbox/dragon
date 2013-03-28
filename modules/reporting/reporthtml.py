# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import base64
import random

from lib.dragon.common.constants import CUCKOO_ROOT
from lib.dragon.common.abstracts import Report
from lib.dragon.common.exceptions import CuckooReportError
from lib.dragon.common.objects import File

try:
    from jinja2.loaders import FileSystemLoader
    from jinja2.environment import Environment
    HAVE_JINJA2 = True
except ImportError:
    HAVE_JINJA2 = False

HAX0RS = [
    {
        "pic" : base64.b64encode(open(os.path.join(CUCKOO_ROOT, "data", "apt", "haxors", "1.jpg"), "rb").read()),
        "alias" : "C4$|-|_Y0",
        "name" : "Ouyang Yang",
        "age" : "Too old",
        "nationality" : "Chinese",
        "expertise" : "",
        "targets" : "",
        "unit" : "PLA Catering Unit",
        "loc" : "29.351944,89.311389",
    },
    {
        "pic" : base64.b64encode(open(os.path.join(CUCKOO_ROOT, "data", "apt", "haxors", "2.jpg"), "rb").read()),
        "alias" : "TattooBoy",
        "name" : "Shangguan Quan",
        "age" : "17",
        "nationality" : "Chinese",
        "expertise" : "",
        "targets" : "",
        "unit" : "PLA Soccer Team",
        "loc" : "39.7175,113.142778",
    },
    {
        "pic" : base64.b64encode(open(os.path.join(CUCKOO_ROOT, "data", "apt", "haxors", "3.jpg"), "rb").read()),
        "alias" : "HandsomeGorilla",
        "name" : "Xiahou Qie",
        "age" : "40+",
        "nationality" : "Chinese",
        "expertise" : "Exploiting Java, espionage, counter-espionage, counter-counter-espionage, counter-counter-counter-espionage, loving animals",
        "targets" : "Every industry, especially yours",
        "unit" : "PLA 34th Hackers Battalion",
        "loc" : "24.978611,113.420833",
    },
    {
        "pic" : base64.b64encode(open(os.path.join(CUCKOO_ROOT, "data", "apt", "haxors", "4.jpg"), "rb").read()),
        "alias" : "PeaceOnTheStr33ts",
        "name" : "Yuwen Bai",
        "age" : "15",
        "nationality" : "Chinese",
        "expertise" : "",
        "targets" : "",
        "unit" : "PLA Chess Club",
        "loc" : "34.559444,105.86",
    },
]

class ReportHTML(Report):
    """Stores report in HTML format."""

    def run(self, results):
        """Writes report.
        @param results: Cuckoo results dict.
        @raise CuckooReportError: if fails to write report.
        """
        if not HAVE_JINJA2:
            raise CuckooReportError("Failed to generate HTML report: Jinja2 Python library is not installed")

        shots_path = os.path.join(self.analysis_path, "shots")
        if os.path.exists(shots_path):
            shots = []
            counter = 1
            for shot_name in os.listdir(shots_path):
                if not shot_name.endswith(".jpg"):
                    continue

                shot_path = os.path.join(shots_path, shot_name)

                if os.path.getsize(shot_path) == 0:
                    continue

                shot = {}
                shot["id"] = os.path.splitext(File(shot_path).get_name())[0]
                shot["data"] = base64.b64encode(open(shot_path, "rb").read())
                shots.append(shot)

                counter += 1

            shots.sort(key=lambda shot: shot["id"])
            results["screenshots"] = shots
        else:
            results["screenshots"] = []


        #results["apt"] = random.choice(HAX0RS)
        results["apt"] = HAX0RS[2]

        env = Environment(autoescape=True)
        env.loader = FileSystemLoader(os.path.join(CUCKOO_ROOT, "data", "html"))

        try:
            tpl = env.get_template("report.html")
            html = tpl.render({"results" : results})
        except Exception as e:
            raise CuckooReportError("Failed to generate HTML report: %s" % e)
        
        try:
            report = open(os.path.join(self.reports_path, "report.html"), "w")
            report.write(html)
            report.close()
        except (TypeError, IOError) as e:
            raise CuckooReportError("Failed to write HTML report: %s" % e)

        return True
