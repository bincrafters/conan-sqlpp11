#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class sqlpp11Conan(ConanFile):
    name = "sqlpp11"
    version = "0.54"
    description = "A type safe embedded domain specific language for SQL queries and results in C++."
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/bincrafters/conan-sqlpp11"
    homepage = "https://github.com/rbock/sqlpp11"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD 2-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"
    requires = "date/2.4@bincrafters/stable"

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256="107e2e8ae6c37ba8db2aa1c290708ac6b651f9597c5619af6e2b84bbc5ab74e1")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_TESTS"] = False
        cmake.definitions['HinnantDate_ROOT_DIR'] = self.deps_cpp_info['date'].include_paths[0]
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()
