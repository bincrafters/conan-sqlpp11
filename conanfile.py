#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class sqlpp11Conan(ConanFile):
    name = "sqlpp11"
    version = "0.52"
    license = "BSD 2-Clause License"
    url = "https://github.com/bincrafters/conan-sqlpp11"
    description = "A type safe embedded domain specific language for SQL queries and results in C++."
    settings = "os", "compiler", "build_type", "arch"
    requires = "date/1.0.0@memsharded/testing"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/rbock/sqlpp11")
        with tools.chdir("sqlpp11"):
            self.run("git checkout %s" % self.version)

    def build(self):        
        cmake = CMake(self)
        cmake.definitions["HinnantDate_ROOT_DIR"] = self.deps_cpp_info["date"].rootpath + "/" + self.deps_cpp_info["date"].includedirs[0]
        cmake.configure(source_dir="%s/sqlpp11" % self.source_folder)
        cmake.build()
        cmake.test()
        cmake.install()
        
    def package_id(self):
        self.info.header_only()
