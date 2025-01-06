"""
 Copyright (C) 2025  sophie (itsme@itssophi.ee)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import shutil
import glob
import re

class Build():
    def __init__(self):
        self._source = "./src" 
        self._destination = "./public"
        self.template_prefix = "_._"
        self.regex_placeholder = r"\{\{[^}]*\}\}"
        self.no_output = False

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, sourcee:str):
        self._source = "./" + sourcee.replace("./", "")

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destinationn:str):
        self._destination = "./" + destinationn.replace("./", "")

    def start(self):
        if not self.no_output:
            print("Building…")

        p = re.compile(self.regex_placeholder)
        
        try:
            shutil.rmtree(self.destination)
        except FileNotFoundError:
            pass #the directory isn't there yet, normal case on first use
        shutil.copytree(self.source, self.destination)

        includes = []
        for i in self._find_templates():
            if self._is_textfile(i):
                includes.append(i)
            elif os.path.isdir(i):
                for y in self._findall(i):
                    if self._is_textfile(y):
                        includes.append(y)
            else:
                raise FileNotFoundError(f"{i} isn't a text file. Or at least I am unable to read it.")
        
        file_paths_wo_includes = []
        for i in self._findall(self.destination):
            if self._is_textfile(i) and not(i in includes):
                file_paths_wo_includes.append(i)

        # first, it replaces every placholder in the files that should be filled that
        # way, then the rest. This allows faster processing for nested includes as so
        # that the same includes don't get processed twice (in a 1 level nesting).
        self._check_and_replace(includes, p)
        self._check_and_replace(file_paths_wo_includes, p)

        self._remove_includes()

        if not self.no_output:
            print("Complete")

    def _find_templates(self):
        formatted_path = self.destination + "/**/" + self.template_prefix + "*"
        return glob.glob(formatted_path, recursive=True)

    def _findall(self, directory:str):
        formatted_path = directory + "/**/*"
        return glob.glob (formatted_path, recursive = True)

    def _remove_includes (self):
        for i in self._find_templates():
            if os.path.isdir(i):
                shutil.rmtree(i)
            elif os.path.isfile(i):
                os.remove(i)
            else:
                raise FileNotFoundError(f"FATAL: {i} should have been raised as no text file before but it didn't happen.")

    def _is_textfile(self, path:str):
        if os.path.isfile(path):
            with open(path, "r") as i_file:
                try:
                    i_file.read()
                except:
                    return False
                else:
                    return True
        else:
            return False
                
    def _check_and_replace(self, paths:list[str], p:re.Pattern):
        while paths:
            path = paths[0]
            with open(path, "r") as file_r:
                file_r_before = file_r.read()
            regex_matches = p.findall(file_r_before)
            if not regex_matches:
                paths.pop(0)
            else:
                for i in regex_matches:
                    try:
                        with open(self.destination + "/" + i.replace("{", "").replace("}", "").replace("./", ""), "r") as filler:
                            with open(path, "w") as file_w:
                                file_w.write(file_r_before.replace(i, filler.read()))
                    except:
                        raise TypeError(f"{i} located in {path} isn't a valid placeholder. This mostly means that the path is wrongly formatted")
                        print(f"\033[1;31m WARN: {i} located in {path} isn't a valid placeholder. This mostly means that the path is wrongly formatted (whole file skipped)\033[00m")
                        paths.pop(0)